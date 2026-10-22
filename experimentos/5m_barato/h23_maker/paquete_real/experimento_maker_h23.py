#!/usr/bin/env python3
"""experimento_maker_h23.py -- H23-MAKER-V1 REAL (PAQUETE PREPARADO, NO ENVIADO). Va en la raiz de /root/polymarket-research-dev junto a
experimento_maker_h47.py (NO lo modifica: lo importa y lo extiende por subclase; el diff contra H47 es CERO lineas).

⚠️ Con --confirmo-dinero-real ENVIA ORDENES REALES con la wallet DEDICADA. Sin esa bandera es un ENSAYO EN SECO (lee solo datos publicos, simula
con el modelo CONS del harness). Puertas de Javi (19/20-Oct), TODAS exigidas por el codigo en real, fail-closed:
  1. H47-B real terminado: el ledger de H47-B debe tener, tras su ultimo `config`, un `fin_ejecucion` SIN kill, SIN parada, con pujas >= n_max de ese
     config, config.escalon == 'B', n_max >= N_MAX['B'] (230), t_stop == 60 y config.codigo_sha == `h47=` del OK (un run abortado/Ctrl-C/senal no llega a su N), sin ordenes abiertas sin verificar y sin kill pendiente (se LEE y se exige). El VEREDICTO de la calibracion lo atestigua el fichero del punto 3.
  2. /code-review adversarial (medium como minimo) de ESTE fichero + test_experimento_maker_h23.py.
  3. OK FINAL de Javi: el chief crea /root/polymarket-research-datalogs/H23_OK_JAVI.txt (texto libre: fecha + motivo) que DEBE contener
     `sha=<16 hex del sha256 de ESTE fichero>`, `regla=<hash_config>` y los sha de lo que ejecuta: `h47=` (experimento_maker_h47.py), `pares=`
     (experimento_pares_cola_15m.py), `contabilidad=` (pares_contabilidad.py), `shadow=` (h23_shadow.py, Refs) (imprimirlos con `--imprimir-sha`; tambien van en el evento `config`), y pasa --ok-final-javi
     "<mismo texto>". Si el fichero cambia (o la regla), el OK deja de valer: hay que reemitirlo.
Sin las tres cosas el real NO arranca.

POLITICA (h23_regla.py, congelada; informe v4_comprar_lo_bueno §4): par BTC 5m/15m que cierra en C (C % 900 == 0); lado s por TWAP60 oficial
(ref15 = twap60(C-900), ref5 = twap60(C-300), |gap| >= 1 bp); puja GTC POST-ONLY de compra en el 5m lado s UNIENDOSE al mejor bid AJENO mientras
querer(...) lo permita (cota bid15, p <= p_limite(bid15, umbral), margen >= -0,05, libro no cruzado, T > 10 s); se CANCELA en cuanto la condicion se
rompe. Tras cancelar hay que ASENTAR (>= 1,5 s, regla del arnes) antes de volver a pujar = variante `join_r` del shadow (su EV es el que aplica a
este ejecutor, NO el de `join`). UN relleno (aunque parcial) CIERRA la puja del mercado (como H47). Brazo A (umbral 0,05, el congelado) por defecto;
B (0,02) solo con --brazo B y ledger aparte.
CAMINO CALIENTE (cancelar): cada vuelta de `paso()` evalua PRIMERO la orden viva (reaccion rapida, antes de cualquier REST de lectura de rellenos), y
las lecturas REST (liquidar/verificar) re-evaluan antes de cada llamada y con limite 1 mientras hay orden viva; `h23_cancela` registra t_evento
(ultimo mensaje WS de los libros), t_detecta, t_cancel y las latencias. Un libro NO fresco (CONEXION no sana: sin PING/PONG en WS_MAX_S, o un token 5m/15m sin mensajes
> EDAD_TOKEN_MAX_S=120 s como respaldo) equivale a no tener vista: se cancela y no se puja; un libro QUIETO con la conexion viva NO se cancela.
`ms_cancel_rtt` de `h23_cancela` puede incluir X.cancelar durmiendo ASENTAR_S (1,5 s) + get_order en el camino «ack» (commit 0b0eede035 de dev: orden con
ack del POST y `already canceled or matched`): el evento lleva `camino_ack` y `rtt_incluye_asentar_s`; no leer ese rtt como latencia de red. La puja viva se compara con el bid AJENO (mejor_bid_ajeno), igual que el replay.
LIMITES DE DINERO: los de H47 intactos (presupuesto util <= 5 USD, suelo dinamico verificado on-chain, N fijo, 5 vivas max, tope 3 USD/orden, kill
persistente, cuadre on-chain, lock de la wallet). N_MAX['H23'] = N_MAX['H23B'] = 40 mercados con intencion (~12 dias a ~3,3 cotizaciones/dia segun el replay).
Tamano: 5 acc (minimo del mercado) o ceil(1 USD/precio) como H47 (NO los 2 EUR de la simulacion). UNIVERSO EJECUTABLE: p en [0,10; 0,60] (tamano
<= 10 acc y coste <= 3 USD/orden) y T > 12 s; fuera de el NO se puja (ver INFORME_ARREGLOS_20OCT.md para lo que el replay pierde por ello).
KILL POR BRAZO V3 (Javi 20-Oct; la regla H23, h23_regla.py y su replay NO cambian): estilo PLAN_MAESTRO §2 sobre el ACUMULADO del brazo. n = posiciones cerradas con desenlace
oficial de TODOS los ledgers reales del brazo (`experimento_h47_H23_ledger*.jsonl` o `..._H23B_ledger*.jsonl`) desde el ultimo `kill_brazo_rearmado`; s = coste medio. Tras CADA
posicion (n >= 3) dispara si perdida acumulada >= z*sigma1*s*sqrt(n) - 0,05*s*n (el tope duro acumulado ES esta formula con el n acumulado). Ademas, tope de TANDA: perdida de las
posiciones de ESTA ejecucion >= 5,0 USD (= el presupuesto util): PARA la tanda (evento `tope_tanda`, cancela lo vivo) SIN kill persistente (como kill persistente seria un
test repetido por tanda: 43-99 % de falso disparo en la simulacion). El kill persistente es solo la formula acumulada. Un reseteo de suelo / nueva tanda NO reinicia el acumulado: solo `--rearmar-kill-brazo "motivo"`. Lectura fail-closed:
un ledger hermano ilegible = no arranca. Parametros en KILL_BRAZO_V3 con hash propio (`hash_kill_v3`: `kill=` en el OK y `config.kill_brazo_v3`). Evento `kill_brazo` persistente.
Falso disparo/potencia por simulacion secuencial (sim_kill_v3.py) en el informe. HONESTO: con n acumulado < ~10 posiciones la formula sigma es INALCANZABLE (exige ~10 perdidas
seguidas con sigma1=2); la proteccion real a n bajo es el SUELO DE SALDO / presupuesto util de H47 (5 USD) y el tope de tanda; el kill sigma solo actua con n acumulado grande. s_n es la
media movil del PREFIJO (coste medio de las n primeras posiciones). El rebate teorico no cuenta como ingreso en el kill; las posiciones con relleno incierto (orden abierta/fill desconocido)
o sin desenlace oficial tras DESENLACE_MAX_PASADAS intentos / DESENLACE_MAX_MIN min = FAIL-CLOSED (no se postean pujas nuevas); al arrancar, la PUERTA resuelve y evalua las posiciones
pendientes antes de la primera orden de una tanda. Dedupe por oid y slug; patron de ledgers estricto (`_tandaN`, nunca copias). Ledger ilegible (hermano o propio) = no opera; recuperacion:
`--aceptar-linea-ilegible-brazo "motivo"`. kill_brazo / kill_brazo_rearmado / tope_tanda con fsync.
Ledger propio `experimento_h47_H23_ledger.jsonl` / `..._H23B_ledger.jsonl` (el glob `experimento_h47_*_ledger.jsonl` de H47 los cuenta como hermanos).
Uso:  .venv/bin/python experimento_maker_h23.py                       (ENSAYO EN SECO)
      .venv/bin/python experimento_maker_h23.py --imprimir-sha       (sha del fichero y hash de la regla para el OK)
      .venv/bin/python experimento_maker_h23.py --confirmo-dinero-real --ok-final-javi "<texto>"   (REAL; ver puertas)
"""
import argparse
import base64
import hashlib
import json
import math
import os
import re
import sys
import time
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
sys.path.insert(0, str(AQUI / "experimentos/5m_barato/h23_maker"))      # h23_regla (fuente unica de la regla)
import experimento_maker_h47 as H   # noqa: E402
import h23_regla as R               # noqa: E402

