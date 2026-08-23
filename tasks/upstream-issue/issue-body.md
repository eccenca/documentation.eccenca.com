### Context

When `markdown.extensions.fenced_code` and `pymdownx.superfences` are both enabled, the
precedence between their two fenced-code processors is not stable across builds. It
varies with the process's `PYTHONHASHSEED`, so the same input produces different HTML
from one run to the next.

Only superfences understands the `title="..."` fence attribute. On runs where
`fenced_code` wins instead, the fence never opens and the rest of the document is
emitted as raw text inside a `<pre><code>` block — headings included, so their `id`s
disappear and every deep link into them breaks.

Most projects reach this through `markdown.extensions.extra`, which bundles
`fenced_code`. `mkdocs build` on the same input is correct for every seed, so this is a
compatibility regression rather than a config error.

### Bug description

With the attached reproduction:

```
$ sh repro.sh
PYTHONHASHSEED=0   headings=3/3
PYTHONHASHSEED=1   headings=2/3
PYTHONHASHSEED=2   headings=3/3
PYTHONHASHSEED=3   headings=2/3
...
5 of 12 seeds mis-rendered
```

Expected `3/3` for every seed. On a failing seed a section renders as:

```html
<p>```text title=&rdquo;Usage&rdquo;
example</p>
<pre><code>
## section three
...
```

Note the curly quotes: inline processing has been applied to what should have been
code, which is the tell that the fence was never recognised.

Bisecting `extra` isolates the cause precisely. With `pymdownx.superfences` enabled and
twelve seeds each:

| `markdown_extensions` | seeds mis-rendered |
| --- | --- |
| `abbr`, `attr_list`, `def_list`, `footnotes`, `md_in_html`, `tables` | 0 / 12 |
| the same six **plus** `fenced_code` | 5 / 12 |
| `fenced_code` alone | 5 / 12 |
| `extra` (the bundle) | 5 / 12 |

So `fenced_code` is both necessary and sufficient; the other six members of `extra` are
uninvolved.

On our own site (~580 pages) this costs 62 anchors across 5 pages on a failing seed,
and `zensical build --strict` fails on roughly two thirds of cold runs. Because it is
tied to the hash seed rather than to timing, `--clean` does not avoid it.

### Related links

- #641 — same non-determinism family, but that report is about *false-positive* link
  warnings with correct output. Here the warnings are *true positives*: the anchors
  really are absent because the page mis-rendered. #641's `--clean` workaround has no
  effect on this one, so it may be a second mechanism.

`PYTHONHASHSEED` may also be a useful handle for #641 itself: it turns an intermittent
failure into a deterministic one.

### Reproduction

Attached. Two files plus a shell script.

### Steps to reproduce

1. `sh repro.sh`
2. Any seed reporting `2/3` shows the defect; inspect `site/page/index.html`.

### Browser

_No response_

### Versions

Reproduced identically on zensical 0.0.44, 0.0.48, 0.0.52, 0.0.55, 0.0.56 and 0.0.57
(Python 3.13, macOS). Pinning an older version is not a workaround.

Dropping `fenced_code` — in practice, replacing `extra` with its six other members —
avoids it entirely: 0 of 12 seeds mis-render, with byte-equivalent output otherwise.

### Before submitting

- [x] I have read and followed the [bug reporting guidelines](https://zensical.org/docs/community/contribute/report-a-bug/).
- [x] I have attached links to [the documentation](https://zensical.org/docs/), and possibly related [issues](https://github.com/zensical/zensical/issues).
- [x] I assure that I have [removed all customizations](https://zensical.org/docs/community/contribute/report-a-bug/#remove-customizations) before submitting this bug report.
- [x] I have attached a __.zip file__ with a [minimal reproduction](https://zensical.org/docs/community/guides/create-a-reproduction/).
