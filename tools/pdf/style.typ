// =============================================================================
// eccenca Corporate Memory documentation - print style
//
// Renders the book that `dec-tool build-pdf` assembles from the built site.
// Palette, type scale, page geometry, header and footer, the peach title and
// heading bands and the booktabs tables follow the eccenca policy house style
// (eccenca-policy-template, style/eccenca.typ), where they were measured from
// the released policy PDFs. What a technical manual needs and a short policy
// does not is marked DEVIATION, so the two stay comparable.
//
// The fonts are vendored in fonts/ and the build passes --ignore-system-fonts,
// so the PDF does not depend on what is installed where it is built.
// =============================================================================

// -- palette (house style) ----------------------------------------------------
#let ec-orange = rgb("#F29100")
#let ec-peach = rgb("#FCF0E0")
#let ec-slate = rgb("#2E3B45")
#let ec-grey = rgb("#6B757C")
#let ec-link = rgb("#0563C1")
// DEVIATION: the policy palette has no alarm colour; danger admonitions need one.
#let ec-red = rgb("#B3261E")
// DEVIATION: neutral ground for code and for note and info admonitions.
#let ec-wash = rgb("#F3F5F6")

// -- type scale -----------------------------------------------------------------
// The house style's scale was measured at 11pt body text. Every size in the
// text flow is expressed relative to that, so changing size-base rescales the
// book and keeps its proportions. The page furniture and the title page keep
// the measured sizes; they are what makes the house style recognisable.
//
// DEVIATION: the body text is set below the measured 11pt, which suits a
// reference manual of this length better than it would a two-page policy.
#let size-base = 10pt
#let scaled(house) = house / 11pt * size-base

// text flow
#let size-body = size-base
#let size-chapter = scaled(22pt)
#let size-h1 = scaled(14pt)
#let size-h2 = scaled(12pt)
#let size-h3 = scaled(11pt)
// admonitions, cards and tab labels
#let size-small = scaled(10pt)
#let size-table = scaled(9.5pt)
// DEVIATION: code has no size in the policy style, which has no code at all.
#let size-code = scaled(8.5pt)

// page furniture and title page, fixed
#let size-title = 22pt
#let size-subtitle = 16pt
#let size-meta = 10pt
#let size-eyebrow = 9pt

// -- fonts --------------------------------------------------------------------
// DEVIATION: the policy style has neither a monospace face nor an emoji font.
// The docs carry thousands of code blocks and code spans, and emoji in terminal
// transcripts and prose, which would otherwise print as empty boxes. Roboto
// Mono matches Roboto; Noto Color Emoji is the COLRv1 build, vector, so it
// stays sharp at any zoom. DejaVu comes last and catches what the Roboto
// families lack: arrows, box drawing in terminal output, and the Arabic,
// Hebrew, Georgian and Armenian examples. It follows the emoji font, because
// it has monochrome glyphs for symbols such as the warning sign that the docs
// mean as emoji.
#let emoji = "Noto Color Emoji"
#let sans = ("Roboto", emoji, "DejaVu Sans")
#let mono = ("Roboto Mono", emoji, "DejaVu Sans Mono")

// pandoc writes thematic breaks as #divider(), releases before 3.8 as
// #horizontalrule; all of them get the house style's rule.
#let divider(..args) = line(length: 100%, stroke: 0.5pt + ec-orange)
#let horizontalrule = divider()
#let horizontalRule = divider()

// -- documentation blocks (DEVIATION: a policy has none of these) --------------
#let alarm-kinds = ("danger", "error", "failure", "bug")
#let caution-kinds = ("warning", "caution", "attention")

#let admonition(kind: "note", title: none, body) = {
  let accent = if kind in alarm-kinds { ec-red } else if kind in caution-kinds { ec-orange } else { ec-slate }
  let ground = if kind in alarm-kinds { ec-red.lighten(92%) } else if kind in caution-kinds { ec-peach } else { ec-wash }
  block(
    width: 100%,
    fill: ground,
    stroke: (left: 2.5pt + accent),
    inset: (left: 11pt, right: 9pt, y: 8pt),
    above: 1.4em,
    below: 1.4em,
    {
      set text(size: size-small)
      set par(spacing: 1.1em)
      set block(spacing: 1em)
      if title != none {
        block(below: 0.8em, sticky: true, text(weight: "bold", fill: accent, title))
      }
      body
    },
  )
}

// Print shows every tab: each panel under its label, one after the other.
#let tabs(body) = block(width: 100%, above: 1.4em, below: 1.4em, body)

// The orange rule belongs to the label row. As a stroke on the breakable panel
// it would be drawn again at the top of every page the panel continues on.
#let tab(label, body) = block(width: 100%, above: 1.2em, below: 1.2em, {
  block(width: 100%, below: 0pt, sticky: true, stroke: (bottom: 1pt + ec-orange), box(
    fill: ec-peach,
    inset: (x: 8pt, y: 4pt),
    radius: (top-left: 2pt, top-right: 2pt),
    text(size: size-small, weight: "medium", fill: ec-slate, label),
  ))
  block(width: 100%, above: 0pt, inset: (top: 10pt), body)
})

