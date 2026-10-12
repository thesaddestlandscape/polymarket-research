#!/usr/bin/env python3
"""analisis_pares15_patas_sueltas.py -- MISIÓN «pares 15m sin patas sueltas» (Javi 12-Oct, prompt definitivo), pasos 2-6.
SOLO LECTURA. Fuentes: ledgers del ensayo en seco con rellenos simulados (experimento_pares_cola_15m.py, dev 8857438f2b;
datalogs/experimento_pares_dedicada_seco_{sol,btc}_ledger.jsonl, eventos `mercado_fin` medidos) + libro del 15m por
RECEPCIÓN del archivo del volumen (m15_registro, filas q: mejor bid/ask y tamaños) + desenlace oficial (gamma).

Reglas originales (auditadas en el código): de T=898 s a T=90 s una puja maker post-only de 5 acciones en YES y otra
en NO; un relleno cierra ese lado; la otra puja sigue quieta; a T=90 s se cancela todo y lo suelto va a resolución.
anclar = unirse al mejor bid sin moverse; crear = 1 tick sobre el mejor bid ajeno, recolocar si nos superan (<=3);
mixta = crear la primera orden de cada lado y después anclar.

Contabilidad: unidades emparejadas = min(acc YES, acc NO) a precio medio de cada lado; residuo = exceso de un lado a su
precio medio (va a resolución). Maker sin comisión; tomador 0,07·p·(1-p) por acción. Reembolso maker NO se suma.
Políticas nuevas (hipótesis, se evalúan sobre la MISMA muestra = DESCUBRIMIENTO; nada aquí es validación):
  A_TAKER(m, L): al PRIMER relleno de un mercado (lado X, precio p), leer el ask del lado contrario a t+L (recepción);
     si p + ask + fee(ask) <= 1 - m y hay tamaño en el nivel 1, comprar como tomador lo que falte (hasta 5; lo que no
     quepa en el nivel 1 se queda como residuo) y cancelar la puja maker del contrario. Si no hay margen -> sigue el
     camino ORIGINAL (esperar al maker).
  B_SALIR(L): al primer relleno, si no se puede completar con margen m=0, vender la pata X al bid de X a t+L como
     tomador (fee) y cancelar la puja del contrario (el mercado termina). Si se puede completar -> como A.
  NO_OPERAR: 0.
Uso: python3 analisis_pares15_patas_sueltas.py [--hasta 2026-10-12] [--desde ...]
"""
import argparse
import bisect
import collections
import gzip
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
from analisis_experimento_pares_sim import ganadores  # noqa: E402

DL = Path("/root/polymarket-research-datalogs")
REG = Path("/mnt/HC_Volume_106538179/m15_registro")
ACC = 5.0


def fee(p):
    return 0.07 * p * (1 - p)


def cargar_mercados(desde, hasta):
    M = []
    for mo in ("sol", "btc"):
        f = DL / f"experimento_pares_dedicada_seco_{mo}_ledger.jsonl"
        for ln in f.read_text().splitlines():
            e = json.loads(ln)
            if e.get("tipo") != "mercado_fin" or e.get("real") or not e.get("medido"):
                continue
            if not (desde <= e.get("ts", "") < hasta):
                continue
            r = e.get("rellenos") or {}
            fills = [(x["t_deteccion"], lado, x["acc"], x["precio"], x) for lado in ("YES", "NO") for x in r.get(lado, []) if x["acc"] > 0]
            M.append({"moneda": mo.upper(), "id": str(e["id"]), "slug": e["slug"], "pol": e["politica"], "fills": sorted(fills),
                      "cierre": int(e["slug"].rsplit("-", 1)[-1]) + 900, "dia": e["ts"][:10]})
    return M


def cargar_libros(mercados):
    """{(market_id, lado): ([recv], [bid], [ask], [bid_sz], [ask_sz])} solo para nuestros mercados."""
    ids = {m["id"] for m in mercados}
    dias = sorted({datetime.fromtimestamp(m["cierre"], timezone.utc).date().isoformat() for m in mercados})
    tok, L = {}, collections.defaultdict(lambda: ([], [], [], [], []))
    for d in dias:
        f = REG / f"m15_registro_{d}.csv.gz"
        if not f.exists():
            print(f"⚠️ sin {f.name}", file=sys.stderr)
            continue
        with gzip.open(f, "rt", errors="replace") as fh:
            try:
                for ln in fh:
                    c = ln.rstrip("\n").split(",")
                    if c[0] == "k" and len(c) > 7 and c[5] in ids:
                        tok[c[2]] = (c[5], c[7])
                    elif c[0] == "q" and c[2] in tok:
                        try:
                            r = int(c[7]) if len(c) > 7 and c[7] else int(c[1])
                            g = lambda x: None if x in ("", "None") else float(x)  # noqa: E731
                            s = L[tok[c[2]]]
                            for col, v in zip(s, (r, g(c[3]), g(c[4]), g(c[5]) or 0.0, g(c[6]) or 0.0)):
                                col.append(v)
                        except (ValueError, IndexError):
                            continue
            except (EOFError, OSError):
                pass
    for k, s in L.items():
        o = sorted(range(len(s[0])), key=s[0].__getitem__)
        L[k] = tuple([col[i] for i in o] for col in s)
    return L


