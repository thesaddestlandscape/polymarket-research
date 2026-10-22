#!/usr/bin/env python3
"""h23_shadow_v3r.py -- H23-MAKER-V3 SHADOW con TRANSPORTE ROBUSTO y MULTIMONEDA (22-Oct-2026, misión 5m barato, orden de Javi «TODOS los datos de H23»). DRY-RUN: solo lectura.

NO cambia ninguna decisión: importa `Nucleo` (la lógica) y la regla (h23_regla_v3, hash 3eeff503cf0a75c9) de h23_shadow_v3.py SIN tocarlas (test de equivalencia en test_h23_shadow_v3r.py:
mismas filas que el shadow v3 con el mismo flujo de mensajes). Cambia SOLO el transporte y añade tres cosas:
  (1) LECTOR EN PROCESO HIJO (h23_ws_lector.py), una conexión por TOKEN (--topologia 4; 2 = por mercado; 1 = como v3): el padre puede ir lento (cola no acotada en el hijo) y el
      búfer de envío del servidor por conexión se reparte entre 4. Motivo: 20-22 Oct, 139/152 huecos eran `1013 slow consumer` y solo ~51 % de los pares salían completos (los de más tráfico).
  (2) RELOJ LÓGICO: cada trama lleva la hora de RECEPCIÓN tomada en el read del hijo; los eventos propios (par nuevo, lado, cierre) se ordenan con esas horas (cola con latidos del hijo
      cada 50 ms) => decisiones idénticas aunque el padre vaya retrasado; el retraso de proceso se mide (`lag_*` en la fila ws_pair). Un hueco de UNA conexión limpia solo los libros
      de SUS tokens (las demás siguen vivas) y se mide: caídas, ms de hueco, ms dentro de la ventana de cotización (fila `ws_pair`, por par).
  (3) MULTIMONEDA (--monedas BTC,ETH,SOL,XRP,DOGE,BNB): mismo par 5m/15m, misma regla y brazos A/B; cada fila lleva `coin`. Referencias TWAP60 oficiales por moneda.
  (4) REGISTRO PROPIO DE PARES (--registro-dir): q/t/g/c compactos en ms (formato en h23_pares_lector.py) con foto de estado a C-310 s y snapshots del servidor; fuente SIN los huecos
      silenciosos del registro maker_ms (que no marca caídas ni escribe q al reconectar) para replays de H23. Retención --retencion-registro-dias (def. 7), gz, fuera de git.
Salida de decisión: <salida>/h23_shadow_v3_YYYY-MM-DD.jsonl.gz (retención 14 d, fuera de git) = mismo esquema que v3 (+ `coin`, `tr`="v3r", filas `ws_pair`). Estado = el propio log (reinicio idempotente).
Uso:  nice -n 5 .venv/bin/python -I h23_shadow_v3r.py --salida DIR --monedas BTC [--topologia 4] [--registro-dir DIR] [--minutos N (solo humo, salida distinta de producción)]
      --resumen | --resolver-solo
Lo lanza/registra la sesión principal (screen propuesta en H23_DATOS_COMPLETOS.md). Sin órdenes, sin claves, sin endpoints privados.
"""
import argparse
import asyncio
import gzip
import heapq
import itertools
import json
import os
import pickle
import resource
import signal
import struct
import subprocess
import sys
import threading
import time
from collections import Counter, deque
from datetime import datetime, timedelta, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import h23_regla_v3 as R  # noqa: E402
import h23_shadow_v3 as V3  # noqa: E402

VERSION = 3
SALIDA_DEFECTO = "/root/polymarket-research-datalogs/h23_shadow_v3r"
REGISTRO_DEFECTO = "/mnt/HC_Volume_106538179/h23_pares"
LECTOR = HERE / "h23_ws_lector.py"
GAMMA = V3.GAMMA
ANTES_S = V3.ANTES_S
MONEDAS_TODAS = ("BTC", "ETH", "SOL", "XRP", "DOGE", "BNB")
REG_ANTES_S = 310                 # el registro propio arranca 310 s antes del cierre (foto de estado) y acaba en el cierre
HB_TICK_MS = 1000                 # como v3: tick de tiempo tras 1 s sin mensajes
RSS_MAX_MB = 700.0
ahora_ms = V3.ahora_ms


