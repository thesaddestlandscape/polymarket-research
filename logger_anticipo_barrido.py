#!/usr/bin/env python3
"""logger_anticipo_barrido.py -- logger de anticipación del barrido (SPEC_LOGGER_ANTICIPAR_BARRIDO_05nov, OK Javi 05-Nov).
Solo lectura de feeds PUBLICOS (sin claves, sin órdenes). Proceso independiente (screen `logl2`), NO en observadores.

Salidas (CSV.gz diario, append; escritas en el volumen con symlink en /root/polymarket-research-datalogs; fuera de git):
  anticipo_perp_1s_D.csv.gz  rejilla de 1 s por RECEPCION y símbolo (BTC/ETH/SOL/XRP USDT-M perp): aggTrade agregado
        (n, vol_compra, vol_venta, vwap, high, low, primer/último precio), liquidaciones del segundo y OI (REST fapi).
        Filas con estado=ok solo con el WS vivo; n=0 y volúmenes 0 son ceros EXPLICITOS; con n=0 los campos de precio
        (vwap, high, low, primero, ultimo) van VACIOS (05-Nov: antes repetían el último precio y parecían datos).
        oi vacío y oi_recv_ms vacío si aún no hay lectura de OI (antes 0). ts_s = segundo de RECEPCION; la fila se emite
        0-274 ms después de cerrarlo: unir con t >= ts_emision_ms, nunca por ts_s <= t//1000 (hasta 1 s de futuro).
        Silencio del socket >2 s -> NO se escriben segundos (missing != 0); al volver, fila estado=gap con
        sym='*', ts_s=inicio y n=segundos perdidos. OJO: un REINICIO del proceso NO deja fila gap (el estado no se
        persiste): detectar huecos SIEMPRE por continuidad de ts_s.
  anticipo_liq_D.csv.gz      un evento forceOrder por fila (hora de evento T del exchange y de recepción en ms).
L2 de Polymarket 5m: NO se duplica; ya lo graba libro5_ms (libro_estado_ws, feed crudo B/d/T con recepción y seq,
volumen /mnt/.../libro5_ms). Uso offline: unir por ms de recepción.
Retención 21 d (propia, al arrancar y al cambiar de día). Reinicio: append; el hueco del reinicio NO queda marcado (ver arriba): continuidad de ts_s.
"""
import asyncio
import glob
import gzip
import json
import os
import sys
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import websockets

VOL = Path("/mnt/HC_Volume_106538179/datalogs_auto")
LINK = Path("/root/polymarket-research-datalogs")
RETENCION_DIAS = 21
SIMB = {"BTCUSDT": "BTC", "ETHUSDT": "ETH", "SOLUSDT": "SOL", "XRPUSDT": "XRP"}
# Ruta /market/ (la antigua /stream da timeout desde esta IP, verificado 05-Nov)
WS_URL = "wss://fstream.binance.com/market/stream?streams=" + "/".join(
    [f"{s.lower()}@aggTrade" for s in SIMB] + [f"{s.lower()}@forceOrder" for s in SIMB])
FAPI_OI = "https://fapi.binance.com/fapi/v1/openInterest?symbol="
SILENCIO_MS = 2000
H_PERP = ("ts_s,sym,estado,n,vol_compra,vol_venta,vwap,high,low,primero,ultimo,liq_n,liq_qty_compra,liq_qty_venta,"
          "oi,oi_recv_ms,ts_emision_ms\n")
H_LIQ = "T_ms,recv_ms,sym,lado,precio,qty,precio_prom,estado\n"

agg = {}        # (sec, sym) -> [n, vb, vs, pv, hi, lo, first, last, liqn, liqb, liqs]
ultimo_px = {}  # sym -> último precio
oi = {s: (0.0, 0) for s in SIMB.values()}
estado = {"last_msg": 0, "conectado": False, "n_msg": 0, "n_filas": 0, "n_liq": 0, "gap_ini": None}
_abiertos = {}


def _log(m):
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {m}", flush=True)


def _fichero(prefijo, dia, cabecera):
    clave = (prefijo, dia)
    f = _abiertos.get(clave)
    if f:
        return f
    for k in [k for k in _abiertos if k[0] == prefijo]:      # cambio de día: cierre limpio del anterior
        _abiertos.pop(k).close()
    nombre = f"{prefijo}_{dia}.csv.gz"
    ruta = VOL / nombre
    nuevo = not ruta.exists() or ruta.stat().st_size == 0
    f = gzip.open(ruta, "at", encoding="utf-8")
    if nuevo:
        f.write(cabecera)
    enlace = LINK / nombre
    if not enlace.is_symlink() and not enlace.exists():
        enlace.symlink_to(ruta)
    _abiertos[clave] = f
    _retencion()
    return f


def _retencion():
    lim = time.time() - RETENCION_DIAS * 86400
    for pat in ("anticipo_perp_1s_*.csv.gz", "anticipo_liq_*.csv.gz"):
        for r in glob.glob(str(VOL / pat)):
            try:
                if os.path.getmtime(r) < lim:
                    os.remove(r)
                    l = LINK / os.path.basename(r)
                    if l.is_symlink():
                        l.unlink()
                    _log(f"retención: borrado {r}")
            except OSError:
                pass


def _dia(ms):
    return datetime.fromtimestamp(ms / 1000, timezone.utc).strftime("%Y-%m-%d")


