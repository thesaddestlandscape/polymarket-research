#!/usr/bin/env python3
"""binance_jump_cruzado_fase0.py -- salto de Binance -> libros de OTRAS monedas y de marcos LARGOS (1 h / 4 h).
FASE 0, SOLO OBSERVACIÓN, nunca envía órdenes (30-Sep noche, Javi: "8 - amplía el observador", "9 - lo mismo").

Hipótesis (programa cripto10, datalogs analisis_persistente_30sep/cripto10_30sep/HIPOTESIS_Y_DISENO.md):
  #8  tras un salto de BTC (u otra moneda), los libros de las DEMÁS monedas se recotizan más tarde que el de la
      moneda que salta (sus creadores de mercado miran su propio subyacente);
  #9  los mercados de 1 h y 4 h se recotizan más tarde que los de 5/15 min.
binance_jump_leadlag_fase0 solo leía (por REST) los 5m/15m de la moneda que salta. Este módulo lee, en los MISMOS
offsets (0 / 0,3 / 0,6 / 1 / 2 / 4 s), los mercados vigentes 5m/15m de las 6 monedas, 60min de BTC/ETH/SOL (los que
trae el universo) y 4h de las 6 monedas, del lado del salto.

Por qué por WebSocket y no por REST: 20+ mercados x 6 lecturas por salto multiplicarían las peticiones al CLOB y
podrían provocar 429 al ejecutor real de PRECIERRE, que lee su libro por REST en el mismo servidor. Aquí todo sale
de libro_estado_ws (libro en memoria del mismo proceso): cero peticiones al CLOB por salto. Coste: `edad_libro_ms`
(tiempo desde la última actualización del libro) se registra para no confundir un libro quieto con uno sin datos.
La moneda que salta también se registra (fuente ws) para calibrar ws frente al REST del observador original.

Se llama desde binance_jump_leadlag_fase0._evento dentro de try/except: un fallo aquí nunca afecta al original.
Salida: /root/polymarket-research-datalogs/binance_jump_cruzado_YYYY-MM-DD.csv.gz (gz diario, retención 21 días,
fuera de git; ~8-10 MB/día estimados).
"""
import csv
import gzip
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

DATALOGS = Path("/root/polymarket-research-datalogs")
RETENCION_DIAS = 21
ACTIVOS = ("BTC", "ETH", "SOL", "XRP", "DOGE", "BNB")
OFFSETS_S = (0.0, 0.3, 0.6, 1.0, 2.0, 4.0)
COLS = ["ts_evento", "activo_salto", "ret_1s_salto", "activo", "ret_1s_propio", "marco", "market", "resto_s",
        "direccion", "offset_s", "t_real_s", "ask", "ask_size", "bid", "bid_size", "edad_libro_ms"]
_pool = ThreadPoolExecutor(max_workers=8, thread_name_prefix="jump_cruzado")
_lock = threading.Lock()
_mercados = {}            # (activo, marco) -> (market, fin_epoch, token_up, token_down)
_estado = {"iniciado": False, "ult_limpieza": 0.0}


def _log(msg):
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] [cruzado] {msg}", flush=True)


