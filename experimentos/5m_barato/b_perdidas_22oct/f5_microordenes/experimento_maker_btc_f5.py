#!/usr/bin/env python3
"""experimento_maker_btc_f5.py -- F5: ENSAYO de micro-órdenes MAKER en BTC 5m banda de relleno 0,10-0,30 (observar ciclo de vida y selección adversa PROPIA).
ESTADO: BORRADOR EN DEV, NO REVISADO. No se ha ejecutado en real ni se ejecutará sin /code-review adversarial (MEDIUM) + OK final de Javi.
Sin --confirmo-dinero-real es un ENSAYO EN SECO (H47 no crea cliente CLOB, no firma, no envía; lee gamma + WS públicos).

QUÉ ES: una capa FINA sobre `experimento_maker_h47.py` (4 /code-review, 120 tests), que NO se edita (el working tree de dev tiene cambios sin commit de
otro agente). Esta capa solo (1) añade BTC a la tabla de k (k=1: follow-touch, top − 1 tick), (2) congela los parámetros del ensayo F5 y los EXIGE
(monedas=btc, N<=N_F5, presupuesto<=5, size=5, t_stop=60, max_vivas<=2, tope de órdenes por puja), (3) separa el LEDGER del de B (n_usadas y el tope N salen del
ledger propio) pero con un nombre que `ledgers_reales_hermanos()` y `reinicio_suelo_compartido` SÍ ven (suelo y cuadre compartidos con B y pares),
(4) en REAL exige un fichero de autorización escrito por el chief tras el OK de Javi cuyo contenido liga sha del código H47 + sha de este fichero + parámetros
(cualquier edición posterior invalida la autorización: fail-closed), (5) ventana horaria y carga del VPS.
La banda 0,10-0,30 es la de H35 (en_banda: bid top en (0,11, 0,30]; objetivo en [0,10, 0,30]); 0,05-0,10 queda FUERA: el nocional mínimo de 1 $ exigiría 11-20 acc (> SIZE_MAX=10 del código revisado).
No lee .env ni secretos (eso lo hace H47 solo en real, vía X.cliente_dedicado()).
Uso:  .venv/bin/python experimento_maker_btc_f5.py --escalon B --n 40 --duracion-max-min 120              (SECO)
      .venv/bin/python experimento_maker_btc_f5.py --escalon B --n 40 --confirmo-dinero-real            (REAL: solo con autorización)
"""
import argparse
import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

DEV = Path("/root/polymarket-research-dev")
sys.path.insert(0, str(DEV))
import experimento_maker_h47 as H                # noqa: E402
import experimento_pares_cola_15m as X           # noqa: E402

QUI = Path(__file__).resolve()
AUTORIZACION = H.DATALOGS / "f5_btc_autorizacion.json"   # lo escribe el CHIEF tras el OK de Javi; este script nunca lo crea

# ---- parámetros CONGELADOS ex ante (ESPECIFICACION.md §1). Cambiar uno = versión nueva del ensayo.
F5 = {
    "moneda": "btc", "k": 1, "t_stop": 60.0, "size": 5, "min_nocional": 1.0,
    "presupuesto_util": 5.0,          # pérdida máxima = tope de pruebas de Javi (5 €); el suelo de H47 lo hace cumplir (saldo − 5)
    "n_max_A": 20, "n_max_B": 40,     # N fijo de PUJAS (mercados con intención de POST); ver potencia en ESPECIFICACION §2
    "max_vivas": 2, "max_ordenes_puja": 25,   # B real llegó a 54 órdenes en una puja (tormenta de repegado): tope duro
    "hora_prohibida_utc": (6, 9),     # racimo de crons 06-09Z: latencia contaminada
    "carga_max_ratio": 3.0,           # load5/nproc > 3 sostenido = sobresuscripción real (CLAUDE.md): no se arranca
    "escalones": ("A", "B"),
}


