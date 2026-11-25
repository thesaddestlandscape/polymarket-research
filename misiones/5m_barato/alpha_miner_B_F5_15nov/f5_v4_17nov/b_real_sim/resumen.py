import sys, glob, os, re, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import valida_v5 as V
tags = sorted({re.sub(r'_2026-10-2\d\.pkl', '', os.path.basename(f))[3:] for f in glob.glob(V.H + 'out_verif_v5/V5_r2_*.pkl')})
for t in tags:
    try: o, _ = V.evalua(V.carga(t), verbose=False)
    except AssertionError: continue
    print(f"{t:38s} sim {o['sim']:3d} TP {o['TP']:3d} FP {o['FP']:2d} FN {o['FN']:3d} prec {o['precision']:.3f} rec {o['recall']:.3f} rec_aj {o['recall_ajeno']:.3f} rec_pr {o['recall_propio']:.3f} +-50ms {o['pct_50ms']:.2f} EVtp {o['EV_TP_motor']:+.3f}/{o['EV_TP_real']:+.3f} EVfp {o['EV_FP_motor']:+.2f} EVfn {o['EV_FN_real']:+.3f}")
