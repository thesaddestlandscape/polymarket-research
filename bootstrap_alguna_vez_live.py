#!/usr/bin/env python3
"""Bootstrap ÚNICO (se corre a mano una vez, no es un cron) para el fix
estructural del "cementerio" (project_candidatas_estancadas_diagnostico_05ago,
Parte 3): calcula el conjunto histórico completo de nombres base de
estrategia que ALGUNA VEZ han estado en pares_permitidos_live, escaneando
TODO el historial de git de config_live.json (154 commits a 06-Ago, existe
desde 03-Jul) -- no solo el estado actual.

Se persiste en data/live/estrategias_alguna_vez_live.json y, a partir de
ahí, shadow_predict.py lo mantiene actualizado él solo cada ciclo (añade
cualquier nombre nuevo que aparezca en pares_permitidos_live, nunca
necesita re-escanear git) -- ver ACUMULAR_SHADOW_AUNQUE_DESACTIVADA en
shadow_predict.py para el uso real.

Granularidad: nombre BASE de estrategia (antes del primer '#'), la misma
que ya usa ACUMULAR_SHADOW_AUNQUE_DESACTIVADA -- si CUALQUIER subtype de
una estrategia estuvo live alguna vez, la familia entera queda excluida de
la exención automática (mismo criterio que el mecanismo que sustituye, sin
introducir una granularidad nueva).
"""
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
CONFIG_LIVE = REPO / "data/live/config_live.json"
SALIDA = REPO / "data/live/estrategias_alguna_vez_live.json"


def _commits_que_tocan(path):
    out = subprocess.check_output(
        ["git", "log", "--format=%H", "--", str(path)], cwd=REPO
    )
    return out.decode().split()


def main() -> int:
    commits = _commits_que_tocan(CONFIG_LIVE)
    print(f"[bootstrap] {len(commits)} commits tocan config_live.json")

    nombres = set()
    tuplas_vistas = set()
    errores = 0
    for i, c in enumerate(commits):
        try:
            raw = subprocess.check_output(
                ["git", "show", f"{c}:data/live/config_live.json"],
                cwd=REPO, stderr=subprocess.DEVNULL,
            )
            d = json.loads(raw)
        except Exception:
            errores += 1
            continue
        for t in d.get("pares_permitidos_live", []):
            if not isinstance(t, str):
                continue
            tuplas_vistas.add(t)
            nombres.add(t.split("#")[0])
        # Los ~18 commits más antiguos (desde 671d7f1, 03-Jul) usaban un
        # esquema previo a pares_permitidos_live -- "estrategias_permitidas_live"
        # (lista de nombres base, ej. ["UPDOWN_GBM"]) + "subtypes_permitidos_live"
        # (subtypes sin dirección). Sin esto, esos commits no aportaban nada al
        # histórico -- hoy resulta inofensivo porque los 2 nombres que aparecen
        # ahí (UPDOWN_GBM, GBM_LATE_15M) reaparecen más tarde bajo el esquema
        # nuevo, pero es incidental, no por diseño (hallazgo /code-review 06-Ago).
        for n in d.get("estrategias_permitidas_live", []):
            if isinstance(n, str):
                nombres.add(n)
        if (i + 1) % 30 == 0:
            print(f"[bootstrap] procesados {i+1}/{len(commits)}...")

    print(f"[bootstrap] {errores} commits sin JSON parseable (ignorados)")
    print(f"[bootstrap] {len(tuplas_vistas)} tuplas distintas vistas en pares_permitidos_live histórico")
    print(f"[bootstrap] {len(nombres)} nombres base de estrategia alguna vez live:")
    for n in sorted(nombres):
        print(f"   {n}")

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    SALIDA.write_text(json.dumps(sorted(nombres), indent=2, ensure_ascii=False))
    print(f"[bootstrap] escrito {SALIDA}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
