#!/usr/bin/env python3
"""cancel_evidencia.py — registro de EVIDENCIA DE CANCELACIÓN de las órdenes propias de la Sonda/B. SOLO REGISTRO: no decide, no envía, no firma.

Qué guarda (JSONL diario, append-only, una línea = un evento con `eid` estable para deduplicar):
  alta         t_envio/t_ack del POST de cada puja (ancla de reloj para el exchange) + oid, token, precio.
  intencion    hora (ms, reloj propio) en que la Sonda decide cancelar una puja + estado del libro WS en ese instante (nivel propio, top-5 bid/ask).
  cancel_try   CADA llamada a cli.cancel_order: t_pre (justo antes de llamar), t_resp (justo al volver), resultado (canceled / not_canceled con su
               motivo / excepción con status). Se envuelve el método del cliente (valor devuelto y excepciones pasan intactos).
  user_trade   evento `trade` del canal de USUARIO del CLOB WS: hora del exchange, hora de RECEPCIÓN, id, estado (MATCHED/MINED/CONFIRMED/FAILED),
               order_id, rol maker/taker, precio, tamaño. fuente='ws' (tiempo real) o 'rest' (backfill tras un hueco: sin hora de recepción válida).
  user_order   evento `order` (PLACEMENT/UPDATE/CANCELLATION) con hora del exchange: ancla directa de la cancelación efectiva.
  rest_orden   get_order de las órdenes recientes tras una reconexión (size_matched/status): cierra huecos del WS.
  ws_estado, mercado, muestra, latido   cobertura del canal, conditionId resuelto por token, muestras crudas del esquema real, contadores de salud.
El postproceso (cancel_postproceso.py) une todo y clasifica cada relleno como antes/después de la intención SIN estimar bloque-2,2 s.

Garantías de diseño: (1) FAIL-OPEN hacia la operación: cualquier fallo del registro se traga y se cuenta; jamás se propaga a la Sonda ni retrasa una
cancelación: en el camino crítico solo se toma la hora y se encolan datos CRUDOS (copia O(n) en C, sin ordenar ni serializar); todo el formato y la
escritura va en el hilo escritor, con cola acotada (si se llena se descarta y se cuenta). (2) No cambia ninguna decisión. (3) Sin órdenes: no importa ni
llama a post_order/crear/firmar; el canal de usuario y el backfill son de SOLO LECTURA y solo arrancan con env.real y credenciales ya cargadas en el
cliente (no lee .env). (4) Los campos owner/api key se eliminan del crudo antes de escribir. (5) SIGKILL/reinicio: la línea parcial se repara al reabrir;
el lector tolera líneas corruptas y deduplica por eid."""
import atexit
import collections
import functools
import gzip
import hashlib
import heapq
import inspect
import itertools
import json
import os
import queue
import re
import shutil
import subprocess
import sys
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

REG_VER = "ce2"
DIR_POR_DEFECTO = Path("/root/polymarket-research-datalogs/sonda1/cancel_evid")
BASE = "cancel_evid"
WS_USER_URL = "wss://ws-subscriptions-clob.polymarket.com/ws/user"
CLOB_MARKETS_POR_TOKEN = "https://clob.polymarket.com/markets-by-token/{tok}"      # público, sin credenciales (verificado 03-Nov: devuelve condition_id)
GAMMA_MARKETS = "https://gamma-api.polymarket.com/markets"                          # fallback público: ?clob_token_ids=
PING_S = 10.0
COLA_MAX = 20000
LIBRE_MIN_BYTES = 1024 ** 3
LATIDO_S = 60.0
OIDS_MAX = 5000
N_TRY_MAX = 2000
MARKETS_MAX = 24
MUESTRAS_POR_TIPO = 3
BACKFILL_VENTANA_S = 1200
SUB_MARGEN_MS = 1000
GATE_ESPERA_S = 6.0                 # el POST real espera como mucho esto a que el canal de usuario esté suscrito+confirmado; si no, NO se envía (fail-closed)
GATE_SIN_ESPERA_TRAS = 2            # tras N bloqueos SEGUIDOS el canal se da por caído: el gate ya no espera (no bloquea el bucle principal 6 s por puja), solo evalúa
GATE_REINTENTO_LARGO_S = 30.0       # canal "caído" (>=N seguidos): cada tanto se hace UN intento con espera completa para detectar la recuperación (sin él, el bloqueo sería perpetuo)
GATE_DEDUP_S = 20.0                 # bloqueos del MISMO token dentro de esta ventana = un solo intento de envío (no se cuentan por gate)
GATE_AVISO_CADA = 3                 # aviso (Telegram) al llegar a N bloqueos seguidos y luego cada N*GATE_AVISO_CADA
ERR_FRAME_MAX = 5                   # frames de error seguidos tras los que se abandona el canal (backoff 1->30 s entre reintentos)
PING_CONF_S = 1.0                   # hasta que la sesión esté confirmada se hace PING cada 1 s (no cada PING_S=10 s: sería > GATE_ESPERA_S)
GATE_RX_MAX_MS = 25000              # el canal debe haber recibido algo (PONG/evento) hace menos de esto (PING cada PING_S=10 s)
BACKFILL_COOLDOWN_S = 30            # mínimo entre backfills (anti-429: nunca competir con POST/DELETE de la Sonda)
BACKFILL_MAX_LLAMADAS_H = 120       # tope de llamadas REST de backfill por hora
BACKFILL_MAX_ORDENES = 15           # get_order por backfill
BACKFILL_PAUSA_429_S = 900          # tras un 429, backfill desactivado este tiempo
BACKFILL_VIDA_ORDEN_S = 420         # una puja (mercado de 5 min) no puede seguir viva mucho más
MBB_BACKOFF_INI_S = 2.0
MBB_BACKOFF_MAX_S = 60.0
RESOLVER_BACKOFF_S = (1.0, 2.0, 4.0)
RESOLVER_REPEDIR_S = 5.0
RETENCION_DIAS = 30
MANT_RETRASO_S = 60                 # el mantenimiento (gz/retención) corre al minuto de arrancar y luego una vez por día UTC
GZ_DESPUES_DIAS = 2                 # hoy y ayer siguen en claro (pueden llegar eventos tardíos)
CAMPOS_PRIVADOS = {"owner", "trade_owner", "order_owner", "apiKey", "api_key", "secret", "passphrase", "auth"}


def ahora_ms():
    return time.time_ns() // 1_000_000


def _dia(t_ms):
    return datetime.fromtimestamp(t_ms / 1000, timezone.utc).strftime("%Y-%m-%d")


def _log(msg):
    try:
        print(f"[{datetime.now(timezone.utc):%H:%M:%S}] cancel_evidencia: {msg}", file=sys.stderr, flush=True)
    except Exception:
        pass


def eid_de(*clave):
    return hashlib.sha1(json.dumps(clave, sort_keys=True, default=str).encode()).hexdigest()[:16]


def ts_a_ms(x):
    """(ms, unidad) de un timestamp del exchange: número < 1e11 se toma como SEGUNDOS (resolución 1 s: la tabla lo marca); None si ilegible."""
    try:
        v = float(x)
    except (TypeError, ValueError):
        return None, None
    if v <= 0:
        return None, None
    return (int(v * 1000), "s") if v < 1e11 else (int(v), "ms")


def limpiar(obj):
    """Copia sin campos privados (owner, claves, auth), recursiva."""
    if isinstance(obj, dict):
        return {k: limpiar(v) for k, v in obj.items() if k not in CAMPOS_PRIVADOS}
    if isinstance(obj, list):
        return [limpiar(v) for v in obj]
    return obj


def _f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


# ───────────────────────── escritor ─────────────────────────
_TL = threading.local()            # tok/env de la puja que está dentro de Puja.lanzar (para el re-chequeo atómico justo antes de env.enviar)


class EnvioBloqueado(Exception):
    """Re-chequeo final del gate fallido justo antes del POST. Se hace pasar por un rechazo 4xx 'post-only' (mercado): sonda1 lo trata como puja no
    enviada, sin contar para el kill de errores de API."""
    status_code = 400

    def __init__(self, motivo):
        super().__init__(f"cancel_evid gate: post-only NO enviado ({motivo})")
        self.error_msg = str(self)


RAIZ_PROYECTO = "/root/polymarket-research"
_ALERTA_DIR = [None]               # directorio del registro (lo fija Registro): ahí cae ALERTA_envio_bloqueado.txt si Telegram falla


def _avisar_telegram(msg):
    """Aviso por shadow_digest.enviar_telegram SIEMPRE en un subproceso del python del sistema (el venv no trae `requests`; así no se toca sys.path ni el
    proceso de la Sonda). Hilo aparte, nunca bloquea. Éxito = código de salida 0 (enviar_telegram devolvió True). Si falla: log + fichero
    ALERTA_envio_bloqueado.txt en el directorio del registro (lo lee vigia_sonda1_registro_auditoria.py)."""
    def _t():
        try:
            r = subprocess.run(["/usr/bin/python3", "-c", "import sys; sys.path.insert(0, sys.argv[1]); from shadow_digest import enviar_telegram; "
                                "sys.exit(0 if enviar_telegram(sys.argv[2], bot='cripto') is True else 3)", RAIZ_PROYECTO, msg],
                               cwd=RAIZ_PROYECTO, capture_output=True, text=True, timeout=60)
            if r.returncode == 0:
                return
            err = f"rc={r.returncode} {r.stderr[-200:]}"
        except BaseException as e:
            err = f"{type(e).__name__}: {e}"
        _log(f"ALERTA (Telegram fallido: {err}): {msg}")
        try:
            d = Path(_ALERTA_DIR[0] or DIR_POR_DEFECTO)
            d.mkdir(parents=True, exist_ok=True)
            with open(d / "ALERTA_envio_bloqueado.txt", "a") as f:
                f.write(f"{datetime.now(timezone.utc).isoformat()} {msg}\n")
        except Exception:
            pass
    threading.Thread(target=_t, daemon=True, name="cancel_evid_aviso").start()


