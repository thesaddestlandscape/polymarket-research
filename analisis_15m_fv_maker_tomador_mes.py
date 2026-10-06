#!/usr/bin/env python3
"""analisis_15m_fv_maker_tomador_mes.py -- misión "15m como activo autónomo", punto 3 (06-Oct), sobre el MES
(16-Sep..05-Oct, Javi: "hazlo con los datos del último mes"). ¿Cómo se cobra la única señal con información demostrada
en el 15m, el fair value Chainlink? (ronda 2: supera al azar al mismo precio, p_ind 0,015, pero como TOMADOR +0,003 a
latencia 0 → −0,041 a ~45 s → −0,066 a +215 ms.) Compara TOMADOR, MAKER informado que CANCELA, controles e HÍBRIDO.

Fuentes por día (mismas que analisis_15m_dataset_mes.py): fotos del libro 15m de ambos lados (libro_ambos_lados, ~45 s,
sin tamaños), ticks Chainlink RTDS source=chainlink (hora de RECEPCIÓN), referencia oficial de apertura (TWAP60 PolyBolt
o RTDS [e-62,e-3]), firehose de operaciones (polymarket_activity: tomador, outcome, lado, precio, tamaño; hora de
recepción ~0,9 s tarde -> se ANTEDATA 900 ms, lo que favorece el relleno frente a la cancelación: conservador),
desenlace oficial.

FV continuo: en cada foto se fija σ (300 s de ticks, como el dataset); entre fotos el FV se recalcula en cada tick de
Chainlink con ese σ y el tiempo restante real: FV(t') = Φ(ln(S(t')/ref) / (σ·sqrt(T_rest(t')))).

Estrategias (U = 0,03 / 0,05 / 0,10 fijados ANTES; LAT = 250 / 1000 ms de envío y de cancelación):
  TOMADOR       en la foto i, si FV_s − ask_s >= U: compra 5 acciones. Cota OPT = ask de la foto i; PES = ask de la
                foto siguiente. Comisión 0,07·p·(1−p).
  MAKER_INF     en la foto i, si FV_s − bid_s >= U: puja en bid_s desde t_i+LAT; se CANCELA en cuanto un tick de
                Chainlink deja FV_s − precio < U (efecto tick+LAT), o en la foto siguiente (+LAT) donde se re-decide.
  MAKER_CONTRA  control: cuando FV_s − bid_s <= −U (el FV dice que ese lado está CARO); cancela al dejar de serlo.
  MAKER_SIEMPRE línea base sin información: siempre en el mejor bid de ambos lados, sin cancelar (debe perder).
  HIBRIDO       MAKER_INF; si la ventana termina sin relleno y en la foto siguiente FV_s − ask_s >= U, cruza al ask.
  Relleno de un bid del lado s a precio b: fila del firehose "BUY s a p" (el dueño del bid consumido aparece siempre así;
  el firehose mezcla filas de tomador y de maker, ver auditoria_15m_datos.py), agregada por tx: OPT p <= b (cabeza de
  cola); PES p < b (la atravesó). Corregido el 06-Oct tras la auditoría (antes: venta tomadora de s o compra del contrario).
  5 acciones por relleno (o el tamaño de la operación si es menor), tope 50 por lado y mercado. Maker sin comisión y
  sin contar devoluciones. Solo entre inicio+5 s y cierre−10 s, precio en [0,05-0,95].
Estadística: unidad = MERCADO (YES+NO); IC90 por bootstrap de DÍAS; sin los 2 mejores días; DESC (16-28 Sep) y PRUEBA
(30-Sep..05-Oct) por separado (nada se ajusta: los umbrales son fijos); por moneda; selección adversa = acierto de lo
rellenado − FV medio en el instante del relleno.
Limitación: sin tamaños de cola ni libro entre fotos -> las dos cotas acotan, no miden, la cola real. El firehose (RTDS
activity) no se ha validado al 100 % contra el on-chain.
Uso: (ulimit -v 3500000; python3 analisis_15m_fv_maker_tomador_mes.py [--desde 2026-09-16] [--hasta 2026-10-05])
  -> datalogs/m15mes/fvmaker_D.csv (por mercado-lado) + resumen.  --solo-resumen para rehacer el resumen.
"""
import argparse
import bisect
import collections
import csv
import math
import random
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402
from analisis_b1_compradores_mes import refs_dia, twap_rtds  # noqa: E402
from analisis_15m_dataset_mes import DL, PR, abrir, fich, ts_ms  # noqa: E402

