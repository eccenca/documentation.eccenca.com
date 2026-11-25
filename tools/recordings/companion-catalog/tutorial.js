// Clips of the tutorial "Build a Companion catalog", one per step.
// The clips build on each other: clip 2 needs the catalog of clip 1, and so on.
const B = require('../lib/browser');
const BTN = { sel: 'button' };
const DIALOG = '.eccgui-dialog__wrapper';

const TEXT = {
  sl_desc: 'Finds every supplier of a hardware part, with country and price.',
  sl_sys: 'You receive the name of a hardware part.\nFind every hardware item with this name in the product data, together with its supplier, the country of the supplier and its price.\nReturn the list sorted by price, cheapest first.',
  pa_desc: 'Answers questions of the purchasing team about hardware parts, their suppliers and their prices.',
  pa_sys: 'You help the purchasing team with questions about hardware parts, their suppliers and their prices.\nLook up the data before you answer and do not guess prices.\nTo compare the suppliers of a part, start the supplier_lookup task agent.\nAnswer with a short table of part, supplier, country and price.',
  sk_desc: 'Finds the cheapest supplier of a hardware part.',
  sk_prompt: 'Find the cheapest supplier of the hardware part the user named.\nStart the supplier_lookup task agent, then name the cheapest supplier with country and price, followed by the complete list.\n\nThe user asked: {{ skill.argument }}',
};
const BASE_CATALOG = 'CMEM Base Companion Catalog (base)';
const CATALOG = 'Procurement Companion';
// Ground truth from the product data: suppliers of the parts with exactly this name.
const EXPECTED_ROWS = [6, 6];

// The input, textarea or button of the form group whose label starts with `label`.
async function field(page, label, what = 'input, textarea, button') {
  const h = await page.evaluateHandle((label, what) => {
    const ls = [...document.querySelectorAll('label, .eccgui-label, .bp6-label')].filter(l => l.getClientRects().length && (l.innerText || '').trim().startsWith(label));
    const l = ls[ls.length - 1];
    if (!l) return null;
    let c = l.parentElement;
    for (let i = 0; i < 6 && c; i++, c = c.parentElement) {
      const el = [...c.querySelectorAll(what)].find(e => e.getClientRects().length && !l.contains(e));
      if (el) return el;
    }
    return null;
  }, label, what);
  const el = h.asElement();
  if (!el) throw new Error('field not found: ' + label);
  return el;
}

async function fill(page, label, text) {
  await B.click(page, await field(page, label, 'input, textarea'), { after: 300 });
  await B.type(page, text);
}

// Clicks an entry of an open popover menu or list box by its text.
async function option(page, text, o = {}) {
  const el = await B.find(page, text, { sel: '.bp6-popover-content .bp6-menu-item, .bp6-popover-content li, [role=option], [role=menuitem]', partial: o.partial, timeout: 20000 });
  await B.click(page, el, { after: o.after ?? 900 });
}

// Blueprint multiselects keep the typed query after a selection. Clearing it with Backspace would
// delete the selected tags, so the query is selected and deleted only when it is not empty.
async function multiselect(page, label, text, opt) {
  const el = await field(page, label, 'input');
  await B.click(page, el, { after: 500 });
  await B.type(page, text, { after: 1200 });
  await option(page, opt, { partial: true });
  if (await el.evaluate(e => e.value.length)) { await el.evaluate(e => e.select()); await page.keyboard.press('Delete'); }
  await page.keyboard.press('Escape'); await B.sleep(500);
}

async function scrollTo(page, el) {
  await el.evaluate(e => e.scrollIntoView({ behavior: 'smooth', block: 'center' }));
  await B.sleep(900);
}

// /default/<module>: /explore redirects to the default application view of an installed package.
async function openCompanion(page) {
  await B.go(page, '/default/companion');
  await B.sleep(3500);
}

async function selectCatalog(page) {
  const already = await page.evaluate(t => [...document.querySelectorAll('button')].some(b => b.getClientRects().length && b.innerText.trim() === t), CATALOG);
  if (already) { await B.sleep(800); return; }
  await B.click(page, BASE_CATALOG, BTN);
  await option(page, CATALOG);
}

