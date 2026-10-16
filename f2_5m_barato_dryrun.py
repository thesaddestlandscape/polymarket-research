#!/usr/bin/env python3
"""f2_5m_barato_dryrun.py — F2 del ejecutor dedicado (diseño informes/ejecutor_baja_latencia_diseno_15oct.md; Javi 16-Oct:
"primero vamos con 1", conectar también a v1). SOLO DRY-RUN: NUNCA envía órdenes (Enviador con dry_run=True fijo; no existe
opción para cambiarlo). Corre las reglas CONGELADAS en VIVO sobre el camino caliente de ejecutor_rapido y deja constancia de
qué habría hecho y en cuánto tiempo, para conciliarlo al día siguiente con los vigías offline (analisis_f2_5m_barato.py).

Reglas (las funciones de decisión se IMPORTAN de los ficheros congelados, no se copian; importar no altera sus hashes):
  v4 (= regla v1 + ejecución multinivel + guarda de libro cruzado + memoria compacta; vigia_5m_barato_forward.py):
     par 5m/15m que cierra en C, lado s por TWAP60 (ref15 = twap60(C-900), ref5 = twap60(C-300), |gap| >= 1 bp);
     SEÑAL si margen(bid15_s, ask5_s) >= 0,05, ningún libro cruzado, (C-300)s+1,5 s <= t < C-10 s; evento = primer instante
     con señal, re-armado tras 2 s sin señal; oficial = primer evento por (cierre, moneda).
  V7 (analisis_5m_barato_disparo15m.py): cada operación del 15m (token s u opuesto), como mucho una cada 100 ms por par;
     p* = p_limite(min(0,99, bid15_s + DELTA)); FOK virtual que casa a t+L si ask5_s(t+L) <= p*; una por (mercado, DELTA, L).
Medición: t_recv del disparador (reloj local, recepción WS PROPIA) -> decisión -> orden prefirmada tomada del Armero (solo
  BTC; resto de monedas detección sin firma) -> Enviador.enviar en dry-run (ms decisión->"envío"). Relleno SIMULADO con el
  libro L2 COMPLETO de nuestro WS a t+L (L = 150/215/355 para v4; 223/355 para V7): acciones <= p_lim recorriendo niveles.
  Además: hora de llegada real de ref5 (la regla offline la supone conocida a +1,5 s) y motivos de no disparo por par.
Salida (regla 6b; KB/día, sin gz): /root/polymarket-research-datalogs/f2_5m_barato/f2_YYYY-MM-DD.jsonl (+ ledger del
  Enviador f2_ledger_<arranque>.jsonl). Retención: manual (pocos MB en un mes).
Uso: nohup python3 f2_5m_barato_dryrun.py [--monedas BTC,ETH,...] [--sin-firma] > logs/f2_5m_barato.log 2>&1 &
NO va en observadores (su cadena de imports reinicia observadores) ni en el watchdog: herramienta de medición manual.
"""
import argparse
import bisect
import heapq
import json
import math
import os
import queue
import sys
import threading
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import requests

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
import ejecutor_rapido as er  # noqa: E402
import vigia_5m_barato_forward as V  # noqa: E402  (regla v4 congelada: margen, p_limite, fee, CONFIG)
import analisis_5m_barato_disparo15m as V7  # noqa: E402  (regla V7 congelada: DELTAS, LATS)

GAMMA = "https://gamma-api.polymarket.com"
PRICES = REPO / "data" / "prices"
OUT = Path("/root/polymarket-research-datalogs/f2_5m_barato")
MONEDAS = ("BTC", "ETH", "SOL", "XRP", "DOGE", "BNB")
LATS_V4 = (150, V.CONFIG["latencia_oficial_ms"], 355)
UMBRAL = V.CONFIG["umbral_margen_neto"]
REARME = V.CONFIG["rearme_ms"]
REF_MS = V.CONFIG["ref_conocible_ms"]
FIN_S = V.CONFIG["fin_margen_s"]
GAP_MIN = V.CONFIG["gap_min_bps"]
DISPARO_MIN_MS = 100
ANTES_S = 60                      # suscribirse al par 60 s antes de abrir el 5m (libro listo y rejilla firmada)
assert REF_MS == 1500 and REARME == 2000 and UMBRAL == 0.05, "la regla v4 congelada cambió: revisar F2"


def utc_dia(t_s=None):
    return datetime.fromtimestamp(t_s or time.time(), timezone.utc).strftime("%Y-%m-%d")


