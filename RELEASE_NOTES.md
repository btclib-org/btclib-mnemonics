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

- **Coming from `btclib_wallet.mnemonic`**, import the same modules
  from `btclib_mnemonics` instead. The functions answering a BIP32
  extended private key are not here: `bip39.mxprv_from_mnemonic`,
  `electrum.mxprv_from_mnemonic` and `slip39.mxprv_from_mnemonics` give
  way to the seed and the master secret they were derived from, and
  `electrum.old_master_pub_key_from_mnemonic` to the private key of
  `old_master_prv_key_from_mnemonic`. The exceptions are
  `BTClibMnemonics*`, not btclib's.