const save = page => B.click(page, 'Save changes', { ...BTN, partial: true, after: 3000 });

async function addAgent(page, kind, id, desc, model, sys, taskAgent) {
  await B.click(page, 'Add a new agent', { ...BTN, after: 1000 });
  await B.click(page, kind, { ...BTN, within: DIALOG });
  await fill(page, 'Identifier', id);
  await B.click(page, 'Create', { ...BTN, within: DIALOG, after: 2500 });
  await fill(page, 'Description', desc);
  await B.click(page, 'Pick a named model', { ...BTN, after: 800 });
  await option(page, model);
  await fill(page, 'System message', sys);
  await scrollTo(page, await B.find(page, 'Add filter entry', BTN));
  await B.click(page, 'Add filter entry', { ...BTN, after: 1200 });
  await multiselect(page, 'Servers', 'cmem_explore', 'cmem_explore');
  await B.click(page, 'Read-only: any', { partial: true, after: 1500 });
  if (taskAgent) {
    await scrollTo(page, await field(page, 'Task agents', 'input'));
    await multiselect(page, 'Task agents', 'supplier', taskAgent);
  }
  await scrollTo(page, await field(page, 'Focus graphs', 'input'));
  await multiselect(page, 'Focus graphs', 'http://ld.company.org/prod-inst/', 'Add new item');
  await B.sleep(1200);
  await save(page);
}

// Waits until the chat stops changing for 6 seconds (at most 4 minutes), then counts the rows of the
// last table in the answer.
let rows = [];
async function waitAnswer(page) {
  let last = '', same = 0;
  for (let i = 0; i < 240 && same < 6; i++) {
    await B.sleep(1000);
    const t = await page.evaluate(() => document.body.innerText.length + ':' + !!document.querySelector('[class*=spinner], [class*=loading]'));
    if (t === last && !t.endsWith('true')) same++; else same = 0;
    last = t;
  }
  await B.sleep(1500);
  rows.push(await page.evaluate(() => { const t = [...document.querySelectorAll('table')].pop(); return t ? t.querySelectorAll('tbody tr').length : -1; }));
}

