#!/usr/bin/env python3
"""analisis_maker_cancelacion_binance.py -- simula un MAKER que cotiza en el mejor bid de YES y NO de los mercados
up/down y CANCELA el lado amenazado cuando Binance se mueve en su contra, antes de que llegue el tomador (que
Polymarket retrasa 150 ms). Fuente: registro en ms de libro_estado_ws (datalogs maker_ms_YYYY-MM-DD_<pid>.csv.gz:
h = top del libro con hora del exchange, t = todas las operaciones, b = mid Binance por hora de RECEPCIÓN, k = mapa
token -> moneda/marco/mercado/cierre/lado). Desenlace OFICIAL (gamma por id, closed=true; se informa la cobertura).

Por qué (05-Oct, Javi: "haz que el hueco Binance -> Polymarket nos dé ventaja"): como tomador está cerrado (ni a +0,15 s
hay celda con IC90>0; en 300 ms el ask ya se movió 2-3,6c), pero ese movimiento lo hacen makers que recotizan a
tiempo; las wallets que ganan de forma sistemática acumulan pares como makers. Un maker QUIETO pierde −6/−10c por
mercado (analisis_pares_maker_sim_30sep.py): la línea base sin cancelación de aquí debe reproducirlo (si no, el
simulador está mal).

Modelo (conservador a propósito):
- Cotiza 1 bid por token (YES y NO) en el mejor bid del momento, SH acciones, hasta MAX_SH por lado y mercado,
  solo con entre T_MIN_S y T_MAX_S hasta el cierre y precio en [P_MIN, P_MAX].
- Relleno: una operación del CLOB por DEBAJO de nuestro precio (lo atravesó), o volumen a nuestro precio que supera
  la cola que teníamos delante al entrar (nos ponemos al final).
- Cancelación: Binance (mid) se mueve >= UMBRAL bps en VENTANA ms en contra del lado (sube -> amenaza NO; baja ->
  amenaza YES) => ese lado se cancela con efecto en t_recepción + LAT ms; no recotiza hasta ENFRIAMIENTO ms después.
- Pago a resolución con desenlace oficial; maker sin comisión; NO se cuenta la devolución del 20 % (conservador).
Unidad estadística: el MERCADO (PnL por mercado), IC90 por días. Gate de cualquier celda (no se mira aquí): n>=40
mercados, >=5 días, EV>0 con IC90 por días >0, ninguna moneda >60 % del PnL.
Uso: python3 analisis_maker_cancelacion_binance.py [--desde YYYY-MM-DD] [--hasta YYYY-MM-DD] [--marco 5min]
Solo lectura.
"""
import argparse
import bisect
import collections
import csv
import glob
import gzip
import io
import json
import random
import sys
from pathlib import Path

import requests

DATALOGS = Path("/root/polymarket-research-datalogs")
CACHE = DATALOGS / "maker_ms_desenlaces_cache.json"
SIMBOLO = {"BTC": "BTCUSDT", "ETH": "ETHUSDT", "SOL": "SOLUSDT", "XRP": "XRPUSDT", "DOGE": "DOGEUSDT",
           "BNB": "BNBUSDT"}
SH, MAX_SH = 5.0, 50.0
P_MIN, P_MAX = 0.05, 0.95


def leer(dias):
    """-> (meta {token: (act, marco, mid, fin_iso, lado)}, libro {token: [(t,bb,ba,bsz)]}, trades {token: [(t,p,side,sz)]},
    binance {sym: ([t], [mid])}). Tolera el final truncado de cada gz (corte brusco del proceso)."""
    meta, libro, trades = {}, collections.defaultdict(list), collections.defaultdict(list)
    bt, bm = collections.defaultdict(list), collections.defaultdict(list)
    for dia in dias:
        for f in sorted(DATALOGS.glob(f"maker_ms_{dia}_*.csv.gz")):
            try:
                with gzip.open(f, "rt", encoding="utf-8") as fh:
                    for r in csv.reader(fh):
                        try:
                            tipo = r[0]
                            if tipo == "h":
                                libro[r[2]].append((int(r[1]), float(r[3]) if r[3] not in ("", "None") else None,
                                                    float(r[4]) if r[4] not in ("", "None") else None,
                                                    float(r[5]) if r[5] not in ("", "None") else 0.0))
                            elif tipo == "t":
                                trades[r[2]].append((int(r[1]), float(r[3]), r[4], float(r[5])))
                            elif tipo == "b":
                                bt[r[2]].append(int(r[1]))
                                bm[r[2]].append((float(r[3]) + float(r[4])) / 2)
                            elif tipo == "k":
                                meta[r[2]] = (r[3], r[4], r[5], r[6], r[7])
                        except (ValueError, IndexError):
                            continue
            except (EOFError, OSError, gzip.BadGzipFile) as e:
                print(f"  aviso: {f.name} truncado ({type(e).__name__}); se usa lo leído", file=sys.stderr)
    for d in (libro, trades):
        for k in d:
            d[k].sort(key=lambda x: x[0])  # solo por hora: un lado vacío del libro es None y no se compara
    binance = {}
    for s in bt:
        orden = sorted(range(len(bt[s])), key=bt[s].__getitem__)
        binance[s] = ([bt[s][i] for i in orden], [bm[s][i] for i in orden])
    return meta, libro, trades, binance


