#!/usr/bin/env python3
"""analisis_5m_barato_reconciliacion.py -- MISIÓN 5m barato (Javi 14-Oct, prompt "validar el alpha"): pasos 2 y 4.
Reconstruye FILA A FILA los eventos oficiales de v4 (hash 77a75859ae5cf22e; NO se modifica: se importan sus funciones
fee/pnl_de y se leen sus eventos_D.csv) y recalcula cada métrica del informe desde las filas:
  - libro de operaciones (ledger) con mercado, moneda, hora, precios, comisión, ejecución simulada, desenlace, PnL;
  - reconciliación PnL total / mejor día / mejor operación / sin BTC / drawdown;
  - deriva: EV últimos 3 días vs anteriores con prueba de permutación por DÍAS;
  - curva de latencia con n e IC90 bootstrap por evento;
  - clases a +215 ms (A sigue barato / B cancelado o repreciado / C consumido / D otro nivel) y EV HIPOTÉTICO al ask de
    la señal (mismo precio, mismo stake, neto de comisión) para separar selección de precio; rasgos conocibles en t0
    que distinguen las clases (edad del bid15, Binance firmado hacia el lado, actividad, margen, tiempo restante).
  - B2/B3/B4 con n.
Uso: python3 analisis_5m_barato_reconciliacion.py [--periodo OOS|PRE|TODO]
Salida: datalogs/m5barato_mision/ledger_v4_<periodo>.csv + reconciliacion_<periodo>.txt
"""
import argparse
import csv
import importlib.util
import random
import statistics as st
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
_s = importlib.util.spec_from_file_location("v4", REPO / "vigia_5m_barato_forward.py")
V4 = importlib.util.module_from_spec(_s)
_s.loader.exec_module(V4)
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402

OUT = Path("/root/polymarket-research-datalogs/m5barato_mision")
RNG = random.Random(14)


def dia(e):
    return datetime.fromtimestamp(int(e["cierre"]), timezone.utc).date().isoformat()


def f(x, d=None):
    try:
        return float(x)
    except (TypeError, ValueError):
        return d


def boot_ev(pares, n=4000):
    """IC90 de sum(pnl)/sum(coste) remuestreando eventos."""
    if len(pares) < 3:
        return (None, None)
    m = []
    for _ in range(n):
        s = [pares[RNG.randrange(len(pares))] for _ in pares]
        c = sum(x[1] for x in s)
        if c > 0:
            m.append(sum(x[0] for x in s) / c)
    m.sort()
    return (round(m[int(.05 * len(m))], 3), round(m[int(.95 * len(m))], 3))


