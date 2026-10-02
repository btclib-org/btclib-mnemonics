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

## v2026.11 (work in progress, not released yet)

### `CONTRIBUTING.md` says the maintainer self-merges while the bot review is off

*The review* says no ack of record exists while `claude-review.yml` is off,
and that a local review of a named sha, by a reviewer other than the author,
stands in (issue btclib-org/.github#1527).

### `SECURITY.md` says where randomness comes from

`SECURITY.md` names `os.urandom` beside `secrets`, and says a weak
`entropy_source` a caller passes to `slip39.mnemonics_from_master_secret`
is the caller's (issue #24).

### `CONTRIBUTING.md` lists the jobs that do not pass `--locked`

`CONTRIBUTING.md` lists the jobs that install without `--locked`, and the
comments that said every job passes it no longer do
(btclib-org/btclib#2440, issue #25).

### The verification command pins the tag for every signer

SECURITY.md and RELEASING.md said a `reusable-attest.yml` release took no
`--source-ref`; it takes the tag (issue #25, btclib-org/btclib#2447).

### The weekly vendored-vectors check compares the vendored bytes

`check_vendored_vectors.py` holds each vendored file to the ledger's `ours`,
or `blob` where there is none, and `blob` to upstream's at the pinned commit;
a mismatch fails the run (btclib-org/btclib#2439, issue #25).

## v2026.10.2

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

### `pypi-install.yml` retries the install of the version the release published

Each install cell retries `pip install btclib-mnemonics==<version>` until a
deadline, while the index does not serve it, where a cell whose edge held the
previous page failed after the wait (issue btclib-org/.github#1458).

### The OpenSSF Baseline badge

`README.md`'s badge row ends with the OpenSSF Baseline badge, beside the
Best Practices badge, section 2 of the organization standard admitting it
on the same property (issue btclib-org/.github#1460).

### `pypi-install.yml` runs its install through `install_published_release.py`

The retry the entry `pypi-install.yml` retries the install of the version the
release published describes now runs as btclib-org/.github's
`install_published_release.py` (issue btclib-org/.github#1458).

### The release's attestation bundle is attached as `*.intoto.jsonl`

`RELEASING.md`'s verification and recovery commands name the bundle
`<tag>.intoto.jsonl`, the name `reusable-github-release.yml` attaches it under
(issue btclib-org/.github#1468).

### `codeql.yml`'s aggregate runs `check_run_jobs.py`

The aggregate's step runs `check_run_jobs.py`, which reads the run's jobs
listing again up to a deadline while a row of `analyze` is unfinished
(issue btclib-org/.github#1463).

### `generate_sbom.py` carries a not-affected list into the bill of materials

`generate_sbom.py` reads `.github/vex.toml`, where the tree lists the
vulnerabilities its release is not affected by, into the document's
`vulnerabilities`; no list, no key (issue btclib-org/.github#1469).

### `SECURITY.md` promises a response time

`SECURITY.md` says a report is acknowledged within 7 days, and a fix or a
published advisory within 90 (issue btclib-org/.github#1460).

### `WordLists.load_lang` honours a replacement file

Given a file for a registered language, `load_lang` loads that file and
records it, where it silently kept the registered word-list (closes #21).

### `release.yml` audits the lock before it publishes

The `audit` job calls btclib-org/.github's `reusable-audit.yml`, which runs
`uv audit` over what the wheel declares, and both publish jobs wait for its
success (issue btclib-org/.github#1466).

### `generate_sbom.py` is btclib-org/.github's

The `dist` job writes the bill of materials with btclib-org/.github's
`generate_sbom.py`, served from `main`, and the tree keeps no copy of it
(issue btclib-org/.github#1478).

### `CLAUDE.md` carries the shared primary-checkout section

The shared section *The primary checkout is the maintainer's* replaces this
tree's, *Model* names only the model, and the draft-pull-request bullet names
`codeql: every job passed` too (issue btclib-org/.github#1494).

### `Dependency review` is a required check

- **`REPOSITORY.md` reads `lint / Dependency review` back with the other
  required checks** (issue btclib-org/.github#1465).

### `[tool.uv] required-version` is `>=0.12.18`

- **`required-version` reads `>=0.12.18`, not `>=0.12.19`** (issue
  btclib-org/.github#1482): the Dependabot service refused `0.12.19` with
  `tool_version_not_supported`.

### `SECURITY.md` names the latest security review

`SECURITY.md` gives the date of the latest security review and links the issue
that records it (issue btclib-org/.github#1362).

### BIP39 refuses 512-bit entropy and 48-word mnemonics

A 512-bit entropy or a 48-word mnemonic is refused, which breaks callers
that pass either (closes #16). A word count outside 12, 15, 18, 21 and 24
is refused before any word is decoded (closes #20).

### Entropy longer than the largest size is refused, not truncated

This holds in every scheme, Electrum's included, which breaks callers that
pass more (closes #15). Dice rolls and the CSPRNG keep the leftmost bits
at their own width, leading zeros included, so their first bit is unbiased.

### SLIP-0039 secrets are 16 to 64 bytes and mnemonics 20 to 59 words

Longer ones are refused, before any word is decoded for a mnemonic, which
breaks callers that pass them (closes #19).

### Every refusal is one of the two exceptions, and none quotes an unknown name

A lone surrogate, an unreadable word-list file and a bad `WordLists` or
`wordlists` argument are refused as the two exceptions. No refusal quotes an
unknown `lang` or `mnemonic_type` (closes #17, closes #18, closes #22).

### The fuzz harness calls every decoder `tests/fuzz_test.py` lists

`fuzz/fuzz_mnemonics.py` calls each decoder in `DECODERS`, a test holds the
two together, and recombination is driven with valid shares (closes #23).

### A `Signed-off-by:` trailer on every commit of a pull request

*Pull requests* says every commit of a pull request carries a
`Signed-off-by:` trailer, and how to add it (issue
btclib-org/.github#1467).

### The primary-checkout section uses one form for the checkout

- **The section writes the checkout as `"${checkout:?}"` throughout, says
  what `<scratchpad>` is and names the pull** (issue
  btclib-org/.github#1500).

### The `python` inventory has a copy kept in the tree

`docs/source/_inventories/python.inv` is read when `docs.python.org` fails,
so an outage of that site no longer fails the `-n -W` docs build (issue
btclib-org/.github#1508).

### The release's attestation is signed by `reusable-build.yml`, at SLSA Build L3

`release.yml` calls `reusable-build.yml`, which signs the files before the
publish jobs wait for approval (issue btclib-org/.github#1506).

## v2026.9.29

### The repository opens

BIP39, SLIP-0039 and Electrum mnemonics, their entropy and the dispatch
telling them apart, moved out of `btclib-wallet` onto the standard
library alone (issue btclib-org/btclib-wallet#30).

### Mnemonic refusals name the parameter and quote no secret

Carried from btclib-org/btclib-wallet#134 to btclib-org/btclib-wallet#137:
a wrong type is a `BTClibMnemonicsTypeError` naming its parameter, and an
unknown word, index, checksum or padding is refused without its content.
