#!/usr/bin/env python3
"""valor_relativo_anidado_fase0.py -- FASE 0, SOLO OBSERVACIÓN (hilo de observadores_fase0.py). 30-Sep.

Idea: el último tramo de 5 min de cada ventana de 15 min cierra en el mismo instante y con el mismo precio de cierre;
solo cambia la referencia de apertura. Si ref15 < ref5, "Up en 5 min" IMPLICA "Up en 15 min", así que el Up de 15 min
no puede valer menos que el Up de 5 min (simétrico con Down si ref15 > ref5). El mercado de 5 min es el eficiente
(ninguna zona con edge al ask real); el de 15 min es donde han salido todas las pistas. Aquí se usa el de 5 min como
precio justo del de 15 min y se compra UNA pata, la barata (no es el arbitraje anidado de dos patas, refutado).

Retrospectivo con fotos de 1-2 min (analisis_valor_relativo_5m_15m.py, 10-30 Sep): la implicación se cumple en el
99,7 % de 10.284 pares y comprar cuando bid(5m) - ask(15m) >= 3c da EV +0,05 por € (n=352, IC90 (-0,10,+0,19),
13/21 días): prometedor pero sin demostrar, porque las dos fotos distaban hasta 20 s. Este observador lo mide con
los dos libros en el MISMO milisegundo (libro_estado_ws, top de libro O(1)).

Pares medidos (PARES): 5m>15m, 5m>4h y 15m>4h; las columnas "15"/"5" son el tramo LARGO y el CORTO del par.
Cada CADA_S, en el último tramo corto de cada ventana larga y para cada moneda, registra:
  - una fila base cada BASE_S (para conocer la distribución del margen), y
  - una fila de evento (como mucho una por segundo) mientras margen = bid5(lado) - ask15(lado) >= MARGEN_EVENTO,
con tamaños, antigüedad de cada top, referencias, y también la pata inversa (lado contrario: bid15 - ask5).
Salida: /root/polymarket-research-datalogs/valor_relativo_anidado_v2_YYYY-MM-DD.csv (gz al día siguiente, 21 días).
NO envía ni simula órdenes. El desenlace se cruza después con resolution_sniper_obs.
"""
import csv
import gzip
import os
import shutil
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

import libro_estado_ws as LE
from resolution_sniper_observer import ASSETS, _TAIL, mercado_slot, token_ids

DATALOGS = Path("/root/polymarket-research-datalogs")
CADA_S, BASE_S, MARGEN_EVENTO, GAP_MIN_BPS = 0.25, 10.0, 0.02, 1.0
RETENCION_DIAS = 21
# (corto, segundos, largo, segundos): el corto es el último tramo del largo y cierran a la vez. 30-Sep: añadidos los
# pares con 4 h (misma regla TWAP de Chainlink; los de 60 min NO entran: resuelven con la vela 1H de Binance).
PARES = [("5m", 300, "15m", 900), ("5m", 300, "4h", 14400), ("15m", 900, "4h", 14400)]
PREFIJO = "valor_relativo_anidado_v2"
TWAP_N_MIN = 20
CAMPOS = ["ts_ms", "tipo", "par", "activo", "fin", "resto_s", "market15", "market5", "ref15", "ref5", "gap_bps", "lado",
          "ask15", "ask15_size", "edad15_ms", "bid5", "bid5_size", "edad5_ms", "margen",
          "bid15", "ask5", "inv_ask5", "inv_ask5_size", "inv_bid15", "inv_margen"]
_lock = threading.Lock()


def _log(msg):
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _ref(activo, ini):
    with _TAIL._lock:
        dq = list(_TAIL._buf_oracle.get(activo, ()))
    # 02-Oct: ventana OFICIAL del twap60 de apertura = [ini-62, ini-3] (antes [ini-60, ini]).
    v = [p for t, p in dq if ini - 62 <= t <= ini - 3 and p > 0]
    return (sum(v) / len(v)) if len(v) >= TWAP_N_MIN else None


def _escribir(fila):
    ruta = DATALOGS / f"{PREFIJO}_{datetime.now(timezone.utc):%Y-%m-%d}.csv"
    with _lock:
        nuevo = not ruta.exists()
        with open(ruta, "a", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=CAMPOS)
            if nuevo:
                w.writeheader()
            w.writerow(fila)


def _mantenimiento():
    hoy = f"{datetime.now(timezone.utc):%Y-%m-%d}"
    for f in DATALOGS.glob(f"{PREFIJO}_*.csv"):
        if hoy not in f.name:
            with open(f, "rb") as a, gzip.open(str(f) + ".gz", "wb") as b:
                shutil.copyfileobj(a, b)
            f.unlink()
    for f in DATALOGS.glob(f"{PREFIJO}_*.csv.gz"):
        if time.time() - f.stat().st_mtime > RETENCION_DIAS * 86400:
            f.unlink()


