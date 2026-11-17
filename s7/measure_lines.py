"""Measure each single-line take: duration, first and last voiced sample.

Same envelope detector as take 2, and it is proved in the same run before its
numbers are believed: a file with 1 s of appended digital silence must keep its
last voiced sample where it was and show the full empty tail; a file with 1 s of
appended -45 dBFS noise must move it to the end of the noise.
"""
import json, os, subprocess, sys
import numpy as np
import librosa

SR = 24000
THR = -45.0          # dBFS, frame RMS, 20 ms frames / 5 ms hop
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lines')


def dl(url, key):
    os.makedirs(OUT, exist_ok=True)
    p = os.path.join(OUT, f'{key}.mp3')
    if not os.path.exists(p) or os.path.getsize(p) < 2000:
        subprocess.run(['curl', '-sS', '-L', '-o', p, url], check=True)
    return p


def env(y, sr):
    w, h = int(0.020 * sr), int(0.005 * sr)
    f = librosa.util.frame(y, frame_length=w, hop_length=h)
    rms = np.sqrt(np.mean(f ** 2, axis=0))
    db = 20 * np.log10(np.maximum(rms, 1e-12))
    return db, h / sr


def voiced_bounds(y, sr, thr=THR):
    db, hop = env(y, sr)
    idx = np.where(db > thr)[0]
    if len(idx) == 0:
        return None, None
    return float(idx[0] * hop), float((idx[-1] * hop) + 0.020)


def measure(path):
    y, sr = librosa.load(path, sr=None, mono=True)
    sr = int(sr)
    f, l = voiced_bounds(y, sr)
    return {'file': os.path.basename(path), 'sr': sr, 'dur': round(len(y) / sr, 3),
            'first': round(f, 3) if f is not None else None,
            'last': round(l, 3) if l is not None else None,
            'voiced': round(l - f, 3) if f is not None else None}


def selftest(path):
    y, sr = librosa.load(path, sr=None, mono=True)
    sr = int(sr)
    f0, l0 = voiced_bounds(y, sr)
    sil = np.concatenate([y, np.zeros(sr, dtype=y.dtype)])
    f1, l1 = voiced_bounds(sil, sr)
    noise = np.concatenate([y, (10 ** (-45 / 20) * np.random.RandomState(0)
                                .randn(sr)).astype(y.dtype)])
    f2, l2 = voiced_bounds(noise, sr)
    return {'base_last': round(l0, 3), 'after_silence_last': round(l1, 3),
            'after_quiet_noise_last': round(l2, 3),
            'empty_tail_after_silence_s': round((len(sil) / sr) - l1, 3),
            'validated': abs(l0 - l1) < 0.01 and l2 > l0 + 0.9}


if __name__ == '__main__':
    pairs = json.loads(sys.argv[1])       # {"L01": "https://...", ...}
    res = {}
    for k, url in pairs.items():
        p = dl(url, k)
        res[k] = measure(p)
        if 'selftest' not in res:
            res['selftest_' + k] = selftest(p)
    print(json.dumps(res, indent=1))
    old = {}
    mf = os.path.join(OUT, 'measured.json')
    if os.path.exists(mf):
        old = json.load(open(mf))
    old.update(res)
    json.dump(old, open(mf, 'w'), indent=1)