def desenlaces(mids):
    try:
        c = json.loads(CACHE.read_text())
    except Exception:
        c = {}
    pend = sorted(m for m in set(mids) if m not in c)
    ses = requests.Session()
    for k in range(0, len(pend), 40):
        try:
            for m in ses.get("https://gamma-api.polymarket.com/markets", timeout=20,
                             params=[("id", x) for x in pend[k:k + 40]] + [("closed", "true"), ("limit", "40")]).json() or []:
                pr = m.get("outcomePrices")
                pr = json.loads(pr) if isinstance(pr, str) else pr
                if pr and float(pr[0]) >= 0.999:
                    c[str(m["id"])] = "YES"
                elif pr and float(pr[1]) >= 0.999:
                    c[str(m["id"])] = "NO"
        except Exception as e:
            print(f"  desenlaces lote {k // 40}: {type(e).__name__}", file=sys.stderr)
    if pend:
        CACHE.write_text(json.dumps(c))
    return c


def alarmas(bin_t, bin_m, t_ini, t_fin, umbral_bps, ventana_ms):
    """Instantes (recepción) en que Binance se movió >= umbral en la ventana: lista de (t, +1 sube / -1 baja)."""
    out = []
    i0 = bisect.bisect_left(bin_t, t_ini - ventana_ms)
    j = i0
    for i in range(bisect.bisect_left(bin_t, t_ini), bisect.bisect_right(bin_t, t_fin)):
        while bin_t[j] < bin_t[i] - ventana_ms:
            j += 1
        ref = bin_m[j]
        if ref > 0:
            mov = (bin_m[i] / ref - 1) * 1e4
            if abs(mov) >= umbral_bps:
                out.append((bin_t[i], 1 if mov > 0 else -1))
    return out