def _tipo_frame(raw):
    """pong | evento (order/trade de usuario) | error (auth/rechazo) | otro. SOLO pong/evento cuentan como tráfico y confirmación.
    No verificado con el servidor real: que el PONG implique que la suscripción ya está procesada, ni el formato exacto de los frames de error de /ws/user."""
    if raw == "PONG":
        return "pong"
    try:
        d = json.loads(raw)
    except Exception:
        return "otro"
    for m in (d if isinstance(d, list) else [d]):
        if not isinstance(m, dict):
            continue
        if m.get("error") or m.get("errorMsg") or m.get("error_msg") or str(m.get("type", "")).lower() == "error" or str(m.get("event_type", "")).lower() == "error":
            return "error"
        if m.get("event_type") in ("order", "trade"):
            return "evento"
    return "otro"


class Escritor:
    """Hilo escritor con cola acotada. Un elemento de la cola es un dict (evento ya formado) o un callable sin argumentos que devuelve una lista de
    dicts (se evalúa EN ESTE HILO: formato, ordenación, sha1 y E/S salen del camino crítico). put() NUNCA bloquea ni lanza. Un fichero por día UTC."""

    def __init__(self, directorio=None, libre_fn=None, latido_s=LATIDO_S, extra_latido=None):
        self.dir = Path(directorio or DIR_POR_DEFECTO)
        self.q = queue.Queue(COLA_MAX)
        self.errores = self.descartados = self.escritos = 0
        self.ultimo_error = None
        self._libre = libre_fn or self._libre_real
        self._fd, self._fd_dia = None, None
        self._parar = threading.Event()
        self.latido_s, self.extra_latido = latido_s, extra_latido
        self._t_latido = time.monotonic()
        self._t_log_error = 0.0
        self._mant_lock = threading.Lock()
        self._ult_mant = None
        self._t_mant = time.monotonic() + MANT_RETRASO_S
        self._h = threading.Thread(target=self._bucle, daemon=True, name="cancel_evid_writer")
        self._h.start()
        atexit.register(self.cerrar)

    def _libre_real(self):
        """Bytes libres. Fail-visible: si no se puede medir ni el directorio ni un ancestro, LANZA (queda contado como error y en el latido)."""
        p = self.dir
        while True:
            try:
                st = os.statvfs(p)
                return st.f_bavail * st.f_frsize
            except OSError:
                if p == p.parent:
                    raise
                p = p.parent

    def put(self, item):
        try:
            self.q.put_nowait(item)
            return True
        except Exception:
            self.descartados += 1
            return False

    def _abrir(self, dia):
        if self._fd is not None and self._fd_dia == dia:
            return self._fd
        if self._fd is not None:
            os.close(self._fd)
            self._fd = None
        self.dir.mkdir(parents=True, exist_ok=True)
        p = self.dir / f"{BASE}_{dia}.jsonl"
        fd = os.open(p, os.O_WRONLY | os.O_APPEND | os.O_CREAT, 0o644)
        try:                                              # reparar línea parcial de un SIGKILL previo: asegurar salto de línea final
            n = os.fstat(fd).st_size
            if n:
                with open(p, "rb") as f:
                    f.seek(n - 1)
                    if f.read(1) != b"\n":
                        os.write(fd, b"\n")
        except Exception:
            self.errores += 1
        self._fd, self._fd_dia = fd, dia
        return fd

    def _escribir(self, ev):
        libre = self._libre()
        if libre is not None and libre < LIBRE_MIN_BYTES:
            raise OSError(f"disco libre {libre} < {LIBRE_MIN_BYTES}: no se escribe")
        ev = dict(ev)
        ev.setdefault("reg_ver", REG_VER)
        fd = self._abrir(_dia(int(ev.get("t_ms") or ahora_ms())))
        data = (json.dumps(ev, sort_keys=True, default=str) + "\n").encode()
        while data:                                       # write puede ser parcial: bucle completo
            n = os.write(fd, data)
            if n <= 0:
                raise OSError("write devolvió 0")
            data = data[n:]
        self.escritos += 1

    def _procesar(self, item):
        evs = item() if callable(item) else [item]
        for ev in (evs or []):
            self._escribir(ev)

    def _error(self, e):
        self.errores += 1
        self.ultimo_error = f"{type(e).__name__}: {e}"[:200]
        if time.monotonic() - self._t_log_error > 60:
            self._t_log_error = time.monotonic()
            _log(f"error de escritura/formato ({self.errores} acumulados): {self.ultimo_error}")

    def _latido(self):
        ev = {"k": "latido", "t_ms": ahora_ms(), "escritos": self.escritos, "errores": self.errores, "descartados": self.descartados,
              "cola": self.q.qsize(), "ultimo_error": self.ultimo_error}
        if self.extra_latido:
            try:
                ev.update(self.extra_latido())
            except Exception:
                pass
        ev["eid"] = eid_de("latido", ev["t_ms"])
        try:
            self._escribir(ev)
        except Exception as e:
            self._error(e)

    def _bucle(self):
        while True:
            try:
                item = self.q.get(timeout=0.2)
            except queue.Empty:
                item = None
                if self._parar.is_set():
                    return
            if item is not None:
                try:
                    self._procesar(item)
                except Exception as e:
                    self._error(e)
                finally:
                    self.q.task_done()
            if time.monotonic() >= self._t_mant and self._ult_mant != _dia(ahora_ms()):
                self._ult_mant = _dia(ahora_ms())
                try:
                    self.mantenimiento()
                except Exception as e:
                    self._error(e)
            if self.latido_s and time.monotonic() - self._t_latido >= self.latido_s:
                self._t_latido = time.monotonic()
                self._latido()

    def mantenimiento(self):
        """gzip de los JSONL de >= GZ_DESPUES_DIAS días (verificado antes de borrar el original) y retención de RETENCION_DIAS (regla 6b). Idempotente."""
        with self._mant_lock:
            hoy = datetime.now(timezone.utc).date()
            for p in sorted(self.dir.glob(f"{BASE}_*.jsonl*")):
                try:
                    d = datetime.strptime(p.name[len(BASE) + 1:len(BASE) + 11], "%Y-%m-%d").date()
                except ValueError:
                    continue
                edad = (hoy - d).days
                if edad > RETENCION_DIAS:
                    p.unlink(missing_ok=True)
                elif edad >= GZ_DESPUES_DIAS and p.suffix == ".jsonl":
                    gz, tmp = p.with_name(p.name + ".gz"), p.with_name(p.name + ".gz.tmp")
                    with open(p, "rb") as f, gzip.open(tmp, "wb") as g:
                        shutil.copyfileobj(f, g)
                    with open(p, "rb") as f, gzip.open(tmp, "rb") as g:                 # verificar antes de borrar
                        if hashlib.sha256(f.read()).digest() != hashlib.sha256(g.read()).digest():
                            tmp.unlink(missing_ok=True)
                            raise OSError(f"gz no coincide: {p.name}")
                    os.replace(tmp, gz)
                    p.unlink(missing_ok=True)

    def vaciar(self, timeout=5.0):
        t0 = time.time()
        while self.q.unfinished_tasks and time.time() - t0 < timeout:
            time.sleep(0.01)
        return not self.q.unfinished_tasks

    def cerrar(self):
        try:
            self.vaciar(3.0)
            self._parar.set()
            if self._fd is not None:
                os.close(self._fd)
                self._fd = None
        except Exception:
            pass


