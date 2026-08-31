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

REPO = Path(__file__).resolve().parent
OUT = REPO / "data/shadow/wallet_mirror_gate_bucket_fino.json"


def _cargar_veredictos_crudos_previos() -> dict:
    """{clave_str: veredicto_crudo} de la corrida anterior -- mismo guard
    de 2 días que el resto de gates (31-Ago, /code-review encontró que
    esta ruta "fina" evitaba por completo el guard del grid principal
    vía la promoción aditiva en wallet_mirror_gate_bucket.py::evaluar()).
    Este gate ya opera con dinero real (WALLET_MIRROR#BTC, DRY_RUN=False
    desde 11-Ago). Fail-closed: fichero ausente/corrupto -> {}."""
    try:
        with open(OUT, encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        return {}
    return {clave_str: info.get("veredicto_crudo_hoy") or info.get("veredicto")
            for clave_str, info in data.items() if isinstance(info, dict)}


def main() -> int:
    grupos = cargar_filas()
    print(f"Grupos (tipo,activo,marco,grande): {len(grupos)}")
    veredictos_crudos_previos = _cargar_veredictos_crudos_previos()

    pendientes = []
    resultado = {}
    for clave, filas in grupos.items():
        tipo, activo, marco, grande = clave
        clave_str = f"{tipo}#{activo}#{marco}#{grande}"
        info = evaluar_tupla(filas)
        if not info:
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
    salida_final = {}
    for idx, p in enumerate(pendientes):
        if idx not in sobreviven:
            continue
        info = p["info"]
        if p["diff"] < 0:
            veredicto_crudo = "malo_confirmado"
        elif info["pnl_medio"] >= 0:
            veredicto_crudo = "bueno_confirmado"
        else:
            continue

        info["veredicto_crudo_hoy"] = veredicto_crudo
        if veredicto_crudo == "malo_confirmado":
            veredicto = "malo_confirmado"
        elif veredictos_crudos_previos.get(p["clave_str"]) == "bueno_confirmado":
            veredicto = "bueno_confirmado"
        else:
            veredicto = "sin_concluir"
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

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(salida_final, f, indent=2, ensure_ascii=False)
    print(f"\nGuardado en {OUT} ({len(salida_final)} claves con veredicto)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
