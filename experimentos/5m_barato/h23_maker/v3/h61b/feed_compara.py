#!/usr/bin/env python3
"""feed_compara.py D [moneda=BTC] -- HITO 1a: ¿el aggTrade 'live' (multivenue binance_spot, fetch propio) es el mismo que el 'reg' (x_D del registro ms) que uso el replay H61?
Mide (solo lectura): cobertura bidireccional por (T,p,q), diferencia de recepcion, huecos, y CONCORDANCIA DE LA SENAL congelada (ret W=500ms, X=0,5bps) en instantes aleatorios del dia
(ambos lados Up/Down). Salida JSON a stdout (y a H61B_OUT/feed_D_moneda.json si existe la variable). Uso: nice -n 19 ionice -c3 python3 -I feed_compara.py 2026-10-20  (ulimit -v 2500000)"""
import gzip, json, os, subprocess, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import h61b_regla as R
import h61b_feeds as F


def cargar_con_sello(D, moneda):
    sim = moneda + "USDT"
    reg, mv = [], []
    f = F.CACHE + f"x_{D}.csv.gz"
    if os.path.exists(f):
        with gzip.open(f, "rt") as fh:
            for ln in fh:
                c = ln.rstrip("\n").split(",")
                if len(c) >= 8 and c[0] == "x" and c[2] == sim:
                    try: reg.append((int(c[1]), int(c[7]), float(c[3]), float(c[4])))
                    except ValueError: pass
    for f in F.ficheros_mv(D):
        p = subprocess.run(f"nice -n 19 zcat {f} | grep -a ',T,{moneda},'", shell=True, capture_output=True, text=True)
        for ln in p.stdout.splitlines():
            c = ln.split(",")
            if len(c) >= 7 and c[0] == "binance_spot" and c[1] == "T":
                try: mv.append((int(c[3]), int(c[4]), float(c[5]), float(c[6])))
                except ValueError: pass
    return reg, mv


def pct(a, q): return None if not len(a) else float(np.percentile(a, q))


def main(D, moneda="BTC"):
    reg, mv = cargar_con_sello(D, moneda)
    out = dict(dia=D, moneda=moneda, n_reg=len(reg), n_live=len(mv))
    if not reg or not mv:
        out["estado"] = "MISSING (falta una de las dos fuentes)"; return out
    # dedup exacto
    reg = sorted(set(reg)); mv = sorted(set(mv))
    out["n_reg_dedup"], out["n_live_dedup"] = len(reg), len(mv)
    kr = {}
    for T, rx, p, q in reg: kr.setdefault((T, p, q), []).append(rx)
    km = {}
    for T, rx, p, q in mv: km.setdefault((T, p, q), []).append(rx)
    com = set(kr) & set(km)
    out["claves_reg"], out["claves_live"], out["claves_comunes"] = len(kr), len(km), len(com)
    out["pct_reg_en_live"] = round(len(com) / len(kr), 5); out["pct_live_en_reg"] = round(len(com) / len(km), 5)
    d = np.array([km[k][0] - kr[k][0] for k in com], dtype=np.float64)
    out["rx_live_menos_reg_ms"] = dict(p1=pct(d, 1), p10=pct(d, 10), p50=pct(d, 50), p90=pct(d, 90), p99=pct(d, 99), media=float(d.mean()))
    out["reg_rx_menos_T_ms"] = dict(p50=pct(np.array([r[1] - r[0] for r in reg]), 50), p90=pct(np.array([r[1] - r[0] for r in reg]), 90))
    out["live_rx_menos_T_ms"] = dict(p50=pct(np.array([r[1] - r[0] for r in mv]), 50), p90=pct(np.array([r[1] - r[0] for r in mv]), 90))
    for nom, fu in (("reg", reg), ("live", mv)):
        rx = np.array(sorted(r[1] for r in fu)); g = np.diff(rx)
        out["huecos_" + nom] = dict(trades_por_s=round(len(rx) / max(1, (rx[-1] - rx[0]) / 1000), 3), p50_ms=pct(g, 50), p90_ms=pct(g, 90), p99_ms=pct(g, 99),
                                    frac_mayor_1s=float((g > 1000).mean()), frac_mayor_5s=float((g > 5000).mean()), max_s=float(g.max() / 1000))
    # concordancia de la senal congelada
    ar = np.array(sorted((r[1], r[2]) for r in reg)); am = np.array(sorted((r[1], r[2]) for r in mv))
    rr, pr = ar[:, 0].astype(np.int64), ar[:, 1]; rm, pm = am[:, 0].astype(np.int64), am[:, 1]
    lo, hi = max(rr[0], rm[0]) + 10000, min(rr[-1], rm[-1]) - 10000
    rng = np.random.default_rng(7); t = np.sort(rng.integers(lo, hi, 400000))
    for lado in ("Up", "Down"):
        a = R.ret_bps(rr, pr, t, lado); b = R.ret_bps(rm, pm, t, lado)
        da, db = a < -R.X_BPS, b < -R.X_BPS
        nanA, nanB = np.isnan(a), np.isnan(b)
        both = ~nanA & ~nanB
        out["senal_" + lado] = dict(n_instantes=len(t), dispara_reg=round(float(da.mean()), 4), dispara_live=round(float(db.mean()), 4),
                                    discrepan=round(float((da != db).mean()), 5), solo_reg=round(float((da & ~db).mean()), 5), solo_live=round(float((~da & db).mean()), 5),
                                    nan_reg=round(float(nanA.mean()), 5), nan_live=round(float(nanB.mean()), 5),
                                    ret_dif_abs_bps_p50=pct(np.abs(a[both] - b[both]), 50), ret_dif_abs_bps_p90=pct(np.abs(a[both] - b[both]), 90), ret_dif_abs_bps_p99=pct(np.abs(a[both] - b[both]), 99))
    return out


if __name__ == "__main__":
    D = sys.argv[1]; coin = sys.argv[2] if len(sys.argv) > 2 else "BTC"
    o = main(D, coin)
    s = json.dumps(o, indent=1, default=float)
    if os.environ.get("H61B_OUT"):
        os.makedirs(os.environ["H61B_OUT"], exist_ok=True)
        open(os.path.join(os.environ["H61B_OUT"], f"feed_{D}_{coin}.json"), "w").write(s)
    print(s)