def particion(topologia, toks):
    """toks = [5u, 5d, 15u, 15d]. 4 = una conexión por token; 2 = por mercado; 1 = todo junto (como v3)."""
    if topologia == 4:
        return [[t] for t in toks]
    if topologia == 2:
        return [toks[:2], toks[2:]]
    return [list(toks)]


# ---------------------------------------------------------------------------------------------------------------------
class Info:
    """Contabilidad de transporte por par."""
    __slots__ = ("coin", "mkt", "c", "grupos", "tok2grp", "caidas", "motivos", "hueco_abierto", "huecos", "n_frames", "lag_max", "lag_sum", "lag_n", "t_conn",
                 "n_c", "reg_idx", "slot_de")

    def __init__(self, coin, mkt, c, grupos):
        self.coin, self.mkt, self.c, self.grupos = coin, mkt, c, grupos
        self.tok2grp = {t: i for i, g in enumerate(grupos) for t in g}
        self.caidas, self.motivos = 0, Counter()
        self.hueco_abierto = {}                     # grp -> t_gap (ms) mientras no llegue el snapshot de TODOS sus tokens
        self.huecos = []                            # [(t_gap, t_ok, grp)]
        self.n_frames = self.lag_max = self.lag_sum = self.lag_n = 0
        self.t_conn = {}
        self.n_c = 0
        self.reg_idx = None
        self.slot_de = {}


class NucleoR(V3.Nucleo):
    """Nucleo de v3 + hueco por grupo + moneda en cada fila + marca de transporte."""

    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
        self.coin_de = {}

    def emit(self, row):
        mkt = row.get("mkt")
        if mkt in self.coin_de:
            row["coin"] = self.coin_de[mkt]
        row["tr"] = "v3r"
        return super().emit(row)

    def gap_grp(self, mkt, grp, toks, t_ms, motivo):
        """Cae SOLO la conexión `grp`: se limpian los libros de SUS tokens (las demás conexiones siguen vivas) y se cancelan las pujas (fail-closed, igual que v1/v3)."""
        p = self.pares.get(mkt)
        if p is None or p.cerrado:
            return
        p.reconex += 1
        self.emit({"k": f"gap|{mkt}|{grp}|{t_ms}", "tipo": "gap", "mkt": mkt, "grp": grp, "r": t_ms, "T": V3._r(p.c - t_ms / 1000.0, 2), "motivo": (motivo or "")[:80]})
        for tk in toks:
            l = p.lib.get(tk)
            if l is not None:
                l.bids, l.asks, l.vivo = {}, {}, False
        self.evaluar(p, t_ms, forzar_causa="gap")


# ---------------------------------------------------------------------------------------------------------------------
# Registro propio de pares (ver h23_pares_lector.py para el formato)
class RegistroPares:
    def __init__(self, d, retencion_dias=7):
        self.d = Path(d)
        self.d.mkdir(parents=True, exist_ok=True)
        self.retencion = retencion_dias
        self.q = deque()
        self.lk = threading.Lock()
        self.parar = threading.Event()
        self.ultimo = {}                            # token -> ultimo top escrito
        self.hilo = threading.Thread(target=self._bucle, daemon=True, name="h23_registro")
        self.hilo.start()
        self.t_ret = 0.0

    def put(self, coin, t_ms, linea):
        with self.lk:
            self.q.append((coin, _dia(t_ms), linea))

    def _vaciar(self):
        with self.lk:
            items, self.q = list(self.q), deque()
        por = {}
        for coin, dia, ln in items:
            por.setdefault((coin, dia), []).append(ln)
        for (coin, dia), lns in por.items():
            blob = gzip.compress(("\n".join(lns) + "\n").encode(), 6)
            with open(self.d / f"h23_pares_{coin}_{dia}.csv.gz", "ab") as f:
                f.write(blob)
                f.flush()
                os.fsync(f.fileno())

    def _bucle(self):
        while not self.parar.wait(5):
            try:
                self._vaciar()
                if time.time() - self.t_ret > 3600:
                    self.t_ret = time.time()
                    self.aplicar_retencion()
            except Exception as e:
                print(f"{datetime.now(timezone.utc).isoformat()} registro: {type(e).__name__}: {e}", file=sys.stderr, flush=True)

    def aplicar_retencion(self):
        lim = (datetime.now(timezone.utc) - timedelta(days=self.retencion)).strftime("%Y-%m-%d")
        for f in self.d.glob("h23_pares_*_????-??-??.csv.gz"):
            if f.name[-17:-7] < lim:
                f.unlink()

    def cerrar(self):
        self.parar.set()
        self.hilo.join(timeout=6)
        self._vaciar()


