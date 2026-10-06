#!/usr/bin/env python3
"""analisis_arbitraje_anidado_maker_frontera.py -- B1 nueva fase, paso 2 (06-Oct, Javi: "¿podemos estar ya colocados
cuando aparezca la liquidez barata?").

Precursor del paso 1: el arbitraje nace casi siempre desde un estado "cerca de la frontera" (neto de asks >= THETA, con
neto = 1 - askA - askB - fee(askA) - fee(askB)), visible >= 500 ms antes. Política simulada, CAUSAL (solo datos con
recepción <= decisión), sobre las ventanas 5m>15m del registro ms con ref conocible (mismo par que el escáner):
  - cuando neto >= THETA: poner PUJAS maker (comisión 0) en A (15m) y B (5m) a pA = min(bidA + 1 tick, askA - 1 tick),
    pB igual, solo si pA + pB <= 1 - MARGEN; SHARES acciones por pata; llegan al libro LAT_POST ms después.
  - cola: si la puja mejora el mejor bid somos los primeros de un nivel nuevo; si iguala, delante va el tamaño visible.
  - relleno: una operación del token a precio < nuestra puja nos llena; a precio == consume primero la cola de delante.
  - cancelación: cuando neto < THETA - 0,01 (o al cerrar el 5m - 10 s), efectiva LAT_CANCEL ms después.
  - pata suelta (solo una llena): tres políticas, reportadas por separado:
      COMPLETAR = comprar la otra como tomador al ask en t_relleno + L_TAKER (215 ms), al precio que haya;
      COMPLETAR_SI_GARANTIZA = solo si p_llena + ask_otra + fee <= 1, si no queda abierta;
      ABIERTA = sin cubrir (PnL DIRECCIONAL con desenlace oficial; nunca se cuenta como arbitraje).
Resultado: arbitraje verdadero (ambas pujas llenas) aparte de lo cubierto y de lo direccional; por ventana; sin la
ventana BTC 06-Oct 07:00. Uso: --theta -0.02 [--margen 0.01] [--desde ...]
"""
import argparse
import bisect
import collections
import glob
import gzip
import statistics as st
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_arbitraje_anidado_ms_scanner import cargar_twap60, fee, GAP_MIN_BPS, REF_CONOCIBLE_MS  # noqa: E402
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402

DL = "/root/polymarket-research-datalogs"
TICK = 0.01
LAT_POST, LAT_CANCEL, L_TAKER = 100, 100, 215
SHARES = 5.0


def cargar(desde_ms):
    fich = sorted(glob.glob(f"{DL}/maker_ms_*.csv.gz"), key=lambda f: Path(f).stat().st_mtime)
    tw = cargar_twap60(sorted({Path(f).name[9:19] for f in fich}))
    meta, idx, V, tok2 = {}, collections.defaultdict(dict), {}, {}
    for f in fich:
        try:
            for ln in gzip.open(f, "rt"):
                c = ln.rstrip("\n").split(",")
                tp = c[0]
                if tp == "k" and c[4] in ("5min", "15min"):
                    cierre = int(datetime.fromisoformat(c[6]).timestamp())
                    idx[(c[3], cierre)][(c[4], c[7])] = (c[2], c[5])
                    k = (c[3], cierre)
                    t = idx[k]
                    if k not in V and all(x in t for x in (("5min", "YES"), ("5min", "NO"), ("15min", "YES"), ("15min", "NO"))):
                        rl, rc = tw.get(c[3], {}).get(cierre - 900), tw.get(c[3], {}).get(cierre - 300)
                        if rl is None or rc is None or abs((rc / rl - 1) * 1e4) < GAP_MIN_BPS:
                            V[k] = None
                            continue
                        if rl < rc:
                            (A, ml), (B, mc), pa, pb = t[("15min", "YES")], t[("5min", "NO")], "Up_largo", "Down_corto"
                        else:
                            (A, ml), (B, mc), pa, pb = t[("15min", "NO")], t[("5min", "YES")], "Down_largo", "Up_corto"
                        V[k] = {"A": A, "B": B, "ml": ml, "mc": mc, "pa": pa, "pb": pb, "q": {A: [], B: []}, "t": {A: [], B: []}}
                        tok2[A], tok2[B] = k, k
                elif tp in ("q", "t"):
                    k = tok2.get(c[2])
                    if k is None or V.get(k) is None:
                        continue
                    w = V[k]
                    if tp == "q":
                        tr = int(c[7]) if len(c) > 7 and c[7] else int(c[1])
                        f_ = lambda x: None if x in ("", "None") else float(x)
                        w["q"][c[2]].append((tr, f_(c[3]), f_(c[4]), f_(c[5]) or 0.0, f_(c[6]) or 0.0))
                    else:
                        tr = int(c[6]) if len(c) > 6 and c[6] else int(c[1])
                        w["t"][c[2]].append((tr, float(c[3]), float(c[5])))
        except (EOFError, OSError):
            pass
    return {k: v for k, v in V.items() if v and k[1] * 1000 > desde_ms + 300_000}