// A code block with a title bar, or one whose widest line has to fit: terminal
// tables drawn with box characters fall apart when a line wraps, so for those
// the build passes the widest line in characters, and the text shrinks until
// it fits. 0.61 em is the advance of Roboto Mono (0.600) and of the DejaVu Sans
// Mono box glyphs (0.602), with a little room; 18pt is the block's inset.
#let codeblock(title: "", columns: none, body) = block(width: 100%, above: 1.2em, below: 1.2em, {
  if title != "" {
    block(
      below: 0pt,
      sticky: true,
      width: 100%,
      fill: ec-slate,
      inset: (x: 9pt, y: 4pt),
      radius: (top-left: 2pt, top-right: 2pt),
      text(size: size-code, weight: "medium", fill: white, title),
    )
  }
  set block(above: 0pt)
  if columns == none {
    body
  } else {
    layout(region => {
      let fitting = (region.width - 18pt) / (columns * 0.61)
      show raw.where(block: true): set text(size: calc.min(size-code, fitting))
      body
    })
  }
})

#let cards(..items) = grid(columns: (1fr, 1fr), column-gutter: 10pt, row-gutter: 10pt, ..items.pos())

// A card is not breakable: split across pages, its title and rule would stay
// behind on one page and its text start the next.
#let card(body) = block(width: 100%, breakable: false, stroke: 0.5pt + ec-grey.lighten(55%), radius: 2pt, inset: 10pt, {
  set text(size: size-small)
  set par(spacing: 1em, justify: false)
  set block(spacing: 0.9em)
  set list(indent: 0.2em, body-indent: 0.8em)
  body
})