# ---------------------------------------------------------------- reglas puras (probadas sin red)
def sha_fichero(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()[:16]


def validar_parametros(monedas, escalon, n, presupuesto, size, t_stop, max_vivas, min_nocional):
    """Lista de errores (vacía = válido). La capa NO relaja nunca lo congelado."""
    e = []
    if tuple(monedas) != (F5["moneda"],):
        e.append(f"monedas debe ser exactamente ('{F5['moneda']}',), recibido {tuple(monedas)}")
    if escalon not in F5["escalones"]:
        e.append(f"escalón {escalon!r} fuera de {F5['escalones']}")
    else:
        tope = F5["n_max_" + escalon]
        if n is None or not (1 <= n <= tope):
            e.append(f"--n debe estar en 1..{tope} (escalón {escalon})")
    if not (0 < presupuesto <= F5["presupuesto_util"] + 1e-9):
        e.append(f"presupuesto {presupuesto} fuera de (0, {F5['presupuesto_util']}]")
    if size != F5["size"]:
        e.append(f"size debe ser {F5['size']}")
    if abs(t_stop - F5["t_stop"]) > 1e-9:
        e.append(f"t_stop debe ser {F5['t_stop']}")
    if not (1 <= max_vivas <= F5["max_vivas"]):
        e.append(f"max_vivas en 1..{F5['max_vivas']}")
    if abs(min_nocional - F5["min_nocional"]) > 1e-9:
        e.append("min_nocional debe ser 1.0")
    return e


def hora_permitida(ahora_utc):
    """False en [06:00, 09:00) UTC (racimo de crons)."""
    lo, hi = F5["hora_prohibida_utc"]
    return not (lo <= ahora_utc.hour < hi)


def carga_ok(load5, nproc):
    """Fail-closed: carga ilegible -> no se arranca."""
    try:
        return float(load5) / max(1, int(nproc)) <= F5["carga_max_ratio"]
    except (TypeError, ValueError):
        return False


def clave_autorizacion(sha_h47, sha_f5, escalon, n, presupuesto):
    return {"sha_h47": sha_h47, "sha_f5": sha_f5, "escalon": escalon, "n": int(n), "presupuesto": float(presupuesto)}


def autorizacion_valida(auth, sha_h47, sha_f5, escalon, n, presupuesto, ahora_utc):
    """Devuelve (ok, motivo). auth = dict del fichero de autorización. Exige: mismas shas, mismo escalón, n <= autorizado, presupuesto <= autorizado, no caducada
    (campo `caduca_utc` ISO) y `ok_javi` de verdad (texto con fecha). Cualquier campo ausente -> NO."""
    if not isinstance(auth, dict):
        return False, "autorización ausente o ilegible"
    for k in ("sha_h47", "sha_f5", "escalon", "n", "presupuesto", "ok_javi", "caduca_utc"):
        if k not in auth:
            return False, f"falta {k}"
    if auth["sha_h47"] != sha_h47:
        return False, "el código de H47 cambió desde la autorización"
    if auth["sha_f5"] != sha_f5:
        return False, "este fichero cambió desde la autorización"
    if auth["escalon"] != escalon:
        return False, "escalón distinto del autorizado"
    try:
        if int(n) > int(auth["n"]) or float(presupuesto) > float(auth["presupuesto"]) + 1e-9:
            return False, "n o presupuesto por encima de lo autorizado"
        cad = datetime.fromisoformat(str(auth["caduca_utc"]).replace("Z", "+00:00"))
    except (TypeError, ValueError):
        return False, "n/presupuesto/caduca ilegibles"
    if cad.tzinfo is None or ahora_utc >= cad:
        return False, "autorización caducada (o sin zona horaria)"
    if not str(auth["ok_javi"]).strip():
        return False, "ok_javi vacío"
    return True, "ok"


def aplicar(h=H):
    """Añade BTC al código de H47 SIN editarlo: k=1 y tope de órdenes por puja. Devuelve lo previo para poder restaurar (tests)."""
    previo = (dict(h.K_POR_MONEDA), h.MAX_ORDENES_PUJA)
    h.K_POR_MONEDA[F5["moneda"]] = F5["k"]
    h.MAX_ORDENES_PUJA = min(h.MAX_ORDENES_PUJA, F5["max_ordenes_puja"])
    return previo


def restaurar(previo, h=H):
    h.K_POR_MONEDA.clear()
    h.K_POR_MONEDA.update(previo[0])
    h.MAX_ORDENES_PUJA = previo[1]


def rutas(real, escalon):
    """Ledger propio (n_usadas y N salen de él, no del de B) con nombre visible para ledgers_reales_hermanos() (real) o `_seco_` (seco).
    Un único .KILL y un único lock de la wallet, como H47."""
    H.configurar_rutas(real, f"F5BTC_{escalon}", F5["t_stop"])


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--escalon", choices=F5["escalones"], default="B")
    ap.add_argument("--n", type=int, default=None)
    ap.add_argument("--confirmo-dinero-real", action="store_true")
    ap.add_argument("--presupuesto-util", type=float, default=F5["presupuesto_util"])
    ap.add_argument("--duracion-max-min", type=float, default=None)
    a = ap.parse_args(argv)
    real = a.confirmo_dinero_real
    n = a.n if a.n is not None else F5["n_max_" + a.escalon]
    err = validar_parametros((F5["moneda"],), a.escalon, n, a.presupuesto_util, F5["size"], F5["t_stop"], F5["max_vivas"], F5["min_nocional"])
    if err:
        sys.exit("parámetros no válidos: " + "; ".join(err))
    ahora = datetime.now(timezone.utc)
    if real:
        if not hora_permitida(ahora):
            sys.exit("06:00-09:00Z: no se opera")
        try:
            la = float(open("/proc/loadavg").read().split()[1])
        except (OSError, ValueError, IndexError):
            sys.exit("carga ilegible: no se opera")
        if not carga_ok(la, os.cpu_count() or 1):
            sys.exit(f"load5 {la} demasiado alta para {os.cpu_count()} núcleos: no se opera")
        try:
            auth = json.loads(AUTORIZACION.read_text())
        except (OSError, ValueError):
            auth = None
        ok, motivo = autorizacion_valida(auth, sha_fichero(H.__file__), sha_fichero(QUI), a.escalon, n, a.presupuesto_util, ahora)
        if not ok:
            sys.exit(f"REAL sin autorización válida ({motivo}): {AUTORIZACION}")
    aplicar()
    argv47 = ["--escalon", "B" if a.escalon == "B" else "A", "--n", str(n), "--monedas", F5["moneda"], "--t-stop", str(int(F5["t_stop"])),
              "--size", str(F5["size"]), "--min-nocional", "1.0", "--presupuesto-util", str(a.presupuesto_util), "--max-vivas", str(F5["max_vivas"])]
    if a.duracion_max_min:
        argv47 += ["--duracion-max-min", str(a.duracion_max_min)]
    if real:
        argv47.append("--confirmo-dinero-real")
    # H47.main llama a configurar_rutas(real, escalon, t_stop) con su escalón: lo reconducimos al nuestro para que el ledger sea el de F5
    orig = H.configurar_rutas
    H.configurar_rutas = lambda r, e, t=F5["t_stop"]: orig(r, f"F5BTC_{e}", t)
    try:
        return H.main(argv47)
    finally:
        H.configurar_rutas = orig


if __name__ == "__main__":
    sys.exit(main())
