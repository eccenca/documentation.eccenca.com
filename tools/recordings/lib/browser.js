// Shared building blocks for scripted screen recordings: browser, sign-in, drawn pointer,
// clicking, typing and recording. Configuration comes from environment variables, see README.md.
const fs = require('fs');
const puppeteer = require('puppeteer-core');

const sleep = ms => new Promise(r => setTimeout(r, ms));

function env(name, fallback) {
  const v = process.env[name];
  if (v) return v;
  if (fallback !== undefined) return fallback;
  throw new Error(`Environment variable ${name} is not set, see tools/recordings/README.md`);
}

const BASE = () => env('CMEM_BASE_URI').replace(/\/$/, '');

// Chrome or Chromium: CHROME_PATH, otherwise the usual install locations.
function chromePath() {
  if (process.env.CHROME_PATH) return process.env.CHROME_PATH;
  const known = [
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '/Applications/Chromium.app/Contents/MacOS/Chromium',
    '/usr/bin/google-chrome', '/usr/bin/google-chrome-stable', '/usr/bin/chromium', '/usr/bin/chromium-browser',
  ];
  const found = known.find(p => fs.existsSync(p));
  if (!found) throw new Error('No Chrome found, set CHROME_PATH');
  return found;
}

// Drawn mouse pointer plus click marker: a headless browser shows no pointer.
const POINTER = () => {
  const add = () => {
    if (document.getElementById('__cur')) return;
    const c = document.createElement('div'); c.id = '__cur';
    c.innerHTML = '<svg width="22" height="22" viewBox="0 0 22 22"><path d="M2 1 L2 17 L6.5 13 L9.5 20 L12.5 18.7 L9.5 12 L15.5 12 Z" fill="#111" stroke="#fff" stroke-width="1.4" stroke-linejoin="round"/></svg>';
    Object.assign(c.style, { position: 'fixed', left: '0', top: '0', width: '22px', height: '22px', zIndex: 2147483647, pointerEvents: 'none', transform: 'translate(-2px,-1px)' });
    document.documentElement.appendChild(c);
    const pos = window.__curPos || { x: -50, y: -50 };
    c.style.left = pos.x + 'px'; c.style.top = pos.y + 'px';
    document.addEventListener('mousemove', e => { window.__curPos = { x: e.clientX, y: e.clientY }; c.style.left = e.clientX + 'px'; c.style.top = e.clientY + 'px'; }, true);
    document.addEventListener('mousedown', e => {
      const r = document.createElement('div');
      Object.assign(r.style, { position: 'fixed', left: (e.clientX - 14) + 'px', top: (e.clientY - 14) + 'px', width: '28px', height: '28px', borderRadius: '50%', background: 'rgba(240,120,0,.35)', border: '2px solid rgba(240,120,0,.9)', zIndex: 2147483646, pointerEvents: 'none', transition: 'transform .45s ease-out, opacity .45s ease-out' });
      document.documentElement.appendChild(r);
      requestAnimationFrame(() => { r.style.transform = 'scale(1.7)'; r.style.opacity = '0'; });
      setTimeout(() => r.remove(), 600);
    }, true);
  };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', add); else add();
};

// The warning about the fallback admin group of a test instance is not part of any product flow.
// Only its fixed-position container is hidden; hiding a larger ancestor hides the whole application.
const HIDE_FALLBACK_ADMIN_WARNING = () => {
  const hide = () => {
    const w = document.createTreeWalker(document.body || document, NodeFilter.SHOW_TEXT);
    let t; while ((t = w.nextNode())) {
      if (!/fallback admin group/.test(t.nodeValue)) continue;
      let c = t.parentElement;
      for (let i = 0; i < 12 && c && c !== document.body; i++, c = c.parentElement) {
        if (getComputedStyle(c).position === 'fixed') { c.style.visibility = 'hidden'; break; }
      }
    }
  };
  new MutationObserver(hide).observe(document, { childList: true, subtree: true });
};

// Opens a headless browser in US English. The recording has the CSS size of the viewport (1280x800).
async function open({ width = 1280, height = 800, scale = 1.125, pointer = true } = {}) {
  const browser = await puppeteer.launch({
    executablePath: chromePath(), headless: true,
    args: ['--lang=en-US', '--hide-scrollbars'],
    defaultViewport: { width, height, deviceScaleFactor: scale },
  });
  const page = await browser.newPage();
  await page.setExtraHTTPHeaders({ 'Accept-Language': 'en-US,en;q=0.9' });
  await page.evaluateOnNewDocument(() => {
    Object.defineProperty(navigator, 'language', { get: () => 'en-US' });
    Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] });
  });
  const cdp = await page.createCDPSession();
  await cdp.send('Emulation.setLocaleOverride', { locale: 'en-US' });
  if (pointer) await page.evaluateOnNewDocument(POINTER);
  await page.evaluateOnNewDocument(HIDE_FALLBACK_ADMIN_WARNING);
  return { browser, page };
}

