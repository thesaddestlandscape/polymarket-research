#!/usr/bin/env python3
"""h61b_vigia.py -- vigia diario del brazo C (H61b) EMPAREJADO con v3. Aplica el gate del JSON CONGELADO (../H61b_CONGELADA.json, sha verificado) sin retocarlo. Solo lectura de DL/h61b/rows_*.
Datos validos: dias >= 2026-10-22 (campo `datos_validos`). Los dias previos (DISC 06-18 / 19-21) solo salen como DESCRIPTIVO ciego en --descriptivo (NO cuentan para el gate).
Lectura del gate (definiciones explicitas, ninguna cambia la regla):
  retencion      = n_cierres con relleno en C / n_cierres con relleno en v3, misma celda (cola base, 79/60, tamano real, un relleno cierra), por brazo
  n_C            = n_cierres con relleno en C (con desenlace oficial)
  dEV pond       = EV_pond(C) - EV_pond(v3), IC90 por DIAS (bootstrap de dias; no estimable con <5 dias)
  gate H23 (C)   = n>=40, >=10 dias, EV pond>=+0,10, IC90 dias>0, sin 2 mejores dias>0
  kill           = EV pond de C sin 2 mejores dias < -0,15 con n>=20
Estado por brazo/feed: INSUFICIENTE (<5 dias o n<5) | EN_CURSO | KILL | GATE_OK_SOLO_DRY_RUN. Ninguno autoriza dinero real. Uso: python3 -I h61b_vigia.py [--coin BTC] [--hasta D] [--descriptivo] [--telegram]"""
import json, os, sys, datetime
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import h61b_regla as RG
import h61b_stats as S

CEL = dict(cola="base", lp=79, lc=60, mult=1, modo="primer")


def evaluar_brazo(rows_por_dia, brazo, feed, gate=RG.GATE):
    rows = [r for rs in rows_por_dia.values() for r in rs]
    pv = S.posiciones(rows, "v3", brazo, **CEL); pc = S.posiciones(rows, feed, brazo, **CEL)
    evc = S.ev_dias([(d, x, c) for d, x, c, *_ in pc.values()]); evv = S.ev_dias([(d, x, c) for d, x, c, *_ in pv.values()])
    nC, nV = len(pc), len(pv)
    miss_c = sum(1 for v in pc.values() if v[1] is None)
    dif = S.dif_ev_dias(pc, pv)
    ret = (nC / nV) if nV else float("nan")
    g = gate["h23"]
    isnan = lambda x: x != x
    h23_ok = bool(evc.get("n", 0) >= g["n"] and evc.get("dias", 0) >= g["dias"] and evc.get("ev", -9) >= g["ev_pond_min"] and not isnan(evc.get("ic90_lo", float("nan"))) and evc["ic90_lo"] > 0
                  and not isnan(evc.get("sin2", float("nan"))) and evc["sin2"] > g["sin2_min"])
    h61_ok = bool(ret >= gate["retencion_min"] and evc.get("n", 0) >= gate["n_cierres_C_min"] and not isnan(dif.get("ic90_lo", float("nan"))) and dif.get("dev", -1) > 0 and dif["ic90_lo"] > 0)
    k = gate["kill"]
    kill = bool(evc.get("n", 0) >= k["n"] and not isnan(evc.get("sin2", float("nan"))) and evc["sin2"] < k["ev_pond_sin2_max"])
    ndias = len({d for d in rows_por_dia})
    if kill: est = "KILL"
    elif ndias < S.MIN_DIAS_IC or evc.get("n", 0) < 5: est = "INSUFICIENTE"
    elif h23_ok and h61_ok: est = "GATE_OK_SOLO_DRY_RUN"
    else: est = "EN_CURSO"
    return dict(brazo=brazo, feed=feed, estado=est, dias_datos=ndias, n_v3=nV, n_C=nC, retencion=ret, pos_sin_desenlace_C=miss_c, ev_C=evc, ev_v3=evv, dif=dif, gate_h23_C=h23_ok, gate_h61b=h61_ok, kill=kill)


