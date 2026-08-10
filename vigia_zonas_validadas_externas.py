#!/usr/bin/env python3
"""vigia_zonas_validadas_externas.py — vigía diario de las zonas de precio
validadas externamente vía ballenas_timing_history.csv post-TWAP (10-Ago),
mismo patrón que vigia_gate_bucket_propio.py.

Re-corre analisis_zonas_validadas_externas_post_twap_10ago.py cada día
(ballenas_timing_history.csv crece solo) y avisa por Telegram solo cuando
una zona ENTRA o SALE del conjunto confirmado -- para que Javi vea si el
margen se sostiene o se erosiona con más n, sin repetir el mismo aviso
cada día.
"""
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

DATA_PATH = REPO / "data/shadow/zonas_validadas_externas.json"
LATCH = REPO / "data/live/vigia_zonas_validadas_externas_latch.json"


def main() -> int:
    from shadow_digest import enviar_telegram

    r = subprocess.run([sys.executable, str(REPO / "analisis_zonas_validadas_externas_post_twap_10ago.py")],
                        capture_output=True, text=True, timeout=120, cwd=str(REPO))
    if r.returncode != 0:
        print(f"ERROR ejecutando analisis_zonas_validadas_externas_post_twap_10ago.py: {r.stderr[-2000:]}")
        return 1

    nuevo = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    try:
        previo = json.loads(LATCH.read_text(encoding="utf-8")) if LATCH.exists() else {}
    except Exception:
        previo = {}

    avisos = []
    for tupla_str, info in nuevo.items():
        zonas_nuevas = {tuple(z) for z in info.get("zonas_bueno_confirmado", [])}
        zonas_antes = {tuple(z) for z in previo.get(tupla_str, {}).get("zonas_bueno_confirmado", [])}
        entraron = zonas_nuevas - zonas_antes
        salieron = zonas_antes - zonas_nuevas
        for lo, hi in sorted(entraron):
            det = info["detalle_por_bucket"].get(f"{lo:.2f}", {})
            avisos.append(f"🟢 {tupla_str} [{lo:.2f},{hi:.2f}) ENTRA confirmada "
                          f"(n={det.get('n')} margen={det.get('margen_pp'):+.1f}pp)")
        for lo, hi in sorted(salieron):
            avisos.append(f"🔴 {tupla_str} [{lo:.2f},{hi:.2f}) SALE de confirmada (revisar por qué)")

    if avisos:
        msg = "🐋 Zonas validadas externas (post-TWAP) — cambios hoy:\n" + "\n".join(avisos)
        print(msg)
        enviar_telegram(msg)
    else:
        print("Sin cambios hoy en las zonas confirmadas.")

    LATCH.write_text(json.dumps(nuevo, ensure_ascii=False, indent=1), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
