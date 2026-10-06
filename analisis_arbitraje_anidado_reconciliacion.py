#!/usr/bin/env python3
"""analisis_arbitraje_anidado_reconciliacion.py -- B1 paso 1 (06-Oct, Javi: "auditar B1 hasta el último milisegundo").

Une las dos fuentes y separa lo que no debe mezclarse:
  FUENTE D (dry-run, 02-Oct..): arbitraje_anidado_dryrun_*.csv. t0 = instante en que el observador (sondeo cada 50 ms del
    estado del libro en memoria) ve neto >= 0,0005. Valora la LLEGADA a t0+L mirando el histórico del libro MUESTREADO A
    100 ms (LE.en): "llena" = en esa foto el ask < precio detectado, o == y tamaño >= shares. Con muestreo de 100 ms,
    150/200/250 ms leen casi la misma foto. 200/250/300 ms solo existen desde el 05-Oct 16:53Z.
  FUENTE M (registro ms, 05-Oct 16:06Z..): episodios de analisis_arbitraje_anidado_ms_scanner.py (cada cambio del top,
    hora de recepción). Dos medidas DISTINTAS por pata y latencia:
      viva_L  = el nivel detectado nunca dejó de servir en [t0, t0+L]  (persistencia continua)
      llena_L = en t0+L el nivel está disponible (semántica FOK en la llegada, como D; puede haber vuelto)
Nada se ha ejecutado nunca (dry-run): "realmente se ejecutó" = 0 en todas las filas; no existe la fila "Actual".
Tiempos: t0 = detección (recepción); t_order = t0 + decisión (~5 ms con firma caliente); t_exchange = t_order + red
(~30 ms) + 150 ms de taker delay del exchange -> L ≈ 215-250 ms medidos el 05-Oct (POST 226 ms mediana incluye el
retraso). t_fill = t_exchange (FOK: casa o muere). t_expire = primer cambio que deja la pata sin servir;
t_close = primer instante con neto < 0,0005 (fin del episodio).
Uso: python3 analisis_arbitraje_anidado_reconciliacion.py --episodios <csv del escáner> [--tabla salida.csv]
"""
import argparse
import collections
import csv
import statistics as st
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_arbitraje_anidado_autopsia import cargar_oportunidades, pago, fee  # noqa: E402
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402

LATS_D = [150, 200, 250, 300, 400, 600, 1000]
LATS_M = [25, 50, 75, 100, 150, 200, 250, 300, 400, 500, 1000]


