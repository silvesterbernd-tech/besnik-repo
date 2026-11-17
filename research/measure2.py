import numpy as np, librosa, json, sys
SR=22050
HOP=0.005  # 5 ms resolution

def rms_env(y):
    h=int(SR*HOP); w=int(SR*0.020)
    if len(y)<w: y=np.pad(y,(0,w-len(y)))
    f=librosa.util.frame(y,frame_length=w,hop_length=h)
    return np.sqrt(np.mean(f**2,axis=0)), HOP

def body_level(r):
    n=len(r); return float(np.median(r[int(n*0.10):int(n*0.80)]))

def ending(y):
    r,step=rms_env(y); body=body_level(r)
    if body<=0: return dict(error='silent file')
    rel=r/body
    idx=np.where(rel>0.03)[0]
    if len(idx)==0: return dict(error='nothing audible')
    last=idx[-1]; cut_s=last*step
    # level just before the cut (200 ms ending 40 ms before last audible)
    a=max(0,int((cut_s-0.200)/step)); b=max(1,int((cut_s-0.040)/step))
    pre=float(np.mean(r[a:b])) if b>a else 0.0
    # after: 40-300 ms past cut
    n=len(y); z0=int((cut_s+0.040)*SR); z1=min(n,int((cut_s+0.300)*SR))
    zseg=y[z0:z1] if z1>z0 else np.array([0.0])
    tail_max=float(np.max(np.abs(zseg)))
    tail_exact=float(np.mean(zseg==0.0)) if len(zseg) else 1.0
    # fade: last 0.5 s vs 1.0-1.5 s before last audible
    q=lambda t0,t1: float(np.mean(r[max(0,int((cut_s-t1)/step)):max(1,int((cut_s-t0)/step))]))
    early=q(1.0,1.5); late=q(0.0,0.5)
    db=lambda x: 20*np.log10(max(x,1e-9))
    return dict(duration=round(len(y)/SR,2), body_rms=round(body,5),
      last_audible=round(cut_s,3), pre_rms=round(pre,5),
      pre_vs_body_db=round(db(pre)-db(body),2),
      tail_max_abs=tail_max, tail_exact_frac=round(tail_exact,4),
      late_vs_early_db=round(db(late)-db(early),2) if early>0 else None)

def chroma_windows(y, win=2.0, hop=1.0):
    c=librosa.feature.chroma_cqt(y=y,sr=SR,hop_length=512)
    w=int(win*SR/512); h=int(hop*SR/512)
    out=[]
    for i in range(0,max(1,c.shape[1]-w+1),h):
        v=c[:,i:i+w].mean(axis=1); v=v/ (np.linalg.norm(v)+1e-9); out.append(v)
    return c,out

def chord_test(y):
    c,ws=chroma_windows(y)
    M=np.array(ws)
    sims=[]
    for i in range(len(M)):
        for j in range(i+1,min(len(M),i+4)):
            sims.append(float(np.dot(M[i],M[j])))
    names=['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
    dom=[names[int(np.argmax(m))] for m in M]
    return dict(n_windows=len(M), min_pairwise_cos=round(min(sims),3) if sims else None,
                mean_pairwise_cos=round(float(np.mean(sims)),3) if sims else None,
                dominant_seq=dom, n_distinct_dominant=len(set(dom)))

if __name__=='__main__':
    y,sr=librosa.load(sys.argv[1],sr=SR,mono=True)
    print(json.dumps(dict(file=sys.argv[1], ending=ending(y), chroma=chord_test(y)),indent=1,ensure_ascii=False))