# ───────────────────────────── salida (cola -> hilo escritor, nada de disco en el camino caliente) ─────────────────────
_cola = queue.Queue()


def log(ev):
    ev.setdefault("t_log_ms", er.ahora_ms())
    _cola.put(ev)


def _escritor():
    OUT.mkdir(parents=True, exist_ok=True)
    while True:
        ev = _cola.get()
        try:
            with open(OUT / f"f2_{utc_dia(ev['t_log_ms'] / 1000)}.jsonl", "a") as f:
                f.write(json.dumps(ev, default=str) + "\n")
        except Exception as e:
            print(f"[f2] escritor: {type(e).__name__}: {e}", file=sys.stderr, flush=True)


# ───────────────────────────── referencias TWAP60 (seguimiento del CSV de PolyBolt) ─────────────────────────────
class Refs:
    """twap60 oficial (source=chainlink) en múltiplos de 300 s, con la HORA LOCAL a la que lo leímos."""

    def __init__(self):
        self.v = {}                       # (moneda, e) -> (valor, t_lectura_ms, timestamp_utc del fetcher)
        self.lock = threading.Lock()
        threading.Thread(target=self._seguir, daemon=True, name="refs").start()

    def _linea(self, ln, t_ms):
        c = ln.rstrip("\n").split(",")
        if len(c) < 7 or c[2] != "twap60" or c[6] != "chainlink":
            return
        try:
            e = int(c[4]) // 1000
            if e % 300:
                return
            with self.lock:
                self.v.setdefault((c[1], e), (float(c[3]), t_ms, c[0]))
        except ValueError:
            pass

    def _seguir(self):
        dia, f, pos = None, None, 0
        while True:
            try:
                d = utc_dia()
                if d != dia:
                    if f:
                        for ln in iter(f.readline, ""):     # restos del día anterior
                            if ln.endswith("\n"):
                                self._linea(ln, er.ahora_ms())
                        f.close()
                        f = None
                    p = PRICES / f"polybolt_{d}.csv"
                    if not p.exists():
                        time.sleep(0.2)
                        continue
                    f, dia = open(p), d
                    hist = True                   # histórico del día (ref15 puede ser de hace 10 min): sin hora
                else:
                    hist = False
                while True:
                    pos = f.tell()
                    ln = f.readline()
                    if not ln:
                        break
                    if not ln.endswith("\n"):     # línea a medio escribir: releer luego
                        f.seek(pos)
                        break
                    self._linea(ln, None if hist else er.ahora_ms())
            except Exception as e:
                print(f"[f2] refs: {type(e).__name__}: {e}", file=sys.stderr, flush=True)
                try:
                    f and f.close()
                except Exception:
                    pass
                f, dia = None, None
            time.sleep(0.05)

    def get(self, mo, e):
        with self.lock:
            return self.v.get((mo, e))


# ───────────────────────────── planificador de comprobaciones a t+L (un hilo, montículo) ─────────────────────────────
class Agenda:
    def __init__(self):
        self.h, self.cv, self.n = [], threading.Condition(), 0
        threading.Thread(target=self._bucle, daemon=True, name="agenda").start()

    def en(self, t_ms, fn):
        with self.cv:
            self.n += 1
            heapq.heappush(self.h, (t_ms, self.n, fn))
            self.cv.notify()

    def _bucle(self):
        while True:
            with self.cv:
                while not self.h or self.h[0][0] > er.ahora_ms():
                    self.cv.wait(None if not self.h else max(0.0, (self.h[0][0] - er.ahora_ms()) / 1000))
                _, _, fn = heapq.heappop(self.h)
            try:
                fn()
            except Exception as e:
                print(f"[f2] agenda: {type(e).__name__}: {e}", file=sys.stderr, flush=True)


def relleno(lib, tk, p_lim, acc_obj):
    """Compra virtual contra el libro L2 completo de nuestro WS AHORA: niveles ask <= p_lim hasta acc_obj."""
    if not lib.fresco(tk):
        return {"clase": "UNKNOWN_libro_no_fresco"}
    asks = sorted((p, s) for p, s in lib.lib[tk]["asks"].items() if s > 0)
    top = lib.top.get(tk)
    if not asks:
        return {"clase": "sin_ask", "ask": None}
    falta, coste, por = acc_obj, 0.0, []
    for p, s in asks:
        if p > p_lim + 1e-9 or falta <= 0:
            break
        x = min(falta, s)
        por.append((p, round(x, 3)))
        coste += x * p
        falta -= x
    acc = acc_obj - falta
    bid = top[1] if top else None
    if acc <= 0:
        return {"clase": "no_llena", "ask": asks[0][0], "ask_sz": asks[0][1], "bid": bid}
    return {"clase": "llena" if falta <= 1e-9 else "parcial", "ask": asks[0][0], "ask_sz": asks[0][1], "bid": bid,
            "acciones": round(acc, 3), "precio": round(coste / acc, 5), "niveles": por,
            "pnl_si_gana": round(acc * (1 - coste / acc - V.fee(coste / acc)), 4),
            "pnl_si_pierde": round(-acc * (coste / acc + V.fee(coste / acc)), 4)}


