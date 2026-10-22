#!/usr/bin/env python3
"""experimento_maker_h47_r3.py -- VARIANTE de B (H47-B maker ETH/SOL/XRP 5m) con la regla R2/R3 de la seleccion adversa (reglas_congeladas.json v2).
⚠️ NO EJECUTAR todavia. Con --confirmo-dinero-real ENVIARIA ORDENES REALES con la wallet DEDICADA (herencia directa de experimento_maker_h47.Exp47). Requiere, en este orden:
  (1) gate forward del brazo shadow (r3_shadow/r3_vigia.py) CONFIRMADA para la regla elegida; (2) /code-review MEDIUM de ESTE fichero + su test; (3) OK final de Javi;
  (4) peldaño micro-real (wallet dedicada, <= 5 EUR de exposicion, lo opera solo la sesion principal). Nunca en cron/screen/watchdog.
Sin --confirmo-dinero-real es un ENSAYO EN SECO (heredado: no crea cliente CLOB, no firma, no envia; rellenos simulados CONS). Este fichero NO modifica
/root/polymarket-research-dev/experimento_maker_h47.py (sha congelado hasta 500 pujas de B): lo IMPORTA y lo EXTIENDE por herencia.

QUE CAMBIA respecto a B, y solo esto:
  - La puja de B (H35 DEEP_PEG: top - k ticks, banda 0,10-0,30, T 298..60, repegado, un relleno cierra la puja) solo se coloca/mantiene si regla(R2|R3) es verdadera EN CADA
    DECISION (alta y repegado). Regla falsa => `objetivo_h35` devuelve None => B ya sabe lo que hacer (no cotiza; si hay puja viva la cancela: evento `cancela_banda`).
  - R2: bid15(mismo lado, 15m que contiene al 5m) - puja <= 0,03 (en milesimas enteras). R3: R2 AND >= 26 acc casadas en el 5m en 30 s AND hora UTC >= 4. Las funciones de la
    regla son LAS MISMAS del brazo shadow (r3_shadow/r3_regla.py::regla): una sola implementacion, importada.
  - Fail-closed: sin libro 15m, 15m cruzado (bid >= ask), WS del 15m viejo, ventana de vol30 incompleta, token no coincide con el libro, excepcion al evaluar => NO cotiza.
  - Ledger PROPIO `experimento_h47_B_R3_ledger.jsonl` (mismo lock y mismo .KILL que toda la wallet; los demas ledgers lo ven como hermano: suelos y tope total comunes).
    Cada `puja_post`/`repega`/`cancela_banda` lleva `r3` (bid15, ask15, lvl15m, vol30, hora, regla, ok, motivo) y cada alta ademas un evento `r3_decision` ANTES del POST.
  - Guardas nuevas: sha256 de experimento_maker_h47.py debe coincidir con el REVISADO (B_SHA_REVISADO); si B cambia, esto no arranca hasta nueva revision.
    Solo escalon B; --n <= 500; defecto --regla R3. No hay --rearmar-kill/--reiniciar-suelo/--rotar-tanda aqui (operaciones de mantenimiento de la wallet: pendiente de
    decidir en la revision; hoy se hacen con el flujo de experimento_maker_h47.py sobre el ledger de B).
Uso: .venv/bin/python experimentos/5m_barato/b_seleccion_adversa/b_r3/experimento_maker_h47_r3.py --regla R3 --n 20            (ENSAYO EN SECO)"""
import argparse
import hashlib
import json
import queue
import sys
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

AQUI = Path(__file__).resolve().parent
DEV = Path("/root/polymarket-research-dev")
sys.path.insert(0, str(AQUI.parent / "r3_shadow"))
sys.path.insert(0, str(DEV))
sys.path.insert(0, "/root/polymarket-research")
import r3_regla as RR                      # noqa: E402  (la MISMA regla que el brazo shadow)
import experimento_pares_cola_15m as X     # noqa: E402
import experimento_maker_h47 as H          # noqa: E402

