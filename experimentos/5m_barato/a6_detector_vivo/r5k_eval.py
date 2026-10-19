#!/usr/bin/env python3
"""r5k_eval.py -- A6: precisión y latencia del detector en vivo de H43 R5K contra on-chain (solo lectura).

Repite offline, con el detector `DetectorR5K` y los eventos CRUDOS de libro5 (T = last_trade_price con hora de recepción;
G = huecos; B = snapshots), lo que haría en vivo, y lo compara con las filas de banda on-chain de pass1.py
(m5_onchain, maker/tomador explícitos) para los mismos mercados BTC 5m.
Uso: python3 -I r5k_eval.py --desde ISO --hasta ISO --tg f1.TG.gz ... --b f1.B.gz ... --k k1.csv ... --band b1.csv.gz ... --out out.json
Sin red salvo que falte el desenlace en caché (no se llama: se reporta como missing)."""
import argparse
import bisect
import json
import os
import random
import statistics
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from detector_r5k import DetectorR5K, normalizar, OFFSET, K, T_MIN, T_MAX, T_COS_MAX, BANDA_LO, BANDA_HI  # noqa: E402
from r5k_io import tokens_btc5, eventos_libro5, banda_cadena_cruda, desenlaces_cache, desenlaces_gamma, tomadores_cadena  # noqa: E402


def pct(v, qs=(5, 25, 50, 75, 95)):
    v = sorted(v)
    if not v:
        return None
    return {f"p{q}": round(v[min(len(v) - 1, int(len(v) * q / 100))], 3) for q in qs}


def unid_cosechable(rows, des):
    """MISMO criterio que h43_auditoria_datos/a4_definicion_k_y_regimen.py::unid_cosechable. rows: (ts, ord, mkt, lado, acc,
    coste, T, pc). Devuelve {(mkt,lado): {c, p, acc, completa, take}}; sin desenlace -> sin unidad (se cuenta aparte)."""
    seq = defaultdict(list)
    for r in sorted(rows, key=lambda r: (r[2], r[3], r[0], r[1])):
        seq[(r[2], r[3])].append(r)
    U, sin_des = {}, 0
    for k, lst in seq.items():
        mkt, lado = k
        cum, crossed, need, take = 0.0, False, K, []
        for ts, _o, _m, _l, acc, coste, T, pc in lst:
            if not crossed:
                new = cum + acc
                if new >= OFFSET:
                    crossed = True
                    cand = min(new - OFFSET, acc)
                else:
                    cum = new
                    continue
            else:
                cand = acc
            if not (T_MIN < T <= T_COS_MAX):
                continue
            th = min(cand, need)
            if th <= 0:
                continue
            take.append((pc, th, ts))
            need -= th
            if need <= 1e-9:
                break
        if not take:
            continue
        g = des.get(mkt)
        if g is None:
            sin_des += 1
            continue
        c = sum(t * p for p, t, _ in take)
        pnl = sum(t * ((1.0 if g == lado else 0.0) - p) for p, t, _ in take)
        U[k] = {"c": c, "p": pnl, "acc": K - need, "completa": need <= 1e-9, "take": take, "t0": take[0][2]}
    return U, sin_des


def ev(us):
    c = sum(u["c"] for u in us)
    p = sum(u["p"] for u in us)
    return {"n": len(us), "coste": round(c, 2), "pnl": round(p, 2), "ev": round(p / c, 4) if c else None}


def ic90_cierre(grupos, B=2000, seed=11):
    g = list(grupos.values())
    if len(g) < 3:
        return None
    r = random.Random(seed)
    bs = []
    for _ in range(B):
        m = [r.choice(g) for _ in g]
        c = sum(x[0] for x in m)
        bs.append(sum(x[1] for x in m) / c if c else 0.0)
    bs.sort()
    return [round(bs[int(B * .05)], 3), round(bs[int(B * .95) - 1], 3)]


def tomadores_cadena_total(onchain_files, tok):
    out = []
    for f in onchain_files:
        out += tomadores_cadena(f, tok)
    return out


