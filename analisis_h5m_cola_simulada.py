#!/usr/bin/env python3
"""analisis_h5m_cola_simulada.py -- (a) de la decisión de Javi 14-Oct: ¿qué EV tendríamos NOSOTROS en la celda confirmada
H5M-BARATO-MAKER-v1 (comprar como maker el lado de 0,10-0,30 con T en (60, 300] en 5m) teniendo en cuenta NUESTRA
posición en la cola? El vigía forward mide a makers que SÍ se rellenaron; aquí se simula una orden virtual nuestra sobre
el registro ms (m5_registro_D.csv.gz: q = top del libro sin muestrear, t = operaciones, ambos con hora del exchange y de
recepción) con el mismo modelo de rellenos del ensayo en seco de pares (experimento_pares_cola_15m.simular_rellenos,
16ª /code-review):
  - un bid nuestro en el token s a precio b se consume con VENTAS tomadoras de s a p <= b y COMPRAS tomadoras del
    contrario a p' >= 1-b (acuñación); las compras de s no cuentan;
  - precio equivalente < b -> atravesó el nivel: llena entera; == b -> suma volumen y llena lo que supere la cola que
    teníamos delante al entrar (las cancelaciones de delante no se ven: conservador en relleno);
  - solo operaciones con hora del EXCHANGE >= decisión (recepción) + LAT_POST_MS y <= cancelación + LAT_CANCEL_MS.

Políticas FIJADAS antes de mirar resultados (una orden por mercado-lado, SH acciones, sin recolocar):
  ANCLAR: al primer top (recepción) con T en (60, 300] y bid b en (0,10, 0,30] con ask > b -> bid en b, cola delante =
          tamaño del mejor bid en ese top.
  CREAR:  al primer top con T en (60, 300], b+0,01 en (0,10, 0,30] y b+0,01 < ask -> bid en b+0,01, cola delante 0.
  SEGUIR: (añadida 14-Oct tras ver en una muestra que una orden FIJA es el maker pasivo que pierde, antes de mirar su
          resultado) cotiza SIEMPRE en el mejor bid mientras b esté en (0,10, 0,30] con ask > b: cada top nuevo con otro
          bid -> cancelar (efectiva + LAT_CANCEL_MS) y recolocar en el nuevo b al FINAL de la cola (cola = tamaño del
          bid); si b sale de la banda, cancelar y esperar. Acumula hasta SH acciones por mercado-lado.
  SEGUIR_CABEZA: igual con cola delante 0 (cota optimista: mide cuánto pesa la posición en la cola).
  Todas se cancelan a T = 60 s. PnL a resolución con desenlace OFICIAL (gamma closed=true), SIN reembolso de maker
  (se informa aparte una estimación: 20 % de la comisión 0,07·p·(1-p) por acción rellenada).

Fidelidad: por día se compara con el vigía H5M (makers on-chain rellenados, todos y "final de la cola").
Salida: datalogs/h5m_cola_sim/unidades_D.csv.gz (caché por día) + informe.txt/json.
Uso: nice -n 19 ionice -c3 python3 analisis_h5m_cola_simulada.py --desde 2026-10-09 [--hasta D] [--max-lineas N]
"""
import argparse
import csv
import gzip
import json
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402
from archivo_volumen import VOL  # noqa: E402

OUT = Path("/root/polymarket-research-datalogs/h5m_cola_sim")
VIGIA = Path("/root/polymarket-research-datalogs/vigia_5m_barato_maker")
P_LO, P_HI = 0.10, 0.30          # banda (P_LO, P_HI] como la congelada
T_MIN, T_MAX = 60, 300
SH = 5.0                          # acciones por orden (min_order_size)
LAT_POST_MS = 68                  # GTC post-only medida 07-Oct (P50)
LAT_CANCEL_MS = 60
POLITICAS = ("ANCLAR", "CREAR", "SEGUIR", "SEGUIR_CABEZA")
SEGUIDORAS = ("SEGUIR", "SEGUIR_CABEZA")
RNG = np.random.default_rng(14)