def tam_orden(p):
    """Tamaño de la orden prefirmada a precio p: max(5, 2 €/p) en centésimas (rejilla del CLOB)."""
    return max(V.CONFIG["min_acciones"], math.ceil(V.CONFIG["stake_eur"] / p * 100) / 100)


# ───────────────────────────── un par 5m/15m de una moneda y un cierre ─────────────────────────────
class Par:
    def __init__(self, mo, cie, m5, m15, ctx):
        self.mo, self.cie, self.ctx = mo, cie, ctx
        self.m5, self.m15 = m5, m15                   # dict: id, slug, up, down, tick, neg
        self.s = None                                  # "Up"/"Down" cuando llega ref5
        self.motivos = Counter()
        self.v4 = {"activo": False, "ult": None, "n": 0}
        self.v7_ult, self.v7_hecho, self.v7_intentos = -10 ** 12, set(), Counter()
        self.t_ini, self.t_fin = (cie - 300) * 1000 + REF_MS, (cie - FIN_S) * 1000
        self.toks = [m5["up"], m5["down"], m15["up"], m15["down"]]
        self.lib = er.Libro(self.toks, al_cambiar=self.al_cambiar, al_trade=self.al_trade)
        self.lock = threading.Lock()

    def iniciar(self):
        self.lib.iniciar()
        threading.Thread(target=self._esperar_refs, daemon=True, name=f"refs_{self.mo}_{self.cie}").start()

        return self

    def _esperar_refs(self):
        r15 = None
        while er.ahora_ms() < self.t_fin:
            r15 = r15 or self.ctx.refs.get(self.mo, self.cie - 900)
            r5 = self.ctx.refs.get(self.mo, self.cie - 300)
            if r15 and r5:
                gap = (r5[0] / r15[0] - 1) * 1e4
                ev = {"tipo": "par_refs", "moneda": self.mo, "cierre": self.cie, "ref15": r15[0], "ref5": r5[0],
                      "gap_bps": round(gap, 3), "ref5_leida_ms": r5[1], "ref5_ts_fetcher": r5[2],
                      "ref5_retraso_ms": None if r5[1] is None else r5[1] - (self.cie - 300) * 1000,
                      "mercado_5m": self.m5["id"], "mercado_15m": self.m15["id"]}
                if abs(gap) < GAP_MIN:
                    ev["descartado"] = "gap<min"
                    log(ev)
                    return
                s = "Up" if r15[0] > r5[0] else "Down"
                self.tc = self.m5["up"] if s == "Up" else self.m5["down"]          # 5m lado s (compra)
                self.to = self.m15["up"] if s == "Up" else self.m15["down"]        # 15m lado s (cota)
                self.to_op = self.m15["down"] if s == "Up" else self.m15["up"]
                self.s = s
                ev["lado"] = s
                log(ev)
                return
            time.sleep(0.02)
        log({"tipo": "par_sin_ref", "moneda": self.mo, "cierre": self.cie, "ref15": bool(r15)})

    def claves_rejilla(self):
        """Rejilla COMPLETA 0,01..0,99 del 5m, ordenada por URGENCIA (cerca de p_limite(bid15 + DELTA) primero, si ya hay
        libro): ambos tokens mientras no se conoce s (ref5 llega ~1,3-1,6 s tras abrir), solo el de s después (la mitad
        de firmas a renovar). Se firma en el proceso firmador antes de abrir la ventana; dentro solo se repone."""
        if self.s is None:
            pares = ((self.m5["up"], self.m15["up"]), (self.m5["down"], self.m15["down"]))
        else:
            pares = ((self.tc, self.to),)
        claves = []
        for t5, t15 in pares:
            top = self.lib.top.get(t15)
            centro = [V.p_limite(min(0.99, top[1] + dl)) for dl in (0.0,) + tuple(V7.DELTAS)] \
                if top and top[1] is not None else []
            centro = [c for c in centro if c] or [0.5]
            for p in (round(x / 100, 2) for x in range(1, 100)):
                claves.append((min(abs(p - c) for c in centro), (t5, p, tam_orden(p), "BUY")))
        return [k for _, k in sorted(claves, key=lambda x: x[0])]

    def _ventana(self, t):
        if self.s is None:
            self.motivos["sin_lado_aun"] += 1
            return False
        if not (self.t_ini <= t < self.t_fin):
            return False
        return True

    def _decidir(self, regla, t_evento, p_lim, extra):
        """Camino caliente: orden prefirmada + Enviador en DRY-RUN. Devuelve meta de tiempos."""
        t_dec0 = time.time_ns()
        signed = None
        arm = self.ctx.armero                 # una sola lectura: el hilo principal puede ponerlo a None
        if arm is not None and self.mo == "BTC":
            signed = arm.tomar((self.tc, p_lim, tam_orden(p_lim), "BUY"))
        t_arm = time.time_ns()
        clave = f"{regla}|{self.mo}|{self.cie}|{extra.get('n', '')}|{extra.get('delta', '')}|{t_evento}"
        fut = self.ctx.env.enviar(clave, signed, "FOK", t_evento, inline=self.ctx.inline,
                                  meta={"regla": regla, "moneda": self.mo, "cierre": self.cie, "p_lim": p_lim,
                                        "prefirmada": signed is not None})
        return {"ms_evento_a_decision": round(t_dec0 / 1e6 - t_evento, 3),
                "ms_tomar_firma": round((t_arm - t_dec0) / 1e6, 3), "prefirmada": signed is not None,
                "enviador": fut is not None}

    # ── v4 ──
    def al_cambiar(self, tk, t, top):
        if self.s is None or tk not in (self.tc, self.to) or not self._ventana(t):
            return
        qc, qo = self.lib.top.get(self.tc), self.lib.top.get(self.to)
        with self.lock:
            senal = bool(qc and qo and qc[3] is not None and qo[1] is not None and V.margen(qo[1], qc[3]) >= UMBRAL)
            if senal and ((qo[3] is not None and qo[1] > qo[3]) or (qc[1] is not None and qc[1] > qc[3])):
                self.motivos["senal_descartada_libro_cruzado"] += 1
                senal = False
            if not senal:
                if self.v4["activo"] and t - self.v4["ult"] >= REARME:
                    self.v4["activo"] = False
                return
            self.v4["ult"] = t
            if self.v4["activo"]:
                return
            self.v4["activo"] = True
            self.v4["n"] += 1
            n = self.v4["n"]
        ask0, bid_o = qc[3], qo[1]
        p_lim = V.p_limite(bid_o)
        acc = max(V.CONFIG["min_acciones"], V.CONFIG["stake_eur"] / ask0)
        tiempos = self._decidir("v4", t, p_lim, {"n": n})
        ev = {"tipo": "v4_evento", "moneda": self.mo, "cierre": self.cie, "n": n, "es_primero": n == 1,
              "lado": self.s, "mercado_5m": self.m5["id"], "t_deteccion": t, "resto_s": round(self.cie - t / 1000, 2),
              "ask5_t0": ask0, "ask5_sz_t0": qc[4], "bid15_t0": bid_o, "margen_neto": V.margen(bid_o, ask0),
              "p_lim": p_lim, "acc_obj": round(acc, 3), "disparador": "5m" if tk == self.tc else "15m", **tiempos}
        log(ev)
        for L in LATS_V4:
            self.ctx.agenda.en(t + L, lambda L=L: log({"tipo": "v4_relleno", "moneda": self.mo, "cierre": self.cie,
                                                       "n": n, "L": L, "t_comprobado": er.ahora_ms(),
                                                       **relleno(self.lib, self.tc, p_lim, acc)}))

    # ── V7 ──
    def al_trade(self, tk, t, msg):
        if self.s is None or tk not in (self.to, self.to_op) or not self._ventana(t):
            return
        with self.lock:
            if t - self.v7_ult < DISPARO_MIN_MS:
                return
            self.v7_ult = t
        q15 = self.lib.top.get(self.to)
        if not q15 or q15[1] is None or (q15[3] is not None and q15[1] > q15[3]):
            self.motivos["v7_q15_invalido"] += 1
            return
        for dl in V7.DELTAS:
            p_lim = V.p_limite(min(0.99, q15[1] + dl))
            if p_lim is None:
                continue
            pend = [L for L in V7.LATS if (dl, L) not in self.v7_hecho]
            if not pend:
                continue
            self.v7_intentos[dl] += 1
            tiempos = self._decidir("V7", t, p_lim, {"delta": dl}) if self.v7_intentos[dl] <= 3 else {}
            for L in pend:
                def comprobar(L=L, dl=dl, p_lim=p_lim):
                    if (dl, L) in self.v7_hecho:
                        return
                    q = self.lib.top.get(self.tc)
                    if not q or q[3] is None or q[3] > p_lim + 1e-9 or (q[1] is not None and q[1] > q[3]):
                        return
                    self.v7_hecho.add((dl, L))
                    ask = q[3]
                    acc = min(max(5.0, 2.0 / ask), q[4] or 0)
                    log({"tipo": "v7_casa", "moneda": self.mo, "cierre": self.cie, "mercado_5m": self.m5["id"],
                         "lado": self.s, "delta": dl, "L": L, "t": t, "t_comprobado": er.ahora_ms(),
                         "bid15": q15[1], "p_lim": p_lim, "ask": ask, "acc": round(acc, 3),
                         "intentos_previos": self.v7_intentos[dl] - 1, "disparo_tok": "s" if tk == self.to else "op",
                         **tiempos})
                self.ctx.agenda.en(t + L, comprobar)

    def cerrar(self):
        self.lib.parar()
        log({"tipo": "par_fin", "moneda": self.mo, "cierre": self.cie, "lado": self.s, "v4_eventos": self.v4["n"],
             "v7_intentos": dict(self.v7_intentos), "v7_casadas": sorted(self.v7_hecho), "n_msg_ws": self.lib.n_msg,
             "errores_ws": self.lib.errores[-5:], "motivos": dict(self.motivos)})


