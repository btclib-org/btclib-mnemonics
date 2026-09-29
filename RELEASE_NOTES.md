# Release notes

Notable changes are documented here.
[CHANGELOG.md](./CHANGELOG.md) is the record behind them: this file says
what a user has to act on, that one says what changed.

Versions are *[calendar versions](https://calver.org/)*, `YYYY.M.D`: the
number says when a release was cut, and promises nothing about
compatibility, so a breaking change is announced in this file — read it
before upgrading, rather than a digit.

## v2026.10 (work in progress, not released yet)

The first release of `btclib-mnemonics`: there is no earlier version of
it to upgrade from.

Coming from `btclib_wallet.mnemonic`, import the modules from
`btclib_mnemonics` instead: `bip39`, `dispatch`, `electrum`, `entropy`,
`mnemonic` and `slip39` keep their names. What does not carry over, one
name at a time:

- **`btclib_wallet.mnemonic`'s own names** -- `WORDLISTS`, `BinStr`,
  `Entropy`, `Mnemonic`, `indexes_from_mnemonic`,
  `mnemonic_from_indexes`, `normalize_mnemonic` and the entropy
  functions it re-exported -- are not re-exported by `btclib_mnemonics`,
  whose root publishes its modules only: import each from the module
  that defines it, `mnemonic` or `entropy`.
- **`bip39.mxprv_from_mnemonic`** is not here: derive the master key
  from `bip39.seed_from_mnemonic`'s seed.
- **`electrum.mxprv_from_mnemonic`** is not here: derive the master key
  from `electrum.seed_from_mnemonic`'s seed, a function new in this
  package, as the version `electrum.version_from_mnemonic` answers asks.
- **`electrum.old_master_pub_key_from_mnemonic`** is not here: take the
  public key of `electrum.old_master_prv_key_from_mnemonic`'s private key.
- **`slip39.mxprv_from_mnemonics`** is not here: derive the master key
  from `slip39.master_secret_from_mnemonics`'s master secret.
- **`entropy.bin_str_entropy_from_bytes`** is private: pass the bytes to
  the scheme's `mnemonic_from_entropy`, which reads them.
- **`entropy.bin_str_entropy_from_entropy`** is private, for the same
  reason.
- **`entropy.bin_str_entropy_from_int`** is private, for the same reason.
- **`entropy.bin_str_entropy_from_str`** is private: pass the binary
  string itself.
- **`entropy.bin_str_entropy_from_wordlist_indexes`** is private: use
  `mnemonic.mnemonic_from_indexes` and the scheme's
  `entropy_from_mnemonic`.
- **`entropy.bytes_entropy_from_str`** is private: `int(entropy,
  2).to_bytes(len(entropy) // 8, "big")` is the conversion.
- **`entropy.wordlist_indexes_from_bin_str_entropy`** is private: use the
  scheme's `mnemonic_from_entropy` and `mnemonic.indexes_from_mnemonic`.
- **The exceptions** are `BTClibMnemonicsException`,
  `BTClibMnemonicsTypeError` and `BTClibMnemonicsValueError`, not
  btclib's; each of the last two is also a `TypeError` or a `ValueError`.