csv.field_size_limit(10 ** 7)
OUT = DL / "m15mes"
SH, MAX_SH = 5.0, 50.0
P_MIN, P_MAX = 0.05, 0.95
FEE = 0.07
UMBRALES = (0.03, 0.05, 0.10)
LATS = (250, 1000)
ANTEDATA_MS = 900
DESC = ("2026-09-16", "2026-09-28")
PRUEBA = ("2026-09-30", "2026-10-05")
CAMPOS = ["dia", "moneda", "market", "lado", "gana", "estr", "U", "lat", "cota", "acciones", "coste", "pnl", "fv_sum"]


def phi_v(z):
    from math import erf
    return 0.5 * (1 + np.vectorize(erf)(z / math.sqrt(2)))


def leer_dia(d):
    fl = fich(DL, "libro_ambos_lados", d)
    if not fl:
        return None
    fotos, info = collections.defaultdict(list), {}
    g = lambda x: float(x) if x not in ("", None) else None
    for r in csv.DictReader(abrir(fl)):
        if r["marco"] != "15min":
            continue
        try:
            t = ts_ms(r["timestamp_utc"])
            fin = int(datetime.fromisoformat(r["end_date"]).timestamp())
        except (ValueError, KeyError):
            continue
        v = (t, g(r["ask_yes"]), g(r["ask_no"]), g(r["bid_yes"]), g(r["bid_no"]))
        if None in v[1:] or v[3] > v[1] or v[4] > v[2]:
            continue                                     # incompleta o libro cruzado
        fotos[r["market_id"]].append(v)
        info[r["market_id"]] = (r["activo"], fin, r["condition_id"])
    for v in fotos.values():
        v.sort()
    conds = {v[2] for v in info.values()}
    # firehose -> por condition_id: lista (t_antedatado, lado_vendedor_equivalente, precio_en_ese_lado, tamaño)
    vend = collections.defaultdict(list)
    ff = fich(DL, "polymarket_activity", d)
    if ff:
        try:
            for r in csv.DictReader(abrir(ff)):
                if r["condition_id"] not in conds:
                    continue
                try:
                    t = ts_ms(r["timestamp_utc"]) - ANTEDATA_MS
                    p, sz = float(r["price"]), float(r["size"] or 0)
                except ValueError:
                    continue
                # AUDITORÍA 06-Oct (auditoria_15m_datos.py): el firehose trae la fila del TOMADOR (35 %) y la de cada
                # MAKER rellenado (65 %, con el lado del maker) y no hay forma fiable de distinguirlas sin on-chain.
                # Regla sin identidad: cuando se consumen bids del lado s a p, el dueño de ese bid aparece SIEMPRE como
                # "BUY s a p" (cruce normal o acuñación). Una compra tomadora de s a p <= nuestro bid solo es posible si
                # el ask bajó hasta nuestro bid, y entonces también nos habría llenado. -> filas BUY, agregadas por tx.
                if r["side"] != "BUY":
                    continue
                o = "YES" if r["outcome"] in ("Up", "Yes") else "NO"
                vend[r["condition_id"]].append((t, o, round(p, 4), sz, r["transaction_hash"]))
        except (EOFError, OSError):
            pass
    for k, v in list(vend.items()):
        agg = {}
        for t, o, p, sz, tx in v:                       # una operación por (tx, lado, precio)
            a = agg.setdefault((tx, o, p), [t, o, p, 0.0])
            a[3] += sz
        vend[k] = sorted(tuple(x) for x in agg.values())
    cl = collections.defaultdict(lambda: ([], []))
    for dd in ((date.fromisoformat(d) - timedelta(days=1)).isoformat(), d):
        fc = fich(PR, "chainlink", dd)
        if not fc:
            continue
        for r in csv.DictReader(abrir(fc)):
            if r.get("source", "chainlink") != "chainlink":
                continue
            try:
                cl[r["asset"]][0].append(ts_ms(r["timestamp_utc"]))
                cl[r["asset"]][1].append(float(r["price_usd"]))
            except (ValueError, KeyError):
                continue
    clv = {}
    for k, (a, b) in cl.items():
        o = np.argsort(a, kind="stable")
        clv[k] = (np.array(a, dtype=np.int64)[o], np.array(b)[o])
    return fotos, info, vend, clv


