// Terminal clips through ttyd (https://github.com/tsl0922/ttyd): the terminal runs as a web page,
// so it is recorded like any other page. See README.md for how to start ttyd.
const os = require('os');
const path = require('path');
const fs = require('fs');
const { sleep, env } = require('./browser');

// The default WebGL renderer of xterm.js stays blank in a headless browser: use the DOM renderer.
async function openTerminal(page, { fontSize = 18 } = {}) {
  const url = env('TTYD_URL', 'http://127.0.0.1:7681').replace(/\/$/, '');
  await page.goto(`${url}/?rendererType=dom&fontSize=${fontSize}`, { waitUntil: 'networkidle2' });
  await page.waitForSelector('.xterm-rows', { timeout: 15000 });
  await sleep(1500);
  await page.click('.xterm');
}

// The visible text of the terminal.
const screen = page => page.evaluate(() => document.querySelector('.xterm-rows').innerText);

async function waitForText(page, pattern, { timeout = 60000 } = {}) {
  const t0 = Date.now();
  while (Date.now() - t0 < timeout) {
    if (pattern.test(await screen(page))) return;
    await sleep(500);
  }
  throw new Error('terminal did not show ' + pattern);
}

async function enter(page, text, delay) {
  await page.keyboard.type(text, { delay });
  await page.keyboard.press('Enter');
}

// Off camera: a neutral working folder, a neutral prompt and an empty screen, so that no user name,
// path or branch name is shown. Returns the folder.
async function prepare(page, { folder } = {}) {
  const dir = folder || fs.mkdtempSync(path.join(os.tmpdir(), 'demo-'));
  await enter(page, `cd '${dir}' && PROMPT='$ ' RPROMPT='' PS1='$ ' && clear`, 2);
  await sleep(1200);
  return dir;
}

// Types a command at about 12 characters per second and runs it.
async function command(page, text, { delay = 80, after = 1500 } = {}) {
  await page.keyboard.type(text, { delay });
  await sleep(600);
  await page.keyboard.press('Enter');
  await sleep(after);
}

// Hides every terminal row that shows the start screen of Claude Code: logo, version, model and plan,
// working folder and notices. Claude Code redraws its whole screen, so the rows are checked on every change;
// a row with other content is shown again.
async function hideClaudeStartScreen(page) {
  await page.evaluate(() => {
    const banner = /[\u2590\u259b\u259c\u259d\u2598]|Claude Code v\d|\u00b7 Claude (Max|Pro|Team|Enterprise)|^\s*\u258e|more notices? hidden/;
    const apply = () => {
      for (const r of document.querySelectorAll('.xterm-rows > div')) {
        r.style.visibility = banner.test(r.textContent) ? 'hidden' : '';
      }
    };
    apply();
    new MutationObserver(apply).observe(document.querySelector('.xterm-rows'), { childList: true, subtree: true, characterData: true });
  });
}

// Off camera: starts Claude Code in its default permission mode and without its shell tool, so that it
// works only through the MCP servers and the clip shows its permission prompts. Its start screen with
// account, plan and promotional notices is hidden. In a folder Claude Code has not seen, it first asks
// whether to trust the folder: this is confirmed. `env` sets environment variables for Claude Code only.
async function startClaude(page, { args = '', env = '' } = {}) {
  await enter(page, `${env} claude --permission-mode default --disallowedTools Bash ${args}`.trim(), 2);
  const ready = /\/effort|for shortcuts|Try "/;
  await waitForText(page, /trust this folder|\/effort|for shortcuts|Try "/, { timeout: 60000 });
  if (/trust this folder/.test(await screen(page))) {
    if (/\u276f\s*No/.test(await screen(page))) await page.keyboard.press('ArrowDown');
    await page.keyboard.press('Enter');
    await waitForText(page, ready, { timeout: 60000 });
  }
  await hideClaudeStartScreen(page);
  await sleep(2000);
}

// Ends Claude Code. Closing the browser alone leaves the process running under ttyd.
async function exitClaude(page) {
  await enter(page, '/exit', 2);
  await sleep(2000);
}

module.exports = { openTerminal, screen, waitForText, prepare, command, startClaude, hideClaudeStartScreen, exitClaude };
