-- pandoc filter for `dec-tool build-pdf`.
--
-- Maps the class-tagged divs that tools/build_pdf.py leaves in the normalized
-- book onto the functions in style.typ. Filters run bottom-up, so nested tabs
-- and admonitions are already raw Typst by the time their parent is wrapped.

local List = pandoc.List

local function raw(s)
  return pandoc.RawBlock('typst', s)
end

local function typst_string(s)
  return '"' .. (s:gsub('\\', '\\\\'):gsub('"', '\\"')) .. '"'
end

local function typst_inlines(inlines)
  local out = pandoc.write(pandoc.Pandoc({ pandoc.Plain(inlines) }), 'typst')
  return (out:gsub('%s+$', ''))
end

local function wrap(open, blocks, close)
  local out = List({ raw(open) })
  out:extend(blocks)
  out:insert(raw(close))
  return out
end

-- pandoc keeps data-* attributes, with or without the prefix depending on version.
local function attr(el, name)
  return el.attributes[name] or el.attributes['data-' .. name] or ''
end

function Div(el)
  local c = el.classes
  if c:includes('admonition-title') then
    -- Consumed by the enclosing admonition below.
    return nil
  elseif c:includes('chapter-break') then
    -- A new page on screen, a right-hand page in print; style.typ decides.
    return raw('#chapter-break()')
  elseif c:includes('part-contents') then
    return raw('#part-contents()')
  elseif c:includes('keep-with-next') then
    -- A short lead line under a heading: it stays with the block after it, so
    -- heading and line do not sit alone at the foot of a page.
    return wrap('#keep-with-next[', el.content, ']')
  elseif c:includes('operator-fields') then
    return wrap('#operator-fields[', el.content, ']')
  elseif c:includes('part-end') then
    -- The web addresses the part cites; the print edition only.
    return raw('#part-addresses()')
  elseif c:includes('admonition') then
    local kind = 'note'
    for _, cl in ipairs(c) do
      if cl ~= 'admonition' then
        kind = cl
        break
      end
    end
    local title = 'none'
    local body = List()
    for _, b in ipairs(el.content) do
      if title == 'none' and b.t == 'Div' and b.classes:includes('admonition-title') then
        title = '[' .. typst_inlines(pandoc.utils.blocks_to_inlines(b.content)) .. ']'
      else
        body:insert(b)
      end
    end
    return wrap('#admonition(kind: ' .. typst_string(kind) .. ', title: ' .. title .. ')[', body, ']')
  elseif c:includes('tabs') then
    return wrap('#tabs[', el.content, ']')
  elseif c:includes('tab') then
    return wrap('#tab(' .. typst_string(attr(el, 'label')) .. ')[', el.content, ']')
  elseif c:includes('codeblock') then
    local columns = attr(el, 'columns')
    local fit = columns:match('^%d+$') and (', columns: ' .. columns) or ''
    return wrap('#codeblock(title: ' .. typst_string(attr(el, 'title')) .. fit .. ')[', el.content, ']')
  elseif c:includes('cards') then
    local out = List({ raw('#cards(') })
    for _, b in ipairs(el.content) do
      if b.t == 'BulletList' then
        for _, item in ipairs(b.content) do
          out:insert(raw('card['))
          out:extend(item)
          out:insert(raw('],'))
        end
      end
    end
    out:insert(raw(')'))
    return out
  end
  -- Theme wrappers (scroll containers, grids without cards): content only.
  return el.content
end

function Image(img)
  if img.classes:includes('icon') then
    img.attributes['height'] = '0.95em'
    return img
  elseif img.classes:includes('bordered') then
    return {
      pandoc.RawInline('typst', '#box(stroke: 0.5pt + ec-grey.lighten(55%))['),
      img,
      pandoc.RawInline('typst', ']'),
    }
  end
end
