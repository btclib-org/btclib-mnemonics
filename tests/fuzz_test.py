# Copyright (c) The btclib developers
# Distributed under the MIT software license, see the accompanying
# LICENSE file or https://opensource.org/license/mit for the full text.

"""Every decoder, on input nobody wrote down.

The rest of the suite is fixed vectors: exactly what conformance needs,
and blind to the malformed sentences that never make it into a
specification's test section. This file is the converse. It does not
assert that a decoder accepts the right things -- the vectors do that --
but that it *fails the way the package says it fails*, whatever it is
handed: an IndexError off a short slice or a KeyError off a word-list
lookup reaches a caller who catches `BTClibMnemonicsValueError` to reject
bad input and has no reason to expect anything else.

`fuzz/`'s atheris harness asks the same question of the same decoders
for an hour a week; this asks it on every run, for as long as hypothesis
spends on a test. Arbitrary text rarely spells a word, so the sentences
below are also drawn from the word-lists themselves, which is what
reaches the checksum, the padding and the header fields behind the
lookup.
"""

from __future__ import annotations

import contextlib
from collections.abc import Callable
from typing import Any

import pytest
from hypothesis import given
from hypothesis import strategies as st

from btclib_mnemonics import bip39, dispatch, electrum, slip39
from btclib_mnemonics.exceptions import (
    BTClibMnemonicsTypeError,
    BTClibMnemonicsValueError,
)
from btclib_mnemonics.mnemonic import WORDLISTS

# what a decoder of this package is allowed to raise. Anything else
# leaves the contract src/btclib_mnemonics/exceptions.py documents
CONTRACT = (BTClibMnemonicsValueError, BTClibMnemonicsTypeError)

DECODERS: dict[str, Callable[[str], Any]] = {
    "bip39.entropy_from_mnemonic": bip39.entropy_from_mnemonic,
    "bip39.lang_from_mnemonic": bip39.lang_from_mnemonic,
    "electrum.version_from_mnemonic": electrum.version_from_mnemonic,
    "electrum.entropy_from_mnemonic": electrum.entropy_from_mnemonic,
    "electrum.lang_from_mnemonic": electrum.lang_from_mnemonic,
    "electrum.hex_seed_from_old_mnemonic": electrum.hex_seed_from_old_mnemonic,
    "slip39.share_from_mnemonic": slip39.share_from_mnemonic,
}


def _sentences(lang: str, min_size: int, max_size: int) -> st.SearchStrategy[str]:
    """Return a strategy for sentences of words from one word-list."""
    words = st.sampled_from(list(WORDLISTS.wordlist(lang)))
    return st.lists(words, min_size=min_size, max_size=max_size).map(" ".join)


def _read(decoder: Callable[[str], Any], sentence: str) -> None:
    with contextlib.suppress(*CONTRACT):
        decoder(sentence)


@pytest.mark.parametrize("name", DECODERS)
@given(text=st.text(max_size=256))
def test_a_decoder_refuses_text_within_the_contract(name: str, text: str) -> None:
    """Arbitrary text is read, or refused as the package's own exception."""
    _read(DECODERS[name], text)


@pytest.mark.parametrize("name", DECODERS)
@given(sentence=_sentences("en", 0, 25))
def test_a_decoder_refuses_english_words_within_the_contract(
    name: str, sentence: str
) -> None:
    """Sentences of BIP39 words reach the checksum and the version."""
    _read(DECODERS[name], sentence)


@given(sentence=_sentences("slip39", 0, 40))
def test_a_share_is_read_within_the_contract(sentence: str) -> None:
    """Sentences of SLIP-0039 words reach the header and the checksum."""
    _read(slip39.share_from_mnemonic, sentence)


_FIELD = st.integers(min_value=0, max_value=15)
_COUNT = st.integers(min_value=1, max_value=16)


@st.composite
def _shares(draw: st.DrawFn) -> slip39.Share:
    """Return a share whose every field is within what the format holds."""
    group_count = draw(_COUNT)
    n_bytes = 2 * draw(st.integers(min_value=8, max_value=24))
    return slip39.Share(
        identifier=draw(st.integers(min_value=0, max_value=(1 << 15) - 1)),
        extendable=draw(st.booleans()),
        iteration_exponent=draw(_FIELD),
        group_index=draw(_FIELD),
        group_threshold=draw(st.integers(min_value=1, max_value=group_count)),
        group_count=group_count,
        member_index=draw(_FIELD),
        member_threshold=draw(_COUNT),
        value=draw(st.binary(min_size=n_bytes, max_size=n_bytes)),
    )


@given(share=_shares())
def test_a_share_encodes_and_decodes_back(share: slip39.Share) -> None:
    """The decoder is the encoder's inverse over every field it holds.

    Random words almost never carry a valid checksum, so the round trip
    is driven from the share rather than from the sentence.
    """
    mnemonic = slip39.mnemonic_from_share(share)
    assert slip39.share_from_mnemonic(mnemonic) == share


@given(text=st.text(max_size=128))
def test_dispatch_answers_every_text(text: str) -> None:
    """Dispatch refuses nothing that is a str: it answers "" instead."""
    seed_types = dispatch.all_seed_types_from_mnemonic(text)
    assert dispatch.seed_type_from_mnemonic(text) == (
        seed_types[0] if seed_types else ""
    )