def cargar(coin, desde, hasta, prefijo="rows"):
    return {d: S.leer_dia(f) for d, f in S.dias_con_datos(coin, desde, hasta, prefijo=prefijo)}


def informe(coin="BTC", desde=RG.DATOS_VALIDOS_DESDE, hasta=None, prefijo="rows", brazos=("A", "B")):
    sha = RG.verificar_congelada()
    hoy = datetime.datetime.utcnow().strftime("%Y-%m-%d")
    por_dia = {d: r for d, r in cargar(coin, desde, hasta, prefijo).items() if d < hoy}      # el dia en curso nunca cuenta
    res = dict(congelada_sha=sha, codigo_sha=RG.hash_codigo(), coin=coin, desde=desde, dias=sorted(por_dia), brazos=[])
    feeds = sorted({r["var"] for rs in por_dia.values() for r in rs if r["var"].startswith("C_")})
    for feed in feeds:
        for brazo in brazos:
            res["brazos"].append(evaluar_brazo(por_dia, brazo, feed))
    return res


def texto(res):
    L = [f"H61b vigia {res['coin']} (congelada sha {res['congelada_sha']}) datos validos >= {res['desde']}: {len(res['dias'])} dias {res['dias']}"]
    f = lambda x: "n/e" if x != x else f"{x:+.3f}"
    for b in res["brazos"]:
        e, v, d = b["ev_C"], b["ev_v3"], b["dif"]
        L.append(f"[{b['brazo']}/{b['feed']}] {b['estado']}  retencion {f(b['retencion'])} (nC={b['n_C']}/nV={b['n_v3']}, sin desenlace {b['pos_sin_desenlace_C']})  "
                 f"EV_C {f(e.get('ev', float('nan')))} IC90d ({f(e.get('ic90_lo', float('nan')))},{f(e.get('ic90_hi', float('nan')))}) sin2 {f(e.get('sin2', float('nan')))}  "
                 f"EV_v3 {f(v.get('ev', float('nan')))}  dEV {f(d.get('dev', float('nan')))} IC90d ({f(d.get('ic90_lo', float('nan')))},{f(d.get('ic90_hi', float('nan')))}) dPnL {f(d.get('dpnl_total', float('nan')))}  "
                 f"gateH23 {b['gate_h23_C']} gateH61b {b['gate_h61b']} kill {b['kill']}")
    return "\n".join(L)


def main():
    a = sys.argv[1:]
    coin = a[a.index("--coin") + 1] if "--coin" in a else "BTC"
    hasta = a[a.index("--hasta") + 1] if "--hasta" in a else None
    desde = a[a.index("--desde") + 1] if "--desde" in a else RG.DATOS_VALIDOS_DESDE
    ext = "--ext" in a
    res = informe(coin, desde, hasta, "rows_ext", ("U00", "U01", "U10")) if ext else informe(coin, desde, hasta)
    nom = "h61c_vigia" if ext else "h61b_vigia"
    os.makedirs(S.DL + "vigia", exist_ok=True)
    tag = datetime.datetime.utcnow().strftime("%Y-%m-%d")
    json.dump(res, open(S.DL + f"vigia/{nom}_{coin}.json", "w"), indent=1, default=float)
    t = texto(res); print(t)
    open(S.DL + f"vigia/{nom}_{coin}.txt", "w").write(t + "\n")
    if "--telegram" in a:
        estados = "|".join(f"{b['brazo']}/{b['feed']}={b['estado']}" for b in res["brazos"])   # firma = SOLO el estado, no valores recalculados (trampa de los latch)
        lf = S.DL + f"vigia/latch_{nom}_{coin}.json"
        prev = json.load(open(lf)).get("firma") if os.path.exists(lf) else None
        if estados != prev and any(b["estado"] in ("KILL", "GATE_OK_SOLO_DRY_RUN") for b in res["brazos"]):
            sys.path.insert(0, "/root/polymarket-research")
            from shadow_digest import enviar_telegram
            enviar_telegram("H61b (dry-run): " + estados + "\n" + t[:900])
        json.dump(dict(firma=estados), open(lf, "w"))


if __name__ == "__main__":
    main()