def libro_en(L, mid, lado, t_ms):
    s = L.get((mid, lado))
    if not s:
        return None
    i = bisect.bisect_right(s[0], t_ms) - 1
    return None if i < 0 else (s[1][i], s[2][i], s[3][i], s[4][i])


def pnl_original(m, gan):
    acc = {"YES": 0.0, "NO": 0.0}
    cost = {"YES": 0.0, "NO": 0.0}
    for _t, lado, a, p, _x in m["fills"]:
        acc[lado] += a
        cost[lado] += a * p
    par = min(acc.values())
    pm = {s: cost[s] / acc[s] if acc[s] else 0.0 for s in acc}
    pnl_par = par * (1 - pm["YES"] - pm["NO"])
    pnl_res = sum((acc[s] - par) * ((1.0 if gan == s else 0.0) - pm[s]) for s in acc)
    lado_res = next((s for s in acc if acc[s] - par > 1e-9), None)
    return {"par": par, "pnl_par": pnl_par, "pnl_res": pnl_res, "lado_res": lado_res, "acc": acc, "pm": pm,
            "riesgo": cost["YES"] + cost["NO"]}


def politica_nueva(m, gan, L, lat_ms, margen, salir):
    """Devuelve (pnl, tipo) para A_TAKER (salir=False) o B_SALIR (salir=True). Sin rellenos -> igual que original (0)."""
    o = pnl_original(m, gan)
    if not m["fills"]:
        return 0.0, "sin_relleno", 0.0
    t1, X, a1, p1, _x = m["fills"][0]
    C = "NO" if X == "YES" else "YES"
    t_dec = int(t1 * 1000) + lat_ms
    bc, bx = libro_en(L, m["id"], C, t_dec), libro_en(L, m["id"], X, t_dec)
    # completar como tomador
    if bc and bc[1] is not None and bc[3] > 0:
        ask = bc[1]
        if p1 + ask + fee(ask) <= 1 - margen + 1e-12:
            n = min(a1, bc[3])
            pnl = n * (1 - p1 - ask - fee(ask)) + (a1 - n) * ((1.0 if gan == X else 0.0) - p1)
            return pnl, ("completa" if n >= a1 - 1e-9 else "completa_parcial"), n * ask
    if salir and bx and bx[0] is not None and bx[2] > 0:
        bid = bx[0]
        n = min(a1, bx[2])
        pnl = n * (bid - p1 - fee(bid)) + (a1 - n) * ((1.0 if gan == X else 0.0) - p1)
        return pnl, "sale", 0.0
    if salir:
        return a1 * ((1.0 if gan == X else 0.0) - p1), "sin_bid_mantiene", 0.0
    return o["pnl_par"] + o["pnl_res"], "sigue_original", 0.0


