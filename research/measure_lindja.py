#!/usr/bin/env python3
"""Lindja measurement pass (Aug 11 2026). Same method as the Marimanga tape:
tempo via onset autocorrelation, key via Krumhansl profile correlation,
bass-region pitch histogram via pyin on a low-passed mix. Honest numbers only.
"""
import librosa
import numpy as np
import scipy.signal

FILES = {
    "tvp1985": "/workspace/lindja/tvp1985.mp3",
    "albumver": "/workspace/lindja/albumver.mp3",
    "demo1986": "/workspace/lindja/demo1986.mp3",
}

NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

# Krumhansl-Kessler major/minor profiles, normalized
MAJ = np.array([6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88])
MIN = np.array([6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17])


def key_from_chroma(chroma):
    chroma_mean = chroma.mean(axis=1)
    best = None
    for root in range(12):
        for kind, prof in (("maj", MAJ), ("min", MIN)):
            rolled = np.roll(prof, root)
            score = np.dot(chroma_mean, rolled) / (np.linalg.norm(chroma_mean) * np.linalg.norm(rolled) + 1e-9)
            if best is None or score > best[2]:
                best = (NOTES[root], kind, score)
    return best


def tempo_of(y, sr):
    onset = librosa.onset.onset_strength(y=y, sr=sr)
    tempo, beats = librosa.beat.beat_track(onset_envelope=onset, sr=sr, tightness=100)
    # also autocorrelation estimate
    ac = librosa.autocorrelate(onset - onset.mean())
    # find the strongest lag in a plausible BPM range (60-200)
    min_lag = int(sr / 200 * 0.5)  # hop-based; recompute properly below
    hop = 512
    lag_min = int(60 * sr / (200 * hop))
    lag_max = int(60 * sr / (60 * hop))
    seg = ac[lag_min:lag_max]
    lag = np.argmax(seg) + lag_min
    tempo_ac = 60.0 * sr / (hop * lag)
    return float(np.atleast_1d(tempo)[0]), tempo_ac


def bass_hist(y, sr, top=5):
    y_lp = scipy.signal.sosfilt(scipy.signal.butter(6, 250 / (sr / 2), "low", output="sos"), y)
    f0, voiced, probs = librosa.pyin(y_lp, fmin=librosa.note_to_hz("E1"), fmax=librosa.note_to_hz("E3"), sr=sr, hop_length=512)
    cents = librosa.hz_to_midi(f0[voiced])
    cents = np.round(cents).astype(int) % 12
    counts = np.bincount(cents, minlength=12)
    order = np.argsort(counts)[::-1][:top]
    total = counts.sum()
    return [(NOTES[i], counts[i], round(100 * counts[i] / total, 1)) for i in order], int(total)


for name, path in FILES.items():
    y, sr = librosa.load(path, sr=22050, mono=True)
    dur = len(y) / sr
    tempo, tempo_ac = tempo_of(y, sr)
    chroma = librosa.feature.chroma_cqt(y=y, sr=sr, hop_length=512)
    key, kind, kscore = key_from_chroma(chroma)
    bass, n_voiced = bass_hist(y, sr)
    print(f"== {name} ({dur:.0f}s) ==")
    print(f"  tempo (beat_track): {tempo:.1f} BPM | tempo (autocorr): {tempo_ac:.1f} BPM")
    print(f"  key: {key} {kind} (score {kscore:.3f})")
    print(f"  bass histogram (top {len(bass)}, {n_voiced} voiced frames): {bass}")
    print()
