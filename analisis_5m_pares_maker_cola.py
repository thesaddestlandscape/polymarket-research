#!/usr/bin/env python3
"""5m barato subestrategia 4 REORIENTADA (OK Javi 14-Oct): COMPLETAR PARES COMO MAKER en 5m, con nuestra posición en la cola.

Motivo: en BTC el relleno maker de la banda barata con el OTRO lado ya comprado antes gana +0,046 €/€ (4/5 días) y el de
un solo lado ≈0 (analisis_h5m_poblacion_pares_antes.py). Aquí se simula NUESTRA versión sobre el registro ms
(m5_registro_D.csv.gz; q = t_ex,token,bid,ask,bsz,asz,t_rx; t = t_ex,token,precio,side,tam,t_rx) con el modelo de rellenos
de analisis_h5m_cola_simulada.py (ventas tomadoras del token a p <= b y compras tomadoras del contrario a p' >= 1-b;
precio equivalente < b atraviesa y llena; == b suma volumen y llena lo que supere la cola de delante; solo operaciones con
hora del exchange >= post + 68 ms y <= cancelación + 60 ms).

POLÍTICAS FIJADAS ANTES DE MIRAR (14-Oct ~16:30Z), por mercado 5m, dos tokens, hasta SH=5 acciones por token:
  - Modo PATA 1 (el otro token sin rellenos): cotiza en el MEJOR bid b mientras T en (60, 300], b en (0,10, BANDA] y b < ask
    (recoloca al final de la cola en cada top nuevo, como SEGUIR).
  - Modo COMPLETAR (el otro token ya tiene rellenos a precio medio p1, conocido a la hora de RECEPCIÓN de la operación):
    precio = min(mejor bid, tope) con tope = floor((1 − p1 − M)·100)/100, mientras T en (10, 300] y precio < ask; si el
    precio queda por debajo del mejor bid la cola de delante es desconocida → solo rellena lo que ATRAVIESA (conservador)
    hasta que el mejor bid baje a nuestro precio (entonces cola = tamaño del bid en ese instante, final de la cola).
  - Se cancela todo a T = 10 s (pata 1 a T = 60 s). Lo que quede sin pareja se valora al desenlace OFICIAL.
  Rejilla elegible SOLO en DESC (05-09): BANDA ∈ {0,30, 0,45} × M ∈ {0,02, 0,04}, cola FINAL. Variante CABEZA (cola 0) =
  cota optimista, informativa, NO elegible. Universo de decisión: BTC (Javi: foco BTC); el resto, diagnóstico.
  OOS 10-13 (pares 5m nunca mirados en OOS) se juzga UNA vez con la política elegida en DESC.
Métricas por mercado: EV/€ = ΣPnL/Σcoste, $/mercado con rellenos, % pares completos (≥5 y ≥5), coste medio del par, PnL de
pares vs patas sueltas, IC90 por días; reembolso maker estimado aparte (20 % de 0,07·p·(1−p) por acción).
Salida: datalogs/m5_pares_maker/mercados_D.csv.gz (caché por día) + informe.txt.
Uso: nice -n 19 ionice -c3 /usr/bin/python3 analisis_5m_pares_maker_cola.py [--dias 2026-10-05,...]
"""
import argparse
import csv
import gzip
import math
import sys
from datetime import datetime
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402
from archivo_volumen import VOL  # noqa: E402

OUT = Path("/root/polymarket-research-datalogs/m5_pares_maker")
DIAS = ["2026-10-05", "2026-10-06", "2026-10-07", "2026-10-08", "2026-10-09",
        "2026-10-10", "2026-10-11", "2026-10-12", "2026-10-13"]
DESC, OOS = DIAS[:5], DIAS[5:]
P_LO = 0.10
T1_MIN, T2_MIN, T_MAX = 60, 10, 300
SH = 5.0
LAT_POST_MS, LAT_CANCEL_MS = 68, 60
INF = float("inf")
POLS = [(f"B{int(b * 100)}_M{int(m * 100)}_{c}", b, m, c) for c in ("FINAL", "CABEZA") for b in (0.30, 0.45) for m in (0.02, 0.04)]
ELEGIBLES = [p[0] for p in POLS if p[3] == "FINAL"]