def _dia(ms):
    return datetime.fromtimestamp(ms / 1000.0, timezone.utc).strftime("%Y-%m-%d")


def _num(x):
    return "" if x is None else (repr(x) if isinstance(x, float) else str(x))


# ---------------------------------------------------------------------------------------------------------------------
class Transporte:
    """Hijo lector + reloj lógico + enrutado de tramas al Nucleo. TODO corre en el bucle asyncio del padre (sin hilos que toquen el Nucleo)."""

    def __init__(self, nuc, topologia=4, registro=None, nice_hijo=-10, lector=None):
        self.nuc, self.topologia, self.reg = nuc, topologia, registro
        self.info = {}                              # mkt5 -> Info
        self.frames = deque()                       # tramas del hijo, en orden de recepción
        self.cmds = []                              # heap (ts, seq, fn, args)
        self.seq = itertools.count()
        self.wm = 0                                 # reloj lógico = hora del último latido/trama procesado
        self.ult_m = 0
        self.ult_tick = 0
        self.proc = None
        self.reader_task = None
        self.nice_hijo = nice_hijo
        self.activos = {}                           # (mkt5, grp) -> (tokens, fin_ms)  (para relanzar el hijo)
        self.lector = lector or [sys.executable, "-I", str(LECTOR), "--hijo"]
        self.lag_global_max = 0
        self.t_frame_wall = ahora_ms()                # hora de pared de la ultima trama leida del pipe (para forzar el reloj si el hijo calla)
        self.stats = nuc.stats
        self.parando = False

    # -- hijo ------------------------------------------------------------------------------------------------------------
    async def lanzar(self):
        def preexec():
            try:
                os.nice(self.nice_hijo)
            except OSError:
                pass
        self.proc = await asyncio.create_subprocess_exec(*self.lector, stdin=asyncio.subprocess.PIPE, stdout=asyncio.subprocess.PIPE,
                                                         stderr=None, preexec_fn=preexec, limit=1 << 22)
        self.reader_task = asyncio.create_task(self._leer())

    async def _enviar(self, obj):
        if self.proc is None or self.proc.stdin is None or self.proc.stdin.is_closing():
            return
        try:
            self.proc.stdin.write((json.dumps(obj) + "\n").encode())
            await self.proc.stdin.drain()
        except (BrokenPipeError, ConnectionResetError):
            pass

    async def _leer(self):
        rd = self.proc.stdout
        try:
            while True:
                hdr = await rd.readexactly(4)
                body = await rd.readexactly(struct.unpack("<I", hdr)[0])
                self.frames.append(pickle.loads(body))
                self.t_frame_wall = ahora_ms()
                self.pump()
        except (asyncio.IncompleteReadError, ConnectionResetError, EOFError):
            pass
        finally:
            self.pump()
            if not self.parando:
                await self._hijo_muerto()

    async def _hijo_muerto(self):
        """El hijo murió: hueco en TODOS los grupos activos (libros de sus tokens fuera hasta el nuevo snapshot) y se relanza + resuscribe."""
        t = ahora_ms()
        self.stats["hijo_relanzado"] += 1
        print(f"{datetime.now(timezone.utc).isoformat()} hijo lector muerto; relanzando", file=sys.stderr, flush=True)
        for (mkt, grp) in list(self.activos):
            self.cmd(self._on_g, t, mkt, grp, "hijo_muerto")
        await asyncio.sleep(0.2)
        await self.lanzar()
        t2 = ahora_ms()
        for (mkt, grp), (toks, fin_ms) in list(self.activos.items()):
            if fin_ms > t2:
                await self._enviar({"op": "sub", "pair": mkt, "grp": grp, "tokens": toks, "fin_ms": fin_ms})
            else:
                self.activos.pop((mkt, grp), None)

    async def parar(self):
        self.parando = True
        await self._enviar({"op": "exit"})
        if self.proc is not None:
            try:
                await asyncio.wait_for(self.proc.wait(), 3)
            except asyncio.TimeoutError:
                self.proc.kill()
        if self.reader_task:
            self.reader_task.cancel()

    # -- eventos propios ordenados con el reloj del hijo ------------------------------------------------------------------------
    def cmd(self, fn, ts, *args):
        heapq.heappush(self.cmds, (ts, next(self.seq), fn, args))
        self.pump()

    def vigilar_reloj(self):
        """Si el hijo lleva > 1,5 s sin tramas (muerto/atascado) los comandos pendientes no pueden esperar al reloj del hijo: se fuerza con la hora de pared (fail-open SOLO para eventos
        propios; las tramas siguen ordenadas)."""
        if self.cmds and ahora_ms() - self.t_frame_wall > 1500:
            self.stats["reloj_forzado"] += 1
            self.wm = max(self.wm, ahora_ms())
            self.pump()

    def pump(self):
        """Procesa tramas y comandos en orden de hora. Un comando de hora ts espera a que el reloj del hijo haya pasado ts (latido <= 50 ms): así no se procesa antes
        ninguna trama recibida antes que él y que aún estuviera en el pipe."""
        fr, cm = self.frames, self.cmds
        while True:
            if cm and (not fr and self.wm >= cm[0][0] or fr and cm[0][0] <= fr[0][1]):
                ts, _, fn, args = heapq.heappop(cm)
                fn(ts, *args)
                continue
            if fr:
                self._trama(fr.popleft())
                continue
            return

    def _trama(self, f):
        kind, t, pair, grp, payload = f
        if t > self.wm:
            self.wm = t
        if kind == "h":
            if t - self.ult_m >= HB_TICK_MS and t - self.ult_tick >= HB_TICK_MS:
                self.ult_tick = t
                self.nuc.tick(t)
            return
        info = self.info.get(pair)
        if kind == "m":
            self.ult_m = t
            if info is not None:
                self._m(info, t, grp, payload)
        elif kind == "p":
            p = self.nuc.pares.get(pair)
            if p is not None:
                self.nuc.vivo(p, t)
        elif kind == "c":
            self._on_c(t, pair, grp, payload)
        elif kind == "g":
            self._on_g(t, pair, grp, payload)
        elif kind == "e":
            print(f"hijo: {payload}", file=sys.stderr, flush=True)

    def _on_c(self, t, mkt, grp, n):
        info = self.info.get(mkt)
        if info is None:
            return
        info.n_c += 1
        info.t_conn.setdefault(grp, t)
        if self.reg is not None and info.reg_idx is not None:
            self.reg.put(info.coin, t, f"c,{info.c},{grp},{t - info.c * 1000}")

    def _on_g(self, t, mkt, grp, motivo):
        info = self.info.get(mkt)
        if info is None or info.coin is None:
            return
        p = self.nuc.pares.get(mkt)
        if p is None or p.cerrado:
            return
        info.caidas += 1
        info.motivos[(motivo or "")[:40]] += 1
        info.hueco_abierto.setdefault(grp, t)
        self.stats["caidas"] += 1
        self.nuc.gap_grp(mkt, grp, info.grupos[grp], t, motivo)
        if self.reg is not None and info.reg_idx is not None:
            self.reg.put(info.coin, t, f"g,{info.c},{grp},{t - info.c * 1000},{(motivo or '')[:40].replace(',', ';')}")

    def _m(self, info, t, grp, raw):
        nuc = self.nuc
        info.n_frames += 1
        lag = ahora_ms() - t
        if lag > info.lag_max:
            info.lag_max = lag
        info.lag_sum += lag
        info.lag_n += 1
        try:
            datos = json.loads(raw)
        except ValueError:
            return
        toks = info.grupos[grp]
        tset = set(toks)
        for msg in (datos if isinstance(datos, list) else [datos]):
            if not isinstance(msg, dict):
                continue
            et = msg.get("event_type")
            try:
                if et == "price_change":
                    ents = [e for e in (msg.get("price_changes") or []) if e.get("asset_id") in tset]
                    if ents:
                        nuc.on_price_change(t, ents)
                        self._rec_q(info, t, msg, {e.get("asset_id") for e in ents}, "p")
                elif et == "last_trade_price" and msg.get("asset_id") in tset:
                    self._rec_t(info, t, msg)
                    nuc.on_trade(msg["asset_id"], t, msg)
                elif et == "book" and msg.get("asset_id") in tset:
                    nuc.on_book(msg["asset_id"], t, msg.get("bids"), msg.get("asks"))
                    self._cerrar_hueco(info, t, grp, msg["asset_id"])
                    self._rec_q(info, t, msg, {msg["asset_id"]}, "b")
            except Exception as e:
                nuc.stats["error_mensaje"] += 1
                if nuc.stats["error_mensaje"] in (1, 10, 100, 1000):
                    nuc.emit({"k": f"error_msg|{t}", "tipo": "error", "r": t, "m": f"{et}: {type(e).__name__}: {str(e)[:80]}"})

    def _cerrar_hueco(self, info, t, grp, token):
        """El hueco de un grupo se cierra cuando TODOS sus tokens han recibido su snapshot posterior a la caída."""
        if grp not in info.hueco_abierto:
            return
        p = self.nuc.pares.get(info.mkt)
        if p is None:
            return
        if all(p.lib[tk].vivo for tk in info.grupos[grp]):
            info.huecos.append((info.hueco_abierto.pop(grp), t, grp))

    # -- registro propio ----------------------------------------------------------------------------------------------------------------
    def _rec_q(self, info, t, msg, tokens, src):
        if self.reg is None or info.reg_idx is None:
            return
        p = self.nuc.pares.get(info.mkt)
        if p is None or t < (info.c - REG_ANTES_S) * 1000 or t > info.c * 1000 + 1000:
            return
        try:
            ev = int(msg.get("timestamp") or t)
        except (TypeError, ValueError):
            ev = t
        for tk in tokens:
            l = p.lib.get(tk)
            if l is None or not l.vivo:
                continue
            bb = max((px for px, s in l.bids.items() if s > 0), default=None)
            ba = min((px for px, s in l.asks.items() if s > 0), default=None)
            top = (bb, ba, l.bids.get(bb) if bb is not None else None, l.asks.get(ba) if ba is not None else None)
            if src == "p" and self.reg.ultimo.get(tk) == top:
                continue
            self.reg.ultimo[tk] = top
            slot = info.slot_de[tk]
            self.reg.put(info.coin, t, f"q,{info.c},{slot},{t - info.c * 1000},{ev - t},{_num(top[0])},{_num(top[1])},{_num(top[2])},{_num(top[3])},{src}")

    def _rec_t(self, info, t, msg):
        if self.reg is None or info.reg_idx is None or t < (info.c - REG_ANTES_S) * 1000 or t > info.c * 1000 + 1000:
            return
        try:
            ev = int(msg.get("timestamp") or t)
        except (TypeError, ValueError):
            ev = t
        slot = info.slot_de.get(msg.get("asset_id"))
        if slot is None:
            return
        self.reg.put(info.coin, t, f"t,{info.c},{slot},{t - info.c * 1000},{ev - t},{msg.get('price')},{msg.get('side')},{msg.get('size')}")

    def foto_estado(self, ts, mkt):
        """A C-310 s: fila q con el estado vigente de cada token (la ventana de cotización empieza a C-298,5 s)."""
        info = self.info.get(mkt)
        p = self.nuc.pares.get(mkt)
        if info is None or p is None or p.cerrado or self.reg is None:
            return
        for tk, slot in info.slot_de.items():
            l = p.lib.get(tk)
            if l is None or not l.vivo:
                continue
            bb = max((px for px, s in l.bids.items() if s > 0), default=None)
            ba = min((px for px, s in l.asks.items() if s > 0), default=None)
            top = (bb, ba, l.bids.get(bb) if bb is not None else None, l.asks.get(ba) if ba is not None else None)
            self.reg.ultimo[tk] = top
            self.reg.put(info.coin, ts, f"q,{info.c},{slot},{ts - info.c * 1000},0,{_num(top[0])},{_num(top[1])},{_num(top[2])},{_num(top[3])},s")

    # -- ciclo de vida del par ------------------------------------------------------------------------------------------------------------
    def abrir_par(self, ts, coin, c, m5, m15):
        p = self.nuc.nuevo_par(c, m5, m15, ts)
        self.nuc.coin_de[m5["id"]] = coin
        toks = [m5["up"], m5["down"], m15["up"], m15["down"]]
        gr = particion(self.topologia, toks)
        info = Info(coin, m5["id"], c, gr)
        self.info[m5["id"]] = info
        return p, info, toks, gr

    def cerrar_par_cmd(self, ts, mkt, abortado):
        """Fila ws_pair + cierre del Nucleo. Se emite ANTES de cerrar para que `ws_pair` y `mercado_fin` salgan juntos."""
        info = self.info.get(mkt)
        p = self.nuc.pares.get(mkt)
        if info is not None and p is not None and not p.cerrado:
            t_ini, t_fin = p.t_ini, p.t_fin
            hz = [(a, b if b is not None else ts, g) for a, b, g in info.huecos] + [(a, ts, g) for g, a in info.hueco_abierto.items()]
            tot = sum(max(0, b - a) for a, b, _ in hz)
            en_v = sum(max(0, min(b, t_fin) - max(a, t_ini)) for a, b, _ in hz)
            self.nuc.emit({"k": f"ws|{mkt}", "tipo": "ws_pair", "mkt": mkt, "cierre": info.c, "r": ts, "topologia": self.topologia, "n_grupos": len(info.grupos),
                           "n_conexiones": info.n_c, "caidas": info.caidas, "motivos": dict(info.motivos), "hueco_ms": tot, "hueco_max_ms": max((b - a for a, b, _ in hz), default=0),
                           "hueco_en_ventana_ms": en_v, "huecos_abiertos_al_cierre": len(info.hueco_abierto), "n_frames": info.n_frames,
                           "lag_max_ms": info.lag_max, "lag_medio_ms": round(info.lag_sum / info.lag_n, 1) if info.lag_n else None, "abortado": abortado})
        self.nuc.cerrar_par(mkt, ts, abortado=abortado)
        self.info.pop(mkt, None)
        for k in [k for k in self.activos if k[0] == mkt]:
            self.activos.pop(k, None)