# ───────────────────────── registrador ─────────────────────────
class Registro:
    def __init__(self, escritor, ahora=ahora_ms):
        self.w, self.ahora = escritor, ahora
        self._oids = collections.OrderedDict()             # oid(lower) -> (t_visto_ms, oid original) (LRU acotado)
        self._canc_ok = collections.OrderedDict()          # oids con cancelación confirmada (ya no pueden estar vivas)
        self._lock = threading.Lock()
        self.api_key = None
        self.errores = 0
        self._n_try = collections.OrderedDict()            # SOLO lo toca el hilo escritor (cierres de cancel_try): sin lock
        self._muestras = collections.Counter()
        self.canal = None                                  # CanalUsuario (si existe): para backfill/latido
        self.resolutor = None
        self.avisar = _avisar_telegram                     # inyectable (tests); NUNCA bloquea ni lanza
        self._gl = threading.Lock()
        self._bloq = self._cargar_bloq()                   # contador PERSISTENTE de envíos bloqueados {total, seguidos, ...}
        self.inconsistente = None                          # causa si una reversión quedó a medias: bloquea envíos hasta reinicio
        self.sin_canal = False                             # True si algún env real no pudo asociarse a un canal; se limpia al asociarse
        self._t_largo = 0.0                                # monotonic del último intento largo con el canal "caído"
        self._ult_cont = (None, 0.0)                       # (tok, monotonic) del último bloqueo CONTADO: dedup por intento de envío
        self._ver = self._ver_esc = 0                      # versión del contador: orden de escritura garantizado
        self._wl = threading.Lock()                        # serializa la escritura del contador (fuera de _gl)
        _ALERTA_DIR[0] = getattr(escritor, "dir", None)

    # --- oids propios (acceso desde varios hilos: siempre bajo lock, siempre copia para iterar) ---
    def conocer_oid(self, oid):
        if not oid:
            return
        k = str(oid).lower()
        with self._lock:
            self._oids[k] = (self.ahora(), str(oid))
            self._oids.move_to_end(k)
            while len(self._oids) > OIDS_MAX:
                self._oids.popitem(last=False)

    def oids_snapshot(self, desde_ms=None):
        with self._lock:
            return frozenset(k for k, (t, _) in self._oids.items() if desde_ms is None or t >= desde_ms)

    def oids_recientes(self, desde_ms):
        """oids (grafía ORIGINAL, para REST) vistos desde `desde_ms`, sin cancelación confirmada, del MÁS reciente al más antiguo."""
        with self._lock:
            return [o for t, o in sorted(self._oids.values(), key=lambda x: -x[0]) if t >= desde_ms and o.lower() not in self._canc_ok]

    def _emitir(self, fn):
        try:
            self.w.put(fn)
        except Exception:
            self.errores += 1

    # --- alta de la puja (ancla de reloj: t_envio/t_ack) ---
    def alta(self, puja):
        try:
            t = self.ahora()
            oid = getattr(puja, "oid", None)
            self.conocer_oid(oid)
            tok, t_env = getattr(puja, "tok", None), getattr(puja, "t_envio", None)
            d = dict(oid=oid, slug=getattr(puja, "slug", None), tok=tok, precio=getattr(puja, "precio", None),
                     t_envio_ms=t_env, t_ack_ms=getattr(puja, "t_ack", None), **self._cobertura_ws(tok, t_env))
            clave = d["oid"] if d["oid"] else (d["slug"], d["tok"], d["t_envio_ms"])        # sin oid: slug+token+t_envio (no colisionan)
            self._emitir(lambda: [{"k": "alta", "t_ms": t, "eid": eid_de("alta", clave), **d}])
        except Exception:
            self.errores += 1

    def _cobertura_ws(self, tok, t_env):
        """¿Estaba el canal suscrito a este mercado ANTES del POST? ok | tarde (suscrito <1 s antes o después) | sin_suscripcion | sin_condition | sin_canal.
        Marca explícita de las anclas de PLACEMENT en riesgo; el postproceso solo usa anclas realmente recibidas."""
        try:
            canal = self.canal
            if canal is None:
                return {"ancla_ws": "sin_canal"}
            cond = None
            if self.resolutor is not None:
                cond = self.resolutor.vistos.get(tok)
            if cond is None and canal.modo_markets != "vacio":
                return {"ancla_ws": "sin_condition"}
            t_sub = canal.t_suscrito(cond)
            if t_sub is None:
                return {"ancla_ws": "sin_suscripcion", "cond": cond}
            return {"ancla_ws": "ok" if (t_env is not None and t_sub <= t_env - SUB_MARGEN_MS) else "tarde", "cond": cond, "t_sub_ms": t_sub}
        except Exception:
            return {"ancla_ws": "error"}

    # --- contador persistente de envíos bloqueados ---
    def _ruta_bloq(self):
        try:
            return Path(self.w.dir) / "envio_bloqueado.json"
        except Exception:
            return None

    def _cargar_bloq(self):
        base = {"total": 0, "seguidos": 0, "ultimo_ms": None, "motivo": None}
        try:
            r = self._ruta_bloq()
            if r is not None and r.exists():
                base.update({k: v for k, v in json.loads(r.read_text()).items() if k in ("total", "ultimo_ms", "motivo")})   # `seguidos` NO se hereda: estado rancio de otro proceso
        except Exception:
            pass                                           # ilegible: se parte de cero (el contador solo informa, no decide)
        return base

    def _guardar_bloq(self, copia):
        try:
            r = self._ruta_bloq()
            if r is None:
                return
            v = copia.pop("_v")
            with self._wl:
                if v <= self._ver_esc:                       # un snapshot más viejo nunca pisa a uno más nuevo
                    return
                self._ver_esc = v
                tmp = r.with_suffix(".tmp")
                with open(tmp, "w") as f:
                    json.dump(copia, f)
                    f.flush()
                    os.fsync(f.fileno())
                os.replace(tmp, r)
        except Exception:
            self.errores += 1

    def estado_bloqueos(self):
        with self._gl:
            return dict(self._bloq)

    def _gate_ok(self):
        copia = None
        with self._gl:
            if self._bloq["seguidos"]:
                self._bloq["seguidos"] = 0
                self._ver += 1
                copia = dict(self._bloq, _v=self._ver)
        if copia is not None:
            self._guardar_bloq(copia)

    def _bloqueo(self, tok, motivo, espera_ms, fase):
        mono = time.monotonic()
        copia = n = tot = None
        with self._gl:
            if not (self._ult_cont[0] == tok and mono - self._ult_cont[1] < GATE_DEDUP_S):     # varios gates del MISMO intento de envío = un solo bloqueo
                self._ult_cont = (tok, mono)                 # se refresca SOLO al contar: la ventana de dedup expira y la racha avanza
                self._bloq["total"] += 1
                self._bloq["seguidos"] += 1
                self._bloq["ultimo_ms"], self._bloq["motivo"] = self.ahora(), motivo
                self._ver += 1
                copia = dict(self._bloq, _v=self._ver)
                n, tot = copia["seguidos"], copia["total"]
                if n == GATE_SIN_ESPERA_TRAS:
                    self._t_largo = mono                    # el 1er intento largo periódico llega GATE_REINTENTO_LARGO_S después de darlo por caído
        if copia is not None:
            self._guardar_bloq(copia)                       # fsync FUERA del lock del camino de envío
        try:
            self.evento("envio_bloqueado", tok=tok, motivo=motivo, espera_ms=espera_ms, fase=fase, contado=copia is not None,
                        **({"seguidos": n, "total": tot} if copia is not None else {}))
        except Exception:
            self.errores += 1
        if n is not None and (n == GATE_AVISO_CADA or (n > GATE_AVISO_CADA and n % (GATE_AVISO_CADA * GATE_AVISO_CADA) == 0)):
            try:
                self.avisar(f"Sonda1 registro: {n} envios REALES bloqueados seguidos por el gate de cancel_evidencia (motivo={motivo}, total={tot}). "
                            f"La Sonda NO esta enviando ordenes. Revisar canal de usuario (ver ws_estado / envio_bloqueado.json).")
            except Exception:
                self.errores += 1

    def marcar_inconsistente(self, causa):
        """Reversión a medias: se bloquea todo envío real hasta reiniciar (no se limpia solo) y se avisa UNA vez."""
        if not self.inconsistente:
            self.inconsistente = causa
            _log(f"ESTADO INCONSISTENTE ({causa}): envíos reales bloqueados hasta reinicio")
            try:
                self.avisar(f"Sonda1 registro: estado INCONSISTENTE tras revertir un envio bloqueado ({causa}). Envios reales bloqueados hasta reiniciar la Sonda.")
            except Exception:
                self.errores += 1

    def _canal_de(self, env):
        """Canal ASOCIADO al env (por api_key). Con env real y sin canal asociado => None (sin_canal, fail-closed); sin env (uso legado) => reg.canal."""
        if env is None:
            return self.canal
        c = getattr(env, "_cancel_canal", None)
        if c is None:
            try:
                c = _CANAL_DE.get(env)
            except TypeError:
                c = None
        return c

    def _evaluar(self, canal, tok, primera):
        if canal is None:
            return False, "sin_canal"
        if self.resolutor is None and canal.modo_markets != "vacio":
            return False, "sin_resolutor"
        cond = None
        if self.resolutor is not None:
            if primera:
                self.resolutor.pedir(tok)
            cond = self.resolutor.vistos.get(tok)
        if cond is None and canal.modo_markets != "vacio":
            return False, "sin_condition"
        return canal.listo_para_enviar(cond, self.ahora())

    def gate_envio(self, tok, env=None, espera_s=None, dormir=time.sleep, fase="espera", reset=True):
        """Puerta previa al POST real (fail-closed). Espera (por Condition del canal, no busy-wait) hasta `espera_s` a que EXISTA una sesión concreta que cubre
        el mercado del token, confirmada, con antigüedad >= SUB_MARGEN_MS y con tráfico propio reciente. Tras GATE_SIN_ESPERA_TRAS bloqueos seguidos no espera
        (tope global: un canal caído no retiene el bucle principal). Devuelve (ok, motivo); si no es ok registra `envio_bloqueado` (contador persistente + aviso)."""
        t0 = time.monotonic()
        if espera_s is None:
            espera_s = GATE_ESPERA_S
        with self._gl:
            if self._bloq["seguidos"] >= GATE_SIN_ESPERA_TRAS and espera_s > 0:
                if t0 - self._t_largo >= GATE_REINTENTO_LARGO_S:
                    self._t_largo = t0                       # un intento largo periódico: detecta la recuperación del canal (modo lista: el 1er intento siempre falla)
                else:
                    espera_s = 0.0
        motivo, canal, primera = "sin_canal", self._canal_de(env), True
        try:
            while self.inconsistente is None:
                canal = self._canal_de(env)
                gen = getattr(canal, "_gen", None)
                ok, motivo = self._evaluar(canal, tok, primera)
                primera = False
                if ok:
                    if reset:
                        self._gate_ok()
                    return True, ""
                rest = espera_s - (time.monotonic() - t0)
                if rest <= 0 or motivo in ("sin_canal", "sin_resolutor", "hilo_muerto"):
                    break
                esp = getattr(canal, "esperar", None)
                if esp is None:
                    dormir(0.05)
                else:
                    esp(min(rest, 0.25) if motivo in ("sin_condition", "suscripcion_reciente") else min(rest, 1.0), gen)
        except Exception as e:
            self.errores += 1
            motivo = f"error:{type(e).__name__}"
        if self.inconsistente is not None:
            motivo = "estado_inconsistente"
        self._bloqueo(tok, motivo, int((time.monotonic() - t0) * 1000), fase)
        return False, motivo

    # --- intención (hook de Puja._cancelar): solo hora + copia barata; el resto en el hilo escritor ---
    def intencion(self, puja):
        try:
            t = self.ahora()
            if getattr(puja, "t_cancel", None) is not None:
                return
            oid = getattr(puja, "oid", None)
            self.conocer_oid(oid)
            bids = asks = None
            err = None
            try:
                lib = getattr(puja, "lib", None)
                libro = lib.lib[puja.tok] if lib is not None else None
                if libro:
                    bids, asks = list(libro["bids"].items()), list(libro["asks"].items())    # copia atómica en C (sin Python por nivel)
                vivo = getattr(lib, "vivo_ms", None)
            except Exception as e:
                err, vivo = f"{type(e).__name__}: {e}"[:120], None
            o = getattr(puja, "o", None) or {}
            d = dict(oid=oid, slug=getattr(puja, "slug", None), tok=getattr(puja, "tok", None), precio=getattr(puja, "precio", None),
                     t_envio_ms=getattr(puja, "t_envio", None), t_ack_ms=getattr(puja, "t_ack", None), size=o.get("size"))

            def fmt():
                ev = {"k": "intencion", "t_ms": t, "eid": eid_de("int", oid if oid else (d["slug"], d["tok"], d["t_envio_ms"])), "t_int_ms": t, **d}
                if err:
                    ev["libro_error"] = err
                elif bids is not None:
                    ev["bids_top5"] = [[float(p), float(s)] for p, s in heapq.nlargest(5, ((p, s) for p, s in bids if s))]
                    ev["asks_top5"] = [[float(p), float(s)] for p, s in heapq.nsmallest(5, ((p, s) for p, s in asks if s))]
                    ev["nivel_propio"] = next((float(s) for p, s in bids if d["precio"] is not None and abs(float(p) - float(d["precio"])) < 1e-9), 0.0) if bids else None
                    ev["vivo_ms"] = vivo
                return [ev]
            self._emitir(fmt)
        except Exception:
            self.errores += 1

    # --- cancel_order a nivel de cliente: solo horas + referencias; todo lo demás en el hilo escritor ---
    def cancel_try(self, payload, t_pre, t_resp, resp, exc):
        try:
            oid = getattr(payload, "orderID", None) or (payload.get("orderID") if isinstance(payload, dict) else None)
            self.conocer_oid(oid)

            def fmt():
                n = self._n_try.get(oid, 0) + 1
                self._n_try[oid] = n
                self._n_try.move_to_end(oid)
                while len(self._n_try) > N_TRY_MAX:
                    self._n_try.popitem(last=False)
                canc = no_canc = None
                if isinstance(resp, dict):
                    canc = [str(x) for x in (resp.get("canceled") or [])]
                    nc = resp.get("not_canceled") or {}
                    no_canc = {str(k): str(v)[:200] for k, v in nc.items()} if isinstance(nc, dict) else str(nc)[:200]
                ev = dict(k="cancel_try", t_ms=t_pre, eid=eid_de("try", oid, n, t_pre), oid=oid, intento=n, t_pre_ms=t_pre, t_resp_ms=t_resp,
                          canceled=canc, not_canceled=no_canc)
                if exc is not None:
                    ev.update(excepcion=type(exc).__name__[:60], status=getattr(exc, "status_code", None), mensaje=str(getattr(exc, "error_msg", exc))[:300])
                elif not isinstance(resp, dict):
                    ev["resp_cruda"] = str(resp)[:200]
                if canc and str(oid).lower() in [c.lower() for c in canc]:      # terminal: ya no hace falta el contador de esa orden
                    self._n_try.pop(oid, None)
                    with self._lock:
                        self._canc_ok[str(oid).lower()] = True
                        while len(self._canc_ok) > OIDS_MAX:
                            self._canc_ok.popitem(last=False)
                return [ev]
            self._emitir(fmt)
        except Exception:
            self.errores += 1

    # --- canal de usuario ---
    def usuario(self, msg, t_recv, fuente="ws", sesion=None, seq=None):
        """Convierte un mensaje del canal de usuario en 0..n eventos (en el hilo escritor). Nunca lanza."""
        try:
            mias = self.oids_snapshot()                    # copia bajo lock: el hilo del WS nunca itera el set vivo
            api_key = self.api_key
            et = str(msg.get("event_type") or msg.get("type") or "").lower() if isinstance(msg, dict) else ""
            muestra = None
            if et and fuente == "ws" and self._muestras[et] < MUESTRAS_POR_TIPO:      # el backfill REST no gasta las muestras del esquema WS
                self._muestras[et] += 1
                muestra = limpiar(msg)

            def fmt():
                out = []
                for ev in parsear_usuario(msg, t_recv, mias, api_key, fuente):
                    out.append({**ev, "sesion": sesion, "seq_rx": seq})
                if muestra is not None:
                    out.append({"k": "muestra", "t_ms": t_recv, "eid": eid_de("muestra", et, t_recv), "event_type": et, "crudo": json.dumps(muestra, default=str)[:2000]})
                return out
            self._emitir(fmt)
        except Exception:
            self.errores += 1

    def evento(self, kind, **kw):
        t = self.ahora()
        self._emitir(lambda: [{"k": kind, "t_ms": t, "eid": eid_de(kind, t, sorted(kw.items(), key=lambda kv: kv[0]).__repr__()[:200]), **kw}])

    def estado_ws(self, estado, **kw):
        self.evento("ws_estado", estado=estado, **kw)


