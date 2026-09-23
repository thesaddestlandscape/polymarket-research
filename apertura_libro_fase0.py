#!/usr/bin/env python3
"""apertura_libro_fase0.py -- (23-Sep, idea Javi: "comprar en el primer segundo a un céntimo... ponerte algo que
avise justo antes de que se vaya a abrir cada mercado"). FASE 0, SOLO OBSERVACIÓN (no envía órdenes).

Mide si en el nacimiento de un mercado Up/Down existe un ask barato comprable:
  (a) LISTADO: detecta el instante en que el slug de una ventana futura aparece en gamma-api y consulta
      el libro de YES y NO cada ~0,3 s durante 30 s;
  (b) INICIO DE VENTANA: consulta ambos libros cada ~0,25 s desde T-3 s hasta T+10 s.
Registra el mejor ask (y su tamaño) de cada lado -> data/shadow/apertura_libro_fase0.csv.
Uso: python3 apertura_libro_fase0.py [minutos_de_ejecucion]
"""
import csv, json, sys, threading, time
from datetime import datetime, timezone
from pathlib import Path
import requests

REPO = Path(__file__).resolve().parent
OUT = REPO / "data" / "shadow" / "apertura_libro_fase0.csv"
G = "https://gamma-api.polymarket.com/events"
C = "https://clob.polymarket.com/book"
COINS = ["btc", "eth", "sol", "xrp", "doge", "bnb"]
MARCOS = {"5m": 300, "15m": 900}
S = requests.Session()
_lock = threading.Lock()
CAMPOS = ["ts_utc", "fase", "slug", "rel_s", "ask_yes", "size_yes", "ask_no", "size_no", "lat_ms"]


def _escribir(fila):
    with _lock:
        nuevo = not OUT.exists()
        with open(OUT, "a", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=CAMPOS)
            if nuevo:
                w.writeheader()
            w.writerow(fila)


def _mejor(tok):
    try:
        b = S.get(C, params={"token_id": tok}, timeout=3).json()
        asks = [(float(x["price"]), float(x["size"])) for x in b.get("asks", [])]
        return min(asks) if asks else (None, None)
    except Exception:
        return (None, None)


def _tokens(slug):
    try:
        e = S.get(G, params={"slug": slug}, timeout=5).json()
        if not e:
            return None
        m = e[0]["markets"][0]
        if m.get("closed"):
            return None
        return json.loads(m["clobTokenIds"])
    except Exception:
        return None


def _sondear(fase, slug, toks, ref, dur_s, cada_s):
    fin = time.time() + dur_s
    while time.time() < fin:
        t = time.time()
        (ay, sy), (an, sn) = _mejor(toks[0]), _mejor(toks[1])
        _escribir({"ts_utc": datetime.now(timezone.utc).isoformat(timespec="milliseconds"), "fase": fase,
                   "slug": slug, "rel_s": round(t - ref, 2), "ask_yes": ay, "size_yes": sy,
                   "ask_no": an, "size_no": sn, "lat_ms": round((time.time() - t) * 1000)})
        time.sleep(max(0.0, cada_s - (time.time() - t)))


def main():
    minutos = float(sys.argv[1]) if len(sys.argv) > 1 else 60
    fin = time.time() + minutos * 60
    vistos, programados = set(), set()
    print(f"apertura_libro_fase0 arrancado ({minutos} min)", flush=True)
    while time.time() < fin:
        ahora = time.time()
        for marco, dur in MARCOS.items():
            base = (int(ahora) // dur) * dur
            for k in range(1, 9):          # ventanas futuras (hasta ~2h en 15m, 40 min en 5m)
                t0 = base + k * dur
                for c in COINS:
                    slug = f"{c}-updown-{marco}-{t0}"
                    if slug not in vistos:
                        toks = _tokens(slug)
                        if toks:           # (a) acaba de aparecer (o ya existía al arrancar)
                            vistos.add(slug)
                            fase = "listado_nuevo" if ahora - (t0 - 8 * dur) > 0 and k >= 7 else "listado_ya_existia"
                            threading.Thread(target=_sondear, args=(fase, slug, toks, ahora, 30, 0.3), daemon=True).start()
                    if slug in vistos and slug not in programados and t0 - ahora < 20:
                        toks = _tokens(slug)
                        if toks:           # (b) inicio de ventana
                            programados.add(slug)
                            def _ini(slug=slug, toks=toks, t0=t0):
                                while time.time() < t0 - 3:
                                    time.sleep(0.05)
                                _sondear("inicio_ventana", slug, toks, t0, 13, 0.25)
                            threading.Thread(target=_ini, daemon=True).start()
        time.sleep(5)
    time.sleep(35)
    print("fin", flush=True)


if __name__ == "__main__":
    main()
