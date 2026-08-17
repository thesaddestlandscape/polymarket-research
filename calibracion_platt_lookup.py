"""
calibracion_platt_lookup.py — 17-Ago. Aplica la corrección Platt granular
(calibracion_platt_granular.json, calculada por
analisis_calibracion_platt_granular.py) a estrategias que NO pasan por el
loop genérico de shadow_predict.py::_buscar_calibracion() — hoy, los
ejecutores de baja latencia de ballenas (ballenas_executor_5min.py,
ballenas_executor_btc15m.py), que calculan prob_yes_modelo (prob_bucket)
fuera de ese loop y por tanto nunca recibían la corrección.

Bug real encontrado 17-Ago (barrido de salud / auditoría de calibración,
CLAUDE.md pt.2): BALLENAS_TARDIAS es "mal_calibrado_confirmado" en
gate_calibracion.json (n=2661, gap_medio=+0.0063, CI90% no cruza 0) pero
NINGUNA corrección granular llegaba a aplicarse nunca -- el propio fichero
calibracion_platt_granular.json ya tenía una corrección VALIDADA
(BALLENAS_TARDIAS#DOGE#5min, n_oos_validado=130, mejora_media_oos=+0.0373)
completamente sin usar porque estos dos ejecutores nunca la consultaban.

Mismo criterio de seguridad que _buscar_calibracion() en shadow_predict.py
(fail-closed: sin fichero, sin clave, o calibracion_prob=null -> prob_bucket
crudo sin tocar, exactamente el comportamiento actual). Módulo deliberadamente
pequeño y sin dependencias pesadas -- los ejecutores de ballenas son
sensibles a latencia.
"""
import json
import math
from pathlib import Path

_PATH = Path(__file__).resolve().parent / "data" / "shadow" / "calibracion_platt_granular.json"
_cache = {"mtime": None, "datos": {}}


def _norm_cdf(x):
    if x < -8.0: return 0.0
    if x >  8.0: return 1.0
    sign = 1.0 if x >= 0 else -1.0
    x = abs(x)
    t = 1.0 / (1.0 + 0.2316419 * x)
    d = 0.3989422820 * math.exp(-0.5 * x * x)
    p = d * t * (0.3193815302
        + t * (-0.3565637813
        + t * (1.7814779372
        + t * (-1.8212559978
        + t * 1.3302744929))))
    return 1.0 - p if sign > 0 else p


def _norm_ppf(p, lo=-8.0, hi=8.0, it=60):
    if p <= 1e-9: return -8.0
    if p >= 1 - 1e-9: return 8.0
    for _ in range(it):
        mid = (lo + hi) / 2
        if _norm_cdf(mid) < p:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def _datos() -> dict:
    try:
        mtime = _PATH.stat().st_mtime
    except OSError:
        return _cache["datos"]
    if _cache["mtime"] != mtime:
        try:
            _cache["datos"] = json.loads(_PATH.read_text(encoding="utf-8"))
            _cache["mtime"] = mtime
        except Exception:
            pass
    return _cache["datos"]


def entrada(nombre: str, activo: str, marco: str) -> dict | None:
    """(a,b) validado para nombre#activo#marco, o None si no hay clave o no
    pasó rigor -- llamar UNA vez por ventana/poll (no por banda de precio:
    la clave es (estrategia,activo,marco), no depende de la banda) y
    reusar el resultado con aplicar()."""
    try:
        entry = _datos().get(f"{nombre}#{activo}#{marco}")
        return entry.get("calibracion_prob") if entry else None
    except Exception:
        return None


def aplicar(calib: dict | None, prob_raw: float) -> float:
    """Aplica el (a,b) de entrada() a prob_raw -- si calib es None, devuelve
    prob_raw sin tocar (fail-closed). Nunca lanza excepción."""
    if not calib:
        return prob_raw
    try:
        return _norm_cdf(calib["a"] + calib["b"] * _norm_ppf(prob_raw))
    except Exception:
        return prob_raw


def calibrar(nombre: str, activo: str, marco: str, prob_raw: float) -> float:
    """Atajo entrada()+aplicar() para llamadas puntuales (una sola banda,
    ej. ballenas_executor_btc15m.py). Devuelve prob_raw recalibrado si
    existe una corrección Platt granular VALIDADA para nombre#activo#marco
    (ej. "BALLENAS_TARDIAS#ETH#5min") -- si no existe la clave, o existe
    pero calibracion_prob es null (evaluada y no pasó rigor), devuelve
    prob_raw sin tocar. Nunca lanza excepción."""
    return aplicar(entrada(nombre, activo, marco), prob_raw)