def emparejar_tk(tk_ch, ws_all, w_lo=-4.0, w_hi=25.0):
    """tk_ch: (ts_est, tx, li, token, side, shares, usdc); ws_all: (token, side, size, recv_s, price, mkt). Voraz por hora;
    clave (token, side), tamaño ±2e-3(+1e-4 rel.), ts_cadena - recv en [w_lo, w_hi]. Devuelve (parejas(gi,i,lag), ch_sin, ws_sin)."""
    por = defaultdict(list)
    for i, w in enumerate(ws_all):
        por[(w[0], w[1])].append((w[3], w[2], i))
    for v in por.values():
        v.sort()
    usado, parejas = set(), []
    for gi in sorted(range(len(tk_ch)), key=lambda g: tk_ch[g][0]):
        ts, _tx, _li, t, side, sh, _usd = tk_ch[gi]
        lst = por.get((t, side), [])
        tl = [x[0] for x in lst]
        j = bisect.bisect_left(tl, ts - w_hi)
        while j < len(lst) and lst[j][0] <= ts - w_lo:
            if lst[j][2] not in usado and abs(lst[j][1] - sh) <= 2e-3 + 1e-4 * sh:
                usado.add(lst[j][2])
                parejas.append((gi, lst[j][2], ts - lst[j][0]))
                break
            j += 1
    pa = {g for g, _i, _l in parejas}
    return parejas, [g for g in range(len(tk_ch)) if g not in pa], [i for i in range(len(ws_all)) if i not in usado]