class Pata:
    """Cotizaciones sucesivas de un token: segmentos [precio, cola, t_post, t_cancel, vol, lleno]."""
    __slots__ = ("segs", "t_fin")

    def __init__(self, t_fin):
        self.segs, self.t_fin = [], t_fin

    @property
    def lleno(self):
        return sum(g[5] for g in self.segs)

    @property
    def coste(self):
        return sum(g[5] * g[0] for g in self.segs)

    def viva(self, t):
        return bool(self.segs) and self.segs[-1][3] > t

    def cotizar(self, precio, cola, t_rx, t_fin):
        self.segs.append([precio, cola, t_rx + LAT_POST_MS, t_fin, 0.0, 0.0])

    def cancelar(self, t_rx):
        if self.segs and self.segs[-1][3] > t_rx:
            self.segs[-1][3] = t_rx

    def consumir(self, t_ex, pe):
        """Devuelve True si hubo relleno nuevo (para avisar al otro token)."""
        nuevo = False
        for g in self.segs:
            falta = SH - self.lleno
            if falta <= 1e-9:
                break
            if t_ex < g[2] or t_ex > g[3] + LAT_CANCEL_MS:
                continue
            if pe[0] < g[0] - 1e-9:
                g[5] += falta
                nuevo = True
            elif abs(pe[0] - g[0]) < 1e-9 and g[1] < INF:
                g[4] += pe[1]
                n = min(g[5] + falta, max(g[5], g[4] - g[1]))
                if n > g[5] + 1e-12:
                    g[5] = n
                    nuevo = True
        return nuevo