def sigma_en(ct, cp, t):
    k = np.searchsorted(ct, t, side="right") - 1
    k0 = np.searchsorted(ct, t - 300_000)
    if k < 0 or k - k0 < 21:
        return None
    pr = cp[k0:k + 1]
    r = np.diff(np.log(pr))
    r = r[r != 0]
    if len(r) < 20:
        return None
    dur = max(1.0, (ct[k] - ct[k0]) / 1000)
    return math.sqrt(float((r * r).sum()) / dur)


def procesar_dia(d, PB, RT):
    datos = leer_dia(d)
    if datos is None:
        print(f"  {d}: sin libro_ambos_lados")
        return 0
    fotos, info, vend, clv = datos
    des = desenlaces(set(fotos))
    filas = []
    for mid, fs in fotos.items():
        mo, fin, cond = info[mid]
        if mid not in des or mo not in clv:
            continue
        ini = fin - 900
        ref = PB.get((mo, ini)) or twap_rtds(RT, mo, ini)
        if ref is None:
            continue
        ct, cp = clv[mo]
        t_lo, t_hi = ini * 1000 + 5000, fin * 1000 - 10_000
        fs = [f for f in fs if t_lo <= f[0] <= t_hi]
        if len(fs) < 2:
            continue
        # ticks del mercado y FV continuo con σ de la foto vigente
        a, b = np.searchsorted(ct, fs[0][0]), np.searchsorted(ct, t_hi, side="right")
        tt, pp = ct[a:b], cp[a:b]
        sig = [sigma_en(ct, cp, f[0]) for f in fs]
        fv_tick = np.full(len(tt), np.nan)
        tf = np.array([f[0] for f in fs])
        if len(tt):
            jf = np.searchsorted(tf, tt, side="right") - 1
            s_arr = np.array([s if s else np.nan for s in sig])[np.clip(jf, 0, None)]
            T = np.maximum(1.0, fin - tt / 1000)
            fv_tick = phi_v(np.log(pp / ref) / (s_arr * np.sqrt(T)))
        fv_foto = []
        for f, s in zip(fs, sig):
            k = np.searchsorted(ct, f[0], side="right") - 1
            if k < 0 or not s:
                fv_foto.append(np.nan)
                continue
            fv_foto.append(float(phi_v(np.array([math.log(cp[k] / ref) / (s * math.sqrt(max(1.0, fin - f[0] / 1000)))]))[0]))
        V = vend.get(cond, [])
        vt = [x[0] for x in V]
        for lado in ("YES", "NO"):
            gana = 1.0 if des[mid] == lado else 0.0
            fvF = np.array(fv_foto) if lado == "YES" else 1 - np.array(fv_foto)
            fvT = fv_tick if lado == "YES" else 1 - fv_tick
            bid = [f[3] if lado == "YES" else f[4] for f in fs]
            ask = [f[1] if lado == "YES" else f[2] for f in fs]
            fills_lado = [(x[0], x[2], x[3]) for x in V if x[1] == lado]
            ft = [x[0] for x in fills_lado]

            def fv_en(t):
                k = np.searchsorted(tt, t, side="right") - 1
                return fvT[k] if k >= 0 and not np.isnan(fvT[k]) else fvF[max(0, np.searchsorted(tf, t, side="right") - 1)]

            def simular(cond_foto, sigue, lat, cota, hibrido_U=None):
                sh = coste = pnl = fvs = 0.0
                for i in range(len(fs)):
                    if sh >= MAX_SH or not (P_MIN <= bid[i] <= P_MAX) or np.isnan(fvF[i]) or not cond_foto(fvF[i], bid[i]):
                        continue
                    pr = bid[i]
                    t_on = fs[i][0] + lat
                    t_off = (fs[i + 1][0] + lat) if i + 1 < len(fs) else t_hi
                    if sigue is not None and len(tt):
                        k0, k1 = np.searchsorted(tt, fs[i][0], side="right"), np.searchsorted(tt, t_off - lat, side="right")
                        malos = np.flatnonzero(~sigue(fvT[k0:k1], pr))
                        if len(malos):
                            t_off = min(t_off, int(tt[k0 + malos[0]]) + lat)
                    lleno_aqui = 0.0
                    if t_off > t_on:
                        for j in range(bisect.bisect_left(ft, t_on), bisect.bisect_left(ft, t_off)):
                            _, p, sz = fills_lado[j]
                            if (p < pr - 1e-9) if cota == "PES" else (p <= pr + 1e-9):
                                q = min(SH, sz, MAX_SH - sh)
                                if q <= 0:
                                    break
                                sh += q
                                lleno_aqui += q
                                coste += q * pr
                                pnl += q * (gana - pr)
                                fvs += q * fv_en(ft[j])
                    if hibrido_U is not None and not lleno_aqui and i + 1 < len(fs) and sh < MAX_SH:
                        a2 = ask[i + 1]
                        if P_MIN <= a2 <= P_MAX and not np.isnan(fvF[i + 1]) and fvF[i + 1] - a2 >= hibrido_U:
                            q = min(SH, MAX_SH - sh)
                            f = FEE * a2 * (1 - a2)
                            sh += q
                            coste += q * (a2 + f)
                            pnl += q * (gana - a2 - f)
                            fvs += q * fvF[i + 1]
                return sh, coste, pnl, fvs

            def guardar(estr, U, lat, cota, r):
                if r[0] > 0:
                    filas.append([d, mo, mid, lado, gana, estr, U, lat, cota, r[0], round(r[1], 4), round(r[2], 4),
                                  round(r[3], 4)])

            for cota in ("OPT", "PES"):
                guardar("MAKER_SIEMPRE", 0, 0, cota, simular(lambda fv, b: True, None, 0, cota))
            for U in UMBRALES:
                for cota in ("OPT", "PES"):
                    sh = coste = pnl = fvs = 0.0
                    for i in range(len(fs)):
                        if sh >= MAX_SH or np.isnan(fvF[i]) or fvF[i] - ask[i] < U:
                            continue
                        p = ask[i] if cota == "OPT" else (ask[i + 1] if i + 1 < len(fs) else None)
                        if p is None or not (P_MIN <= p <= P_MAX):
                            continue
                        q = min(SH, MAX_SH - sh)
                        f = FEE * p * (1 - p)
                        sh += q
                        coste += q * (p + f)
                        pnl += q * (gana - p - f)
                        fvs += q * fvF[i]
                    guardar("TOMADOR", U, 0, cota, (sh, coste, pnl, fvs))
                    for lat in LATS:
                        guardar("MAKER_INF", U, lat, cota, simular(lambda fv, b, U=U: fv - b >= U,
                                                                   lambda fvs_, b, U=U: fvs_ - b >= U, lat, cota))
                        guardar("MAKER_CONTRA", U, lat, cota, simular(lambda fv, b, U=U: fv - b <= -U,
                                                                      lambda fvs_, b, U=U: fvs_ - b <= -U, lat, cota))
                        guardar("HIBRIDO", U, lat, cota, simular(lambda fv, b, U=U: fv - b >= U,
                                                                 lambda fvs_, b, U=U: fvs_ - b >= U, lat, cota,
                                                                 hibrido_U=U))
    with open(OUT / f"fvmaker_{d}.csv", "w", newline="") as fo:
        w = csv.writer(fo)
        w.writerow(CAMPOS)
        w.writerows(filas)
    print(f"  {d}: mercados {len(fotos)}, filas {len(filas)}", flush=True)
    return len(filas)