def parsear_usuario(msg, t_recv, oids, api_key=None, fuente="ws"):
    """Eventos `trade` y `order` del canal de usuario -> filas. `mine` = order_id en oids propios (o owner == api_key). Esquema documentado de
    Polymarket (trade: id,status,taker_order_id,maker_orders[{order_id,matched_amount,price,owner}],trader_side,timestamp,match_time;
    order: id,type PLACEMENT/UPDATE/CANCELLATION,timestamp,size_matched,price). El esquema REAL se captura en los eventos `muestra`."""
    out = []
    if not isinstance(msg, dict):
        return out
    et = str(msg.get("event_type") or msg.get("type") or "").lower()
    ts, un = ts_a_ms(msg.get("timestamp"))
    mt, _ = ts_a_ms(msg.get("match_time") or msg.get("matchtime"))
    mias = {str(o).lower() for o in oids}

    def mio(oid, owner):
        return (oid is not None and str(oid).lower() in mias) or (api_key is not None and owner is not None and str(owner) == str(api_key))

    if et == "trade":
        tid, st = msg.get("id"), str(msg.get("status") or "").upper()
        base = dict(t_ms=t_recv, t_recv_ms=t_recv, ts_ex_ms=ts, ts_ex_unidad=un, match_ms=mt, trade_id=tid, status=st, side=msg.get("side"),
                    asset_id=msg.get("asset_id"), market=msg.get("market"), taker_order_id=msg.get("taker_order_id"),
                    trader_side=msg.get("trader_side"), tx_hash=msg.get("transaction_hash"), fuente=fuente)
        n = 0
        to = msg.get("taker_order_id")
        if mio(to, msg.get("owner") if str(msg.get("trader_side") or "").upper() == "TAKER" else None):
            out.append({"k": "user_trade", "eid": eid_de("ut", tid, st, to, "taker", fuente), "oid": to, "rol": "taker", "precio": _f(msg.get("price")),
                        "size": _f(msg.get("size")), **base})
            n += 1
        for mo in (msg.get("maker_orders") or []):
            if isinstance(mo, dict) and mio(mo.get("order_id"), mo.get("owner")):
                oid = mo.get("order_id")
                out.append({"k": "user_trade", "eid": eid_de("ut", tid, st, oid, "maker", fuente), "oid": oid, "rol": "maker", "precio": _f(mo.get("price")),
                            "size": _f(mo.get("matched_amount")), **base})
                n += 1
        if n == 0:                                       # no atribuible a una orden conocida: se conserva crudo (fail-visible)
            out.append({"k": "user_trade", "eid": eid_de("ut", tid, st, "sin_oid", fuente), "oid": None, "rol": None, "precio": _f(msg.get("price")),
                        "size": _f(msg.get("size")), "crudo": limpiar(msg), **base})
    elif et == "order":
        oid = msg.get("id")
        out.append({"k": "user_order", "eid": eid_de("uo", oid, msg.get("type"), ts, msg.get("size_matched"), fuente), "t_ms": t_recv, "t_recv_ms": t_recv,
                    "oid": oid, "mine": mio(oid, msg.get("owner") or msg.get("order_owner")), "tipo": str(msg.get("type") or "").upper(),
                    "ts_ex_ms": ts, "ts_ex_unidad": un, "size_matched": _f(msg.get("size_matched")), "original_size": _f(msg.get("original_size")),
                    "precio": _f(msg.get("price")), "asset_id": msg.get("asset_id"), "fuente": fuente})
    return out


# ───────────────────────── envoltorios (parche en memoria, sin editar sonda1.py) ─────────────────────────
def envolver_cancel_cliente(cli, reg):
    """cli.cancel_order(...) -> mismo valor / misma excepción; registra t_pre, t_resp y resultado. Idempotente por marca en el propio método."""
    orig = getattr(cli, "cancel_order", None)
    if orig is None or getattr(orig, "_cancel_evid", False):
        return False

    def cancel_order(*a, **k):
        t0 = reg.ahora()
        resp = exc = None
        try:
            resp = orig(*a, **k)
            return resp
        except BaseException as e:
            exc = e
            raise
        finally:
            try:
                reg.cancel_try(a[0] if a else k.get("payload"), t0, reg.ahora(), resp, exc)
            except Exception:
                pass
    cancel_order._cancel_evid = True
    cli.cancel_order = cancel_order
    return True


def envolver_cancel_seco(env, reg):
    """EnvioSeco no tiene cliente: se envuelve env.cancelar (bool) para que el flujo seco también deje registro (tests/dry-run)."""
    orig = getattr(env, "cancelar", None)
    if orig is None or getattr(orig, "_cancel_evid", False):
        return False

    def cancelar(oid, *a, **k):
        t0 = reg.ahora()
        r = exc = None
        try:
            r = orig(oid, *a, **k)
            return r
        except BaseException as e:
            exc = e
            raise
        finally:
            try:
                reg.cancel_try({"orderID": oid}, t0, reg.ahora(), {"canceled": [oid] if r else [], "not_canceled": {} if r else {oid: "seco"}}, exc)
            except Exception:
                pass
    cancelar._cancel_evid = True
    env.cancelar = cancelar
    return True


def envolver_intencion(clase_puja, reg):
    """Puja._cancelar(self, ahora, kill=True): registra la intención y llama al original con los mismos argumentos. Idempotente."""
    orig = getattr(clase_puja, "_cancelar", None)
    if orig is None or getattr(orig, "_cancel_evid", False):
        return False

    @functools.wraps(orig)
    def _cancelar(self, *a, **k):
        reg.intencion(self)
        return orig(self, *a, **k)
    _cancelar._cancel_evid = True
    clase_puja._cancelar = _cancelar
    return True


