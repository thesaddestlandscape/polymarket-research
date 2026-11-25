#!/usr/bin/env python3
"""
new_market_universo.py -- PROTOTIPO endurecido (13-Nov, staging; NO lanzado, NO integrado, sin screen).

Escucha `new_market` del WS del CLOB (patron sniper_listados_fase0) y persiste los Up/Down de las 6 monedas con TOKENS ya resueltos
en UNIV_DIR/new_market_universo_<dia>.csv.gz (formato y lectura en universo_5m_io; fuera de git; retencion 7 d). Sirve para sembrar
libro_estado_ws sin gamma /markets/{id} y para conocer los 5m ~24 h antes.
SOLO ESCRIBE ese fichero. No envia ordenes ni firma. Gamma solo en lectura (<= 1,8 GET/s, 12 slugs por GET): relleno de huecos al
arrancar, al reconectar y cada RELLENO_PERIODICO_S; salta los slugs que YA estan en el fichero (los haya escrito este listener o el
adelanto de capture_markets) y al primer 429 aborta y no vuelve a llamar hasta la pausa de universo_5m_io.pausa_tras_429.
Cierre limpio con SIGTERM/SIGINT (sale en <= ~5 s; cada lote ya esta en disco, nada que volcar). Reconexion con backoff.
Dedupe por market_id contra hoy+ayer en disco (reinicio idempotente); ws y gamma no se duplican: el que llega segundo se descarta.
"""
import asyncio, json, os, random, signal, sys, threading, time
from datetime import datetime, timezone
from pathlib import Path

import requests
import websockets

sys.path.insert(0, str(Path(__file__).resolve().parent))
import universo_5m_io as U

WS_URL = os.environ.get("NMU_WS_URL", "wss://ws-subscriptions-clob.polymarket.com/ws/market")
GAMMA_EVENTS = os.environ.get("NMU_GAMMA_URL", "https://gamma-api.polymarket.com/events")
PING_S = 10.0
SIN_MENSAJES_S = 30.0                       # ni mensajes ni PONG en 30 s: conexion muerta (new_market llega cada ~5 min; el PONG cuenta)
HORIZONTE_RELLENO_MIN = int(os.environ.get("NMU_HORIZONTE_MIN", "1440"))
RELLENO_PERIODICO_S = 600
LOTE_SLUGS = 12
GAMMA_INTERVALO_S = 0.55                    # ritmo COMPARTIDO con capture_markets y el delta (universo_5m_io.esperar_turno)
ARRANQUE_JITTER_S = float(os.environ.get('NMU_JITTER_S', '20'))   # arranque en frio escalonado: el primer relleno espera U(0, 20 s)
STAT_S = 60
DESFASE_RELOJ_MS = 5000                     # |recepcion - evento| mediano > 5 s => reloj local o del exchange desfasado (se avisa en el log)


def _log(m):
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {m}", flush=True)


