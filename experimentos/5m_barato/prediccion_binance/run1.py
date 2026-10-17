from model import *
import sys
tag = sys.argv[1] if len(sys.argv) > 1 else "ds"
res = []
for H in (150, 250, 400):
    d = load(H, tag)
    tr = d[d.dia.isin(DIAS[:2])].reset_index(drop=True); te = d[d.dia.isin(DIAS[2:])].reset_index(drop=True)
    print(f"\n=== {tag} H={H} train n={len(tr)} pos Y1={tr.Y1.sum()} Y3={tr.Y3.sum()} | OOS n={len(te)} pos Y1={te.Y1.sum()} Y3={te.Y3.sum()}")
    for tgt in ("Y1", "Y3"):
        for nm, cols in (("BIN", BIN + CODE), ("CTX", CTX), ("ALL", BIN + CTX)):
            if nm == "CTX" and tag != "ds": continue
            row = {"H": H, "tgt": tgt, "set": nm}
            for kind in ("lin", "hgb"):
                s, _ = fit_score(tr, te, cols, tgt, kind, oof_on=False)
                row[kind] = auc(te[tgt].values, s)
                row[kind + "_d"] = [round(auc(te[te.dia == x][tgt].values, s[(te.dia == x).values]), 3) for x in DIAS[2:]]
            print(tgt, nm, {k: (round(v, 3) if isinstance(v, float) else v) for k, v in row.items() if k not in ("H","tgt","set")}, flush=True)
