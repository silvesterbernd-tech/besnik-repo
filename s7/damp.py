import numpy as np, json
from scipy.io import wavfile
SR=48000
sr,x=wavfile.read('song7_mix.wav'); x=x.astype(np.float64)/32767.0
def db(seg):
    r=np.sqrt(np.mean(seg**2)); return 20*np.log10(max(r,1e-12))
body=db(x[int(56.25*SR):int(56.40*SR)])
# hand damp: design fixed before measuring
T_RING_END=56.60; T_20DB=56.71; T_ZERO=56.725; CUT=56.73; DROP=24.0
i0,i1,i2,i3=int(T_RING_END*SR),int(T_20DB*SR),int(T_ZERO*SR),int(CUT*SR)
y=x[:i3].copy()
ramp=np.linspace(0.0,-DROP,i1-i0)
y[i0:i1]*=10**(ramp/20.0)                 # 24 dB of energy gone in 110 ms
y[i1:i2]*=10**((-DROP*np.linspace(1,1.0,i2-i1))/20.0)  # hold, then 15 ms taper
k=np.arange(i2-i1)/(i2-i1)
y[i1:i2]*=(1-k)                           # taper to exact zero (amplitude)
y[i1:i2]*=10**(-DROP/20.0)
out=np.concatenate([y,np.zeros(int(0.40*SR))])
print(f"strum body {body:.1f} dB | dur {len(out)/SR:.3f} s")
l50=db(out[i3-int(0.05*SR):i3]); l100=db(out[i3-int(0.10*SR):i3])
print(f"last50 {l50:.1f} = {l50-body:+.1f} vs strum | last100 {l100:.1f} = {l100-body:+.1f}")
print(f"level at 56.66 (pre-ramp) {db(out[int(56.58*SR):int(56.60*SR)]):.1f} dB")
# slope in dB/s across the ramp, 10 ms blocks
blocks=[db(out[int((56.60+k*0.01)*SR):int((56.61+k*0.01)*SR)]) for k in range(11)]
print("ramp 10ms blocks:",[round(b,1) for b in blocks])
print(f"ramp slope {(blocks[0]-blocks[-1])/0.10:.0f} dB/s ; instrument's own decay 23-25 dB/s")
print(f"max sample step last 100 ms {np.max(np.abs(np.diff(out[i3-int(0.1*SR):i3]))):.4f} FS")
nz=np.where(np.abs(out)>0)[0]; print(f"first exact zero {(nz[nz<i3][-1]+1)/SR:.4f} s, zeros to end {np.mean(out[i3+int(0.01*SR):]==0):.4f}")
prof=[db(out[int((CUT-1.5+k*0.05)*SR):int((CUT-1.45+k*0.05)*SR)]) for k in range(30)]
print("last 1.5 s 50ms profile:",[round(p,1) for p in prof])
print("monotonic?", all(prof[i]>=prof[i+1] for i in range(len(prof)-1)))
wavfile.write('song7_damp.wav',SR,(np.clip(out,-1,1)*32767).astype(np.int16))
sl=out[int((CUT-11.9)*SR):]; wavfile.write('s7_damp_tail12.wav',SR,(np.clip(sl,-1,1)*32767).astype(np.int16))
print(f"tail slice {len(sl)/SR:.3f} s, cut 11.9 s in")
json.dump({'body_db':round(body,1),'last50_vs_body':round(l50-body,1),'last100_vs_body':round(l100-body,1),
 'ramp_slope_db_s':round((blocks[0]-blocks[-1])/0.10),'profile':[round(p,1) for p in prof],
 'max_step_last100ms':float(round(np.max(np.abs(np.diff(out[i3-int(0.1*SR):i3]))),4)),'dur':round(len(out)/SR,3)},
 open('damp_report.json','w'),indent=1)