class Orden:
    """Una o varias cotizaciones sucesivas (segmentos [precio, cola, t_post, t_cancel, vol, lleno]) de un mercado-lado."""
    __slots__ = ("pol", "tok", "segs", "t_fin")

    def __init__(self, pol, tok, t_fin):
        self.pol, self.tok, self.segs, self.t_fin = pol, tok, [], t_fin

    def cotizar(self, precio, cola, t_rx):
        self.segs.append([precio, cola, t_rx + LAT_POST_MS, self.t_fin, 0.0, 0.0])

    def cancelar(self, t_rx):
        if self.segs and self.segs[-1][3] > t_rx:
            self.segs[-1][3] = t_rx

    @property
    def lleno(self):
        return sum(g[5] for g in self.segs)

    @property
    def coste(self):
        return sum(g[5] * g[0] for g in self.segs)

    @property
    def viva(self):
        return bool(self.segs) and self.segs[-1][3] == self.t_fin

    def consumir(self, t_ex, pe, sz):
        for g in self.segs:
            falta = SH - self.lleno
            if falta <= 1e-9:
                return
            if t_ex < g[2] or t_ex > g[3] + LAT_CANCEL_MS:
                continue
            if pe < g[0] - 1e-9:
                g[5] += falta
            elif abs(pe - g[0]) < 1e-9:
                g[4] += sz
                nuevo = min(g[5] + falta, max(g[5], g[4] - g[1]))
                g[5] = nuevo


def simular_dia(d, max_lineas=None):
    f = VOL / "m5_registro" / f"m5_registro_{d}.csv.gz"
    if not f.exists():
        return None
    meta = {}                     # token -> (act, mkt, fin_ms, lado)
    por_mkt = {}                  # mkt -> {lado: token}
    ordenes = {}                  # (pol, token) -> Orden
    hechos = set()                # (pol, token) ya decididos (una orden por mercado-lado)
    n = 0
    with gzip.open(f, "rt", errors="replace") as fh:
        try:
            for ln in fh:
                n += 1
                if max_lineas and n > max_lineas:
                    break
                tp = ln[:2]
                if tp == "x," or tp == "ti":
                    continue
                c = ln.rstrip("\n").split(",")
                if tp == "k,":
                    if len(c) >= 8 and c[4] == "5min":
                        fin = int(datetime.fromisoformat(c[6]).timestamp() * 1000)
                        meta[c[2]] = (c[3], c[5], fin, c[7])
                        por_mkt.setdefault(c[5], {})[c[7]] = c[2]
                    continue
                tk = c[2]
                m = meta.get(tk)
                if m is None:
                    continue
                if tp == "q,":
                    try:
                        bid, ask, bsz = float(c[3]), float(c[4]), float(c[5])
                        t_rx = int(c[7])
                    except (ValueError, IndexError):
                        continue
                    T = (m[2] - t_rx) / 1000.0
                    if not (T_MIN < T <= T_MAX):
                        continue
                    for pol in SEGUIDORAS:
                        o = ordenes.get((pol, tk))
                        if o is not None and o.lleno >= SH - 1e-9:
                            continue
                        b = round(bid, 2)
                        ok = P_LO < b <= P_HI and b < ask - 1e-9
                        if o is not None and o.viva:
                            if ok and abs(o.segs[-1][0] - b) < 1e-9:
                                continue                      # seguimos en el top
                            o.cancelar(t_rx)
                        if ok:
                            if o is None:
                                o = ordenes[(pol, tk)] = Orden(pol, tk, m[2] - T_MIN * 1000)
                            o.cotizar(b, bsz if pol == "SEGUIR" else 0.0, t_rx)
                    for pol in ("ANCLAR", "CREAR"):
                        if (pol, tk) in hechos:
                            continue
                        if pol == "ANCLAR":
                            precio, cola = round(bid, 2), bsz
                        else:
                            precio, cola = round(bid + 0.01, 2), 0.0
                        if not (P_LO < precio <= P_HI) or precio >= ask - 1e-9:
                            continue
                        hechos.add((pol, tk))
                        o = ordenes[(pol, tk)] = Orden(pol, tk, m[2] - T_MIN * 1000)
                        o.cotizar(precio, cola, t_rx)
                elif tp == "t,":
                    try:
                        p, side, sz = float(c[3]), c[4], float(c[5])
                        t_ex = int(c[1])
                    except (ValueError, IndexError):
                        continue
                    if side == "SELL":
                        objetivo, pe = tk, p
                    elif side == "BUY":
                        objetivo, pe = por_mkt.get(m[1], {}).get("NO" if m[3] == "YES" else "YES"), round(1.0 - p, 4)
                        if objetivo is None:
                            continue
                    else:
                        continue
                    for pol in POLITICAS:
                        o = ordenes.get((pol, objetivo))
                        if o is not None:
                            o.consumir(t_ex, pe, sz)
        except (EOFError, OSError) as e:
            print(f"  {d}: fichero truncado ({type(e).__name__}) tras {n} líneas", file=sys.stderr)
    des = desenlaces({meta[o.tok][1] for o in ordenes.values()})
    filas = []
    for o in ordenes.values():
        act, mkt, fin, lado = meta[o.tok]
        r = des.get(mkt)
        ll, co = o.lleno, o.coste
        pm = co / ll if ll > 0 else o.segs[0][0]
        filas.append({"dia": d, "pol": o.pol, "mkt": mkt, "act": act, "lado": lado, "precio": round(pm, 4),
                      "cola": o.segs[0][1], "n_cotiz": len(o.segs), "T_post": round((fin - o.segs[0][2]) / 1000, 1),
                      "lleno": round(ll, 4), "des": r or "", "coste": round(co, 6),
                      "pnl": round((ll if r == lado else 0.0) - co, 6) if r else "",
                      "rebate": round(sum(g[5] * 0.2 * 0.07 * g[0] * (1 - g[0]) for g in o.segs), 6)})
    return filas


