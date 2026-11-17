"""Assemble song 7: the 15-bar one-chord bed, the 13 hand-placed line takes.

Follows songs/song7-voice-lines-prereg-20261117.md and its amendment.
Declared choices made before the mix, all recorded in the output:
  - bed: 15 bars, 64 BPM, ring 1.5 s, final strum velocity 0.34 (chosen so the
    level at the cut lands inside Zlatko's 6-10 dB-under-body band: measured
    -6.29 dB, versus -3.16 dB at the builder's default 0.50)
  - voice sits 6 dB above the bed's body level (one number, declared)
  - 15 ms raised-cosine end taper on each line file, only to stop clicks; the
    voice is not faded anywhere else
"""
import json, sys, importlib.util
import numpy as np
import librosa
from scipy.io import wavfile

SR_OUT = 48000


def load_mod(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    sys.modules[name] = m
    spec.loader.exec_module(m)
    return m


bed = load_mod('bed.py', 'bed')
plan = json.load(open('lines/rows.json'))
P = __import__('place').place(plan)
assert not P['errors'], P['errors']

# bed
y_bed, cut_bed = bed.build(64.0, P['bars'], 1.5, ring_vel=0.34)
y_bed = y_bed / np.max(np.abs(y_bed)) * 0.89
y_bed48 = librosa.resample(y_bed, orig_sr=bed.SR, target_sr=SR_OUT)

# voice stem
voice = np.zeros(len(y_bed48), dtype=np.float64)
placed = []
for row in P['rows']:
    y, sr = librosa.load(f"lines/{row['key']}.mp3", sr=SR_OUT, mono=True)
    end = int(round((row['dur'] + 0.040) * SR_OUT))
    y = y[:min(end, len(y))]
    n = int(0.015 * SR_OUT)
    if len(y) > n:
        y[-n:] *= 0.5 * (1 + np.cos(np.linspace(0, np.pi, n)))
    start = int(round(row['start'] * SR_OUT))
    y = y[:max(0, len(voice) - start)]
    voice[start:start + len(y)] += y
    placed.append((row['key'], round(start / SR_OUT, 3), round((start + len(y)) / SR_OUT, 3)))

# gain staging
fr = librosa.util.frame(y_bed48, frame_length=int(0.02 * SR_OUT), hop_length=int(0.01 * SR_OUT))
body = float(np.median(np.sqrt(np.mean(fr ** 2, axis=0))))
vf = librosa.util.frame(voice, frame_length=int(0.02 * SR_OUT), hop_length=int(0.01 * SR_OUT))
vr = np.sqrt(np.mean(vf ** 2, axis=0))
v_db = 20 * np.log10(np.maximum(vr, 1e-12))
voiced = v_db > -45
v_rms = float(np.sqrt(np.mean(vr[voiced] ** 2)))
target = body * (10 ** (6 / 20))
gain = target / max(v_rms, 1e-9)
print(f"bed body rms {body:.5f} ({20*np.log10(body):.2f} dBFS), voice voiced rms {v_rms:.5f} "
      f"({20*np.log10(v_rms):.2f} dBFS), voice gain {gain:.3f} ({20*np.log10(gain):.2f} dB)")

mix = y_bed48 + voice * gain
peak = float(np.max(np.abs(mix)))
print(f"mix peak before limiting {peak:.3f}")
if peak > 0.99:
    mix = mix * (0.99 / peak)
    print(f"scaled mix by {0.99/peak:.3f} to avoid clipping")

wavfile.write('song7_mix.wav', SR_OUT, (np.clip(mix, -1, 1) * 32767).astype(np.int16))
wavfile.write('song7_voice.wav', SR_OUT, (np.clip(voice * gain, -1, 1) * 32767).astype(np.int16))

# checks
cut = None
nz = np.where(np.abs(mix) > 0.0)[0]
cut = int(nz[-1] + 1)
cut_s = cut / SR_OUT
tail = mix[cut + int(0.010 * SR_OUT): cut + int(0.300 * SR_OUT)]
vz = np.where(np.abs(voice[:, ]) > 0.0)[0]
v_last = (vz[-1] + 1) / SR_OUT if len(vz) else None
strum = P['strum_at']
print(f"cut at {cut_s:.3f} s (plan {P['cut_at']}); zeros after cut {np.mean(tail == 0.0):.4f}")
print(f"last voice sample {v_last:.3f} s; strum at {strum:.3f}; gap {strum - v_last:.3f} s "
      f"(preregistered 0.5-2.0)")
print(f"duration {len(mix)/SR_OUT:.2f} s; voice span {P['voice_span']} s (call 38-60)")
json.dump({'plan_bars': P['bars'], 'intro_bars': P['intro_bars'], 'pause_L12': P['pause_L12'],
           'ring_vel': 0.34, 'voice_gain_db': round(20 * np.log10(gain), 2),
           'cut_s': round(cut_s, 3), 'zeros_after_cut': float(np.mean(tail == 0.0)),
           'last_voice_s': round(v_last, 3), 'strum_gap_s': round(strum - v_last, 3),
           'duration_s': round(len(mix) / SR_OUT, 2), 'voice_span_s': P['voice_span'],
           'placed': placed}, open('assemble_report.json', 'w'), indent=1)
