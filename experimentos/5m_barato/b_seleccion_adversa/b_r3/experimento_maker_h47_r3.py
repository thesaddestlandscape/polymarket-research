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
import sys
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

    # -- contexto: libro del 15m del mismo mercado
    def crear_ctx(self, coin, mk):
        c = super().crear_ctx(coin, mk)
        if c is None:
            return None
        c.lib15, c.tok15 = None, {}
        try:
            m15 = mercado_15m(coin, int(mk["ini"]) // 900 * 900)
            if m15:
                c.lib15 = X.Libro([m15["up"], m15["down"]])
                c.tok15 = {c.up: m15["up"], c.dn: m15["down"]}
        except Exception as ex:
            c.lib15 = None
            self._log47({"tipo": "r3_sin_libro15", "slug": mk["slug"], "e": f"{type(ex).__name__}: {str(ex)[:120]}"})
        return c

    def liberar_ctx(self, c):
        try:
            if getattr(c, "lib15", None) is not None:
                c.lib15.parar = True
        except Exception:
            pass
        super().liberar_ctx(c)

    # -- la regla, aplicada al objetivo de B
    def evaluar_regla(self, c, tok, obj, now):
        """(ok, info). Nunca lanza: cualquier fallo => (False, info con motivo)."""
        info = {"slug": c.mk["slug"], "regla": self.regla, "obj": obj, "ok": False, "motivo": None, "v": VERSION_R3}
        try:
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

    def post(self, slug, tok, lado, precio, size, cola, **kw):
        """Antes de cualquier POST (real o seco) queda en el ledger la decision con los rasgos de la regla (bid15 al pujar)."""
        u = self._r3_ultimo if (self._r3_ultimo and self._r3_ultimo.get("slug") == slug) else {"slug": slug, "ok": False, "motivo": "sin_evaluacion"}
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
