"""Song 7 — the bed, built by hand instead of generated whole.

One chord (Em open), one chord for the whole piece, bar-one attack, and a
second-half final ring that is still at body-minus-a-few-dB when the hand lands
on it. The hand-land is a hard cut: nothing after it but exact zeros.

The generator's failure mode (writing a progression under a one-chord brief)
can't happen here because nothing plays a second chord.

Karplus-Strong strings, per-string T60 set so the final strum is still loud at
the cut. Usage:
    python bed.py --tempo 64 --bars 16 --ring 1.5 --out bed16.wav
The cut happens `--ring` seconds after the final strum.
"""
import argparse, math
import numpy as np
from scipy.io import wavfile

SR = 22050

# open Em, low to high
STRINGS = [("E2", 82.4069), ("A2", 0.0), ("B2", 123.4708), ("E3", 164.8138),
           ("G3", 195.9977), ("B3", 246.9417), ("E4", 329.6276)]
VOICING = [82.4069, 123.4708, 164.8138, 195.9977, 246.9417, 329.6276]


def _onepole_lp(x, cutoff, sr=SR):
    """simple one-pole lowpass, gives the pick a soft but present top"""
    a = np.exp(-2 * np.pi * cutoff / sr)
    y = np.zeros_like(x)
    acc = 0.0
    for i in range(len(x)):
        acc = a * acc + (1 - a) * x[i]
        y[i] = acc
    return y


def ks_pluck(f0, dur, t60, amp, rng, bright=1.0, detune_cents=0.0):
    """Karplus-Strong with fractional delay + 2-point averaging loop.

    Detuned slightly per pluck so unison strings beat like strings, not like a
    keyboard. The excitation is noise shaped by the string's own pitch (short
    strings sound brighter), with a pick transient on top.
    """
    total = dur if not hasattr(dur, "__len__") else dur
    n_total = int(total * SR)
    delay = SR / (f0 * 2.0 ** (detune_cents / 1200.0))
    N = int(round(delay))
    frac = delay - N
    g = 0.001 ** (N / (t60 * SR))          # per-string feedback for target T60
    exc = rng.standard_normal(N + 2)
    # string-dependent excitation bandwidth: low strings fatter, high strings
    # brighter (proportional to the string's own pitch)
    cf = min(9000.0, max(4000.0, f0 * 60.0 * bright))
    exc = _onepole_lp(exc, cf)
    exc = exc - exc.mean()
    buf = exc[:N + 1] * amp
    out = np.zeros(n_total)
    i = 0
    for s in range(n_total):
        a = buf[i]
        b = buf[(i + 1) % (N + 1)]
        v = a + frac * (b - a)                     # fractional read
        out[s] = v
        buf[i] = g * 0.5 * (a + b)                 # averaging loss in the loop
        i = (i + 1) % (N + 1)
    # pick transient: 12 ms bright noise, decays fast, gives the attack an edge
    t = int(0.012 * SR)
    tr = rng.standard_normal(t) * np.exp(-np.arange(t) / (0.0025 * SR))
    tr = tr - np.mean(tr)
    tr = np.diff(np.concatenate([[0.0], tr]))
    out[:t] += tr * amp * 1.10
    return out


def _peak(x, f, q, gain_db):
    from scipy.signal import iirpeak, lfilter
    b, a = iirpeak(f / (SR / 2.0), q)
    return lfilter(b, a, x) * (10 ** (gain_db / 20.0) - 1.0) + x


def body(x):
    """a little guitar body: air, top-plate resonance, pick brightness"""
    for f, q, g in ((110.0, 1.3, 2.0), (230.0, 1.4, 1.5), (3200.0, 0.8, 2.5)):
        x = _peak(x, f, q, g)
    return x


