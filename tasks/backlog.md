# Backlog: temporary tag-listing renderer

Work breakdown for [spec.md](spec.md). Nothing here is started.

**Blocked on:** answers to spec §5 (five open questions). B1 and B2 can proceed regardless;
everything else depends on Q1 and Q4.

---

## B0 — Decide the open questions

Spec §5. My recommendations, all "match production / fail loudly":

| # | Question | Recommendation |
|---|---|---|
| 1 | Icons for the 14 unmapped tags | Render plain, as production does |
| 2 | `Graph-Insights` vs `GraphInsights` duplicate | Out of scope; separate content fix |
| 3 | `Load Balancer` mapping missing from `HEAD` | Restore the two `mkdocs.yml` lines |
| 4 | Marker present but unrenderable | Fail the build |
| 5 | `/tags/` size (45 sections, 531 refs) | Include everything |

**Output:** decisions recorded in the spec. **Est:** one review pass.

---

## B1 — Tag index builder

Walk `docs/**/*.md`, parse front matter, build `{tag: [(title, src_path)]}`.

- title = front-matter `title:`, else first body `# ` heading, else skip with a warning
- skip pages with no `tags:`
- tolerate malformed YAML without crashing the build
- pure function over `docs/`, no `site/` knowledge — keeps it unit-testable

**Verify:** 531 tagged pages, 45 distinct tags, `TransformOperator` = 237.
**Est:** small. **Depends on:** nothing.

---

## B2 — Marker parser

Recognise both forms in built HTML and extract the filter:

```
<!-- material/tags -->                                  -> no filter
<!-- material/tags { include: [BeginnersTutorial] } -->  -> include=[BeginnersTutorial]
```

The argument is YAML-ish but not valid YAML (unquoted `[X]` inside braces parses fine, but
do not assume). Parse defensively; an unrecognised argument is an error, not a silent
no-filter.

**Verify:** finds exactly 4 markers across 2 files in the current build.
**Est:** small. **Depends on:** nothing.

---

## B3 — HTML renderer

Emit the markup in spec §3 for one listing.

- anchor id `tag:` + lowercase, spaces → hyphens
- chip class from `extra.tags`; bare `md-tag` when unmapped (pending Q1)
- relative href from the listing page to each target
- escape titles
- ordering per spec §3

**Verify:** byte-compare one rendered block against the production sample in the spec.
**Est:** medium — the relative-URL computation is the fiddly part.
**Depends on:** B1, B2, Q1.

---

## B4 — `tools/render_tag_listings.py`

Wire B1–B3 into a CLI matching `localize_bundle_assets.py`'s shape: takes `[site_dir]`,
prints `[OK]` lines per marker, exits non-zero with a problem list.

- reads `mkdocs.yml` for `extra.tags` and the two `listings_*_sort_by` settings
- idempotent: re-running on an already-rendered `site/` is a no-op, not an error
  (`localize_bundle_assets.py` needed this and it was easy to get wrong)
- fails if any marker remains after processing

**Verify:** `python tools/render_tag_listings.py site` twice in a row, second run clean.
**Est:** small once B1–B3 exist. **Depends on:** B1, B2, B3, Q4.

---

## B5 — Wire into the build

Add to `build` in `Taskfile.yml`, after `zensical build --strict` and alongside
`localize_bundle_assets.py`. Order relative to the localizer does not matter — they touch
disjoint files — but keep the localizer first so the more security-relevant step runs
regardless.

**Verify:** `task clean build` renders listings; `task check` still passes.
**Est:** trivial. **Depends on:** B4.

---

## B6 — Promote the guard

In `check_zensical_output.py`, `tag-listings` currently sits in PENDING and reports
unexpanded markers. Once we render them ourselves it becomes a feature we own, so it
belongs in REQUIRED — same reasoning as redirects and comments.

Keep a separate PENDING probe for "Zensical started doing this itself", so the removal
signal in spec §6 still fires. Distinguishing the two is the fiddly bit: our own output and
Zensical's would both look like a populated listing. Suggest keying the PENDING probe on a
marker being *already expanded before* our script runs.

**Verify:** deliberately skip the render step; `task check` must fail.
**Est:** medium — mostly deciding the probe. **Depends on:** B4, B5.

---

## B7 — Tests

`tests/test_render_tag_listings.py`, following `tests/test_update_di_reference.py`.

- title resolution: front matter wins over H1; H1 fallback; neither → warn
- slugification: `Load Balancer` → `tag:load-balancer`
- sort orders: casefold for tags, title for items, marker order for `include:`
- unmapped tag → no `md-tag-icon` class
- marker parsing: both forms, plus a malformed one
- relative hrefs from different depths

**Verify:** `task test:unit` stays green.
**Est:** medium. **Depends on:** B1–B4.

---

## B8 — Documentation

Extend the README section added during the migration. It currently lists tag listings among
the three missing features; that becomes "reimplemented locally, tracked for removal",
leaving social cards and revision dates as the genuinely-missing two.

**Est:** trivial. **Depends on:** B5.

---

## Sequencing

```
B0 ─┬─> B1 ─┬─> B3 ──> B4 ──> B5 ──> B6 ──> B8
    └─> B2 ─┘                  └──> B7
```

B1 and B2 are independent and can start as soon as Q1/Q4 are settled.

## Risks

- **Relative URL computation** is where this most likely breaks — mike serves the site under
  `/latest/` and `/26.2/`, so anything absolute fails silently in one context. Acceptance
  requires resolving every generated link against `site/` on disk.
- **`/tags/` is large.** 531 references in one page. Watch build time; if it becomes
  noticeable, that is an argument for revisiting Q5.
- **Divergence from production markup.** We match it today, but a Material update could
  change the markup and this becomes a slow drift. Mitigated by the whole thing being
  temporary and by the spec pinning a production sample.
- **The removal signal is the weak point** (B6). If it never fires, this "temporary" script
  becomes permanent. Worth a calendar reminder to re-check backlog #38 rather than relying
  only on the probe.
