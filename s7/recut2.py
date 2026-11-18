import numpy as np, json
from scipy.io import wavfile
SR=48000
_,x = wavfile.read('song7_mix.wav'); x = x.astype(np.float64)/32767.0
def db(seg):
    return 20*np.log10(max(float(np.sqrt(np.mean(seg**2))),1e-12))
strum = db(x[int(56.25*SR):int(56.40*SR)])          # chord body at the last attack
cut, tap = 56.73, 0.015
i = int(round(cut*SR))
seg = x[:i].copy()
n = int(tap*SR)
seg[i-n:] *= 0.5*(1+np.cos(np.linspace(0,np.pi,n)))   # the mute: 15 ms to exact zero
out = np.concatenate([seg, np.zeros(int(0.40*SR))])
print(f"strum body {strum:.1f} dBFS; taper {tap*1000:.0f} ms from {db(seg[i-n-1:i-n+int(0.005*SR)]):.1f} dBFS")
print(f"level in last 50 ms at cut: {db(out[i-int(0.05*SR):i])-strum:+.1f} dB vs strum")
print(f"level in the 50 ms BEFORE the taper: {db(x[i-n-int(0.05*SR):i-n])-strum:+.1f} dB vs strum")
print(f"drop across the taper: {db(x[i-n-int(0.05*SR):i-n])-db(out[i-1:i]):.1f} dB in {tap*1000:.0f} ms")
print(f"zeros after cut 10-300 ms: {np.mean(out[i+int(0.01*SR):i+int(0.3*SR)]==0.0):.4f}; dur {len(out)/SR:.3f}s")
# falsifier 5: monotonic fall across final 1.5 s? (blocks of 25 ms)
b=int(0.025*SR); prof=[db(out[k:k+b]) for k in range(i-int(1.5*SR), i-b, b)]
d=np.diff(prof); print(f"final 1.5 s: {len(prof)} blocks, {int((d<0).sum())} falling steps of {len(d)} -> monotonic={bool((d<=0).all())}; range {prof[0]:.1f}..{max(prof):.1f}")
# falsifier 6: bar-one attack
first = db(out[:int(0.3*SR)]); print(f"first 300 ms {first:.1f} dB ({first-strum:+.1f} vs strum)")
wavfile.write('song7_recut.wav',SR,(np.clip(out,-1,1)*32767).astype(np.int16))
sl = out[int((cut-11.9)*SR):]
wavfile.write('s7_recut_tail12.wav',SR,(np.clip(sl,-1,1)*32767).astype(np.int16))
print(f"tail slice {len(sl)/SR:.3f}s, cut at {11.9:.2f}s inside")
