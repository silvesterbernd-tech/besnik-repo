import numpy as np, json
from scipy.io import wavfile

SR = 48000
sr, x = wavfile.read('song7_mix.wav')
x = x.astype(np.float64) / 32767.0

def rms_db(seg):
    r = np.sqrt(np.mean(seg**2))
    return 20*np.log10(max(r, 1e-12))

nz = np.where(np.abs(x) > 0.0)[0]
cut_old = (nz[-1] + 1) / SR

# reference: the last attack. Zlatko measured 56.25-56.40 = -20.4 dB.
att_a, att_b = 56.25, 56.40
body_strum = rms_db(x[int(att_a*SR):int(att_b*SR)])

# general bed body (assemble's reference: median 20 ms frame RMS over file)
fl, hop = int(0.02*SR), int(0.01*SR)
fr = np.lib.stride_tricks.sliding_window_view(x, fl)[::hop]
vals = np.sqrt(np.mean(fr**2, axis=1))
body_med = float(np.median(vals))
body_med_db = 20*np.log10(max(body_med, 1e-12))

print(f"file dur {len(x)/SR:.3f}s  cut {cut_old:.3f}s  strum-body(56.25-56.40) {body_strum:.1f} dB  median body {body_med_db:.1f} dB")

rows = {}
for c in (56.61, 56.71, 56.73, 56.85, 57.79):
    i = int(round(c*SR))
    l50 = rms_db(x[i-int(0.050*SR):i])
    l200 = rms_db(x[i-int(0.200*SR):i])
    rows[c] = {'last50_vs_strum': round(l50-body_strum,1), 'last200_vs_strum': round(l200-body_strum,1),
               'last200_vs_median': round(l200-body_med_db,1)}
    print(f"cut {c}: 50ms {l50:.1f} dB -> {l50-body_strum:+.1f} vs strum, {l50-body_med_db:+.1f} vs median | "
          f"200ms {l200:.1f} -> {l200-body_strum:+.1f} vs strum, {l200-body_med_db:+.1f} vs median")

# is the old ending a step or a fall?
tail = x[int(cut_old*SR)-int(1.5*SR):int(cut_old*SR)]
seg = 0.05*SR
prof = [rms_db(tail[k:k+int(seg)] if k+int(seg)<=len(tail) else tail[k:]) for k in range(0, len(tail)-5, int(seg))]
print("last 1.5 s in 50 ms blocks:", [round(p,1) for p in prof])
last50 = x[int(cut_old*SR)-int(0.05*SR):int(cut_old*SR)]
print(f"max sample jump in last 50 ms: {np.max(np.abs(np.diff(last50))):.5f} full-scale; last sample |{x[int(cut_old*SR)-1]:.4f}|")

# --- the re-cut: same take, truncated at 56.73, zeros after
cut = 56.73
i = int(round(cut*SR))
new = np.concatenate([x[:i], np.zeros(int(0.40*SR))])
print(f"\nnew cut at {i/SR:.4f} s, level just before cut |{x[i-1]:.4f}| ({20*np.log10(max(abs(x[i-1]),1e-12)):.1f} dBFS)")
print(f"zeros after cut: {np.mean(new[i+int(0.010*SR):i+int(0.300*SR)]==0.0):.4f}")
print(f"duration {len(new)/SR:.3f}s")
wavfile.write('song7_recut.wav', SR, (np.clip(new,-1,1)*32767).astype(np.int16))

# last 12 s slice for Zlatko, wav, cut inside it
sl = new[int((cut-11.9)*SR):]
wavfile.write('s7_recut_tail12.wav', SR, (np.clip(sl,-1,1)*32767).astype(np.int16))
print(f"slice {len(sl)/SR:.3f}s starting {(cut-11.9):.2f}s, cut at {11.9:.2f}s inside it")

json.dump({'cut_old':round(cut_old,3),'strum_body_db':round(body_strum,1),'median_body_db':round(body_med_db,1),
           'table':{str(k):v for k,v in rows.items()},'new_cut':cut,
           'profile_50ms':[round(p,1) for p in prof]}, open('recut_report.json','w'), indent=1)
