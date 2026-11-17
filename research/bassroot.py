import numpy as np, librosa, json, sys
SR=22050
names=['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
def pc(hz):
    return None if hz<=0 else names[int(round(69+12*np.log2(hz/440.0)))%12]
y,sr=librosa.load(sys.argv[1],sr=SR,mono=True)
y=librosa.effects.harmonic(y)                    # strip percussive
from scipy.signal import butter, sosfilt
sos=butter(4,320,'low',fs=SR,output='sos')
low=sosfilt(sos,y)
f0,vf,vp=librosa.pyin(low,fmin=55,fmax=330,sr=SR,frame_length=2048,hop_length=512)
ts=librosa.frames_to_time(np.arange(len(f0)),sr=SR,hop_length=512)
seq=[(round(float(t),1),pc(float(f)),round(float(v),2)) for t,f,v in zip(ts,f0,vf) if np.isfinite(f) and v>0.5]
# collapsed runs
runs=[]
for t,p,v in seq:
    if runs and runs[-1][0]==p: runs[-1][2]=t
    else: runs.append([p,t,t])
hist={}
for t,p,v in seq: hist[p]=hist.get(p,0)+1
print(json.dumps(dict(top=sorted(hist.items(),key=lambda x:-x[1])[:5],
                      n_runs=len(runs), runs=[r for r in runs if r[2]-r[1]>=1.0][:25]),indent=1))
