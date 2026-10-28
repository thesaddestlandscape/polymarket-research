import numpy as np, os
OUT='/root/polymarket-research/experimentos/5m_barato/formula_r4_28oct/out/'
conf=['2026-10-%02d'%d for d in range(19,26)]
med=float(np.median([len(np.load(OUT+'d_%s.npz'%d)['T']) for d in conf]))
inc=[]
for d in ['2026-10-%02d'%k for k in range(9,19)]:
    f=OUT+'d_%s.npz'%d
    if not os.path.exists(f): print(d,'NO CONSTRUIDO'); continue
    z=np.load(f); n=len(z['T']); yc=float(np.isfinite(z['y']).mean()); mc=float(z['matched'].mean())
    ok=(0.65*med<=n<=1.35*med) and yc>=0.99 and mc>=0.35
    print('%s n=%d (ref mediana %.0f) y_cov=%.4f casadas=%.3f -> %s'%(d,n,med,yc,mc,'INCLUIDO' if ok else 'EXCLUIDO'))
    if ok: inc.append(d)
open('/root/polymarket-research/experimentos/5m_barato/formula_r4_28oct/ext_dias_incluidos.txt','w').write(','.join(sorted(inc)))
print('incluidos:',len(inc))
