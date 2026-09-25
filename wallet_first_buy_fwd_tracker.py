#!/usr/bin/env python3
"""wallet_first_buy_fwd_tracker.py -- "seguir wallets informadas EMPEZANDO a comprar", validación
FORWARD diaria (25-Sep, Javi: "construye"). Solo lectura del firehose; nunca envía órdenes.

Idea: no copiar a las ballenas "a nuestro precio" con un rezago de horas, sino entrar L segundos
después de la PRIMERA compra de una wallet en un mercado 5/15min (evento = (wallet, mercado, lado),
primera compra), al precio del siguiente trade tras L s (proxy del ask), reteniendo a resolución
(fee 7 % sobre ganancia). Seleccionar wallets con datos ANTERIORES y medirlas después:
  - Entrenamiento: agregados por wallet (n, suma EV, suma EV^2 con L=1 s) de los TRAIN_DIAS días previos.
  - Selección CONGELADA antes del día de test: n>=MIN_N, EV medio>0 y t>=T_MIN.
  - Test: eventos de esas wallets el día D, EV a L=0,3/1/3 s.
Hallazgo del backtest de 25-Sep (21-24 Sep, 18k wallets, 1,3M eventos): las wallets seleccionadas dan
+0,10 EUR/EUR forward (t=4, iid) PERO: top5 wallets = 84 % del EV, sin ellas +0,02 (t=1,1); t por
clúster de mercado = 1,6; el EV vive en longshots (pf<0,3: +0,3..+1,4; pf 0,4-0,9: -0,03..-0,11) y
en tickets <10 $. Es decir, NO robusto todavía. Este tracker lo mide día a día con esas métricas
honestas; solo se plantea un ejecutor si el pool de días de test lo supera (ver veredicto).
Salidas (data/shadow/wallet_first_buy/): agg_YYYY-MM-DD.json, test_YYYY-MM-DD.csv;
data/shadow/wallet_first_buy_fwd.json y su historial jsonl. Uso: [--dia YYYY-MM-DD] [--backfill FROM TO].
"""
import bisect
import collections
import csv
import gzip
import json
import math
import os
import re
import statistics
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
DATALOGS = Path("/root/polymarket-research-datalogs")
DIR = REPO / "data" / "shadow" / "wallet_first_buy"
OUT = REPO / "data" / "shadow" / "wallet_first_buy_fwd.json"
HIST = REPO / "data" / "shadow" / "wallet_first_buy_fwd_historial.jsonl"
FEE = 0.07
LS = [0.3, 1.0, 3.0]
LSEL = 1.0
TRAIN_DIAS, MIN_N, T_MIN = 3, 15, 2.0
PF_LO, PF_HI = 0.03, 0.97
VEREDICTO_MIN_DIAS, VEREDICTO_T_CLUSTER, VEREDICTO_EX_TOP5, VEREDICTO_MERCADOS = 3, 2.5, 0.03, 300
VEREDICTO_T_SIN_TOP5 = 2.0   # t por clúster de mercado del EV SIN las 5 mejores wallets ex post


