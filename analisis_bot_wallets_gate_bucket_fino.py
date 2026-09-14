#!/usr/bin/env python3
"""analisis_bot_wallets_gate_bucket_fino.py — ventana deslizante (mismo
mecanismo que analisis_gate_bucket_fino.py/analisis_wallet_mirror_gate_
bucket_fino_25ago.py) aplicada a la familia P-GALLINA (SNIPER/DISPERSO/
WEEKLY_TEMPRANO/WEEKLY_TARDIO).

Origen (14-Sep, petición explícita Javi tras encontrar que 5 buckets
SNIPER ya `bueno_confirmado` en el grid fijo (0.05) seguían bloqueados
para dinero real solo porque BUCKETS_APROBADOS_REAL no se había
actualizado desde el 10-Sep, y "creo que con sniper estamos dejando
dinero encima de la mesa, es una estrategia que funciona"): esta familia
tenía grid pero NUNCA tuvo fino, a diferencia de wallet_mirror/sports_
wallet_mirror -- el grid fijo de 0.05 puede diluir un edge real más
estrecho o desplazado del corte del grid (mismo patrón que rescató
BALLENAS_TARDIAS#ETH#5min el 20-Ago y confirmó SEGUIR#BNB#5min[0.44,0.49)
para Wallet Mirror el 11-Sep).

Reusa TODO sin duplicar: `cargar_filas()` de analisis_bot_wallets_gate_
bucket_25ago.py (ya filtra TWAP+fillability real+ratio_vs_stake) da
grupos (arquetipo,activo,marco) -> [(ts,ask,pnl)]; `evaluar_tupla()`/
`bh_fdr_signif()` de analisis_gate_bucket_fino.py (max-statistic + LOO +
bootstrap CI90%, sin reimplementar el rigor); `_degradar()`/`_cargar_
pnl_real_crudo()` del propio gate grid (mismo veto de payout
asimétrico g_kelly + verdad-de-suelo, construido en la misma sesión).
Solo lectura -- no toca ningún gate real ni pares_permitidos_live.
"""
import json
import math
from pathlib import Path

from analisis_bot_wallets_gate_bucket_25ago import (
    cargar_filas, _cargar_pnl_real_crudo, _degradar, F_KELLY,
)
from analisis_gate_bucket_fino import evaluar_tupla, bh_fdr_signif, P_MAX
from gate_confirmacion_historial import (
    cargar_historial_previo, cargar_fecha_historial_previo,
    veredicto_con_tolerancia_diario, sembrar_no_confirmados,
)

REPO = Path(__file__).resolve().parent
OUT = REPO / "data/shadow/bot_wallets_gate_bucket_fino.json"

# 14-Sep: mismo umbral que WALLET_MIRROR (N_MIN_WALLET_MIRROR=40) -- la
# ventana deslizante prueba ~95 posiciones por clave, necesita más n que
# el grid fijo (N_MIN=15) para no sobreajustar al ruido.
N_MIN_FINO = 40


