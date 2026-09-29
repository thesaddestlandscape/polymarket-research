#!/usr/bin/env python3
"""vigia_gbm_late_imbalance_diario.py -- Informe DIARIO (petición Javi,
29-Sep) de gbm_late_imbalance_fase0.py (ronda2 #9): ¿el desequilibrio del
libro al detectar una señal REAL GBM_LATE predice el resultado (EV al ask
real)? SIEMPRE envía mensaje. Solo observación. Cron 08:35 UTC.
"""
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

IN = REPO / "data" / "shadow" / "gbm_late_imbalance_fase0.csv"


def _enviar(msg: str) -> None:
    print(msg)
    try:
        from shadow_digest import enviar_telegram
        enviar_telegram(msg, bot="cripto")
    except Exception as e:
        print(f"[vigia_gbm_late_imbalance_diario] error Telegram: {e}")


def main() -> None:
    if not IN.exists():
        _enviar("📚 *GBM LATE imbalance (ronda2 #9)*: todavía sin datos.")
        return
    from analisis_gbm_late_imbalance import evaluar
    r = evaluar(40, out_print=lambda *_: None)
    partes = [f"📚 *GBM LATE imbalance del libro (ronda2 #9)* — informe diario",
              f"{r['filas']} señales capturadas en {r['dias']} días; {r['unidades']} resueltas y fillables "
              f"(ask 0,10-0,90, ratio >=5x)."]
    top5 = [t for t in r["terciles"] if "imbalance top5" in t[0] or "imbalance_top5" in t[0]]
    if top5:
        partes.append("EV por euro al ask real, tercil de imbalance top5 (IC90 por días):")
        for nombre, n, ev, lo, hi, nd in top5:
            etiqueta = nombre.split()[-1]
            partes.append(f"· {etiqueta}: n={n} EV {ev:+.3f} IC [{lo:+.3f}, {hi:+.3f}] días={nd}")
    else:
        partes.append("Todavía sin n suficiente para terciles (necesita >=45 unidades resueltas).")
    if r["celdas_decisivas"]:
        partes.append("🎯 *Celdas moneda×marco×tercil decisivas (n>=40, >=10 días, IC no cruza cero):*")
        for nombre, n, ev, lo, hi, nd in r["celdas_decisivas"][:8]:
            partes.append(f"· {nombre}: n={n} EV {ev:+.3f} [{lo:+.3f}, {hi:+.3f}] días={nd}")
        partes.append("→ candidata a filtro/timing; requiere checklist + code-review + OK Javi.")
    else:
        falta = max(0, 10 - r["dias"])
        partes.append(f"Ninguna celda decisiva aún (regla: n>=40 y >=10 días; faltan ~{falta} días de captura). "
                      f"Sin edge hasta que alguna celda cruce.")
    _enviar("\n".join(partes))


if __name__ == "__main__":
    main()