module.exports = {
  docs: 'docs/explore-and-author/companion/build-a-companion-catalog',
  prefix: 'companion-tutorial-',

  setup: openCompanion,

  async beforeClip(page, n, first) {
    // off camera: a fresh page before the clips that start from another module state
    if (n === 2 || n === 5 || n === 6) await openCompanion(page);
    if (first && (n === 3 || n === 4)) {
      await B.click(page, 'Catalog', BTN); await B.click(page, 'Agents', BTN); await selectCatalog(page);
    }
  },

  clips: [
    {
      name: 'create-catalog',
      async run(page) {
        await B.click(page, 'Catalog', BTN);
        await B.click(page, 'Catalogs', BTN);
        await B.click(page, 'Add a new catalog', { ...BTN, after: 1000 });
        await fill(page, 'Graph', 'https://ns.eccenca.com/data/companion/procurement/');
        // the label is prefilled from the graph IRI: select it and type over it
        const label = await field(page, 'Label', 'input');
        await B.click(page, label, { after: 300 });
        await label.evaluate(e => e.select()); await B.sleep(400);
        await B.type(page, CATALOG);
        await B.sleep(500);
        await B.click(page, 'Create', { ...BTN, within: DIALOG, after: 3000 });
        const b = await (await B.find(page, CATALOG)).boundingBox();
        await B.glide(page, b.x + b.width / 2, b.y + b.height / 2); await B.sleep(2500);
      },
      // the dialog stays open with an error when the catalog graph already exists
      check: async page => (await page.$(DIALOG)) ? 'the dialog Create a companion catalog is still open' : null,
    },
    {
      name: 'create-task-agent',
      async run(page) {
        await B.click(page, 'Catalog', BTN);
        await B.click(page, 'Agents', { ...BTN, after: 1500 });
        await selectCatalog(page);
        await addAgent(page, 'Task agents', 'supplier_lookup', TEXT.sl_desc, 'fast', TEXT.sl_sys);
      },
    },
    {
      name: 'create-interactive-agent',
      async run(page) {
        await addAgent(page, 'Interactive agents', 'procurement_advisor', TEXT.pa_desc, 'default', TEXT.pa_sys, 'supplier_lookup');
      },
    },
    {
      name: 'create-skill',
      async run(page) {
        await page.evaluate(() => window.scrollTo({ top: 0, behavior: 'smooth' })); await B.sleep(800);
        await B.click(page, 'Skills', { ...BTN, after: 1500 });
        await selectCatalog(page);
        await B.click(page, 'Add a new skill', { ...BTN, after: 1000 });
        await fill(page, 'Identifier', 'cheapest_supplier');
        await B.click(page, 'Create', { ...BTN, within: DIALOG, after: 2500 });
        await fill(page, 'Description', TEXT.sk_desc);
        await fill(page, 'Prompt', TEXT.sk_prompt);
        await B.sleep(800);
        await save(page);
      },
    },
    {
      name: 'agent-network',
      async run(page) {
        await B.click(page, 'Agent network', { ...BTN, after: 2000 });
        await B.click(page, 'By catalog', { ...BTN, after: 2500 });
        // scrollIntoView on a control at the bottom would scroll the whole page
        await B.click(page, 'Fit View', { ...BTN, noScroll: true, after: 1800 });
        // the mouse wheel does not zoom in a headless browser: use the + control
        const zoomIn = await page.$('.react-flow__controls-zoomin');
        for (let i = 0; i < 3; i++) await B.click(page, zoomIn, { noScroll: true, hover: 300, after: 700 });
        await B.sleep(800);
        // drag an empty spot of the canvas so that the group of the catalog moves to the middle
        const p = await page.evaluate(name => {
          const n = [...document.querySelectorAll('.react-flow__node')].find(n => n.className.includes('group') && n.innerText.trim().startsWith(name));
          const r = n.getBoundingClientRect(), f = document.querySelector('.react-flow').getBoundingClientRect();
          const dx = (f.x + f.width / 2) - (r.x + r.width / 2), dy = (f.y + f.height / 2) - (r.y + r.height / 2);
          for (let y = f.y + 20; y < f.bottom - 20; y += 15) for (let x = f.x + 60; x < f.right - 20; x += 15) {
            const e = document.elementFromPoint(x, y);
            if (e && e.classList.contains('react-flow__pane') && x + dx > 0 && y + dy > 0) return { x, y, dx, dy };
          }
          return null;
        }, CATALOG);
        if (p) {
          await B.glide(page, p.x, p.y); await B.sleep(400);
          await page.mouse.down(); await B.glide(page, p.x + p.dx, p.y + p.dy, 1100); await page.mouse.up();
          await B.sleep(1200);
        }
        const node = await page.evaluateHandle(() => [...document.querySelectorAll('.react-flow__node')].find(n => n.className.includes('agent') && n.innerText.includes('Procurement Advisor')));
        await B.click(page, node.asElement(), { after: 4000 });
      },
    },
    {
      name: 'ask-companion',
      keep: 3, tail: 5,
      // the answers of the language model vary: record again until both lists are complete and correct
      retries: 4,
      async run(page) {
        rows = [];
        await B.click(page, 'Chat with the companion', { ...BTN, after: 2500 });
        await B.click(page, 'New chat', { ...BTN, after: 1500 });
        await B.click(page, 'Ask the companion', { sel: 'textarea', after: 400 });
        await B.type(page, 'Who supplies the Resonator Transformer, and which supplier is cheapest?');
        await page.keyboard.press('Enter');
        await waitAnswer(page);
        await B.click(page, 'New chat', { ...BTN, after: 1500 });
        await B.click(page, 'Ask the companion', { sel: 'textarea', after: 400 });
        await B.type(page, '/', { after: 1200 });
        await B.click(page, '/cheapest_supplier', { after: 900 });
        await B.type(page, 'Multiplexer Transistor');
        await page.keyboard.press('Enter');
        await waitAnswer(page);
      },
      async check() {
        return rows.join() === EXPECTED_ROWS.join() ? null : `answer rows ${rows.join('/')}, expected ${EXPECTED_ROWS.join('/')}`;
      },
    },
  ],
};