def ev(pares):
    c = sum(p[1] for p in pares)
    return round(sum(p[0] for p in pares) / c, 4) if c > 0 else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--periodo", default="OOS", choices=["OOS", "PRE", "TODO"])
    a = ap.parse_args()
    OUT.mkdir(exist_ok=True)
    E = []
    for fi in sorted(V4.SALIDA.glob("eventos_*.csv")):
        E += list(csv.DictReader(open(fi)))
    cong = int(datetime.fromisoformat(V4.CONFIG["congelado_utc"]).timestamp() * 1000)
    filtro = {"OOS": lambda e: int(e["t_deteccion"]) >= cong, "PRE": lambda e: int(e["t_deteccion"]) < cong,
              "TODO": lambda e: True}[a.periodo]
    prim = [e for e in E if e["regla"] == "B1_5m" and e["es_primero"] == "1" and filtro(e)]
    todos = [e for e in E if e["regla"] == "B1_5m" and filtro(e)]
    des = desenlaces({e["market_compra"] for e in E})
    L = []
    # ---------- 1. ledger ----------
    campos = ["event_id", "dia", "moneda", "lado", "cierre", "market_compra", "market_otro", "t_deteccion_utc", "resto_s",
              "ref15", "ref5", "gap_bps", "bid15_t0", "ask5_t0", "fee_ask5_t0", "margen_neto", "p_limite", "acciones_obj",
              "clase_L215", "precio_L215", "acciones_L215", "fee_L215", "coste_L215", "desenlace", "gana", "pnl_bruto",
              "fee_total", "pnl_neto", "ejecutable", "motivo", "edad_bid15_ms", "edad_ask5_ms", "bin_ret_5s_lado_bps",
              "bin_ret_1s_lado_bps", "ev_hip_ask_t0"]
    ledger = []
    for e in prim:
        r = des.get(e["market_compra"])
        gana = None if r is None else ((r == "YES") == (e["lado"] == "Up"))
        acc, pr = f(e["L215_acciones"], 0.0), f(e["L215_precio"])
        ejec = acc > 0 and pr is not None
        sgn = 1 if e["lado"] == "Up" else -1
        a0 = f(e["ask_compra_t0"])
        acc0 = max(V4.CONFIG["min_acciones"], V4.CONFIG["stake_eur"] / a0)
        hip = None if gana is None else round(((1.0 if gana else 0.0) - a0 - V4.fee(a0)) / (a0 + V4.fee(a0)), 4)
        fila = {"event_id": e["event_id"], "dia": dia(e), "moneda": e["moneda"], "lado": e["lado"], "cierre": e["cierre"],
                "market_compra": e["market_compra"], "market_otro": e["market_otro"],
                "t_deteccion_utc": datetime.fromtimestamp(int(e["t_deteccion"]) / 1000, timezone.utc).isoformat(timespec="milliseconds"),
                "resto_s": e["resto_s"], "ref15": e["ref15"], "ref5": e["ref5"], "gap_bps": e["gap_bps"],
                "bid15_t0": e["bid_otro_t0"], "ask5_t0": e["ask_compra_t0"], "fee_ask5_t0": round(V4.fee(a0), 5),
                "margen_neto": e["margen_neto"], "p_limite": e["p_limite"], "acciones_obj": e["acciones_objetivo"],
                "clase_L215": e["L215_clase"], "precio_L215": pr if ejec else "", "acciones_L215": acc,
                "fee_L215": round(V4.fee(pr), 5) if ejec else "", "coste_L215": round(acc * (pr + V4.fee(pr)), 4) if ejec else 0,
                "desenlace": r or "NO_DISPONIBLE", "gana": gana,
                "pnl_bruto": round(acc * ((1.0 if gana else 0.0) - pr), 4) if ejec and gana is not None else "",
                "fee_total": round(acc * V4.fee(pr), 4) if ejec else "",
                "pnl_neto": round(acc * ((1.0 if gana else 0.0) - pr - V4.fee(pr)), 4) if ejec and gana is not None else "",
                "ejecutable": ejec,
                "motivo": ("lleno: ask a +215 ms <= p_limite" if ejec else
                           {"C_consumido": "una operación a ask_t0 consumió el nivel entre t0 y t0+215",
                            "B_cancelado_o_repreciado": "el ask subió sobre p_limite sin operación a ask_t0 (cancelado/repreciado)",
                            "UNKNOWN": "sin libro para reconstruir"}.get(e["L215_clase"], e["L215_clase"])),
                "edad_bid15_ms": e["o_edad_bid_ms"], "edad_ask5_ms": e["c_edad_ask_ms"],
                "bin_ret_5s_lado_bps": round(sgn * f(e["bin_ret_5s_bps"], 0), 3) if e["bin_ret_5s_bps"] not in ("", "None") else "",
                "bin_ret_1s_lado_bps": round(sgn * f(e["bin_ret_1s_bps"], 0), 3) if e["bin_ret_1s_bps"] not in ("", "None") else "",
                "ev_hip_ask_t0": hip}
        ledger.append(fila)
    with open(OUT / f"ledger_v4_{a.periodo}.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=campos)
        w.writeheader()
        w.writerows(ledger)
    # ---------- 2. reconciliación ----------
    ej = [x for x in ledger if x["ejecutable"] and x["pnl_neto"] != ""]
    pares = [(x["pnl_neto"], x["coste_L215"]) for x in ej]
    pnl = sum(p[0] for p in pares)
    L.append(f"=== v4 {a.periodo}: {len(prim)} señales primeras, {len(ej)} ejecutables a +215 ms, desenlace disponible "
             f"{sum(1 for x in ledger if x['desenlace'] != 'NO_DISPONIBLE')}/{len(ledger)}")
    L.append(f"PnL neto {pnl:+.3f} € | coste {sum(p[1] for p in pares):.3f} € | EV/€ {ev(pares):+.4f} IC90 eventos {boot_ev(pares)} | "
             f"acierto {sum(1 for x in ej if x['gana'])}/{len(ej)}")
    pd_ = defaultdict(lambda: [0.0, 0.0, 0])
    for x in ej:
        pd_[x["dia"]][0] += x["pnl_neto"]
        pd_[x["dia"]][1] += x["coste_L215"]
        pd_[x["dia"]][2] += 1
    L.append("PnL por día (día de CIERRE; solo días con ejecutables): " + " | ".join(
        f"{d[5:]} {v[0]:+.2f}€ n={v[2]}" for d, v in sorted(pd_.items())))
    if pd_:
        md = max(pd_, key=lambda d: pd_[d][0])
        resto = [(x["pnl_neto"], x["coste_L215"]) for x in ej if x["dia"] != md]
        L.append(f"mejor día {md}: {pd_[md][0]:+.3f} € = {pd_[md][0] / pnl:.0%} del total (resto de días {pnl - pd_[md][0]:+.3f} €, "
                 f"EV/€ sin él {ev(resto)})")
    mej = max(ej, key=lambda x: x["pnl_neto"]) if ej else None
    if mej:
        L.append(f"mejor operación {mej['event_id']} {mej['pnl_neto']:+.3f} € (precio {mej['precio_L215']}, {mej['acciones_L215']:.2f} acc, "
                 f"{mej['dia']}) -> sin ella {pnl - mej['pnl_neto']:+.3f} €")
    acum = pico = dd = 0.0
    for x in sorted(ej, key=lambda x: x["t_deteccion_utc"]):
        acum += x["pnl_neto"]
        pico = max(pico, acum)
        dd = max(dd, pico - acum)
    L.append(f"drawdown máximo (orden de detección) {dd:.3f} €")
    L.append("\nPor moneda (señales / ejecutables / coste / PnL / EV/€ / mejor op):")
    for m in sorted({x["moneda"] for x in ledger}):
        s = [x for x in ledger if x["moneda"] == m]
        sj = [x for x in ej if x["moneda"] == m]
        pp = [(x["pnl_neto"], x["coste_L215"]) for x in sj]
        L.append(f"  {m:5s} {len(s):3d} / {len(sj):2d} / {sum(p[1] for p in pp):6.2f} € / {sum(p[0] for p in pp):+7.2f} € / "
                 f"{ev(pp)} / {max((x['pnl_neto'] for x in sj), default=None)}")
    # ---------- 3. deriva ----------
    dias = sorted(pd_)
    if len(dias) >= 6:
        u3 = dias[-3:]
        ev_a = sum(pd_[d][0] for d in u3) / sum(pd_[d][1] for d in u3)
        ev_b = sum(pd_[d][0] for d in dias[:-3]) / sum(pd_[d][1] for d in dias[:-3])
        obs = ev_b - ev_a
        cnt, N = 0, 5000
        for _ in range(N):
            perm = dias[:]
            RNG.shuffle(perm)
            a3 = perm[-3:]
            b3 = perm[:-3]
            dd_ = (sum(pd_[d][0] for d in b3) / sum(pd_[d][1] for d in b3)) - (sum(pd_[d][0] for d in a3) / sum(pd_[d][1] for d in a3))
            cnt += dd_ >= obs
        L.append(f"\nDERIVA: EV/€ últimos 3 días ({','.join(d[5:] for d in u3)}) {ev_a:+.3f} vs anteriores {ev_b:+.3f}; "
                 f"p permutación por días (caída >= observada) = {cnt / N:.3f}")
        s3 = [x for x in ledger if x["dia"] in u3]
        sb = [x for x in ledger if x["dia"] in dias[:-3]]
        for nom, g in (("últimos3", s3), ("anteriores", sb)):
            gj = [x for x in g if x["ejecutable"]]
            L.append(f"  {nom}: señales {len(g)} ejecutables {len(gj)} ({len(gj) / max(1, len(g)):.0%}) monedas "
                     f"{dict(Counter(x['moneda'] for x in gj))} edad bid15 med "
                     f"{st.median([f(x['edad_bid15_ms']) for x in g if f(x['edad_bid15_ms']) is not None] or [0]):.0f} ms")
    # ---------- 4. latencia ----------
    L.append("\nLATENCIA (mismos eventos primeros; EV/€ = PnL/coste de ejecutables; IC90 bootstrap por evento):")
    for lat in V4.CONFIG["latencias_diagnostico_ms"] + ["jitter"]:
        pref = f"L{lat}" if lat != "jitter" else "jitter"
        pp = [p for p in (V4.pnl_de(e, des, pref) for e in prim) if p and p[1] > 0]
        L.append(f"  {pref:7s} n={len(pp):2d} PnL {sum(p[0] for p in pp):+7.2f} € EV/€ {ev(pp)} IC90 {boot_ev(pp)}")
    # ---------- 5. clases y selección adversa ----------
    L.append("\nCLASES a +215 ms y EV HIPOTÉTICO comprando TODAS al ask de la señal (mismo precio/stake, neto de comisión):")
    grupos = {"desaparecen (B+C)": [x for x in ledger if x["clase_L215"].startswith(("B", "C"))],
              "  B cancelado/repreciado": [x for x in ledger if x["clase_L215"].startswith("B")],
              "  C consumido": [x for x in ledger if x["clase_L215"].startswith("C")],
              "quedan (A+D)": [x for x in ledger if x["clase_L215"].startswith(("A", "D"))]}
    for nom, g in grupos.items():
        g2 = [x for x in g if x["ev_hip_ask_t0"] is not None]
        pp = [(x["ev_hip_ask_t0"], 1.0) for x in g2]
        L.append(f"  {nom:26s} n={len(g):2d} acierto {sum(1 for x in g2 if x['gana'])}/{len(g2)} EV/€ hip "
                 f"{st.mean([p[0] for p in pp]) if pp else float('nan'):+.3f} IC90 {boot_ev(pp)}")
    L.append("  rasgos conocibles en t0 (mediana) — desaparecen vs quedan; y quedan ganadoras vs perdedoras:")
    for rasgo in ("edad_bid15_ms", "edad_ask5_ms", "bin_ret_5s_lado_bps", "bin_ret_1s_lado_bps", "margen_neto", "resto_s", "ask5_t0"):
        def med(g):
            v = [f(x[rasgo]) for x in g if f(x[rasgo]) is not None]
            return f"{st.median(v):+.3f}" if v else "nan"
        q = grupos["quedan (A+D)"]
        L.append(f"    {rasgo:22s} desap {med(grupos['desaparecen (B+C)'])} | quedan {med(q)} | quedan-ganan "
                 f"{med([x for x in q if x['gana']])} | quedan-pierden {med([x for x in q if x['gana'] is False])}")
    # ---------- 6. re-armes ----------
    pp = [p for p in (V4.pnl_de(e, des, "L215") for e in todos) if p and p[1] > 0]
    L.append(f"\nTodos los eventos con re-armes (descriptivo, no independientes): n={len(pp)} PnL {sum(p[0] for p in pp):+.2f} "
             f"EV/€ {ev(pp)}")
    txt = "\n".join(L)
    print(txt)
    (OUT / f"reconciliacion_{a.periodo}.txt").write_text(txt + "\n")


if __name__ == "__main__":
    main()