class Serie:
    """Estados ordenados por hora con su índice de tiempos (sin cachés por id(), que Python reutiliza)."""
    def __init__(self, filas):
        self.v = sorted(filas, key=lambda x: x[0])
        self.t = [x[0] for x in self.v]

    def __add__(self, otra):
        return self.v + otra.v


def estado(qs, t):
    i = bisect.bisect_right(qs.t, t) - 1
    return qs.v[i] if i >= 0 else None


def simular_pata(qs, ts, precio, t_on, t_off):
    """Puja maker de SHARES a `precio` viva en [t_on, t_off). -> instante de relleno o None."""
    e = estado(qs, t_on)
    ts = ts.v[bisect.bisect_left(ts.t, t_on):]
    if e is None or e[1] is None:
        return None
    delante = e[3] if abs(e[1] - precio) < 1e-9 else 0.0     # igualar el mejor bid: cola visible delante
    consumido = 0.0
    for tr, p, sz in ts:
        if tr >= t_off:
            break
        if p < precio - 1e-9:
            return tr
        if abs(p - precio) < 1e-9:
            consumido += sz
            if consumido >= delante + SHARES:
                return tr
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--theta", type=float, default=-0.02)
    ap.add_argument("--margen", type=float, default=0.01)
    ap.add_argument("--desde", default="2026-10-05T16:06")
    a = ap.parse_args()
    desde = int(datetime.fromisoformat(a.desde).replace(tzinfo=timezone.utc).timestamp() * 1000)
    V = cargar(desde)
    des = desenlaces({w[m] for w in V.values() for m in ("ml", "mc")})
    res = []
    for (mon, cierre), w in V.items():
        if w["ml"] not in des or w["mc"] not in des:
            continue
        pagoA = 1.0 if (des[w["ml"]] == "YES") == w["pa"].startswith("Up") else 0.0
        pagoB = 1.0 if (des[w["mc"]] == "YES") == w["pb"].startswith("Up") else 0.0
        qa, qb = Serie(w["q"][w["A"]]), Serie(w["q"][w["B"]])
        ta, tb = Serie(w["t"][w["A"]]), Serie(w["t"][w["B"]])
        t_ini = (cierre - 300) * 1000 + REF_CONOCIBLE_MS
        t_fin = cierre * 1000 - 10_000
        # instantes de decisión = cambios de top de A o B
        cambios = sorted({x[0] for x in qa + qb if t_ini <= x[0] < t_fin})
        activo_hasta = -1
        for ic, t in enumerate(cambios):
            if t < activo_hasta:
                continue
            ea, eb = estado(qa, t), estado(qb, t)
            if not ea or not eb or ea[2] is None or eb[2] is None or ea[1] is None or eb[1] is None:
                continue
            neto = 1 - ea[2] - eb[2] - fee(ea[2]) - fee(eb[2])
            if neto < a.theta:
                continue
            pA = round(min(ea[1] + TICK, ea[2] - TICK), 2)
            pB = round(min(eb[1] + TICK, eb[2] - TICK), 2)
            if pA <= 0 or pB <= 0 or pA + pB > 1 - a.margen + 1e-9:
                continue
            # fin de la cotización: primer cambio con neto < theta - 0,01, o t_fin
            t_off = t_fin
            for t2 in cambios[ic + 1:]:
                e2a, e2b = estado(qa, t2), estado(qb, t2)
                if e2a and e2b and e2a[2] is not None and e2b[2] is not None:
                    n2 = 1 - e2a[2] - e2b[2] - fee(e2a[2]) - fee(e2b[2])
                    if n2 < a.theta - 0.01:
                        t_off = t2 + LAT_CANCEL
                        break
            t_on = t + LAT_POST
            fA = simular_pata(qa, ta, pA, t_on, t_off)
            fB = simular_pata(qb, tb, pB, t_on, t_off)
            r = {"ventana": f"{mon}_{cierre}", "t": t, "pA": pA, "pB": pB, "fA": fA, "fB": fB,
                 "dur_ms": t_off - t_on}
            if fA and fB:
                r["clase"] = "TRUE_ARB"
                r["pnl"] = SHARES * (pagoA + pagoB - pA - pB)
                r["garantizado"] = SHARES * (1 - pA - pB)
            elif fA or fB:
                lado = "A" if fA else "B"
                p_llena, pago_llena = (pA, pagoA) if fA else (pB, pagoB)
                qo, pago_otra = (qb, pagoB) if fA else (qa, pagoA)
                tf = fA or fB
                eo = estado(qo, tf + L_TAKER)
                ask_o = eo[2] if eo else None
                r["clase"] = "PARCIAL_" + lado
                r["direccional"] = SHARES * (pago_llena - p_llena)
                if ask_o is not None:
                    r["completar"] = SHARES * (pago_llena + pago_otra - p_llena - ask_o - fee(ask_o))
                    r["completar_garantia"] = SHARES * (1 - p_llena - ask_o - fee(ask_o))
                else:
                    r["completar"] = None
                    r["completar_garantia"] = None
            else:
                r["clase"] = "NADA"
            res.append(r)
            activo_hasta = t_off
    print(f"theta {a.theta} margen {a.margen}: ventanas {len(V)}, cotizaciones {len(res)}, "
          f"en {len({r['ventana'] for r in res})} ventanas")
    c = collections.Counter(r["clase"] for r in res)
    print(f"  clases: {dict(c)}")
    for nombre, filtro in (("TODAS", lambda r: True), ("SIN BTC 06-Oct 07:00", lambda r: r["ventana"] != "BTC_1791270000")):
        R = [r for r in res if filtro(r)]
        tr = [r for r in R if r["clase"] == "TRUE_ARB"]
        par = [r for r in R if r["clase"].startswith("PARCIAL")]
        comp = [r["completar"] for r in par if r.get("completar") is not None]
        compg = [(r["completar"] if r["completar_garantia"] is not None and r["completar_garantia"] >= 0 else r["direccional"])
                 for r in par if r.get("completar") is not None]
        print(f"  [{nombre}] TRUE_ARB n={len(tr)} PnL {sum(r['pnl'] for r in tr):+.2f} $ (garantizado "
              f"{sum(r['garantizado'] for r in tr):+.2f}) | PARCIALES n={len(par)}: si se COMPLETAN como tomador "
              f"{sum(comp):+.2f} $ | completar solo si garantiza (si no, abierta) {sum(compg):+.2f} $ | ABIERTAS "
              f"(DIRECCIONAL, aparte) {sum(r['direccional'] for r in par):+.2f} $")
        if par:
            print(f"     ¿qué pata se llena sola? A(15m) {sum(r['clase'] == 'PARCIAL_A' for r in par)}, "
                  f"B(5m) {sum(r['clase'] == 'PARCIAL_B' for r in par)} | coste medio de completar por cotización "
                  f"{st.mean(comp) if comp else 0:+.3f} $")
    pv = collections.defaultdict(float)
    for r in res:
        pv[r["ventana"]] += (r.get("pnl") or 0) + (r.get("completar") or 0)
    top = sorted(pv.items(), key=lambda kv: -abs(kv[1]))[:5]
    print("  ventanas con más |PnL| (true-arb + completadas):", [(k, round(v, 2)) for k, v in top])


if __name__ == "__main__":
    main()
