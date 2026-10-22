#!/usr/bin/env python3
"""r3_shadow.py -- BRAZO SHADOW EN TIEMPO REAL de la regla R2/R3 de la seleccion adversa de B (misión 5m barato; ETH/SOL/XRP 5m). DRY-RUN PURO.

SOLO OBSERVA: WS publico de mercado del CLOB (lectura) y gamma-api publica (descubrimiento de mercados). Sin ordenes, sin claves, sin .env, sin endpoints privados,
sin importar nada de produccion ni de dev. La logica vive en r3_regla.py (nucleo puro, con tests); aqui solo hay red, disco y reinicio.

Por cada mercado 5m de ETH/SOL/XRP (y su 15m del mismo lado) vigila el WS desde 25 s antes de abrir hasta T=60 s y evalua 3 politicas x 3 escenarios de relleno
(ver r3_regla.py). Filas (jsonl.gz diario, miembros gzip anadidos):  mkt, smp (rasgos y flags cada 5 s con el top en banda), dec (post/cancela/no_cotiza con motivo),
fill (relleno simulado con rasgos al pujar y al detectar), fin_t (resumen por trader), mkt_fin (cobertura: completo/huecos/reconexiones), latido, error.
El DESENLACE oficial NO lo escribe este proceso: lo anade r3_desenlaces.py (cron) en r3_desenlaces_YYYY-MM-DD.jsonl.gz (un solo escritor por fichero).
Reinicio idempotente: el ESTADO ES EL LOG (claves `k` ya emitidas no se repiten; un mercado visto sin `mkt_fin` se cierra como completo=false y NO se revigila).
Salida: /root/polymarket-research-datalogs/r3_shadow/r3_shadow_YYYY-MM-DD.jsonl.gz, retencion 45 d, fuera de git.
Uso:  nice -n 5 .venv/bin/python -I experimentos/5m_barato/b_seleccion_adversa/r3_shadow/r3_shadow.py [--salida DIR]
      --resumen | --minutos N --salida DIR (SOLO humo; prohibido con la salida por defecto)"""
import argparse
import asyncio
import glob
import gzip
import json
import os
import queue
import resource
import signal
import sys
import threading
import time
import zlib
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import r3_regla as R  # noqa: E402

SALIDA_DEFECTO = "/root/polymarket-research-datalogs/r3_shadow"
GAMMA = "https://gamma-api.polymarket.com/markets"
WS_URL = "wss://ws-subscriptions-clob.polymarket.com/ws/market"
MONEDAS = ("eth", "sol", "xrp")
PRE_S = R.PRE_S            # se suscribe PRE_S s antes de abrir el 5m (fuente unica: r3_regla.PRE_S, de la que deriva el corte arranque_tarde)
RETENCION_DIAS, RELEER_DIAS = 45, 3
RSS_MAX_MB = 450
TICK_S = 0.1


def ahora_ms():
    return time.time_ns() // 1_000_000


def _dia(ms):
    return datetime.fromtimestamp(ms / 1000.0, timezone.utc).strftime("%Y-%m-%d")