def politica_c(m, gan, L, tau_s, lat_ms, salir=True):
    """C_LIMITE(τ): tras el primer relleno (X a p1) se espera al maker del contrario como mucho τ s. Si llega en plazo ->
    camino original. Si no: se cancela la puja del contrario (efectiva a t1+τ) y, con salir=True, se vende X al bid a
    t1+τ+L como tomador; con salir=False se mantiene X a resolución (sin más órdenes)."""
    o = pnl_original(m, gan)
    if not m["fills"]:
        return 0.0, "sin_relleno"
    t1, X, a1, p1, _x = m["fills"][0]
    C = "NO" if X == "YES" else "YES"
    t2 = next((t for t, lado, *_ in m["fills"] if lado == C), None)
    if t2 is not None and t2 - t1 <= tau_s:
        return o["pnl_par"] + o["pnl_res"], "par_en_plazo"
    if not salir:
        return a1 * ((1.0 if gan == X else 0.0) - p1), "mantiene"
    bx = libro_en(L, m["id"], X, int((t1 + tau_s) * 1000) + lat_ms)
    if bx and bx[0] is not None and bx[2] > 0:
        n = min(a1, bx[2])
        return n * (bx[0] - p1 - fee(bx[0])) + (a1 - n) * ((1.0 if gan == X else 0.0) - p1), "sale"
    return a1 * ((1.0 if gan == X else 0.0) - p1), "sin_bid_mantiene"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--desde", default="2026-10-09")
    ap.add_argument("--hasta", default="2026-10-12")
    a = ap.parse_args()
    M = cargar_mercados(a.desde, a.hasta)
    des = ganadores([m["id"] for m in M])
    M = [m for m in M if m["id"] in des]
    print(f"Mercados medidos con desenlace oficial: {len(M)} ({a.desde} → {a.hasta}); SOL {sum(m['moneda'] == 'SOL' for m in M)}, BTC {sum(m['moneda'] == 'BTC' for m in M)}")
    L = cargar_libros(M)
    print(f"libros cargados: {len(L)} (mercado, lado) del archivo m15_registro\n")

    # ---- PASO 2: reproducción y descomposición
    print("== PASO 2: PnL por política y moneda (unidades emparejadas exactas; maker sin comisión) ==")
    print(f"{'moneda':6} {'política':7} {'merc':>4} {'pares':>5} {'PnL pares':>9} {'sueltas':>7} {'PnL suelta':>10} {'ganan':>6} {'TOTAL':>8} {'pares/suelta':>12}")
    agg = collections.defaultdict(lambda: collections.Counter())
    for m in M:
        o = pnl_original(m, des[m["id"]])
        m["o"] = o
        k = (m["moneda"], m["pol"])
        agg[k]["merc"] += 1
        agg[k]["pares"] += o["par"] >= ACC - 1e-9
        agg[k]["pnl_par"] += o["pnl_par"]
        agg[k]["pnl_res"] += o["pnl_res"]
        if o["lado_res"]:
            agg[k]["sueltas"] += 1
            agg[k]["ganan"] += des[m["id"]] == o["lado_res"]
    tot = collections.Counter()
    for k in sorted(agg):
        v = agg[k]
        tot.update(v)
        ppp = v["pnl_par"] / max(1, v["pares"])
        lps = v["pnl_res"] / max(1, v["sueltas"])
        print(f"{k[0]:6} {k[1]:7} {v['merc']:4d} {v['pares']:5d} {v['pnl_par']:+9.2f} {v['sueltas']:7d} {v['pnl_res']:+10.2f} "
              f"{v['ganan']:>2d}/{v['sueltas']:<3d} {v['pnl_par'] + v['pnl_res']:+8.2f} {(-lps / ppp) if ppp > 0 and lps < 0 else float('nan'):12.1f}")
    print(f"{'TOTAL':14} {tot['merc']:4d} {tot['pares']:5d} {tot['pnl_par']:+9.2f} {tot['sueltas']:7d} {tot['pnl_res']:+10.2f} "
          f"{tot['ganan']:>2d}/{tot['sueltas']:<3d} {tot['pnl_par'] + tot['pnl_res']:+8.2f}")
    print(f"  margen medio por par completo: {tot['pnl_par'] / max(1, tot['pares']):+.3f} $ (5 acciones) | pérdida media por pata suelta: "
          f"{tot['pnl_res'] / max(1, tot['sueltas']):+.3f} $ | % del margen de pares consumido por sueltas: {-tot['pnl_res'] / tot['pnl_par']:.0%}")

    # ---- PASO 3: autopsia (primer relleno de mercados que acaban con pata suelta vs que acaban en par)
    print("\n== PASO 3: autopsia del PRIMER relleno (sueltas vs pares) ==")
    grupos = {"suelta": [m for m in M if m["o"]["lado_res"] and m["fills"]], "par": [m for m in M if m["o"]["par"] >= ACC - 1e-9]}
    for g, lst in grupos.items():
        xs = [m["fills"][0][4] for m in lst]
        if not xs:
            continue
        med = lambda k: sorted(x.get(k) for x in xs if x.get(k) is not None)  # noqa: E731
        d1 = sorted((x["mid1"] - x["mid0"]) for x in xs if x.get("mid1") is not None and x.get("mid0") is not None)
        d5 = sorted((x["mid5"] - x["mid0"]) for x in xs if x.get("mid5") is not None and x.get("mid0") is not None)
        T = sorted(m["cierre"] - m["fills"][0][0] for m in lst)
        mid = lambda v: v[len(v) // 2] if v else float("nan")  # noqa: E731
        print(f"  {g:6} n={len(lst):2d} | Δmid +1 s mediana {mid(d1):+.3f} (cae en {sum(1 for x in d1 if x < 0) / max(1, len(d1)):.0%}) | "
              f"Δmid +5 s {mid(d5):+.3f} (cae en {sum(1 for x in d5 if x < 0) / max(1, len(d5)):.0%}) | precio {mid(med('precio')):.2f} | "
              f"espera {mid(med('espera_s')):.0f} s | cola {mid(med('cola')):.0f} | T restante {mid(T):.0f} s")
    sueltas = grupos["suelta"]
    print(f"  patas sueltas: {len(sueltas)}; ganan {sum(des[m['id']] == m['o']['lado_res'] for m in sueltas)}; precio medio "
          f"{sum(m['o']['pm'][m['o']['lado_res']] for m in sueltas) / max(1, len(sueltas)):.2f} (acierto esperable ~ precio si no hubiera selección)")

    # ---- PASOS 4-6: políticas nuevas
    print("\n== PASOS 4-6: políticas nuevas sobre la MISMA muestra (DESCUBRIMIENTO) — PnL total $ y € por mercado ==")
    print(f"{'política':34} {'TOTAL $':>8} {'$/merc':>7} {'completa':>8} {'sale':>5} {'sigue':>5} {'sin 2 mejores':>13} {'SOL':>7} {'BTC':>7}")
    filas = [("ORIGINAL", None)] + [(f"A_TAKER m={mg:.2f} L={lt}", ("A", lt, mg)) for lt in (300, 500, 1000) for mg in (0.0, 0.01, 0.02)] + \
            [(f"B_SALIR L={lt}", ("B", lt, 0.0)) for lt in (300, 500, 1000)] + [("NO_OPERAR", "0")]
    res = {}
    for nom, spec in filas:
        v, tipos = [], collections.Counter()
        for m in M:
            gan = des[m["id"]]
            if spec is None:
                p = m["o"]["pnl_par"] + m["o"]["pnl_res"]
                t = "original"
            elif spec == "0":
                p, t = 0.0, "no"
            else:
                p, t, _ = politica_nueva(m, gan, L, spec[1], spec[2], spec[0] == "B")
            tipos[t] += 1
            v.append((p, m["moneda"]))
        tot_ = sum(x[0] for x in v)
        s2 = sum(sorted((x[0] for x in v), reverse=True)[2:])
        res[nom] = {"total": round(tot_, 2), "por_merc": round(tot_ / len(v), 3), "tipos": dict(tipos)}
        print(f"{nom:34} {tot_:+8.2f} {tot_ / len(v):+7.3f} {tipos['completa'] + tipos['completa_parcial']:8d} {tipos['sale']:5d} "
              f"{tipos['sigue_original']:5d} {s2:+13.2f} {sum(x[0] for x in v if x[1] == 'SOL'):+7.2f} {sum(x[0] for x in v if x[1] == 'BTC'):+7.2f}")
    print("\n== C_LIMITE(τ): esperar al maker del contrario τ s; si no llega, cancelar y SALIR al bid (L=500) o MANTENER ==")
    print(f"{'τ':>5} {'salir: TOTAL $':>14} {'$/merc':>7} {'pares':>5} {'sale':>5} {'sin 2 mejores':>13} | {'mantener: TOTAL $':>17} {'sin 2 mejores':>13}")
    for tau in (2, 5, 10, 20, 30, 60, 120, 300):
        r = [politica_c(m, des[m["id"]], L, tau, 500, True) for m in M]
        r2 = [politica_c(m, des[m["id"]], L, tau, 500, False) for m in M]
        tt, t2_ = sum(x[0] for x in r), sum(x[0] for x in r2)
        res[f"C_salir_tau{tau}"], res[f"C_mantener_tau{tau}"] = round(tt, 2), round(t2_, 2)
        print(f"{tau:5d} {tt:+14.2f} {tt / len(M):+7.3f} {sum(1 for x in r if x[1] == 'par_en_plazo'):5d} {sum(1 for x in r if x[1] == 'sale'):5d} "
              f"{sum(sorted((x[0] for x in r), reverse=True)[2:]):+13.2f} | {t2_:+17.2f} {sum(sorted((x[0] for x in r2), reverse=True)[2:]):+13.2f}")
    # tiempo hasta el 2º relleno en los pares
    w = sorted(next(t for t, lado, *_ in m["fills"] if lado != m["fills"][0][1]) - m["fills"][0][0] for m in M if m["o"]["par"] >= ACC - 1e-9)
    if w:
        print(f"  espera del 2º relleno en los pares: P25 {w[len(w) // 4]:.0f} s · P50 {w[len(w) // 2]:.0f} s · P75 {w[3 * len(w) // 4]:.0f} s · P90 {w[int(.9 * len(w))]:.0f} s")
    out = REPO / "informes" / "pares15_patas_sueltas_descubrimiento_12oct.json"
    out.write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"\nJSON: {out}\nOJO: todo lo de los pasos 4-6 es DESCUBRIMIENTO (misma muestra). Validación: ensayo 'crear' en curso desde 12-Oct 14:59Z.")


if __name__ == "__main__":
    main()
