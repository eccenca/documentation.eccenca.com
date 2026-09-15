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

// -- edition --------------------------------------------------------------------
// `dec-tool build-pdf --edition print` passes `--input edition=print` for the
// book block of a printed book (tasks/spec.md). Everything that differs between
// the editions branches on this flag; without the input the screen PDF is built
// exactly as before.
#let print-edition = sys.inputs.at("edition", default: "screen") == "print"

// -- palette (house style) ----------------------------------------------------
// DEVIATION (print): the book prints in black and white on BoD's presses, which
// screen a grey below 20 % black unevenly or not at all. So text and accents
// print black, the orange turns a dark grey that still reads as a rule, the peach
// bands take the lightest grey BoD accepts, and the grounds lighter than that -
// code and note admonitions - are left white (see the rules that use ec-wash).
#let ec-orange = if print-edition { luma(30%) } else { rgb("#F29100") }
#let ec-peach = if print-edition { luma(80%) } else { rgb("#FCF0E0") }
#let ec-slate = if print-edition { luma(0%) } else { rgb("#2E3B45") }
#let ec-grey = if print-edition { luma(40%) } else { rgb("#6B757C") }
#let ec-link = rgb("#0563C1")
// DEVIATION: the policy palette has no alarm colour; danger admonitions need one.
#let ec-red = if print-edition { luma(0%) } else { rgb("#B3261E") }
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
  // DEVIATION (print): no ground - the light grounds print below BoD's 20 %
  // black - so the bar on the left carries the kind alone.
  let ground = if print-edition { none } else if kind in alarm-kinds { ec-red.lighten(92%) } else if kind in caution-kinds { ec-peach } else { ec-wash }
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
// DEVIATION (print): the text never shrinks below 6 pt, the smallest size that
// stays legible on paper; a wider table then runs past the block's edge.
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
      let size = calc.min(size-code, fitting)
      show raw.where(block: true): set text(size: if print-edition { calc.max(6pt, size) } else { size })
      body
    })
  }
})

// A card is not breakable: split across pages, its title and rule would stay
// behind on one page and its text start the next.
#let card-frame(body, height: auto) = block(
  width: 100%,
  height: height,
  breakable: false,
  stroke: 0.5pt + ec-grey.lighten(55%),
  radius: 2pt,
  inset: 10pt,
  {
    set text(size: size-small)
    set par(spacing: 1em, justify: false)
    set block(spacing: 0.9em)
    set list(indent: 0.2em, body-indent: 0.8em)
    body
  },
)

// tools/pdf/filter.lua passes each card's content through card() to cards().
#let card(body) = body

// The field line under an operator's title in the compact operator reference:
// type, category, plugin ID (tasks/spec.md, §11). Kept with what follows.
#let operator-fields(body) = block(above: 0.35em, below: 0.9em, sticky: true, {
  set par(justify: false)
  text(size: size-small, fill: ec-grey, body)
})

// DEVIATION: facing cards end on one line (tasks/spec.md, §11). The cards of a
// row are measured at the column width and both framed at the height of the
// taller one; a card alone in the last row keeps its own height.
#let cards(..items) = layout(region => {
  let bodies = items.pos()
  let gutter = 10pt
  let width = (region.width - gutter) / 2
  let cells = ()
  for row in range(0, bodies.len(), step: 2) {
    let pair = bodies.slice(row, calc.min(row + 2, bodies.len()))
    let height = if pair.len() < 2 { auto } else {
      calc.max(..pair.map(body => measure(card-frame(body), width: width).height))
    }
    cells += pair.map(body => card-frame(body, height: height))
  }
  grid(columns: (1fr, 1fr), column-gutter: gutter, row-gutter: gutter, ..cells)
})

// DEVIATION: a policy links nowhere outside itself. The docs link to other
// sites and to the published site for what the PDF cannot carry, and such a
// link has to read apart from a jump within the book. The arrow is a glyph,
// not an icon box, so a line cannot break between it and the link text. Its
// font is named, because the emoji font would draw it as a coloured emoji.
#let external-mark = text(font: "DejaVu Sans", weight: "regular", size: 0.8em, fill: ec-link)[↗]

