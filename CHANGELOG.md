# Changelog

<!-- markdownlint-configure-file
  {
    // MD024/no-duplicate-heading - every release repeats the same few
    // headings, which is what keeps the page readable scrolling down it;
    // only a duplicate under the same release heading would be the
    // accident this rule looks for
    "MD024": { "siblings_only": true }
  }
-->

An entry for anything a reader would notice: what changed, and the issue
it answers. That is section 9 of [the organization standard][std], and it
is narrower than "every change" — a comment reworded inside a workflow
changes nothing a reader of this repository meets, and lands without an
entry. [RELEASE_NOTES.md](./RELEASE_NOTES.md) has the release notes,
which say what a user has to act on; this file is the record behind them.

[std]: https://github.com/btclib-org/.github

Neither file states how many entries it holds: a stated number is a line
every open branch has to edit, and the two files carry a union merge
driver that would keep both sides' numbers.

## v2026.10 (work in progress, not released yet)

### `REPOSITORY.md` records what each read-back answers

Each read-back carries what it answered on 2026-09-29, and *Read the
Docs* reads back the imported project, the site it serves and the
release `stable` points at (issue btclib-org/btclib-wallet#30).

### `RELEASING.md`'s bundle verification names the signer workflow

The `--bundle` form of *Verify the provenance of an asset* passes
`--signer-workflow "$signer"`, without which `gh attestation verify` refuses
a good release (closes btclib-org/.github#1446).

### `.clusterfuzzlite/.python-version` pins the fuzz image's interpreter

`.clusterfuzzlite/.python-version` names `3.11`, the fuzz image's interpreter,
so that the Dependency Graph's pip job there reads it rather than a root pin
Dependabot does not support yet (issue btclib-org/.github#1436).

### `RELEASING.md`'s griffe step searches `src`

`griffe check` takes `-s . -s src`, the pair `release.yml`'s `public-api`
job passes, where it answered `ModuleNotFoundError` for the previous
release (issue btclib-org/.github#1447).

### `pypi-install.yml` installs the version the release published

The install names `btclib-mnemonics==<version>` from the tag `release.yml` passes,
where a bare name let a lagging index serve the release before it
(issue btclib-org/.github#1456).

## v2026.9.29

### The repository opens

BIP39, SLIP-0039 and Electrum mnemonics, their entropy and the dispatch
telling them apart, moved out of `btclib-wallet` onto the standard
library alone (issue btclib-org/btclib-wallet#30).

### Mnemonic refusals name the parameter and quote no secret

Carried from btclib-org/btclib-wallet#134 to btclib-org/btclib-wallet#137:
a wrong type is a `BTClibMnemonicsTypeError` naming its parameter, and an
unknown word, index, checksum or padding is refused without its content.
