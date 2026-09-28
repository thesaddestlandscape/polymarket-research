#!/usr/bin/env python3
"""vigia_director_200k.py -- cron diario de director_200k.py (28-Sep,
petición explícita Javi). A diferencia de vigia_buscador_edge_perdido.py
(que solo avisa hallazgos NUEVOS), este envía SIEMPRE un resumen corto --
mismo criterio que vigia_dispersed_bot_progreso_diario.py: es un informe
de estado del portfolio (Parte B, "dirigir y masterizar"), no una alerta
puntual, así que un día sin cambios sigue siendo información útil (saber
que las candidatas top siguen ahí, no que el vigía está callado).
"""
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
OUT = REPO / "data" / "shadow" / "director_200k.json"
TOP_TELEGRAM = 5


def _texto(d: dict) -> str:
    lin = ["🧭 Director 200k -- Parte B (dirigir y masterizar), resumen diario"]
    lin.append(f"{d.get('n_tuplas_live_hoy', '?')} tuplas live hoy")

    pf = d.get("pnl_fiel_sin_conectar_top", [])
    lin.append(f"\n💰 Edge propio sin conectar ({len(pf)} candidatas, n≥15, top {TOP_TELEGRAM}):")
    if not pf:
        lin.append("  (ninguna)")
    for x in pf[:TOP_TELEGRAM]:
        flag = " ⚠️sospechosa" if x.get("sospechosa_integridad") else ""
        lin.append(f"  {x['tupla']}: +{x['pnl_fiel_eur_sin_suelo']}€ (n={x['n_ejecutado']}, "
                   f"fill={x['fill_rate']}){flag}")

    pi = d.get("payout_inverso_sin_decidir", [])
    lin.append(f"\n⚠️ Payout inverso live sin decidir: {len(pi)}")
    for x in pi[:TOP_TELEGRAM]:
        lin.append(f"  {x['tupla']}: g={x['growth_g_f10pct']} n={x['n']}")

    be = d.get("buscador_edge_perdido_forward_ok", [])
    lin.append(f"\n🔎 Edge perdido con hallazgo forward-validado: {len(be)}")
    for x in be[:TOP_TELEGRAM]:
        lin.append(f"  {x['tupla']} | {x['accion']}")

    lin.append("\nNinguna fila es promoción automática -- checklist 6 categorías + /code-review + OK Javi siempre.")
    return "\n".join(lin)


def main() -> int:
    r = subprocess.run([sys.executable, str(REPO / "director_200k.py")],
                       capture_output=True, text=True, timeout=600, cwd=str(REPO))
    if r.returncode != 0:
        print(f"ERROR ejecutando director_200k.py (rc={r.returncode}): "
              f"{r.stdout[-300:]} {r.stderr[-1200:]}")
        return 1
    print(r.stdout[-2000:])
    try:
        datos = json.loads(OUT.read_text(encoding="utf-8"))
        from shadow_digest import enviar_telegram
        ok = enviar_telegram(_texto(datos), bot="cripto")
        print(f"telegram: {'ok' if ok else 'fallo'}")
    except Exception as e:
        print(f"aviso: no se pudo procesar/enviar Telegram: {type(e).__name__}: {e}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
