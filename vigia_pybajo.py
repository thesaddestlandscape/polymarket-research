#!/usr/bin/env python3
"""Vigía H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT: avisa por Telegram (una vez) cuando la
hipótesis cruza su gate n≥289. Read-only, no toca dinero ni config.

Reusa el MISMO filtro e IC que hypothesis_tracker (_eval_custom) para no divergir
del tracker (lección feedback_verificar_filtro_tracker). Al cruzar el gate:
  - IC<umbral_ic_max  → CONFIRMADO: proponer filtro live a Javi.
  - IC>=umbral_ic_max → REVERTIDO: candidato a archivar (el live n=27 daba +).
Decisión final SIEMPRE de Javi (afecta estrategia live).
"""
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

HID = "H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT"
LATCH = REPO / "data/live/vigia_pybajo_latch.json"


def main() -> int:
    import hypothesis_tracker as ht
    from shadow_digest import enviar_telegram

    rows = ht._load_results()
    defs = ht._cargar_hipotesis_custom()
    hdef = next((d for d in defs if d.get("id") == HID), None)
    if hdef is None:
        print(f"[vigia_pybajo] hipótesis {HID} no encontrada en hipotesis_custom.json")
        return 0

    # OJO: hdef["filtro"] usa strategy_prefix "GBM_LATE_15M", que en _aplicar_filtro
    # hace match de PREFIJO y agrupa las variantes shadow-only (_TARDIO, _ESPACIO_ATR,
    # _MULTIHORIZONTE). El gate del autor ("249 baseline + 40 forward") y el filtro que
    # se aplicaría en live son sobre la estrategia EXACTA. Reusamos filtro+IC del tracker
    # pero restringimos a strategy == 'GBM_LATE_15M' para no confirmar de forma prematura.
    filtro = hdef.get("filtro", {})
    subset = [r for r in rows
              if ht._aplicar_filtro(r, filtro) and r.get("strategy") == "GBM_LATE_15M"]
    res = ht._stats(subset)
    n = res.get("n", 0)
    ic = res.get("ic", 0.0)
    pnl = res.get("pnl", 0.0)
    gate_n = hdef.get("umbral_n", 289)
    ic_max = hdef.get("umbral_ic_max", -0.1)
    print(f"[vigia_pybajo] n={n}/{gate_n} ic={ic:+.3f} pnl={pnl:+.2f} status={res.get('status')}")

    if n < gate_n:
        return 0  # aún acumulando

    # Gate cruzado: latch para no repetir el aviso
    if LATCH.exists():
        try:
            prev = json.loads(LATCH.read_text())
            if prev.get("avisado_n_gate"):
                return 0
        except Exception:
            pass

    if ic < ic_max:
        veredicto = (f"🔴 CONFIRMADO (IC={ic:+.3f} < {ic_max}): comprar YES barato que el "
                     f"modelo no cree PIERDE de forma consistente. Propuesta: filtro causal "
                     f"decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M. "
                     f"AFECTA ESTRATEGIA LIVE — tu decisión.")
    else:
        veredicto = (f"🟡 REVERTIDO (IC={ic:+.3f} ≥ {ic_max}): el signo negativo shadow NO "
                     f"aguanta con n≥{gate_n} (coherente con el live n=27 positivo). "
                     f"Candidata a ARCHIVAR — era ruido de la muestra retrospectiva.")

    msg = (f"🔔 VIGÍA pybajo-longshot cruzó gate n≥{gate_n}\n"
           f"n={n} IC={ic:+.3f} PnL_shadow={pnl:+.2f}€\n{veredicto}")
    ok = enviar_telegram(msg)

    LATCH.write_text(json.dumps({
        "avisado_n_gate": True, "n": n, "ic": ic, "pnl": pnl,
        "telegram_ok": ok, "id": HID,
    }, ensure_ascii=False, indent=1))
    print(f"[vigia_pybajo] aviso enviado (telegram={ok}), latch escrito")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        # Fail-loud en log, pero nunca romper el cron
        print(f"[vigia_pybajo] ERROR {type(e).__name__}: {e}")
        sys.exit(0)