def _revertir_intencion(puja, reg, dia0=None):
    """El re-chequeo pre_post bloqueó el POST tras la intención del ledger: sonda1 lo vio como 'rechazo de mercado' (clave 'rechazada', vivas, ordenes_dia).
    Se revierte EN MEMORIA primero y luego se guarda; si algo falla (incluido st.guardar), el estado queda INCONSISTENTE: el gate bloquea todo envío hasta
    reiniciar y se avisa. El evento `post_rechazo` de sonda1 queda en su log con el texto 'cancel_evid gate' (append-only)."""
    try:
        st = getattr(puja, "st", None)
        d = getattr(st, "d", None)
        if d is None:
            raise RuntimeError("sin st.d")
        d["claves"].pop(getattr(puja, "clave", None), None)
        d["vivas"].pop(getattr(puja, "oid", None), None)
        if d.get("dia") == dia0:                                      # si cruzó medianoche el contador ya se reinició: no se decrementa
            d["ordenes_dia"] = max(0, int(d.get("ordenes_dia", 0)) - 1)
        puja.rechazo_mercado = False
        st.guardar()
        try:
            st.evento(tipo="envio_revertido_gate", clave=getattr(puja, "clave", None), oid=getattr(puja, "oid", None))
        except Exception:
            reg.errores += 1
    except Exception as e:
        reg.errores += 1
        reg.marcar_inconsistente(f"{type(e).__name__}: {e}")


def envolver_alta(clase_puja, reg, resolutor=None, gate=False):
    """Puja.lanzar(...) y Puja._adoptar_id(...): al volver, registra el oid propio (alta con t_envio/t_ack) y encola la resolución del mercado.
    El valor devuelto y las excepciones del original pasan intactos."""
    hecho = False
    orig = getattr(clase_puja, "lanzar", None)
    if orig is not None and not getattr(orig, "_cancel_evid", False):
        @functools.wraps(orig)
        def lanzar(self, *a, **k):
            env_ = getattr(self, "env", None)
            tl_puesto = False
            if getattr(env_, "real", True):                               # default fail-closed: si no se sabe, se trata como real
                if gate:
                    ok, _mot = reg.gate_envio(getattr(self, "tok", None), env_, espera_s=0.0, fase="lanzar", reset=False)   # la ESPERA ya ocurrió antes de los prechequeos (ciclo)
                    if not ok:
                        return False
                _TL.tok, _TL.env, _TL.gate, tl_puesto = getattr(self, "tok", None), env_, gate, True    # sin gate también se fija: el envío no es "sin_gate" por azar
            dia0 = getattr(getattr(getattr(self, "st", None), "d", None), "get", lambda *_: None)("dia")
            if resolutor is not None:
                try:
                    resolutor.pedir(getattr(self, "tok", None))
                except Exception:
                    reg.errores += 1
            _TL.bloqueado = False
            bloqueado = False
            try:
                r = orig(self, *a, **k)
            finally:
                bloqueado = tl_puesto and bool(getattr(_TL, "bloqueado", False))
                if tl_puesto:
                    _TL.tok = _TL.env = None
                _TL.bloqueado = False
                if not bloqueado:
                    reg.alta(self)                                      # un envío bloqueado NO es un alta: nada salió
            if bloqueado:
                _revertir_intencion(self, reg, dia0)                     # sonda1 ya había anotado intención/orden/rechazo antes del POST: se deshace
                return False
            if tl_puesto and gate and r is True:
                reg._gate_ok()                                          # solo si el POST salió y hay que hacer polling (True): el canal funciona, se limpia la racha
            return r
        lanzar._cancel_evid = True
        clase_puja.lanzar = lanzar
        hecho = True
    orig2 = getattr(clase_puja, "_adoptar_id", None)
    if orig2 is not None and not getattr(orig2, "_cancel_evid", False):
        @functools.wraps(orig2)
        def _adoptar_id(self, *a, **k):
            r = orig2(self, *a, **k)
            reg.alta(self)
            return r
        _adoptar_id._cancel_evid = True
        clase_puja._adoptar_id = _adoptar_id
        hecho = True
    return hecho


# ───────────────────────── resolución token -> conditionId (REST público, sin credenciales) ─────────────────────────
class Resolutor:
    """Hilo que resuelve el conditionId de cada token (cache) y avisa al canal. REST público. Los reintentos se reencolan con hora de vencimiento
    (heap): el hilo NUNCA duerme con un token pendiente mientras haya otros. Tras un fallo definitivo se puede volver a pedir (pasado RESOLVER_REPEDIR_S)."""

    def __init__(self, reg, resolver_fn=None):
        self.reg, self.canal = reg, None
        self._fn = resolver_fn or self._resolver_http
        self.q = queue.SimpleQueue()
        self.vistos = {}
        self._fallo = {}                                   # tok -> instante (monotonic) del último fallo definitivo
        self._h = threading.Thread(target=self._bucle, daemon=True, name="cancel_evid_resolutor")
        self._h.start()

    def pedir(self, tok):
        if not tok or tok in self.vistos:
            return
        f = self._fallo.get(tok)
        if f is not None and time.monotonic() - f < RESOLVER_REPEDIR_S:
            return
        self._fallo.pop(tok, None)
        self.vistos[tok] = None
        self.q.put((tok, 0))

    @staticmethod
    def _resolver_http(tok):
        import requests
        r = requests.get(CLOB_MARKETS_POR_TOKEN.format(tok=tok), timeout=5)
        if r.status_code == 200 and r.json().get("condition_id"):
            return r.json()["condition_id"]
        r = requests.get(GAMMA_MARKETS, params={"clob_token_ids": tok}, timeout=5)
        j = r.json() if r.status_code == 200 else []
        return j[0].get("conditionId") if isinstance(j, list) and j else None

    def _intentar(self, tok, n, pend):
        try:
            cond = self._fn(tok)
        except Exception as e:
            cond = None
            self.reg.errores += 1
            _log(f"resolver {str(tok)[:10]}…: {type(e).__name__}: {str(e)[:100]}")
        if cond:
            self.vistos[tok] = cond
            self.reg.evento("mercado", tok=tok, condition_id=cond)
            if self.canal is not None:
                self.canal.agregar_mercado(cond)
        elif n < len(RESOLVER_BACKOFF_S):
            heapq.heappush(pend, (time.monotonic() + RESOLVER_BACKOFF_S[n], next(self._seq), tok, n + 1))
        else:
            self.reg.evento("mercado_sin_resolver", tok=tok)
            if self.vistos.get(tok) is None:
                self.vistos.pop(tok, None)                 # permite volver a pedirlo
            self._fallo[tok] = time.monotonic()

    def _bucle(self):
        self._seq = itertools.count()
        pend = []                                          # (vence, seq, tok, n)
        while True:
            ahora = time.monotonic()
            try:
                tok, n = self.q.get(timeout=None if not pend else max(0.0, pend[0][0] - ahora))
                heapq.heappush(pend, (time.monotonic(), next(self._seq), tok, n))
            except queue.Empty:
                pass
            while pend and pend[0][0] <= time.monotonic():
                _, _, tok, n = heapq.heappop(pend)
                self._intentar(tok, n, pend)