def _top(tok):
    u = LE.ultimo(tok) if tok else None
    return u if u else (None, None, None, None, None)


def main():
    LE.iniciar(("5min", "15min"))
    _log("valor_relativo_anidado_fase0 arrancado (solo observación)")
    refs, toks, ult_base, ult_ev, t_mant = {}, {}, {}, {}, 0.0
    while True:
        try:
            ahora = time.time()
            if ahora - t_mant > 3600:
                t_mant = ahora
                _mantenimiento()
            for corto, d_corto, largo, d_largo in PARES:
                ini_l = int(ahora // d_largo) * d_largo
                fin = ini_l + d_largo
                ini_c = fin - d_corto
                if not (ini_c + 5 <= ahora <= fin - 8):
                    continue
                par = f"{corto}>{largo}"
                for activo in ASSETS:
                    k = (par, fin, activo)
                    if k not in refs:
                        r_l, r_c = _ref(activo, ini_l), _ref(activo, ini_c)
                        if r_l is None or r_c is None:
                            continue
                        refs[k] = (r_l, r_c)
                    r15, r5 = refs[k]                       # r15 = referencia del largo, r5 = del corto
                    gap = (r5 / r15 - 1) * 1e4
                    if abs(gap) < GAP_MIN_BPS:
                        continue
                    if k not in toks:
                        _, m15 = mercado_slot(activo, largo, ini_l)
                        _, m5 = mercado_slot(activo, corto, ini_c)
                        if not m15 or not m5:
                            continue
                        toks[k] = (token_ids(m15), token_ids(m5), m15.get("id", ""), m5.get("id", ""))
                        if largo == "4h":                   # el universo del WS no trae 4 h: se piden a demanda
                            LE.pedir([t for t in toks[k][0] if t], ttl_s=d_corto + 120)
                    (y15, n15), (y5, n5), id15, id5 = toks[k]
                    up = gap > 0                            # ref_largo < ref_corto: Up corto => Up largo ; al revés con Down
                    t15, b15, _, a15, a15s = _top(y15 if up else n15)
                    t5, b5, b5s, a5, _ = _top(y5 if up else n5)
                    _, ib15, _, _, _ = _top(n15 if up else y15)     # pata inversa (contrarrecíproco)
                    _, _, _, ia5, ia5s = _top(n5 if up else y5)
                    margen = round(b5 - a15, 4) if a15 and b5 else None
                    inv = round(ib15 - ia5, 4) if ib15 and ia5 else None
                    ahora_ms = int(time.time() * 1000)
                    # 02-Oct: además del margen fijo, evento si el par de dos patas deja neto >0 con la fee REAL
                    # (0,07*p*(1-p) por share; cerca de 0/1 la fee ~0). ask de la pata corta contraria = 1 - bid5.
                    neto = (1 - a15 - (1 - b5) - 0.07 * a15 * (1 - a15) - 0.07 * b5 * (1 - b5)) if a15 and b5 else None
                    evento = ((margen is not None and margen >= MARGEN_EVENTO) or (inv is not None and inv >= MARGEN_EVENTO)
                              or (neto is not None and neto > 0))
                    if evento and ahora - ult_ev.get(k, 0) >= 1.0:
                        ult_ev[k] = ahora
                        tipo = "evento"
                    elif ahora - ult_base.get(k, 0) >= BASE_S:
                        ult_base[k] = ahora
                        tipo = "base"
                    else:
                        continue
                    _escribir({"ts_ms": ahora_ms, "tipo": tipo, "par": par, "activo": activo, "fin": fin,
                               "resto_s": round(fin - ahora, 2), "market15": id15, "market5": id5, "ref15": r15, "ref5": r5,
                               "gap_bps": round(gap, 2), "lado": "Up" if up else "Down", "ask15": a15, "ask15_size": a15s,
                               "edad15_ms": ahora_ms - t15 if t15 else "", "bid5": b5, "bid5_size": b5s,
                               "edad5_ms": ahora_ms - t5 if t5 else "", "margen": margen, "bid15": b15, "ask5": a5,
                               "inv_ask5": ia5, "inv_ask5_size": ia5s, "inv_bid15": ib15, "inv_margen": inv})
            if len(refs) > 500:
                for d in (refs, toks, ult_base, ult_ev):
                    for kk in [kk for kk in d if kk[1] < ahora - 3600]:
                        d.pop(kk, None)
        except Exception as e:
            _log(f"🚨 error en ciclo: {type(e).__name__}: {e}")
            time.sleep(2)
        time.sleep(CADA_S)


if __name__ == "__main__":
    _TAIL.arrancar()
    time.sleep(8)
    main()