def main() -> int:
    grupos = cargar_filas()
    print(f"Grupos (arquetipo,activo,marco): {len(grupos)}")
    pnl_real_crudo = _cargar_pnl_real_crudo()
    historial_previo = cargar_historial_previo(OUT, anidado_por_bucket=False)
    # Este generador corre horario (vigia_bot_wallets_gate_bucket_fino.py,
    # vigias_frecuentes_fase0.py) -- mismo fix de "día" real (no de corrida)
    # que sus 2 hermanos ya usan.
    fecha_historial_previo = cargar_fecha_historial_previo(OUT, anidado_por_bucket=False)
    salida_final = {}

    def _preservar_historial(clave_str: str) -> None:
        hist = historial_previo.get(clave_str)
        if hist and clave_str not in salida_final:
            salida_final[clave_str] = {"veredicto": "sin_concluir", "historial_crudo": hist,
                                        "fecha_historial": fecha_historial_previo.get(clave_str)}

    pendientes = []
    resultado = {}
    filas_por_clave = {}
    for clave, filas in grupos.items():
        arquetipo, activo, marco = clave
        clave_str = f"{arquetipo}#{activo}#{marco}"
        info = evaluar_tupla(filas, seed_key=clave_str)
        if not info:
            _preservar_historial(clave_str)
            continue
        resultado[clave_str] = info
        filas_por_clave[clave_str] = filas
        if info["split_half_ok"] and info["robusto_loo"] and info["robusto_bootstrap"]:
            pendientes.append({"clave_str": clave_str, "activo": activo, "marco": marco,
                                "info": info, "p": info["p_valor"], "diff": info["diff_vs_resto"]})

    # BH-FDR por (activo,marco) -- mismo nivel de agrupación que el grid
    # (analisis_bot_wallets_gate_bucket_25ago.py), no por activo solo.
    por_grupo = {}
    for idx, p in enumerate(pendientes):
        por_grupo.setdefault((p["activo"], p["marco"]), []).append(idx)

    sobreviven = set()
    for grupo, indices in por_grupo.items():
        p_valores_grupo = [pendientes[i]["p"] for i in indices]
        sobreviven |= {indices[j] for j in bh_fdr_signif(p_valores_grupo, q=P_MAX)}

    print(f"\nVentanas candidatas (n>=40 tupla, robustas LOO+bootstrap): {len(pendientes)} "
          f"| sobreviven BH-FDR por (activo,marco): {len(sobreviven)}")

    veredictos = []
    pendientes_confirmacion = []

    for idx, p in enumerate(pendientes):
        if idx not in sobreviven:
            _preservar_historial(p["clave_str"])
            continue
        info = p["info"]
        if p["diff"] < 0:
            veredicto_crudo = "malo_confirmado"
        elif info["pnl_medio"] >= 0 and info["n"] >= N_MIN_FINO:
            veredicto_crudo = "bueno_confirmado"
        else:
            _preservar_historial(p["clave_str"])
            continue

        # g_kelly no viene de evaluar_tupla() (solo agregados) -- se
        # recalcula sobre los pnls (shadow) reales de la ventana ganadora
        # [lo,hi), mismo F_KELLY importado del grid (antes duplicado como
        # literal 0.10, /code-review 14-Sep: se desincronizaría en
        # silencio si alguien tunea F_KELLY solo en el grid).
        pnls_ventana = [pnl for ts, py, pnl in filas_por_clave[p["clave_str"]]
                        if info["lo"] <= py < info["hi"]]
        g_kelly = (sum(math.log(1 + F_KELLY * x) for x in pnls_ventana) / len(pnls_ventana)
                   if pnls_ventana else None)
        info["g_kelly_f10"] = round(g_kelly, 5) if g_kelly is not None else None
        # /code-review 14-Sep: el veto de "verdad de suelo" (trades REALES
        # con dinero, no shadow) necesita un lookup por RANGO [lo,hi) --
        # el bucket exacto del grid (0.05) casi nunca coincide con el
        # corte libre (0.01) de la ventana ganadora fina. Se construye un
        # dict sintético de una sola clave/bucket con los reales que caen
        # dentro de esta ventana concreta, para reusar _degradar() sin
        # tocar su firma.
        reales_en_rango = [pnl for ask, pnl in pnl_real_crudo.get(p["clave_str"], [])
                            if info["lo"] <= ask < info["hi"]]
        pnl_real_ventana = {p["clave_str"]: {f"{info['lo']:.2f}": reales_en_rango}} if reales_en_rango else {}
        veredicto_crudo, nota_payout, nota_real, _ = _degradar(
            veredicto_crudo, info, p["clave_str"],
            f"{info['lo']:.2f}", pnl_real_ventana)
        info["veredicto_crudo_hoy"] = veredicto_crudo
        veredicto, info["historial_crudo"], info["fecha_historial"] = veredicto_con_tolerancia_diario(
            veredicto_crudo, historial_previo.get(p["clave_str"]), fecha_historial_previo.get(p["clave_str"]))
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
        g_kelly_str = f"{g_kelly:+.5f}" if g_kelly is not None else "N/A"
        veredictos.append(
            f"{marca} {p['clave_str']} [{info['lo']:.2f},{info['hi']:.2f}) "
            f"n={info['n']} pnl_medio={info['pnl_medio']:+.3f} g_kelly={g_kelly_str} "
            f"p={info['p_valor']:.4f} loo={info['robusto_loo']} boot90={info['ci90_bootstrap']} "
            f"{veredicto}{nota_payout}{nota_real}"
        )

    print(f"\n{len(veredictos)} ventana(s) con veredicto final:")
    for linea in veredictos:
        print(f"  {linea}")
    if pendientes_confirmacion:
        print(f"\n{len(pendientes_confirmacion)} ventana(s) pendientes de 2ª confirmación mañana:")
        for linea in pendientes_confirmacion:
            print(f"  {linea}")

    sembrar_no_confirmados(historial_previo, salida_final)

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(salida_final, f, indent=2, ensure_ascii=False)
    print(f"\nGuardado en {OUT} ({len(salida_final)} claves con veredicto)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
