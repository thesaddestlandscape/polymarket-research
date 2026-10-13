#!/usr/bin/env python3
"""analisis_pares15_defensa_cancelacion.py -- 13-Oct (Javi: punto 3, "a ver si nos serviría"). ¿Una señal de repricing/
barrido inminente (familia A2 de la misión 15m: edad del precio + Binance; más el movimiento del propio mid) distingue,
ANTES del primer relleno, los mercados que acaban en PATA SUELTA de los que acaban en PAR? Si sí, retirarse del mercado al
saltar la señal evitaría sueltas (−1,23 $ c/u) a costa de pares (+0,29 $ c/u).
SOLO LECTURA. Mercados del ensayo en seco con rellenos simulados (cargar_mercados de analisis_pares15_patas_sueltas.py):
DESCUBRIMIENTO 09-10 Oct (80 merc., anclar/crear/mixta) para elegir umbral; VALIDACIÓN 12-13 Oct (crear, 83 merc.).
Estado por hora de RECEPCIÓN (m15_registro: q = top del libro, x = aggTrade Binance con recepción en c[7]).
Rasgos a t_dec = primer relleno − LAT ms (tiempo para cancelar): bn1 = retorno de Binance 1 s EN CONTRA del lado (bps),
dm2 = caída del mid del propio lado en 2 s, edad = ms desde el último cambio de precio del bid propio.
Veto degenerado (trampa CLAUDE.md, 07-Oct): fracción de la vida de la orden (rejilla 500 ms desde el inicio hasta el primer
relleno) con la señal encendida. Política SALIR: si la señal salta en cualquier punto de la rejilla antes del primer
relleno, se cancela todo y el mercado da 0.
Uso: nice -n 19 python3 analisis_pares15_defensa_cancelacion.py
"""
import bisect
import collections
import gzip
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_pares15_patas_sueltas import cargar_mercados, cargar_libros, libro_en, pnl_original, REG  # noqa: E402
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402

LAT = 200
SIMBOLO = {"BTC": "BTCUSDT", "SOL": "SOLUSDT"}
INF = Path(__file__).resolve().parent / "informes" / "pares15_defensa_cancelacion_13oct.txt"


def cargar_binance(dias):
    B = collections.defaultdict(lambda: ([], []))
    for d in dias:
        f = REG / f"m15_registro_{d}.csv.gz"
        if not f.exists():
            continue
        with gzip.open(f, "rt", errors="replace") as fh:
            try:
                for ln in fh:
                    if ln[0] != "x":
                        continue
                    c = ln.split(",")
                    if c[2] in ("BTCUSDT", "SOLUSDT") and len(c) > 7:
                        try:
                            B[c[2]][0].append(int(c[7])); B[c[2]][1].append(float(c[3]))
                        except ValueError:
                            pass
            except (EOFError, OSError):
                pass
    out = {}
    for s, (t, p) in B.items():
        o = np.argsort(t, kind="stable")
        out[s] = (np.asarray(t)[o], np.asarray(p)[o])
    return out


def precio_bn(B, sym, t_ms):
    t, p = B[sym]
    i = np.searchsorted(t, t_ms, side="right") - 1
    return None if i < 0 else p[i]


def rasgos(m, lado, t_ms, L, B):
    sym = SIMBOLO[m["moneda"]]
    p1, p0 = precio_bn(B, sym, t_ms), precio_bn(B, sym, t_ms - 1000)
    bn1 = None if (p1 is None or p0 is None) else (p1 / p0 - 1) * 1e4 * (-1 if lado == "YES" else 1)  # + = en contra
    a, b = libro_en(L, m["id"], lado, t_ms), libro_en(L, m["id"], lado, t_ms - 2000)
    dm2 = None
    if a and b and None not in (a[0], a[1], b[0], b[1]):
        dm2 = ((b[0] + b[1]) - (a[0] + a[1])) / 2                                              # + = el mid cae
    s = L.get((m["id"], lado))
    edad = None
    if s:
        i = bisect.bisect_right(s[0], t_ms) - 1
        if i >= 0:
            j = i
            while j > 0 and s[1][j - 1] == s[1][i]:
                j -= 1
            edad = t_ms - s[0][j]
    return bn1, dm2, edad


def auc(pos, neg):
    pos, neg = [x for x in pos if x is not None], [x for x in neg if x is not None]
    if not pos or not neg:
        return float("nan"), 0, 0
    g = sum((p > q) + 0.5 * (p == q) for p in pos for q in neg)
    return g / (len(pos) * len(neg)), len(pos), len(neg)


