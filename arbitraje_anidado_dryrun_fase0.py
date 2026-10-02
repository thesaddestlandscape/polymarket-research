#!/usr/bin/env python3
"""arbitraje_anidado_dryrun_fase0.py -- DRY-RUN, NUNCA envía órdenes (02-Oct, Javi: "ok, guarda y dale a todo").

Origen: project_alpha_precierre_naive_02oct (ronda 2) + project_propuestas_pendientes_proxima_sesion_02oct (#1, #2).
El tramo corto (5m) cierra en el mismo instante y con el mismo TWAP60 de Chainlink que el largo (15m/4h); solo cambia
la referencia de apertura. Si ref_largo < ref_corto: Up_largo + Down_corto paga >= 1 SIEMPRE (2 si el cierre cae
entre las dos referencias). Simétrico con Down_largo + Up_corto si ref_largo > ref_corto. Garantía verificada con
desenlace oficial en 26.138/26.138 filas. Hay beneficio sin riesgo cuando
    neto = 1 - ask_A - ask_B - fee(ask_A) - fee(ask_B) > 0,   fee(p) = 0,07 * p * (1 - p) por share (crypto_fees_v2)
(umbral por fee REAL, no un margen fijo: cerca de 0/1 la fee ~0 y 1c ya es beneficio).

Qué hace: cada CADA_S, en el último tramo corto de cada ventana larga, para cada moneda y par (5m>15m, 5m>4h, 15m>4h)
lee los dos tops del libro en el mismo instante (libro_estado_ws, O(1)). Si neto >= NETO_MIN abre un evento (como
mucho uno por segundo y par/moneda/cierre), y LECTURA_S después simula dos órdenes FOK simultáneas al precio
detectado con latencia L en LATENCIAS_S, contra el histórico ms del libro en t+L:
  pata llena si ask(t+L) < límite, o == límite con tamaño >= shares.  -> "ambas" / "solo_A" / "solo_B" / "ninguna".
  Además el neto si se tomara el top en t+L sin límite (re-precio).
Referencias con la ventana oficial [ini-62, ini-3] (valor_relativo_anidado_fase0._ref, mismo código) y |gap| >= 1 bps.
El legging (una pata llena, la otra no) queda expuesto y se valora después con el desenlace oficial.
-> /root/polymarket-research-datalogs/arbitraje_anidado_dryrun_YYYY-MM-DD.csv (gz al día siguiente, RETENCION_DIAS).
Paso a live SOLO si captura >0 neto con n>=40 eventos: pase de casos límite + /code-review + OK de Javi.
"""
import csv
import gzip
import shutil
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

import libro_estado_ws as LE
from resolution_sniper_observer import ASSETS, mercado_slot, token_ids
from valor_relativo_anidado_fase0 import GAP_MIN_BPS, PARES, _ref

DATALOGS = Path("/root/polymarket-research-datalogs")
PREFIJO = "arbitraje_anidado_dryrun"
RETENCION_DIAS = 30
FEE = 0.07
CADA_S = 0.05
NETO_MIN = 0.0005
LATENCIAS_S = [0.15, 0.4, 0.6, 1.0]
LECTURA_S = 1.2
MAX_SHARES, MIN_SHARES = 200.0, 5.0
FIN_MARGEN_S = 3
CAMPOS = (["ts_ms", "par", "activo", "fin", "resto_s", "market_largo", "market_corto", "ref_largo", "ref_corto",
           "gap_bps", "pata_A", "pata_B", "ask_A", "size_A", "edad_A_ms", "ask_B", "size_B", "edad_B_ms", "coste",
           "neto", "shares", "beneficio_usd"]
          + [f"{c}_{int(L * 1000)}" for L in LATENCIAS_S for c in ("fill", "neto_top")])
_lock = threading.Lock()


def _log(msg):
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def fee(p):
    return FEE * p * (1 - p)


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


def _llena(e, limite, shares):
    if not e or e["best_ask"] is None:
        return False
    if e["best_ask"] < limite - 1e-9:
        return True
    return abs(e["best_ask"] - limite) < 1e-9 and (e["ask_size"] or 0) >= shares


def _simular(fila, tok_a, tok_b):
    """Corre en un hilo aparte LECTURA_S después de la detección: lee el histórico ms del libro en t+L."""
    try:
        time.sleep(max(0.0, fila["ts_ms"] / 1000 + LECTURA_S - time.time()))
        for L in LATENCIAS_S:
            t = fila["ts_ms"] + int(L * 1000)
            ea, eb = LE.en(tok_a, t), LE.en(tok_b, t)
            fa, fb = _llena(ea, fila["ask_A"], fila["shares"]), _llena(eb, fila["ask_B"], fila["shares"])
            fila[f"fill_{int(L * 1000)}"] = "ambas" if fa and fb else "solo_A" if fa else "solo_B" if fb else "ninguna"
            if ea and eb and ea["best_ask"] and eb["best_ask"]:
                a, b = ea["best_ask"], eb["best_ask"]
                fila[f"neto_top_{int(L * 1000)}"] = round(1 - a - b - fee(a) - fee(b), 5)
        _escribir(fila)
    except Exception as e:
        _log(f"🚨 simulación falló: {type(e).__name__}: {e}")


