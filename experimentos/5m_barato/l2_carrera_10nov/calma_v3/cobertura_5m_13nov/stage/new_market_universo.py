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
import asyncio, json, os, signal, sys, time
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
GAMMA_INTERVALO_S = 0.55
STAT_S = 60
DESFASE_RELOJ_MS = 5000                     # |recepcion - evento| mediano > 5 s => reloj local o del exchange desfasado (se avisa en el log)


def _log(m):
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {m}", flush=True)


def rellenar_huecos(conocidos, ahora=None, get=None):
    """Gamma (solo lectura): slugs {activo}-updown-5m-{ts} desde la proxima ventana hasta HORIZONTE_RELLENO_MIN que NO estan en
    `conocidos` (set de slugs); 12 por GET; al primer 429 corta. Devuelve (filas, contadores). `get`: inyectable en tests."""
    ahora = int(ahora or time.time())
    get = get or (lambda p: requests.get(GAMMA_EVENTS, params=p, timeout=30, headers={"User-Agent": "nmu/1"}))
    conocidos = set(conocidos)
    sig = ((ahora // 300) + 1) * 300
    pend = {a: [t for t in range(sig, ahora + HORIZONTE_RELLENO_MIN * 60 + 1, 300) if f"{a}-updown-5m-{t}" not in conocidos]
            for a in sorted(U.ACTIVOS)}
    c = {"pendientes": sum(len(v) for v in pend.values()), "gets": 0, "filas": 0, "falta": 0, "abortado_429": False, "errores": 0}
    filas, ult = [], 0.0
    for a, tss in pend.items():
        for i in range(0, len(tss), LOTE_SLUGS):
            lote = [f"{a}-updown-5m-{t}" for t in tss[i:i + LOTE_SLUGS]]
            esp = GAMMA_INTERVALO_S - (time.monotonic() - ult)
            if esp > 0:
                time.sleep(esp)
            ult = time.monotonic()
            c["gets"] += 1
            try:
                r = get([("slug", s) for s in lote])
                if r.status_code == 429:
                    c["abortado_429"] = True
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
        self.cont, self.total, self.lag = {}, {}, []
        self.ult_msg = time.time()
        self.ult_relleno = 0.0
        self.pausa_hasta = 0.0
        self.parar = False
        self.ult_ws = 0.0                                              # epoch del ultimo new_market por WS (para el vigia / log)

    def anotar(self, filas):
        """Descarta lo ya visto (ws vs gamma/capture), registra y devuelve solo lo nuevo."""
        nuevas = []
        for f in filas:
            if f["market_id"] in self.vistos:
                continue
            self.vistos[f["market_id"]] = f["slug"]
            nuevas.append(f)
        return nuevas


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
    return rellenar_huecos({r["slug"] for r in mk.values()})


async def sesion(est):
    async with websockets.connect(WS_URL, ping_interval=20, ping_timeout=20, open_timeout=10, max_queue=None) as ws:
        await ws.send(json.dumps({"type": "market", "assets_ids": [], "custom_feature_enabled": True}))
        _log("WS conectado, escuchando new_market")
        est.ult_msg = t_ping = t_stat = time.time()
        loop = asyncio.get_running_loop()
        fut = None
        while not est.parar:
            ahora = time.time()
            if fut is None and ahora - est.ult_relleno >= RELLENO_PERIODICO_S and ahora >= est.pausa_hasta:
                est.ult_relleno = ahora
                fut = loop.run_in_executor(None, lambda: _relleno_sync(est))
            if fut is not None and fut.done():
                filas = []
                try:
                    filas, c = fut.result()
                    nuevas = est.anotar(filas)               # el WS pudo traerlos mientras tanto
                    if nuevas:
                        U.escribir(nuevas)
                    if c["abortado_429"]:
                        est.pausa_hasta = U.pausa_tras_429(datetime.now(timezone.utc))
                        _log(f"relleno gamma: 429, sin gamma hasta {datetime.fromtimestamp(est.pausa_hasta, timezone.utc):%H:%M:%S}Z")
                    if c["filas"] or c["errores"] or c["abortado_429"]:
                        _log(f"relleno gamma: {c} (nuevas {len(nuevas)})")
                except OSError as ex:
                    _log(f"relleno gamma: no se pudo escribir ({ex}); se reintenta")
                    for f in filas:
                        est.vistos.pop(f["market_id"], None)  # no darlos por vistos: el siguiente relleno los reintenta
                except Exception as ex:
                    _log(f"relleno gamma fallo: {type(ex).__name__}: {ex}")
                fut = None
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
                    for f in nuevas:
                        est.vistos.pop(f["market_id"], None)
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
    _log(f"cierre limpio (new_market recibidos esta ejecucion: {sum(est.total.values())})")


if __name__ == "__main__":
    asyncio.run(main())