# ───────────────────────── canal de usuario (solo lectura) ─────────────────────────
class CanalUsuario:
    """Canal de usuario de SOLO LECTURA. Hilo con su asyncio loop. Una SESIÓN = una conexión /ws/user (auth + markets). Al cambiar el conjunto de mercados
    se abre una sesión NUEVA con la lista completa y, cuando está suscrita (+0,3 s), se cierra la vieja (make-before-break: sin hueco; el solape duplica
    eventos, que se deduplican por eid). Si el servidor no deja abrir la 2ª sesión, se degrada a cerrar y reconectar con backfill. Si cae la única sesión,
    se reconecta con backoff y backfill REST (get_order/get_trades) marcando el hueco (`ws_hueco`). Nunca toca la operación."""

    def __init__(self, reg, creds, markets=(), url=WS_USER_URL, cli=None, backfill=True, esperar_mercados=False, modo_markets="lista"):
        self.reg, self.creds, self.url, self.cli = reg, creds, url, cli
        self.markets = collections.OrderedDict((m, True) for m in markets)
        self._mlock = threading.Lock()
        self._cambio = threading.Event()
        self.modo_markets = modo_markets                      # 'lista' (conditionIds) | 'vacio' (markets=[]: verifica si entrega todo)
        self.esperar_mercados = esperar_mercados and modo_markets != "vacio"
        self.backfill = backfill
        self._parar = threading.Event()
        self.n_msg = self.n_conex = 0
        self.t_caida = None
        self._fin_sesion = {}
        self.una_sesion = False                               # el servidor rechazó una 2ª sesión simultánea: no se vuelve a intentar make-before-break
        self._mbb_espera = MBB_BACKOFF_INI_S
        self._mbb_reintento = None                            # monotonic a partir del cual reintentar un cambio de mercados fallido por error transitorio
        self._bf_ult = None                                   # ms del último backfill (cooldown)
        self._bf_llamadas = collections.deque()               # ms de cada llamada REST de backfill (tope por hora)
        self._bf_pausa_hasta = 0                              # ms hasta los que el backfill está desactivado (429)
        self._t_cond = {}                                     # cond (o '*') -> ms desde que hay cobertura CONTINUA (se conserva al hacer el swap)
        self.suscritos = {}                                   # sesion -> (set(conds), t_sub_ms) de las sesiones vivas
        self._slock = threading.Lock()
        self._cv = threading.Condition(self._slock)          # se notifica en suscripción / confirmación / caída: el gate espera aquí (sin busy-wait)
        self.n_err_frame = 0                                  # frames de error seguidos (se pone a 0 al confirmarse una sesión)
        self.abandonado = False
        self._gen = 0                                         # generación de estado: esperar() no pierde notificaciones entre evaluar y dormir
        self._t_rx_ses = {}                                   # sesion -> ms del último frame recibido EN ESA sesión
        self._seq = itertools.count(1)
        self._t_conf = {}                                     # sesion -> ms del primer frame recibido TRAS suscribir (confirmación: PONG al PING inmediato)
        self.h = threading.Thread(target=self._correr, daemon=True, name="cancel_evid_user_ws")

    def iniciar(self):
        self.h.start()

    def parar(self):
        self._parar.set()

    def agregar_mercado(self, cond):
        if self.modo_markets == "vacio":
            return
        with self._mlock:
            if cond in self.markets:
                return
            self.markets[cond] = True
            while len(self.markets) > MARKETS_MAX:
                self.markets.popitem(last=False)
        self._cambio.set()

    def _lista(self):
        if self.modo_markets == "vacio":
            return []
        with self._mlock:
            return list(self.markets)

    def t_suscrito(self, cond):
        """Instante (ms) desde el que alguna sesión viva está suscrita a `cond` (modo vacío: a todo); None si no lo está."""
        with self._slock:
            return self._t_cond.get("*" if self.modo_markets == "vacio" else cond)

    def _notificar(self):                                     # SIEMPRE con _cv tomado
        self._gen += 1
        self._cv.notify_all()

    def esperar(self, timeout, gen=None):
        """Bloquea hasta una notificación de estado del canal (suscripción, confirmación, caída) o `timeout` s. Si `gen` (leída ANTES de evaluar) ya no
        coincide, hubo un cambio entre evaluar y esperar: vuelve de inmediato."""
        with self._cv:
            if gen is None or self._gen == gen:
                self._cv.wait(timeout)

    def listo_para_enviar(self, cond, ahora_ms_, margen_ms=SUB_MARGEN_MS, rx_max_ms=GATE_RX_MAX_MS):
        """(ok, motivo). Fail-closed: solo True si el hilo vive y existe UNA sesión concreta que cubre `cond` (modo lista: lo contiene; modo vacío: sesión
        con markets=[]), suscrita hace >= margen_ms, CONFIRMADA y con tráfico PROPIO hace <= rx_max_ms. Una sesión vieja/ajena no enmascara a la vigente.
        Tras una caída la sesión desaparece de `suscritos`: bloquea hasta resuscribir."""
        vacio = self.modo_markets == "vacio"
        if not self.h.is_alive():
            return False, "hilo_muerto"
        with self._slock:
            cubren = sorted(((t, n) for n, (cs, t) in self.suscritos.items() if ((not cs) if vacio else (cond is not None and cond in cs))))
            if not cubren:
                return False, "sin_suscripcion"
            mot = "sin_suscripcion"
            for t_sub, n in reversed(cubren):                  # de la más reciente a la más antigua: vale cualquiera que cumpla todo
                if ahora_ms_ - t_sub < margen_ms:
                    mot = "suscripcion_reciente"; continue
                if n not in self._t_conf:
                    mot = "sin_confirmacion"; continue
                rx = self._t_rx_ses.get(n)
                if rx is None or ahora_ms_ - rx > rx_max_ms:
                    mot = "canal_mudo"; continue
                return True, ""
            return False, mot

    def _correr(self):
        import asyncio
        try:
            asyncio.run(self._bucle())
        except Exception as e:
            self.reg.errores += 1
            self.reg.estado_ws("hilo_muerto", e=f"{type(e).__name__}: {e}"[:150])

    @staticmethod
    def _es_429(e):
        return getattr(e, "status_code", None) == 429 or re.search(r"\b429\b", str(e)[:120]) is not None or "too many requests" in str(e).lower()

    def _presupuesto(self, now):
        """Llamadas REST de backfill que aún caben en la hora (tope duro: nunca competir con POST/DELETE de la Sonda por el límite de la API)."""
        while self._bf_llamadas and now - self._bf_llamadas[0] > 3_600_000:
            self._bf_llamadas.popleft()
        return BACKFILL_MAX_LLAMADAS_H - len(self._bf_llamadas)

    def _backfill(self, t_desde, t_hasta):
        """REST de solo lectura (get_order / get_trades) para el hueco [t_desde, t_hasta]. Los trades REST llevan hora en SEGUNDOS y sin recepción válida
        (fuente='rest'): el postproceso los cuenta como cobertura, no como evidencia de orden temporal. Presupuesto: cooldown >=30 s entre backfills,
        tope por hora, <=15 get_order (los más recientes y posiblemente vivos), get_trades acotado al hueco; un 429 apaga el backfill 15 min."""
        cli, reg = self.cli, self.reg
        if cli is None:
            return
        now = reg.ahora()
        motivo = ("pausa_429" if now < self._bf_pausa_hasta else
                  "cooldown" if self._bf_ult is not None and now - self._bf_ult < BACKFILL_COOLDOWN_S * 1000 else
                  "tope_hora" if self._presupuesto(now) <= 1 else None)
        if motivo:
            reg.evento("backfill_omitido", motivo=motivo, t_desde_ms=t_desde, t_hasta_ms=t_hasta)
            return
        self._bf_ult = now
        n_o = n_t = 0
        parado = None
        try:
            # una puja (mercado de 5 min) no puede seguir viva mucho más de BACKFILL_VIDA_ORDEN_S: solo las vistas desde t_desde - esa vida
            for oid in reg.oids_recientes(t_desde - BACKFILL_VIDA_ORDEN_S * 1000)[:BACKFILL_MAX_ORDENES]:
                if self._presupuesto(reg.ahora()) <= 1:
                    parado = "tope_hora"
                    break
                self._bf_llamadas.append(reg.ahora())
                t0 = reg.ahora()
                try:
                    od = cli.get_order(oid)
                except Exception as e:
                    reg.evento("rest_orden", oid=oid, t_pre_ms=t0, t_resp_ms=reg.ahora(), error=f"{type(e).__name__}: {str(e)[:100]}")
                    if self._es_429(e):
                        parado = "429"
                        break
                    continue
                if isinstance(od, dict):
                    n_o += 1
                    reg.evento("rest_orden", oid=oid, t_pre_ms=t0, t_resp_ms=reg.ahora(), size_matched=od.get("size_matched"), status=od.get("status"),
                               created_at=od.get("created_at"), associate_trades=od.get("associate_trades"))
            if parado is None and self._presupuesto(reg.ahora()) >= 1:
                from py_clob_client_v2 import TradeParams
                self._bf_llamadas.append(reg.ahora())
                tr = cli.get_trades(TradeParams(after=max(0, int(t_desde / 1000) - 2), before=int(t_hasta / 1000) + 2))
                for m in (tr if isinstance(tr, list) else []):
                    if isinstance(m, dict):
                        n_t += 1
                        reg.usuario({"event_type": "trade", **m}, reg.ahora(), fuente="rest")          # el REST no trae event_type
        except Exception as e:
            reg.errores += 1
            reg.evento("backfill_error", e=f"{type(e).__name__}: {str(e)[:150]}")
            if self._es_429(e):
                parado = "429"
        if parado == "429":
            self._bf_pausa_hasta = reg.ahora() + BACKFILL_PAUSA_429_S * 1000
            reg.evento("backfill_429", hasta_ms=self._bf_pausa_hasta)
        reg.evento("backfill", t_desde_ms=t_desde, t_hasta_ms=t_hasta, n_ordenes=n_o, n_trades=n_t, parado=parado)

    @staticmethod
    def _clasifica(e):
        """'rechazo' (el servidor dice que no: cierre 1008/4xxx o HTTP 4xx salvo 429) | 'transitorio' (timeout, red, 1011/1006, 429...)."""
        try:
            rc = getattr(e, "rcvd", None)
            code = getattr(rc, "code", None)
            if code == 1008 or (isinstance(code, int) and 4000 <= code <= 4999):
                return "rechazo"
            st = getattr(getattr(e, "response", None), "status_code", None)
            if isinstance(st, int) and 400 <= st < 500 and st != 429:
                return "rechazo"
        except Exception:
            pass
        return "transitorio"

    async def _sesion(self, lista, nombre, parar_ev, listo_ev, info=None):
        """Una conexión. Termina al pedirse parar (limpio) o al fallar (excepción registrada como `caido`)."""
        import asyncio
        import websockets
        try:
            async with websockets.connect(self.url, open_timeout=10, close_timeout=2, max_size=None, ping_interval=None) as ws:
                self.n_conex += 1
                self.reg.estado_ws("conectado", n=self.n_conex, sesion=nombre)
                await ws.send(json.dumps({"auth": {"apiKey": self.creds["apiKey"], "secret": self.creds["secret"],
                                                   "passphrase": self.creds["passphrase"]}, "type": "user", "markets": lista}))
                t_sub = self.reg.ahora()
                with self._cv:
                    self.suscritos[nombre] = (set(lista), t_sub)
                    for c in (lista or ["*"]):
                        self._t_cond.setdefault(c, t_sub)                               # conserva el instante original (SOLO para el ancla ancla_ws; el gate usa la sesión vigente)
                    self._notificar()
                self.reg.estado_ws("suscrito", markets=len(lista), sesion=nombre)
                asyncio.get_running_loop().call_later(0.3, listo_ev.set)           # margen para que el servidor procese la suscripción
                await ws.send("PING")                                              # PING INMEDIATO tras suscribir: su PONG (o cualquier frame posterior) confirma la sesión
                t_ping, ult_ping, confirmada = self.reg.ahora(), time.time(), False
                while not parar_ev.is_set() and not self._parar.is_set():
                    try:
                        raw = await asyncio.wait_for(ws.recv(), timeout=0.3)
                    except asyncio.TimeoutError:
                        raw = None
                    t_recv = self.reg.ahora()
                    if time.time() - ult_ping >= (PING_S if confirmada else PING_CONF_S):     # sin confirmar: PING cada 1 s (el gate espera 6 s)
                        await ws.send("PING")
                        ult_ping = time.time()
                    tipo = _tipo_frame(raw) if raw else None
                    if tipo == "error":                                             # error/auth del servidor: la sesión queda NO confirmada hasta una resuscripción limpia
                        self.n_err_frame += 1
                        self.reg.estado_ws("frame_error", sesion=nombre, crudo=str(raw)[:200], n=self.n_err_frame)
                        if self.n_err_frame >= ERR_FRAME_MAX:                        # tope: se abandona (el gate seguirá bloqueando, hilo_muerto) y se avisa una vez
                            self.abandonado = True
                            self._parar.set()
                            self.reg.avisar(f"Sonda1 registro: canal de usuario abandonado tras {self.n_err_frame} frames de error seguidos (auth?). Envios reales bloqueados.")
                        return "error_frame"                                         # cierra ESTA sesión; el bucle abre una nueva con backoff (fail-closed mientras tanto)
                    elif tipo in ("pong", "evento"):
                        with self._cv:
                            self._t_rx_ses[nombre] = t_recv
                            if not confirmada and t_recv >= t_ping:                  # PONG (o evento de usuario) de ESTA conexión, posterior al PING enviado tras suscribir
                                confirmada = True
                                self.n_err_frame = 0
                                self._t_conf.setdefault(nombre, t_recv)
                                self._notificar()
                    if not raw or raw == "PONG":
                        continue
                    try:
                        datos = json.loads(raw)
                    except ValueError:
                        self.reg.evento("ws_no_json", crudo=str(raw)[:200])
                        continue
                    for m in (datos if isinstance(datos, list) else [datos]):
                        self.n_msg += 1
                        self.reg.usuario(m, t_recv, sesion=nombre, seq=next(self._seq))
            return "parada"
        except Exception as e:
            if info is not None:
                info["tipo"] = self._clasifica(e)
            self.reg.estado_ws("caido", e=f"{type(e).__name__}: {str(e)[:120]}", sesion=nombre)
            return "error"
        finally:
            with self._cv:
                self.suscritos.pop(nombre, None)
                self._t_conf.pop(nombre, None)
                self._t_rx_ses.pop(nombre, None)
                self._notificar()
                vivas = set().union(*[c or {"*"} for c, _ in self.suscritos.values()]) if self.suscritos else set()
                for c in [c for c in self._t_cond if c not in vivas]:
                    del self._t_cond[c]                                                 # cobertura rota: el siguiente t_sub será el nuevo
                self._fin_sesion[nombre] = self.reg.ahora()                      # instante REAL de la caída (el hueco empieza aquí, no cuando el bucle lo nota)

    def _nueva(self, loop, lista, nombre):
        parar_ev, listo_ev, info = __import__("asyncio").Event(), __import__("asyncio").Event(), {}
        return {"nombre": nombre, "lista": lista, "parar": parar_ev, "listo": listo_ev, "info": info,
                "task": loop.create_task(self._sesion(lista, nombre, parar_ev, listo_ev, info))}

    def _purgar(self, ses):
        with self._slock:
            self._fin_sesion.pop(ses["nombre"], None)

    async def _bucle(self):
        import asyncio
        loop = asyncio.get_running_loop()
        actual, n_ses, espera, gap_desde = None, 0, 1.0, None
        while not self._parar.is_set():
            if actual is not None and actual["task"].done():                       # la única sesión viva cayó: hueco hasta reconectar
                with self._slock:
                    gap_desde = gap_desde or self._fin_sesion.pop(actual["nombre"], None) or self.reg.ahora()
                self.t_caida = gap_desde
                actual = None
                await asyncio.sleep(espera)
                espera = min(espera * 2, 30.0)
            if actual is None:
                if self.esperar_mercados and not self._lista():
                    await asyncio.sleep(0.25)
                    continue
                self._cambio.clear()
                n_ses += 1
                actual = self._nueva(loop, self._lista(), f"s{n_ses}")
                t_lanz = self.reg.ahora()
                try:
                    await asyncio.wait_for(asyncio.shield(actual["listo"].wait()), timeout=12)
                except asyncio.TimeoutError:
                    pass
                if actual["listo"].is_set() and not actual["task"].done():
                    espera = 1.0
                    if gap_desde is not None:                                      # reconexión REAL: hueco marcado + backfill
                        t_fin = self.reg.ahora()
                        self.reg.evento("ws_hueco", t_desde_ms=gap_desde, t_hasta_ms=t_fin)
                        if self.backfill and self.cli is not None:
                            loop.run_in_executor(None, self._backfill, max(gap_desde, t_fin - BACKFILL_VENTANA_S * 1000), t_fin)
                        gap_desde = None
                continue
            reintento = self._mbb_reintento is not None and time.monotonic() >= self._mbb_reintento
            if self._cambio.is_set() or reintento:                                  # mercados nuevos: make-before-break
                self._cambio.clear()
                self._mbb_reintento = None
                if self.una_sesion:                                                 # el servidor ya dijo que no admite 2 sesiones: directo a romper-y-reconectar
                    actual["parar"].set()
                    await asyncio.wait({actual["task"]}, timeout=3)
                    self._purgar(actual)
                    self.reg.estado_ws("cambio_con_reconexion", motivo="una_sesion")
                    gap_desde = self.reg.ahora()
                    self.t_caida = gap_desde
                    actual = None
                    continue
                n_ses += 1
                nueva = self._nueva(loop, self._lista(), f"s{n_ses}")
                try:
                    await asyncio.wait_for(asyncio.shield(nueva["listo"].wait()), timeout=5)
                except asyncio.TimeoutError:
                    pass
                if nueva["listo"].is_set() and not nueva["task"].done():
                    vieja, actual = actual, nueva
                    vieja["parar"].set()
                    await asyncio.wait({vieja["task"]}, timeout=3)
                    self._purgar(vieja)
                    self._mbb_espera = MBB_BACKOFF_INI_S
                    self.reg.estado_ws("cambio_sin_hueco", sesion=nueva["nombre"])
                    continue
                if nueva["task"].done() and nueva["info"].get("tipo") == "rechazo":   # rechazo EXPLÍCITO de la 2ª sesión: se recuerda y se degrada
                    self.una_sesion = True
                    self._purgar(nueva)
                    actual["parar"].set()
                    await asyncio.wait({actual["task"]}, timeout=3)
                    self._purgar(actual)
                    self.reg.estado_ws("cambio_con_reconexion", motivo="rechazo_2a_sesion")
                    gap_desde = self.reg.ahora()
                    self.t_caida = gap_desde
                    actual = None
                else:                                                               # timeout / error transitorio: la sesión vieja SIGUE; reintento con backoff
                    nueva["parar"].set()
                    await asyncio.wait({nueva["task"]}, timeout=3)
                    self._purgar(nueva)
                    self.reg.estado_ws("cambio_aplazado", motivo=nueva["info"].get("tipo") or "timeout", espera_s=self._mbb_espera)
                    self._mbb_reintento = time.monotonic() + self._mbb_espera
                    self._mbb_espera = min(self._mbb_espera * 2, MBB_BACKOFF_MAX_S)
                continue
            await asyncio.sleep(0.1)
        for s in ([actual] if actual else []):
            s["parar"].set()
            await asyncio.wait({s["task"]}, timeout=3)


