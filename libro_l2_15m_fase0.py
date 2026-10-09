#!/usr/bin/env python3
"""libro_l2_15m_fase0.py -- MISIÓN DEFINITIVA 15m §9 (07-Oct): captura de PROFUNDIDAD multinivel de los 15m cripto.
Motivo: el registro ms (libro_estado_ws) solo guarda en disco el NIVEL 1 (filas q/h); la profundidad de varios niveles
(pendiente, vacíos, muros, reposición) nunca se ha registrado -> §9 paso 2 sin datos. Solo lectura, sin órdenes.
Cada ~1 s: UNA petición POST /books con los tokens de los 15m de las 6 monedas de la ventana VIVA y de la SIGUIENTE
(pre-posición, §6A/§32). Escribe solo si el hash del libro cambió. Top N_NIVELES por lado, mejor primero.
Fila: t_recepcion_ms,t_libro_ms(exchange),token,bids "p@s;p@s;...",asks "p@s;...";  mapa: fila M,t,token,moneda,
inicio,cierre,lado. Salida datalogs/l2_15m/l2_15m_YYYY-MM-DD.csv.gz (miembros gzip anexados por minuto), retención 60 d en el VOLUMEN /dev/sdb (09-Oct; datalogs/l2_15m es un enlace simbólico; guarda de espacio en los
extractores diarios, archivo_volumen.py).
Cron cada minuto: bucle de ~58 s con flock (sin screen). Uso: python3 libro_l2_15m_fase0.py [--seg 58]
"""
import argparse
import gzip
import json
import time
from datetime import datetime, timezone

import requests

from archivo_volumen import VOL, retencion

OUT = VOL / "l2_15m"
N_NIVELES = 10
MONEDAS = ("btc", "eth", "sol", "xrp", "doge", "bnb")
S = requests.Session()


def tokens():
    ini = int(time.time() // 900 * 900)
    out = []
    for i0 in (ini, ini + 900):
        for m in MONEDAS:
            try:
                r = S.get("https://gamma-api.polymarket.com/markets", params={"slug": f"{m}-updown-15m-{i0}"},
                          timeout=5).json()
            except Exception:
                continue
            if r:
                for tok, lado in zip(json.loads(r[0]["clobTokenIds"]), json.loads(r[0]["outcomes"])):
                    out.append((tok, m.upper(), i0, i0 + 900, lado))
    return out


def niveles(xs, mejor_primero_desc):
    xs = sorted(((float(x["price"]), x["size"]) for x in xs), reverse=mejor_primero_desc)[:N_NIVELES]
    return ";".join(f"{p:g}@{s}" for p, s in xs)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seg", type=float, default=58.0)
    a = ap.parse_args()
    OUT.mkdir(exist_ok=True)
    fin = time.time() + a.seg
    toks, t_tok, ventana = [], 0, None
    hashes = {}
    lineas = []
    while time.time() < fin:
        t0 = time.time()
        v = int(t0 // 900)
        if v != ventana or not toks or t0 - t_tok > 300:
            toks, t_tok, ventana = tokens(), t0, v
            for tok, m, i0, c, lado in toks:
                lineas.append(f"M,{int(t0 * 1000)},{tok},{m},{i0},{c},{lado}\n")
        if toks:
            try:
                r = S.post("https://clob.polymarket.com/books", json=[{"token_id": t[0]} for t in toks], timeout=3)
                rec = int(time.time() * 1000)
                for b in r.json() if r.status_code == 200 else []:
                    tok, h = b.get("asset_id"), b.get("hash")
                    if not tok or hashes.get(tok) == h:
                        continue
                    hashes[tok] = h
                    lineas.append(f"{rec},{b.get('timestamp')},{tok},{niveles(b.get('bids', []), True)},"
                                  f"{niveles(b.get('asks', []), False)}\n")
            except Exception:
                pass
        time.sleep(max(0.0, 1.0 - (time.time() - t0)))
    dia = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    with gzip.open(OUT / f"l2_15m_{dia}.csv.gz", "at", compresslevel=6) as f:
        f.writelines(lineas)
    retencion("l2_15m")


if __name__ == "__main__":
    main()