# ---------------------------------------------------------------------------------------------------------------------
class RefsMon(V3.Refs):
    """TWAP60 oficial por moneda: v[(coin, epoch)] = (valor, hora de lectura | None)."""

    def _linea(self, ln, t_ms):
        c = ln.rstrip("\n").split(",")
        if len(c) < 7 or c[2] != "twap60" or c[6] != "chainlink" or c[1] not in MONEDAS_TODAS:
            return
        try:
            e = int(c[4]) // 1000
            if e % 300:
                return
            with self.lock:
                self.v.setdefault((c[1], e), (float(c[3]), t_ms))
        except ValueError:
            pass

    def get(self, coin, e):
        with self.lock:
            return self.v.get((coin, e))


def restaurar_monedas(dirn, ahora_s, dias=V3.RELEER_DIAS):
    """mkt -> coin desde las filas ya escritas (un reinicio no pierde la moneda de los desenlaces pendientes)."""
    out = {}
    hoy = datetime.fromtimestamp(ahora_s, timezone.utc).date()
    for i in range(dias, -1, -1):
        f = Path(dirn) / f"h23_shadow_v3_{(hoy - timedelta(days=i)).isoformat()}.jsonl.gz"
        if f.exists():
            for row in V3.leer_gz_tolerante(f):
                if row.get("mkt") and row.get("coin"):
                    out[row["mkt"]] = row["coin"]
    return out


