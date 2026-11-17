"""Song 7 bed — measure it against prereg v2, and prove the instruments first.

Prereg v2 wrote six falsifiers. One of them (5, "monotonic fall of RMS across
the final 1.5 s") was written to catch a fade, but any string that rings and is
then cut also falls monotonically across its last 1.5 s. It cannot tell decay
from taper. So it is reported as measured, and a seventh instrument is added to
do the job it was meant to do: the STEP TEST, which asks whether the last
sample before silence is a discontinuity or the continuation of the decay.

Every number here is computed on synthetic files in the same run first:
  hardcut:  sine ring, level cut to exact zero at -7 dB
  fade:     the same ring ramped to zero over the last 500 ms
If the step test scores those two the same, none of its numbers are believed.
"""
import json, sys
import numpy as np
import librosa
from scipy.io import wavfile

SR = 22050
NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']


def load(p):
    y, sr = librosa.load(p, sr=SR, mono=True)
    return y


def frames(y, win=0.020, hop=0.010):
    w, h = int(win * SR), int(hop * SR)
    f = librosa.util.frame(y, frame_length=w, hop_length=h)
    return np.sqrt(np.mean(f ** 2, axis=0))


def body_level(y, skip_s=1.0):
    r = frames(y)
    # median frame RMS, skipping the first second (attack) and the ending
    return float(np.median(r[int(skip_s / 0.010): int(len(r) * 0.85)]))


def ending(y, cut):
    """all the ending numbers, given the sample index where silence begins"""
    r = frames(y)
    body = body_level(y)
    c = cut / SR
    i0 = max(0, int((c - 0.240) / 0.010))
    i1 = max(i0 + 1, int((c - 0.040) / 0.010))
    pre = float(np.mean(r[i0:i1]))
    db = lambda x: 20 * np.log10(max(x, 1e-12))
    tail = y[cut + int(0.010 * SR): cut + int(0.300 * SR)]
    # monotonic fall over the final 1.5 s (prereg v2, falsifier 5)
    j0 = max(0, int((c - 1.5) / 0.010))
    seg = r[j0:int(c / 0.010)]
    rises = int(np.sum(np.diff(seg) > 0.5 * seg[:-1] + 1e-9))
    mono_fall = rises == 0
    # taper test: the 100 ms next to the cut against the 200 ms before that.
    # a fade to zero must dive there; a ring that is simply stopped must not.
    def seg(t0, t1):
        a, b = int((c - t1) * SR), int((c - t0) * SR)
        s = y[max(0, a):max(1, b)]
        return float(np.sqrt(np.mean(s ** 2))) if len(s) else 0.0
    last100, prev200 = seg(0.0, 0.100), seg(0.100, 0.300)
    n = min(20, cut)
    local = float(np.mean(np.abs(np.diff(y[cut - n - 1: cut]))))
    step = float(abs(y[cut - 1]))
    return dict(body_rms=round(body, 5),
                pre_vs_body_db=round(db(pre) - db(body), 2),
                tail_max_abs=float(np.max(np.abs(tail))) if len(tail) else 0.0,
                tail_exact_frac=round(float(np.mean(tail == 0.0)), 4) if len(tail) else 1.0,
                final_1p5s_monotonic_fall=bool(mono_fall),
                rises_in_final_1p5s=rises,
                last_sample=round(step, 6),
                local_slope_20samp=round(local, 8),
                taper_db=round(db(last100) - db(prev200), 2) if prev200 > 0 else None,
                step_ratio=round(step / (local + 1e-12), 1),
                bar_one_attack_db_under_body=None)


def bar_one(y):
    body = body_level(y)
    a = float(np.max(np.abs(y[: int(0.300 * SR)])))
    return round(20 * np.log10(max(a, 1e-12)) - 20 * np.log10(body), 2)


def chord_check(y, verse_regions):
    c = librosa.feature.chroma_cqt(y=y, sr=SR, hop_length=512)
    per = 512 / SR
    wins = []
    for (a, b) in verse_regions:
        i0, i1 = int(a / per), int(b / per)
        w = int(2.0 / per)
        for i in range(i0, max(i0 + 1, i1 - w + 1), int(1.0 / per)):
            v = c[:, i:i + w].mean(axis=1)
            v = v / (np.linalg.norm(v) + 1e-9)
            wins.append(v)
    M = np.array(wins)
    sims = [float(np.dot(M[i], M[j])) for i in range(len(M)) for j in range(i + 1, min(len(M), i + 4))]
    dom = [NAMES[int(np.argmax(m))] for m in M]
    return dict(n_windows=len(M),
                dominant_classes=sorted(set(dom)),
                min_pairwise_cos=round(min(sims), 3) if sims else None,
                mean_pairwise_cos=round(float(np.mean(sims)), 3) if sims else None)


def synth(kind, cut_s=4.0, f0=164.81, total_s=5.0):
    n = int(total_s * SR)
    t = np.arange(n) / SR
    y = 0.4 * np.sin(2 * np.pi * f0 * t) * np.exp(-t / 3.0)
    cut = int(cut_s * SR)
    y[cut:] = 0.0
    if kind == 'fade':
        m = int(0.5 * SR)
        y[cut - m:cut] *= np.linspace(1, 0, m)
    return y[:cut + int(0.3 * SR)], cut


if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else 'bed16.wav'
    out = {'file': path, 'instrument_validation': {}}

    # validate the step test in-call
    for kind in ('hardcut', 'fade'):
        y, cut = synth(kind)
        e = ending(y, cut)
        out['instrument_validation'][kind] = {k: e[k] for k in
                                              ('pre_vs_body_db', 'tail_exact_frac',
                                               'taper_db', 'step_ratio')}

    y = load(path)
    cut = None
    # find the cut: first run of >=300 ms of exact zeros after 80% of the file
    z = np.where(y == 0.0)[0]
    start = int(len(y) * 0.8)
    z = z[z > start]
    if len(z):
        # first zero that begins a >=300ms zero run
        need = int(0.3 * SR)
        for i in z:
            if np.all(y[i:i + need] == 0.0):
                cut = int(i)
                break
    out['cut_s'] = round(cut / SR, 3) if cut else None
    if cut:
        e = ending(y, cut)
        e['bar_one_attack_db_under_body'] = bar_one(y)
        out['ending'] = e
    total = len(y) / SR
    # verse windows: bed has no vocal yet, so the verse spans are the whole
    # pattern in quarters (placeholder until the voice exists)
    regs = [(1.0, total * 0.25), (total * 0.30, total * 0.50)]
    out['chroma'] = chord_check(y, regs)
    print(json.dumps(out, indent=1, ensure_ascii=False))