X = H.X
OK_FICHERO = H.DATALOGS / "H23_OK_JAVI.txt"
H47B_LEDGER = H.DATALOGS / "experimento_h47_B_ledger.jsonl"
H.N_MAX.setdefault("H23", 40)
H.N_MAX.setdefault("H23B", 40)
H.K_POR_MONEDA.setdefault("btc", 0)           # H23 no usa k (join); Exp47.crear_ctx lo busca
T_STOP_H23 = float(R.CONFIG["fin_margen_s"])  # 10 s
H.LOOP_S = 0.02                               # reaccion a eventos: el arnes dormia 100 ms por vuelta (la cancelacion es el edge)
GAMMA_EV = "https://gamma-api.polymarket.com/markets"
EDAD_TOKEN_MAX_S = 120.0                      # respaldo: un libro de UN token (5m o 15m) sin ningun mensaje en este tiempo mientras la conexion esta sana
#   (un libro QUIETO no es un libro viejo: el 15m tiene huecos de >30 s en el 12 % de las ventanas, 4 % de >60 s). La salud la da la CONEXION (PING/PONG).
VIGILAR_SALDO_VIVA_S = 10.0                   # con orden viva el RPC de saldo (bloqueante) se espacia a esto
KILL_BRAZO_CADA_S = 60.0
KILL_BRAZO_MAX_CONSULTAS = 2                  # consultas gamma de desenlace por pasada (cada una bloquea hasta timeout)
KILL_BRAZO_TIMEOUT_S = 3
DESENLACE_MAX_PASADAS = 8                     # consultas de desenlace fallidas de UNA posicion antes de pasar a fail-closed (no postear)
DESENLACE_MAX_MIN = 15.0                      # minutos tras el cierre sin desenlace oficial -> fail-closed (no postear)
PUERTA_REINTENTO_S = 15.0                     # puerta de arranque: reintento de resolver pendientes antes de la 1a orden de una tanda
PUERTA_MAX_CONSULTAS = 20
ARM_RE = {"A": re.compile(r"^experimento_h47_H23_ledger(_tanda[0-9]+)?\.jsonl$"), "B": re.compile(r"^experimento_h47_H23B_ledger(_tanda[0-9]+)?\.jsonl$")}
KILL_BRAZO_GUARDA_S = 20.0                    # no se consulta gamma a menos de esto de la apertura del siguiente 5m cotizable ni durante el
HASH_REGLA = R.hash_config()
AQUI_REGLA = Path(R.__file__).resolve().parent