def mercado_moneda(coin, marco, ini):
    import requests
    ev = requests.get(f"{GAMMA}/events", params={"slug": f"{coin.lower()}-updown-{marco}-{ini}"}, timeout=5).json()
    if not ev:
        return None
    m = ev[0]["markets"][0]
    out = json.loads(m["outcomes"]) if isinstance(m["outcomes"], str) else m["outcomes"]
    toks = json.loads(m["clobTokenIds"]) if isinstance(m["clobTokenIds"], str) else m["clobTokenIds"]
    if [o.lower() for o in out] != ["up", "down"] or len(toks) != 2:
        raise ValueError(f"{coin}-updown-{marco}-{ini}: outcomes {out} inesperados (fail-closed)")
    return {"id": str(m["id"]), "up": toks[0], "down": toks[1]}


async def gestionar_par(tp, refs, coin, c, m5, m15, parar, registro):
    """Abre el par (comando ordenado), suscribe al hijo, espera refs, y cierra a C+0,5 s."""
    ts0 = ahora_ms()
    box = {}

    def abrir(ts):
        if box.get("cancel"):
            return
        p, info, toks, gr = tp.abrir_par(ts, coin, c, m5, m15)
        slots = {m5["up"]: "0", m5["down"]: "1", m15["up"]: "2", m15["down"]: "3"}
        info.slot_de = slots
        if registro is not None:
            info.reg_idx = c
            registro.put(coin, ts, f"P,{c},{m5['id']},{m15['id']},{m5['up']},{m5['down']},{m15['up']},{m15['down']},{coin},{ts - c * 1000}")
        box["p"], box["info"], box["toks"], box["gr"] = p, info, toks, gr
    tp.cmd(abrir, ts0)
    # esperar a que el comando se ejecute (necesita latidos del hijo)
    for _ in range(400):
        if "p" in box:
            break
        await asyncio.sleep(0.01)
    if "p" not in box:
        box["cancel"] = True
        tp.nuc.stats["par_no_abierto"] += 1
        tp.nuc.emit({"k": f"error|abrir|{coin}|{c}", "tipo": "error", "r": ahora_ms(), "m": f"par {coin} {c} no abierto: el reloj del hijo no avanzo en 4 s"})
        return
    p, info, gr = box["p"], box["info"], box["gr"]
    fin_ms = int(c * 1000) + 500
    for i, g in enumerate(gr):
        tp.activos[(m5["id"], i)] = (g, fin_ms + 2000)
        await tp._enviar({"op": "sub", "pair": m5["id"], "grp": i, "tokens": g, "fin_ms": fin_ms + 2000})
    if registro is not None:
        tp.cmd(tp.foto_estado, int((c - REG_ANTES_S) * 1000), m5["id"])
    lado = {"ok": False}

    def fijar(ts, r15, r5, t_r5):
        tp.nuc.fijar_lado(p, r15, r5, t_r5)

    def sin_refs(ts):
        tp.nuc.sin_refs(p, ts)
    abortado = True
    try:
        while not parar.is_set() and ahora_ms() < p.t_fin and not lado["ok"]:
            r15, r5 = refs.get(coin, c - 900), refs.get(coin, c - 300)
            if r15 and r5:
                lado["ok"] = True
                tp.cmd(fijar, r5[1] if r5[1] else ahora_ms(), r15[0], r5[0], r5[1] if r5[1] else ahora_ms())
                break
            await asyncio.sleep(0.02)
        if not lado["ok"] and not parar.is_set():
            tp.cmd(sin_refs, ahora_ms())
        while ahora_ms() < fin_ms and not parar.is_set():
            await asyncio.sleep(0.05)
        abortado = ahora_ms() < fin_ms - 400
    finally:
        await tp._enviar({"op": "unsub", "pair": m5["id"]})
        done = {"v": False}

        def cerrar(ts):
            tp.cerrar_par_cmd(ts, m5["id"], abortado)
            done["v"] = True
        tp.cmd(cerrar, ahora_ms())
        for _ in range(400):
            if done["v"]:
                break
            await asyncio.sleep(0.01)