def _msg(raw, recv):
    d = json.loads(raw).get("data") or {}
    s = SIMB.get(d.get("s") or (d.get("o") or {}).get("s"))
    if not s:
        return
    if d.get("e") == "aggTrade":
        p, q = float(d["p"]), float(d["q"])
        if p <= 0 or q < 0:
            return
        a = agg.setdefault((recv // 1000, s), [0, 0.0, 0.0, 0.0, p, p, p, p, 0, 0.0, 0.0])
        a[0] += 1
        # m=True: comprador es maker -> agresor VENDEDOR
        a[2 if d.get("m") else 1] += q
        a[3] += p * q
        a[4] = max(a[4], p); a[5] = min(a[5], p); a[7] = p
        ultimo_px[s] = p
    elif d.get("e") == "forceOrder":
        o = d["o"]
        p, q = float(o["p"]), float(o["q"])
        ap = float(o.get("ap") or 0)
        f = _fichero("anticipo_liq", _dia(recv), H_LIQ)
        f.write(f"{o['T']},{recv},{s},{o['S']},{p},{q},{ap},ok\n")
        a = agg.setdefault((recv // 1000, s), [0, 0.0, 0.0, 0.0, ultimo_px.get(s, p), ultimo_px.get(s, p),
                                               ultimo_px.get(s, p), ultimo_px.get(s, p), 0, 0.0, 0.0])
        a[8] += 1
        a[9 if o["S"] == "BUY" else 10] += q
        estado["n_liq"] += 1


def _emitir(hasta_sec, desde_sec):
    """Escribe los segundos cerrados [desde_sec, hasta_sec). Vivo = último mensaje a <=2 s del final del segundo."""
    ahora = int(time.time() * 1000)
    for sec in range(desde_sec, hasta_sec):
        vivo = estado["conectado"] and (min(ahora, (sec + 1) * 1000) - estado["last_msg"]) <= SILENCIO_MS \
            and estado["last_msg"] >= sec * 1000 - SILENCIO_MS
        if not vivo:
            if estado["gap_ini"] is None:
                estado["gap_ini"] = sec
            for s in SIMB.values():
                agg.pop((sec, s), None)
            continue
        f = _fichero("anticipo_perp_1s", _dia(sec * 1000), H_PERP)
        if estado["gap_ini"] is not None:
            f.write(f"{estado['gap_ini']},*,gap,{sec - estado['gap_ini']},0,0,0,0,0,0,0,0,0,0,0,0,{ahora}\n")
            estado["gap_ini"] = None
        for s in SIMB.values():
            a = agg.pop((sec, s), None)
            lp = ultimo_px.get(s, 0.0)
            if a is None:
                a = [0, 0.0, 0.0, 0.0, lp, lp, lp, lp, 0, 0.0, 0.0]
            vol = a[1] + a[2]
            if a[0] > 0:
                px = f"{(a[3] / vol if vol > 0 else lp):.8g},{a[4]:.8g},{a[5]:.8g},{a[6]:.8g},{a[7]:.8g}"
            else:
                px = ",,,,"          # n=0: sin precio propio del segundo (no repetir el último)
            oi_txt = f"{oi[s][0]:.6g},{oi[s][1]}" if oi[s][1] else ","
            f.write(f"{sec},{s},ok,{a[0]},{a[1]:.6g},{a[2]:.6g},{px},"
                    f"{a[8]},{a[9]:.6g},{a[10]:.6g},{oi_txt},{ahora}\n")
            estado["n_filas"] += 1


def _flush():
    for f in _abiertos.values():
        try:
            f.flush()
        except Exception as e:
            _log(f"flush: {e}")


async def _emisor():
    desde = int(time.time())
    while True:
        await asyncio.sleep(0.25)
        cur = int(time.time())
        if cur > desde:
            _emitir(cur, desde)
            desde = cur
        if cur % 10 == 0:
            _flush()


def _get_oi(sym):
    with urllib.request.urlopen(FAPI_OI + sym, timeout=3) as r:
        return float(json.loads(r.read())["openInterest"])


async def _poll_oi():
    loop = asyncio.get_running_loop()
    while True:
        t0 = time.time()
        for sym, s in SIMB.items():
            try:
                v = await loop.run_in_executor(None, _get_oi, sym)
                oi[s] = (v, int(time.time() * 1000))
            except Exception:
                pass          # OI antiguo: oi_recv_ms delata su edad
        await asyncio.sleep(max(0.0, 1.0 - (time.time() - t0)))


async def _ws():
    while True:
        try:
            async with websockets.connect(WS_URL, ping_interval=20, ping_timeout=20, max_queue=4096) as ws:
                estado["conectado"] = True
                estado["last_msg"] = int(time.time() * 1000)
                _log("conectado a fstream")
                while True:
                    raw = await asyncio.wait_for(ws.recv(), 10)
                    recv = int(time.time() * 1000)
                    estado["last_msg"] = recv
                    estado["n_msg"] += 1
                    try:
                        _msg(raw, recv)
                    except (ValueError, KeyError, TypeError):
                        continue
        except Exception as e:
            estado["conectado"] = False
            _log(f"conexión perdida ({type(e).__name__}: {e}); reconecta en 3 s")
            await asyncio.sleep(3)


async def _latido():
    while True:
        await asyncio.sleep(60)
        _log(f"latido msgs={estado['n_msg']} filas={estado['n_filas']} liq={estado['n_liq']} gap_ini={estado['gap_ini']}")


async def main():
    VOL.mkdir(parents=True, exist_ok=True)
    _retencion()
    _log("logger_anticipo_barrido arrancado (perp aggTrade+forceOrder+OI, rejilla 1 s)")
    await asyncio.gather(_ws(), _emisor(), _poll_oi(), _latido())


if __name__ == "__main__":
    try:
        asyncio.run(main())
    finally:
        for f in _abiertos.values():
            try:
                f.close()
            except Exception:
                pass
