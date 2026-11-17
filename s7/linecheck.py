"""Do the 13 single-line takes actually carry the 13 lines they were asked for?

The batch submitted 13 jobs, one line each. If a job's audio came back with the
wrong text (or the mapping slipped), the piece would carry a line in the wrong
place, and I cannot hear Albanian mistake it. So: match every line file against
every segment of take 2, whose order is known from its ASR timings.

Instrument: MFCC sequences, per-coefficient z-scored, DTW with cosine cost.
Same line, two renders -> should be the lowest-cost pair in both its row and its
column. Proved here before it is believed:
  - a file against itself must be cost ~0 (same vs same)
  - take 2's own segment 1 vs segment 2 is a known mismatch (different lines)
If the diagonal does not win, the instrument cannot establish identity and the
report says so instead of picking the nicest assignment.
"""
import json, os, sys
import numpy as np
import librosa

SD = os.path.dirname(os.path.abspath(__file__))
SEG_STARTS = [0.28, 2.44, 4.62, 6.94, 9.088, 12.56, 14.34, 15.96, 18.64, 20.94,
              23.96, 26.66, 28.76]
SEG_ENDS = [2.18, 3.712, 5.952, 8.1, 11.712, 14.2, 15.072, 17.856, 20.16, 23.328,
            25.664, 28.72, 30.0]


def feats(y, sr):
    m = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13, n_fft=512, hop_length=int(0.010 * sr))
    m = (m - m.mean(axis=1, keepdims=True)) / (m.std(axis=1, keepdims=True) + 1e-8)
    return m.T


def dtw_cost(a, b):
    d = 1.0 - (a @ b.T) / (np.linalg.norm(a, axis=1)[:, None] * np.linalg.norm(b, axis=1)[None, :] + 1e-8)
    D, wp = librosa.sequence.dtw(C=d)
    return float(D[-1, -1] / (len(a) + len(b)))


def main(take2_path, lines_dir):
    y2, sr = librosa.load(take2_path, sr=16000, mono=True)
    segs = [feats(y2[int(a * sr):int(b * sr)], sr) for a, b in zip(SEG_STARTS, SEG_ENDS)]
    keys = [f'L{i+1:02d}' for i in range(13)]
    lines = {}
    for k in keys:
        p = os.path.join(lines_dir, f'{k}.mp3')
        if os.path.exists(p):
            y, sr2 = librosa.load(p, sr=16000, mono=True)
            lines[k] = feats(y, sr2)
        else:
            print(f'{k}: missing')
    # instrument proof
    same = dtw_cost(segs[0], segs[0])
    diff = dtw_cost(segs[0], segs[1])
    print(f'instrument: same-segment cost {same:.4f}, segment1-vs-2 cost {diff:.4f}, '
          f'separable={diff > 3 * max(same, 1e-6)}')
    M = np.zeros((len(lines), 13))
    order = [k for k in keys if k in lines]
    for i, k in enumerate(order):
        for j, s in enumerate(segs):
            M[i, j] = dtw_cost(lines[k], s)
    print('rows = line takes, cols = take-2 segments (1..13)')
    hits = 0
    for i, k in enumerate(order):
        own = int(k[1:]) - 1          # the segment this line was cut from
        best = int(np.argmin(M[i]))
        second = float(np.sort(M[i])[1])
        ok = best == own
        hits += ok
        print(f'  {k}: own seg {own+1}, best col {best+1} cost {M[i,best]:.4f} '
              f'(2nd {second:.4f}) {"OK" if ok else "MISS"}')
    print(f'own-segment wins {hits}/{len(order)}')
    out = {'order': order, 'matrix': M.round(5).tolist(), 'own_wins': hits,
           'instrument_separable': bool(diff > 3 * max(same, 1e-6))}
    json.dump(out, open(os.path.join(SD, 'linecheck.json'), 'w'), indent=1)


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(SD, 'lines', 'take2.mp3'),
         sys.argv[2] if len(sys.argv) > 2 else os.path.join(SD, 'lines'))