// A heading's number and title, as the running footer prints them.
#let numbered-title(it) = {
  if it.numbering != none {
    numbering(it.numbering, ..counter(heading).at(it.location()))
    [ ]
  }
  it.body
}

// -- print edition: right-hand starts and page furniture --------------------------
// A bound book starts a part, its contents and its text on a right-hand (odd)
// page. The break leaves a blank left-hand page when it has to, and Typst gives
// that page the same header and footer as any other. So the break brackets
// itself with two markers: a page strictly between them was inserted blank.
#let recto-break() = {
  [#metadata("recto-before") <recto-before>]
  pagebreak(weak: true, to: "odd")
  [#metadata("recto-after") <recto-after>]
}

// Pages that carry neither header nor footer in the print edition: the title
// page, the imprint, the part covers and blank pages.
#let bare-page(page) = {
  if page <= 2 { return true }
  if query(heading.where(level: 1)).any(h => h.location().page() == page) { return true }
  let pairs = query(<recto-before>).zip(query(<recto-after>))
  if pairs.any(((before, after)) => before.location().page() < page and page < after.location().page()) {
    return true
  }
  query(<blank-page>).any(marker => marker.location().page() == page)
}

// DEVIATION (print): page numbers sit on the outer edge, as in a bound book. A
// left-hand page names the part beside its number, a right-hand page the page
// the reader is in. The page total means nothing on paper and is left out.
#let print-footer(page-no) = {
  set par(justify: false, leading: 0.56em)
  set text(size: size-meta, fill: ec-orange)
  let started(h) = h.location().page() <= page-no
  let parts = query(heading.where(level: 1)).filter(started)
  let folio = text(weight: "medium", counter(page).display())
  let running = if parts.len() == 0 { none } else if calc.even(page-no) { parts.last() } else {
    let pages = query(heading.where(level: 2).after(parts.last().location())).filter(started)
    if pages.len() > 0 { pages.last() } else { parts.last() }
  }
  // A left-hand page names its part as the part's title band does: Part A: Build.
  let title = if running == none { [] } else if calc.even(page-no) and running.level == 1 {
    [Part #numbering("A", ..counter(heading).at(running.location())): #running.body]
  } else { numbered-title(running) }
  if calc.even(page-no) {
    grid(columns: (auto, 1fr), column-gutter: 1.2em, folio, title)
  } else {
    grid(columns: (1fr, auto), column-gutter: 1.2em, align(right, title), folio)
  }
}

// The label above a contents.
#let contents-title = text(size: size-h2, weight: "bold", fill: ec-slate)[Content]

// The break before a part, its contents and its text: a new page on screen, a
// right-hand page in print. tools/pdf/filter.lua places it before every part.
#let chapter-break() = if print-edition { recto-break() } else { pagebreak(weak: true) }

// DEVIATION: a policy has one contents. A part of this book has a cover page -
// its title and, if the part has one, the diagram of where it sits - and its
// own contents on the pages after: the part's pages and two levels of their
// sections, up to the next part. The build places the call after the cover.
#let part-contents() = {
  chapter-break()
  contents-title
  v(0.4em)
  context {
    let next-part = selector(heading.where(level: 1)).after(here(), inclusive: false)
    set par(justify: false)
    // Closer than the front contents: Build alone lists over 350 entries.
    set block(spacing: 0.8em)
    show outline.entry.where(level: 2): set text(weight: "medium")
    show outline.entry.where(level: 2): set block(above: 1.1em)
    outline(
      title: none,
      indent: auto,
      target: heading.where(level: 2).or(heading.where(level: 3)).or(heading.where(level: 4))
        .after(here()).before(next-part),
    )
  }
  chapter-break()
}

// DEVIATION (print): a link out of the book carries a superscript number, and
// its part ends with a list of the web addresses it cites (tasks/spec.md, §11,
// D15). The numbers run within a part, and an address cited again keeps its
// number. The list is set as text, without link annotations - Typst footnotes
// link marker and entry, and PDF/X output wants no annotations.
#let part-start() = query(heading.where(level: 1).before(here())).at(-1, default: none)