# ───────────────────────────── descubrimiento de mercados ─────────────────────────────
def mercado(mo, marco, ini):
    slug = f"{mo.lower()}-updown-{marco}-{ini}"
    ev = requests.get(f"{GAMMA}/events", params={"slug": slug}, timeout=5).json()
    if not ev:
        return None
    m = ev[0]["markets"][0]
    out = json.loads(m["outcomes"]) if isinstance(m["outcomes"], str) else m["outcomes"]
    toks = json.loads(m["clobTokenIds"]) if isinstance(m["clobTokenIds"], str) else m["clobTokenIds"]
    if [o.lower() for o in out] != ["up", "down"] or len(toks) != 2:
        raise ValueError(f"{slug}: outcomes {out} inesperados (fail-closed)")
    return {"id": str(m["id"]), "slug": slug, "up": toks[0], "down": toks[1],
            "tick": str(m.get("orderPriceMinTickSize") or "0.01"), "neg": bool(m.get("negRisk"))}


class Ctx:
    pass


def fijar_cpu(pid, cpus):
    """sched_setaffinity(pid) solo mueve el hilo con TID == pid: se aplica a cada hilo de /proc/<pid>/task.
    Devuelve cuántos hilos no se pudieron fijar (un hilo que desaparece entre listdir y la llamada no cuenta)."""
    fallos = 0
    for tid in os.listdir(f"/proc/{pid}/task"):
        try:
            os.sched_setaffinity(int(tid), cpus)
        except ProcessLookupError:
            pass
        except OSError:
            fallos += 1
    return fallos


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--monedas", default=",".join(MONEDAS))
    ap.add_argument("--sin-firma", action="store_true", help="no prefirmar (sin cliente de la wallet dedicada)")
    ap.add_argument("--horas", type=float, default=0, help="parar tras N horas (0 = indefinido)")
    ap.add_argument("--cpu", type=int, default=None, help="fijar el proceso (libro+decisión+envío) a este núcleo")
    ap.add_argument("--envio-inline", action="store_true", help="enviar desde el hilo que decide (sin traspaso al pool)")
    a = ap.parse_args()
    monedas = [m.strip().upper() for m in a.monedas.split(",") if m.strip()]
    threading.Thread(target=_escritor, daemon=True, name="escritor").start()
    ctx = Ctx()
    ctx.refs, ctx.agenda, ctx.armero, ctx.inline = Refs(), Agenda(), None, a.envio_inline
    cliente = None
    sys.setswitchinterval(0.0005)             # (B) el hilo de envío no espera 5 ms al GIL del hilo del WS
    permitidas = os.sched_getaffinity(0)
    if a.cpu is not None and (a.cpu not in permitidas or len(permitidas) < 2):
        sys.exit(f"--cpu {a.cpu} no disponible (permitidas {sorted(permitidas)})")
    if not a.sin_firma:
        try:
            from medir_cancelacion_delay import cliente_dedicado
            cliente = cliente_dedicado()
            # el hijo fija SUS núcleos (fuera del caliente) antes de importar nada: arranca ya fuera
            ctx.armero = er.ArmeroProceso("medir_cancelacion_delay:cliente_dedicado", "0.01", False,
                                          caducidad_s=100.0, reserva=2, nice=20,
                                          cpus=(permitidas - {a.cpu}) if a.cpu is not None else None)
        except BaseException as e:            # cliente_dedicado usa sys.exit ante credenciales dudosas
            ctx.armero = None
            print(f"[f2] sin firma: {type(e).__name__}: {e}", flush=True)
    if a.cpu is not None:                     # el padre se fija DESPUÉS de lanzar el firmador; hilos nuevos lo heredan
        fallos = fijar_cpu(os.getpid(), {a.cpu})
        if fallos:
            print(f"[f2] afinidad: {fallos} hilos sin fijar", flush=True)
    riesgo = er.Riesgo([lambda: (True, "dry_run")])
    OUT.mkdir(parents=True, exist_ok=True)
    ctx.env = er.Enviador(cliente, OUT / f"f2_ledger_{int(time.time())}.jsonl", riesgo, dry_run=True)
    assert ctx.env.dry_run is True
    log({"tipo": "arranque", "monedas": monedas, "firma": ctx.armero is not None, "pid": os.getpid(),
         "cpu": a.cpu, "nice": os.nice(0), "envio_inline": a.envio_inline, "switchinterval": sys.getswitchinterval(),
         "armero": type(ctx.armero).__name__ if ctx.armero else None,
         "lats_v4": LATS_V4, "v7_deltas": V7.DELTAS, "v7_lats": V7.LATS, "hash_v4": V.hash_config()})
    print(f"[f2] arranque DRY-RUN monedas={monedas} firma={ctx.armero is not None}", flush=True)
    pares, hecho, ultimas_claves = {}, set(), None
    fin = time.time() + a.horas * 3600 if a.horas else None
    while fin is None or time.time() < fin:
        ahora = time.time()
        cie = (int(ahora // 900) + 1) * 900                 # próximo cierre de 15m
        if cie - 300 - ahora <= ANTES_S and cie - FIN_S > ahora:
            for mo in monedas:
                if (mo, cie) in hecho:
                    continue
                hecho.add((mo, cie))
                try:
                    m5, m15 = mercado(mo, "5m", cie - 300), mercado(mo, "15m", cie - 900)
                except Exception as e:
                    log({"tipo": "par_error", "moneda": mo, "cierre": cie, "error": f"{type(e).__name__}: {e}"})
                    continue
                if not m5 or not m15:
                    log({"tipo": "par_sin_mercado", "moneda": mo, "cierre": cie, "m5": bool(m5), "m15": bool(m15)})
                    continue
                pares[(mo, cie)] = Par(mo, cie, m5, m15, ctx).iniciar()
        for k, p in list(pares.items()):
            if time.time() > k[1] + 2:
                p.cerrar()
                del pares[k]
        if ctx.armero and not ctx.armero.vivo():
            muerto, ctx.armero = ctx.armero, None
            log({"tipo": "firmador_muerto", "errores": muerto.sacar_errores()[-5:]})
            print("[f2] firmador muerto: sigo sin firma", flush=True)
            muerto.parar()                    # pipe, proceso y hilos: nada huérfano
        if ctx.armero:
            llave = tuple(sorted((k, pares[k].s) for k in pares if k[0] == "BTC"))   # cambia al abrir/cerrar o saber s
            if llave != ultimas_claves:       # la rejilla solo cambia al abrir/cerrar un par: nada de trabajo cada 0,5 s
                ctx.armero.armar([c for (k, _) in sorted(llave, key=lambda x: x[0][1]) for c in pares[k].claves_rejilla()])
                ultimas_claves = llave
        errs = ctx.armero.sacar_errores() if ctx.armero is not None else []
        if errs:
            log({"tipo": "armero_errores", "n": len(errs), "primeros": errs[:5]})
        time.sleep(0.5)
    for p in pares.values():
        p.cerrar()
    if ctx.armero is not None:
        ctx.armero.parar()
    ctx.env.vaciar_ledger()
    time.sleep(1)


if __name__ == "__main__":
    main()
