# Spec: temporary tag-listing renderer

**Status:** accepted 2026-08-23, fully implemented §1-§9, **removed 2026-09-03**.
Zensical 0.0.58 ships native `tags` listings and populates `tag.url` itself; the
"Removal" steps below were carried out as part of the 0.0.57 -> 0.0.58 bump.
**Replaced:** Material's `tags` plugin listings, which Zensical did not implement
([zensical/backlog#38](https://github.com/zensical/backlog/issues/38)).
**Lifetime:** delete the moment Zensical ships listings. See "Removal" below.

---

## 1. Problem

`tools/check_zensical_output.py` reports this every build:

```
[PEND] tag-listings: /tags/ article has 3 words, 4 unexpanded
       <!-- material/tags --> marker(s) on 2 page(s) (backlog #38)
```

Per-page tag *chips* work — Zensical renders them, and the icon CSS with them. What is
missing is the *listings*: the generated index of which pages carry which tag.

Two pages are affected, carrying four markers between them:

| Page | Marker | Renders today |
|---|---|---|
| `docs/tags.md` | `<!-- material/tags -->` | nothing — page body is just its title |
| `docs/tutorials/index.md` | `<!-- material/tags { include: [BeginnersTutorial] } -->` | nothing |
| `docs/tutorials/index.md` | `<!-- material/tags { include: [AdvancedTutorial] } -->` | nothing |
| `docs/tutorials/index.md` | `<!-- material/tags { include: [ExpertTutorial] } -->` | nothing |

`/tutorials/` is the more visible loss: it is a landing page whose entire purpose is the
generated list, and it currently shows an intro paragraph followed by blank space.

## 2. Approach

**Post-build HTML injection**, mirroring the existing `tools/localize_bundle_assets.py`.

Zensical passes the markers through to the output verbatim as HTML comments:

```html
<!-- material/tags -->
<!-- material/tags { include: [BeginnersTutorial] } -->
```

so they are addressable in `site/**/*.html` after the build. A script walks the corpus for
tag front matter, renders the listing HTML, and substitutes it for each marker.

### Why this shape

- **Sources stay untouched.** The pages keep Material's own marker syntax, so when
  Zensical implements listings they light up natively and this script is deleted. No
  migration back.
- **Precedent in-tree.** `localize_bundle_assets.py` already post-processes `site/` inside
  `task build`, with the same "assert loudly if the expected pattern is missing" contract.
- **No new dependencies, no template overrides.** Icon styling already works (below).

### Alternatives rejected

| Option | Why not |
|---|---|
| Pre-build: expand markers into `docs/*.md` | Mutates tracked sources; dirty tree after every build |
| Generate a partial + `--8<--` snippets include | Requires editing both pages away from Material syntax, then back later; needs two-phase build |
| Override a Zensical template | Zensical has no listings template to override — the feature is absent, not broken |
| Write a Zensical plugin | Zensical has no plugin API |

## 3. Output contract

Reproduce production's markup exactly. Sample from
`https://documentation.eccenca.com/latest/tutorials/`:

```html
<h2 id="tag:beginnerstutorial">
<span class="md-tag md-tag-icon md-tag--beginners">BeginnersTutorial</span><a class="headerlink" href="#tag:beginnerstutorial" title="Permanent link">¤</a></h2>
<ul>
  <li>
    <a href="../build/active-learning/">
      Active Learning of Linking Rules
    </a>
  </li>
</ul>
```

### Rules, all verified against production

**Anchor id** — `tag:` + tag lowercased with spaces replaced by hyphens.
`Load Balancer` → `tag:load-balancer`, `Graph-Insights` → `tag:graph-insights`.

**Tag chip class** — `md-tag md-tag-icon md-tag--<key>` where `<key>` is
`extra.tags[<tag>]` from `mkdocs.yml`. **Zensical already emits the backing CSS**
(`.md-tag.md-tag--beginners{--md-tag-icon:url(...)}`) on every page, so no CSS work is
needed. For tags absent from `extra.tags`, production omits `md-tag-icon` and the
`md-tag--<key>` modifier, emitting a bare `<span class="md-tag">`. 14 of the 45 tags in
use are unmapped — see §5.

**Item title** — front-matter `title:` if present, otherwise the first `# ` heading in the
body. Verified on three pages; none of the sampled pages set `title:`, and all three
listing titles match their H1 exactly.

**Item link** — relative from the listing page to the target, so it survives mike's
versioned `/latest/`, `/26.2/` prefixes. Never absolute.

**Ordering** — from `mkdocs.yml`:
- tags within an un-filtered listing: casefolded tag name
  (`listings_tags_sort_by: tag_name_casefold`) — confirmed, `/tags/` runs
  AdvancedTutorial, API, Application View, Automate, BeginnersTutorial…
- items within a tag: page title (`listings_sort_by: item_title`)
- markers with `include:` render in **marker order**, not sorted — `/tutorials/` shows
  Beginners, Advanced, Expert, matching source order

**Scope** — a bare `<!-- material/tags -->` lists every tag in use (45 on `/tags/`). An
`include: [X]` marker lists only tag X.

**Self-inclusion** — not an issue: neither `tags.md` nor `tutorials/index.md` carries tag
front matter, so neither can appear in its own listing. Guard anyway.

## 4. Corpus facts

- 531 of 581 pages carry `tags:` front matter
- 45 distinct tags; largest is `TransformOperator` (237 pages), then `WorkflowTask` (77),
  `PythonPlugin` (61), `cmemc` (47)
- The `/tags/` listing is therefore large — production's is ~2100 words

## 5. Open questions — resolved

1. **Unmapped tags.** 14 tags in use have no `extra.tags` icon: `Build`, `Dataset`,
   `DistanceMeasure`, `EvaluateTemplate`, `Explainer`, `Files`, `Graph-Insights`,
   `GraphInsights`, `Introduction`, `LinkRules`, `Load Balancer`, `Plugin`,
   `TransformOperator`, `WorkflowTask`. Match production (render plain, no icon), or take
   the opportunity to map them? **Recommend: match production**, keep this change
   behaviour-neutral. -> decision: match production, no icon

2. **`Graph-Insights` vs `GraphInsights`** are both in use and look like an accidental
   split — 2 tags where 1 was meant. Out of scope for this task, but the listing will make
   it visible on `/tags/`. Worth a separate content fix.  -> decision: separate fix

3. **`Load Balancer` icon.** The T7 work added `overrides/.icons/other/load-balancer.svg`
   (committed, tracked) but the two `mkdocs.yml` lines that reference it are **not** in
   `HEAD` — line 63 still reads `# "Load Balancer": simple-awselasticloadbalancing`. The
   icon file is currently dead weight and the tag renders bare. Probably an accidental
   partial revert. Restore those two lines, or drop the SVG? **Recommend: restore**, it
   was verified working. -> decision: restore it, verify it works (again)

4. **Failure mode.** If a marker is present but the script cannot render it, should
   `task build` fail, or warn and leave the marker? **Recommend: fail**, consistent with
   `localize_bundle_assets.py`, since a silently empty listing is the exact failure this
   whole guard-rail effort exists to prevent. -> decision: fail

5. **`/tags/` page size.** 45 sections listing 531 page references. Acceptable, or should
   the bare marker exclude high-cardinality tags like `TransformOperator`? **Recommend:
   include everything**, matching production.  -> decision: match prod, include everything

## 6. Known limitation: `task serve`

`zensical serve` rebuilds into `site/` on every change, so it would overwrite anything a
post-build step writes. The live-reload preview therefore shows the raw
`<!-- material/tags -->` markers, not the listings - measured: 0 tag sections, 3 markers
left on `/tutorials/`. The same applies to the glightbox localisation.

`task preview` covers the gap: it runs a full `task build` and serves the result on port
8001. Verified: 45 sections on `/tags/`, 3 on `/tutorials/`, 0 markers, 0 unpkg references.
This is inherent to post-build processing and goes away with the script.

## 7. Removal

The trigger is already wired. `check_zensical_output.py` tracks `tag-listings` as `PEND`
and prints a `NEW` banner the moment Zensical renders a listing itself. On that signal:

1. delete `tools/render_tag_listings.py`
2. drop its line from `build` in `Taskfile.yml`
3. delete `overrides/partials/tags.html` if §9 was implemented - Zensical will populate
   `tag.url` itself once it has a listing index, and its stock template already handles it
4. drop the `tag-listings-*` checks from `check_zensical_output.py`

Sources need no changes, because they were never changed.

## 8. Acceptance

- `/tags/` renders 45 tag sections; `/tutorials/` renders 3, in marker order
- zero `<!-- material/tags -->` comments remain in `site/**/*.html`
- `check_zensical_output.py` no longer reports unexpanded markers
- every generated link resolves to a real file in `site/`
- tag chips in listings render with icons for the 31 mapped tags
- `task build` still clean under `--strict`; page count unchanged at 584
- output stable across two consecutive builds (no ordering nondeterminism)

## 9. Link page tag chips to their listing anchor

**Status:** implemented 2026-08-23 as `overrides/partials/tags.html`. All three open
questions settled as recommended; the reachability assertion is `tag-chips-resolve` in
`check_zensical_output.py`.

### Problem

Rendering the listings only solved half the feature. Material also turns each per-page tag
chip into a link to its section on `/tags/`, so a reader can jump from "this page is tagged
Docker" to "everything tagged Docker". Zensical emits the chips as inert `<span>`s.

Measured on the current build: **531 pages carry a tag nav, 703 chips in total, 0 of them
links.** Production, for the same page:

```html
<a href="../../../tags/#tag:configuration" class="md-tag md-tag-icon md-tag--configuration">Configuration</a>
```

versus ours:

```html
<span class="md-tag md-tag-icon md-tag--configuration">Configuration</span>
```

Now that §1-§8 generate those anchors, every one of these links has a valid destination.
The anchors exist; nothing points at them.

### Approach: template override, *not* post-build injection

`zensical/templates/partials/tags.html` is **byte-identical to Material 9.7.7's**. It
already contains the branch that produces a link:

```jinja
{% if tag.url %}
  <a href="{{ tag.url | url }}" class="{{ class }}">{{ tag.name }}</a>
{% else %}
  <span class="{{ class }}">{{ tag.name }}</span>
{% endif %}
```

The template is not the problem - `tag.url` is simply never populated, because Zensical has
no listing index to point at. So the fix is to compute the URL in an override rather than
depend on `tag.url`, exactly as `overrides/partials/tabs-item.html` does for tab icons.

This is strictly better than extending `render_tag_listings.py`:

| | template override | post-build injection |
| :-- | :-- | :-- |
| Works in `task serve` | **yes** | no (see §6) |
| Extra build step | none | another pass over 531 pages |
| Removal when #38 lands | delete one file | more code to unpick |

### Verified feasible

A spike produced output byte-identical to production's, then was reverted. MiniJinja
supports the three filters needed (`url`, `lower`, `replace`):

```jinja
{% set anchor = "tags/" | url ~ "#tag:" ~ (tag.name | lower | replace(" ", "-")) %}
<a href="{{ anchor }}" class="{{ class }}">{{- tag.name -}}</a>
```

`| url` resolves `tags/` relative to the current page, so it survives mike's versioned
prefixes without special handling.

### Open questions

1. **Slug duplication.** The template computes the slug in MiniJinja; `render_tag_listings.
   tag_slug()` computes it in Python. They must agree or every link dangles. Accept the
   duplication with a comment in both places, or have the renderer assert that each anchor
   it emits is reachable? **Recommend: assert** - it is a cheap required check and the
   failure mode is otherwise silent.

2. **Tags with no listing section.** A tag carried *only* by the listing page itself
   produces no section (self-exclusion, §3), so its chip would link to a dead anchor. Does
   not occur today. **Recommend: cover it with the check in Q1** rather than special-casing.

3. **`hide: tags` pages.** The existing template already honours it; the override must keep
   that branch. No decision needed, just do not drop it.