def _ts(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00")).timestamp()


def _pnl(p, ac):
    return (1 - p) / p * (1 - FEE) if ac else -1.0


def _tstat(v):
    n = len(v)
    if n < 2:
        return 0.0
    sd = statistics.pstdev(v)
    return (sum(v) / n) / (sd / math.sqrt(n)) if sd > 0 else 0.0


def _abrir_dia(dia):
    f = DATALOGS / f"polymarket_activity_{dia}.csv"
    if f.exists():
        return open(f, encoding="utf-8", errors="replace", newline="")
    f = DATALOGS / f"polymarket_activity_{dia}.csv.gz"
    return gzip.open(f, "rt", encoding="utf-8", errors="replace", newline="") if f.exists() else None


def procesar_dia(dia):
    """Eventos de primera compra del día con precio de seguimiento a cada L y ganador inferido de
    los trades finales del mercado (>=3 trades en los últimos 20 s, mediana de p_Up)."""
    fh = _abrir_dia(dia)
    if fh is None:
        return None
    mk = collections.defaultdict(list)
    first = {}
    with fh:
        for r in csv.DictReader(fh):
            if r["marco"] not in ("5min", "15min") or not r["market_slug"]:
                continue
            try:
                t, p = _ts(r["timestamp_utc"]), float(r["price"])
                m = re.search(r"-(\d{10})$", r["market_slug"])
            except (ValueError, KeyError, TypeError):
                continue
            if not m:
                continue
            k = r["market_slug"]
            end = int(m.group(1)) + (300 if r["marco"] == "5min" else 900)
            mk[k].append((t, p if r["outcome"] == "Up" else 1 - p, end))
            if r["side"] == "BUY":
                key = (k, r["wallet"].lower(), r["outcome"])
                if key not in first or t < first[key][0]:
                    try:
                        u = float(r["usd_value"] or 0)
                    except ValueError:
                        u = 0.0
                    first[key] = (t, p, u, r["activo"], r["marco"])
    ser, win = {}, {}
    for k, v in mk.items():
        v.sort()
        end = v[0][2]
        late = sorted(b for a, b, _ in v if a >= end - 20)
        win[k] = None if len(late) < 3 else ("Up" if late[len(late) // 2] > 0.5 else "Down" if late[len(late) // 2] < 0.5 else None)
        ser[k] = ([a for a, _, _ in v], [b for _, b, _ in v], end)
    filas = []
    for (k, w, o), (t, p, u, act, marco) in first.items():
        ts_, ups, end = ser[k]
        tte = end - t
        if tte < 15 or win[k] is None:
            continue
        pf = {}
        for L in LS:
            i = bisect.bisect_left(ts_, t + L)
            pf[L] = None
            if i < len(ts_) and ts_[i] - (t + L) <= 3 and ts_[i] < end - 5:
                pf[L] = ups[i] if o == "Up" else 1 - ups[i]
        filas.append({"wallet": w, "slug": k, "activo": act, "marco": marco, "tte": round(tte, 1), "usd": round(u, 2),
                      "ac": win[k] == o, "p_paid": p, **{f"pf_{L}": pf[L] for L in LS}})
    return filas


def _agregados(filas):
    agg = collections.defaultdict(lambda: [0, 0.0, 0.0])
    for r in filas:
        p = r[f"pf_{LSEL}"]
        if p is not None and PF_LO <= p < PF_HI:
            e = _pnl(p, r["ac"])
            a = agg[r["wallet"]]
            a[0] += 1; a[1] += e; a[2] += e * e
    return {w: [n, round(s, 4), round(q, 4)] for w, (n, s, q) in agg.items()}


def _seleccion(dia):
    tot = collections.defaultdict(lambda: [0, 0.0, 0.0])
    usados = []
    for k in range(1, 9):
        d = (date.fromisoformat(dia) - timedelta(days=k)).isoformat()
        f = DIR / f"agg_{d}.json"
        if f.exists() and len(usados) < TRAIN_DIAS:
            for w, (n, s, q) in json.loads(f.read_text()).items():
                a = tot[w]; a[0] += n; a[1] += s; a[2] += q
            usados.append(d)
    sel = set()
    for w, (n, s, q) in tot.items():
        if n < MIN_N or s <= 0:
            continue
        m = s / n
        var = max(q / n - m * m, 0.0)
        if var > 0 and m / math.sqrt(var / n) >= T_MIN:
            sel.add(w)
    return sel, usados, sum(1 for a in tot.values() if a[0] >= MIN_N)


def _stats(rows, L):
    v = [(_pnl(r[f"pf_{L}"], r["ac"]), r) for r in rows if r.get(f"pf_{L}") is not None and PF_LO <= r[f"pf_{L}"] < PF_HI]
    if not v:
        return None
    e = [x for x, _ in v]
    bm, bw = collections.defaultdict(list), collections.defaultdict(list)
    for x, r in v:
        bm[r["slug"]].append(x); bw[r["wallet"]].append(x)
    mm = [sum(a) / len(a) for a in bm.values()]
    tot = sum(e)
    top = sorted(bw.values(), key=lambda a: -sum(a))
    top5 = {id(a) for a in top[:5]}
    excl = {w for w, a in bw.items() if id(a) in top5}
    resto = [x for x, r in v if r["wallet"] not in excl]
    bm_r = collections.defaultdict(list)
    for x, r in v:
        if r["wallet"] not in excl:
            bm_r[r["slug"]].append(x)
    mm_r = [sum(a) / len(a) for a in bm_r.values()]
    return {"n": len(e), "ev": round(tot / len(e), 4), "t_iid": round(_tstat(e), 2), "n_mercados": len(bm),
            "t_cluster_mercado": round(_tstat(mm), 2), "wallets": len(bw),
            "top5_share": round(sum(sum(a) for a in top[:5]) / tot, 2) if tot > 0 else None,
            "ev_sin_top5": round(sum(resto) / len(resto), 4) if resto else None,
            "t_cluster_sin_top5": round(_tstat(mm_r), 2) if mm_r else None}


def _por_precio(rows, L=LSEL):
    g = collections.defaultdict(list)
    for r in rows:
        p = r.get(f"pf_{L}")
        if p is not None and PF_LO <= p < PF_HI:
            g[f"{int(p * 10) / 10:.1f}"].append(_pnl(p, r["ac"]))
    return {k: {"n": len(v), "ev": round(sum(v) / len(v), 3)} for k, v in sorted(g.items()) if len(v) >= 20}


def ejecutar(dia, enviar=True):
    DIR.mkdir(parents=True, exist_ok=True)
    filas = procesar_dia(dia)
    if filas is None:
        print(f"sin datos de {dia}")
        return None
    sel, usados, n_train_w = _seleccion(dia)          # selección con datos ANTERIORES a `dia` (congelada)
    (DIR / f"agg_{dia}.json").write_text(json.dumps(_agregados(filas)))
    test = [r for r in filas if r["wallet"] in sel]
    campos = ["wallet", "slug", "activo", "marco", "tte", "usd", "ac", "p_paid"] + [f"pf_{L}" for L in LS]
    with open(DIR / f"test_{dia}.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        for r in test:
            w.writerow({c: r[c] for c in campos})
    dia_res = {"dia": dia, "train_dias": usados, "wallets_train_n>=15": n_train_w, "seleccionadas": len(sel),
               "eventos_dia_total": len(filas), "test": {str(L): _stats(test, L) for L in LS}}
    pool = []
    for f in sorted(DIR.glob("test_*.csv")):
        for r in csv.DictReader(open(f, encoding="utf-8")):
            for L in LS:
                r[f"pf_{L}"] = float(r[f"pf_{L}"]) if r[f"pf_{L}"] != "" else None
            r["ac"] = r["ac"] == "True"
            pool.append(r)
    dias_test = \
        sum(1 for f in DIR.glob("test_*.csv") if f.stat().st_size > 200)   # solo días con wallets seleccionadas
    pool_res = {str(L): _stats(pool, L) for L in LS}
    s1 = pool_res[str(LSEL)]
    robusto = bool(s1 and dias_test >= VEREDICTO_MIN_DIAS and s1["t_cluster_mercado"] >= VEREDICTO_T_CLUSTER
                   and (s1["ev_sin_top5"] or -1) >= VEREDICTO_EX_TOP5 and s1["n_mercados"] >= VEREDICTO_MERCADOS
                   and (s1["t_cluster_sin_top5"] or -9) >= VEREDICTO_T_SIN_TOP5)
    informe = {"actualizado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "ultimo_dia": dia_res,
               "pool": {"dias_test": dias_test, "por_L": pool_res, "por_precio_L1": _por_precio(pool)},
               "veredicto": "CANDIDATA robusta (revisar + checklist)" if robusto else "NO robusta (cluster-t/ex-top5/n_mercados/dias)"}
    OUT.write_text(json.dumps(informe, indent=1, ensure_ascii=False))
    # Watchlist para el día SIGUIENTE (selección congelada con los TRAIN_DIAS días que acaban en `dia`,
    # incluido): la lee wallet_first_buy_follow_fase0.py (observador en tiempo real).
    try:
        dia_sig = (date.fromisoformat(dia) + timedelta(days=1)).isoformat()
        sel_sig, usados_sig, _ = _seleccion(dia_sig)
        tot = collections.defaultdict(lambda: [0, 0.0, 0.0])
        for d in usados_sig:
            for w, (n, sm, q) in json.loads((DIR / f"agg_{d}.json").read_text()).items():
                if w in sel_sig:
                    a = tot[w]; a[0] += n; a[1] += sm; a[2] += q
        (DIR / "watchlist.json").write_text(json.dumps(
            {"para_dia": dia_sig, "train_dias": usados_sig,
             "wallets": {w: {"n": v[0], "ev_medio": round(v[1] / v[0], 4)} for w, v in tot.items()}}))
    except Exception as e:
        print(f"(watchlist no escrita: {e})")
    with open(HIST, "a", encoding="utf-8") as f:
        f.write(json.dumps({"dia": dia, "ultimo_dia": dia_res, "pool_L1": s1, "veredicto": informe["veredicto"]}, ensure_ascii=False) + "\n")
    t1 = dia_res["test"][str(LSEL)] or {}
    msg = [f"🐋 Wallets 'primera compra' -- forward {dia} (sel. con {len(usados)} días previos: {len(sel)} wallets)",
           f"día: n={t1.get('n')} EV/€(L=1s)={t1.get('ev')} t_cluster={t1.get('t_cluster_mercado')} sin top5={t1.get('ev_sin_top5')}",
           f"pool {dias_test} día(s) test: n={s1 and s1['n']} mercados={s1 and s1['n_mercados']} EV/€={s1 and s1['ev']} "
           f"t_cluster={s1 and s1['t_cluster_mercado']} top5={s1 and s1['top5_share']} sin_top5={s1 and s1['ev_sin_top5']} "
           f"(t_cluster sin_top5={s1 and s1['t_cluster_sin_top5']})",
           f"veredicto: {informe['veredicto']}"]
    print("\n".join(msg))
    if enviar:
        try:
            sys.path.insert(0, str(REPO))
            from shadow_digest import enviar_telegram
            enviar_telegram("\n".join(msg))
        except Exception as e:
            print(f"(Telegram falló: {e})")
    return informe


def main():
    a = sys.argv[1:]
    if "--backfill" in a:
        i = a.index("--backfill")
        d0, d1 = date.fromisoformat(a[i + 1]), date.fromisoformat(a[i + 2])
        while d0 <= d1:
            ejecutar(d0.isoformat(), enviar=False)
            d0 += timedelta(days=1)
        return 0
    dia = a[a.index("--dia") + 1] if "--dia" in a else (datetime.now(timezone.utc).date() - timedelta(days=1)).isoformat()
    ejecutar(dia)
    return 0


if __name__ == "__main__":
    sys.exit(main())
