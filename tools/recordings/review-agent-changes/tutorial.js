// Clips of the tutorial "Review the changes of an AI agent", tab "External agent", one per step.
// Claude Code works in a terminal served by ttyd (see ../README.md, "Terminal clips"); the review is done in
// the browser. The clips build on each other: clip 5 continues the conversation of clip 1.
//
// The agent chooses the properties itself. Clip 1 is recorded again until it maps price to schema:price and
// supplier to schema:manufacturer, the run that the tutorial describes. Clip 5 is checked as well: an answer that
// claims the reverted rule was written is wrong. A wrong clip 5 cannot be recorded again on its own, since
// the workflow has run by then: record all clips again.
//
// Besides the clips, the run takes the three screenshots of the tutorial, at 2x, into
// dist/recordings/review-agent-changes/. --install copies only clips and posters: copy the screenshots by hand.
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');
const B = require('../lib/browser');
const T = require('../lib/terminal');

const DOCS = 'docs/build/review-agent-changes';
const OUT = path.resolve(__dirname, '../../../dist/recordings/review-agent-changes');
const PROJECT = '/dataintegration/workbench/projects/product-feed';
const API = '/dataintegration/api/workspace/projects/product-feed/changes';
const BTN = { sel: 'button' };
const DIALOG = '.eccgui-dialog__wrapper';
// Claude Code keeps its MCP servers and conversations per folder.
const FOLDER = '/tmp/product-feed';
// The read-only tools of the Build MCP server need no permission prompt: the clip shows only the prompts
// of the tools that change something.
const ALLOWED = fs.readFileSync(path.join(__dirname, 'allowed.txt'), 'utf8').trim().split('\n');
const PROMPT1 = 'In the project Product Feed, map the columns price and supplier of products.csv in the transformation Transform products to schema.org properties. Choose the properties yourself. Then run the workflow Load products.';
const PROMPT5 = 'The review is done: I reverted the supplier mapping and marked the other changes as reviewed. Run the workflow Load products again.';

const token = () => execFileSync('cmemc', ['admin', 'token']).toString().trim();
const changes = () => execFileSync('curl', ['-sf', '-H', 'Accept: application/json', '-H', `Authorization: Bearer ${token()}`, B.BASE() + API]).toString();

// Registers the Build MCP server for the folder with a fresh token: a token of the test instance lives
// only a few minutes, so this runs before each conversation.
function connectMcp() {
  fs.mkdirSync(FOLDER, { recursive: true });
  execFileSync('bash', ['-c', 'claude mcp remove cmem-build >/dev/null 2>&1 || true'], { cwd: FOLDER });
  execFileSync('claude', ['mcp', 'add', '--transport', 'http', 'cmem-build', `${B.BASE()}/dataintegration/mcp`,
    '--header', `Authorization: Bearer ${token()}`], { cwd: FOLDER, stdio: 'ignore' });
}

// Off camera: the terminal with Claude Code, ready for the prompt. The drawn pointer is hidden, since
// nothing is clicked in the terminal.
async function openClaude(page, args = '') {
  connectMcp();
  await T.openTerminal(page);
  await page.evaluate(() => { const c = document.getElementById('__cur'); if (c) c.style.display = 'none'; });
  await T.prepare(page, { folder: FOLDER });
  await T.startClaude(page, { allowed: ALLOWED, disallowed: ['AskUserQuestion'], args });
}

// Sends a prompt and answers each permission prompt with Yes, after a pause to read it.
// Returns when Claude Code has been idle for about 6 seconds.
async function converse(page, prompt) {
  await B.type(page, prompt);
  await B.sleep(600);
  await page.keyboard.press('Enter');
  let idle = 0;
  for (let i = 0; i < 300 && idle < 4; i++) {
    await B.sleep(1500);
    const s = await T.screen(page);
    if (/Do you want to proceed\?/.test(s)) { await B.sleep(2500); await page.keyboard.press('Enter'); idle = 0; continue; }
    if (/esc to interrupt|…/.test(s.split('\n').slice(-12).join('\n'))) idle = 0; else idle++;
  }
}

// Saves the terminal text for the check and ends Claude Code.
async function closeClaude(page, name) {
  const s = await T.screen(page);
  fs.writeFileSync(path.join(OUT, 'raw', `${name}.screen.txt`), s);
  await T.exitClaude(page);
  return s;
}

// The 2x screenshots, in a browser of their own without the drawn pointer.
async function screenshots(take) {
  const { browser, page } = await B.open({ width: 1384, height: 900, scale: 2, pointer: false });
  const settle = async () => {
    await page.evaluate(() => document.activeElement && document.activeElement.blur());
    await page.mouse.move(1300, 880); await B.sleep(900);
  };
  try { await take(page, settle); } finally { await browser.close(); }
}