def rellenar_huecos(conocidos, ahora=None, get=None, stop=None):
    """Gamma (solo lectura): slugs {activo}-updown-5m-{ts} desde la proxima ventana hasta HORIZONTE_RELLENO_MIN que NO estan en
    `conocidos` (set de slugs); 12 por GET con turno COMPARTIDO entre procesos; no llama si hay pausa 429 compartida; al primer 429
    marca la pausa compartida y corta; `stop` (threading.Event) se comprueba entre lotes. Devuelve (filas, contadores)."""
    ahora = int(ahora or time.time())
    get = get or (lambda p: requests.get(GAMMA_EVENTS, params=p, timeout=30, headers={"User-Agent": "nmu/1"}))
    conocidos = set(conocidos)
    sig = ((ahora // 300) + 1) * 300
    pend = {a: [t for t in range(sig, ahora + HORIZONTE_RELLENO_MIN * 60 + 1, 300) if f"{a}-updown-5m-{t}" not in conocidos]
            for a in sorted(U.ACTIVOS)}
    c = {"pendientes": sum(len(v) for v in pend.values()), "gets": 0, "filas": 0, "falta": 0, "abortado_429": False, "errores": 0,
         "en_pausa": False, "parado": False}
    if U.pausa_activa() > 0:
        c["en_pausa"] = True
        return [], c
    filas = []
    for a, tss in pend.items():
        for i in range(0, len(tss), LOTE_SLUGS):
            if stop is not None and stop.is_set():
                c["parado"] = True
                c["filas"] = len(filas)
                return filas, c
            lote = [f"{a}-updown-5m-{t}" for t in tss[i:i + LOTE_SLUGS]]
            esp = U.esperar_turno(GAMMA_INTERVALO_S)
            if esp > 0:
                if stop is not None:
                    if stop.wait(esp):
                        c["parado"] = True
                        c["filas"] = len(filas)
                        return filas, c
                else:
                    time.sleep(esp)
            c["gets"] += 1
            try:
                r = get([("slug", s) for s in lote])
                if r.status_code == 429:
                    c["abortado_429"] = True
                    U.marcar_429()
                    c["filas"] = len(filas)
                    return filas, c
                r.raise_for_status()
                evs = r.json()
                if not isinstance(evs, list):
                    raise ValueError("respuesta no lista")
            except Exception as ex:
                c["errores"] += 1
                _log(f"relleno gamma: lote {lote[0]}..{lote[-1]} fallo ({type(ex).__name__}); se reintenta en el proximo relleno")
                continue
            t_recv = int(time.time() * 1000)
            hallados = set()
            for ev in evs:
                if isinstance(ev, dict):
                    for f in U.filas_de_evento_gamma(ev, t_recv):
                        if f["slug"] not in hallados:
                            hallados.add(f["slug"])
                            filas.append(f)
            c["falta"] += len(lote) - len(hallados)
    c["filas"] = len(filas)
    return filas, c


class Estado:
    def __init__(self):
        mk, st = U.leer()
        if st["truncados"]:
            _log(f"aviso: {st['truncados']} fichero(s) truncado(s)/ilegible(s); se usa lo legible")
        self.vistos = {k: v["slug"] for k, v in mk.items()}          # market_id -> slug (hoy+ayer en disco)
        self.lock = threading.Lock()                                  # vistos lo tocan el bucle WS y el hilo de relleno
        self.cont, self.total, self.lag = {}, {}, []
        self.ult_msg = time.time()
        self.parar = False
        self.stop_evt = threading.Event()                             # cierra el hilo de relleno (cooperativo, entre lotes)
        self.hilo = None                                              # hilo de relleno (uno solo, daemon: no bloquea el cierre)
        self.ult_ws = 0.0

    def anotar(self, filas):
        """Descarta lo ya visto (ws vs gamma/capture), registra y devuelve solo lo nuevo."""
        nuevas = []
        with self.lock:
            for f in filas:
                if f["market_id"] in self.vistos:
                    continue
                self.vistos[f["market_id"]] = f["slug"]
                nuevas.append(f)
        return nuevas

    def olvidar(self, filas):
        with self.lock:
            for f in filas:
                self.vistos.pop(f["market_id"], None)


def _stats(est):
    if est.cont:
        txt = ", ".join(f"{a}#{m}:{n}" for (a, m), n in sorted(est.cont.items()))
        lag = sorted(est.lag)
        med = lag[len(lag) // 2] if lag else None
        _log(f"new_market ultimo minuto: {txt} | lag recv-evento p50={med} ms | vistos={len(est.vistos)}")
        if med is not None and abs(med) > DESFASE_RELOJ_MS:
            _log(f"AVISO desfase de reloj: lag mediano {med} ms (> {DESFASE_RELOJ_MS}); revisar NTP")
    else:
        _log(f"new_market ultimo minuto: 0 | vistos={len(est.vistos)}")
    est.cont, est.lag = {}, []


def _relleno_sync(est):
    mk, _ = U.leer()
    return rellenar_huecos({r["slug"] for r in mk.values()}, stop=est.stop_evt)


def _ronda_relleno(est):
    """Una ronda de relleno: lee, pide a gamma, deduplica contra lo visto y escribe. Devuelve los contadores (o None si fallo)."""
    filas = []
    try:
        filas, c = _relleno_sync(est)
        nuevas = est.anotar(filas)               # el WS pudo traerlos mientras tanto
        try:
            if nuevas:
                U.escribir(nuevas)
        except OSError as ex:
            est.olvidar(nuevas)                  # no darlos por vistos: la proxima ronda los reintenta
            _log(f"relleno gamma: no se pudo escribir ({ex}); se reintenta")
            return None
        if c["abortado_429"]:
            _log("relleno gamma: 429, pausa compartida activada")
        if c["filas"] or c["errores"] or c["abortado_429"]:
            _log(f"relleno gamma: {c} (nuevas {len(nuevas)})")
        return c
    except Exception as ex:
        _log(f"relleno gamma fallo: {type(ex).__name__}: {ex}")
        return None


def _hilo_relleno(est):
    """Hilo DAEMON unico, independiente del WS (sigue rellenando si el WS esta caido). Una ronda cada RELLENO_PERIODICO_S, la primera
    tras un jitter aleatorio (arranque escalonado). Nunca hay dos rondas concurrentes; se para con est.stop_evt."""
    if est.stop_evt.wait(random.uniform(0, ARRANQUE_JITTER_S)):
        return
    while not est.stop_evt.is_set():
        _ronda_relleno(est)
        if est.stop_evt.wait(RELLENO_PERIODICO_S):
            return


async def sesion(est):
    async with websockets.connect(WS_URL, ping_interval=20, ping_timeout=20, open_timeout=10, max_queue=None) as ws:
        await ws.send(json.dumps({"type": "market", "assets_ids": [], "custom_feature_enabled": True}))
        _log("WS conectado, escuchando new_market")
        est.ult_msg = t_ping = t_stat = time.time()
        while not est.parar:
            try:
                raw = await asyncio.wait_for(ws.recv(), 5)
            except asyncio.TimeoutError:
                raw = None
                if time.time() - est.ult_msg > SIN_MENSAJES_S:
                    raise ConnectionError("sin mensajes ni PONG")
            ahora = time.time()
            if ahora - t_ping >= PING_S:
                await ws.send("PING")
                t_ping = ahora
            if ahora - t_stat >= STAT_S:
                t_stat = ahora
                _stats(est)
            if raw:
                est.ult_msg = ahora
            if not raw or raw == "PONG":
                continue
            t_recv = int(ahora * 1000)
            try:
                j = json.loads(raw)
            except ValueError:
                continue
            lote = []
            for e in (j if isinstance(j, list) else [j]):
                if not isinstance(e, dict) or (e.get("event_type") or e.get("type")) != "new_market":
                    continue
                f = U.parsear_nuevo(e, t_recv)
                if f is not None:
                    lote.append(f)
            nuevas = est.anotar(lote)
            if nuevas:
                try:
                    U.escribir(nuevas)
                except OSError as ex:
                    _log(f"ERROR escribiendo {len(nuevas)} filas ({ex}); se reintentaran por el relleno de gamma")
                    est.olvidar(nuevas)
                    continue
                est.ult_ws = ahora
                for f in nuevas:
                    k = (f["activo"], f["marco"])
                    est.cont[k] = est.cont.get(k, 0) + 1
                    est.total[k] = est.total.get(k, 0) + 1
                    est.lag.append(t_recv - int(f["t_evento_ms"]))


async def main():
    est = Estado()
    U.retencion()
    loop = asyncio.get_running_loop()
    for sg in (signal.SIGTERM, signal.SIGINT):
        try:
            loop.add_signal_handler(sg, lambda: setattr(est, "parar", True))
        except (NotImplementedError, RuntimeError):
            pass
    est.hilo = threading.Thread(target=_hilo_relleno, args=(est,), daemon=True, name="relleno_gamma")
    est.hilo.start()
    _log(f"inicio; {len(est.vistos)} mercados ya en disco (hoy/ayer); salida {U.UNIV_DIR}")
    espera = 1.0
    while not est.parar:
        t0 = time.time()
        try:
            await sesion(est)
        except Exception as ex:
            _log(f"WS caido: {type(ex).__name__}: {ex}")
        if est.parar:
            break
        espera = 1.0 if time.time() - t0 > 60 else min(30.0, espera * 2)
        for _ in range(int(espera * 10)):
            if est.parar:
                break
            await asyncio.sleep(0.1)
    est.stop_evt.set()                                              # el hilo de relleno sale entre lotes (daemon: no bloquea el cierre)
    est.hilo.join(timeout=3.0)
    _log(f"cierre limpio (new_market recibidos esta ejecucion: {sum(est.total.values())}; relleno "
         + ("parado" if not est.hilo.is_alive() else "aun en un GET (daemon, se descarta)") + ")")


if __name__ == "__main__":
    asyncio.run(main())
