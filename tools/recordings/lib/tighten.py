"""Shorten still pauses of a screen recording and encode it as VP9 WebM (BT.709).
Typing is protected: a stretch with frequent small changes (several per second) is never cut,
even when the coarse freeze detection sees it as still.
Pace rule: about 3 s of stillness at the start, still pauses shortened to `keep` seconds (2.5),
about `tail` seconds (4) on the result at the end.
usage: python3 tighten.py in.webm out.webm [keep=2.5] [tail=4]
ffmpeg and ffprobe come from FFMPEG_PATH (default: ffmpeg on the PATH)."""
import os, re, subprocess, sys

FFMPEG = os.environ.get('FFMPEG_PATH', 'ffmpeg')
FFPROBE = os.path.join(os.path.dirname(FFMPEG), 'ffprobe') if os.path.dirname(FFMPEG) else 'ffprobe'

src, dst = sys.argv[1], sys.argv[2]
keep = float(sys.argv[3]) if len(sys.argv) > 3 else 2.5
tail = float(sys.argv[4]) if len(sys.argv) > 4 else 4.0
START = 3.0

def dur(f):
    return float(subprocess.run([FFPROBE, '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f],
                                capture_output=True, text=True).stdout.strip())

cfr = dst + '.cfr.mkv'
subprocess.run([FFMPEG, '-v', 'error', '-y', '-i', src, '-vf', 'fps=25', '-c:v', 'libx264', '-qp', '0', '-preset', 'ultrafast', cfr], check=True)
total = dur(cfr)

# coarse stills
log = subprocess.run([FFMPEG, '-i', cfr, '-vf', 'freezedetect=n=0.001:d=1.4', '-map', '0:v', '-f', 'null', '-'],
                     capture_output=True, text=True).stderr
starts = [float(x) for x in re.findall(r'freeze_start: ([0-9.]+)', log)]
ends = [float(x) for x in re.findall(r'freeze_end: ([0-9.]+)', log)]
if len(ends) < len(starts):
    ends.append(total)

# frames that differ from the previous kept frame by more than encoding noise (a typed character counts)
log = subprocess.run([FFMPEG, '-i', cfr, '-vf', 'mpdecimate=hi=2000:lo=1000:frac=0,showinfo', '-map', '0:v', '-f', 'null', '-'],
                     capture_output=True, text=True).stderr
changes = [float(x) for x in re.findall(r'pts_time:\s*([0-9.]+)', log)]

# active: at least 4 changes within a 1 s window (typing ~12/s, caret blink ~2/s)
active = []
for i, t in enumerate(changes):
    j = i
    while j < len(changes) and changes[j] - t <= 1.0:
        j += 1
    if j - i >= 4:
        a, b = t - 0.3, changes[j - 1] + 0.3
        if active and a <= active[-1][1]:
            active[-1][1] = max(active[-1][1], b)
        else:
            active.append([a, b])

def minus(a, b, holes):
    """[a, b) without the active intervals"""
    out, cur = [], a
    for h0, h1 in holes:
        if h1 <= cur or h0 >= b:
            continue
        if h0 > cur:
            out.append((cur, h0))
        cur = max(cur, h1)
    if cur < b:
        out.append((cur, b))
    return out

cuts = []
for s, e in zip(starts, ends):
    k = tail if e >= total - 0.05 else (START if s < 0.05 else keep)
    if e - s > k + 0.2:
        cuts += [c for c in minus(s + k, e, active) if c[1] - c[0] > 0.2]

# strict stills: nothing moves at all (no typing, no pointer), so they are safe to shorten
log = subprocess.run([FFMPEG, '-i', cfr, '-vf', 'freezedetect=n=0.0002:d=2.6', '-map', '0:v', '-f', 'null', '-'],
                     capture_output=True, text=True).stderr
s2 = [float(x) for x in re.findall(r'freeze_start: ([0-9.]+)', log)]
e2 = [float(x) for x in re.findall(r'freeze_end: ([0-9.]+)', log)]
if len(e2) < len(s2):
    e2.append(total)
for s, e in zip(s2, e2):
    k = tail if e >= total - 0.05 else (START if s < 0.05 else keep)
    if e - s > k + 0.2:
        cuts.append((s + k, e))

expr = '+'.join(f'between(t,{a:.3f},{b:.3f})' for a, b in cuts) or '0'
vf = (f"select='not({expr})',setpts=N/25/TB,"
      "scale=out_color_matrix=bt709:out_range=tv,format=yuv420p")
subprocess.run([FFMPEG, '-v', 'error', '-y', '-i', cfr, '-vf', vf, '-r', '25',
                '-c:v', 'libvpx-vp9', '-crf', '36', '-b:v', '0', '-row-mt', '1',
                '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', '-color_range', 'tv',
                '-an', dst], check=True)
os.remove(cfr)
print(f'{src}: {total:.1f}s -> {dur(dst):.1f}s, {len(cuts)} cuts, {len(active)} protected stretches')
