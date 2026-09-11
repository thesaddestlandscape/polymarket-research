#!/usr/bin/env python3
"""Vigía de cobertura: detecta estrategias ACTIVAS (con volumen real de
predicciones) que el pipeline causal (FEATURE_RULES en shadow_postmortem.py)
todavía no mira, ni en agregado ni por activo.

Origen (12-Jul): auditoría manual encontró 11 estrategias con volumen real
(89 a 838 predicciones/3 días) sin NINGÚN aprendizaje causal — incluida
FAVORITO_CONFIRMADO, candidata top a whitelist ese mismo día. El punto
ciego llevaba semanas sin que nadie lo revisara. Petición explícita de
Javi: este tipo de gap debe auto-detectarse, no depender de que alguien
se acuerde de auditar. Ver [[project_desagregacion_feature_rules_12jul]].

Chequea: para cada estrategia con n>=UMBRAL_N en los últimos 3 días,
¿tiene AL MENOS una clave en FEATURE_RULES (incluida la agregada)? Y si
opera en >1 activo, ¿tiene claves por activo (no solo la agregada)? Avisa
por Telegram (latch por estrategia, no repite hasta que se resuelva y
vuelva a aparecer). Read-only, no toca dinero ni config.
"""
import json
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

import shadow_postmortem as sp  # noqa: E402 — reusa FEATURE_RULES real, no una copia

LATCH = REPO / "data/live/vigia_cobertura_feature_rules_latch.json"
UMBRAL_N = 50  # mismo orden de magnitud que las estrategias detectadas 12-Jul
DIAS = 3


def _predicciones_recientes():
    import csv
    contador = Counter()
    activos_por_estrategia = defaultdict(set)
    hoy = datetime.now(timezone.utc).date()
    for delta in range(DIAS):
        fecha = (hoy - timedelta(days=delta)).isoformat()
        path = REPO / f"data/shadow/predictions_{fecha}.csv"
        if not path.exists():
            continue
        with open(path, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                strat = row.get("strategy", "")
                sub = row.get("subtype", "")
                contador[strat] += 1
                activo = sub.split("#", 1)[0] if sub else ""
                if activo:
                    activos_por_estrategia[strat].add(activo)
    return contador, activos_por_estrategia


def _tiene_cobertura(strat, activos):
    claves = set(sp.FEATURE_RULES.keys())
    tiene_agregada = strat in claves
    tiene_por_activo = any(k.startswith(f"{strat}#{a}") for k in claves for a in activos)
    multi_activo = len(activos) > 1
    if multi_activo:
        return tiene_agregada or tiene_por_activo, tiene_por_activo
    return tiene_agregada, True  # single-asset: "por activo" no aplica


def main() -> int:
    from shadow_digest import enviar_telegram

    contador, activos_por_estrategia = _predicciones_recientes()
    try:
        latch = json.loads(LATCH.read_text()) if LATCH.exists() else {}
    except Exception:
        latch = {}

    gaps = []
    for strat, n in contador.items():
        if n < UMBRAL_N:
            continue
        activos = activos_por_estrategia.get(strat, set())
        cubierta, por_activo = _tiene_cobertura(strat, activos)
        multi = len(activos) > 1
        if not cubierta:
            gaps.append((strat, n, activos, "SIN NINGÚN aprendizaje causal"))
        elif multi and not por_activo:
            gaps.append((strat, n, activos, "solo agregado, sin desagregar por activo"))

    print(f"[vigia_cobertura] {len(contador)} estrategias con predicciones últimos {DIAS}d, "
          f"{len(gaps)} con gap (n>={UMBRAL_N})")

    nuevos = [g for g in gaps if not latch.get(g[0], {}).get("avisado")]
    if nuevos:
        detalle = "\n".join(
            f"  {s}: n={n}/{DIAS}d, activos={sorted(a)} — {motivo}"
            for s, n, a, motivo in nuevos
        )
        msg = (
            f"🔍 VIGÍA cobertura FEATURE_RULES: {len(nuevos)} estrategia(s) con volumen "
            f"real y aprendizaje causal incompleto\n{detalle}\n"
            f"Añadir a FEATURE_RULES en shadow_postmortem.py (ver ejemplos 12-Jul)."
        )
        ok = enviar_telegram(msg)
        print(f"[vigia_cobertura] aviso enviado (telegram={ok})")
        for s, *_ in nuevos:
            latch[s] = {"avisado": True}

    # Resetear latch de estrategias ya resueltas (para que un gap NUEVO en el
    # futuro (ej. estrategia recién creada) sí pueda volver a avisar).
    resueltas = set(latch.keys()) - {g[0] for g in gaps}
    for s in resueltas:
        latch.pop(s, None)

    LATCH.write_text(json.dumps(latch, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"[vigia_cobertura] ERROR {type(e).__name__}: {e}")
        sys.exit(0)