async def principal(args, out, nuc, refs, parar, registro):
    loop = asyncio.get_running_loop()
    tp = Transporte(nuc, topologia=args.topologia, registro=registro)
    await tp.lanzar()
    lanzados, tareas, fallos = set(), [], {}
    t_fin = time.time() + args.minutos * 60 if args.minutos else None
    t_latido = t_ret = 0.0
    tr_res = asyncio.create_task(V3.resolvedor(nuc, parar))
    nuc.emit({"k": f"inicio|{ahora_ms()}", "tipo": "inicio", "r": ahora_ms(), "pid": os.getpid(), "minutos": args.minutos, "records": len(nuc.records),
              "emitidos": len(nuc.emitidos), "hash_regla": R.hash_config(), "monedas": args.monedas, "topologia": args.topologia, "registro": bool(registro),
              "config": {k: V3.CFG[k] for k in ("brazos", "mq", "lat_post_ms", "lat_cancel_ms")}})
    while not parar.is_set() and (t_fin is None or time.time() < t_fin):
        ahora = time.time()
        c = (int(ahora // 900) + 1) * 900
        for coin in args.monedas:
            clave = (coin, c)
            if clave in lanzados or not (c - 300 - ANTES_S <= ahora < c) or fallos.get(clave, (0, 0))[1] > ahora:
                continue
            try:
                m5 = await loop.run_in_executor(None, mercado_moneda, coin, "5m", c - 300)
                m15 = await loop.run_in_executor(None, mercado_moneda, coin, "15m", c - 900)
            except Exception as e:
                n = fallos.get(clave, (0, 0))[0] + 1
                fallos[clave] = (n, ahora + min(3 * n, 20))
                nuc.stats["gamma_mercado_error"] += 1
                if n in (1, 5, 20):
                    nuc.emit({"k": f"error|{coin}|{c}|{n}", "tipo": "error", "r": ahora_ms(), "m": f"gamma {coin} {c}: {type(e).__name__}: {str(e)[:80]}"})
            else:
                if not m5 or not m15:
                    fallos[clave] = (1, ahora + 3)
                else:
                    lanzados.add(clave)
                    if f"fin|{m5['id']}" not in nuc.emitidos:
                        tareas.append(asyncio.create_task(gestionar_par(tp, refs, coin, c, m5, m15, parar, registro)))
        tareas = [t for t in tareas if not t.done()]
        tp.vigilar_reloj()
        lanzados = {k for k in lanzados if k[1] >= c - 1800}
        nuc.podar(time.time())
        if ahora - t_latido > 600:
            t_latido = ahora
            rss = V3.rss_mb()
            nuc.emit({"k": f"latido|{ahora_ms()}", "tipo": "latido", "r": ahora_ms(), "rss_mb": V3._r(rss, 1), "vigilando": len(nuc.pares), "records": len(nuc.records),
                      "stats": dict(nuc.stats), "wm_lag_ms": ahora_ms() - tp.wm if tp.wm else None, "frames_pendientes": len(tp.frames)})
            if rss and rss > RSS_MAX_MB:
                print(f"RSS {rss:.0f} MB > {RSS_MAX_MB:.0f}: salgo para que el watchdog reinicie", file=sys.stderr, flush=True)
                parar.set()
        if ahora - t_ret > 3600:
            t_ret = ahora
            V3.aplicar_retencion(args.salida, ahora)
        await asyncio.sleep(0.5)
    parar.set()
    if tareas:
        await asyncio.gather(*tareas, return_exceptions=True)
    await tr_res
    await tp.parar()
    nuc.emit({"k": f"fin_proceso|{ahora_ms()}", "tipo": "fin_proceso", "r": ahora_ms(), "stats": dict(nuc.stats)})


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--salida", default=SALIDA_DEFECTO)
    ap.add_argument("--monedas", default="BTC")
    ap.add_argument("--topologia", type=int, default=4, choices=(1, 2, 4))
    ap.add_argument("--registro-dir", default=None, help="activa el registro propio de pares (q/t/g/c) en este directorio")
    ap.add_argument("--retencion-registro-dias", type=int, default=7)
    ap.add_argument("--minutos", type=float, default=None, help="SOLO prueba de humo (acotada)")
    ap.add_argument("--resolver-solo", action="store_true")
    ap.add_argument("--resumen", action="store_true")
    args = ap.parse_args()
    args.monedas = [m.strip().upper() for m in args.monedas.split(",") if m.strip()]
    for m in args.monedas:
        if m not in MONEDAS_TODAS:
            sys.exit(f"moneda {m} no soportada")
    if args.resumen:
        V3.resumen(args.salida)
        return 0
    if args.minutos and os.path.abspath(args.salida) == SALIDA_DEFECTO:
        sys.exit("--minutos exige --salida distinta de la de produccion (fail-closed)")
    try:
        resource.setrlimit(resource.RLIMIT_AS, (2_500_000_000, 2_500_000_000))
    except (ValueError, OSError):
        pass
    Path(args.salida).mkdir(parents=True, exist_ok=True)
    emitidos, records = V3.restaurar(args.salida, time.time())
    out = V3.Salida(args.salida)
    nuc = NucleoR(out.put, emitidos, records, prueba=True if args.minutos else None)
    nuc.coin_de.update(restaurar_monedas(args.salida, time.time()))
    registro = RegistroPares(args.registro_dir, args.retencion_registro_dias) if args.registro_dir else None
    refs = None if args.resolver_solo else RefsMon()
    parar = asyncio.Event()

    async def corre():
        loop = asyncio.get_running_loop()
        for s in (signal.SIGTERM, signal.SIGINT):
            loop.add_signal_handler(s, parar.set)
        if args.resolver_solo:
            await V3.resolvedor(nuc, parar, una_vez=True)
        else:
            await principal(args, out, nuc, refs, parar, registro)
    print(f"{datetime.now(timezone.utc).isoformat()} h23_shadow_v3r arrancando pid={os.getpid()} salida={args.salida} monedas={args.monedas} topologia={args.topologia} "
          f"registro={args.registro_dir} records={len(records)} emitidos={len(emitidos)} hash_regla={R.hash_config()}", flush=True)
    try:
        asyncio.run(corre())
    finally:
        out.cerrar()
        if registro:
            registro.cerrar()
        if refs:
            refs.parar.set()
    print(f"{datetime.now(timezone.utc).isoformat()} h23_shadow_v3r terminado stats={dict(nuc.stats)}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
