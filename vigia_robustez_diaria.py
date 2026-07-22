#!/usr/bin/env python3
"""vigia_robustez_diaria.py — corre diariamente los 4 tests de robustez
del checklist quant compartido por Javi 21-Jul (Parameter Stability,
Monte Carlo secuenciación, Noise Test, Randomized OOS) y avisa por
Telegram con las cifras clave. Petición explícita de Javi (22-Jul):
"estos robustos hay que utilizarlos diariamente y sacar resultados".

Mismo patrón que vigia_supervivencia_diaria.py (21-Jul): reusa las
funciones ya construidas en cada analisis_*.py (ejecutar()/ejecutar_live(),
no reimplementa nada), persiste una serie temporal en
data/shadow/robustez_diaria_historico.csv y avisa por Telegram, sin latch
(digest diario, se espera un mensaje por día).

Randomized OOS y Noise Test corren con menos simulaciones que el CLI
manual (n_random=30 en vez de 60, mismo n_shuffles/N_DRAWS en Noise Test
que ya es barato) para que el cron sea rápido y no compita con el fast
loop; el detalle fino (n mayor) se sigue corriendo a mano cuando hace
falta profundizar en un hallazgo concreto.

Solo lectura -- no toca ningún parámetro, config ni gate real.
Cron: 1 vez al día (ver crontab).
"""
import csv
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

HIST = REPO / "data" / "shadow" / "robustez_diaria_historico.csv"
N_RANDOM_OOS_DIARIO = 30


def correr_montecarlo():
    from analisis_montecarlo_secuenciacion import ejecutar
    try:
        return ejecutar()
    except Exception as e:
        print(f"[vigia_robustez] Monte Carlo secuenciación falló: {e}")
        return None


def correr_noise_test():
    from analisis_noise_test import ejecutar
    try:
        resultados, n_evaluados, n_sin_datos = ejecutar()
        con_ret = [r for r in resultados if r["retencion"] is not None]
        fragiles = [r for r in con_ret if r["retencion"] < 0.5]
        peor = min(con_ret, key=lambda r: r["retencion"]) if con_ret else None
        return {
            "n_evaluados": n_evaluados, "n_sin_datos": n_sin_datos,
            "n_con_retencion": len(con_ret), "n_fragiles": len(fragiles),
            "peor_key": peor["key"] if peor else None,
            "peor_feature": peor["feature"] if peor else None,
            "peor_retencion": peor["retencion"] if peor else None,
        }
    except Exception as e:
        print(f"[vigia_robustez] Noise Test falló: {e}")
        return None


def correr_randomized_oos():
    from analisis_randomized_oos import ejecutar_live
    try:
        resultados = ejecutar_live(n_random=N_RANDOM_OOS_DIARIO)
        extremas = [r for r in resultados
                    if r["percentil_ic_reciente"] is not None
                    and (r["percentil_ic_reciente"] >= 90 or r["percentil_ic_reciente"] <= 10)]
        return {
            "n_tuplas": len(resultados),
            "n_extremas": len(extremas),
            "tuplas_extremas": [(r["tupla"], r["percentil_ic_reciente"]) for r in extremas],
        }
    except Exception as e:
        print(f"[vigia_robustez] Randomized OOS falló: {e}")
        return None


def correr_parameter_stability():
    """Vía subprocess (no expone función reutilizable, es print-heavy por
    diseño -- ver analisis_parameter_stability.py) — cuenta veredictos
    ⚠️/✅ en el texto para un headline simple, el log completo queda en
    logs/vigia_robustez.log (redirección del cron)."""
    try:
        out = subprocess.run([sys.executable, str(REPO / "analisis_parameter_stability.py")],
                             capture_output=True, text=True, timeout=480, cwd=str(REPO))
        texto = out.stdout
        n_fragil = texto.count("posible pico frágil")
        n_estable = texto.count("meseta, no pico")
        return {"n_estable": n_estable, "n_fragil": n_fragil}
    except Exception as e:
        print(f"[vigia_robustez] Parameter Stability falló: {e}")
        return None


def main():
    hoy = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    print(f"[vigia_robustez] {hoy} — corriendo los 4 tests de robustez")

    mc = correr_montecarlo()
    noise = correr_noise_test()
    oos = correr_randomized_oos()
    ps = correr_parameter_stability()

    for nombre, r in (("Monte Carlo secuenciación", mc), ("Noise Test", noise),
                      ("Randomized OOS", oos), ("Parameter Stability", ps)):
        print(f"[vigia_robustez] {nombre}: {r}")

    nuevo = not HIST.exists()
    with open(HIST, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if nuevo:
            w.writerow(["fecha", "mc_pct_bust", "mc_percentil_real", "mc_bankroll_final",
                        "noise_n_evaluados", "noise_n_fragiles", "noise_peor_key",
                        "oos_n_tuplas", "oos_n_extremas", "ps_n_estable", "ps_n_fragil"])
        w.writerow([
            hoy,
            mc["pct_bust"] if mc else "", mc["percentil_real"] if mc else "",
            mc["baseline"]["bankroll_final"] if mc else "",
            noise["n_evaluados"] if noise else "", noise["n_fragiles"] if noise else "",
            noise["peor_key"] if noise else "",
            oos["n_tuplas"] if oos else "", oos["n_extremas"] if oos else "",
            ps["n_estable"] if ps else "", ps["n_fragil"] if ps else "",
        ])

    lineas = [f"🔬 Robustez diaria ({hoy})"]
    if mc:
        lineas.append(f"MC secuenciación: P(bust)={mc['pct_bust']:.1f}% · orden real percentil {mc['percentil_real']:.0f}%")
    if noise:
        peor = f" (peor: {noise['peor_key']}/{noise['peor_feature']} {noise['peor_retencion']}x)" if noise["n_fragiles"] else ""
        lineas.append(f"Noise Test: {noise['n_fragiles']}/{noise['n_con_retencion']} filtros frágiles{peor}")
    if oos:
        if oos["n_extremas"]:
            detalle = ", ".join(f"{t} ({p:.0f}%)" for t, p in oos["tuplas_extremas"])
            lineas.append(f"Randomized OOS: {oos['n_extremas']}/{oos['n_tuplas']} tuplas en ventana extrema — {detalle}")
        else:
            lineas.append(f"Randomized OOS: {oos['n_tuplas']} tuplas, ninguna en ventana extrema")
    if ps:
        lineas.append(f"Parameter Stability: {ps['n_estable']} meseta / {ps['n_fragil']} posible pico frágil")
    msg = "\n".join(lineas)

    try:
        from shadow_digest import enviar_telegram
        ok = enviar_telegram(msg)
        print(f"[vigia_robustez] telegram={ok}")
    except Exception as e:
        print(f"[vigia_robustez] no se pudo notificar Telegram: {e}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
