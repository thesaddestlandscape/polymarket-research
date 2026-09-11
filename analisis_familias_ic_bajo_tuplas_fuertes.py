#!/usr/bin/env python3
"""
analisis_familias_ic_bajo_tuplas_fuertes.py — detecta familias cuyo
ic_bayes agregado (strategy_params.json) está cerca de cero (|ic|<=0.06)
pero que esconden tuplas individuales (strategy#subtype#decision) con
pnl_fiel fuerte (pnl_fiel_eur_sin_suelo>15) -- el agregado por familia
diluye el edge real de una moneda/marco concreto (mismo patrón CLAUDE.md
pt.17, "JAMÁS agregado").

Origen (02-Sep, propuesta B9 del barrido de sesión "edge sin capturar"):
encontrado a mano primero en STREAK_MOM_5M (IC agregado +0.019 pero 3
tuplas por moneda con pnl_fiel positivo fuerte, +116,70€ combinado) --
este script generaliza la búsqueda a TODAS las familias en un solo
barrido, en vez de repetir el hallazgo a mano cada vez.

Puramente informativo -- no toca ninguna decisión, solo expone el
ranking para revisión manual cada sesión (mismo espíritu que
gate_bucket_propio.py pero a nivel de familia completa, no de bucket de
precio).

Se fusiona en vigias_frecuentes_fase0.py (screen "vigiasfreq").
"""
import json
from pathlib import Path

REPO = Path(__file__).resolve().parent
UMBRAL_IC_FAMILIA = 0.06
UMBRAL_PNL_TUPLA_FUERTE = 15.0
OUT = REPO / "data" / "shadow" / "familias_ic_bajo_tuplas_fuertes.json"


def calcular() -> dict:
    pnl_fiel = json.loads((REPO / "data" / "shadow" / "pnl_fiel_por_estrategia.json").read_text())
    items = pnl_fiel if isinstance(pnl_fiel, list) else pnl_fiel.get("estrategias", pnl_fiel)
    if isinstance(items, dict):
        items = [dict(v, k=k) for k, v in items.items()]

    params = json.loads((REPO / "data" / "shadow" / "strategy_params.json").read_text())
    est = params.get("estrategias", params)

    por_familia: dict[str, list] = {}
    for x in items:
        fam = x.get("strategy")
        por_familia.setdefault(fam, []).append(x)

    resultado = {}
    for fam, tuplas in por_familia.items():
        ic_fam = est.get(fam, {}).get("ic_bayes")
        if ic_fam is None or abs(ic_fam) > UMBRAL_IC_FAMILIA:
            continue
        fuertes = [
            t for t in tuplas
            if t.get("pnl_fiel_eur_sin_suelo", t.get("pnl_fiel_eur", 0)) > UMBRAL_PNL_TUPLA_FUERTE
        ]
        if not fuertes:
            continue
        resultado[fam] = {
            "ic_bayes_familia": ic_fam,
            "n_tuplas_fuertes": len(fuertes),
            "pnl_fiel_combinado_eur": round(
                sum(t.get("pnl_fiel_eur_sin_suelo", t.get("pnl_fiel_eur", 0)) for t in fuertes), 2
            ),
            "tuplas": sorted(
                [
                    {
                        "k": t.get("k") or f"{t.get('strategy')}#{t.get('subtype')}#{t.get('decision')}",
                        "pnl_fiel_eur_sin_suelo": t.get("pnl_fiel_eur_sin_suelo", t.get("pnl_fiel_eur", 0)),
                        "n_ejecutado": t.get("n_ejecutado"),
                    }
                    for t in fuertes
                ],
                key=lambda r: -r["pnl_fiel_eur_sin_suelo"],
            ),
        }
    return dict(sorted(resultado.items(), key=lambda kv: -kv[1]["pnl_fiel_combinado_eur"]))


def main() -> None:
    resultado = calcular()
    OUT.write_text(json.dumps(resultado, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"[analisis_familias_ic_bajo_tuplas_fuertes] {len(resultado)} familias -> {OUT}")


if __name__ == "__main__":
    main()
