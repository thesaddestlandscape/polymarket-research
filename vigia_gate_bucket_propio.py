#!/usr/bin/env python3
"""vigia_gate_bucket_propio.py — Vigía diario del gate por micro-bucket de
PnL propio (gate_bucket_propio.py / data/shadow/gate_bucket_propio.json).

Petición explícita Javi 28-Jul, imperativa: "tienes que revisar todos los
dias y contarme como van estos datos... es tu responsabilidad". Cron diario
06:55 UTC (mismo patrón que analisis_diario_ballenas_ejecutor.py 06:40 /
wallet_especialistas_observer.py 06:45 / analisis_diario_franja_15min.py
06:50).

Hace 3 cosas:
1. Re-corre analisis_gate_bucket_propio_28jul.py (regenera el JSON con el
   n de hoy -- results.csv crece cada ciclo, así que buckets "sin_concluir"
   pueden cruzar el umbral de rigor (n>=15, shuffle p<0.05, split-half
   consistente) de un día para otro).
2. Diffea contra el estado de AYER (latch) -- avisa por Telegram SOLO
   veredictos NUEVOS (bucket que pasa de sin_concluir a malo_confirmado/
   bueno_confirmado, o que cambia de sentido) para no repetir ruido cada
   día con el mismo hallazgo ya conocido.
3. Reporta cobertura: cuántos buckets siguen sin n suficiente por tupla,
   para saber si merece la pena seguir esperando o si esa tupla nunca va
   a acumular n ahí (ej. BALLENAS_TARDIAS#ETH#5min con n_total=0).

Activación de nuevos vetos: SOLO gate_bucket_propio.py lee el JSON en
shadow_predict.py -- este vigía no toca prob_yes/stake/pares_permitidos_
live, es puramente informativo (igual que vigia_log_growth.py). Un
veredicto nuevo "malo_confirmado" empieza a vetar automáticamente en
cuanto este script actualiza el JSON (mismo cache por mtime que ya usa
gate_bucket_propio.py) -- el aviso de Telegram es para que Javi lo sepa,
no una puerta de aprobación adicional (esa ya se cruzó el 28-Jul: el
mecanismo fue diseñado para auto-extenderse a nuevos buckets que pasen el
MISMO rigor ya aprobado, sin repetir /code-review por cada bucket nuevo
individual -- solo si cambia el propio mecanismo de decisión).
"""
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

DATA_PATH = REPO / "data/shadow/gate_bucket_propio.json"
LATCH = REPO / "data/live/vigia_gate_bucket_propio_latch.json"


def main() -> int:
    from shadow_digest import enviar_telegram

    # 1. Regenerar con datos de hoy
    r = subprocess.run([sys.executable, str(REPO / "analisis_gate_bucket_propio_28jul.py")],
                        capture_output=True, text=True, timeout=120)
    if r.returncode != 0:
        print(f"ERROR ejecutando analisis_gate_bucket_propio_28jul.py: {r.stderr[-2000:]}")
        return 1

    nuevo = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    try:
        previo = json.loads(LATCH.read_text(encoding="utf-8")) if LATCH.exists() else {}
    except Exception:
        previo = {}

    avisos = []
    cobertura = []
    for tupla_str, tabla in nuevo.items():
        veredictos_antes = previo.get(tupla_str, {})
        n_sin_concluir = 0
        n_total_buckets = len(tabla)
        for b, info in tabla.items():
            v_nuevo = info.get("veredicto", "sin_concluir")
            v_antes = veredictos_antes.get(b, {}).get("veredicto", "sin_concluir")
            if v_nuevo != "sin_concluir":
                if v_antes != v_nuevo:
                    avisos.append(
                        f"{'🔴' if v_nuevo == 'malo_confirmado' else '🟢'} {tupla_str} [{b},{float(b)+0.05:.2f}) "
                        f"-> {v_nuevo} (n={info['n']} pnl/tr={info['pnl_medio']:+.3f} p={info.get('shuffle_p')})"
                    )
            else:
                n_sin_concluir += 1
        if n_total_buckets:
            cobertura.append(f"{tupla_str}: {n_total_buckets - n_sin_concluir}/{n_total_buckets} buckets con veredicto")

    print("\n".join(cobertura))

    if avisos:
        msg = "🔬 Gate bucket propio — nuevos veredictos hoy:\n" + "\n".join(avisos)
        print(msg)
        enviar_telegram(msg)
    else:
        print("Sin veredictos nuevos hoy.")

    LATCH.write_text(json.dumps(nuevo, ensure_ascii=False, indent=1), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