// -----------------------------------------------------------------------------
// The book: title page, contents, then the documentation itself.
// -----------------------------------------------------------------------------
#let book(
  title: "",
  subtitle: "",
  context-line: "",
  generated: "",
  version: "",
  site-url: "",
  copyright: "",
  body,
) = {
  set document(
    title: title + " " + subtitle,
    author: "eccenca GmbH",
    keywords: ("Corporate Memory", "documentation", version),
  )

  // -- page furniture (house style geometry) -------------------------------------
  set page(
    paper: "a4",
    margin: (top: 3.9cm, bottom: 2.2cm, left: 2.5cm, right: 2.5cm),
    header-ascent: 1.14cm,
    footer-descent: 0.51cm,
    // The title page carries version and date in its title block, so its
    // header is the logo alone.
    header: context grid(
      columns: (1fr, auto),
      align(left + top, pad(left: -28pt, image("logo.svg", width: 4cm))),
      if here().page() == 1 { [] } else {
        align(right + bottom, text(size: size-meta, fill: ec-grey, weight: "regular", {
          set par(leading: 0.56em)
          [Version #version]
          linebreak()
          [Generated #generated]
        }))
      },
    ),
    // DEVIATION: the policy footer repeats the document title. In a book the
    // chapter the reader is in is the more useful running title.
    footer: context {
      let page-no = here().page()
      if page-no > 1 {
        let chapters = query(heading.where(level: 1)).filter(h => h.location().page() <= page-no)
        let running = if chapters.len() > 0 { chapters.last().body } else { [#title #subtitle] }
        grid(
          columns: (1fr, auto),
          text(size: size-meta, fill: ec-orange, running),
          text(size: size-meta, fill: ec-orange)[Page #counter(page).display() | #counter(page).final().first()],
        )
      }
    },
  )

  // -- base typography (house style) -----------------------------------------------
  set text(
    font: sans,
    weight: "light",
    size: size-body,
    fill: ec-slate,
    lang: "en",
    hyphenate: false,
    // A glyph that none of the vendored fonts has falls back to the fonts
    // built into Typst instead of printing as an empty box.
    fallback: true,
  )
  set par(justify: true, leading: 0.76em, spacing: 2.24em)
  set list(
    indent: 1.84em,
    body-indent: 1.5em,
    spacing: 0.85em,
    marker: level => {
      let markers = (
        box(baseline: -0.144em, circle(radius: 1.5pt, fill: ec-slate)),
        text(size: 1.1em, baseline: 0.03em, weight: "regular")[–],
        box(baseline: -0.144em, circle(radius: 1.1pt, stroke: 0.6pt + ec-slate)),
      )
      // DEVIATION: the policy style stops at three levels; the docs nest deeper,
      // so the markers repeat.
      markers.at(calc.rem(level, markers.len()))
    },
  )
  set enum(indent: 1.84em, body-indent: 1.64em, spacing: 0.85em)
  set block(spacing: 1.52em)
  show link: it => text(fill: ec-link, underline(it))

  // -- code ---------------------------------------------------------------------
  show raw: set text(font: mono, weight: "regular")
  // No horizontal extent: the table rule below splits a code span into several
  // text runs at its break opportunities, and a run whose background reaches
  // past its own edge paints over the last glyph of the run before it.
  show raw.where(block: false): it => highlight(fill: ec-wash, extent: 0pt, text(size: 0.84em, it))
  // The size is a show-set rule of its own, not part of the block below, so
  // that codeblock() can shrink a terminal table from an inner scope.
  show raw.where(block: true): set text(size: size-code)
  show raw.where(block: true): it => block(
    width: 100%,
    fill: ec-wash,
    inset: (x: 9pt, y: 8pt),
    radius: (bottom-left: 2pt, bottom-right: 2pt),
    {
      set par(justify: false, leading: 0.55em)
      it
    },
  )

  // -- headings -------------------------------------------------------------------
  // DEVIATION: one level deeper than a policy. A navigation section is a chapter
  // above the page, so chapters take the title band and pages the band a policy
  // uses for its top-level headings. Chapters start on a new page; the build
  // places that break before the chapter, not in this rule, so content a page
  // shows above its title stays with it.
  show heading.where(level: 1): it => block(
    width: 100%,
    fill: ec-peach,
    inset: (x: 0pt, y: 12pt),
    outset: (x: 2pt),
    below: 1.4em,
    sticky: true,
    text(size: size-chapter, weight: "medium", fill: ec-slate, it.body),
  )
  show heading.where(level: 2): it => block(
    width: 100%,
    fill: ec-peach,
    inset: (x: 0pt, y: 8pt),
    outset: (x: 2pt),
    above: 2.6em,
    below: 1.1em,
    sticky: true,
    text(size: size-h1, weight: "medium", fill: ec-slate, it.body),
  )
  show heading.where(level: 3): it => block(above: 1.8em, below: 0.9em, sticky: true,
    text(size: size-h2, weight: "bold", fill: ec-slate, it.body))
  show heading.where(level: 4): it => block(above: 1.5em, below: 0.8em, sticky: true,
    text(size: size-h3, weight: "bold", fill: ec-slate, it.body))
  show heading.where(level: 5): it => block(above: 1.3em, below: 0.7em, sticky: true,
    text(size: size-h3, weight: "medium", fill: ec-grey, it.body))
  show heading.where(level: 6): it => block(above: 1.3em, below: 0.7em, sticky: true,
    text(size: size-h3, weight: "medium", fill: ec-grey, it.body))

  // -- tables: booktabs (house style) -----------------------------------------------
  set table(
    inset: (x: 5pt, y: 5pt),
    align: left + top,
    stroke: (x, y) => (
      top: if y == 0 { 0.9pt + ec-slate } else if y == 1 { 0.6pt + ec-slate } else {
        0.3pt + ec-grey.lighten(45%)
      },
    ),
  )
  // DEVIATION: breakable. The policy keeps a table whole because it merges rows;
  // the docs have tables longer than a page and no merged rows.
  show figure.where(kind: table): set block(breakable: true)
  show table: it => block(
    breakable: true,
    stroke: (bottom: 0.9pt + ec-slate),
    inset: 0pt,
    above: 1.2em,
    below: 1.2em,
    {
      set text(size: size-table, hyphenate: false)
      set par(justify: false, leading: 0.5em)
      // DEVIATION: break opportunities after @ / . _ - so identifiers, IRIs and
      // addresses wrap inside their cell instead of running into the next one.
      show regex("[@/._-]"): it => it + sym.zws
      it
    },
  )
  show table.cell.where(y: 0): set text(weight: "medium")

  // -- title page ----------------------------------------------------------------------
  // DEVIATION: a page of its own. A policy runs from its title block straight
  // into the text; a manual of this length gets a title page, and its contents
  // start on the next one. The title block itself is the house style's.
  v(3.2cm)
  text(size: size-eyebrow, fill: ec-grey, weight: "regular", tracking: 0.06em, upper(context-line))
  v(0.35em, weak: true)
  block(
    width: 100%,
    fill: ec-peach,
    inset: (x: 0pt, y: 12pt),
    outset: (x: 2pt),
    text(size: size-title, weight: "medium", fill: ec-slate, title),
  )
  v(0.6em, weak: true)
  align(right, text(size: size-subtitle, weight: "light", fill: ec-slate, subtitle))
  v(0.5em, weak: true)
  line(length: 100%, stroke: 0.5pt + ec-grey.lighten(50%))
  v(0.5em, weak: true)
  align(right, text(size: size-meta, fill: ec-grey, weight: "regular")[Generated #generated])
  v(1fr)
  block(text(size: size-meta, fill: ec-grey, weight: "regular", {
    set par(leading: 0.56em, justify: false)
    link(site-url)
    linebreak()
    copyright
  }))
  pagebreak()

  // -- contents ----------------------------------------------------------------------
  text(size: size-h2, weight: "bold", fill: ec-slate)[Content]
  v(0.4em)
  {
    set par(justify: false)
    show outline.entry.where(level: 1): set text(weight: "medium")
    show outline.entry.where(level: 1): set block(above: 1.1em)
    outline(title: none, depth: 2, indent: 1.2em)
  }
  pagebreak(weak: true)

  body
}
