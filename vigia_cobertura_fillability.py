#!/usr/bin/env python3
"""Vigía de cobertura: detecta tuplas (estrategia#subtype#dirección) que se
están ACERCANDO al gate de promoción a live (IC/n en strategy_params.json)
pero no tienen NINGÚN snapshot de fill-ability real (candidatos_evaluacion_live
ni pares_permitidos_live) — es decir, cuando crucen el gate lo harán con cero
dato sobre si de verdad se pueden ejecutar.

Origen (12-Jul): Javi preguntó explícitamente por los mercados de 5 minutos
y se encontró que NINGUNA de las 5 estrategias genuinamente 5min tenía nunca
un snapshot de fill-ability — LATE_WINDOW_5MIN#BTC estaba a 5 resoluciones
del gate estándar. Mismo patrón ya visto con WEEKLY_PRICE (semanas de gate
cumplido sin instrumentar). Análogo a vigia_cobertura_feature_rules.py pero
para instrumentación de fill-ability en vez de aprendizaje causal. Ver
[[project_mercados_5min_auditoria_12jul]].

Chequea: para cada tupla activa en strategy_params.json con ic_bayes>=UMBRAL_IC
y n>=UMBRAL_N_CERCA (acercándose al gate real IC>=0.08 n>=40, pero antes de
cruzarlo), ¿tiene AL MENOS una fila en libro_snapshots.csv (candidato_evaluacion
o motivo real) o está ya en pares_permitidos_live? Avisa por Telegram (latch
por tupla). Read-only, no toca dinero ni config.
"""
import csv
import json
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

STRATEGY_PARAMS = REPO / "data/shadow/strategy_params.json"
CONFIG = REPO / "data/live/config_live.json"
LIBRO = REPO / "data/live/libro_snapshots.csv"
LATCH = REPO / "data/live/vigia_cobertura_fillability_latch.json"

UMBRAL_IC = 0.08
UMBRAL_N_CERCA = 25  # "acercándose" al gate real (n>=40) sin haberlo cruzado todavía
UMBRAL_N_GATE = 40


def _tuplas_con_snapshot():
    tuplas = set()
    if not LIBRO.exists():
        return tuplas
    with open(LIBRO, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            strat = r.get("strategy", "")
            sub = r.get("subtype", "")
            dec = r.get("direction", "")
            if strat and sub and dec:
                tuplas.add(f"{strat}#{sub}#{dec}")
    return tuplas


def _subtypes_reales(dias=7):
    """Subtypes CONCRETOS realmente emitidos (mismo formato que usa
    live_trade.py) por estrategia, leídos de predictions_YYYY-MM-DD.csv
    recientes -- evita las claves 'rollup' de strategy_params.json (agregado
    por duración o por activo sin duración), que no son tuplas instrumentables
    de verdad y duplican cualquier gap 2-3 veces."""
    from datetime import datetime, timedelta, timezone
    subtypes = defaultdict(set)
    hoy = datetime.now(timezone.utc).date()
    for delta in range(dias):
        fecha = (hoy - timedelta(days=delta)).isoformat()
        path = REPO / f"data/shadow/predictions_{fecha}.csv"
        if not path.exists():
            continue
        with open(path, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                strat = row.get("strategy", "")
                sub = row.get("subtype", "")
                if strat and sub:
                    subtypes[strat].add(sub)
    return subtypes


def main() -> int:
    from shadow_digest import enviar_telegram

    params = json.loads(STRATEGY_PARAMS.read_text())
    est = params.get("estrategias", params)
    cfg = json.loads(CONFIG.read_text())
    cubiertas = set(cfg.get("candidatos_evaluacion_live", [])) | set(cfg.get("pares_permitidos_live", []))
    cubiertas |= _tuplas_con_snapshot()

    try:
        latch = json.loads(LATCH.read_text()) if LATCH.exists() else {}
    except Exception:
        latch = {}

    subtypes_reales = _subtypes_reales()

    gaps = []
    for strategy, subs in subtypes_reales.items():
        for subtype in subs:
            clave = f"{strategy}#{subtype}"
            v = est.get(clave)
            if not v:
                continue
            for direccion in ("BUY_YES", "BUY_NO"):
                ic = v.get(f"ic_{direccion}")
                n = v.get(f"n_{direccion}")
                if ic is None or n is None:
                    continue
                if ic < UMBRAL_IC or n < UMBRAL_N_CERCA:
                    continue
                tupla = f"{strategy}#{subtype}#{direccion}"
                if tupla in cubiertas:
                    continue
                estado = "YA CRUZÓ el gate" if n >= UMBRAL_N_GATE else f"a {UMBRAL_N_GATE - n} de cruzarlo"
                gaps.append((tupla, ic, n, estado))

    n_subtypes = sum(len(s) for s in subtypes_reales.values())
    print(f"[vigia_fillability] {n_subtypes} tupla(s) concreta(s) con predicciones recientes, {len(gaps)} sin cobertura")

    nuevos = [g for g in gaps if not latch.get(g[0], {}).get("avisado")]
    if nuevos:
        detalle = "\n".join(f"  {t}: ic={ic:+.3f} n={n} — {estado}" for t, ic, n, estado in nuevos)
        msg = (
            f"🔍 VIGÍA cobertura fill-ability: {len(nuevos)} tupla(s) acercándose/cruzando "
            f"el gate de IC sin NINGÚN dato real de profundidad\n{detalle}\n"
            f"Añadir a candidatos_evaluacion_live en config_live.json antes de proponer whitelist."
        )
        ok = enviar_telegram(msg)
        print(f"[vigia_fillability] aviso enviado (telegram={ok})")
        for t, *_ in nuevos:
            latch[t] = {"avisado": True}

    resueltas = set(latch.keys()) - {g[0] for g in gaps}
    for t in resueltas:
        latch.pop(t, None)

    LATCH.write_text(json.dumps(latch, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"[vigia_fillability] ERROR {type(e).__name__}: {e}")
        sys.exit(0)