def creds_de_cliente(cli):
    """Credenciales YA cargadas en el cliente (en memoria; no se lee ningún .env). None si no hay."""
    c = getattr(cli, "creds", None)
    if c is None:
        return None
    try:
        return {"apiKey": c.api_key, "secret": c.api_secret, "passphrase": c.api_passphrase}
    except Exception:
        return None


# ───────────────────────── instalación ─────────────────────────
_ESTADO = {"reg": None, "canales": {}, "resolutor": None, "S": None}
_LOCK = threading.Lock()
_ADJUNTOS = __import__("weakref").WeakSet()               # envs ya adjuntados si no admiten atributos (clases con __slots__)


def _ya_adjunto(env):
    if getattr(env, "_cancel_evid", False):
        return True
    try:
        return env in _ADJUNTOS
    except TypeError:
        return False


def _marcar_adjunto(env):
    try:
        env._cancel_evid = True
    except Exception:
        try:
            _ADJUNTOS.add(env)
        except TypeError:
            pass


def _asociar_canal(env, canal, reg=None):
    """Asocia (SIEMPRE sobrescribe: un canal muerto no puede quedar pegado) el canal al env. False + señal explícita (`sin_canal`/env_no_asociable) si no se puede."""
    try:
        env._cancel_canal = canal
        return True
    except Exception:
        pass
    try:
        _CANAL_DE[env] = canal                                   # WeakKeyDictionary: exige weakref
        return True
    except TypeError:
        if reg is not None:
            reg.sin_canal = True
            reg.estado_ws("sin_canal", motivo="env_no_asociable")
        return False


def _canal_muerto(c):
    h = getattr(c, "h", None)
    return h is not None and getattr(h, "ident", None) is not None and not h.is_alive() and not getattr(c, "abandonado", False)   # abandonado: NO se revive


def _nuevo_canal(env, reg, cr, markets, url, resolutor, backfill, modo_markets):
    """Crea el CanalUsuario de esta api_key (bajo _LOCK) y lo registra; el llamador lo inicia FUERA del lock."""
    reg.api_key = cr["apiKey"]
    c = CanalUsuario(reg, cr, markets, url, cli=env.cli, backfill=backfill, esperar_mercados=resolutor is not None,
                     modo_markets=modo_markets or os.environ.get('SONDA1_CANCEL_EVIDENCIA_MARKETS', 'lista'))
    _ESTADO["canales"][cr["apiKey"]] = c
    reg.canal = c
    if resolutor is not None:
        resolutor.canal = c
        for m in set(resolutor.vistos.values()) - {None}:
            c.agregar_mercado(m)
    return c


def _revivir_canal(env, reg, markets, url, resolutor, backfill):
    """Si el hilo del canal asociado a este env murió, crea uno nuevo para su api_key y lo asocia (si no, el gate bloquearía para siempre con hilo_muerto)."""
    c = getattr(env, "_cancel_canal", None)
    if c is None:
        try:
            c = _CANAL_DE.get(env)
        except TypeError:
            c = None
    if c is None:
        c = reg.canal                                            # env sin canal asociado pero con canal del registro (muerto)
    if c is None or not _canal_muerto(c):
        return False
    cr = creds_de_cliente(getattr(env, "cli", None))
    if not cr:
        return False
    with _LOCK:
        actual = _ESTADO["canales"].get(cr["apiKey"])
        if actual is not None and not _canal_muerto(actual):
            nuevo = actual                                       # otro env ya lo revivió
        else:
            nuevo = _nuevo_canal(env, reg, cr, list(getattr(c, "markets", ())) or markets, url, resolutor, backfill, getattr(c, "modo_markets", None))
            actual = None
    if actual is None:
        nuevo.iniciar()
        reg.estado_ws("canal_revivido")
    _asociar_canal(env, nuevo, reg)
    return True


def _tok_de(signed):
    """tokenId de una orden firmada (objeto o dict; con o sin sobre `order`). None si no se encuentra (=> el gate bloquea por sin_condition)."""
    for o in (signed, getattr(signed, "order", None), signed.get("order") if isinstance(signed, dict) else None):
        for nombre in ("tokenId", "token_id"):
            v = o.get(nombre) if isinstance(o, dict) else getattr(o, nombre, None)
            if v:
                return str(v)
    return None