def _sha_fichero(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()[:16]


def sha_dependencias():
    """sha256[:16] de todo lo que ejecuta este paquete ademas de el mismo: el arnes H47, el harness de pares, pares_contabilidad (contabilidad de dinero) y el shadow (Refs)."""
    return {"h47": _sha_fichero(H.__file__), "pares": _sha_fichero(X.__file__), "contabilidad": _sha_fichero(H.C.__file__),
            "shadow": _sha_fichero(AQUI_REGLA / "h23_shadow.py")}


def sha_propio():
    """sha256[:16] de ESTE fichero: el OK de Javi se liga a el (cualquier cambio invalida el OK)."""
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()[:16]


def mercado_15m(ini):
    r = H.requests.get(GAMMA_EV, params={"slug": f"btc-updown-15m-{ini}"}, timeout=10).json()
    if not r:
        return None
    m = r[0]
    toks, outs = json.loads(m["clobTokenIds"]), json.loads(m["outcomes"])
    return {"slug": m["slug"], "id": str(m["id"]), "toks": dict(zip(outs, toks))}


def lado_por_refs(ref15, ref5):
    """'Up'|'Down'|None (gap < minimo o referencia ausente). Fuente unica: h23_regla."""
    return R.lado_de_refs(ref15, ref5)


def objetivo_h23(top_5, top_15, umbral):
    """Precio al que querer estar pujando AHORA o None (= no pujar / cancelar). top_*: ((bid,sz)|None, (ask,sz)|None) del libro.
    top_5 debe llevar el bid AJENO (sin nuestra orden): lo garantiza Exp23._top5."""
    (b5, a5), (b15, a15) = top_5, top_15
    return R.querer(b5[0] if b5 else None, a5[0] if a5 else None, b15[0] if b15 else None, a15[0] if a15 else None, umbral)


class LibroH23(X.Libro):
    """Libro del harness + hora de recepcion del ultimo mensaje que TOCO cada token (5m y 15m): `fresco()` solo mide la conexion y el ultimo
    cambio de CUALQUIER token, no la edad del bid15."""

    def __init__(self, toks, registrar_trades=False):
        self.ult_tok = {}
        super().__init__(toks, registrar_trades=registrar_trades)

    def _aplicar(self, m):
        super()._aplicar(m)
        if m.get("event_type") in ("tick_size_change", "last_trade_price"):
            return
        if "price_changes" in m:
            ids = {pc.get("asset_id") for pc in m["price_changes"]}
        elif "bids" in m or "asks" in m:
            ids = {m.get("asset_id")}
        else:
            return
        t = time.time()
        for i in ids:
            if i in self.L:
                self.ult_tok[i] = t

    def edad(self, tk):
        return time.time() - self.ult_tok.get(tk, 0.0)

    def conexion_sana(self):
        """Hilo vivo, sin error y ALGUN mensaje (PONG incluido) en WS_MAX_S: la salud de la conexion, no la actividad del libro."""
        return self.hilo.is_alive() and self.error is None and time.time() - self.ult_msg <= X.WS_MAX_S and self.ult > 0


class Ctx23(H.Ctx):
    def __init__(self, coin, mk, lib, k, mk15):
        super().__init__(coin, mk, lib, k)
        t15 = mk15["toks"]
        self.up15, self.dn15 = t15.get("Up") or t15.get("Yes"), t15.get("Down") or t15.get("No")
        self.s = self.tc = self.to = None
        self.mk15 = mk15


_SIN_CAMBIO = object()


class LibPost:
    """Lib que ve X.Exp.post TRAS firmar (create_order + get_neg_risk son red): ademas de sus comprobaciones (fresco, vacio, tick, t_stop, bid ajeno,
    ask) REVALIDA la regla H23 completa: si objetivo_h23 ya no es el precio firmado (cota bid15, p_limite, margen, cruce, frescura 5m/15m), la comparacion
    `mejor_bid_ajeno != ajeno_dec` de X.post falla (devolvemos un centinela) y NO se envia. Fail-closed."""

    def __init__(self, ex, c, precio):
        self.ex, self.c, self.precio, self.motivo = ex, c, float(precio), None

    def top(self, tk):
        return self.c.lib.top(tk)

    def fresco(self):
        return self.ex._libro_fresco(self.c)

    @property
    def tick_cambiado(self):
        return self.c.lib.tick_cambiado

    def mejor_bid_ajeno(self, tk):
        obj = self.ex._objetivo(self.c, None)
        if obj is None or abs(obj - self.precio) > 1e-9:
            self.motivo = {"objetivo_ahora": obj, "precio_firmado": self.precio}
            return _SIN_CAMBIO
        return self.c.lib.mejor_bid_ajeno(tk)


# ------------------------------------------------------------------ kill por brazo V3 (puro, probado sin red)
# VERSION NUEVA del kill (Javi, 20-Oct): el de h23_regla.CONFIG['kill_brazo'] (n>=20, EV sin 2 mejores dias) no puede dispararse con N=40 (~6-9 posiciones). La
# regla H23 y su replay NO cambian (h23_regla.py intacto: su hash no cambia). Estilo PLAN_MAESTRO §2: perdida acumulada >= z*sigma1*s*sqrt(n) - margen_ev*s*n,
# con n = posiciones con desenlace oficial, s = coste medio por posicion, comprobada tras CADA posicion cerrada (n >= n_min), mas un tope duro de perdida.
# Falso disparo y potencia: SIMULACION SECUENCIAL (INFORME_ARREGLOS_20OCT.md, sim_kill_v2.py); cualquier cambio de un parametro o de la funcion cambia el hash.
KILL_BRAZO_V3 = {"version": 3, "nombre": "H23-KILL-V3", "z": 1.645, "sigma1": 2.0, "margen_ev": 0.05, "n_min": 3, "tope_tanda_usd": 5.0,
                 "presupuesto_ref_usd": 5.0, "acumulado": "ledgers_del_brazo_desde_ultimo_rearme", "rebate": "no_cuenta_como_ingreso",
                 "s": "media_movil_del_prefijo",
                 "nota": "con n acumulado < ~10 posiciones la formula sigma es INALCANZABLE (exige ~10 perdidas seguidas con sigma1=2): la proteccion real a n bajo es el "
                         "suelo de saldo/presupuesto util de H47 (5 USD) y el tope de tanda; el kill sigma solo actua con n acumulado grande"}


def evaluar_kill_v3(posiciones, cfg=None, t_tanda=0.0):
    """posiciones: ACUMULADO del brazo [{'slug','acc','coste','gana','fin', 't_int'}] (gana None = sin desenlace oficial: NO cuenta, missing != 0). En orden de cierre, TRAS CADA
    posicion: (a) tope de tanda (el ejecutor lo trata como PARADA de tanda, no como kill; la formula (b) si es kill persistente): perdida de las posiciones con t_int >= t_tanda (esta ejecucion; sin t_int cuentan todas) >= tope_tanda_usd; (b) con n >= n_min: perdida acumulada
    >= z*sigma1*s_n*sqrt(n) - margen_ev*s_n*n, con s_n = MEDIA MOVIL DEL PREFIJO (coste medio de las n primeras posiciones, no de todas). PnL = acc*gana - coste: el rebate
    teorico del maker NO se cuenta como ingreso (cota pesimista: perdidas algo mayores). Las posiciones con relleno incierto (orden abierta/fill desconocido) llegan con gana=None. Devuelve (dispara, info)."""
    cfg = cfg or KILL_BRAZO_V3
    ps = sorted((p for p in posiciones if p.get("gana") is not None and p["acc"] > 1e-9 and p["coste"] > 0), key=lambda p: p.get("fin", 0))
    info = {"n": len(ps), "sin_desenlace": sum(1 for p in posiciones if p.get("gana") is None), "perdida": 0.0, "perdida_tanda": 0.0, "umbral": None, "causa": None}
    perdida = tanda = coste_cum = 0.0
    for i, p in enumerate(ps, 1):
        pnl = p["acc"] * (1.0 if p["gana"] else 0.0) - p["coste"]
        perdida -= pnl
        if p.get("t_int", t_tanda) >= t_tanda:
            tanda -= pnl
        coste_cum += p["coste"]
        s = coste_cum / i
        umbral = cfg["z"] * cfg["sigma1"] * s * math.sqrt(i) - cfg["margen_ev"] * s * i
        info.update(n_disparo=i, perdida=round(perdida, 4), perdida_tanda=round(tanda, 4), umbral=round(umbral, 4), s=round(s, 4))
        if tanda >= cfg["tope_tanda_usd"] - 1e-9:
            info["causa"] = "tope_tanda"
            return True, info
        if i >= cfg["n_min"] and perdida >= umbral:
            info["causa"] = "sigma"
            return True, info
    info.pop("n_disparo", None)
    return False, info


def hash_kill_v3(cfg=None):
    """Hash propio del kill: parametros + codigo de evaluar_kill_v3 (entra en el OK y en `config`)."""
    import inspect
    h = hashlib.sha256(json.dumps(cfg or KILL_BRAZO_V3, sort_keys=True).encode())
    for fn in (evaluar_kill_v3, agrupar_posiciones, estado_acumulado, escanear_brazo, leer_ledger_brazo, ledgers_del_brazo):
        h.update(inspect.getsource(fn).encode())
    return h.hexdigest()[:16]


def t_rearme(eventos):
    """Epoch del ultimo `kill_brazo_rearmado` real (0.0 si no hay): tras un rearme solo cuentan las ordenes posteriores."""
    return max([H.C.ts_epoch(e) or 0.0 for e in eventos if e.get("real") and e.get("tipo") == "kill_brazo_rearmado"] or [0.0])


def kill_brazo_pendiente(eventos):
    """Motivo del ultimo `kill_brazo` real si no hay un `kill_brazo_rearmado` posterior; None si no hay."""
    pend = None
    for e in eventos:
        if e.get("real") and e.get("tipo") == "kill_brazo":
            pend = e.get("motivo") or "kill_brazo"
        elif e.get("real") and e.get("tipo") == "kill_brazo_rearmado":
            pend = None
    return pend


class LedgerBrazoIlegible(Exception):
    pass


def ledgers_del_brazo(brazo, dirn=None, propio=None):
    """Ledgers reales de OTRAS tandas del brazo (sin el propio), con patron ESTRICTO: A `experimento_h47_H23_ledger[_tandaN].jsonl`, B `..._H23B_ledger[_tandaN].jsonl`.
    Copias/backups (`.bak`, `_copia`, `.jsonl~`, ...) y el otro brazo / H47-B no se recogen."""
    dirn = Path(dirn) if dirn is not None else X.LEDGER.parent
    propio = Path(propio) if propio is not None else X.LEDGER
    return [f for f in sorted(dirn.iterdir()) if ARM_RE[brazo].match(f.name) and f.resolve() != propio.resolve()]


def agrupar_posiciones(ordenes, t_rearme=0.0):
    """Una posicion cruda por mercado con relleno: [{'slug','acc','coste','toks','t_int','incierta'}]; ignora alias/ilegibles/sin relleno y lo anterior al rearme.
    `incierta` = alguna orden aun abierta (hi > lo: relleno aun no verificado / fill desconocido): su PnL no es fiable -> sin desenlace fiable (fail-closed)."""
    por_slug = {}
    for o in ordenes:
        if o.alias or o.ilegible or o.lo <= 1e-9 or o.t_int <= t_rearme:
            continue
        p = por_slug.setdefault(o.slug, {"slug": o.slug, "acc": 0.0, "coste": 0.0, "toks": set(), "t_int": o.t_int, "incierta": False})
        p["acc"] += o.lo
        p["coste"] += o.lo * o.precio
        p["toks"].add(o.tok)
        p["t_int"] = min(p["t_int"], o.t_int)
        p["incierta"] = p["incierta"] or bool(o.abierta)
    return list(por_slug.values())


def leer_ledger_brazo(f):
    """(eventos, malas[(n_linea, texto)]) de un ledger: una linea que no es un objeto JSON va a `malas`; un fichero ilegible lanza LedgerBrazoIlegible."""
    ev, malas = [], []
    try:
        with open(f, "rb") as fh:
            for n, raw in enumerate(fh, 1):
                t = raw.decode("utf-8", "replace").rstrip("\n")
                if not t.strip():
                    continue
                try:
                    e = json.loads(t)
                except ValueError:
                    malas.append((n, t))
                    continue
                if isinstance(e, dict):
                    ev.append(e)
                else:
                    malas.append((n, t))
    except OSError as e:
        raise LedgerBrazoIlegible(f"{Path(f).name}: {type(e).__name__}: {str(e)[:100]}")
    return ev, malas


def escanear_brazo(brazo, dirn=None, con_propio=True):
    """Lee los ledgers del brazo (hermanos + propio si existe). Devuelve {'por_fichero': {nombre: (eventos, malas)}, 'sin_aceptar': [(nombre, n, texto)]}: las lineas ilegibles
    solo valen si un evento `h23_linea_ilegible_aceptada` (auditado, con motivo) las acepto por (fichero, sha)."""
    ficheros = ledgers_del_brazo(brazo, dirn)
    if con_propio and X.LEDGER.exists():
        ficheros.append(X.LEDGER)
    por, acept = {}, set()
    for f in ficheros:
        por[f.name] = leer_ledger_brazo(f)
        for e in por[f.name][0]:
            if e.get("real") and e.get("tipo") == "h23_linea_ilegible_aceptada":
                acept |= {(str(x[0]), str(x[1])) for x in e.get("aceptadas", [])}
    sin = [(nm, n, t) for nm, (ev, malas) in por.items() for n, t in malas if (nm, H._sha(t)) not in acept]
    return {"por_fichero": por, "sin_aceptar": sin}


def estado_acumulado(brazo, eventos_propios=None, dirn=None):
    """Estado del brazo sobre TODOS sus ledgers reales, FAIL-CLOSED: una linea ilegible sin aceptar (en un ledger hermano o en el PROPIO) o un fichero ilegible lanza
    LedgerBrazoIlegible. Dedupe por oid (sin nombre de fichero: una copia no duplica) y por slug (una posicion por mercado). Devuelve {'pendiente', 't_rearme',
    'previas': posiciones crudas de los hermanos tras el rearme, 'ordenes_previas': {oid: Orden}}."""
    esc = escanear_brazo(brazo, dirn, con_propio=eventos_propios is None)
    if esc["sin_aceptar"]:
        nm, n, t = esc["sin_aceptar"][0]
        raise LedgerBrazoIlegible(f"{len(esc['sin_aceptar'])} linea(s) ilegible(s) sin aceptar (p. ej. {nm}:{n}: {t[:60]!r}); usar --aceptar-linea-ilegible-brazo")
    propio = X.LEDGER.name
    eventos = list(eventos_propios) if eventos_propios is not None else list(esc["por_fichero"].get(propio, ([], []))[0])
    ords = {}
    for nm, (ev, _) in esc["por_fichero"].items():
        if nm == propio:
            continue
        eventos += [e for e in ev if e.get("real") and e.get("tipo") in ("kill_brazo", "kill_brazo_rearmado")]
        for oid, o in H.C.plegar(ev).items():
            ords.setdefault(oid, o)
    eventos.sort(key=lambda e: H.C.ts_epoch(e) or 0.0)
    t_r = t_rearme(eventos)
    return {"pendiente": kill_brazo_pendiente(eventos), "t_rearme": t_r, "previas": agrupar_posiciones(ords.values(), t_r), "ordenes_previas": ords}


def aceptar_lineas_brazo(brazo, motivo, leer=input, dirn=None):
    """Recuperacion de un ledger truncado (hermano o propio), como H47 `aceptar_linea_ilegible`: muestra cada linea, SOLO acepta las que parezcan un JSON cortado por un crash
    (si hay alguna de otro tipo no acepta ninguna), exige motivo y confirmacion escrita, y deja un evento `h23_linea_ilegible_aceptada` (fichero + sha + linea cruda en base64)
    en el ledger propio con fsync. Devuelve el evento o None."""
    if motivo is None or not str(motivo).strip():
        raise SystemExit("--aceptar-linea-ilegible-brazo exige un motivo no vacio")
    sin = escanear_brazo(brazo, dirn)["sin_aceptar"]
    if not sin:
        print("no hay lineas ilegibles sin aceptar")
        return None
    raras = [x for x in sin if not H.parece_truncada(x[2])]
    if raras:
        raise SystemExit(f"{len(raras)} linea(s) ilegible(s) NO parecen un JSON cortado por un crash (p. ej. {raras[0][0]}:{raras[0][1]}: {raras[0][2][:80]!r}): "
                         "investigar a mano; no se acepta ninguna")
    for nm, n, t in sin:
        print(f"{nm}:{n}: {t[:300]!r}", flush=True)
    if not H._confirmar(leer, f"ACEPTAR LINEA ILEGIBLE BRAZO {brazo}"):
        print("no confirmado: nada cambia")
        return None
    ev = {"tipo": "h23_linea_ilegible_aceptada", "real": True, "brazo": brazo, "motivo": str(motivo)[:300],
          "aceptadas": sorted({(nm, H._sha(t)) for nm, _, t in sin}),
          "lineas_crudas": {H._sha(t): {"fichero": nm, "linea": n, "base64": base64.b64encode(t.encode("utf-8", "replace")).decode()} for nm, n, t in sin}}
    X.log(ev)
    H._fsync_ledger()
    return ev


def desenlace_token(slug):
    """Token ganador (id) de un mercado 5m por gamma, o None si aun no hay desenlace oficial claro (missing, nunca 0)."""
    r = H.requests.get(GAMMA_EV, params={"slug": slug, "closed": "true"}, timeout=KILL_BRAZO_TIMEOUT_S).json()
    if not r:
        return None
    m = r[0]
    if not m.get("closed"):
        return None
    toks, pr = json.loads(m["clobTokenIds"]), [float(x) for x in json.loads(m["outcomePrices"])]
    if len(toks) != len(pr) or sorted(pr) != [0.0, 1.0]:
        return None
    return toks[pr.index(1.0)]


class Exp23(H.Exp47):
    def __init__(self, real, brazo="A", n_max=None, size=5, min_nocional=1.0, presupuesto=H.PRESUPUESTO_UTIL, max_vivas=H.MAX_VIVAS, refs=None):
        if brazo not in R.CONFIG["brazos"]:
            sys.exit(f"--brazo debe ser uno de {tuple(R.CONFIG['brazos'])}")
        self.brazo, self.umbral, self.refs = brazo, R.CONFIG["brazos"][brazo], refs
        self.kill_brazo, self.t_rearme_brazo, self.tanda_agotada, self.sin_desenlace = None, 0.0, None, None
        self._en_reaccion, self._ctx_actual, self._poll_ms = False, None, None
        self._ult_vigilar, self._ult_kb, self._des = 0.0, 0.0, {}
        self._intentos, self._ult_puerta, self.puerta_ok, self._sd_avisado = {}, 0.0, not real, None
        super().__init__(real, "H23" if brazo == "A" else "H23B", n_max, T_STOP_H23, size, min_nocional, ("btc",), presupuesto, max_vivas)
        self.t_inicio_tanda = time.time()
        self._previas, self._ordenes_previas = [], {}
        if real:
            try:
                st = estado_acumulado(brazo)
            except LedgerBrazoIlegible as e:
                sys.exit(f"ledger hermano del brazo {brazo} ilegible ({e}): el acumulado del kill no es fiable, no se opera (fail-closed)")
            self.kill_brazo, self.t_rearme_brazo, self._previas, self._ordenes_previas = st["pendiente"], st["t_rearme"], st["previas"], st["ordenes_previas"]

    # ---- etiquetas: ningun evento de H23 sale marcado como H35 (puja_fin/config los escribe H47 con 'H35')
    def _log47(self, ev):
        if ev.get("tipo") in ("puja_fin", "config", "mercado_fin", "puja_post", "h23_cancela", "h23_revalida_aborta", "kill_brazo", "tope_tanda", "par_refs", "puerta_arranque_ok", "puerta_arranque_pendiente", "kill_brazo_sin_desenlace"):
            ev["variante"] = f"H23-{self.brazo}"
            ev.update(brazo=self.brazo, umbral=self.umbral, hash_regla=HASH_REGLA)
            if ev["tipo"] == "config":
                ev["codigo_sha_h23"] = sha_propio()
                ev["dependencias"] = sha_dependencias()
                ev["kill_brazo_v3"] = {"hash": hash_kill_v3(), **KILL_BRAZO_V3}
        super()._log47(ev)

    # ---- descubrimiento: solo el 5m que cierra con su 15m (C % 900 == 0)
    def lanzar_mercados(self, ahora):
        self._vigilar_kill_brazo(ahora)
        if self.parada or self.kill or self.senal or self.kill_brazo or self.n_usadas() >= self.n_max:
            return
        c = (int(ahora // 900) + 1) * 900
        if not (c - 300 - 60 <= ahora < c - self.t_stop - 30):
            return
        slug = f"btc-updown-5m-{c - 300}"
        if slug in self.ctxs or ahora < self._gamma_err.get(slug, 0):
            return
        try:
            mk, mk15 = H.mercado_5m("btc", c - 300), mercado_15m(c - 900)
        except Exception as e:
            self._gamma_err[slug] = ahora + 10
            self._log47({"tipo": "gamma_error", "slug": slug, "e": str(e)[:160]})
            return
        if not mk or not mk15:
            self._gamma_err[slug] = ahora + 10
            return
        cx = self.crear_ctx("btc", mk, mk15)
        self.ctxs[slug] = cx if cx is not None else "saltado"

    def crear_ctx(self, coin, mk, mk15=None):
        if mk15 is None:
            return None
        base = super().crear_ctx(coin, mk)                  # valida tokens/slug usado/tick 0,01; abre un Libro 5m que se sustituye
        if base is None:
            return None
        base.lib.parar = True
        try:
            toks = [base.up, base.dn] + [t for t in (mk15["toks"].get("Up"), mk15["toks"].get("Down")) if t]
            lib = LibroH23(toks, registrar_trades=True)
        except Exception as ex:
            self._log47({"tipo": "ws_no_conecta_salto", "slug": mk["slug"], "e": str(ex)[:160]})
            return None
        return Ctx23(coin, mk, lib, 0, mk15)

    def _fijar_lado(self, c):
        if c.s is not None or self.refs is None:
            return
        r15, r5 = self.refs.get(c.mk["fin"] - 900), self.refs.get(c.mk["fin"] - 300)
        if not (r15 and r5):
            return
        s = lado_por_refs(r15[0], r5[0])
        self._log47({"tipo": "par_refs", "slug": c.mk["slug"], "ref15": r15[0], "ref5": r5[0], "lado": s, "leida_ms": r5[1]})
        if s is None:
            c.s = "descartado"
            return
        c.s = s
        c.tc, c.to = (c.up, c.up15) if s == "Up" else (c.dn, c.dn15)

    def elegir_cara(self, c):
        return c.tc

    # ---- vista del libro y objetivo (UNICA fuente para decidir, cancelar y revalidar tras firmar)
    def _libro_fresco(self, c):
        """Conexion SANA (`LibroH23.conexion_sana()`: PING/PONG reciente, hilo vivo, sin error) y, como respaldo, ningun libro usado (5m y 15m cara s) con mas de EDAD_TOKEN_MAX_S sin
        mensajes. Un libro quieto con la conexion viva NO se cancela; si la conexion muere se cancela en WS_MAX_S. Sin vista = cancelar (fail-closed)."""
        if not c.lib.conexion_sana():                       # NO X.Libro.fresco(): exige cambios en <= 120 s y trata un libro quieto como muerto
            return False
        return all(c.lib.edad(tk) <= EDAD_TOKEN_MAX_S for tk in (c.tc, c.to))

    def _top5(self, c, o):
        """(bid, ask) del 5m lado s. Con orden viva el bid es el AJENO: se resta SIEMPRE nuestro tamano restante (sea o no `visto`). Si el WS aun no
        mostraba nuestra orden se resta de mas -> el bid ajeno sale mas bajo o ausente -> se cancela (el lado SEGURO respecto al replay, que no nos tiene
        en el libro): nunca se queda donde el replay cancelaria. top() incluye nuestra orden y, si somos el unico en el nivel, el replay ya habria movido."""
        b, a = c.lib.top(c.tc)
        if o is None:
            return b, a
        e = c.estado[c.tc]
        resto = max(0.0, float(o["size"]) - sum(r["acc"] for r in e["rellenos"] if r["oid"] == e["oid"]))
        aj = c.lib.mejor_bid_ajeno(c.tc, float(o["precio"]), resto, True)
        return ((aj, 0.0) if aj is not None else None), a

    def _objetivo(self, c, o=None):
        if c.s in (None, "descartado") or c.tc is None or self.kill_brazo or self.tanda_agotada:
            return None
        ahora = time.time()
        if ahora < c.mk["fin"] - 300 + R.CONFIG["ref_conocible_ms"] / 1000.0 or c.mk["fin"] - ahora <= self.t_stop:
            return None
        if c.lib.tick_cambiado or not self._libro_fresco(c):
            return None
        return objetivo_h23(self._top5(c, o), c.lib.top(c.to), self.umbral)

    def _t_evento(self, c):
        ts = [c.lib.ult_tok.get(t) for t in (c.tc, c.to) if c.lib.ult_tok.get(t)]
        return max(ts) if ts else getattr(c.lib, "ult", None)

    def _marcar_visto(self, c, tok, e, o, ahora):
        """Bloque `visto` de Exp47.decidir (1ª /code-review #10 de H47): sin el, un 'already canceled or matched' en una orden < 30 s (X.cancelar solo lo
        acepta si la orden esta vista o madura) acababa en KILL compartido de la wallet."""
        if o.get("visto"):
            return
        resto = float(o["size"]) - sum(r["acc"] for r in e["rellenos"] if r["oid"] == e["oid"])
        nivel_ok = c.lib.tamano_nivel(tok, o["precio"]) >= (o.get("cola") or 0.0) + max(0.0, resto) - 1e-9
        plazo_ok = ahora - float(o.get("t_post") or 0.0) >= X.VISTO_MAX_S
        if nivel_ok or plazo_ok:
            o["visto"] = True
            self._log47({"tipo": "visto", "oid": e["oid"], "t": ahora, "espera_s": round(ahora - float(o["t_post"]), 3),
                         "criterio": "nivel" if nivel_ok else "plazo", "simulado": not self.real})

    def _reaccion_viva(self, c, T, ahora, origen):
        """CAMINO CALIENTE: si hay orden viva y la condicion se rompe, el bid ajeno cambia, el libro deja de estar fresco o se acaba la ventana,
        CANCELAR YA (sin limite de cadencia). Devuelve True si cancelo."""
        if c.tc is None:
            return False
        tok = c.tc
        e = c.estado[tok]
        o = self.vivas.get(e["oid"]) if e["oid"] else None
        if o is None:
            return False
        self._marcar_visto(c, tok, e, o, ahora)
        t_det = time.time()
        objetivo = self._objetivo(c, o)
        if objetivo is not None and abs(objetivo - float(o["precio"])) < 1e-9:
            return False
        causa = ("kill_brazo" if (self.kill_brazo or self.tanda_agotada) else "libro_no_fresco" if not self._libro_fresco(c) else
                 "condicion" if objetivo is None else "bid_cambia")
        t_ev, h = self._t_evento(c), e["oid"]
        self._en_reaccion = True
        try:
            n_ev = len(X.leer_ledger())
            t_c0 = time.time()
            ok = self.cancelar(h)
            t_c1 = time.time()
            camino_ack = any(ev.get("tipo") == "cancel_ya_terminal_ack" for ev in X.leer_ledger()[n_ev:])
            if not ok:
                return False
            c.t_accion = t_c1
            e["oid"] = None
            self._log47({"tipo": "h23_cancela", "slug": c.mk["slug"], "de": o["precio"], "objetivo": objetivo, "T": round(T, 2), "causa": causa,
                         "origen": origen, "t_evento": t_ev, "t_detecta": t_det, "t_cancel": t_c0, "t_cancel_ret": t_c1,
                         "camino_ack": camino_ack, "rtt_incluye_asentar_s": X.ASENTAR_S if camino_ack else 0.0,
                         "edad_5m_s": round(c.lib.edad(c.tc), 2), "edad_15m_s": round(c.lib.edad(c.to), 2),
                         "ms_evento_a_cancel": round((t_c0 - t_ev) * 1000, 1) if t_ev else None, "ms_cancel_rtt": round((t_c1 - t_c0) * 1000, 1),
                         "ult_poll_rest_ms": self._poll_ms})
            self.liquidar(h, o, True, c.estado, c.lib, T)           # relleno previo a la cancelacion, AHORA (tras cancelar)
            if e["llenas"] > 1e-9:
                e["cerrado"] = True
            return True
        finally:
            self._en_reaccion = False

    def _reaccion_rapida(self, c):
        if c is None or c.fase != "activa" or self._en_reaccion:
            return False
        ahora = time.time()
        return self._reaccion_viva(c, c.mk["fin"] - ahora, ahora, "rapida")

    def paso(self, c):
        """Reaccion ANTES de la logica del arnes: Exp47.paso sale sin llegar a decidir() si el libro no esta fresco (hasta WS_MAX_S=5 s con la puja viva)
        y hace REST (liquidar/verificar) antes de decidir."""
        self._ctx_actual = c
        try:
            if c.fase == "activa" and not (self.kill or self.senal):
                self._reaccion_rapida(c)
            super().paso(c)
        finally:
            self._ctx_actual = None

    def liquidar(self, h, o, es_cancelada, estado, lib, T):
        if not self._en_reaccion:
            self._reaccion_rapida(self._ctx_actual)                  # nunca una lectura REST con una cancelacion pendiente de decidir
            if not es_cancelada and h not in self.vivas:             # la reaccion pudo cancelarla (y ya la liquido): releer, no usar los argumentos viejos
                if h not in self.canceladas:
                    return None
                es_cancelada, o = True, self.canceladas[h]
        t0 = time.time()
        r = super().liquidar(h, o, es_cancelada, estado, lib, T)
        self._poll_ms = round((time.time() - t0) * 1000, 1)
        return r

    def verificar(self, limite=None):
        if not self._en_reaccion:
            self._reaccion_rapida(self._ctx_actual)
        if self.vivas and limite is not None and limite > 1:
            limite = 1                                              # mientras hay orden viva, lecturas de una en una
        return super().verificar(limite=limite)

    def vigilar_saldo(self, ahora):
        """RPC on-chain bloqueante: con orden viva se espacia (el cuadre y el suelo se siguen vigilando, a >= VIGILAR_SALDO_VIVA_S)."""
        if (self.vivas or self.canceladas) and ahora - self._ult_vigilar < VIGILAR_SALDO_VIVA_S:
            return
        self._ult_vigilar = ahora
        super().vigilar_saldo(ahora)

    # ---- kill por brazo
    def posiciones_brazo(self):
        """ACUMULADO del brazo: ordenes de esta ejecucion + las de los ledgers hermanos (desde el ultimo rearme), deduplicadas por oid (lo propio manda) y agrupadas por mercado.
        gana None = sin desenlace FIABLE: no resuelto, o relleno incierto (orden abierta / fill desconocido)."""
        t_r = getattr(self, "t_rearme_brazo", 0.0)
        ords = dict(getattr(self, "_ordenes_previas", {}))
        ords.update(self.ordenes())
        out = []
        for p in agrupar_posiciones(ords.values(), t_r):
            try:
                fin = int(p["slug"].rsplit("-", 1)[1]) + 300
            except (ValueError, IndexError):
                continue
            w = self._des.get(p["slug"])
            out.append({"slug": p["slug"], "dia": time.strftime("%Y-%m-%d", time.gmtime(fin)), "acc": p["acc"], "coste": p["coste"], "incierta": p["incierta"],
                        "gana": None if (w is None or p["incierta"]) else (w in p["toks"]), "fin": fin, "t_int": p["t_int"]})
        return out

    def _log_durable(self, ev):
        """Evento de seguridad (kill_brazo, tope_tanda, ...) con fsync: si no llega a disco -> kill de la wallet (fail-closed)."""
        self._log47(ev)
        try:
            H._fsync_ledger()
        except Exception as e:
            self.kill = self.kill or f"no se pudo hacer fsync de {ev.get('tipo')}: {type(e).__name__}: {str(e)[:100]}"

    def _resolver_pendientes(self, pos, ahora, max_n):
        """Consulta el desenlace oficial de las posiciones pendientes (cerradas hace > 60 s), ROTANDO: primero las de menos intentos, luego las mas antiguas. Cada fallo de
        gamma cuenta un intento y se registra; nunca deja la evaluacion sin hacer."""
        pend = sorted((p for p in pos if p["gana"] is None and not p.get("incierta") and ahora > p["fin"] + 60 and p["slug"] not in self._des),
                      key=lambda p: (self._intentos.get(p["slug"], 0), p["fin"]))
        for p in pend[:max_n]:
            self._intentos[p["slug"]] = self._intentos.get(p["slug"], 0) + 1
            try:
                w = desenlace_token(p["slug"])
            except Exception as e:
                self._log47({"tipo": "desenlace_error", "slug": p["slug"], "intento": self._intentos[p["slug"]], "e": f"{type(e).__name__}: {str(e)[:120]}"})
                continue
            if w is not None:
                self._des[p["slug"]] = w

    def _motivo_sin_desenlace(self, pos, ahora):
        """Fail-closed: una posicion que lleva > DESENLACE_MAX_MIN min desde el cierre, o >= DESENLACE_MAX_PASADAS intentos fallidos, sin desenlace oficial (o con relleno incierto)
        deja el kill ciego -> NO se postean pujas nuevas hasta que se resuelva."""
        for p in pos:
            if p["gana"] is not None or ahora <= p["fin"] + 60:
                continue
            if p.get("incierta"):
                return f"{p['slug']}: relleno incierto (orden abierta/fill desconocido): sin desenlace fiable"
            if ahora - p["fin"] > DESENLACE_MAX_MIN * 60 or self._intentos.get(p["slug"], 0) >= DESENLACE_MAX_PASADAS:
                return f"{p['slug']}: sin desenlace oficial tras {self._intentos.get(p['slug'], 0)} intentos / {round((ahora - p['fin']) / 60, 1)} min"
        return None

    def _evaluar_kill(self, pos):
        t_t = getattr(self, "t_inicio_tanda", 0.0)
        dispara, info = evaluar_kill_v3(pos, {**KILL_BRAZO_V3, "tope_tanda_usd": math.inf}, t_tanda=t_t)       # (a) formula sobre el ACUMULADO: kill PERSISTENTE
        if dispara:
            motivo = (f"kill V3 de brazo {self.brazo} (sigma): perdida acumulada {info['perdida']} $ >= umbral {info['umbral']} tras {info['n_disparo']} "
                      f"posiciones acumuladas")
            self.kill_brazo = motivo
            self._log_durable({"tipo": "kill_brazo", "motivo": motivo, "info": info})
            self.parar(motivo)
            return
        tope, info = evaluar_kill_v3(pos, {**KILL_BRAZO_V3, "sigma1": math.inf}, t_tanda=t_t)               # (b) tope de TANDA: para ESTA ejecucion, sin kill persistente
        if tope and not self.tanda_agotada:
            self.tanda_agotada = (f"tope de tanda {self.brazo}: perdida de esta ejecucion {info['perdida_tanda']} $ >= {KILL_BRAZO_V3['tope_tanda_usd']} $ "
                                  f"(acumulado {info['perdida']} $)")
            self._log_durable({"tipo": "tope_tanda", "motivo": self.tanda_agotada, "info": info})
            self.parar(self.tanda_agotada)

    def _vigilar_kill_brazo(self, ahora):
        """Gamma bloquea hasta KILL_BRAZO_TIMEOUT_S: nunca con orden viva/cancelada, ni con un mercado activo, ni a < KILL_BRAZO_GUARDA_S de la apertura del siguiente 5m
        cotizable; como mucho KILL_BRAZO_MAX_CONSULTAS por pasada, ROTANDO candidatos. Un fallo de gamma NO apaga la evaluacion (se evalua con los desenlaces ya cacheados) y,
        si una posicion no se resuelve (intentos/minutos), se pasa a fail-closed: no se postean pujas nuevas."""
        if not self.real or self.kill_brazo or ahora - self._ult_kb < KILL_BRAZO_CADA_S or self.vivas or self.canceladas:
            return
        c_sig = (int(ahora // 900) + 1) * 900
        if c_sig - 300 - KILL_BRAZO_GUARDA_S <= ahora < c_sig or any(isinstance(x, H.Ctx) and x.fase == "activa" for x in self.ctxs.values()):
            return
        self._ult_kb = ahora
        try:
            pos = self.posiciones_brazo()
            self._resolver_pendientes(pos, ahora, KILL_BRAZO_MAX_CONSULTAS)
            pos = self.posiciones_brazo()
        except Exception as e:
            self.sin_desenlace = f"posiciones del brazo ilegibles: {type(e).__name__}: {str(e)[:100]}"
            self._log47({"tipo": "kill_brazo_error", "e": self.sin_desenlace})
            return
        m = self._motivo_sin_desenlace(pos, ahora)
        if m != self.sin_desenlace:
            self.sin_desenlace = m
            self._log47({"tipo": "kill_brazo_sin_desenlace", "motivo": m})
        self._evaluar_kill(pos)

    def _puerta(self, ahora):
        """Puerta de arranque: ANTES de la primera orden de una tanda se resuelven las posiciones pendientes de tandas anteriores y se evalua el kill acumulado. Si no se
        pueden resolver (gamma, relleno incierto) no se postea (fail-closed); se reintenta cada PUERTA_REINTENTO_S. Sin ordenes vivas (aqui se puede bloquear)."""
        if self.puerta_ok:
            return True
        if ahora - self._ult_puerta < PUERTA_REINTENTO_S or self.vivas or self.canceladas:
            return False
        self._ult_puerta = ahora
        try:
            pos = self.posiciones_brazo()
            self._resolver_pendientes(pos, ahora, PUERTA_MAX_CONSULTAS)
            pos = self.posiciones_brazo()
        except Exception as e:
            self._log47({"tipo": "puerta_arranque_error", "e": f"{type(e).__name__}: {str(e)[:120]}"})
            return False
        self._evaluar_kill(pos)
        if self.kill_brazo or self.tanda_agotada:
            return False
        pend = [p["slug"] for p in pos if p["gana"] is None]
        if pend:
            self._log47({"tipo": "puerta_arranque_pendiente", "pendientes": pend[:10], "n": len(pend)})
            return False
        self.puerta_ok = True
        self._log47({"tipo": "puerta_arranque_ok", "posiciones": len(pos)})
        return True

    # ---- decision
    def decidir(self, c, T, ahora):
        self._fijar_lado(c)
        self.sincronizar_rellenos(c)
        if c.tc is None:
            return
        tok = c.tc
        e = c.estado[tok]
        o = self.vivas.get(e["oid"]) if e["oid"] else None
        if o is not None:
            self._marcar_visto(c, tok, e, o, ahora)
        if e["cerrado"] or e["llenas"] > 1e-9:                       # un relleno (aunque parcial) cierra la puja
            e["cerrado"] = True
            c.fin_puja = c.fin_puja or "relleno"
            if o is not None and self.cancelar(e["oid"]):
                self.liquidar(e["oid"], o, True, c.estado, c.lib, T)
                e["oid"] = None
            return
        if o is not None:
            self._reaccion_viva(c, T, ahora, "decidir")
            return
        # ---- sin orden viva: ¿pujar? (mismos topes que H47)
        objetivo = self._objetivo(c, None)
        if objetivo is None or self.parada or self.kill or self.senal or self.kill_brazo:
            return
        if any(x["tok"] == tok for x in self.canceladas.values()):
            return                                                    # cancelada sin asentar: no se repone todavia (>= 1,5 s)
        if time.time() < self.enfriar_tok.get(tok, 0) or ahora - c.t_accion < H.MIN_ENTRE_ACCIONES_S:
            return
        if c.mk["slug"] not in self.slugs_usados:
            if self.n_usadas() >= self.n_max or len(self.pujas_en_libro() - {c.mk["slug"]}) >= self.max_vivas:
                return
        if len(self.vivas) + len(self.canceladas) >= self.max_vivas:
            return
        if c.n_ord >= min(R.CONFIG["max_cotiz_por_mercado"], H.MAX_ORDENES_PUJA) or self.n_ordenes_total >= H.MAX_ORDENES_TOTAL:
            c.fin_puja = c.fin_puja or "tope_ordenes"
            e["cerrado"] = True
            return
        size = H.tamano_orden(objetivo, self.size, self.min_nocional)
        if size is None:
            self._bloqueo(("tam", objetivo), {"tipo": "bloqueo_tamano", "precio": objetivo})
            return
        mn = c.mk.get("min_size")
        if mn is not None and size < float(mn) - 1e-9:
            self._bloqueo(("minsize",), {"tipo": "bloqueo_min_size_mercado", "min": mn, "size": size})
            return
        if self.sin_desenlace or not self._puerta(ahora):           # fail-closed: kill ciego o posiciones previas sin resolver
            return
        if not self.puede_enviar(size * objetivo):
            return
        if c.mk["fin"] - time.time() <= self.t_stop + 2 or c.lib.tick_cambiado:
            return
        b, a = c.lib.top(tok)
        cola_dec = c.lib.tamano_nivel(tok, objetivo)
        n_ev = len(X.leer_ledger())
        lp = LibPost(self, c, objetivo)                              # revalida la regla H23 TRAS firmar y antes de post_order
        h = self.post(c.mk["slug"], tok, c.lados[tok], objetivo, size, cola_dec, lib=lp, ajeno_dec=c.lib.mejor_bid_ajeno(tok),
                      ask_dec=a[0] if a else None, fin=c.mk["fin"])
        c.t_accion = time.time()
        if h is None and lp.motivo is not None:
            self._log47({"tipo": "h23_revalida_aborta", "slug": c.mk["slug"], **lp.motivo})
        if h is not None or any(ev.get("tipo") == "intencion_post" and ev.get("slug") == c.mk["slug"] for ev in X.leer_ledger()[n_ev:]):
            self.slugs_usados.add(c.mk["slug"])
            c.tok = c.tok or tok
        if h is None:
            return
        e["oid"] = h
        c.hashes.append(h)
        c.n_ord += 1
        c.posteado = True
        b15 = c.lib.top(c.to)[0]
        self._log47({"tipo": "puja_post", "oid": h, "slug": c.mk["slug"], "coin": "btc", "lado": c.lados[tok], "precio": objetivo,
                     "size": size, "cola": cola_dec, "libro": self._libro5(c.lib, tok), "bid15": b15[0] if b15 else None,
                     "T": round(c.mk["fin"] - time.time(), 2), "n_orden": c.n_ord, "t_dec": ahora})
        if c.libro_dec is None:
            c.libro_dec = self._libro5(c.lib, tok)


# ------------------------------------------------------------------ puertas del modo real
def h47b_terminado(eventos, sha_h47=None):
    """(ok, motivo) sobre el ledger de H47-B: tras su ULTIMO `config` real debe haber un `fin_ejecucion` real sin kill y sin ordenes abiertas sin
    verificar; ademas sin kill pendiente (ultimo `kill` sin `kill_rearmado` posterior). Fail-closed ante cualquier duda."""
    cfg = fin = None
    pend = None
    for i, e in enumerate(eventos):
        if not isinstance(e, dict) or not e.get("real"):
            continue
        t = e.get("tipo")
        if t == "config":
            cfg, fin = i, None
        elif t == "fin_ejecucion" and cfg is not None:
            fin = i
        elif t == "kill":
            pend = e.get("motivo") or "kill"
        elif t == "kill_rearmado":
            pend = None
    if cfg is None:
        return False, "el ledger de H47-B no tiene ningun `config` real: no hay evidencia de que haya corrido"
    if fin is None:
        return False, "H47-B no ha terminado: tras su ultimo `config` real no hay `fin_ejecucion` (en curso o muerto sin cerrar)"
    f = eventos[fin]
    c0 = eventos[cfg]
    if c0.get("escalon") != "B":
        return False, f"el ultimo config del ledger no es del escalon B (escalon {c0.get('escalon')!r})"
    try:
        if int(c0["n_max"]) < int(H.N_MAX["B"]):
            return False, f"H47-B corrio con n_max {c0['n_max']} < {H.N_MAX['B']} (el escalon B completo)"
        if abs(float(c0["t_stop"]) - float(H.T_STOP_DEF)) > 1e-9:
            return False, f"H47-B corrio con t_stop {c0['t_stop']} != {H.T_STOP_DEF}"
    except (KeyError, TypeError, ValueError):
        return False, "config.n_max/t_stop ilegibles: no se puede comprobar el escalon B completo"
    if sha_h47 is not None and c0.get("codigo_sha") != sha_h47:
        return False, f"H47-B corrio con otro codigo (config.codigo_sha {c0.get('codigo_sha')!r} != h47 del OK {sha_h47!r})"
    if f.get("parada"):
        return False, f"H47-B termino por parada ({str(f.get('parada'))[:160]}), no por N alcanzado"
    try:
        n_max, pujas = int(c0["n_max"]), int(f["pujas"])
    except (KeyError, TypeError, ValueError):
        return False, "config.n_max o fin_ejecucion.pujas ilegibles: no se puede comprobar que H47-B llego a su N"
    if pujas < n_max:
        return False, f"H47-B no llego a su N (pujas {pujas} < n_max {n_max}): abortado, Ctrl-C o senal"
    if f.get("kill"):
        return False, f"H47-B termino con kill: {str(f.get('kill'))[:160]}"
    if f.get("abiertas_sin_verificar"):
        return False, f"H47-B termino con {f.get('abiertas_sin_verificar')} ordenes abiertas sin verificar"
    if pend:
        return False, f"H47-B tiene un kill sin rearmar: {str(pend)[:160]}"
    return True, f"H47-B terminado sin kill (pujas {f.get('pujas')}, ordenes {f.get('ordenes')}, parada {f.get('parada')})"


def leer_ledger_ruta(ruta):
    """(eventos, lineas_ilegibles_tras_el_ultimo_config) de un ledger JSONL; (None, 0) si no existe. No usa la cache global de X (no toca el
    ledger propio). Una linea cortada antes del ultimo `config` no importa; despues, bloquea (fail-closed)."""
    if not Path(ruta).exists():
        return None, 0
    ev, malas = [], 0
    for ln in Path(ruta).read_text().splitlines():
        if not ln.strip():
            continue
        try:
            e = json.loads(ln)
        except ValueError:
            malas += 1
            continue
        ev.append(e)
        if isinstance(e, dict) and e.get("real") and e.get("tipo") == "config":
            malas = 0
    return ev, malas


def exigir_puertas(real, ok_final, ledger_b=None):
    """Real SOLO con: (1) H47-B terminado sin kill (se LEE su ledger), (2) fichero de OK de Javi con el MISMO texto que la bandera y ligado al sha de
    ESTE fichero y al hash de la regla (fail-closed). No hace nada en seco."""
    if not real:
        return
    if not ok_final or not ok_final.strip():
        sys.exit("real exige --ok-final-javi con el texto del OK final de Javi")
    if not OK_FICHERO.exists():
        sys.exit(f"falta {OK_FICHERO} (lo crea el chief tras el OK FINAL de Javi, H47-B y el /code-review): no se envia nada")
    txt = OK_FICHERO.read_text().strip()
    if txt != ok_final.strip():
        sys.exit("el texto de --ok-final-javi no coincide con el fichero de OK")
    if f"sha={sha_propio()}" not in txt or f"regla={HASH_REGLA}" not in txt:
        sys.exit(f"el OK no esta ligado a ESTE codigo: debe contener `sha={sha_propio()}` y `regla={HASH_REGLA}` (cualquier cambio del fichero o de "
                 "la regla invalida el OK; reemitirlo tras el /code-review del fichero actual)")
    if f"kill={hash_kill_v3()}" not in txt:
        sys.exit(f"el OK no liga el kill V3 de brazo: debe contener `kill={hash_kill_v3()}` (cualquier cambio de parametros/funcion invalida el OK)")
    deps = sha_dependencias()
    falta = [f"{k}={v}" for k, v in deps.items() if f"{k}={v}" not in txt]
    if falta:
        sys.exit(f"el OK no liga las dependencias que ejecuta el paquete: faltan {falta} (imprimir con --imprimir-sha; reemitir el OK)")
    ruta = ledger_b if ledger_b is not None else H47B_LEDGER
    eventos, malas = leer_ledger_ruta(ruta)
    if eventos is None:
        sys.exit(f"falta el ledger de H47-B ({ruta}): no hay evidencia de H47-B terminado; no se envia nada")
    if malas:
        sys.exit(f"el ledger de H47-B tiene {malas} linea(s) ilegible(s): revisar antes de dar por terminado H47-B (fail-closed)")
    ok, motivo = h47b_terminado(eventos, sha_h47=deps["h47"])
    if not ok:
        sys.exit(f"puerta H47-B: {motivo}")
    print(f"puerta H47-B ok: {motivo}", flush=True)


def configurar_rutas(real, brazo):
    esc = "H23" if brazo == "A" else "H23B"
    H.configurar_rutas(real, esc, T_STOP_H23)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--brazo", default="A", choices=tuple(R.CONFIG["brazos"]))
    ap.add_argument("--n", type=int, default=None, help="mercados con intencion (<= N_MAX['H23'] = 40)")
    ap.add_argument("--confirmo-dinero-real", action="store_true")
    ap.add_argument("--ok-final-javi", default=None)
    ap.add_argument("--imprimir-sha", action="store_true", help="imprime sha=<fichero> regla=<hash> para el fichero de OK y sale")
    ap.add_argument("--rearmar-kill-brazo", default=None, metavar="MOTIVO", help="rearma el kill de brazo del ledger de --brazo (solo real; lock)")
    ap.add_argument("--aceptar-linea-ilegible-brazo", default=None, metavar="MOTIVO",
                    help="acepta (auditado: muestra la linea, motivo, confirmacion escrita, fsync) lineas ilegibles que parezcan un JSON cortado en los ledgers del brazo (solo real)")
    ap.add_argument("--size", type=int, default=5)
    ap.add_argument("--min-nocional", type=float, default=1.0)
    ap.add_argument("--presupuesto-util", type=float, default=H.PRESUPUESTO_UTIL)
    ap.add_argument("--max-vivas", type=int, default=2)
    ap.add_argument("--duracion-max-min", type=float, default=None)
    a = ap.parse_args(argv)
    if a.imprimir_sha:
        print(f"sha={sha_propio()} regla={HASH_REGLA} " + " ".join(f"{k}={v}" for k, v in sha_dependencias().items()) + f" kill={hash_kill_v3()}")
        return 0
    real = a.confirmo_dinero_real
    exigir_puertas(real, a.ok_final_javi)
    configurar_rutas(real, a.brazo)
    if a.rearmar_kill_brazo is not None:
        if not real or not a.rearmar_kill_brazo.strip():
            sys.exit("--rearmar-kill-brazo exige --confirmo-dinero-real y un motivo no vacio")
        import fcntl
        fd = open(X.LOCK, "w")
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError:
            sys.exit("otra instancia sigue activa (lock)")
        X._CACHE = None
        try:
            k = estado_acumulado(a.brazo)["pendiente"]
        except LedgerBrazoIlegible as e:
            sys.exit(f"ledger hermano ilegible ({e}): no se rearma (fail-closed)")
        if not k:
            sys.exit("no hay kill de brazo pendiente")
        X.log({"tipo": "kill_brazo_rearmado", "real": True, "motivo": a.rearmar_kill_brazo[:300], "kill": str(k)[:300]})
        try:
            H._fsync_ledger()                                       # el rearme llega a disco antes de seguir (si no, no se da por rearmado)
        except Exception as e:
            sys.exit(f"no se pudo hacer fsync del rearme ({type(e).__name__}): comprobar el ledger antes de relanzar")
        print("kill de brazo rearmado; relanzar sin --rearmar-kill-brazo")
        return 0
    if a.aceptar_linea_ilegible_brazo is not None:
        if not real or not a.aceptar_linea_ilegible_brazo.strip():
            sys.exit("--aceptar-linea-ilegible-brazo exige --confirmo-dinero-real y un motivo no vacio")
        import fcntl
        fd = open(X.LOCK, "w")
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError:
            sys.exit("otra instancia sigue activa (lock)")
        X._CACHE = None
        ev = aceptar_lineas_brazo(a.brazo, a.aceptar_linea_ilegible_brazo)
        print("lineas aceptadas: relanzar sin --aceptar-linea-ilegible-brazo" if ev else "sin cambios")
        return 0
    if real:
        try:
            k = estado_acumulado(a.brazo)["pendiente"]
        except LedgerBrazoIlegible as e:
            sys.exit(f"ledger hermano del brazo ilegible ({e}): el acumulado del kill no es fiable, no se opera (fail-closed)")
        if k:
            sys.exit(f"kill de brazo pendiente ({k[:200]}): revisar y rearmar con --rearmar-kill-brazo")
        _ = H.tomar_lock_pares()
    sys.path.insert(0, str(AQUI / "experimentos/5m_barato/h23_maker"))
    import h23_shadow as S                       # Refs (solo lectura del CSV de PolyBolt)
    refs = S.Refs()
    ex = Exp23(real, a.brazo, a.n, a.size, a.min_nocional, a.presupuesto_util, a.max_vivas, refs=refs)
    print(f"{'REAL' if real else 'ENSAYO EN SECO'} H23 brazo {a.brazo}: N={ex.n_max} (ya usadas {ex.n_usadas()}); kill={ex.kill}; ledger {X.LEDGER}", flush=True)
    if real and ex.kill:
        sys.exit("kill pendiente: revisar y rearmar (con el rearme de H47)")
    ex.run(duracion_max_s=a.duracion_max_min * 60 if a.duracion_max_min else None)
    return 0


if __name__ == "__main__":
    sys.exit(main())
