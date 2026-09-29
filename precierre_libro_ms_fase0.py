#!/usr/bin/env python3
"""precierre_libro_ms_fase0.py -- FASE 0 (solo observación) del test de
"maker en reposo con requote/cancelación en ms" en el PRECIERRE (ronda1 #4,
Javi 29-Sep: "como podemos llegar a lo no llenado... pruébalo").

Resultado previo con snapshots de 10-15 s: un bid pasivo a ask-2c en T-60 solo
llena el 16 % y lo que llena acierta 71-77 % (vs 90-91 % de lo no llenado):
selección adversa. Para saber si un requote/cancelación en ms la evita hace
falta la película del libro y de las ejecuciones a resolución ms. Este
grabador vuelca, por cada mercado up/down 5m/15m (BTC/ETH/SOL/XRP), los
últimos 100 s previos al cierre y 5 s posteriores desde libro_estado_ws (WS,
histórico muestreado a 100 ms + trades last_trade_price): cambios de best
bid/ask, imbalance e impresiones de trades con timestamp ms ->
/root/polymarket-research-datalogs/precierre_libro_ms_fase0.csv (fuera de git).
La simulación (maker pegado a ask-1 tick, cancelación si el spot Binance
bookTicker se mueve en contra X bps, relleno = trade a <= mi bid) se hace a
posteriori en analisis_precierre_maker_ms.py con z de precierre_multioffset
(dirección) y binance_bookticker (ms). NO coloca órdenes.
"""
import csv
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
import libro_estado_ws as LE  # noqa: E402

DATALOGS = Path("/root/polymarket-research-datalogs")
RETENCION_DIAS = 5           # 29-Sep (Javi: "no podemos permitir" el consumo de disco, raíz al 88 %): gz diario + borrado > 5 días
_ULT_LIMPIEZA = [0.0]
ACTIVOS = {"BTC", "ETH", "SOL", "XRP"}
ANTES_S, DESPUES_S, ESPERA_S = 70, 3, 8      # ventana mínima: el precierre vive en los últimos ~60 s
COLS = ["market_id", "activo", "marco", "end_ts", "token", "tipo", "t_ms", "rel_fin_ms", "best_bid", "best_ask",
        "imb1", "imb5", "precio", "side", "size"]


def _log(msg):
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _out():
    return DATALOGS / f"precierre_libro_ms_{datetime.now(timezone.utc).strftime('%Y-%m-%d')}.csv.gz"


def _limpiar():
    """Borra ficheros > RETENCION_DIAS (una vez por hora)."""
    if time.time() - _ULT_LIMPIEZA[0] < 3600:
        return
    _ULT_LIMPIEZA[0] = time.time()
    corte = time.time() - RETENCION_DIAS * 86400
    for f in DATALOGS.glob("precierre_libro_ms_*.csv.gz"):
        try:
            if f.stat().st_mtime < corte:
                f.unlink()
                _log(f"retención: borrado {f.name}")
        except OSError:
            pass


def _volcar(mid, activo, marco, end_ts, yes, no):
    _limpiar()
    ini, fin = int((end_ts - ANTES_S) * 1000), int((end_ts + DESPUES_S) * 1000)
    filas = []
    prev = None
    for (t, bb, ba, i1, i5, i10, d5) in LE.hist_rango(yes, ini, fin):   # el libro del NO es el espejo del YES (bids<->asks a 1-p): solo se guarda el YES
        if True:
            lado = "YES"
            if (bb, ba) == prev:
                continue                       # solo cambios de mejor bid/ask
            prev = (bb, ba)
            filas.append({"market_id": mid, "activo": activo, "marco": marco, "end_ts": end_ts, "token": lado,
                          "tipo": "book", "t_ms": t, "rel_fin_ms": t - int(end_ts * 1000), "best_bid": bb, "best_ask": ba,
                          "imb1": i1, "imb5": i5})
    for lado, tk in (("YES", yes), ("NO", no)):
        for (t, p, side, size) in LE.trades(tk, ini, fin):
            if lado == "NO":                       # normaliza a precio/lado del token YES
                p, side = round(1 - p, 4), ("SELL" if side == "BUY" else "BUY")
            filas.append({"market_id": mid, "activo": activo, "marco": marco, "end_ts": end_ts, "token": lado,
                          "tipo": "trade", "t_ms": t, "rel_fin_ms": t - int(end_ts * 1000), "precio": p, "side": side,
                          "size": size})
    if filas:
        import gzip
        out = _out()
        nuevo = not out.exists()
        with gzip.open(out, "at", newline="", encoding="utf-8") as f:     # miembros gzip concatenados: legible con gzip.open/zcat
            w = csv.DictWriter(f, fieldnames=COLS)
            if nuevo:
                w.writeheader()
            w.writerows(filas)
    return len(filas)


def main():
    _log("arrancado -- película ms del libro y trades en los últimos 100 s de cada up/down 5m/15m (BTC/ETH/SOL/XRP)")
    LE.iniciar(("5min",), activos=ACTIVOS)
    LE.iniciar(("15min",))
    import live_trade as lt
    from fetch_libro_ambos_lados import _universo_activo
    pend, hechos = {}, set()      # el universo activo excluye los vencidos: guardamos el registro propio
    while True:
        try:
            ahora = time.time()
            for mid, (activo, marco, _cid, edt) in _universo_activo().items():
                if activo not in ACTIVOS or marco not in ("5min", "15min") or mid in pend or mid in hechos:
                    continue
                try:
                    yes, no, _ = lt._get_token_ids(mid)
                except Exception:
                    continue
                pend[mid] = (activo, marco, edt.timestamp() if hasattr(edt, "timestamp") else float(edt), yes, no)
            for mid in list(pend):
                activo, marco, end_ts, yes, no = pend[mid]
                if ahora >= end_ts + ESPERA_S:
                    n = _volcar(mid, activo, marco, end_ts, yes, no)
                    hechos.add(mid)
                    pend.pop(mid)
                    if n:
                        _log(f"{activo}#{marco} {mid}: {n} filas")
            if len(hechos) > 5000:
                hechos = set(list(hechos)[-2000:])
        except Exception as e:
            _log(f"WARN ciclo fallido: {type(e).__name__}: {e}")
        time.sleep(3)


if __name__ == "__main__":
    main()