def _envolver_enviar(env, reg):
    """Envío del env (post): RE-CHEQUEO atómico del gate justo antes del POST (sin espera) cuando viene de Puja.lanzar (_TL.env is env); si la sesión cayó entre
    el gate y aquí, NO se envía (EnvioBloqueado). Los envíos que NO pasan por Puja.lanzar (prueba de 0,01 y paquete de sonda1.py) no se gatean: son órdenes
    sueltas, lanzadas a mano, sin ancla de cancelación que proteger; se anota `envio_sin_gate` para que quede auditado."""
    orig = getattr(env, "enviar", None)
    if orig is None or getattr(orig, "_cancel_evid", False):
        return

    @functools.wraps(orig)
    def enviar(signed, *a, **k):
        if getattr(_TL, "env", None) is env:
            if getattr(_TL, "gate", False):
                ok, mot = reg.gate_envio(getattr(_TL, "tok", None), env, espera_s=0.0, fase="pre_post", reset=False)
                if not ok:
                    _TL.bloqueado = True
                    raise EnvioBloqueado(mot)
        else:                                                                          # prueba de 0,01 / paquete de sonda1 (no pasan por Puja.lanzar): mismo gate, espera corta
            tok = _tok_de(signed)
            if tok is not None and reg.resolutor is not None:
                try:
                    reg.resolutor.pedir(tok)
                except Exception:
                    reg.errores += 1
            ok, mot = reg.gate_envio(tok, env, espera_s=2.0, fase="pre_post_suelto", reset=False)
            if not ok:
                raise EnvioBloqueado(mot)
        return orig(signed, *a, **k)
    enviar._cancel_evid = True
    try:
        env.enviar = enviar
    except Exception:
        reg.errores += 1


_CANAL_DE = __import__("weakref").WeakKeyDictionary()


def adjuntar_env(env, reg, markets=(), canal=True, url=WS_USER_URL, resolutor=None, backfill=True, modo_markets=None):
    """Idempotente por OBJETO env (marca en el objeto o WeakSet, no id()). Real: envuelve cli.cancel_order y arranca el canal de usuario (solo lectura,
    uno por api_key). Seco: envuelve env.cancelar, sin red."""
    with _LOCK:
        if _ya_adjunto(env):
            return False
    try:                                                   # la marca se pone SOLO al terminar la instalación (si falla, el siguiente ciclo la reintenta; todo es idempotente)
        if getattr(env, "real", False) and getattr(env, "cli", None) is not None:
            envolver_cancel_cliente(env.cli, reg)
            cr = creds_de_cliente(env.cli)
            _envolver_enviar(env, reg)
            if canal and cr:
                with _LOCK:
                    c = _ESTADO["canales"].get(cr["apiKey"])
                    ya = c is not None and not _canal_muerto(c)                       # 2º env con la misma api_key: comparte canal (queda ASOCIADO a este env)
                    if not ya:
                        c = _nuevo_canal(env, reg, cr, markets, url, resolutor, backfill, modo_markets)
                if _asociar_canal(env, c, reg):
                    reg.sin_canal = False                                             # canal asociado: se limpia el estado
                if reg.canal is None:
                    reg.canal = c
                if not ya:
                    c.iniciar()
            elif canal and not cr:
                reg.estado_ws("sin_credenciales")
                reg.estado_ws("sin_canal", motivo="sin_credenciales")                 # estado explícito: el gate bloqueará y avisará (no es silencio)
                reg.sin_canal = True
        else:
            envolver_cancel_seco(env, reg)
            if getattr(env, "real", False):
                _envolver_enviar(env, reg)                                            # real sin cliente: también gateado
        with _LOCK:
            _marcar_adjunto(env)
        return True
    except Exception:
        reg.errores += 1
        return False


def _envolver_init(clase, reg, **kw):
    """Clase de env (EnvioReal/EnvioSeco): tras __init__ adjunta el env (así se cubren también las cancelaciones de arranque/reconciliación, que ocurren
    antes del primer ciclo_mercado). Idempotente; si el original falla, la excepción pasa intacta."""
    orig = getattr(clase, "__init__", None)
    if orig is None or getattr(orig, "_cancel_evid", False):
        return False

    @functools.wraps(orig)
    def __init__(self, *a, **k):
        orig(self, *a, **k)
        try:
            adjuntar_env(self, reg, **kw)
        except Exception:
            reg.errores += 1
    __init__._cancel_evid = True
    clase.__init__ = __init__
    return True


def _saltar(a, k, ba, reg, motivo):
    """Rastro de un ciclo saltado por el gate: SIEMPRE log; fila en el skip_csv de sonda1 (localizado por nombre o, si la firma no se pudo enlazar, por forma)."""
    slug = ba.get("slug")
    skip = ba.get("skip_csv") or next((v for v in (*a, *k.values()) if hasattr(v, "fila")), None)
    try:
        skip.fila({"dia": f"{datetime.now(timezone.utc):%Y-%m-%d}", "t_ms": ahora_ms(), "slug": slug, "motivo": motivo})
    except Exception:
        reg.errores += 1
        motivo += " (SIN fila en skip_csv)"
    _log(f"salto {slug}: {motivo}")
    return (None, None)                                           # lo mismo que devuelve el `saltar` de sonda1 (tupla de dos None)


def instalar(S, directorio=None, markets=None, canal=True, url=WS_USER_URL, resolver_fn=None, backfill=True):
    """Engancha el registro a `sonda1` (módulo S): Puja._cancelar (intención), Puja.lanzar/_adoptar_id (alta + oid propio + mercado a resolver),
    EnvioReal/EnvioSeco.__init__ (adjunta el env nada más crearse) y ciclo_mercado (respaldo: adjunta el env si se creó antes de instalar y pide el
    conditionId del token). Todo fail-open e idempotente. Sin SONDA1_CANCEL_EVIDENCIA=1 NO se instala (lo decide quien llama, ver LEEME_FASE2.txt)."""
    with _LOCK:
        if getattr(S, "_cancel_evid_instalado", False):
            return _ESTADO["reg"]
        S._cancel_evid_instalado = True
        if _ESTADO["reg"] is not None and directorio and Path(directorio) != _ESTADO["reg"].w.dir:
            _log(f"instalar: directorio {directorio} IGNORADO (el registro de este proceso ya escribe en {_ESTADO['reg'].w.dir})")
        if _ESTADO["reg"] is None:
            w = Escritor(directorio or os.environ.get("SONDA1_CANCEL_EVIDENCIA_DIR") or DIR_POR_DEFECTO)
            _ESTADO["reg"] = Registro(w)
            w.extra_latido = lambda: {"reg_errores": _ESTADO["reg"].errores, "oids": len(_ESTADO["reg"]._oids),
                                      "envio_bloqueado": _ESTADO["reg"].estado_bloqueos(), "sin_canal": bool(getattr(_ESTADO["reg"], "sin_canal", False)),
                                      **({"ws_msgs": _ESTADO["reg"].canal.n_msg, "ws_conex": _ESTADO["reg"].canal.n_conex} if _ESTADO["reg"].canal else {})}
        reg = _ESTADO["reg"]
        if _ESTADO["resolutor"] is None and canal:
            _ESTADO["resolutor"] = Resolutor(reg, resolver_fn)
            reg.resolutor = _ESTADO["resolutor"]
    res = _ESTADO["resolutor"]
    envolver_intencion(S.Puja, reg)
    gate_ciclo = True                                      # SIEMPRE: con env real y sin canal/resolutor el gate BLOQUEA (sin_canal/sin_resolutor); solo el seco queda libre
    envolver_alta(S.Puja, reg, res, gate=gate_ciclo)
    for nombre in ("EnvioReal", "EnvioSeco"):
        if hasattr(S, nombre):
            _envolver_init(getattr(S, nombre), reg, markets=markets or (), canal=canal, url=url, resolutor=res, backfill=backfill)
    orig = S.ciclo_mercado
    sig = inspect.signature(orig)

    @functools.wraps(orig)          # inspect.signature sigue __wrapped__: RA.instalar (que usa la firma) sigue funcionando si se instala encima
    def ciclo(*a, **k):
        env, ba = None, {}
        try:
            try:
                ba = sig.bind_partial(*a, **k).arguments
            except TypeError:
                ba = {}
            env = ba.get("env")
            if env is None or not hasattr(env, "cancelar"):          # firma opaca (otro envoltorio debajo): se busca por forma
                env = next((v for v in (*a, *k.values()) if hasattr(v, "cancelar") and hasattr(v, "real")), None)
            if env is not None:
                adjuntar_env(env, reg, markets or (), canal, url, res, backfill)
                if gate_ciclo and getattr(env, "real", True):
                    _revivir_canal(env, reg, markets or (), url, res, backfill)
            toks, idx = ba.get("toks") or [], ba.get("idx")
            tok = toks[idx] if toks and isinstance(idx, int) and 0 <= idx < len(toks) else None     # el token que se PUJA (no toks[0])
            if res is not None and tok is not None:
                res.pedir(tok)
            if gate_ciclo and env is not None and getattr(env, "real", True):      # GATE ANTES de libro/prechequeos/saldo: la espera no deja comprobaciones rancias
                if tok is None:                                                    # sin token válido no hay gate posible: bloqueo explícito, un solo aviso
                    if not getattr(reg, "_aviso_tok", False):
                        reg._aviso_tok = True
                        reg.avisar("Sonda1 registro: ciclo_mercado sin token valido (toks/idx) con env real: envio bloqueado (tok_invalido).")
                    return _saltar(a, k, ba, reg, "envio_bloqueado:tok_invalido")
                ok, mot = reg.gate_envio(tok, env, reset=False)
                if not ok:
                    return _saltar(a, k, ba, reg, f"envio_bloqueado:{mot}")
        except Exception as e:
            reg.errores += 1
            if gate_ciclo and env is not None and getattr(env, "real", True):      # env REAL conocido: fail-closed, con rastro
                return _saltar(a, k, ba, reg, f"gate_error:{type(e).__name__}")
            _log(f"ciclo: excepcion previa al gate ({type(e).__name__}: {e}); env={'desconocido' if env is None else 'no real'}: se sigue "
                 f"(Puja.lanzar vuelve a gatear: sin env se trata como real)")
        return orig(*a, **k)
    S.ciclo_mercado = ciclo
    return reg
