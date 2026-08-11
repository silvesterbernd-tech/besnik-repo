#!/usr/bin/env python3
"""albumver split measurement: main song (0-190s) vs hidden track (190-273s).
Chroma-based key (Krumhansl), onset tempo, plus compare hidden track vs demo1986."""
import librosa
import numpy as np

NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
MAJ = np.array([6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88])
MIN = np.array([6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17])

def analyze(path, t0, t1, label):
    y, sr = librosa.load(path, sr=22050, mono=True)
    seg = y[int(t0 * sr):int(t1 * sr)]
    if len(seg) < sr:
        print(f"{label}: too short"); return
    onset = librosa.onset.onset_strength(y=seg, sr=sr)
    tempo, _ = librosa.beat.beat_track(onset_envelope=onset, sr=sr, tightness=100)
    tempo = float(np.atleast_1d(tempo)[0])
    # autocorr peaks
    ac = librosa.autocorrelate(onset - onset.mean())
    hop = 512
    cands = []
    for lag in range(int(60 * sr / (240 * hop)), int(60 * sr / (60 * hop))):
        cands.append((ac[lag], 60.0 * sr / (hop * lag)))
    cands.sort(reverse=True)
    top = [round(c[1], 1) for c in cands[:3]]
    chroma = librosa.feature.chroma_cqt(y=seg, sr=sr, hop_length=512)
    cm = chroma.mean(axis=1)
    best = None
    for root in range(12):
        for kind, prof in (("maj", MAJ), ("min", MIN)):
            rolled = np.roll(prof, root)
            s = np.dot(cm, rolled) / (np.linalg.norm(cm) * np.linalg.norm(rolled) + 1e-9)
            if best is None or s > best[2]:
                best = (NOTES[root], kind, s)
    print(f"{label}: {len(seg)/sr:.0f}s | tempo {tempo:.1f} (peaks {top}) | key {best[0]} {best[1]} ({best[2]:.3f})")
    return seg, sr, chroma

print("== albumver split ==")
seg_main, sr, ch_main = analyze("/workspace/lindja/albumver.mp3", 0, 190, "main song 0-190s")
seg_hidden, sr, ch_hidden = analyze("/workspace/lindja/albumver.mp3", 190, 273, "hidden 190-273s")
seg_demo, sr, ch_demo = analyze("/workspace/lindja/demo1986.mp3", 0, 139, "demo full")

# cross-similarity of hidden vs demo chroma (mean-max cosine, same trick as before)
def sim(a, b):
    # a: 12 x T, b: 12 x U -> mean over time of max cosine across shifts
    a = a / (np.linalg.norm(a, axis=0, keepdims=True) + 1e-9)
    b = b / (np.linalg.norm(b, axis=0, keepdims=True) + 1e-9)
    vals = []
    for i in range(a.shape[1]):
        vals.append(np.max(a[:, i] @ b))
    return float(np.mean(vals))

print(f"\nchroma similarity hidden vs demo: {sim(ch_hidden, ch_demo):.3f}")
print(f"chroma similarity hidden vs main:  {sim(ch_hidden, ch_main):.3f}")
print(f"chroma similarity main vs demo:     {sim(ch_main, ch_demo):.3f}")
