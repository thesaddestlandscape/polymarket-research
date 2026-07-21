#!/usr/bin/env python3
"""Vigía: avisa por Telegram (una vez, latch) cuando alguna de
BALLENAS_TARDIAS#{ETH,SOL,XRP}#5min#BUY_YES cruza n>=UMBRAL_N en
libro_snapshots.csv (motivo=candidato_evaluacion) -- la fill-ability real
que instrumentamos el 21-Jul (roadmap Fase 2, ver
project_ballenas_5min_roadmap_avance_21jul) y que antes de esa fecha
tenía 0 filas.

Petición explícita de Javi (21-Jul): "avísame cuando llegue a n≥30 en
cualquiera de los casos" -- no revisarlo a mano cada sesión, que avise
solo cuando cruce. Decisión de avanzar a /code-review + DRY_RUN=False
sigue siendo de Javi, este vigía solo informa que ya hay dato suficiente
para repetir el análisis.

Read-only sobre libro_snapshots.csv, no toca dinero ni config.
"""
import csv
import json
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

LIBRO = REPO / "data/live/libro_snapshots.csv"
LATCH = REPO / "data/live/vigia_ballenas_5min_fillability_latch.json"

STRATEGY = "BALLENAS_TARDIAS"
ACTIVOS = ("ETH", "SOL", "XRP")
UMBRAL_N = 30


def _cargar_latch():
    try:
        return json.loads(LATCH.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _guardar_latch(estado):
    LATCH.write_text(json.dumps(estado, indent=2, ensure_ascii=False), encoding="utf-8")


def _contar():
    c = Counter()
    ratios = {a: [] for a in ACTIVOS}
    try:
        with open(LIBRO, encoding="utf-8") as f:
            for r in csv.DictReader(f):
                if r.get("strategy") != STRATEGY:
                    continue
                sub = r.get("subtype") or ""
                if "#" not in sub:
                    continue
                activo, marco = sub.split("#", 1)
                if activo not in ACTIVOS or marco != "5min":
                    continue
                c[activo] += 1
                try:
                    ratios[activo].append(float(r.get("ratio_vs_stake") or 0))
                except (TypeError, ValueError):
                    pass
    except FileNotFoundError:
        pass
    return c, ratios


def main() -> int:
    latch = _cargar_latch()
    c, ratios = _contar()

    avisos = []
    for activo in ACTIVOS:
        n = c.get(activo, 0)
        clave = f"{STRATEGY}#{activo}#5min#BUY_YES"
        if n < UMBRAL_N:
            continue
        if latch.get(clave, {}).get("avisado"):
            continue
        rs = ratios[activo]
        r5 = sum(1 for x in rs if x >= 5)
        pct = (r5 / len(rs) * 100) if rs else 0.0
        avisos.append((activo, n, pct))
        latch[clave] = {"avisado": True, "n": n, "pct_fillable": round(pct, 1),
                         "avisado_en": datetime.now(timezone.utc).isoformat(timespec="seconds")}

    if avisos:
        lineas = [f"🐋 Fill-ability BALLENAS_TARDIAS#5min cruzó n>={UMBRAL_N}:"]
        for activo, n, pct in avisos:
            lineas.append(f"  {activo}: n={n}  ratio_vs_stake>=5x: {pct:.1f}%")
        lineas.append("Repetir análisis de gate log-growth + fill-ability antes de /code-review.")
        msg = "\n".join(lineas)
        try:
            from shadow_digest import enviar_telegram
            ok = enviar_telegram(msg)
            print(f"[vigia_ballenas_5min_fillability] {len(avisos)} aviso(s) enviado(s) (telegram={ok})")
        except Exception as e:
            print(f"[vigia_ballenas_5min_fillability] error enviando telegram: {e}")
        _guardar_latch(latch)
    else:
        estado = " | ".join(f"{a}={c.get(a,0)}" for a in ACTIVOS)
        print(f"[vigia_ballenas_5min_fillability] sin cruces nuevos (n actual: {estado})")

    return 0


if __name__ == "__main__":
    sys.exit(main())