def resumen():
    import pandas as pd
    fs = sorted(OUT.glob("fvmaker_2026-*.csv"))
    df = pd.concat([pd.read_csv(f, dtype={"market": str}) for f in fs], ignore_index=True)
    print(f"\nRESUMEN ({len(fs)} días, {df['market'].nunique()} mercados con algún relleno)")
    rng = random.Random(7)
    clave = ["estr", "U", "lat", "cota"]
    print(f"{'estrategia':13} {'U':>4} {'lat':>4} {'cota':>4} | {'merc':>6} {'acc':>7} {'$/merc':>7} {'PnL/€':>7} | "
          f"{'IC90 días $/merc':>18} {'d+':>5} {'sin2':>7} | {'DESC':>7} {'PRUEBA':>7} | {'acierto':>7} {'FV':>6} "
          f"{'s.adv':>6} | por moneda PnL/€")
    for k, g in df.groupby(clave, sort=True):
        pm = g.groupby(["dia", "market"])[["pnl", "coste"]].sum().reset_index()
        pdia = pm.groupby("dia").agg(p=("pnl", "sum"), n=("pnl", "size"), c=("coste", "sum"))
        P, N = pdia["p"].values, pdia["n"].values
        bs = []
        for _ in range(2000):
            ix = [rng.randrange(len(P)) for _ in P]
            bs.append(P[ix].sum() / N[ix].sum())
        bs.sort()
        o = np.argsort(-P)
        sin2 = (P.sum() - P[o[:2]].sum()) / (N.sum() - N[o[:2]].sum())
        dsc = pm[(pm.dia >= DESC[0]) & (pm.dia <= DESC[1])]
        pru = pm[(pm.dia >= PRUEBA[0]) & (pm.dia <= PRUEBA[1])]
        acc = g["acciones"].sum()
        acierto = (g["acciones"] * g["gana"]).sum() / acc
        fvm = g["fv_sum"].sum() / acc
        mon = g.groupby("moneda")[["pnl", "coste"]].sum()
        print(f"{k[0]:13} {k[1]:4.2f} {k[2]:4} {k[3]:>4} | {len(pm):6} {acc:7.0f} {pm.pnl.mean():+7.3f} "
              f"{g.pnl.sum() / g.coste.sum():+7.3f} | ({bs[100]:+.3f},{bs[1899]:+.3f}) {(P > 0).sum():2}/{len(P)} "
              f"{sin2:+7.3f} | {dsc.pnl.mean():+7.3f} {pru.pnl.mean():+7.3f} | {acierto:7.3f} {fvm:6.3f} "
              f"{acierto - fvm:+6.3f} | " + " ".join(f"{m}:{r.pnl / r.coste:+.2f}" for m, r in mon.iterrows()))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--desde", default="2026-09-16")
    ap.add_argument("--hasta", default="2026-10-05")
    ap.add_argument("--solo-resumen", action="store_true")
    a = ap.parse_args()
    if not a.solo_resumen:
        d0, d1 = date.fromisoformat(a.desde), date.fromisoformat(a.hasta)
        dias = [(d0 + timedelta(days=i)).isoformat() for i in range((d1 - d0).days + 1)]
        PB, RT = {}, collections.defaultdict(lambda: [0.0, 0])
        for d in [(d0 - timedelta(days=1)).isoformat()] + dias:
            refs_dia(d, PB, RT)
        for d in dias:
            procesar_dia(d, PB, RT)
    resumen()


if __name__ == "__main__":
    main()
