#!/usr/bin/env python3
"""macro_release_fast_fase0.py -- FASE 0, SOLO OBSERVACIÓN: ¿cuánto tardamos en tener un dato macro
frente a lo que tarda el libro de Polymarket en repreciarse? (ronda 1 #7, Javi 30-Sep: "soluciónalo,
tiene que haber una manera").

Contexto: con Statistics Canada WDS el dato del PIB llegó a +38,9 s y el libro se repreció en 1-5 s.
Aquí se prueba la vía rápida: la propia página/fichero del organismo que pasa de 404 a 200 en el
instante de la publicación, sondeada en paralelo saltándose la caché Varnish de 60 s (cabecera Cookie
de sesión o POST -> pass al origen; un ?x= devuelve 301 y NO sirve), y a la vez se graba el libro real de cada tramo del mercado por REST cada ~0,3 s.

Uso:  macro_release_fast_fase0.py <evento.json>
evento.json: {"nombre","when_utc","urls":[url | {"url","modo":cookie|post|auth|param|plano,"hilos","paso","regex","sin_dato","cabeceras","ya_publicado"}],"regex":{"clave":"expr con 1 grupo"},"event_slugs":[...]}
Salidas en /root/polymarket-research-datalogs/macro_fast/<nombre>_{fuente.jsonl,libro.csv,pagina.html}.
No envía órdenes. El proceso espera hasta T-25 s y termina en T+150 s.
"""
import csv
import json
import random
import re
import sys
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

DIR = Path("/root/polymarket-research-datalogs/macro_fast")
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36")
HILOS_FUENTE, HILOS_LIBRO = 8, 6
ANTES_S, DESPUES_S = 25, 150
_lock = threading.Lock()
_fin = threading.Event()
_primero = {}
_n = {}
_cruda = set()


def _ms() -> int:
    return int(time.time() * 1000)


def _fuente(ent: dict, idx: int, t0: float, f_log, regex: dict, nombre: str) -> None:
    """Un hilo de sondeo. modo: 'cookie' (cabecera Cookie de sesión aleatoria -> Varnish hace pass, age=0),
    'post' (POST vacío, tampoco se cachea), 'auth' (Authorization), 'param' (?x=aleatorio, para bls.gov),
    'plano' (GET normal, caché de 60 s: control).
    OJO: un parámetro ?x= en bea.gov devuelve 301 cacheado un año; no sirve como anti-caché."""
    url, modo, hilos, paso = ent["url"], ent.get("modo", "cookie"), ent.get("hilos", HILOS_FUENTE), ent.get("paso", 0.15)
    clave = f"{modo} {url}"
    ses = requests.Session()
    ses.headers.update({"User-Agent": UA, "Accept": "text/html,application/xhtml+xml,*/*"})
    time.sleep(idx * paso)                       # escalonado: 1 petición cada `paso` s por entrada
    ult = None
    while not _fin.is_set() and clave not in _primero:   # con el dato en la mano se deja de sondear esa entrada
        t_env = _ms()
        try:
            h = dict(ent.get("cabeceras") or {})
            destino = url
            if modo == "param":                  # bls.gov sí acepta ?x= (bea.gov NO: 301)
                destino = f"{url}{'&' if '?' in url else '?'}x={random.randrange(10**9)}"
            if modo == "cookie":
                h["Cookie"] = f"SESS{random.randrange(16**8):08x}={random.randrange(16**12):012x}"
            elif modo == "auth":
                h["Authorization"] = f"Bearer {random.randrange(16**12):012x}"
            r = (ses.post(destino, data=b"", headers=h, timeout=6, allow_redirects=False) if modo == "post"
                 else ses.get(destino, headers=h, timeout=6, allow_redirects=False))
            est = r.status_code
            binario = "pdf" in r.headers.get("content-type", "")
            cuerpo = r.text if est == 200 and not binario else ""
            cab = {k: r.headers.get(k) for k in ("age", "last-modified", "date", "x-drupal-cache", "x-hits", "content-length")}
        except Exception as e:
            est, cuerpo, cab = f"ERR {type(e).__name__}", "", {}
        t_rec = _ms()
        with _lock:
            _n[clave] = _n.get(clave, 0) + 1
            vals, es_nuevo = {}, False
            if est == 200 and clave not in _primero:
                for k, ex in (ent.get("regex") or regex).items():
                    m = re.search(ex, cuerpo, re.I | re.S)
                    vals[k] = m.group(1) if m else None
                # "ya_publicado": valores que la página YA muestra antes de la hora (p. ej. el mes anterior en una
                # URL fija como empsit.nr0.htm); mientras la regex siga devolviendo eso, no hay dato nuevo.
                # Solo cuenta como dato una página 200 que ya lo trae; "sin_dato" (PDF) cuenta por el cambio de estado.
                viejo = ent.get("ya_publicado") or {}
                es_nuevo = any(v is not None and v != viejo.get(k) for k, v in vals.items()) or bool(ent.get("sin_dato"))
            if est != ult or es_nuevo:
                fila = {"t_envio_ms": t_env, "t_recibido_ms": t_rec, "rel_s": round(t_rec / 1000 - t0, 3),
                        "rel_envio_s": round(t_env / 1000 - t0, 3), "modo": modo, "url": url, "estado": est,
                        "bytes": len(cuerpo), "cab": cab, "n_peticiones": _n[clave], "valores": vals}
                if cuerpo and clave not in _cruda and (es_nuevo or not ent.get("ya_publicado")):
                    _cruda.add(clave)                 # primer 200 tal cual, traiga o no el dato (para revisar la regex)
                    (DIR / f"{nombre}_cruda_{len(_cruda)}_{modo}.html").write_text(cuerpo, encoding="utf-8")
                if es_nuevo:
                    _primero[clave] = fila
                f_log.write(json.dumps(fila) + "\n")
                f_log.flush()
        ult = est
        time.sleep(max(0.0, hilos * paso - (_ms() - t_env) / 1000))