def emparejar(ch_grupos, ws_ev, w_lo=-3.0, w_hi=25.0):
    """Empareja grupos on-chain (tx, mkt, lado, pc2, acc_suma, ts) con eventos WS (mkt, lado, pc2, size, recv_s) por clave,
    tamaño (±2e-3) y hora (ts_cadena - recv_s en [w_lo, w_hi]); voraz en orden de hora. Devuelve (parejas, ch_sin, ws_sin)."""
    por = defaultdict(list)
    for i, (m, l, pc, sz, t) in enumerate(ws_ev):
        por[(m, l, pc)].append((t, sz, i))
    for v in por.values():
        v.sort()
    usado = set()
    parejas, ch_sin = [], []
    for gi, (tx, m, l, pc, acc, ts) in sorted(enumerate(ch_grupos), key=lambda x: x[1][5]):
        lst = por.get((m, l, pc), [])
        ts_list = [x[0] for x in lst]
        j = bisect.bisect_left(ts_list, ts - w_hi)
        mejor = None
        while j < len(lst) and lst[j][0] <= ts - w_lo:
            t, sz, i = lst[j]
            if i not in usado and abs(sz - acc) <= 2e-3 + 1e-4 * acc:
                lag = ts - t
                if mejor is None or lag < mejor[0]:         # el más cercano hacia atrás (WS llega ANTES que el bloque)
                    mejor = (lag, i)
                    break
            j += 1
        if mejor is None:
            ch_sin.append(gi)
        else:
            usado.add(mejor[1])
            parejas.append((gi, mejor[1], mejor[0]))
    ws_sin = [i for i in range(len(ws_ev)) if i not in usado]
    return parejas, ch_sin, ws_sin


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--desde", required=True)
    ap.add_argument("--hasta", required=True)
    ap.add_argument("--tg", nargs="+", required=True)
    ap.add_argument("--b", nargs="*", default=[])
    ap.add_argument("--k", nargs="+", required=True)
    ap.add_argument("--onchain", nargs="+", required=True, help="m5_onchain_D.csv.gz (filas F del exchange)")
    ap.add_argument("--out", required=True)
    ap.add_argument("--gamma-cache", default=None, help="si se da, completa los desenlaces que falten con gamma pública (caché propia)")
    a = ap.parse_args()
    d0 = datetime.fromisoformat(a.desde.replace("Z", "+00:00")).timestamp()
    d1 = datetime.fromisoformat(a.hasta.replace("Z", "+00:00")).timestamp()
    tok = tokens_btc5(a.k)
    tok = {t: v for t, v in tok.items() if d0 <= v[2] <= d1}
    mkts = {v[0] for v in tok.values()}
    cierre = {v[0]: v[2] for v in tok.values()}
    print(f"tokens BTC5 en ventana: {len(tok)} ({len(mkts)} mercados)", flush=True)

    # ---- 1) repetición en vivo con el detector ----
    det = DetectorR5K(tok, max_edad_s=10 ** 9)           # sin poda: evaluamos al final
    t_proc, n_ev, ultimo_recv = 0.0, 0, None
    lag_feed, lag_recv_ev = [], []
    ws_all = []                                          # (token, side, size, recv_s, price, mkt) de TODO T de los tokens BTC5 en ventana
    ficheros = {}
    for e in eventos_libro5(a.tg, a.b, tok):
        if e[0] == "T":
            _, recv, t_ev, tk, pr, side, sz = e
            mk, lado_tk, cie = tok[tk]
            if not (d0 - 400 <= recv / 1000.0 <= d1 + 10):
                continue
            ws_all.append((tk, side, sz, recv / 1000.0, pr, mk))
            lag_feed.append(recv - t_ev)
            t0 = time.perf_counter()
            det.on_trade(tk, recv, pr, side, sz)
            t_proc += time.perf_counter() - t0
            n_ev += 1
            ultimo_recv = recv
        elif e[0] == "G":
            if e[3] == "baja":
                continue                                  # token retirado por cierre: no es pérdida
            if e[3] == "arranque" and ultimo_recv is not None:
                det.on_gap(None, ultimo_recv)             # proceso nuevo: hueco desde el último evento del anterior
            det.on_gap(e[2], e[1])
            ultimo_recv = e[1]
        else:
            det.on_snapshot(e[2], e[1])
            ultimo_recv = e[1]
    print(f"eventos T procesados {n_ev}, detector {t_proc / max(n_ev, 1) * 1e6:.1f} us/evento, filas banda {len(det.filas)}", flush=True)

    # ---- 2) verdad on-chain ----
    ch = [r for f in a.onchain for r in banda_cadena_cruda(f, tok) if r["mkt"] in mkts]
    print(f"filas banda on-chain en ventana: {len(ch)}", flush=True)
    des = desenlaces_cache()
    if a.gamma_cache:
        des.update(desenlaces_gamma([m for m in mkts if m not in des], a.gamma_cache))
    cobertura_des = sum(1 for m in mkts if m in des)
    completo = {m: det.completo(m, cierre[m]) for m in mkts}

    # ---- 3) emparejado por ORDEN TOMADORA: un last_trade_price del WS = una orden tomadora on-chain (size exacto) ----
    tk_ch = [x for x in tomadores_cadena_total(a.onchain, tok) if d0 - 400 <= x[0] <= d1 + 10]
    parejas, ch_sin, ws_sin = emparejar_tk(tk_ch, ws_all)

    def en_cobertura(m):
        return completo.get(m, False)

    def en_banda_t(m, t_s):
        return T_MIN + 10 < cierre[m] - t_s <= T_MAX - 10        # interior: evita el sesgo del T estimado por bloque en los bordes

    mp_ch = {gi: (i, lag) for gi, i, lag in parejas}
    mp_ws = {i: gi for gi, i, lag in parejas}
    res = {"ventana": [a.desde, a.hasta], "mercados": len(mkts), "mercados_completos": sum(completo.values()),
           "cobertura_desenlace": f"{cobertura_des}/{len(mkts)}", "detector_us_por_evento": round(t_proc / max(n_ev, 1) * 1e6, 2),
           "n_eventos_T_btc5": n_ev}
    for etiqueta, filtro in (("todos", lambda m: True), ("solo_cobertura_completa", en_cobertura)):
        ch_t = [gi for gi in range(len(tk_ch)) if filtro(tok[tk_ch[gi][3]][0])]
        ws_t = [i for i in range(len(ws_all)) if filtro(ws_all[i][5])]
        ch_ok = [gi for gi in ch_t if gi in mp_ch]
        ws_ok = [i for i in ws_t if i in mp_ws]
        vch = lambda L: sum(tk_ch[g][5] for g in L)
        vws = lambda L: sum(ws_all[i][2] for i in L)
        res[f"eventos_orden_tomadora|{etiqueta}"] = {
            "ordenes_cadena": len(ch_t), "con_pareja_ws": len(ch_ok), "recall": round(len(ch_ok) / len(ch_t), 5) if ch_t else None,
            "recall_volumen": round(vch(ch_ok) / vch(ch_t), 5) if ch_t else None,
            "eventos_ws": len(ws_t), "ws_con_pareja_cadena": len(ws_ok),
            "precision": round(len(ws_ok) / len(ws_t), 5) if ws_t else None,
            "precision_volumen": round(vws(ws_ok) / vws(ws_t), 5) if ws_t else None}
    # los que faltan: ¿dentro de un hueco conocido del feed?
    falt = [gi for gi in range(len(tk_ch)) if gi not in mp_ch]
    en_h = [gi for gi in falt if det.en_hueco(tok[tk_ch[gi][3]][0], tk_ch[gi][0] * 1000.0 - 2200)]
    res["ordenes_cadena_sin_pareja"] = {"n": len(falt), "dentro_de_hueco_conocido": len(en_h), "sin_hueco_conocido": len(falt) - len(en_h),
                                        "volumen_acc": round(sum(tk_ch[g][5] for g in falt), 1)}
    lags = [lag for gi, i, lag in parejas]
    res["lag_cadena_menos_recepcion_s"] = {"n": len(lags), **(pct(lags, (1, 5, 25, 50, 75, 95, 99)) or {})}
    res["feed_recepcion_menos_t_msg_ms"] = {"n": len(lag_feed), **(pct(lag_feed, (5, 25, 50, 75, 90, 99)) or {})}
    dp = defaultdict(int)
    for gi, i, lag in parejas:
        usd, sh = tk_ch[gi][6], tk_ch[gi][5]
        dp[round(ws_all[i][4] - round(usd / sh, 2), 2)] += 1
    tot = sum(dp.values())
    res["precio_ws_menos_precio_medio_cadena_redondeado"] = {"n": tot, "exacto": round(dp.get(0.0, 0) / tot, 4) if tot else None,
                                                             "dentro_1c": round((dp.get(0.0, 0) + dp.get(0.01, 0) + dp.get(-0.01, 0)) / tot, 4) if tot else None}

    # ---- 4) acumulado por unidad y cruce ----
    cum_ch, cum_ws = defaultdict(float), defaultdict(float)
    for r in ch:
        cum_ch[(r["mkt"], r["lado"])] += r["acc"]
    for key, v in det.cum.items():
        cum_ws[key] = v
    claves = {(m, l) for m in mkts for l in ("YES", "NO")}
    def comp_cum(filtro):
        err_rel, err_abs, dentro5, dentro10, n = [], [], 0, 0, 0
        for k in claves:
            if not filtro(k) or cum_ch.get(k, 0.0) < 500:
                continue
            c, w = cum_ch[k], cum_ws.get(k, 0.0)
            n += 1
            e = (w - c) / c
            err_rel.append(e)
            err_abs.append(w - c)
            dentro5 += abs(e) <= 0.05
            dentro10 += abs(e) <= 0.10
        return {"n_unidades_cum_cadena_ge500": n, "error_relativo_ws_vs_cadena": pct(err_rel), "error_abs_acc": pct(err_abs),
                "dentro_5pct": dentro5, "dentro_10pct": dentro10}
    res["cum|todas"] = comp_cum(lambda k: True)
    res["cum|cobertura_completa"] = comp_cum(lambda k: en_cobertura(k[0]))
    def confusion(filtro):
        tp = fp = fn = tn = 0
        for k in claves:
            if not filtro(k):
                continue
            c, w = cum_ch.get(k, 0.0) >= OFFSET, cum_ws.get(k, 0.0) >= OFFSET
            tp += c and w
            fp += (not c) and w
            fn += c and (not w)
            tn += (not c) and (not w)
        return {"TP": tp, "FP": fp, "FN": fn, "TN": tn,
                "acuerdo_cruce": round((tp + tn) / max(tp + fp + fn + tn, 1), 4),
                "precision": round(tp / (tp + fp), 4) if tp + fp else None, "recall": round(tp / (tp + fn), 4) if tp + fn else None}
    res["cruce_5000|todas"] = confusion(lambda k: True)
    res["cruce_5000|cobertura_completa"] = confusion(lambda k: en_cobertura(k[0]))
    # tiempos de cruce
    ch_rows = sorted(((r["ts"], r["li"], r["mkt"], r["lado"], r["acc"], r["coste"], r["T"], r["pc"]) for r in ch),
                     key=lambda r: (r[2], r[3], r[0], r[1]))
    cruce_ch, cum = {}, defaultdict(float)
    for ts, li, m, l, acc, _c, T, pc in ch_rows:
        cum[(m, l)] += acc
        if (m, l) not in cruce_ch and cum[(m, l)] >= OFFSET:
            cruce_ch[(m, l)] = ts
    dif = []
    for c in det.cruces:
        k = (c["mkt"], c["lado"])
        if k in cruce_ch and en_cobertura(c["mkt"]):
            dif.append(cruce_ch[k] - c["t_recv_ms"] / 1000.0)
    res["cruce_t_cadena_menos_t_ws_s"] = {"n": len(dif), **(pct(dif) or {})}

    # ---- 5) unidades R5K y EV con desenlace oficial (mismo código para las dos fuentes) ----
    rows_ws = [(f[0], i, f[1], f[2], f[3], f[4], f[5], f[6]) for i, f in enumerate(det.filas)]
    U_ws, sd_ws = unid_cosechable(rows_ws, des)
    U_ch, sd_ch = unid_cosechable([(r["ts"], r["li"], r["mkt"], r["lado"], r["acc"], r["coste"], r["T"], r["pc"]) for r in ch], des)
    solo_det = det.unidades()
    res["unidades"] = {"ws": ev(list(U_ws.values())), "cadena": ev(list(U_ch.values())), "sin_desenlace": {"ws": sd_ws, "cadena": sd_ch}}
    # el detector (estado en línea) debe dar las MISMAS unidades que el recomputo offline sobre sus filas
    coinc = sum(1 for k, u in solo_det.items() if k in U_ws and abs(sum(p * t for p, t, _ in u["take"]) - U_ws[k]["c"]) < 1e-6)
    res["autoconsistencia_detector_vs_recomputo"] = {"unidades_detector": len(solo_det), "coinciden_coste": coinc}
    for etiqueta, filtro in (("todas", lambda k: True), ("cobertura_completa", lambda k: en_cobertura(k[0]))):
        kw, kc = {k for k in U_ws if filtro(k)}, {k for k in U_ch if filtro(k)}
        both = kw & kc
        res[f"unidades|{etiqueta}"] = {
            "solo_cadena": len(kc - kw), "solo_ws": len(kw - kc), "ambas": len(both),
            "ev_cadena": ev([U_ch[k] for k in kc]), "ev_ws": ev([U_ws[k] for k in kw]),
            "en_ambas|ev_cadena": ev([U_ch[k] for k in both]), "en_ambas|ev_ws": ev([U_ws[k] for k in both]),
            "solo_cadena|ev": ev([U_ch[k] for k in kc - kw]), "solo_ws|ev": ev([U_ws[k] for k in kw - kc]),
            "precio_medio_dif_en_ambas": pct([U_ws[k]["c"] / U_ws[k]["acc"] - U_ch[k]["c"] / U_ch[k]["acc"] for k in both
                                              if U_ws[k]["acc"] and U_ch[k]["acc"]])}
        gws = defaultdict(lambda: [0.0, 0.0])
        for k in kw:
            u = U_ws[k]
            f = cierre[k[0]]
            gws[f][0] += u["c"]
            gws[f][1] += u["p"]
        res[f"unidades|{etiqueta}"]["ic90_cierre_ev_ws"] = ic90_cierre(gws)
    # ventana operable: tiempo desde el cruce detectado hasta consumir las K acciones (población)
    ven = []
    for k, u in solo_det.items():
        if u["completa"] and en_cobertura(k[0]):
            ven.append((u["take"][-1][2] - u["t_cruce_ms"]) / 1000.0)
    res["ventana_cruce_a_cosecha_completa_s"] = {"n": len(ven), **(pct(ven) or {})}
    Tc = [c["T"] for c in det.cruces if en_cobertura(c["mkt"])]
    res["T_restante_al_cruce_s"] = {"n": len(Tc), **(pct(Tc) or {})}
    res["huecos"] = {"mercados_incompletos": len(mkts) - sum(completo.values()), "stats_detector": dict(det.stats)}
    json.dump(res, open(a.out, "w"), indent=1, ensure_ascii=False)
    print(json.dumps(res, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