// Opens a path of the deployment and signs in on the way if needed (OAUTH_USER, OAUTH_PASSWORD).
async function go(page, url) {
  for (let i = 0; i < 4; i++) {
    await page.goto(url.startsWith('http') ? url : BASE() + url, { waitUntil: 'networkidle2', timeout: 90000 });
    if (await page.$('#username')) {
      await page.type('#username', env('OAUTH_USER')); await page.type('#password', env('OAUTH_PASSWORD'));
      await Promise.all([page.waitForNavigation({ waitUntil: 'networkidle2', timeout: 90000 }), page.click('#kc-login')]);
      continue;
    }
    return;
  }
}

// Finds a visible element by exact text, aria-label, title or placeholder (innermost, last match wins),
// or by CSS with the prefix "css:". Options: sel (candidate selector), within, partial, timeout.
async function find(page, target, { within, timeout = 15000, partial = false, sel } = {}) {
  const t0 = Date.now();
  while (Date.now() - t0 < timeout) {
    const h = await page.evaluateHandle((t, within, partial, tags) => {
      const root = within ? document.querySelector(within) : document;
      if (!root) return null;
      if (t.startsWith('css:')) { const all = [...root.querySelectorAll(t.slice(4))].filter(e => e.getClientRects().length); return all[0] || null; }
      const s = tags || 'button, a, [role=tab], [role=menuitem], [role=option], li, span, div, label, h1, h2, h3, h4, input, textarea, p, td';
      const m = x => partial ? x.includes(t) : x === t;
      const c = [...root.querySelectorAll(s)].filter(e => {
        if (!e.getClientRects().length) return false;
        return [(e.getAttribute('aria-label') || ''), (e.getAttribute('title') || ''), (e.getAttribute('placeholder') || ''), (e.innerText || '')].map(x => x.trim()).some(m);
      });
      const inner = c.filter(e => !c.some(o => o !== e && e.contains(o)));
      return inner[inner.length - 1] || null;
    }, target, within, partial, sel);
    const el = h.asElement();
    if (el) return el;
    await sleep(300);
  }
  throw new Error('not found: ' + target);
}

// Visible, eased pointer movement, about 1 second by default (pace rule).
let POS = { x: 640, y: 400 };
async function glide(page, x, y, ms = 1000) {
  const n = 28, from = { ...POS };
  for (let i = 1; i <= n; i++) {
    const t = i / n, e = t < .5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2;
    await page.mouse.move(from.x + (x - from.x) * e, from.y + (y - from.y) * e);
    await sleep(ms / n);
  }
  POS = { x, y };
}

// Moves the pointer to an element, rests (hover, 0.6 s), clicks and waits (after, at least 1.5 s).
// Options as for find, plus noScroll, dx, dy, hover, after.
async function click(page, target, opts = {}) {
  const el = typeof target === 'string' ? await find(page, target, opts) : target;
  if (!opts.noScroll) await el.evaluate(e => e.scrollIntoView({ block: 'nearest', inline: 'nearest' }));
  await sleep(150);
  const b = await el.boundingBox();
  if (!b) throw new Error('no box: ' + target);
  await glide(page, b.x + (opts.dx ?? b.width / 2), b.y + (opts.dy ?? b.height / 2));
  await sleep(opts.hover ?? 600);
  await page.mouse.down(); await sleep(80); await page.mouse.up();
  await sleep(Math.max(opts.after ?? 700, 1500));
  return el;
}

// Pace rule: about 12 characters per second; a text of more than 100 characters at about
// 100 characters per second, followed by a pause of 0.65 seconds.
const LONG_TEXT = 100;
function typingDelay(text, delay) {
  return text.length > LONG_TEXT ? 10 : (delay ?? 80);
}

// Types a text. Line breaks are entered with Shift+Enter, so that a chat input does not send.
async function type(page, text, { delay, after } = {}) {
  const long = text.length > LONG_TEXT, d = typingDelay(text, delay);
  const lines = text.split('\n');
  for (let i = 0; i < lines.length; i++) {
    if (lines[i]) await page.keyboard.type(lines[i], { delay: d });
    if (i < lines.length - 1) { await page.keyboard.down('Shift'); await page.keyboard.press('Enter'); await page.keyboard.up('Shift'); }
  }
  await sleep(long ? 650 : (after ?? 400));
}

// Records what fn does: about 3 seconds of stillness before, about 4 seconds on the result after.
async function record(page, file, fn) {
  const rec = await page.screencast({ path: file, ffmpegPath: env('FFMPEG_PATH', 'ffmpeg') });
  try { await sleep(3500); await fn(); await sleep(4000); } finally { await rec.stop(); }
}

module.exports = { sleep, env, BASE, open, go, find, glide, click, type, typingDelay, record };
