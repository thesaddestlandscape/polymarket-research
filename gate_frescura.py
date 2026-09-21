#!/usr/bin/env python3
"""gate_frescura.py -- guardia de ANTIGUEDAD compartida para los JSON de gates que deciden
dinero real (21-Sep, aprobado por Javi).

Hueco encontrado el 21-Sep: bot_wallets_gate_bucket.py y candidata9_gate_bucket.py leian su JSON en
caliente (cache por mtime) SIN ningun limite de edad -- si el vigia diario que lo regenera fallaba
(OOM, timeout: visto 81 veces seguidas en el grid de WALLET_MIRROR), el ejecutor real seguia
operando con veredictos de hace dias. wallet_mirror_gate_bucket.py (2h15) y gate_bucket_propio.py
(30h) ya tenian guardia; estos dos no.

Regla: FAIL-CLOSED. Fichero ausente, ilegible o mas viejo que su maximo -> no es fresco -> no se opera.
Solo afecta a las rutas de DINERO REAL (permitido_real / evaluar_para_recheck); `evaluar()` (tracking
del dry-run) no se toca."""
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent
SHADOW = REPO / "data" / "shadow"

# 24h de cron diario + 6h de margen: mismo criterio que gate_bucket_propio.MAX_ANTIGUEDAD_S.
MAX_ANTIGUEDAD_DIARIO_S = 30 * 3600
# Gates horarios (regenerados por vigias_frecuentes_fase0): mismo valor que
# wallet_mirror_gate_bucket.MAX_ANTIGUEDAD_S (2 x 3600 + 900).
MAX_ANTIGUEDAD_HORARIO_S = 2 * 3600 + 900

# Registro para el informe diario de salud (mantener en sync con los modulos que los leen).
GATES_CRITICOS = {
    "bot_wallets_gate_bucket.json": MAX_ANTIGUEDAD_DIARIO_S,
    "bot_wallets_edge_medido_real.json": MAX_ANTIGUEDAD_DIARIO_S,
    "candidata9_10_gate_bucket.json": MAX_ANTIGUEDAD_DIARIO_S,
    "candidata9_edge_medido_real.json": MAX_ANTIGUEDAD_DIARIO_S,
    "gate_bucket_propio.json": MAX_ANTIGUEDAD_DIARIO_S,
    "wallet_mirror_gate_bucket.json": MAX_ANTIGUEDAD_HORARIO_S,
    "wallet_mirror_gate_bucket_fino.json": MAX_ANTIGUEDAD_HORARIO_S,
}

_ultimo_aviso: dict = {}
AVISO_CADA_S = 3600


def antiguedad_s(path: Path):
    """Segundos desde la ultima modificacion, o None si no existe/no se puede leer."""
    try:
        return time.time() - Path(path).stat().st_mtime
    except OSError:
        return None


def esta_fresco(path: Path, max_s: float = MAX_ANTIGUEDAD_DIARIO_S) -> bool:
    a = antiguedad_s(path)
    return a is not None and a <= max_s


def avisar_obsoleto(path: Path, max_s: float = MAX_ANTIGUEDAD_DIARIO_S) -> None:
    """Deja rastro en el log del ejecutor (como mucho 1 vez/hora por fichero) cuando la guardia bloquea."""
    nombre = Path(path).name
    ahora = time.time()
    if ahora - _ultimo_aviso.get(nombre, 0.0) < AVISO_CADA_S:
        return
    _ultimo_aviso[nombre] = ahora
    a = antiguedad_s(path)
    edad = "no existe" if a is None else f"{a / 3600:.1f}h"
    print(f"[gate_frescura] ⛔ {nombre} OBSOLETO ({edad} > {max_s / 3600:.1f}h) -- FAIL-CLOSED: "
          f"no se opera con este gate hasta que se regenere", flush=True)


def _umbrales_desalineados() -> list:
    """gate_bucket_propio y wallet_mirror_gate_bucket conservan SU PROPIA constante de antiguedad. Si
    alguien cambia una y no la otra, el informe de salud alertaria con un umbral distinto del que bloquea
    al ejecutor. Se compara aqui (import perezoso) y se reporta la deriva."""
    out = []
    for modulo, esperado in (("gate_bucket_propio", MAX_ANTIGUEDAD_DIARIO_S),
                             ("wallet_mirror_gate_bucket", MAX_ANTIGUEDAD_HORARIO_S)):
        try:
            real = getattr(__import__(modulo), "MAX_ANTIGUEDAD_S")
        except Exception:
            continue
        if real != esperado:
            out.append({"gate": modulo, "antiguedad_h": None, "maximo_h": round(esperado / 3600, 2),
                        "nota": f"umbral desalineado: {modulo}.MAX_ANTIGUEDAD_S={real / 3600:.2f}h "
                                f"vs gate_frescura={esperado / 3600:.2f}h"})
    return out


def informe_gates() -> list:
    """Para analisis_diario_salud_sistema: gates criticos obsoletos o ausentes (+ deriva de umbrales)."""
    malos = _umbrales_desalineados()
    for nombre, max_s in GATES_CRITICOS.items():
        a = antiguedad_s(SHADOW / nombre)
        if a is None or a > max_s:
            malos.append({"gate": nombre, "antiguedad_h": None if a is None else round(a / 3600, 1),
                          "maximo_h": round(max_s / 3600, 2)})
    return malos