def pct(v, ps=(.1, .25, .5, .75, .9, .95, .99)):
    v = sorted(v)
    if not v:
        return "n=0"
    return "n=%d " % len(v) + " ".join(f"P{int(p * 100)}={v[min(len(v) - 1, int(len(v) * p))]:g}" for p in ps)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--episodios", required=True)
    ap.add_argument("--tabla", default=None)
    a = ap.parse_args()
    ops = [r for r in cargar_oportunidades() if float(r["shares"]) >= 5]
    E = list(csv.DictReader(open(a.episodios, encoding="utf-8")))
    des = desenlaces({r[k] for r in ops for k in ("market_largo", "market_corto")} |
                     {e[k] for e in E for k in ("mid_l", "mid_c")})

    # ---------- vida (fuente D): el observador re-registra como mucho 1/s mientras sigue viva ----------
    import glob
    import gzip
    todas = collections.defaultdict(list)
    for f in sorted(glob.glob("/root/polymarket-research-datalogs/arbitraje_anidado_dryrun_*.csv*")):
        with (gzip.open if f.endswith(".gz") else open)(f, "rt") as fh:
            for r in csv.DictReader(fh):
                todas[(r["par"], r["activo"], r["fin"], r["pata_A"])].append(int(r["ts_ms"]))

    tabla = []
    for r in ops:
        k = (r["par"], r["activo"], r["fin"], r["pata_A"])
        pA, pB = pago(r["pata_A"], r, des), pago(r["pata_B"], r, des)
        sh, aA, aB = float(r["shares"]), float(r["ask_A"]), float(r["ask_B"])
        coste = aA + fee(aA) + aB + fee(aB)
        ts = sorted(todas[k])
        fila = {"t0_ms": r["ts_ms"], "par": r["par"], "activo": r["activo"], "fin": r["fin"], "pata_A": r["pata_A"],
                "ask_A": aA, "ask_B": aB, "edad_A_ms": r["edad_A_ms"], "edad_B_ms": r["edad_B_ms"], "shares": sh,
                "neto_share": float(r["neto"]), "garantizado_usd": round(sh * (1 - coste), 4),
                "extra_pago2_usd": (sh if (pA is not None and pB is not None and pA + pB == 2) else 0.0),
                "vida_min_s_1s": round((ts[-1] - ts[0]) / 1000, 1), "detecciones": len(ts),
                "desenlace": "ok" if pA is not None and pB is not None else "falta", "ejecutada_real": 0}
        for L in LATS_D:
            fila[f"D_{L}"] = r.get(f"fill_{L}") or "sin_dato"
            fila[f"D_neto_top_{L}"] = r.get(f"neto_top_{L}") or ""
        # motivo de fallo a 400 ms (D no guarda la causa; M sí, ver abajo)
        tabla.append(fila)
    print(f"== Tabla maestra (fuente D): {len(tabla)} oportunidades con shares>=5; desenlace oficial "
          f"{sum(f['desenlace'] == 'ok' for f in tabla)}/{len(tabla)}; ejecutadas de verdad: 0 (dry-run) ==")
    if a.tabla:
        with open(a.tabla, "w", newline="", encoding="utf-8") as fo:
            w = csv.DictWriter(fo, fieldnames=list(tabla[0]))
            w.writeheader()
            w.writerows(tabla)
        print(f"   -> {a.tabla}")

    # ---------- 3. P(ambas | L), cada fuente por separado ----------
    print("\n== 3. P(ambas | L) ==")
    print("  FUENTE D (FOK en la llegada, foto de 100 ms):")
    for L in LATS_D:
        v = [f[f"D_{L}"] for f in tabla if f[f"D_{L}"] != "sin_dato"]
        if v:
            c = collections.Counter(v)
            print(f"   {L:5} ms n={len(v):3} ambas {c['ambas'] / len(v):5.1%} | solo_A {c['solo_A']} solo_B {c['solo_B']} "
                  f"ninguna {c['ninguna']}")
    print(f"  FUENTE M ({len(E)} episodios sin look-ahead, {len({(e['moneda'], e['cierre']) for e in E})} ventanas):")
    for L in LATS_M:
        viva = sum(int(e[f"viva_A_{L}"]) and int(e[f"viva_B_{L}"]) for e in E)
        llena = sum(int(e[f"llena_A_{L}"]) and int(e[f"llena_B_{L}"]) for e in E)
        print(f"   {L:5} ms ambas VIVAS de forma continua {viva / len(E):5.1%} | ambas LLENAN en la llegada (FOK) "
              f"{llena / len(E):5.1%}")
    # mismo criterio, M ponderado por dinero garantizado
    print("  FUENTE M ponderada por $ garantizados (lo que importa):")
    tot = sum(float(e["garantizado_usd"]) for e in E)
    for L in (100, 150, 200, 250, 300, 400):
        g = sum(float(e["garantizado_usd"]) for e in E if int(e[f"llena_A_{L}"]) and int(e[f"llena_B_{L}"]))
        print(f"   {L:5} ms garantizado capturable {g:7.2f} $ de {tot:.2f} $ ({g / tot:5.1%})")

    # ---------- 4. PnL por niveles (fuente D, misma muestra para todas las L comparables) ----------
    print("\n== 4. PnL por niveles (fuente D; Actual = 0: nunca se envió una orden) ==")
    for L in (150, 250, 400, 600, 1000):
        S = [f for f in tabla if f[f"D_{L}"] != "sin_dato" and f["desenlace"] == "ok"]
        if not S:
            continue
        ideal_g = sum(f["garantizado_usd"] for f in S)
        ideal_x = sum(f["extra_pago2_usd"] for f in S)
        exe = sum(f["shares"] * float(f[f"D_neto_top_{L}"]) for f in S if f[f"D_neto_top_{L}"] != "")
        true_g = sum(f["garantizado_usd"] for f in S if f[f"D_{L}"] == "ambas")
        true_x = sum(f["extra_pago2_usd"] for f in S if f[f"D_{L}"] == "ambas")
        direc = []
        for f in S:
            if f[f"D_{L}"] in ("solo_A", "solo_B"):
                r = next(o for o in ops if o["ts_ms"] == f["t0_ms"] and o["pata_A"] == f["pata_A"])
                p_ = "A" if f[f"D_{L}"] == "solo_A" else "B"
                pg = pago(r[f"pata_{p_}"], r, des)
                ask = float(r[f"ask_{p_}"])
                direc.append(f["shares"] * (pg - ask - fee(ask)))
        print(f"  L={L:4} n={len(S):2} | IDEAL garantizado {ideal_g:+7.2f} $ (+extra pago 2 {ideal_x:+.2f}) | "
              f"EJECUTABLE TEÓRICO (ambas al top de t0+L) {exe:+7.2f} $ | TRUE-ARB garantizado {true_g:+7.2f} $ "
              f"(+extra {true_x:+.2f}) | DIRECCIONAL aparte {sum(direc):+7.2f} $ (n={len(direc)}, exposición media "
              f"{st.mean([f['shares'] * float(f['ask_A']) for f in S]):.1f} $)")
        print(f"         pérdida por timing (ideal-ejecutable) {ideal_g - exe:+.2f} | por legging/FOK (ideal-true) "
              f"{ideal_g - true_g:+.2f} | fees incluidas en el neto (0,07·p·(1-p) por share)")

    # ---------- 6-7. vida del arbitraje ----------
    print("\n== 6-7. Vida del arbitraje ==")
    print("  FUENTE D (cota inferior, resolución 1 s; 0 = una sola detección):", pct([f["vida_min_s_1s"] for f in tabla]))
    print("  FUENTE M vida por hora de recepción (ms):", pct([int(e["vida_recv_ms"]) for e in E]))
    print("  FUENTE M vida por hora del exchange (ms):", pct([int(e["vida_exch_ms"]) for e in E]))
    for nombre, clave in (("tamaño (neto/share)", lambda e: "<1c" if float(e["neto0"]) < .01 else "1-5c" if float(e["neto0"]) < .05 else ">=5c"),
                          ("moneda", lambda e: e["moneda"]),
                          ("dirección", lambda e: e["pata_A"]),
                          ("pata que cambia en t0", lambda e: ("15m" if (e["cambia"] == "A") == e["pata_A"].endswith("largo") else "5m")),
                          ("Binance |ret 1 s|", lambda e: "sin" if e["bin_1000"] in ("", "None") else "<1bp" if abs(float(e["bin_1000"])) < 1 else ">=1bp")):
        g = collections.defaultdict(list)
        for e in E:
            g[clave(e)].append(e)
        print(f"  por {nombre}:")
        for k, v in sorted(g.items()):
            print(f"     {k:14} vida {pct([int(e['vida_recv_ms']) for e in v], (.25, .5, .9))} | garantizado "
                  f"{sum(float(e['garantizado_usd']) for e in v):6.2f} $")
    print("\n== Muerte de cada pata (fuente M) ==")
    for p in ("A", "B"):
        d = [int(e[f"muerte_{p}_ms"]) for e in E if e[f"muerte_{p}_ms"] not in ("", "None")]
        print(f"  pata {p}: {pct(d)} | causas {dict(collections.Counter(e[f'causa_{p}'] for e in E))}")
    both = []
    for e in E:
        ms = [int(e[f"muerte_{p}_ms"]) for p in ("A", "B") if e[f"muerte_{p}_ms"] not in ("", "None")]
        if len(ms) == 2:
            both.append(max(ms))
    print("  hasta que mueren AMBAS:", pct(both))


if __name__ == "__main__":
    main()
