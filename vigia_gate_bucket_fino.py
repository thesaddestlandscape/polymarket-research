#!/usr/bin/env python3
"""vigia_gate_bucket_fino.py — Vigía diario de la ventana deslizante de
precio (analisis_gate_bucket_fino.py / data/shadow/gate_bucket_fino.json).
Mismo patrón exacto que vigia_gate_bucket_propio.py, adaptado a que aquí
cada tupla tiene UNA sola ventana ganadora (no una tabla de buckets fijos)
-- diff más simple: tupla presente/ausente/cambio de veredicto o de rango.

Origen (20-Ago, petición explícita Javi: "esto lo vamos a tener que
conectar a todo el sistema... solo así sabremos cuáles son los micro-
buckets que dan dinero de forma exacta"). Ver docstring de
analisis_gate_bucket_fino.py para el hallazgo que lo motivó (grid fijo de
0.05 diluyendo un edge real más estrecho en BALLENAS_TARDIAS#ETH#5min,
tupla LIVE).

Activación: gate_bucket_propio.py::evaluar() ya lee gate_bucket_fino.json
como fuente adicional de promoción a bueno_confirmado (mismo cache por
mtime) -- este vigía no toca prob_yes/stake/pares_permitidos_live, es
puramente informativo. Un veredicto nuevo empieza a aplicar automáticamente
en cuanto este script actualiza el JSON, igual que vigia_gate_bucket_
propio.py -- el aviso de Telegram es para que Javi lo sepa, no una puerta
de aprobación adicional.
"""
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

DATA_PATH = REPO / "data/shadow/gate_bucket_fino.json"
LATCH = REPO / "data/live/vigia_gate_bucket_fino_latch.json"


def main() -> int:
    from shadow_digest import enviar_telegram

    r = subprocess.run([sys.executable, str(REPO / "analisis_gate_bucket_fino.py")],
                        capture_output=True, text=True, timeout=180, cwd=str(REPO))
    if r.returncode != 0:
        print(f"ERROR ejecutando analisis_gate_bucket_fino.py: {r.stderr[-2000:]}")
        return 1

    nuevo = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    try:
        previo = json.loads(LATCH.read_text(encoding="utf-8")) if LATCH.exists() else {}
    except Exception:
        previo = {}

    avisos = []
    for tupla_str, info in nuevo.items():
        v_nuevo = info.get("veredicto", "sin_concluir")
        antes = previo.get(tupla_str, {})
        v_antes = antes.get("veredicto", "sin_concluir")
        rango_antes = (antes.get("lo"), antes.get("hi"))
        rango_nuevo = (info.get("lo"), info.get("hi"))
        if v_nuevo != v_antes or rango_nuevo != rango_antes:
            # /code-review 01-Sep: tras el fix de preservación de historial,
            # una tupla puede pasar a "sin_concluir" vía un placeholder que
            # SOLO tiene veredicto+historial_crudo (sin lo/hi/n/pnl_medio,
            # p.ej. porque salió de pares_permitidos_live/candidatos_
            # evaluacion_live o cayó por debajo de N_MIN hoy) -- usar
            # valores por defecto en vez de indexar directo evita el
            # KeyError que tumbaba este cron.
            lo, hi = info.get("lo"), info.get("hi")
            rango_txt = f"[{lo:.2f},{hi:.2f})" if lo is not None and hi is not None else "(sin ventana hoy)"
            n_txt = info.get("n", "?")
            pnl_txt = f"{info['pnl_medio']:+.3f}" if info.get("pnl_medio") is not None else "?"
            avisos.append(
                f"{'🔴' if v_nuevo == 'malo_confirmado' else '🟢'} {tupla_str} "
                f"{rango_txt} -> {v_nuevo} "
                f"(n={n_txt} pnl/tr={pnl_txt} p={info.get('p_valor')})"
            )

    print(f"{len(nuevo)} tupla(s) con ventana confirmada hoy, {len(avisos)} cambio(s) nuevo(s)")

    if avisos:
        msg = "🪟 Gate bucket FINO (ventana deslizante) — cambios hoy:\n" + "\n".join(avisos)
        print(msg)
        enviar_telegram(msg)
    else:
        print("Sin cambios nuevos hoy.")

    LATCH.write_text(json.dumps(nuevo, ensure_ascii=False, indent=1), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
