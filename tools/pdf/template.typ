// pandoc template for `dec-tool build-pdf`.
//
// pandoc places the normalized book at the body variable at the end. Layout,
// title page and contents live in style.typ; the edition details arrive as
// `typst compile --input` values, so nothing from the build is spliced into
// Typst source as text. Every dollar sign here is pandoc template syntax, even
// inside a comment.
#import "/tools/pdf/style.typ": *

$if(highlighting-definitions)$
$highlighting-definitions$

$endif$
#show: book.with(
  title: sys.inputs.at("title"),
  subtitle: sys.inputs.at("subtitle"),
  context-line: sys.inputs.at("context"),
  generated: sys.inputs.at("generated"),
  commit: sys.inputs.at("commit"),
  version: sys.inputs.at("version"),
  site-url: sys.inputs.at("site-url"),
  copyright: sys.inputs.at("copyright"),
)

$body$