def strum(t0, strings, vel, rng, dur=6.0, spread=0.022, t60=None):
    """Down-stroke, low string first, small per-string offsets."""
    n = int(dur * SR)
    layer = np.zeros(n)
    for k, f0 in enumerate(strings):
        off = int((spread * k + rng.uniform(0, 0.008)) * SR)
        if off >= n:
            continue
        d = (n - off) / SR
        t60k = (t60 or (12.0 if f0 < 140 else 8.5 if f0 < 210 else 6.0))
        pl = ks_pluck(f0, d, t60k, vel * rng.uniform(0.85, 1.0), rng,
                      detune_cents=rng.uniform(-4.0, 4.0))
        layer[off:off + len(pl)] += pl
    return body(layer)


def dyad(t0, fs, vel, rng, dur=5.0, spread=0.006):
    n = int(dur * SR)
    layer = np.zeros(n)
    for k, f0 in enumerate(fs):
        off = int((spread * k + rng.uniform(0, 0.004)) * SR)
        pl = ks_pluck(f0, (n - off) / SR, 8.0 if f0 < 210 else 6.0,
                      vel * rng.uniform(0.85, 1.0), rng,
                      detune_cents=rng.uniform(-4.0, 4.0))
        layer[off:off + len(pl)] += pl
    return body(layer)


def add(track, layer, t0):
    i = max(0, int(round(t0 * SR)))
    n = min(len(layer), len(track) - i)
    if n > 0:
        track[i:i + n] += layer[:n]


def build(tempo=64.0, bars=16, ring=1.5, seed=7, ring_vel=0.50, ring_t60=11.0):
    rng = np.random.default_rng(seed)
    beat = 60.0 / tempo
    bar = 4 * beat
    total = bars * bar + ring + 0.4
    track = np.zeros(int(total * SR))

    E2, B2, E3, G3, B3, E4 = VOICING
    full = VOICING

    for b in range(bars):
        t = b * bar
        j = lambda: rng.uniform(-0.012, 0.012)
        # thumb / fingers pattern, one chord, hand moving
        add(track, strum(0, [E2], 0.55, rng), t + 0.0 + j())
        add(track, dyad(0, [E3, G3], 0.34, rng), t + 0.5 * beat + j())
        add(track, strum(0, [B2], 0.42, rng), t + 1.0 * beat + j())
        add(track, dyad(0, [B3, E4], 0.24, rng), t + 1.75 * beat + j())
        add(track, strum(0, [E2, B2], 0.50, rng), t + 2.0 * beat + j())
        add(track, dyad(0, [G3, B3], 0.30, rng), t + 2.5 * beat + j())
        add(track, strum(0, [B2], 0.38, rng), t + 3.0 * beat + j())
        add(track, dyad(0, [E3, B3], 0.26, rng), t + 3.5 * beat + j())

    # the final ring: the whole chord, still loud at the hand
    t_ring = bars * bar   # ring lands at the bar line, right after the last pattern note
    add(track, strum(0, full, ring_vel, rng, dur=ring + 0.5, spread=0.014,
                     t60=ring_t60), t_ring)

    cut = t_ring + ring
    c = int(round(cut * SR))
    body = track[:c]
    # 400 ms of exact zeros after the hand, then trim
    tail = np.zeros(int(0.4 * SR))
    y = np.concatenate([body, tail])
    # gentle DC block + soft ceiling
    y = y - np.convolve(y, np.ones(200) / 200, "same")
    peak = np.max(np.abs(y))
    if peak > 1e-9:
        y = y / peak * 0.89
    return y, cut


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--tempo", type=float, default=64.0)
    ap.add_argument("--bars", type=int, default=16)
    ap.add_argument("--ring", type=float, default=1.5)
    ap.add_argument("--out", default="bed.wav")
    a = ap.parse_args()
    y, cut = build(a.tempo, a.bars, a.ring)
    wavfile.write(a.out, SR, (np.clip(y, -1, 1) * 32767).astype(np.int16))
    print(f"{a.out}  dur={len(y)/SR:.2f}s  cut={cut:.3f}s  peak={np.max(np.abs(y)):.3f}")