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
from concurrent.futures import ProcessPoolExecutor, TimeoutError as FutureTimeoutError
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

HIST = REPO / "data" / "shadow" / "robustez_diaria_historico.csv"
N_RANDOM_OOS_DIARIO = 30

# 07-Sep (barrido de salud, petición explícita Javi tras encontrar este
# vigía sin NINGÚN timeout -- a diferencia de correr_parameter_stability(),
# que ya usa subprocess.run(timeout=480), las otras 3 llamadas eran
# funciones en proceso SIN protección alguna. Medido en vivo hoy:
# correr_noise_test() tarda >280s (lee results.csv completo, 356MB+,
# mismo patrón de crecimiento que ya rompió otros 3 vigías esta misma
# sesión) -- sin timeout, un cron diario a las 22:15 UTC podía quedarse
# corriendo horas sin que nadie lo notara. correr_montecarlo() (52s) y
# correr_randomized_oos() (26s) están sanos hoy, pero se protegen igual
# por si crecen mañana -- "el sistema tiene que vigilar esto", no solo
# reaccionar cuando ya se ha roto.
TIMEOUT_MONTECARLO_S = 300
TIMEOUT_NOISE_TEST_S = 600
TIMEOUT_RANDOMIZED_OOS_S = 300


def _con_timeout(func, timeout_s, nombre):
    """Ejecuta func() en un PROCESO aparte con timeout real (a diferencia
    de un hilo, un ProcessPoolExecutor sí se puede matar de verdad si se
    excede el timeout -- el trabajo pesado aquí es CPU/IO-bound, un hilo
    seguiría corriendo en segundo plano indefinidamente aunque
    abandonáramos la espera)."""
    try:
        with ProcessPoolExecutor(max_workers=1) as ex:
            fut = ex.submit(func)
            return fut.result(timeout=timeout_s)
    except FutureTimeoutError:
        print(f"[vigia_robustez] {nombre} excedió el timeout ({timeout_s}s) -- abortado")
        return None
    except Exception as e:
        print(f"[vigia_robustez] {nombre} falló: {e}")
        return None


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
        # 09-Sep (barrido de salud, hallazgo real): timeout 480s->1200s.
        # Medido en vivo: no terminó ni en 700s (results.csv ya 380MB+,
        # analisis_parameter_stability.py hace ~15-20 pasadas O(n) completas
        # sobre las filas resueltas cargadas en memoria) -- MISMA causa raíz
        # que el resto de lentitud del pipeline hoy (calcular_params() en
        # shadow_postmortem.py, ver project_disco_ram_critico_09sep),
        # deliberadamente NO resuelta de fondo hoy (decisión explícita Javi
        # de aparcar el rediseño grande). Este vigía es solo diario
        # (22:15 UTC), un peor caso de 20min no bloquea nada del pipeline
        # en vivo -- parche operativo, no la solución real.
        out = subprocess.run([sys.executable, str(REPO / "analisis_parameter_stability.py")],
                             capture_output=True, text=True, timeout=1200, cwd=str(REPO))
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

    mc = _con_timeout(correr_montecarlo, TIMEOUT_MONTECARLO_S, "Monte Carlo secuenciación")
    noise = _con_timeout(correr_noise_test, TIMEOUT_NOISE_TEST_S, "Noise Test")
    oos = _con_timeout(correr_randomized_oos, TIMEOUT_RANDOMIZED_OOS_S, "Randomized OOS")
    ps = correr_parameter_stability()  # ya protegido (subprocess.run(timeout=480))

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
