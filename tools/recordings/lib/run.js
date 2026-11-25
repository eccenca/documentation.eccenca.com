// Records the clips of one tutorial.
// usage: node lib/run.js <tutorial> [--clips 2,3] [--dry] [--install]
//   --clips    record only these clips (numbers from 1); the test data is reset only when the first clip is included
//   --dry      run the steps without recording and save a screenshot of the end of each clip
//   --install  copy the finished clips and posters into the documentation folder of the tutorial
// Results go to dist/recordings/<tutorial>/.
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');
const B = require('./browser');

const ROOT = path.resolve(__dirname, '../../..');

function args() {
  const a = process.argv.slice(2), o = { tutorial: a[0], dry: a.includes('--dry'), install: a.includes('--install') };
  const i = a.indexOf('--clips');
  if (i >= 0) o.clips = a[i + 1].split(',').map(Number);
  if (!o.tutorial || o.tutorial.startsWith('--')) {
    console.error('usage: node lib/run.js <tutorial> [--clips 2,3] [--dry] [--install]');
    process.exit(2);
  }
  return o;
}

function ffmpeg(...a) {
  execFileSync(B.env('FFMPEG_PATH', 'ffmpeg'), ['-v', 'error', '-y', ...a], { stdio: 'inherit' });
}

(async () => {
  const o = args();
  const dir = path.join(__dirname, '..', o.tutorial);
  const t = require(path.join(dir, 'tutorial.js'));
  const numbers = o.clips || t.clips.map((_, i) => i + 1);
  const out = path.join(ROOT, 'dist', 'recordings', o.tutorial);
  fs.mkdirSync(path.join(out, 'raw'), { recursive: true });

  if (numbers[0] === 1 && fs.existsSync(path.join(dir, 'reset.sh'))) {
    console.log('reset test data');
    execFileSync('bash', [path.join(dir, 'reset.sh')], { stdio: 'inherit' });
  }

  const { browser, page } = await B.open(t.viewport || {});
  let failed = false;
  try {
    if (t.setup) await t.setup(page);
    for (const n of numbers) {
      const clip = t.clips[n - 1];
      const raw = path.join(out, 'raw', `${clip.name}.webm`);
      for (let attempt = 1; ; attempt++) {
        console.log(`clip ${n} ${clip.name}` + (attempt > 1 ? ` (attempt ${attempt})` : ''));
        if (t.beforeClip) await t.beforeClip(page, n, n === numbers[0]);
        if (o.dry) await clip.run(page);
        else await B.record(page, raw, () => clip.run(page));
        await page.screenshot({ path: path.join(out, 'raw', `${clip.name}.end.png`) });
        const problem = clip.check ? await clip.check(page) : null;
        if (!problem) break;
        console.log(`  check failed: ${problem}`);
        if (attempt > (clip.retries || 0)) { failed = true; break; }
      }
      if (failed) break;
    }
  } catch (e) {
    failed = true;
    console.error('FAILED:', e.message);
    await page.screenshot({ path: path.join(out, 'raw', 'failure.png') }).catch(() => {});
  } finally {
    if (t.teardown) await t.teardown(page).catch(() => {});
    await browser.close();
  }
  if (failed) process.exit(1);
  if (o.dry) return console.log(`dry run done, end screenshots in ${path.relative(ROOT, out)}/raw/`);

  for (const n of numbers) {
    const clip = t.clips[n - 1];
    const name = `${t.prefix}${clip.name}`, video = path.join(out, `${name}.webm`);
    execFileSync('python3', [path.join(__dirname, 'tighten.py'), path.join(out, 'raw', `${clip.name}.webm`), video,
      String(clip.keep ?? 2.5), String(clip.tail ?? 4)], { stdio: 'inherit' });
    // the poster is the last frame: the result of the step
    ffmpeg('-sseof', '-0.2', '-i', video, '-frames:v', '1', '-update', '1', path.join(out, `${name}.png`));
    if (o.install) {
      for (const ext of ['webm', 'png']) fs.copyFileSync(path.join(out, `${name}.${ext}`), path.join(ROOT, t.docs, `${name}.${ext}`));
    }
  }
  console.log(`clips in ${path.relative(ROOT, out)}/` + (o.install ? `, copied to ${t.docs}/` : ''));
})().catch(e => { console.error(e); process.exit(1); });