B_SHA_REVISADO = "c82f5dc5f304b8a699fa576309f42baf062f46098c0fdd7ce47cb29f435e364b"   # sha256 de experimento_maker_h47.py contra el que se escribio y probo esto (22-Oct)
ESCALON_LEDGER = "B_R3"
VERSION_R3 = "R3-22oct2026-v1"
LOG_EVENTOS_R3 = ("puja_post", "repega", "cancela_banda")
LIBRO15_ANTICIPO_S = 90.0        # el 15m SIGUIENTE se prepara (gamma + WS) 90 s antes de empezar: B lanza el 5m 30 s antes de abrir
LIBRO15_PERIODO_S = 1.0          # cadencia del hilo de preparacion (fuera del bucle de decision)
LIBRO15_BACKOFF_S = (2.0, 5.0, 15.0)     # reintentos tras un fallo de gamma/WS (el ultimo se repite)


def sha_b():
    return hashlib.sha256(Path(H.__file__).read_bytes()).hexdigest()


def verificar_sha_b():
    """Fail-closed: B cambio => esta variante no se ha revisado contra ese codigo."""
    s = sha_b()
    if s != B_SHA_REVISADO:
        sys.exit(f"experimento_maker_h47.py cambio (sha {s[:16]}... != revisado {B_SHA_REVISADO[:16]}...): revisar esta variante contra el B actual y actualizar B_SHA_REVISADO")
    return s


def hora_utc(now):
    return datetime.fromtimestamp(now, timezone.utc).hour


def mercado_15m(coin, ini15):
    """{up, down} del 15m `coin-updown-15m-{ini15}` (gamma publica); None si no existe. Fail-closed si los outcomes no son [Up, Down]."""
    r = H.requests.get(H.GAMMA, params={"slug": f"{coin}-updown-15m-{ini15}"}, timeout=10).json()
    if not r:
        return None
    m = r[0]
    toks, outs = json.loads(m["clobTokenIds"]), json.loads(m["outcomes"])
    if [str(o).lower() for o in outs] != ["up", "down"] or len(toks) != 2:
        return None
    return {"up": toks[0], "down": toks[1], "slug": m["slug"]}


def vol30(c, now):
    """Acciones casadas en el 5m en (max(now-30, apertura), now] por RECEPCION (last_trade_price de los dos tokens, X.Libro con registrar_trades). None si el libro se
    conecto despues del inicio de la ventana (dato ausente != 0)."""
    ini_v = max(now - RR.VENTANA_VOL_S, float(c.mk["ini"]))
    if c.t_inicio > ini_v:
        return None
    lib = c.lib
    with lib.lk:
        tr = list(lib.trades[c.up]) + list(lib.trades[c.dn])
    return float(sum(sz for (t_r, _tx, _p, sz, _sd) in tr if ini_v < t_r <= now))