def simular_dia(d):
    f = VOL / "m5_registro" / f"m5_registro_{d}.csv.gz"
    if not f.exists():
        return None
    meta, par = {}, {}                       # token -> (act, mkt, fin_ms, lado); token -> token contrario
    por_mkt = {}
    top = {}                                 # token -> (bid, ask, bsz)
    est = {}                                 # (pol, token) -> Pata
    aviso = {}                               # (pol, token) -> t_rx desde el que el OTRO token tiene rellenos

    def evaluar(pol, tk, t_rx):
        nom, banda, M, colam = pol
        m = meta[tk]
        T = (m[2] - t_rx) / 1000.0
        tp = top.get(tk)
        if tp is None or not (T2_MIN < T <= T_MAX):
            return
        o = est.get((nom, tk))
        if o is not None and o.lleno >= SH - 1e-9:
            return
        bid, ask, bsz = tp
        b = round(bid, 2)
        otro = est.get((nom, par.get(tk)))
        completar = otro is not None and otro.lleno > 1e-9 and aviso.get((nom, tk), INF) <= t_rx
        if completar:
            p1 = otro.coste / otro.lleno
            tope = math.floor((1.0 - p1 - M) * 100 + 1e-6) / 100
            precio = min(b, tope)
            ok = precio > 0.0 and precio < ask - 1e-9
            cola = (0.0 if colam == "CABEZA" else bsz) if abs(precio - b) < 1e-9 else INF
            t_fin = m[2] - T2_MIN * 1000
        else:
            precio = b
            ok = T > T1_MIN and P_LO < b <= banda and b < ask - 1e-9
            cola = 0.0 if colam == "CABEZA" else bsz
            t_fin = m[2] - T1_MIN * 1000
        if o is not None and o.viva(t_rx):
            g = o.segs[-1]
            if ok and abs(g[0] - precio) < 1e-9:
                if g[1] == INF and cola < INF:          # el mejor bid bajó a nuestro precio: pasamos a cola conocida
                    o.cancelar(t_rx)
                    o.segs.append([precio, cola, t_rx, t_fin, 0.0, 0.0])
                return
            o.cancelar(t_rx)
        if ok:
            if o is None:
                o = est[(nom, tk)] = Pata(t_fin)
            o.cotizar(precio, cola, t_rx, t_fin)

    with gzip.open(f, "rt", errors="replace") as fh:
        try:
            for ln in fh:
                tp_ = ln[:2]
                if tp_ not in ("k,", "q,", "t,"):
                    continue
                c = ln.rstrip("\n").split(",")
                if tp_ == "k,":
                    if len(c) >= 8 and c[4] == "5min" and c[2] not in meta:
                        fin = int(datetime.fromisoformat(c[6]).timestamp() * 1000)
                        meta[c[2]] = (c[3], c[5], fin, c[7])
                        d_ = por_mkt.setdefault(c[5], {})
                        d_[c[7]] = c[2]
                        if len(d_) == 2:
                            a, b_ = d_.get("YES"), d_.get("NO")
                            if a and b_:
                                par[a], par[b_] = b_, a
                    continue
                tk = c[2]
                if tk not in meta or tk not in par:
                    continue
                if tp_ == "q,":
                    try:
                        top[tk] = (float(c[3]), float(c[4]), float(c[5]))
                        t_rx = int(c[7])
                    except (ValueError, IndexError):
                        continue
                    for pol in POLS:
                        evaluar(pol, tk, t_rx)
                else:
                    try:
                        p, side, sz, t_ex = float(c[3]), c[4], float(c[5]), int(c[1])
                        t_rx = int(c[6]) if len(c) > 6 and c[6] else t_ex + 50
                    except (ValueError, IndexError):
                        continue
                    if side == "SELL":
                        obj, pe = tk, (p, sz)
                    elif side == "BUY":
                        obj, pe = par[tk], (round(1.0 - p, 4), sz)
                    else:
                        continue
                    for pol in POLS:
                        o = est.get((pol[0], obj))
                        if o is not None and o.consumir(t_ex, pe):
                            k = (pol[0], par[obj])
                            if k not in aviso:
                                aviso[k] = t_rx
                                evaluar(pol, par[obj], t_rx)
        except (EOFError, OSError) as e:
            print(f"  {d}: fichero truncado ({type(e).__name__})", file=sys.stderr)
    mkts = {meta[tk][1] for (_, tk) in est}
    des = desenlaces(mkts)
    sin = len([m for m in mkts if m not in des])
    print(f"  {d}: desenlace oficial {len(mkts) - sin}/{len(mkts)} mercados con órdenes ({(len(mkts) - sin) / max(1, len(mkts)):.1%})", flush=True)
    filas = []
    for pol in POLS:
        vistos = set()
        for (nom, tk), o in est.items():
            if nom != pol[0] or meta[tk][1] in vistos:
                continue
            act, mkt, fin, _ = meta[tk]
            vistos.add(mkt)
            r = des.get(mkt)
            if not r:
                continue
            q, cst, reb = {}, {}, 0.0
            for lado in ("YES", "NO"):
                t2 = por_mkt[mkt].get(lado)
                o2 = est.get((nom, t2))
                q[lado] = o2.lleno if o2 else 0.0
                cst[lado] = o2.coste if o2 else 0.0
                if o2:
                    reb += sum(g[5] * 0.2 * 0.07 * g[0] * (1 - g[0]) for g in o2.segs)
            if q["YES"] + q["NO"] <= 1e-9:
                continue
            pares = min(q["YES"], q["NO"])
            coste = cst["YES"] + cst["NO"]
            pnl = q[r] - coste
            pm = {k: (cst[k] / q[k] if q[k] > 0 else 0.0) for k in q}
            pnl_pares = pares * (1.0 - pm["YES"] - pm["NO"]) if pares > 0 else 0.0
            filas.append({"dia": d, "pol": nom, "act": act, "mkt": mkt, "qY": round(q["YES"], 4), "qN": round(q["NO"], 4),
                          "pY": round(pm["YES"], 4), "pN": round(pm["NO"], 4), "coste": round(coste, 6),
                          "pnl": round(pnl, 6), "pnl_pares": round(pnl_pares, 6), "completo": int(pares >= SH - 1e-9),
                          "rebate": round(reb, 6), "des": r})
    return filas


def cargar(d):
    OUT.mkdir(parents=True, exist_ok=True)
    c = OUT / f"mercados_{d}.csv.gz"
    if c.exists():
        with gzip.open(c, "rt") as fh:
            return list(csv.DictReader(fh))
    filas = simular_dia(d)
    if filas is None:
        return []
    with gzip.open(c, "wt") as fh:
        w = csv.DictWriter(fh, fieldnames=list(filas[0].keys()) if filas else ["dia"])
        w.writeheader()
        w.writerows(filas)
    print(f"{d}: {len(filas)} mercado-política simulados", flush=True)
    return [{k: str(v) for k, v in r.items()} for r in filas]