def _limpia(o):
    if isinstance(o, float) and (o != o or o in (float("inf"), float("-inf"))):
        return None
    if isinstance(o, dict):
        return {k: _limpia(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_limpia(v) for v in o]
    return o


# ------------------------------------------------------------------ disco
class Salida:
    def __init__(self, d, prefijo="r3_shadow"):
        self.d, self.prefijo = Path(d), prefijo
        self.d.mkdir(parents=True, exist_ok=True)
        self.q = queue.SimpleQueue()
        self.parar = threading.Event()
        self.hilo = threading.Thread(target=self._bucle, daemon=True, name="r3_escritor")
        self.hilo.start()

    def put(self, row):
        self.q.put_nowait(row)

    def _vaciar(self):
        por_dia = {}
        try:
            while True:
                row = self.q.get_nowait()
                try:
                    ln = json.dumps(row, separators=(",", ":"), allow_nan=False)
                except ValueError:
                    ln = json.dumps(_limpia(row), separators=(",", ":"), allow_nan=False)
                por_dia.setdefault(_dia(row.get("r") or ahora_ms()), []).append(ln)
        except queue.Empty:
            pass
        for dia, lineas in por_dia.items():
            blob = gzip.compress(("\n".join(lineas) + "\n").encode(), 6)
            with open(self.d / f"{self.prefijo}_{dia}.jsonl.gz", "ab") as f:
                f.write(blob)
                f.flush()
                os.fsync(f.fileno())

    def _bucle(self):
        while not self.parar.wait(5):
            try:
                self._vaciar()
            except Exception as e:
                print(f"{datetime.now(timezone.utc).isoformat()} escritor: {type(e).__name__}: {e}", file=sys.stderr, flush=True)

    def cerrar(self):
        self.parar.set()
        self.hilo.join(timeout=6)
        self._vaciar()


def leer_gz_tolerante(path, tipos=None):
    """Lee miembros gzip concatenados EN STREAMING (memoria plana: antes cada miembro copiaba el resto del fichero en `unused_data`, O(miembros x tamano)); tolera un ultimo
    miembro truncado o corrupto (proceso muerto a mitad de escritura: se devuelve lo anterior y se para). `tipos` (iterable de str): solo las filas de esos tipos; el filtro es
    una busqueda de subcadena sobre la linea ANTES de json.loads (las filas se escriben compactas: `"tipo":"fill"`), y despues se verifica el valor parseado."""
    pats = None if tipos is None else tuple(f'"tipo":"{t}"'.encode() for t in tipos)
    ok = None if tipos is None else frozenset(tipos)
    try:
        f = gzip.open(path, "rb")
    except OSError:
        return
    try:
        for raw in f:
            if pats is not None and not any(p in raw for p in pats):
                continue
            try:
                row = json.loads(raw.decode(errors="replace"))
            except ValueError:
                continue
            if ok is not None and row.get("tipo") not in ok:
                continue
            yield row
    except (EOFError, OSError, zlib.error):
        return
    finally:
        f.close()


def restaurar(dirn, ahora_s, prefijo="r3_shadow", dias=RELEER_DIAS):
    """(emitidos, vistos, terminados): claves ya escritas, slugs con `mkt` y slugs con `mkt_fin` de los ultimos `dias` dias."""
    emitidos, vistos, terminados = set(), set(), set()
    hoy = datetime.fromtimestamp(ahora_s, timezone.utc).date()
    for i in range(dias, -1, -1):
        f = Path(dirn) / f"{prefijo}_{(hoy - timedelta(days=i)).isoformat()}.jsonl.gz"
        if not f.exists():
            continue
        for row in leer_gz_tolerante(f):
            k = row.get("k")
            if k:
                emitidos.add(k)
            if row.get("tipo") == "mkt":
                vistos.add(row["slug"])
            elif row.get("tipo") == "mkt_fin":
                terminados.add(row["slug"])
    return emitidos, vistos, terminados


def aplicar_retencion(dirn, ahora_s, prefijo="r3_shadow", dias=RETENCION_DIAS):
    lim = (datetime.fromtimestamp(ahora_s, timezone.utc) - timedelta(days=dias)).strftime("%Y-%m-%d")
    borrados = []
    for f in glob.glob(str(Path(dirn) / f"{prefijo}_*.jsonl.gz")):
        d = os.path.basename(f)[len(prefijo) + 1:-len(".jsonl.gz")]
        if len(d) == 10 and d < lim:
            os.remove(f)
            borrados.append(f)
    return borrados


# ------------------------------------------------------------------ red (solo lectura)
def mercado_gamma(coin, marco, ini):
    """{slug,id,up,down} del mercado `coin-updown-{marco}-{ini}`; None si no existe. Fail-closed si los outcomes no son [Up, Down]."""
    import requests
    slug = f"{coin}-updown-{marco}-{ini}"
    r = requests.get(GAMMA, params={"slug": slug}, timeout=8).json()
    if not r:
        return None
    m = r[0]
    out = json.loads(m["outcomes"]) if isinstance(m["outcomes"], str) else m["outcomes"]
    toks = json.loads(m["clobTokenIds"]) if isinstance(m["clobTokenIds"], str) else m["clobTokenIds"]
    if [o.lower() for o in out] != ["up", "down"] or len(toks) != 2:
        raise ValueError(f"{slug}: outcomes {out} inesperados (fail-closed)")
    return {"slug": slug, "id": str(m["id"]), "up": toks[0], "down": toks[1]}


async def mk15_cacheado(cache15, coin, ini15, loop, fetch=None):
    """mercado 15m (coin, ini15) con cache SOLO de resultados validos: un None/{}/error de gamma (el 15m aun no listado) NO se cachea y se reintenta en la siguiente vuelta
    (antes se guardaba el None y el 5m entero quedaba sin R2/R3 mientras durara el 15m). Devuelve el mercado o None; las excepciones suben al llamador (backoff por slug)."""
    k = (coin, ini15)
    v = cache15.get(k)
    if v:
        return v
    v = await loop.run_in_executor(None, fetch or mercado_gamma, coin, "15m", ini15)
    if v:
        cache15[k] = v
    return v


async def vigilar(nuc, m, parar, fin_ms):
    import websockets
    toks = [m.up, m.dn, m.u15, m.d15]
    primera = True
    while not parar.is_set() and not m.cerrado and ahora_ms() < fin_ms:
        try:
            async with websockets.connect(WS_URL, open_timeout=10, close_timeout=2, max_size=None, ping_interval=None) as ws:
                await ws.send(json.dumps({"assets_ids": toks, "type": "market"}))
                if not primera:
                    m.reconectado(time.time())
                primera = False

                async def latido():
                    while True:
                        await asyncio.sleep(2.0)
                        await ws.send("PING")
                tl = asyncio.create_task(latido())
                try:
                    while not parar.is_set() and not m.cerrado and ahora_ms() < fin_ms:
                        try:
                            raw = await asyncio.wait_for(ws.recv(), timeout=1.0)
                        except asyncio.TimeoutError:
                            continue
                        t = time.time()
                        if isinstance(raw, (bytes, bytearray)):
                            raw = raw.decode("utf-8", "replace")
                        if not raw or raw[0] not in "[{":
                            m.vivo(t)                        # PONG: conexion viva (un libro quieto no es un libro roto)
                            continue
                        try:
                            datos = json.loads(raw)
                        except ValueError:
                            continue
                        for msg in (datos if isinstance(datos, list) else [datos]):
                            if isinstance(msg, dict):
                                try:
                                    m.on_msg(msg, t)
                                except Exception as e:
                                    nuc.stats["error_mensaje"] = nuc.stats.get("error_mensaje", 0) + 1
                                    if nuc.stats["error_mensaje"] in (1, 10, 100, 1000):
                                        nuc.emit({"k": f"error_msg|{m.slug}|{nuc.stats['error_mensaje']}", "tipo": "error", "r": ahora_ms(),
                                                  "m": f"{type(e).__name__}: {str(e)[:80]}"})
                finally:
                    tl.cancel()
        except asyncio.CancelledError:
            raise
        except Exception as e:
            nuc.stats["ws_error"] = nuc.stats.get("ws_error", 0) + 1
            if not m.cerrado:
                m.huecos += 1
            await asyncio.sleep(0.5)
            if nuc.stats["ws_error"] in (1, 10, 100, 1000):
                nuc.emit({"k": f"ws_error|{m.slug}|{nuc.stats['ws_error']}", "tipo": "error", "r": ahora_ms(), "m": f"ws {type(e).__name__}: {str(e)[:80]}"})


def rss_mb():
    with open("/proc/self/status") as f:
        for ln in f:
            if ln.startswith("VmRSS"):
                return int(ln.split()[1]) / 1024.0
    return None


async def ticker(nuc, parar):
    while not parar.is_set():
        t0 = time.time()
        try:
            nuc.tick(t0)
        except Exception as e:
            nuc.stats["error_tick"] = nuc.stats.get("error_tick", 0) + 1
            nuc.emit({"k": f"error_tick|{ahora_ms()}", "tipo": "error", "r": ahora_ms(), "m": f"tick {type(e).__name__}: {str(e)[:100]}"})
        await asyncio.sleep(max(0.0, TICK_S - (time.time() - t0)))


async def principal(args, nuc, vistos, terminados, parar):
    loop = asyncio.get_running_loop()
    lanzados, tareas, fallos, cache15 = set(vistos), [], {}, {}
    t_fin = time.time() + args.minutos * 60 if args.minutos else None
    t_latido = t_ret = 0.0
    tr_tick = asyncio.create_task(ticker(nuc, parar))
    # mercados vistos sin cierre (proceso muerto): se cierran como incompletos y no se revigilan
    for s in sorted(vistos - terminados):
        try:
            coin = s.split("-")[0]
            ini = int(s.rsplit("-", 1)[1])
        except (ValueError, IndexError):
            continue
        nuc.emit({"k": f"mkt_fin|{s}", "tipo": "mkt_fin", "r": ahora_ms(), "slug": s, "coin": coin, "cierre": ini + 300, "completo": False, "arranque_tarde": None,
                  "huecos": None, "reconex": None, "n_msgs": None, "n_smp": None, "n_dec": None, "parada": "reinicio_proceso"})
    nuc.emit({"k": f"inicio|{ahora_ms()}", "tipo": "inicio", "r": ahora_ms(), "pid": os.getpid(), "minutos": args.minutos, "emitidos": len(nuc.emitidos), "version": R.VERSION,
              "config": {"topes_b": {"max_vivas": R.MAX_VIVAS, "ordenes_puja": R.MAX_ORDENES_PUJA, "ordenes_total_dia": R.MAX_ORDENES_TOTAL}, "arranque_tarde_corte": "ini-PRE_S+TOL",
                         "PRE_S": R.PRE_S, "ARRANQUE_TOL_S": R.ARRANQUE_TOL_S, "R2_MAX_MILS": R.R2_MAX_MILS, "VOL30_MIN": R.VOL30_MIN, "HORA_MIN": R.HORA_MIN, "T_INI": R.T_INI, "T_STOP": R.T_STOP, "k": R.K_POR_MONEDA,
                         "escenarios": list(R.ESCENARIOS), "politicas": list(R.POLITICAS)}})
    while not parar.is_set() and (t_fin is None or time.time() < t_fin):
        ahora = time.time()
        ini_act = int(ahora // 300 * 300)
        for ini in (ini_act, ini_act + 300):
            if not (ini - PRE_S <= ahora < ini + 300 - R.T_STOP - 5):
                continue
            for coin in MONEDAS:
                slug = f"{coin}-updown-5m-{ini}"
                if slug in lanzados or fallos.get(slug, (0, 0))[1] > ahora:
                    continue
                ini15 = ini // 900 * 900
                try:
                    mk5 = await loop.run_in_executor(None, mercado_gamma, coin, "5m", ini)
                    mk15 = await mk15_cacheado(cache15, coin, ini15, loop)
                except Exception as e:
                    n = fallos.get(slug, (0, 0))[0] + 1
                    fallos[slug] = (n, ahora + min(2 * n, 15))
                    nuc.stats["gamma_error"] = nuc.stats.get("gamma_error", 0) + 1
                    if n in (1, 5, 20):
                        nuc.emit({"k": f"gamma_error|{slug}|{n}", "tipo": "error", "r": ahora_ms(), "m": f"gamma {slug}: {type(e).__name__}: {str(e)[:80]}"})
                    continue
                if not mk5 or not mk15:
                    n = fallos.get(slug, (0, 0))[0] + 1
                    fallos[slug] = (n, ahora + min(2 * n, 15))
                    continue
                lanzados.add(slug)
                m = nuc.nuevo(coin, ini, mk5, mk15, ahora_ms())
                tareas.append(asyncio.create_task(vigilar(nuc, m, parar, (m.fin - R.T_STOP + 15) * 1000)))
        tareas = [t for t in tareas if not t.done()]
        nuc.podar(ahora)
        for k in [k for k in cache15 if k[1] < ini_act // 900 * 900 - 1800]:
            del cache15[k]
        if len(lanzados) > 5000:
            lanzados = {s for s in lanzados if int(s.rsplit("-", 1)[1]) > ahora - 7200}
        if ahora - t_latido > 600:
            t_latido = ahora
            rss = rss_mb()
            nuc.emit({"k": f"latido|{ahora_ms()}", "tipo": "latido", "r": ahora_ms(), "rss_mb": None if rss is None else round(rss, 1),
                      "vigilando": sum(1 for m in nuc.mercados.values() if not m.cerrado), "stats": dict(nuc.stats)})
            if rss and rss > RSS_MAX_MB:
                print(f"RSS {rss:.0f} MB > {RSS_MAX_MB}: salgo para que el watchdog reinicie", file=sys.stderr, flush=True)
                parar.set()
        if ahora - t_ret > 3600:
            t_ret = ahora
            if not args.minutos:
                aplicar_retencion(args.salida, ahora)
        await asyncio.sleep(0.25)
    parar.set()
    if tareas:
        await asyncio.gather(*tareas, return_exceptions=True)
    await tr_tick
    for m in list(nuc.mercados.values()):                # lo que queda abierto al parar: cierre incompleto
        if not m.cerrado:
            nuc.cerrar(m, time.time(), "parada_proceso")
    nuc.emit({"k": f"fin_proceso|{ahora_ms()}", "tipo": "fin_proceso", "r": ahora_ms(), "stats": dict(nuc.stats)})


def resumen(dirn):
    tot = Counter()
    for f in sorted(glob.glob(str(Path(dirn) / "r3_shadow_*.jsonl.gz"))):
        c = Counter(r.get("tipo") for r in leer_gz_tolerante(f))
        print(os.path.basename(f), dict(c))
        tot.update(c)
    print("TOTAL", dict(tot))


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--salida", default=SALIDA_DEFECTO)
    ap.add_argument("--minutos", type=float, default=None, help="SOLO prueba de humo (acotada)")
    ap.add_argument("--resumen", action="store_true")
    args = ap.parse_args()
    if args.resumen:
        resumen(args.salida)
        return 0
    if args.minutos and os.path.abspath(args.salida) == SALIDA_DEFECTO:
        sys.exit("--minutos exige --salida distinta de la de produccion (fail-closed)")
    try:
        resource.setrlimit(resource.RLIMIT_AS, (1_500_000_000, 1_500_000_000))
    except (ValueError, OSError):
        pass
    Path(args.salida).mkdir(parents=True, exist_ok=True)
    emitidos, vistos, terminados = restaurar(args.salida, time.time())
    out = Salida(args.salida)
    nuc = R.Nucleo(out.put, emitidos, prueba=True if args.minutos else None)
    parar = asyncio.Event()

    async def corre():
        loop = asyncio.get_running_loop()
        for s in (signal.SIGTERM, signal.SIGINT):
            loop.add_signal_handler(s, parar.set)
        await principal(args, nuc, vistos, terminados, parar)
    print(f"{datetime.now(timezone.utc).isoformat()} r3_shadow arrancando pid={os.getpid()} salida={args.salida} emitidos={len(emitidos)} "
          f"vistos={len(vistos)} sin_cierre={len(vistos - terminados)}", flush=True)
    try:
        asyncio.run(corre())
    finally:
        out.cerrar()
    print(f"{datetime.now(timezone.utc).isoformat()} r3_shadow terminado stats={dict(nuc.stats)}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