class Exp47R3(H.Exp47):
    def __init__(self, real, escalon="B", n_max=None, t_stop=H.T_STOP_DEF, size=5, min_nocional=1.0, monedas=("eth", "sol", "xrp"), presupuesto=H.PRESUPUESTO_UTIL,
                 max_vivas=H.MAX_VIVAS, regla="R3"):
        if escalon != "B":
            sys.exit("la variante R3 solo existe para el escalon B")
        if regla not in ("R2", "R3"):
            sys.exit("--regla debe ser R2 o R3")
        self.regla = regla
        self._r3_ctx = None
        self._r3_ultimo = None
        self._r3_err = 0
        # libros 15m COMPARTIDOS por (moneda, inicio del 15m): los 3 mercados 5m de una ventana de 15m usan el mismo; se crean en un hilo aparte, NUNCA en el bucle de decision
        self._lib15 = {}                 # (coin, ini15) -> {"lib": X.Libro, "m15": {up, down, slug}, "t": creado}
        self._lk15 = threading.Lock()
        self._fallo15 = {}               # (coin, ini15) -> (n fallos, proximo intento)
        self._ev15 = queue.SimpleQueue() # eventos del hilo -> ledger, escritos por el hilo principal (el ledger no es seguro entre hilos)
        self._stop15 = threading.Event()
        self._hilo15 = None
        self._fetch15 = mercado_15m                              # inyectables en tests (sin red)
        self._nuevo_libro15 = lambda toks: X.Libro(toks)
        super().__init__(real, escalon, n_max, t_stop, size, min_nocional, monedas, presupuesto, max_vivas)

    # -- ledger: etiqueta de variante y rasgos de la regla en cada decision
    def _log47(self, ev):
        ev["linea_r3"] = ESCALON_LEDGER                              # B tiene ya `variante` (H35/H35b): la nuestra va aparte
        u = self._r3_ultimo
        if u is not None and ev.get("tipo") in LOG_EVENTOS_R3 and ev.get("slug") == u.get("slug"):
            ev["r3"] = u
        if ev.get("tipo") == "config":
            ev.update({"regla": self.regla, "version_r3": VERSION_R3, "b_sha": sha_b()[:16], "r2_max_mils": RR.R2_MAX_MILS, "vol30_min": RR.VOL30_MIN, "hora_min": RR.HORA_MIN})
        super()._log47(ev)

    # -- libros 15m: hilo de preparacion (gamma + WS) fuera del bucle de decision, compartidos por (moneda, ini15), con reintentos
    def claves15(self, ahora):
        cur = int(ahora // 900 * 900)
        ks = [(coin, cur) for coin in self.monedas]
        if ahora >= cur + 900 - LIBRO15_ANTICIPO_S:
            ks += [(coin, cur + 900) for coin in self.monedas]
        return ks

    @staticmethod
    def _libro_vivo(lib):
        try:
            return bool(lib.hilo.is_alive()) and lib.error is None
        except Exception:
            return False

    def preparar_libros15(self, ahora):
        """Crea los libros 15m que faltan (o cuyo hilo WS murio) y limpia los de ventanas pasadas. Sincrono (lo llama el hilo `_bucle15`; tests, directamente).
        Fallos: backoff 2/5/15 s y evento `r3_sin_libro15` (1.o, 5.o y 20.o fallo); nunca lanza por un fallo de red. Devuelve cuantos libros creo."""
        creados = 0
        for k in self.claves15(ahora):
            with self._lk15:
                e = self._lib15.get(k)
            if e is not None:
                if self._libro_vivo(e["lib"]):
                    continue
                with self._lk15:
                    self._lib15.pop(k, None)
                try:
                    e["lib"].parar = True
                except Exception:
                    pass
                self._ev15.put({"tipo": "r3_libro15_muerto", "coin": k[0], "ini15": k[1]})
            n_f, prox = self._fallo15.get(k, (0, 0.0))
            if ahora < prox:
                continue
            try:
                m15 = self._fetch15(k[0], k[1])
                if not m15:
                    raise LookupError("15m no listado todavia en gamma")
                lib = self._nuevo_libro15([m15["up"], m15["down"]])
            except Exception as ex:
                n_f += 1
                self._fallo15[k] = (n_f, ahora + LIBRO15_BACKOFF_S[min(n_f, len(LIBRO15_BACKOFF_S)) - 1])
                if n_f in (1, 5, 20):
                    self._ev15.put({"tipo": "r3_sin_libro15", "coin": k[0], "ini15": k[1], "n": n_f, "e": f"{type(ex).__name__}: {str(ex)[:120]}"})
                continue
            with self._lk15:
                self._lib15[k] = {"lib": lib, "m15": m15, "t": ahora}
            self._fallo15.pop(k, None)
            self._ev15.put({"tipo": "r3_libro15", "coin": k[0], "ini15": k[1], "slug": m15.get("slug"), "intentos": n_f + 1})
            creados += 1
        with self._lk15:
            viejos = [k for k in self._lib15 if k[1] + 900 < ahora - 60]
            libs = [self._lib15.pop(k)["lib"] for k in viejos]
        for lib in libs:
            try:
                lib.parar = True
            except Exception:
                pass
        for k in [k for k in self._fallo15 if k[1] + 900 < ahora - 60]:
            del self._fallo15[k]
        return creados

    def _bucle15(self):
        while not self._stop15.wait(LIBRO15_PERIODO_S):
            try:
                self.preparar_libros15(time.time())
            except Exception as ex:                                  # el hilo no muere: lo registra y sigue
                self._ev15.put({"tipo": "r3_error_hilo15", "e": f"{type(ex).__name__}: {str(ex)[:120]}"})

    def _drenar_ev15(self):
        """Pasa al ledger (hilo principal) los eventos del hilo de libros 15m."""
        try:
            while True:
                self._log47(self._ev15.get_nowait())
        except queue.Empty:
            pass

    def lanzar_mercados(self, ahora):
        self._drenar_ev15()
        return super().lanzar_mercados(ahora)

    def run(self, duracion_max_s=None):
        self._hilo15 = threading.Thread(target=self._bucle15, daemon=True, name="r3_libros15")
        self._hilo15.start()
        try:
            return super().run(duracion_max_s)
        finally:
            self._stop15.set()
            self._hilo15.join(timeout=3)
            with self._lk15:
                libs = [e["lib"] for e in self._lib15.values()]
                self._lib15.clear()
            for lib in libs:
                try:
                    lib.parar = True
                except Exception:
                    pass
            self._drenar_ev15()

    # -- contexto: el libro del 15m se ADJUNTA (lookup sin red) en vez de crearse aqui
    def crear_ctx(self, coin, mk):
        c = super().crear_ctx(coin, mk)
        if c is None:
            return None
        c.lib15, c.tok15 = None, {}
        c.k15 = (coin, int(mk["ini"]) // 900 * 900)
        self._adjuntar15(c)
        return c

    def _adjuntar15(self, c):
        """Si el hilo ya tiene el libro 15m de este contexto (o lo ha recreado), lo adjunta; si no, el contexto sigue sin 15m => la regla NO cotiza (fail-closed)."""
        k = getattr(c, "k15", None)
        if k is None:
            return
        with self._lk15:
            e = self._lib15.get(k)
        if e is not None and c.lib15 is not e["lib"]:
            c.lib15 = e["lib"]
            c.tok15 = {c.up: e["m15"]["up"], c.dn: e["m15"]["down"]}

    def liberar_ctx(self, c):
        c.lib15 = None                                               # el libro 15m es COMPARTIDO: lo cierra el hilo al caducar la ventana, no un 5m que termina
        super().liberar_ctx(c)

    # -- la regla, aplicada al objetivo de B
    def evaluar_regla(self, c, tok, obj, now):
        """(ok, info). Nunca lanza: cualquier fallo => (False, info con motivo)."""
        info = {"slug": c.mk["slug"], "regla": self.regla, "obj": obj, "ok": False, "motivo": None, "v": VERSION_R3}
        try:
            self._adjuntar15(c)
            l15 = getattr(c, "lib15", None)
            f = {"fresco": False, "b15m": None, "cruzado15": False, "objm": H.mils(obj), "vol30": vol30(c, now), "hora": hora_utc(now)}
            if l15 is not None and tok in c.tok15:
                t15 = c.tok15[tok]
                f["fresco"] = bool(l15.fresco()) and bool(c.lib.fresco())
                b15, a15 = l15.top(t15)
                f["b15m"] = H.mils(b15[0]) if b15 else None
                f["cruzado15"] = bool(b15 and a15 and b15[0] >= a15[0] - 1e-9)
                info.update({"b15": b15[0] if b15 else None, "a15": a15[0] if a15 else None})
            ok, motivo = RR.regla(self.regla, f)
            info.update({"ok": bool(ok), "motivo": motivo, "lvl15m": (f["b15m"] - f["objm"]) if f["b15m"] is not None else None, "vol30": f["vol30"], "hora": f["hora"]})
            return bool(ok), info
        except Exception as ex:
            self._r3_err += 1
            info["motivo"] = f"excepcion {type(ex).__name__}: {str(ex)[:80]}"
            return False, info

    def decidir(self, c, T, ahora):
        orig = H.objetivo_h35
        self._r3_ctx = (c, ahora)
        self._r3_ultimo = None                                       # sin evaluacion rancia de un ciclo/mercado anterior: lo que se loguee o autorice sale de ESTE decidir

        def objetivo_con_regla(bid, ask, k):
            o = orig(bid, ask, k)
            if o is None:
                return None
            cc, now = self._r3_ctx
            tok = cc.tok or self.elegir_cara(cc)
            b, a = cc.lib.top(tok) if tok else (None, None)
            if tok is None or b is None or a is None or abs(b[0] - bid) > 1e-9 or abs(a[0] - ask) > 1e-9:
                self._r3_ultimo = {"slug": cc.mk["slug"], "regla": self.regla, "obj": o, "ok": False, "motivo": "token_no_coincide", "v": VERSION_R3}
                return None                                          # el libro cambio entre la lectura de B y la nuestra: no se cotiza
            ok, info = self.evaluar_regla(cc, tok, o, now)
            self._r3_ultimo = info
            return o if ok else None
        H.objetivo_h35 = objetivo_con_regla
        try:
            return super().decidir(c, T, ahora)
        finally:
            H.objetivo_h35 = orig
            self._r3_ctx = None
            self._r3_ultimo = None

    def post(self, slug, tok, lado, precio, size, cola, **kw):
        """Antes de cualquier POST (real o seco) queda en el ledger la decision con los rasgos de la regla (bid15 al pujar)."""
        u = self._r3_ultimo if (self._r3_ultimo and self._r3_ultimo.get("slug") == slug) else {"slug": slug, "ok": False, "motivo": "sin_evaluacion"}
        if u.get("ok") and (u.get("obj") is None or abs(float(u["obj"]) - float(precio)) > 1e-9):
            u = dict(u, ok=False, motivo="obj_distinto_precio", precio_post=precio)    # la evaluacion es de OTRO objetivo: no autoriza este precio
        if not u.get("ok"):                                           # defensa en profundidad: nunca se envia con la regla en falso
            self._log47({"tipo": "r3_bloqueo_post", "slug": slug, "precio": precio, "r3": u})
            return None
        self._log47({"tipo": "r3_decision", "slug": slug, "lado": lado, "precio": precio, "size": size, "cola": cola, "r3": u})
        return super().post(slug, tok, lado, precio, size, cola, **kw)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--regla", choices=("R2", "R3"), default="R3")
    ap.add_argument("--n", type=int, default=None, help="pujas (<= 500)")
    ap.add_argument("--confirmo-dinero-real", action="store_true")
    ap.add_argument("--monedas", default="eth,sol,xrp")
    ap.add_argument("--presupuesto-util", type=float, default=H.PRESUPUESTO_UTIL)
    ap.add_argument("--max-vivas", type=int, default=H.MAX_VIVAS)
    ap.add_argument("--duracion-max-min", type=float, default=None, help="ensayo en seco: tope de duracion")
    a = ap.parse_args(argv)
    verificar_sha_b()
    real = a.confirmo_dinero_real
    monedas = tuple(x.strip() for x in a.monedas.split(",") if x.strip())
    if not monedas or any(m not in H.K_POR_MONEDA for m in monedas):
        sys.exit(f"--monedas: elegir entre {tuple(H.K_POR_MONEDA)}")
    H.configurar_rutas(real, ESCALON_LEDGER, H.T_STOP_DEF)
    if real:
        _ = H.tomar_lock_pares()
    ex = Exp47R3(real, "B", a.n, H.T_STOP_DEF, 5, 1.0, monedas, a.presupuesto_util, a.max_vivas, a.regla)
    print(f"{'REAL' if real else 'ENSAYO EN SECO'} H47-{ESCALON_LEDGER} regla {a.regla}: N={ex.n_max} (ya usadas {ex.n_usadas()}), monedas {monedas}; kill={ex.kill}; ledger {X.LEDGER}", flush=True)
    if real and ex.kill:
        sys.exit("kill pendiente: revisar y rearmar (con el flujo de experimento_maker_h47.py)")
    ex.run(duracion_max_s=a.duracion_max_min * 60 if a.duracion_max_min else None)
    return 0


if __name__ == "__main__":
    sys.exit(main())