// The Changes card of the project overview.
const changesCard = page => page.evaluate(() => {
  const h = [...document.querySelectorAll('*')].find(e => e.childElementCount === 0 && e.innerText && e.innerText.trim() === 'Changes');
  let c = h; while (c && !(c.getBoundingClientRect().height > 80 && /Review changes/.test(c.innerText))) c = c.parentElement;
  const r = c.getBoundingClientRect(); return { x: r.x, y: r.y, width: r.width, height: r.height };
});

let attempts1 = 0;

module.exports = {
  docs: DOCS,
  prefix: 'review-agent-changes-',
  async beforeClip(page, n) {
    // run.js runs reset.sh before the first attempt; each further attempt of clip 1 needs a fresh project
    if (n === 1 && attempts1++) execFileSync('bash', [path.join(__dirname, 'reset.sh')], { stdio: 'inherit' });
    if (n === 1) await openClaude(page);
    if (n === 2) { await B.go(page, PROJECT); await B.sleep(3000); }
    if (n === 5) await openClaude(page, '--continue');
  },
  clips: [
    {
      // 1 the agent changes the project and requests the run
      name: 'agent-changes', keep: 3, tail: 5, retries: 5,
      run: page => converse(page, PROMPT1),
      async check(page) {
        await closeClaude(page, 'agent-changes');
        // each summary appears more than once in the response: compare distinct summaries
        const j = changes();
        const added = [...new Set(j.match(/Added (value|object) mapping '[^']+' \([^)]*\)/g) || [])];
        const ok = added.length === 2 && added.some(a => /\(price → https:\/\/schema\.org\/price\)/.test(a))
          && added.some(a => /\(supplier → https:\/\/schema\.org\/manufacturer\)/.test(a))
          && /Proposed to run workflow 'Load products'/.test(j);
        if (!ok) return 'changes: ' + (added.join(' | ') || 'none');
        await screenshots(async (p, settle) => {
          await B.go(p, PROJECT); await B.sleep(4000); await settle();
          const c = await changesCard(p);
          await p.screenshot({ path: path.join(OUT, 'review-agent-changes-card.png'), clip: { x: c.x - 8, y: c.y - 8, width: c.width + 16, height: c.height + 16 } });
          await B.go(p, `${PROJECT}/changes?f_ids=changeState&types=keyword&f_keys=unreviewed`); await B.sleep(4500); await settle();
          await p.screenshot({ path: path.join(OUT, 'review-agent-changes-unreviewed.png'), clip: { x: 56, y: 56, width: 910, height: 440 } });
        });
        return null;
      },
    },
    {
      // 2 open the review and list only the changes of the agent
      name: 'open-review',
      async run(page) {
        const c = await changesCard(page);
        await B.glide(page, c.x + c.width / 2, c.y + c.height / 2); await B.sleep(2000);
        await B.click(page, 'Review changes', { after: 3500 });
        await B.click(page, 'mcp:claude-code', { partial: true, after: 3000 });
      },
    },
    {
      // 3 revert the rule that maps the column supplier
      name: 'revert-change',
      async run(page) {
        const btn = await page.evaluateHandle(() => {
          const r = [...document.querySelectorAll('tr')].find(r => /Added value mapping '[^']+' \(supplier/.test(r.innerText));
          const b = [...r.querySelectorAll('button')]; return b[b.length - 1];
        });
        await B.click(page, btn.asElement(), { after: 1200 });
        await B.click(page, 'Revert this change', { after: 1800 });
        await B.click(page, 'Revert', { ...BTN, within: DIALOG, after: 3500 });
      },
    },
    {
      // 4 mark the remaining changes as reviewed
      name: 'mark-reviewed',
      async run(page) {
        await B.click(page, 'Mark all as reviewed', { ...BTN, after: 2500 });
        await B.click(page, 'Confirm', { ...BTN, within: DIALOG, after: 3500 });
      },
    },
    {
      // 5 the agent runs the workflow, in the conversation of clip 1
      name: 'agent-runs-workflow', keep: 3, tail: 5,
      run: page => converse(page, PROMPT5),
      async check(page) {
        const s = await closeClaude(page, 'agent-runs-workflow');
        if (!/Executed workflow 'Load products'/.test(changes())) return 'no executed workflow in the change journal';
        // manufacturer may come up only together with the revert, never as a property that was written
        const answer = s.slice(s.lastIndexOf('Run the workflow Load products again.'));
        if (/manufacturer/i.test(answer) && !/revert|removed|not (in|written|included|part)|no longer|only the price/i.test(answer)) {
          return 'the answer claims manufacturer: ' + answer.replace(/\s+/g, ' ').slice(0, 300);
        }
        await screenshots(async (p, settle) => {
          await B.go(p, `${PROJECT}/changes`); await B.sleep(4500); await settle();
          await p.screenshot({ path: path.join(OUT, 'review-agent-changes-after-run.png'), clip: { x: 56, y: 56, width: 910, height: 520 } });
        });
        return null;
      },
    },
  ],
};
