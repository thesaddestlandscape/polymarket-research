#!/usr/bin/env python3
"""Criterio ÚNICO del filtro wallet+micro-bucket de Wallet Mirror (cripto y sports) — 14-Oct (OK Javi: "que opere con
sentido y sin riesgo"). Sin dependencias de cripto ni de sports: cada llamador pasa su función de equilibrio con SU
comisión real (cripto: wallet_mirror_tracker; sports: sports_wallet_mirror_frescura con sports_resolve.FEE).

Antes, cada módulo exigía Wilson90 BAJO del acierto reciente > 0,50 FIJO en cada (wallet, bucket): en un bucket barato
el equilibrio es ~precio, así que vetaba TODO bucket < 0,40 (cripto: 0 de 183 combinaciones aprobadas por debajo) y WM
BTC 15m [0,35-0,40) bueno_confirmado no podía operar; y en los caros pedía 7/8 sin mirar el precio.

Ahora, con las últimas `n_rec` copias resueltas de la wallet en ESE bucket (acierto en términos de NUESTRA posición):
  1. menos de n_rec copias -> veto "sin_evidencia" (fail-closed);
  2. degradada frente a su propio histórico del bucket (Wilson90 alto < histórico − margen_pp) -> veto "degradada";
  3. acierto reciente < equilibrio al PRECIO MEDIO del bucket + MARGEN_EQUILIBRIO -> veto "bajo_equilibrio": sus
     últimas copias no ganan dinero a este precio con colchón.
Con n=8 este filtro NO confirma edge (no tiene potencia): aparta wallets que hoy pierden en ese precio. La edge del
bucket la exige el gate bueno_confirmado del ejecutor, que se comprueba antes. Respecto a la regla vieja: abre los
buckets baratos y, en los medios/altos, pide el acierto que da dinero a ese precio + 5 pp (p. ej. 6/8 a 0,65 en vez de
7/8) — cambio consciente, revisado (/code-review medium 14-Oct).
"""
MARGEN_EQUILIBRIO = 0.05


def equilibrio_por_accion(p: float, fee: float) -> float:
    """Comisión tomadora fee·p·(1−p) por ACCIÓN (cripto): acierto mínimo h = p·(1 + fee·(1−p))."""
    return p * (1.0 + fee * (1.0 - p))


def equilibrio_ganadoras(p: float, fee: float) -> float:
    """Comisión fee·(1−p) por € SOLO en ganadoras (sports): h = p / (1 − fee·p·(1−p))."""
    return p / (1.0 - fee * p * (1.0 - p))


def evaluar_bucket(aciertos_pos: list, b: float, step: float, equilibrio, n_rec: int, min_antiguos: int,
                   margen_pp: float, wilson_ci):
    """aciertos_pos: aciertos (0/1) de NUESTRA posición, en orden cronológico, de una (wallet, bucket).
    equilibrio: función p -> acierto mínimo con la comisión del llamador. wilson_ci: la del llamador (Z 90 %).
    Devuelve (aprobada: bool, motivo: str, info: dict)."""
    if len(aciertos_pos) < n_rec:
        return False, f"sin_evidencia (n={len(aciertos_pos)}<{n_rec})", {}
    recientes = aciertos_pos[-n_rec:]
    k, n = sum(recientes), len(recientes)
    antiguos = aciertos_pos[:-n_rec]
    if len(antiguos) >= min_antiguos:
        hist = sum(antiguos) / len(antiguos)
        if wilson_ci(k, n)[1] * 100 < hist * 100 - margen_pp:
            return False, f"degradada ({k}/{n} vs histórico {hist:.0%})", {}
    exige = equilibrio(min(0.99, round(b + step / 2, 4))) + MARGEN_EQUILIBRIO
    if k / n < exige:
        return False, f"bajo_equilibrio ({k}/{n} < {exige:.2f})", {}
    return True, "ok", {"n": n, "hit_posicion_reciente": round(k / n, 4)}