def ic_dias(v):
    v = np.asarray(v, float)
    if len(v) < 2:
        return (float("nan"), float("nan"))
    m = v[RNG.integers(0, len(v), size=(2000, len(v)))].mean(1)
    return (float(np.quantile(m, .05)), float(np.quantile(m, .95)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--desde", default="2026-10-09")
    ap.add_argument("--hasta")
    ap.add_argument("--max-lineas", type=int, default=None, help="prueba rápida: no cachea")
    a = ap.parse_args()
    OUT.mkdir(exist_ok=True)
    d0 = date.fromisoformat(a.desde)
    d1 = date.fromisoformat(a.hasta) if a.hasta else datetime.now(timezone.utc).date() - timedelta(days=1)
    filas = []
    d = d0
    while d <= d1:
        ds = d.isoformat()
        cache = OUT / f"unidades_{ds}.csv.gz"
        if cache.exists() and not a.max_lineas:
            with gzip.open(cache, "rt") as fh:
                filas += list(csv.DictReader(fh))
        else:
            fs = simular_dia(ds, a.max_lineas)
            if fs is not None:
                cob = np.mean([bool(x["des"]) for x in fs]) if fs else 0.0
                print(f"{ds}: {len(fs)} órdenes, cobertura desenlaces {cob:.1%}")
                if not a.max_lineas and cob >= 0.99:
                    with gzip.open(cache, "wt") as fh:
                        w = csv.DictWriter(fh, fieldnames=list(fs[0].keys()))
                        w.writeheader()
                        w.writerows(fs)
                filas += fs
        d += timedelta(days=1)
    lin = [f"H5M cola simulada (SH={SH:g} acc, post {LAT_POST_MS} ms, cancel T={T_MIN}s+{LAT_CANCEL_MS} ms, sin reembolso)"]
    res = {}
    vig = {}
    try:
        vig = json.loads((VIGIA / "informe.json").read_text()).get("dias", {})
    except Exception:
        pass
    for pol in POLITICAS:
        F = [x for x in filas if x["pol"] == pol and x["des"]]
        R = [x for x in F if float(x["lleno"]) > 0]
        dias = sorted({x["dia"] for x in F})
        ev_d, lin_d = [], []
        for ds in dias:
            Rd = [x for x in R if x["dia"] == ds]
            Fd = [x for x in F if x["dia"] == ds]
            ev = np.mean([float(x["pnl"]) / float(x["coste"]) for x in Rd]) if Rd else float("nan")
            usd = sum(float(x["pnl"]) for x in Rd)
            reb = sum(float(x["rebate"]) for x in Rd)
            ev_d.append(ev)
            v = vig.get(ds, {})
            lin_d.append(f"    {ds}: órdenes {len(Fd)} | rellenas {len(Rd)} ({len(Rd) / max(1, len(Fd)):.0%}) | EV/€ {ev:+.4f} "
                         f"| PnL {usd:+.2f} $ (+reemb {reb:.2f}) | vigía makers {v.get('ev', float('nan')):+.4f} final cola "
                         f"{v.get('ev_final_cola', float('nan')):+.4f}")
        evs = [float(x["pnl"]) / float(x["coste"]) for x in R]
        lo, hi = ic_dias([e for e in ev_d if e == e])
        sinbtc = [float(x["pnl"]) / float(x["coste"]) for x in R if x["act"] != "BTC"]
        llenas = [x for x in R if float(x["lleno"]) >= SH - 1e-9]
        parc = [x for x in R if float(x["lleno"]) < SH - 1e-9]
        res[pol] = {"ordenes": len(F), "rellenas": len(R), "ev_unidad": float(np.mean(evs)) if evs else None,
                    "ic90_dias": [lo, hi], "ev_sin_btc": float(np.mean(sinbtc)) if sinbtc else None,
                    "pnl_usd": sum(float(x["pnl"]) for x in R), "dias": len(dias)}
        lin.append(f"\n{pol}: órdenes {len(F)} | rellenas {len(R)} ({len(R) / max(1, len(F)):.0%}; enteras {len(llenas)}, parciales "
                   f"{len(parc)}) | EV/€ unidad {np.mean(evs) if evs else float('nan'):+.4f} IC90 días ({lo:+.4f},{hi:+.4f}) | "
                   f"sin BTC {np.mean(sinbtc) if sinbtc else float('nan'):+.4f} | PnL {res[pol]['pnl_usd']:+.2f} $ en {len(dias)} días")
        for nombre, sub in (("enteras", llenas), ("parciales", parc)):
            if sub:
                lin.append(f"    {nombre}: EV/€ {np.mean([float(x['pnl']) / float(x['coste']) for x in sub]):+.4f} n={len(sub)} "
                           f"acierto {np.mean([x['des'] == x['lado'] for x in sub]):.1%} precio medio "
                           f"{np.mean([float(x['precio']) for x in sub]):.3f}")
        nr = [x for x in F if float(x["lleno"]) == 0]
        if nr:
            lin.append(f"    NO rellenas n={len(nr)}: acierto del lado {np.mean([x['des'] == x['lado'] for x in nr]):.1%} "
                       f"precio medio {np.mean([float(x['precio']) for x in nr]):.3f} (selección adversa si acierta más que las rellenas)")
        lin += lin_d
    txt = "\n".join(lin)
    print(txt)
    if not a.max_lineas:
        (OUT / "informe.txt").write_text(txt + "\n")
        (OUT / "informe.json").write_text(json.dumps(res, indent=1, default=str))


if __name__ == "__main__":
    main()
