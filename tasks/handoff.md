# Handoff: finishing the Zensical migration

**Repository:** `eccenca/documentation.eccenca.com`
**Branch:** `feature/zensical`
**Goal:** make `feature/zensical` mergeable into `main` without silently losing documentation features.

---

## 1. Context

The repo is migrating from Material for MkDocs (private Insiders fork, pinned at
`9.6.14-insiders-4.53.16`) to [Zensical](https://zensical.org). Material for MkDocs is in
maintenance mode; `9.7.0` was the final feature release and made all former Insiders
features public.

The `feature/zensical` branch already contains the hardest piece of work: `tools/build_nav.py`
generates a 571-line `nav.yml` from the 53 `docs/**/.pages` files, wired in via
`INHERIT: nav.yml`. This works correctly and is not to be changed.

**The problem this handoff addresses:** Zensical silently ignores MkDocs plugins it has not
implemented. `zensical build --strict` reports `No issues found` while six features vanish from
the output. CI is green, the deploy succeeds, and the published site is missing functionality.
Nothing in the current setup would catch this.

---

## 2. Verified baseline

Measured on `feature/zensical` with `zensical 0.0.55` (branch pins `^0.0.44`):

```
Build finished in 25.33s   (cold)
Build finished in  5.00s   (warm)
No issues found            (also with --strict)
559/559 markdown files rendered, no orphaned pages, 404.html present
```

Inspecting the generated `site/` directory:

| Plugin in `mkdocs.yml` | Actual effect on output |
|---|---|
| `glightbox` | Works natively — active on 98 pages |
| `privacy` (`assets_fetch: true`) | **Not applied.** `fonts.googleapis.com`, `fonts.gstatic.com` and `unpkg.com` are requested directly from the browser on all 560 pages. No `assets/externals/` directory is produced. |
| `social` (`cards: true`) | **Not applied.** Zero `og:image` tags in the entire site. |
| `tags` (listings) | **Partially applied.** Tags render, but listings do not: `site/tags/index.html` has a 2-word article body, and `site/tutorials/index.html` lost its entire generated tutorial list (3 `<!-- material/tags -->` markers produce nothing). |
| `redirects` | **Not applied.** `/cmemc/` and `/explore-and-author/building-a-customized-user-interface/` return 404. |
| `meta` (`docs/.meta.yml` → `comments: true`) | **Not applied.** Giscus appears on 0 of 560 pages. |
| `git-revision-date-localized` | **Not applied.** No "Last update" on any page. |
| `autolinks` | Irrelevant — see T6. |

Reproduce:

```bash
git checkout feature/zensical
pip install zensical            # pulls mkdocs-material 9.7.6 + mkdocs 1.6.1 transitively
zensical build --strict
python tools/check_zensical_output.py site
```

---

## 3. Ground rules

- **Do not touch** `tools/build_nav.py`, `nav.yml`, or the `docs/**/.pages` files. The `.pages`
  files remain the source of truth for navigation; `nav.yml` is generated from them.
- **Do not delete** `docs/**/.pages` even though `awesome-pages` is gone — `build_nav.py` reads them.
- **Do not** attempt to reimplement social cards, tag listings, or revision dates. Those are
  deferred (section 5).
- Every task below has a machine-checkable acceptance criterion via
  `tools/check_zensical_output.py`. A task is not done until that script says so.
- Keep commits scoped to one task each.

---

## 4. Tasks

### T1 — Rebase onto `main` (do this first)

The branch was forked before several changes landed on `main` and would silently revert them.

Missing from `feature/zensical` relative to `main`:

- `pyproject.toml`: `pytest = "^9.1.1"` dev dependency and the `[tool.pytest.ini_options]` block
  with the `integration` marker
- `Taskfile.yml`: the `test`, `test:unit` and `test:integration` tasks; the `rumdl ... check --fix
  docs/build/integrations/index.md` command
- `.github/workflows/test.yml`: the `test` step running `task test:unit`
- `.markdownlint.jsonc`: the `"key"`, `"name"`, `"param"` entries
- `overrides/.icons/eccenca/module-marketplace.svg`
- Updates to `data/integrations.yml`, `data/plugins.json`, `tools/update_di_reference.py`,
  `tools/templates/plugin.md`, `tests/test_update_di_reference.py`

**Acceptance:** `task test:unit` exists and passes; `git diff main -- .markdownlint.jsonc
tests/ data/` shows no unintended reversions.

---

### T2 — Remove the Material for MkDocs Insiders dependency

`zensical` already depends on the **public** `mkdocs-material 9.7.6` and `mkdocs 1.6.1` for its
compatibility layer. The branch still pins the private Insiders fork, which overrides that with an
older version and keeps a deploy-time secret in CI for no reason.

1. `pyproject.toml`: delete the `mkdocs-material = {git = "git@github.com:eccenca/mkdocs-material-insiders.git", ...}` line.
2. `Taskfile.yml`: delete the `use:public`, `use:insider-ssh` and `use:insider-https-token` tasks
   and the `MATERIAL_TAG` / `MATERIAL_INSIDER_TAG` variables.
3. `.github/workflows/pages.yml`: delete the `reconfigure private repository access` step and stop
   passing `secrets.ACCESS_TOKEN`.
4. Also drop `Pillow` and `CairoSVG` — they exist only for social-card rendering and are used
   nowhere in `tools/` or `tests/`. Re-add them when social cards return (see section 5). If you
   drop them, also remove the `libcairo2-dev libfreetype6-dev libjpeg-dev libpng-dev` apt step from
   `pages.yml`.
5. `poetry lock` and commit the lockfile.

**Acceptance:** a clean `poetry install` succeeds with no SSH key and no `ACCESS_TOKEN`; the build
still produces 559 pages.

---

### T3 — Pin Zensical explicitly and bump

`zensical = "^0.0.44"` resolves under Poetry to `>=0.0.44,<0.0.45`, i.e. hard-pinned to 0.0.44
while 0.0.57 is current. That determinism is correct for a 0.0.x dependency, but the pin should be
deliberate and current.

Bump to the latest released 0.0.x, run the full build, and confirm page count and check-script
output are unchanged. Add a short comment in `pyproject.toml` explaining that the caret pin is
intentionally narrow and must be bumped manually.

**Acceptance:** `zensical --version` in CI matches the pin; build output is byte-comparable in page
count to the baseline.

---

### T4 — Self-host web fonts (highest priority)

**This is the most serious regression.** `theme.font: {text: Roboto, code: Roboto Mono}` causes
every one of the 560 pages to request `fonts.googleapis.com` and `fonts.gstatic.com` directly.
The `privacy` plugin used to localise these; it no longer runs. For a German company publishing a
site with an Imprint link, third-party font loading is a known legal exposure, not a cosmetic
issue.

1. Verify the regression against production first: confirm that
   `https://documentation.eccenca.com/` currently serves fonts from its own origin.
2. Download the Roboto and Roboto Mono WOFF2 subsets actually used and commit them under
   `docs/assets/fonts/`.
3. Set `theme.font: false` in `mkdocs.yml` to stop Zensical emitting the Google Fonts link tags.
4. Add the corresponding `@font-face` declarations to `docs/assets/extra.css`, matching the
   weights currently in use, with `font-display: swap`.

**Acceptance:** `check_zensical_output.py` reports no `fonts.googleapis.com` or `fonts.gstatic.com`
under `external-assets`, and the rendered site is visually unchanged.

---

### T5 — Vendor tablesort

`extra_javascript` loads `https://unpkg.com/tablesort@5.3.0/dist/tablesort.min.js` on all 560
pages. Same root cause as T4.

Commit `tablesort@5.3.0` to `docs/assets/tablesort.min.js` and change `extra_javascript` to the
local path. Leave the existing `assets/tablesort.js` initialiser as-is; only the CDN entry changes.

**Acceptance:** no `unpkg.com` under `external-assets`; sortable tables still sort.

---

### T6 — Replace `redirects`, `meta`, and remove `autolinks`

**`redirects`** — two mappings from `mkdocs.yml`:

| Old URL | Target |
|---|---|
| `/cmemc/` | `/automate/cmemc-command-line-interface/` |
| `/explore-and-author/building-a-customized-user-interface/` | `/explore-and-author/graph-exploration/building-a-customized-user-interface/` |

Create static `index.html` stubs at those paths under `docs/` (Zensical copies non-markdown files
verbatim into `site/`). Each stub needs a `<meta http-equiv="refresh">`, a `<link rel="canonical">`
to the target, and a plain visible link as a no-JS fallback. Verify the stubs are not picked up
into the navigation.

**`meta`** — `docs/.meta.yml` only sets `comments: true` globally. Replace it by inverting the
condition in `overrides/partials/comments.html`: comments render by default, and only the three
pages carrying explicit `comments: false` front matter opt out (`docs/index.md`,
`docs/getting-started/with-your-sandbox/index.md`,
`docs/getting-started/with-your-sandbox/material.md`). Note the template is rendered by MiniJinja,
not Jinja2 — verify whichever `is undefined` / default-value construct you pick actually works in
the build rather than assuming Jinja2 semantics.

**`autolinks`** — safe to delete outright. I checked all 1,220 markdown links in `docs/`: 284 are
bare filenames, and all 284 resolve relative to their own directory. The plugin was a no-op.

Then clean `mkdocs.yml`: remove the `privacy`, `redirects`, `meta` and `autolinks` plugin entries,
since we now implement those ourselves and leaving them in risks double behaviour when Zensical
implements them later. **Leave `social`, `tags` and `git-revision-date-localized` in place** — they
are inert today and will start working automatically once Zensical maps them.

While in `mkdocs.yml`, also drop the redundant `codehilite` markdown extension (superseded by
`pymdownx.highlight`) and the dead MkDocs-only options `include_search_page`, `search_index_only`
and `static_templates`.

**Acceptance:** `redirects`, `comments-default-on` and `comments-opt-out` all pass in the check
script.

---

### T7 — Restore the Load Balancer tag icon

`simple-awselasticloadbalancing` is commented out in both the `extra.tags` map and `theme.icon.tag`
on this branch. The icon is absent from the current Simple Icons set shipped by both Zensical and
Material 9.7.6 — this is an upstream Simple Icons removal, not a Zensical gap.

Add a replacement SVG under `overrides/.icons/eccenca/` and re-enable the `"Load Balancer"` tag
mapping, so the tag stops rendering without an icon.

**Acceptance:** the `Load Balancer` tag renders with an icon; no commented-out mappings remain.

---

### T8 — Wire in the guard rails

Two automated guards, both added to `task check` and to `.github/workflows/test.yml`:

**a) Output parity check.** `tools/check_zensical_output.py` (provided alongside this handoff — copy
it into `tools/`) inspects the built `site/` and fails on regressions in the features we own. It
also reports the three deferred features as `PEND`, and prints a loud banner when one of them
starts passing. That banner is the signal to revisit the migration. Run it after `task build`.

