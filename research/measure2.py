#!/usr/bin/env python3
"""Lindja follow-up: (1) demo tempo check across BPM range via onset autocorr peaks,
(2) section-by-section bass/chroma for albumver to locate the D#/G# cluster,
(3) section bass for tvp1985 to compare structure with the album version."""
import librosa
import numpy as np
import scipy.signal

NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

# ---------- 1) demo tempo, top autocorr peaks ----------
y, sr = librosa.load("/workspace/lindja/demo1986.mp3", sr=22050, mono=True)
onset = librosa.onset.onset_strength(y=y, sr=sr)
ac = librosa.autocorrelate(onset - onset.mean())
hop = 512
peaks = []
for lag in range(int(60 * sr / (220 * hop)), int(60 * sr / (70 * hop))):
    peaks.append((ac[lag], 60.0 * sr / (hop * lag)))
peaks.sort(reverse=True)
print("demo1986 onset-autocorr top 5 BPM candidates:", [round(p[1], 1) for p in peaks[:5]])

# ---------- 2) albumver sections ----------
def bass_top(y, sr, t0, t1, top=4):
    seg = y[int(t0 * sr):int(t1 * sr)]
    if len(seg) < sr:
        return []
    y_lp = scipy.signal.sosfilt(scipy.signal.butter(6, 250 / (sr / 2), "low", output="sos"), seg)
    f0, voiced, probs = librosa.pyin(y_lp, fmin=librosa.note_to_hz("E1"), fmax=librosa.note_to_hz("E3"), sr=sr, hop_length=512)
    cents = np.round(librosa.hz_to_midi(f0[voiced])).astype(int) % 12
    counts = np.bincount(cents, minlength=12)
    order = np.argsort(counts)[::-1][:top]
    total = counts.sum()
    return [(NOTES[i], round(100 * counts[i] / total, 1)) for i in order if counts[i] > 0]

print("\nalbumver sections (bass top notes, % of voiced frames):")
for label, t0, t1 in [("0-30s", 0, 30), ("30-60s", 30, 60), ("60-90s", 60, 90), ("90-120s", 90, 120),
                      ("120-150s", 120, 150), ("150-180s", 150, 180), ("180-210s", 180, 210),
                      ("210-240s", 210, 240), ("240-273s", 240, 273)]:
    print(f"  {label}: {bass_top(y, sr, t0, t1)}")

print("\ntvp1985 sections (bass top notes, % of voiced frames):")
y2, sr2 = librosa.load("/workspace/lindja/tvp1985.mp3", sr=22050, mono=True)
for label, t0, t1 in [("0-30s", 0, 30), ("30-60s", 30, 60), ("60-90s", 60, 90), ("90-120s", 90, 120),
                      ("120-150s", 120, 150), ("150-170s", 150, 170)]:
    print(f"  {label}: {bass_top(y2, sr2, t0, t1)}")

# ---------- 3) where does D#/G# live in albumver? frame-level ----------
y_lp = scipy.signal.sosfilt(scipy.signal.butter(6, 250 / (sr / 2), "low", output="sos"), y)
f0, voiced, probs = librosa.pyin(y_lp, fmin=librosa.note_to_hz("E1"), fmax=librosa.note_to_hz("E3"), sr=sr, hop_length=512)
cents = np.round(librosa.hz_to_midi(f0)).astype(int) % 12
times = librosa.times_like(f0, sr=sr, hop_length=512)
ds = times[(cents == 3) & voiced]   # D#
gs = times[(cents == 8) & voiced]   # G#
print(f"\nalbumver D# frames: {len(ds)} -> {round(ds.min(),1)}-{round(ds.max(),1)}s, median {round(np.median(ds),1)}s")
print(f"albumver G# frames: {len(gs)} -> {round(gs.min(),1)}-{round(gs.max(),1)}s, median {round(np.median(gs),1)}s")