def _libro(tokens: list, idx: int, t0: float, w, n_hilos: int, pausa: float) -> None:
    ses = requests.Session()
    mios = tokens[idx::n_hilos]
    while not _fin.is_set():
        for pregunta, tok in mios:
            t_env = _ms()
            try:
                j = ses.get("https://clob.polymarket.com/book", params={"token_id": tok}, timeout=4).json()
                asks = sorted((float(a["price"]), float(a["size"])) for a in (j.get("asks") or []))
                bids = sorted(((float(b["price"]), float(b["size"])) for b in (j.get("bids") or [])), reverse=True)
                fila = [_ms(), round(_ms() / 1000 - t0, 3), pregunta, bids[0][0] if bids else "", bids[0][1] if bids else "",
                        asks[0][0] if asks else "", asks[0][1] if asks else "", _ms() - t_env]
            except Exception as e:
                fila = [_ms(), round(_ms() / 1000 - t0, 3), pregunta, "", "", "", "", f"ERR {type(e).__name__}"]
            with _lock:
                w.writerow(fila)
            time.sleep(pausa)        # por petición: no competir con los ejecutores live por el límite del CLOB


def main() -> int:
    global ANTES_S, DESPUES_S
    ev = json.loads(Path(sys.argv[1]).read_text())
    ANTES_S, DESPUES_S = ev.get("antes_s", ANTES_S), ev.get("despues_s", DESPUES_S)
    nombre = re.sub(r"[^a-z0-9]+", "_", ev["nombre"].lower()).strip("_")
    t0 = datetime.fromisoformat(ev["when_utc"].replace("Z", "+00:00")).timestamp()
    DIR.mkdir(parents=True, exist_ok=True)
    tokens = []
    for slug in ev.get("event_slugs", []):
        try:
            e = requests.get("https://gamma-api.polymarket.com/events", params={"slug": slug}, timeout=15).json()[0]
            for m in e["markets"]:
                tokens.append((m["question"][:80], json.loads(m["clobTokenIds"])[0]))
        except Exception as ex:
            print("no se pudo cargar", slug, ex, flush=True)
    print(f"{ev['nombre']}: {len(ev['urls'])} URLs, {len(tokens)} tramos; esperando a T-{ANTES_S}s", flush=True)
    while time.time() < t0 - ANTES_S:
        time.sleep(min(30, max(0.2, t0 - ANTES_S - time.time())))
    f_log = open(DIR / f"{nombre}_fuente.jsonl", "a", encoding="utf-8")
    f_lib = open(DIR / f"{nombre}_libro.csv", "a", newline="", encoding="utf-8")
    w = csv.writer(f_lib)
    w.writerow(["t_ms", "rel_s", "pregunta", "bid", "bid_size", "ask", "ask_size", "lat_ms"])
    ents = [{"url": u} if isinstance(u, str) else u for u in ev["urls"]]
    hilos = [threading.Thread(target=_fuente, args=(e, i, t0, f_log, ev.get("regex", {}), nombre), daemon=True)
             for e in ents for i in range(e.get("hilos", HILOS_FUENTE))]
    n_lib, pausa = ev.get("libro_hilos", HILOS_LIBRO), ev.get("libro_pausa_s", 0.05)
    hilos += [threading.Thread(target=_libro, args=(tokens, i, t0, w, n_lib, pausa), daemon=True) for i in range(n_lib)]
    for h in hilos:
        h.start()
    while time.time() < t0 + DESPUES_S:
        time.sleep(1)
    _fin.set()
    time.sleep(1.5)
    f_lib.close()
    f_log.close()
    for clave, fila in sorted(_primero.items(), key=lambda kv: kv[1]["t_recibido_ms"]):
        print(f"primer 200 con dato: {fila['rel_s']:+.3f} s (enviada {fila['rel_envio_s']:+.3f})  {clave}  "
              f"{fila.get('valores')}  {fila.get('cab')}", flush=True)
    print("peticiones por entrada:", json.dumps(_n), flush=True)
    if not _primero:
        print("ninguna URL devolvió el dato en la ventana", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
