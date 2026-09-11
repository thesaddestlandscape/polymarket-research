#!/usr/bin/env python3
"""vigia_fade_regimen_arquetipoA.py — vigía diario de
analisis_fade_regimen_arquetipoA.py (26-Ago, petición explícita Javi:
"solucionar todo lo que tiene arquetipo A o está en el cementerio",
generalización del hallazgo puntual MOMENTUM_IBS_15M#BNB#15min#BUY_NO).

Re-corre el análisis con datos frescos (fade_depth_universal_fase0.csv +
libro_snapshots.csv + results.csv crecen cada día) y avisa por Telegram
SOLO tuplas cuyo veredicto_final cambia a "fade_confirmado*" (nuevo, o
que no lo era ayer) -- mismo patrón latch que vigia_gate_bucket_propio.py.

⚠️ Caveat importante que debe ir SIEMPRE en el aviso: este mecanismo
screenea ~270+ tuplas independientes cada corrida (multiple-testing real,
no solo un puñado de filtros sobre una tupla) -- un "fade_confirmado" es
un candidato fuerte para seguir vigilando con datos NUEVOS que lleguen
después de la primera detección, NO una confirmación lista para tocar
dinero real. La re-ejecución diaria con n creciente ES la validación
forward (mismo criterio que gate_bucket_propio.py) -- un veredicto que
se mantiene varios días seguidos con n creciente es mucho más fiable que
la primera detección. NO conecta a prob_yes/stake/pares_permitidos_live
-- puramente informativo, igual que gate_bucket_propio.py hasta que
alguien decida construir un ejecutor.
"""
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

DATA_PATH = REPO / "data/shadow/fade_regimen_arquetipoA.json"
LATCH = REPO / "data/live/vigia_fade_regimen_arquetipoA_latch.json"


def main() -> int:
    from shadow_digest import enviar_telegram

    r = subprocess.run(
        [sys.executable, str(REPO / "analisis_fade_regimen_arquetipoA.py")],
        capture_output=True, text=True, timeout=300, cwd=str(REPO),
    )
    if r.returncode != 0:
        print(f"ERROR ejecutando analisis_fade_regimen_arquetipoA.py: {r.stderr[-2000:]}")
        return 1
    print(r.stdout[-2000:])

    nuevo = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    try:
        previo = json.loads(LATCH.read_text(encoding="utf-8")) if LATCH.exists() else {}
    except Exception:
        previo = {}

    avisos = []
    n_negativas = 0
    n_confirmadas = 0
    for tupla_str, entrada in nuevo.items():
        if entrada.get("original", {}).get("veredicto") == "negativo_candidata_fade":
            n_negativas += 1
        vf_nuevo = entrada.get("veredicto_final", "")
        vf_antes = previo.get(tupla_str, {}).get("veredicto_final", "")
        if vf_nuevo.startswith("fade_confirmado"):
            n_confirmadas += 1
            if vf_nuevo != vf_antes:
                if vf_nuevo == "fade_confirmado_sin_filtro":
                    stats = entrada.get("fade_sin_filtro", {})
                else:
                    filtro = vf_nuevo.split(":", 1)[1]
                    stats = entrada.get("filtros_regimen", {}).get(filtro, {})
                avisos.append(
                    f"🟢 {tupla_str} -> {vf_nuevo} "
                    f"(n={stats.get('n')} pnl/tr={stats.get('pnl_medio'):+.3f} "
                    f"p={stats.get('p_binomial')})"
                )

    print(f"Candidatas negativas evaluadas: {n_negativas} | fade_confirmado (con o sin filtro): {n_confirmadas}")

    if avisos:
        msg = (
            "🪞 Fade régimen arquetipo A — nuevos veredictos hoy:\n"
            + "\n".join(avisos)
            + "\n\n⚠️ Screening de ~270 tuplas independientes -- candidato "
              "fuerte para seguir vigilando con n creciente, NO confirmación "
              "lista para dinero real (mismo criterio que gate_bucket_propio)."
        )
        print(msg)
        enviar_telegram(msg)
    else:
        print("Sin veredictos fade_confirmado nuevos hoy.")

    LATCH.write_text(json.dumps(nuevo, ensure_ascii=False, indent=1), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