def main():
    LE.iniciar(("5min", "15min"))
    _log(f"arbitraje_anidado_dryrun_fase0 arrancado (NETO_MIN {NETO_MIN}, latencias {LATENCIAS_S}, DRY-RUN sin órdenes)")
    refs, toks, ult_ev, t_mant, n_ev = {}, {}, {}, 0.0, 0
    while True:
        try:
            ahora = time.time()
            if ahora - t_mant > 3600:
                t_mant = ahora
                _mantenimiento()
                _log(f"{n_ev} eventos en la última hora")
                n_ev = 0
            for corto, d_corto, largo, d_largo in PARES:
                ini_l = int(ahora // d_largo) * d_largo
                fin = ini_l + d_largo
                ini_c = fin - d_corto
                if not (ini_c + 5 <= ahora <= fin - FIN_MARGEN_S):
                    continue
                par = f"{corto}>{largo}"
                for activo in ASSETS:
                    k = (par, fin, activo)
                    if k not in refs:
                        r_l, r_c = _ref(activo, ini_l), _ref(activo, ini_c)
                        if r_l is None or r_c is None:
                            continue
                        refs[k] = (r_l, r_c)
                    r_l, r_c = refs[k]
                    gap = (r_c / r_l - 1) * 1e4
                    if abs(gap) < GAP_MIN_BPS:
                        continue
                    if k not in toks:
                        _, ml = mercado_slot(activo, largo, ini_l)
                        _, mc = mercado_slot(activo, corto, ini_c)
                        if not ml or not mc:
                            continue
                        (yl, nl), (yc, nc) = token_ids(ml), token_ids(mc)
                        # ref_largo < ref_corto  =>  Up_largo + Down_corto ;  al revés  =>  Down_largo + Up_corto
                        a, b = (yl, nc) if gap > 0 else (nl, yc)
                        toks[k] = (a, b, ml.get("id", ""), mc.get("id", ""), "Up_largo" if gap > 0 else "Down_largo",
                                   "Down_corto" if gap > 0 else "Up_corto")
                        LE.pedir([t for t in (a, b) if t], ttl_s=d_corto + 120)
                    tok_a, tok_b, id_l, id_c, pa, pb = toks[k]
                    ua, ub = LE.ultimo(tok_a), LE.ultimo(tok_b)
                    if not ua or not ub or ua[3] is None or ub[3] is None:
                        continue
                    a, b = ua[3], ub[3]
                    neto = 1 - a - b - fee(a) - fee(b)
                    if neto < NETO_MIN or ahora - ult_ev.get(k, 0) < 1.0:
                        continue
                    ult_ev[k] = ahora
                    n_ev += 1
                    ahora_ms = int(time.time() * 1000)
                    shares = min(ua[4] or 0, ub[4] or 0, MAX_SHARES)
                    fila = {"ts_ms": ahora_ms, "par": par, "activo": activo, "fin": fin, "resto_s": round(fin - ahora, 2),
                            "market_largo": id_l, "market_corto": id_c, "ref_largo": r_l, "ref_corto": r_c,
                            "gap_bps": round(gap, 2), "pata_A": pa, "pata_B": pb, "ask_A": a, "size_A": ua[4],
                            "edad_A_ms": ahora_ms - ua[0], "ask_B": b, "size_B": ub[4], "edad_B_ms": ahora_ms - ub[0],
                            "coste": round(a + b, 4), "neto": round(neto, 5), "shares": shares,
                            "beneficio_usd": round(neto * shares, 4) if shares >= MIN_SHARES else 0.0}
                    threading.Thread(target=_simular, args=(fila, tok_a, tok_b), daemon=True).start()
            if len(refs) > 500:
                for d in (refs, toks, ult_ev):
                    for kk in [kk for kk in d if kk[1] < ahora - 3600]:
                        d.pop(kk, None)
        except Exception as e:
            _log(f"🚨 error en ciclo: {type(e).__name__}: {e}")
            time.sleep(2)
        time.sleep(CADA_S)


if __name__ == "__main__":
    from resolution_sniper_observer import _TAIL
    _TAIL.arrancar()
    time.sleep(8)
    main()