def _refrescar():
    """Cada 20 s: mercado vigente por (moneda, marco) y alta de sus tokens en libro_estado_ws."""
    import libro_estado_ws as LE
    import live_trade as lt
    from fetch_libro_ambos_lados import _universo_activo
    from resolution_sniper_observer import mercado_slot, token_ids
    while True:
        try:
            ahora = time.time()
            nuevo = {}
            for tag, dur in (("5m", 300), ("15m", 900), ("4h", 14400)):
                ini = int(ahora // dur) * dur
                for a in ACTIVOS:
                    slug, mkt = mercado_slot(a, tag, ini)
                    if mkt:
                        up, dn = token_ids(mkt)
                        if up and dn:
                            nuevo[(a, tag)] = (slug, ini + dur, up, dn)
            h = {}
            for mid, (a, marco, _cid, edt) in _universo_activo().items():
                if marco == "60min" and a in ACTIVOS:
                    fin = edt.timestamp()
                    if fin > ahora and (a not in h or fin < h[a][1]):
                        h[a] = (mid, fin)
            for a, (mid, fin) in h.items():
                try:
                    up, dn, _ = lt._get_token_ids(mid)
                    if up and dn:
                        nuevo[(a, "1h")] = (str(mid), fin, up, dn)
                except Exception:
                    continue
            LE.pedir([t for v in nuevo.values() for t in (v[2], v[3])], ttl_s=900)
            with _lock:
                _mercados.clear()
                _mercados.update(nuevo)
        except Exception as e:
            _log(f"refresco falló: {type(e).__name__}: {e}")
        time.sleep(20)


def _iniciar():
    if _estado["iniciado"]:
        return
    _estado["iniciado"] = True
    import libro_estado_ws as LE
    LE.iniciar(("5min", "15min", "60min"))
    threading.Thread(target=_refrescar, daemon=True, name="jump_cruzado_refresco").start()
    _log("arrancado (libros por WebSocket, cero peticiones REST por salto)")


def _limpiar():
    if time.time() - _estado["ult_limpieza"] < 3600:
        return
    _estado["ult_limpieza"] = time.time()
    corte = time.time() - RETENCION_DIAS * 86400
    for f in DATALOGS.glob("binance_jump_cruzado_*.csv.gz"):
        try:
            if f.stat().st_mtime < corte:
                f.unlink()
        except OSError:
            pass


def _muestrear(t0, activo_salto, ret, rets_propios, objetivos):
    import libro_estado_ws as LE
    filas = []
    ts = datetime.fromtimestamp(t0, timezone.utc).isoformat(timespec="milliseconds")
    for off in OFFSETS_S:
        espera = t0 + off - time.time()
        if espera > 0:
            time.sleep(espera)
        ahora_ms = int(time.time() * 1000)
        for (a, tag), (mkt, fin, tok) in objetivos.items():
            top = LE.ultimo(tok)            # (t_ms, best_bid, bid_size, best_ask, ask_size) o None
            filas.append({"ts_evento": ts, "activo_salto": activo_salto, "ret_1s_salto": round(ret, 6), "activo": a,
                          "ret_1s_propio": rets_propios.get(a), "marco": tag, "market": mkt, "resto_s": round(fin - t0, 1),
                          "direccion": "Up" if ret > 0 else "Down", "offset_s": off,
                          "t_real_s": round(time.time() - t0, 3),
                          "ask": top[3] if top else None, "ask_size": top[4] if top else None,
                          "bid": top[1] if top else None, "bid_size": top[2] if top else None,
                          "edad_libro_ms": (ahora_ms - top[0]) if top else None})
    _limpiar()
    out = DATALOGS / f"binance_jump_cruzado_{datetime.now(timezone.utc).strftime('%Y-%m-%d')}.csv.gz"
    with _lock:
        nuevo = not out.exists()
        with gzip.open(out, "at", newline="", encoding="utf-8") as f:     # miembros gzip concatenados
            w = csv.DictWriter(f, fieldnames=COLS)
            if nuevo:
                w.writeheader()
            w.writerows(filas)


def evento(activo_salto, t0, ret, rets_propios):
    """Llamado por binance_jump_leadlag_fase0 en cada salto. No bloquea: encola y vuelve."""
    _iniciar()
    with _lock:
        mk = dict(_mercados)
    arriba = ret > 0
    objetivos = {}
    for (a, tag), (mkt, fin, up, dn) in mk.items():
        if fin - t0 >= 5:
            objetivos[(a, tag)] = (mkt, fin, up if arriba else dn)
    if objetivos:
        _pool.submit(_muestrear, t0, activo_salto, ret, rets_propios, objetivos)