REGLAS = {f"bn1>={k}": (lambda r, k=k: r[0] is not None and r[0] >= k) for k in (1, 2, 3, 5)}
REGLAS.update({f"dm2>={c}": (lambda r, c=c: r[1] is not None and r[1] >= c) for c in (0.01, 0.02, 0.03)})
REGLAS.update({"A2: edad<300 y bn1>=1": lambda r: r[2] is not None and r[2] < 300 and r[0] is not None and r[0] >= 1,
               "bn1>=2 o dm2>=0.02": lambda r: (r[0] is not None and r[0] >= 2) or (r[1] is not None and r[1] >= 0.02)})


def evaluar(M, gan, L, B, Lg, titulo):
    filas = []
    for m in M:
        g = gan.get(m["id"])
        if g is None or not m["fills"]:
            filas.append((m, None, 0.0, None, []))
            continue
        o = pnl_original(m, g)
        pnl = o["pnl_par"] + o["pnl_res"]
        t0, lado = m["fills"][0][0], m["fills"][0][1]
        suelta = o["lado_res"] is not None
        rr = rasgos(m, lado, int(t0 * 1000) - LAT, L, B)
        inicio = (m["cierre"] - 898) * 1000
        rej = []
        for t in range(inicio, int(t0 * 1000) - LAT + 1, 500):
            rej.append((rasgos(m, "YES", t, L, B), rasgos(m, "NO", t, L, B)))
        filas.append((m, suelta, pnl, rr, rej))
    vivos = [f for f in filas if f[1] is not None]
    n_s = sum(f[1] for f in vivos)
    Lg(f"\n===== {titulo}: {len(filas)} mercados, {len(vivos)} con relleno, sueltas {n_s}, PnL base {sum(f[2] for f in filas):+.2f} $")
    for i, nom in enumerate(["bn1 (Binance 1 s en contra, bps)", "dm2 (caída del mid propio 2 s)", "edad del precio (ms; menor=joven)"]):
        pos = [f[3][i] for f in vivos if f[1]]
        neg = [f[3][i] for f in vivos if not f[1]]
        if i == 2:
            pos, neg = [-x if x is not None else None for x in pos], [-x if x is not None else None for x in neg]
        a, npos, nneg = auc(pos, neg)
        Lg(f"  AUC suelta vs par, {nom}: {a:.3f} (n {npos}/{nneg})")
    res = {}
    for nom, R in REGLAS.items():
        enc_frac, sal, pnl_pol, ev_s, ev_p = [], 0, 0.0, 0, 0
        for m, suelta, pnl, rr, rej in filas:
            hits = [R(y) or R(nn) for y, nn in rej]
            enc_frac.append(np.mean(hits) if hits else 0.0)
            if any(hits):
                sal += 1
                ev_s += bool(suelta)
                ev_p += suelta is False
            else:
                pnl_pol += pnl
        res[nom] = pnl_pol
        Lg(f"  SALIR si [{nom:22s}] antes del 1er relleno: sale en {sal:3d}/{len(filas)} merc. (evita {ev_s} sueltas, "
           f"pierde {ev_p} pares) | señal encendida P50 {np.median(enc_frac):.0%} de la vida | PnL {pnl_pol:+.2f} $")
    return res


def main():
    lines = []

    def Lg(s=""):
        print(s, flush=True)
        lines.append(s)
    desc = cargar_mercados("2026-10-09", "2026-10-11")
    val = [m for m in cargar_mercados("2026-10-12T14:59", "2026-10-14") if m["pol"] == "crear"]
    todos = desc + val
    gan = desenlaces({m["id"] for m in todos})
    L = cargar_libros(todos)
    dias = sorted({m["dia"] for m in todos} | {"2026-10-13"})
    B = cargar_binance(dias)
    Lg(f"Defensa por cancelación en pares 15m (LAT={LAT} ms). Binance: " + ", ".join(f"{s} {len(v[0])}" for s, v in B.items()))
    evaluar(desc, gan, L, B, Lg, "DESCUBRIMIENTO 09-10 Oct (todas las políticas)")
    evaluar(val, gan, L, B, Lg, "VALIDACIÓN 12-13 Oct (crear)")
    Lg("\nLectura: una regla solo sirve si en DESCUBRIMIENTO evita más sueltas que pares con la señal encendida una fracción "
       "pequeña de la vida, y repite en VALIDACIÓN (10 reglas miradas: corregir por multiplicidad).")
    INF.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"-> {INF}")


if __name__ == "__main__":
    main()