def simular_token(libro, trades, t_ini, t_fin, cancela, lat_ms, enfr_ms):
    """Bids en el mejor bid de un token. cancela: lista ordenada de instantes de recepción que amenazan a este token.
    -> (acciones, coste)."""
    sh_tot, coste = 0.0, 0.0
    ia = 0
    bloqueado_hasta = -1
    cotiz = None                       # (precio, cola_delante, vol_a_precio, t_desde, t_cancel_efectiva)
    lt = [x[0] for x in libro]
    it = bisect.bisect_left([x[0] for x in trades], t_ini)
    ih = bisect.bisect_left(lt, t_ini)
    eventos = []
    for x in libro[ih:]:
        if x[0] > t_fin:
            break
        eventos.append((x[0], 0, x))
    for x in trades[it:]:
        if x[0] > t_fin:
            break
        eventos.append((x[0], 1, x))
    for tc in cancela:
        eventos.append((tc + lat_ms, 2, tc))
    eventos.sort(key=lambda e: (e[0], e[1]))
    for t, tipo, x in eventos:
        if tipo == 2:                                  # la cancelación surte efecto
            cotiz = None
            bloqueado_hasta = max(bloqueado_hasta, t + enfr_ms)
            continue
        if tipo == 0:                                  # nuevo top: (re)cotizar en el mejor bid si no hay cotización
            _, bb, _ba, bsz = x
            if cotiz is None and t >= bloqueado_hasta and bb and P_MIN <= bb <= P_MAX and sh_tot < MAX_SH:
                cotiz = [bb, bsz, 0.0]
            elif cotiz is not None and bb and bb > cotiz[0]:
                cotiz = [bb, bsz, 0.0] if t >= bloqueado_hasta else None   # el mejor bid subió: nos movemos
            continue
        if cotiz is None:                              # operación
            continue
        _, p, _side, sz = x
        # sin filtrar por `side`: una compra de NO puede casar contra un bid de YES (acuñación) y el campo no dice
        # quién consumió el bid. Una operación a precio <= nuestro bid solo puede consumir bids de ese nivel (si el
        # ask hubiera llegado ahí, nuestra orden habría cruzado), así que basta el precio.
        lleno = False
        if p < cotiz[0] - 1e-9:
            lleno = True
        elif abs(p - cotiz[0]) < 1e-9:
            cotiz[2] += sz
            lleno = cotiz[2] > cotiz[1]
        if lleno:
            q = min(SH, MAX_SH - sh_tot)
            sh_tot += q
            coste += q * cotiz[0]
            cotiz = None if sh_tot >= MAX_SH else [cotiz[0], 0.0, 0.0]
    return sh_tot, coste


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--desde", required=True)
    ap.add_argument("--hasta")
    ap.add_argument("--marco", default=None)
    ap.add_argument("--parar-s", type=int, default=10, help="deja de cotizar N s antes del cierre")
    a = ap.parse_args()
    import datetime as dt
    d0 = dt.date.fromisoformat(a.desde)
    d1 = dt.date.fromisoformat(a.hasta) if a.hasta else d0
    dias = [(d0 + dt.timedelta(days=i)).isoformat() for i in range((d1 - d0).days + 1)]
    meta, libro, trades, binance = leer(dias)
    mercados = collections.defaultdict(dict)   # mid -> {lado: token}
    info = {}
    for tk, (act, marco, mid, fin, lado) in meta.items():
        if a.marco and marco != a.marco:
            continue
        if marco not in ("5min", "15min"):
            continue
        mercados[mid][lado] = tk
        info[mid] = (act, marco, fin)
    des = desenlaces(list(mercados))
    con = [m for m in mercados if m in des and len(mercados[m]) == 2]
    print(f"días {dias}: mercados {len(mercados)}, con desenlace oficial y 2 lados {len(con)} "
          f"({len(con) / max(1, len(mercados)):.0%})")
    configs = [("SIN cancelar", None, None, 0)]
    for umbral in (1.0, 2.0):
        for lat in (100, 150, 200, 250):
            configs.append((f"cancela {umbral:g}bps/1s lat {lat}ms", umbral, lat, 2000))
    for nombre, umbral, lat, enfr in configs:
        por_mercado = []
        for mid in con:
            act, marco, fin = info[mid]
            try:
                t_fin = int(dt.datetime.fromisoformat(fin).timestamp() * 1000)
            except ValueError:
                continue
            dur = 300000 if marco == "5min" else 900000
            t_ini, t_stop = t_fin - dur, t_fin - a.parar_s * 1000
            sym = SIMBOLO.get(act)
            if sym not in binance:
                continue
            alarm = alarmas(*binance[sym], t_ini, t_stop, umbral, 1000) if umbral else []
            pnl, sh_y, sh_n = 0.0, 0.0, 0.0
            for lado, tk in mercados[mid].items():
                amenaza = -1 if lado == "YES" else 1           # baja Binance amenaza YES; sube amenaza NO
                canc = [t for t, s in alarm if s == amenaza]
                sh, coste = simular_token(libro.get(tk, []), trades.get(tk, []), t_ini, t_stop, canc, lat or 0, enfr)
                pago = sh * (1.0 if des[mid] == lado else 0.0)
                pnl += pago - coste
                if lado == "YES":
                    sh_y = sh
                else:
                    sh_n = sh
            if sh_y or sh_n:
                por_mercado.append((dt.datetime.fromtimestamp(t_fin / 1000, dt.timezone.utc).date().isoformat(),
                                    act, marco, pnl, sh_y, sh_n))
        resumen(nombre, por_mercado)


def resumen(nombre, filas):
    if not filas:
        print(f"{nombre:34} sin rellenos")
        return
    pnl = [f[3] for f in filas]
    por_dia = collections.defaultdict(list)
    for f in filas:
        por_dia[f[0]].append(f[3])
    pares = sum(1 for f in filas if f[4] and f[5])
    ic = None
    if len(por_dia) >= 3:
        rng, ms, ks = random.Random(7), [], list(por_dia)
        for _ in range(2000):
            v = [x for k in (rng.choice(ks) for _ in ks) for x in por_dia[k]]
            ms.append(sum(v) / len(v))
        ms.sort()
        ic = (round(ms[100], 3), round(ms[1899], 3))
    print(f"{nombre:34} mercados={len(filas):5} con par={pares / len(filas):.0%} PnL/mercado={sum(pnl) / len(pnl):+.3f}$ "
          f"total={sum(pnl):+.1f}$ días={len(por_dia)} IC90_días={ic}")
    por = collections.defaultdict(list)
    for f in filas:
        por[(f[1], f[2])].append(f[3])
    print("    " + "  ".join(f"{k[0]}{k[1][:-3]}:{sum(v) / len(v):+.2f}(n{len(v)})" for k, v in sorted(por.items())))


if __name__ == "__main__":
    main()