def resumen(filas, pol, act=None, dias=None):
    s = [r for r in filas if r["pol"] == pol and (act is None or r["act"] == act) and (dias is None or r["dia"] in dias)]
    if not s:
        return None
    co = sum(float(r["coste"]) for r in s)
    pn = sum(float(r["pnl"]) for r in s)
    reb = sum(float(r["rebate"]) for r in s)
    pdia = {}
    for r in s:
        a = pdia.setdefault(r["dia"], [0.0, 0.0])
        a[0] += float(r["pnl"])
        a[1] += float(r["coste"])
    evd = np.array([a[0] / a[1] for a in pdia.values() if a[1] > 0])
    rng = np.random.default_rng(5)
    if len(evd) >= 2:
        bs = evd[rng.integers(0, len(evd), size=(3000, len(evd)))].mean(1)
        ic = (np.quantile(bs, .05), np.quantile(bs, .95))
    else:
        ic = (float("nan"), float("nan"))
    comp = [r for r in s if r["completo"] == "1"]
    suelta = sum(float(r["pnl"]) - float(r["pnl_pares"]) for r in s)
    cpar = np.mean([float(r["pY"]) + float(r["pN"]) for r in comp]) if comp else float("nan")
    return {"n": len(s), "ev": pn / co if co else float("nan"), "pnl": pn, "pnl_merc": pn / len(s), "reb": reb,
            "ic": ic, "dias_pos": int((evd > 0).sum()), "n_dias": len(evd), "pct_comp": len(comp) / len(s),
            "coste_par": cpar, "pnl_pares": sum(float(r["pnl_pares"]) for r in s), "pnl_sueltas": suelta}


def linea(nom, x):
    return (f"  {nom:18s} merc {x['n']:5d} | EV/€ {x['ev']:+.4f} IC90 días ({x['ic'][0]:+.4f},{x['ic'][1]:+.4f}) "
            f"{x['dias_pos']}/{x['n_dias']} días+ | PnL {x['pnl']:+8.2f} $ ({x['pnl_merc']:+.3f}/merc; +reemb {x['reb']:.2f}) | "
            f"pares completos {x['pct_comp']:.0%} coste par {x['coste_par']:.3f} | PnL pares {x['pnl_pares']:+.2f} sueltas {x['pnl_sueltas']:+.2f}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dias", default=",".join(DIAS))
    a = ap.parse_args()
    filas = []
    for d in a.dias.split(","):
        filas += cargar(d)
    L = ["5m PARES MAKER (subestrategia 4 reorientada) — selección en DESC 05-09 (BTC), juicio único en OOS 10-13"]
    L.append("\n== DESC 05-09 · BTC")
    mejor, mejor_ev = None, -9.0
    for pol in POLS:
        x = resumen(filas, pol[0], "BTC", DESC)
        if x:
            L.append(linea(pol[0], x))
            if pol[0] in ELEGIBLES and x["ev"] > mejor_ev:
                mejor, mejor_ev = pol[0], x["ev"]
    L.append(f"  ELEGIDA (solo DESC, cola FINAL): {mejor}")
    L.append("\n== OOS 10-13 · BTC (juicio único de la elegida; CABEZA = cota optimista)")
    for nom in (mejor, mejor.replace("FINAL", "CABEZA")):
        x = resumen(filas, nom, "BTC", OOS)
        if x:
            L.append(linea(nom, x))
    x = resumen(filas, mejor, "BTC", OOS)
    if x:
        L.append(f"  VEREDICTO OOS BTC {mejor}: {'POSITIVA (IC90 días > 0) -> congelar + forward' if x['ic'][0] > 0 else 'NO pasa (IC90 días cruza 0 o negativa)'}")
    L.append("\n== Diagnóstico otras monedas (NO para elegir) — política elegida, todos los días")
    for act in ("ETH", "SOL", "XRP", "DOGE", "BNB"):
        x = resumen(filas, mejor, act)
        if x:
            L.append(linea(act, x))
    txt = "\n".join(L)
    print(txt)
    (OUT / "informe.txt").write_text(txt + "\n")


if __name__ == "__main__":
    main()