**b) Navigation drift check.** Nothing currently guarantees `nav.yml` matches the `.pages` files.
Add a task that regenerates `nav.yml` into a temporary file and diffs it against the committed one,
failing on any difference. Consider adding it to `.pre-commit-config.yaml` as well.

**Acceptance:** `task check` fails if any `.pages` file is edited without regenerating `nav.yml`,
and fails if any T4–T6 regression is reintroduced.

---

## 5. Deferred — do not implement

These are genuine Zensical gaps with open backlog issues. They are the reason this migration is
not finished, and they must be visible to whoever decides on the merge:

| Feature | Zensical backlog | Impact if merged today |
|---|---|---|
| Social cards | [#37](https://github.com/zensical/backlog/issues/37) (Tier 2) | No `og:image` anywhere — link previews break in Slack, LinkedIn, X for the whole documentation |
| Tag listings | [#38](https://github.com/zensical/backlog/issues/38) (Tier 1) | `/tags/` and `/tutorials/` become near-empty landing pages |
| Revision dates | [#18](https://github.com/zensical/backlog/issues/18) (Tier 2) | "Last update" disappears site-wide |

The check script tracks all three. When any starts passing, remove it from the `PENDING` set and
re-evaluate.

---

## 6. Definition of done

- [ ] `task test:unit` passes (T1)
- [ ] `poetry install` needs no SSH key and no `ACCESS_TOKEN` (T2)
- [ ] `zensical build --strict` reports no issues and renders 559 pages
- [ ] `python tools/check_zensical_output.py site` exits 0
- [ ] Navigation drift check passes
- [ ] The three deferred items are reported as `PEND`, not silently absent
- [ ] A short note in `README.md` states that the site is built with Zensical and that three
      Material features are pending, linking to this document

**Merge decision is not part of this task.** Deliver the branch in the state above and surface the
three deferred items; the call on whether that trade is acceptable belongs to the repository owners.
