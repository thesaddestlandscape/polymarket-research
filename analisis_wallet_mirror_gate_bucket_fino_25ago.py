#!/usr/bin/env python3
"""analisis_wallet_mirror_gate_bucket_fino_25ago.py — ventana deslizante
(mismo mecanismo que analisis_gate_bucket_fino.py, 20-Ago) aplicada a
WALLET_MIRROR. Petición explícita Javi 25-Ago: "revisa los micro-buckets
finos de todo [wallet mirror] porque quiza tengamos algo que podamos
promocionar" -- wallet_mirror_gate_bucket.json (grid fijo 0.05) solo tiene
2 bueno_confirmado, ambos BTC (ya en live); pero hay volumen sin explotar
en otros activos (ETH#15min n=1859, SOL#15min n=1644, XRP#15min n=487,
DOGE#15min n=267 combinando grande+no_grande) que el grid fijo podría
estar diluyendo, mismo patrón que rescató BALLENAS_TARDIAS#ETH#5min el
20-Ago.

Reusa TODO sin duplicar: `cargar_filas()` de
analisis_wallet_mirror_gate_bucket_10ago.py (ya filtra TWAP+fillability
real vía sigue_fillable_en_decision) da grupos (tipo,activo,marco,grande)
-> [(ts,ask,pnl)]; `evaluar_tupla()`/`bh_fdr_signif()` de
analisis_gate_bucket_fino.py (max-statistic + LOO + bootstrap CI90%, sin
reimplementar el rigor). Solo lectura -- no toca ningún gate real ni
pares_permitidos_live.
"""
import json
from pathlib import Path

from analisis_wallet_mirror_gate_bucket_10ago import cargar_filas
from analisis_gate_bucket_fino import evaluar_tupla, bh_fdr_signif, P_MAX
from gate_confirmacion_historial import (
    cargar_historial_previo, veredicto_con_tolerancia, sembrar_no_confirmados,
)

REPO = Path(__file__).resolve().parent
OUT = REPO / "data/shadow/wallet_mirror_gate_bucket_fino.json"

# 01-Sep: umbral propio de WALLET_MIRROR, n>=40 (no el N_MIN_VENTANA=15
# compartido de analisis_gate_bucket_fino.py, que usan otras familias live
# y no se toca aqui para no ampliar el radio del cambio) -- ventanas
# confirmadas con n=30 (ej. SEGUIR#BTC#15min#1[0.35,0.40) n=30) se
# revertian con mas datos tras disparar dinero real, ver nota
# _pares_walletmirror_pausa_nota_2026-09-01 en config_live.json.
N_MIN_WALLET_MIRROR = 40


def main() -> int:
    grupos = cargar_filas()
    print(f"Grupos (tipo,activo,marco,grande): {len(grupos)}")
    historial_previo = cargar_historial_previo(OUT, anidado_por_bucket=False)
    salida_final = {}

    def _preservar_historial(clave_str: str) -> None:
        """/code-review 01-Sep: ver misma función en analisis_gate_bucket_
        fino.py -- sin esto, un bucket que no sobrevive hoy (incluyendo
        cuando evaluar_tupla() devuelve falsy por falta de datos) desaparece
        del fichero entero (json.dump sobreescribe) y pierde su
        historial_crudo aunque no haya pasado ningún día malo."""
        hist = historial_previo.get(clave_str)
        if hist and clave_str not in salida_final:
            salida_final[clave_str] = {"veredicto": "sin_concluir", "historial_crudo": hist}

    pendientes = []
    resultado = {}
    for clave, filas in grupos.items():
        tipo, activo, marco, grande = clave
        clave_str = f"{tipo}#{activo}#{marco}#{grande}"
        info = evaluar_tupla(filas)
        if not info:
            _preservar_historial(clave_str)
            continue
        resultado[clave_str] = info
        if info["split_half_ok"] and info["robusto_loo"] and info["robusto_bootstrap"]:
            pendientes.append({"clave_str": clave_str, "activo": activo, "info": info,
                                "p": info["p_valor"], "diff": info["diff_vs_resto"]})

    por_activo = {}
    for idx, p in enumerate(pendientes):
        por_activo.setdefault(p["activo"], []).append(idx)

    sobreviven = set()
    for activo, indices in por_activo.items():
        p_valores_grupo = [pendientes[i]["p"] for i in indices]
        sobreviven_grupo = bh_fdr_signif(p_valores_grupo, q=P_MAX)
        sobreviven |= {indices[j] for j in sobreviven_grupo}

    print(f"\nVentanas candidatas (n>=40 tupla, robustas LOO+bootstrap): {len(pendientes)} "
          f"| sobreviven BH-FDR por activo: {len(sobreviven)}")

    veredictos = []
    pendientes_confirmacion = []

    for idx, p in enumerate(pendientes):
        if idx not in sobreviven:
            _preservar_historial(p["clave_str"])
            continue
        info = p["info"]
        if p["diff"] < 0:
            veredicto_crudo = "malo_confirmado"
        elif info["pnl_medio"] >= 0 and info["n"] >= N_MIN_WALLET_MIRROR:
            veredicto_crudo = "bueno_confirmado"
        else:
            _preservar_historial(p["clave_str"])
            continue

        info["veredicto_crudo_hoy"] = veredicto_crudo
        # 01-Sep (petición explícita Javi, "un día de mala racha no puede
        # entorpecer esto"): 2 de los últimos 3 días (incluido hoy), no solo
        # el día inmediatamente anterior -- ver gate_confirmacion_historial.py.
        veredicto, info["historial_crudo"] = veredicto_con_tolerancia(
            veredicto_crudo, historial_previo.get(p["clave_str"]))
        if veredicto == "sin_concluir" and veredicto_crudo == "bueno_confirmado":
            pendientes_confirmacion.append(
                f"⏳ {p['clave_str']} [{info['lo']:.2f},{info['hi']:.2f}) n={info['n']} "
                f"pnl_medio={info['pnl_medio']:+.3f} bueno_confirmado HOY, esperando confirmación de mañana"
            )

        info["veredicto"] = veredicto
        salida_final[p["clave_str"]] = info
        if veredicto == "sin_concluir":
            continue
        marca = "🔴" if veredicto == "malo_confirmado" else "🟢"
        veredictos.append(
            f"{marca} {p['clave_str']} [{info['lo']:.2f},{info['hi']:.2f}) "
            f"n={info['n']} pnl_medio={info['pnl_medio']:+.3f} p={info['p_valor']:.4f} "
            f"loo={info['robusto_loo']} boot90={info['ci90_bootstrap']} {veredicto}"
        )

    print(f"\n{len(veredictos)} ventana(s) con veredicto final:")
    for linea in veredictos:
        print(f"  {linea}")
    if pendientes_confirmacion:
        print(f"\n{len(pendientes_confirmacion)} ventana(s) pendientes de 2ª confirmación mañana:")
        for linea in pendientes_confirmacion:
            print(f"  {linea}")

    # /code-review 01-Sep, ronda 2: barrido final de seguridad centralizado
    # (antes duplicado inline en los 3 ficheros "_fino") -- cualquier clave
    # con historial_crudo previo no preservada por ninguno de los puntos de
    # salida de arriba (p.ej. info truthy pero sin pasar split_half_ok/
    # robusto_loo/robusto_bootstrap) igualmente conserva su historial en vez
    # de perderlo.
    sembrar_no_confirmados(historial_previo, salida_final)

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(salida_final, f, indent=2, ensure_ascii=False)
    print(f"\nGuardado en {OUT} ({len(salida_final)} claves con veredicto)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