#let cited-addresses() = {
  let part = part-start()
  let cited = selector(<web-address>)
  query(if part == none { cited } else { cited.after(part.location()) }.before(here()))
}

#let web-address(address) = {
  [#metadata(address) <web-address>]
  context {
    let order = ()
    for cited in cited-addresses() {
      if cited.value not in order { order.push(cited.value) }
    }
    super(str(order.position(value => value == address) + 1))
  }
}

// The build places the call at the end of every part (tools/build_pdf.py).
#let part-addresses() = if print-edition {
  context {
    let order = ()
    let pages = (:)
    for cited in cited-addresses() {
      let page = numbering("1", ..counter(page).at(cited.location()))
      let known = pages.at(cited.value, default: none)
      if known == none {
        order.push(cited.value)
        pages.insert(cited.value, (page,))
      } else if page not in known {
        pages.insert(cited.value, known + (page,))
      }
    }
    if order.len() > 0 {
      pagebreak(weak: true)
      heading(level: 2, numbering: none, outlined: false, bookmarked: true)[Web addresses]
      set text(size: size-table)
      set par(justify: false)
      show regex("[/._-]"): mark => mark + sym.zws
      grid(
        columns: (auto, 1fr),
        column-gutter: 0.8em,
        row-gutter: 0.65em,
        ..order.enumerate().map(((index, address)) => {
          let cited = pages.at(address)
          let label = if cited.len() == 1 { "p." } else { "pp." }
          (str(index + 1), [#address #text(fill: ec-grey)[(#label~#cited.join(", "))]])
        }).flatten(),
      )
    }
  }
}

// DEVIATION (print): the back of the title page is the imprint - edition,
// publisher, authors, licence and the online edition - and it carries the
// edition stamp the screen PDF prints in its header. tools/pdf/print.yml holds
// the publisher and the section modes. The authors arrive as an input: the build
// applies the names and exclusions of print.yml to tools/pdf/authors.yml.
#let imprint(title: "", context-line: "", subtitle: "", generated: "", site-url: "", copyright: "", authors: "") = {
  let config = yaml("print.yml")
  let mode(section) = if type(section) == dictionary { section.at("mode", default: "full") } else { section }
  let shortened = config.at("sections", default: (:)).values().any(section => mode(section) != "full")
  set text(size: size-small, fill: ec-slate)
  set par(justify: false, leading: 0.6em, spacing: 1.2em)
  let entry(label, body) = block(below: 1.3em, [#text(weight: "bold", label) \ #body])
  v(1fr)
  entry(title)[#context-line, #subtitle \ Print edition, generated #generated]
  entry("Publisher")[#config.publisher.name \ #config.publisher.address.join(linebreak())]
  entry("Authors")[The contributors to the documentation, most commits to the printed pages first: #authors.]
  // The URL is a string: written as markup, Typst would turn it into a link.
  entry("Licence")[
    This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License,
    #"https://creativecommons.org/licenses/by-sa/4.0/". #copyright
  ]
  entry("Online edition")[
    #site-url
    #if shortened [\ The online edition is the complete reference; this print edition shortens some of its sections.]
  ]
  entry("Typesetting")[
    Typeset with Typst from the Markdown sources of the documentation, in Roboto, Roboto Mono, Noto Color
    Emoji and DejaVu.
  ]
}

// -----------------------------------------------------------------------------
// The book: title page, contents, then the documentation itself.
// -----------------------------------------------------------------------------
#let book(
  title: "",
  subtitle: "",
  context-line: "",
  generated: "",
  commit: "",
  version: "",
  site-url: "",
  copyright: "",
  authors: "",
  body,
) = {
  set document(
    title: title + " " + subtitle,
    author: "eccenca GmbH",
    keywords: ("Corporate Memory", "documentation", version),
  )

  // DEVIATION: the commit next to the date, so a PDF can be traced to its source.
  let generated = if commit == "" { generated } else { generated + " (" + commit + ")" }

  // -- page furniture (house style geometry) -------------------------------------
  set page(
    paper: "a4",
    // DEVIATION (print): a bound book mirrors its margins - wider inside for the
    // binding, narrower outside - and keeps the 16 cm text width. Its header is
    // empty, with no logo and no version on text pages, so the top margin
    // shrinks to what a page without it needs.
    binding: if print-edition { left } else { auto },
    margin: if print-edition {
      (top: 2.5cm, bottom: 2.2cm, inside: 3.0cm, outside: 2.0cm)
    } else {
      (top: 3.9cm, bottom: 2.2cm, left: 2.5cm, right: 2.5cm)
    },
    header-ascent: 1.14cm,
    footer-descent: 0.51cm,
    // The title page carries version and date in its title block, so its
    // header is the logo alone.
    header: if print-edition { none } else {
      context grid(
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
      )
    },
    // DEVIATION: the policy footer repeats the document title. In a book the
    // chapter and the page the reader is in are the more useful running title.
    footer: context {
      let page-no = here().page()
      if print-edition {
        if not bare-page(page-no) { print-footer(page-no) }
      } else if page-no > 1 {
        // A long page title wraps; spread to the full width, it would gape.
        set par(justify: false, leading: 0.56em)
        let started(h) = h.location().page() <= page-no
        let chapters = query(heading.where(level: 1)).filter(started)
        let running = if chapters.len() == 0 { [#title #subtitle] } else {
          let chapter = chapters.last()
          let pages = query(heading.where(level: 2).after(chapter.location())).filter(started)
          numbered-title(chapter)
          if pages.len() > 0 { [ › #numbered-title(pages.last())] }
        }
        grid(
          columns: (1fr, auto),
          column-gutter: 1em,
          text(size: size-meta, fill: ec-orange, running),
          text(size: size-meta, fill: ec-orange)[Page #counter(page).display() | #counter(page).final().first()],
        )
      }
    },
  )

  // -- base typography (house style) -----------------------------------------------
  // DEVIATION (print): tools/pdf/print.yml may set a heavier body weight, which
  // prints darker in black and white.
  let body-weight = if print-edition { yaml("print.yml").at("body-weight", default: "light") } else { "light" }
  set text(
    font: sans,
    weight: body-weight,
    size: size-body,
    fill: ec-slate,
    lang: "en",
    // DEVIATION (print): justified text without hyphenation opens gaps that
    // a printed page shows more plainly than a screen. Titles stay whole.
    hyphenate: print-edition,
    // A glyph that none of the vendored fonts has falls back to the fonts
    // built into Typst instead of printing as an empty box.
    fallback: true,
  )
  show heading: set text(hyphenate: false)
  // DEVIATION (print): the house spacing suits a two-page policy; over a
  // thousand printed pages it costs a tenth of the book (tasks/spec.md, §5).
  set par(justify: true, leading: 0.76em, spacing: if print-edition { 1.2em } else { 2.24em })
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
  set block(spacing: if print-edition { 1.0em } else { 1.52em })
  // DEVIATION (print): paper cannot follow a link. A link within the book prints
  // the page it leads to, a link out of the book a number whose address its part
  // lists at the end (part-addresses), and neither leaves a link in the PDF
  // (tasks/spec.md, R4, D15).
  show link: it => if not print-edition {
    text(fill: ec-link, underline(it))
    if type(it.dest) == str and it.dest.starts-with(regex("https?://")) { external-mark }
  } else if type(it.dest) == label {
    // Always printed, also for a target on the same page: a reference that
    // appears only across pages moves lines, which moves the target back, and
    // the layout never settles.
    it.body
    context [~(p.~#numbering("1", ..counter(page).at(locate(it.dest))))]
  } else if type(it.dest) == str {
    let address = it.dest.trim("mailto:", at: start)
    it.body
    // An address that prints as its own text needs no number repeating it.
    if it.body.at("text", default: none) != address { web-address(address) }
  } else {
    it.body
  }
  // Footnotes carry addresses: set small, and breakable after / . _ -.
  show footnote.entry: set text(size: size-table)
  show footnote.entry: it => {
    show regex("[/._-]"): mark => mark + sym.zws
    it
  }
  // DEVIATION (print): contents entries without link annotations.
  show outline.entry: it => if print-edition { block(it.indented(it.prefix(), it.inner())) } else { it }

  // -- code ---------------------------------------------------------------------
  show raw: set text(font: mono, weight: "regular")
  // No horizontal extent: the table rule below splits a code span into several
  // text runs at its break opportunities, and a run whose background reaches
  // past its own edge paints over the last glyph of the run before it.
  // DEVIATION (print): no ground behind code, which would print below BoD's 20 %
  // black. The monospace face marks a code span, a thin frame a code block.
  show raw.where(block: false): it => if print-edition { text(size: 0.84em, it) } else {
    highlight(fill: ec-wash, extent: 0pt, text(size: 0.84em, it))
  }
  // The size is a show-set rule of its own, not part of the block below, so
  // that codeblock() can shrink a terminal table from an inner scope.
  show raw.where(block: true): set text(size: size-code)
  show raw.where(block: true): it => block(
    width: 100%,
    fill: if print-edition { none } else { ec-wash },
    stroke: if print-edition { 0.5pt + ec-grey } else { none },
    inset: (x: 9pt, y: 8pt),
    radius: (bottom-left: 2pt, bottom-right: 2pt),
    {
      set par(justify: false, leading: 0.55em)
      it
    },
  )
  // DEVIATION (print): a line of code breaks only at spaces and a few marks, so
  // a long URL or identifier ran past the frame. A zero-width space after
  // / . _ - & ; = ? , lets it wrap inside; the spaces would end up in copied
  // code, which paper does not have. They go into the block's text: a regex
  // show rule exceeds Typst's grouping depth on a long block. Defined after the
  // frame, so it runs first and the frame takes the new block. A block without
  // a mark to break after, or with a zero-width space already, is left as it
  // is: every block the rule replaces holds one, which ends the recursion.
  // Terminal tables keep their lines: codeblock() shrinks them to fit.
  show raw.where(block: true): it => if (
    not print-edition
      or it.text.contains(sym.zws)
      or not it.text.contains(regex("[/._&;=?,-]"))
      or it.text.contains(regex("[─-╿]"))
  ) { it } else {
    let fields = it.fields()
    let _ = fields.remove("text")
    let _ = fields.remove("lines", default: none)
    raw(..fields, it.text.replace(regex("[/._&;=?,-]"), mark => mark.text + sym.zws))
  }

  // -- headings -------------------------------------------------------------------
  // DEVIATION: one level deeper than a policy. A navigation section is a chapter
  // above the page, so chapters take the title band and pages the band a policy
  // uses for its top-level headings. Chapters start on a new page; the build
  // places that break before the chapter, not in this rule, so content a page
  // shows above its title stays with it.
  //
  // DEVIATION: a policy numbers 1.1.1. if it numbers at all. The parts of the
  // book are lettered and a part numbers its pages from 1 (A, A.1, A.1.1.1), down
  // to the sections its contents list; deeper headings carry no number.
  set heading(numbering: "A.1.1.1")
  show heading.where(level: 5): set heading(numbering: none)
  show heading.where(level: 6): set heading(numbering: none)
  let with-number(it, gap) = {
    if it.numbering != none {
      counter(heading).display(it.numbering)
      h(gap)
    }
    it.body
  }
  show heading.where(level: 1): it => block(
    width: 100%,
    fill: ec-peach,
    inset: (x: 0pt, y: 12pt),
    outset: (x: 2pt),
    below: 1.4em,
    sticky: true,
    // DEVIATION: a part's title names it as one - Part A: Build.
    text(size: size-chapter, weight: "medium", fill: ec-slate)[Part #counter(heading).display("A"): #it.body],
  )
  show heading.where(level: 2): it => block(
    width: 100%,
    fill: ec-peach,
    inset: (x: 0pt, y: 8pt),
    outset: (x: 2pt),
    above: 2.6em,
    below: 1.1em,
    sticky: true,
    text(size: size-h1, weight: "medium", fill: ec-slate, with-number(it, 0.6em)),
  )
  show heading.where(level: 3): it => block(above: 1.8em, below: 0.9em, sticky: true,
    text(size: size-h2, weight: "bold", fill: ec-slate, with-number(it, 0.5em)))
  show heading.where(level: 4): it => block(above: 1.5em, below: 0.8em, sticky: true,
    text(size: size-h3, weight: "bold", fill: ec-slate, with-number(it, 0.5em)))
  show heading.where(level: 5): it => block(above: 1.3em, below: 0.7em, sticky: true,
    text(size: size-h3, weight: "medium", fill: ec-grey, it.body))
  show heading.where(level: 6): it => block(above: 1.3em, below: 0.7em, sticky: true,
    text(size: size-h3, weight: "medium", fill: ec-grey, it.body))

  // -- figures ----------------------------------------------------------------------
  // DEVIATION: image figures carry no number. The site numbers none, and pages
  // that need numbers write them into the caption and refer to them in the text
  // ("see figure 3"); a book-wide number in front printed "Figure 15: Figure 2:".
  show figure.where(kind: image): set figure(numbering: none)
  // DEVIATION: a figure does not break across pages, and Typst does not shrink an
  // image taller than the page, so a tall screenshot at the column width ran into
  // the footer. An image in a figure that is taller than the page body, less room
  // for a two-line caption, is scaled down to that height, in proportion. Only
  // images in figures: `layout` is block-level, and an image in a line of text
  // stays inline. The scaled image has a height, which ends the recursion.
  show figure.where(kind: image): it => {
    show image: img => if img.height != auto { img } else {
      layout(region => {
        let room = region.height - 4em.to-absolute()
        if measure(img, width: region.width).height <= room { img } else {
          let fields = img.fields()
          let source = fields.remove("source")
          let _ = fields.remove("width", default: none)
          let _ = fields.remove("height", default: none)
          image(source, ..fields, height: room)
        }
      })
    }
    it
  }

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
  //
  // DEVIATION (print): page 1 of the book block. The header that carries the
  // logo on screen is empty in print, so the logo sits on the page itself. The
  // page names the publisher; date, link and copyright move to the imprint.
  if print-edition {
    place(top + left, dx: -28pt, dy: -1.3cm, image("logo.svg", width: 4cm))
    v(4.6cm)
  } else {
    v(3.2cm)
  }
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
  if print-edition {
    v(1fr)
    text(size: size-subtitle, weight: "regular", fill: ec-slate, yaml("print.yml").publisher.name)
  } else {
    v(0.5em, weak: true)
    align(right, text(size: size-meta, fill: ec-grey, weight: "regular")[Generated #generated])
    v(1fr)
    block(text(size: size-meta, fill: ec-grey, weight: "regular", {
      set par(leading: 0.56em, justify: false)
      link(site-url)
      linebreak()
      copyright
    }))
  }
  pagebreak()

  // -- imprint (print) ------------------------------------------------------------------
  if print-edition {
    imprint(
      title: title, context-line: context-line, subtitle: subtitle,
      generated: generated, site-url: site-url, copyright: copyright, authors: authors,
    )
    pagebreak()
  }

  // -- contents ----------------------------------------------------------------------
  // The parts only. Each part opens with the contents of its pages.
  contents-title
  v(0.4em)
  {
    set par(justify: false)
    show outline.entry: set text(weight: "medium")
    show outline.entry: set block(above: 1.1em)
    outline(title: none, depth: 1, indent: auto)
  }
  // In print the break before the first part follows directly: a weak break here
  // would leave the blank page before part A outside its markers.
  if not print-edition {
    pagebreak(weak: true)
  }

  body

  // DEVIATION (print): the build reads the page count from this marker and asks
  // for one blank last page when it is odd (tools/build_pdf.py, unpadded_pages).
  if print-edition {
    context [#metadata(here().page()) <book-end>]
    if sys.inputs.at("pad", default: "false") == "true" {
      pagebreak()
      [#metadata("pad") <blank-page>]
    }
  }
}
