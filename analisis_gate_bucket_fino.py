"""
analisis_gate_bucket_fino.py — gate de entrada por VENTANA DESLIZANTE de
precio (paso 0.01, ancho 0.05 libre, no anclado al grid fijo 0.00/0.05/
0.10/...) sobre NUESTRO PROPIO histórico de PnL (results.csv). Complementa
a gate_bucket_propio.py/analisis_gate_bucket_propio_28jul.py, NO lo
sustituye -- reusa su carga de datos, su BH-FDR por (familia,moneda) y su
filtro TWAP tal cual, importados de ahí sin duplicar.

Origen (20-Ago, petición explícita Javi, "esto lo vamos a tener que
conectar a todo el sistema... solo así sabremos cuáles son los micro-
buckets que dan dinero de forma exacta"): al investigar por qué
BALLENAS_TARDIAS#ETH#5min#BUY_YES (tupla LIVE) lleva 8 días sin operar
pese a que el grid fijo nunca confirma nada, se encontró que el bucket
fijo [0.05,0.10) (n=53, pnl/tr=+0.25€) mezclaba una zona real más
estrecha [0.05,0.09) (n=39, pnl/tr=+0.73€) con una cola [0.09,0.10)
que pierde el 100% de las veces (n=14, pnl/tr=-1.07€) -- el grid fijo
diluía un edge real casi a la mitad. Ver idea_gate_bucket_fino_ventana_
deslizante_20ago en memoria para el hallazgo original completo (incluye
el caveat de fragilidad: n=39 con solo 4 aciertos, alta varianza).

Por qué el rigor es DISTINTO al de gate_bucket_propio.py, no solo "más
fino": con paso 0.01 y ancho 0.05 se evalúan ~95 posiciones de ventana
por tupla -- comparar la MEJOR posición encontrada contra un shuffle
simple (ventana vs resto) infla falsos positivos, porque "elegir la
mejor de 95" ya es en sí mismo un test múltiple que un shuffle de 2
grupos no corrige. Aquí se usa un test de PERMUTACIÓN MAX-STATISTIC
(estilo Westfall-Young): en cada shuffle se re-hace el MISMO barrido de
~95 ventanas y se guarda el mejor |diff| alcanzable por puro azar bajo
esa misma búsqueda -- el p-valor final ya lleva incorporada la
corrección por haber buscado entre muchas ventanas, no hace falta BH-FDR
adicional DENTRO de la tupla (el BH-FDR por familia+moneda que se aplica
después es el mismo de siempre, ENTRE tuplas).

Solo lectura -- no cambia prob_yes/stake/pares_permitidos_live. Genera
data/shadow/gate_bucket_fino.json, consumido por gate_bucket_propio.py
como fuente adicional de PROMOCIÓN a bueno_confirmado (mismo patrón
aditivo que _zonas_validadas_externamente(): solo puede promover un
veredicto propio "sin_concluir", nunca pisa un malo_confirmado/
bueno_confirmado ya decidido por el grid fijo o por otra extensión).
"""
import json
from pathlib import Path

import numpy as np

from gate_confirmacion_historial import (
    cargar_historial_previo, veredicto_con_tolerancia, sembrar_no_confirmados,
)
from analisis_gate_bucket_propio_28jul import (
    cargar_tuplas_live, cargar_filas, bh_fdr_signif,
    N_MIN as N_MIN_GRUESO, P_MAX,
)
from kelly_precio_gate import _familia

REPO = Path(__file__).resolve().parent
OUT = str(REPO / "data/shadow/gate_bucket_fino.json")

STEP_SCAN = 0.01     # paso de la ventana deslizante
WIDTH = 0.05          # mismo ancho que el grid fijo, pero SIN anclar a múltiplos de 0.05
N_MIN_VENTANA = 40    # 01-Sep: subido de 15->40 (mismo fix que WALLET_MIRROR el
# mismo día, ver nota "_pares_walletmirror_pausa_nota_2026-09-01" en
# config_live.json) -- confirmar con n=15-30 dispara dinero real y luego se
# revierte a sin_concluir/malo_confirmado con más datos (el gate NUNCA debería
# ser más laxo que el estándar de rigor del resto del proyecto, CLAUDE.md:
# "ninguna conclusión de estrategia con n<15" es el PISO absoluto, no el
# listón de confirmación para dinero real). Único impacto en tuplas YA live:
# BALLENAS_CONFIRMADAS_15M#ETH#15min#BUY_YES (único bucket fino confirmado,
# n=17) pasa a sin_concluir -- su grid tampoco confirma nada (sin_concluir),
# así que el gate combinado (evaluar()) deja de decir bueno_confirmado y el
# ejecutor fail-closed (ballenas_executor_15min.py) deja de operar la tupla
# hasta que acumule n>=40 real -- mismo criterio que WALLET_MIRROR, sin tocar
# pares_permitidos_live (no hace falta, el gate ya protege solo).
N_MIN_TUPLA = 40      # mínimo total en la tupla para que valga la pena buscar
ITERS = 2000

_rng = np.random.default_rng(77)


def _posiciones_validas(py_sorted, n_total):
    """Índices [idx_lo, idx_hi) de cada ventana [lo, lo+WIDTH) con paso
    STEP_SCAN que tiene >= N_MIN_VENTANA filas -- calculado UNA VEZ por
    tupla (los límites de índice no cambian entre permutaciones porque
    solo se baraja pnl, nunca py)."""
    posiciones = []
    lo = 0.0
    while lo <= 0.95 + 1e-9:
        hi = lo + WIDTH
        idx_lo = int(np.searchsorted(py_sorted, lo, side="left"))
        idx_hi = int(np.searchsorted(py_sorted, hi, side="left"))
        n_v = idx_hi - idx_lo
        if n_v >= N_MIN_VENTANA and n_v < n_total:
            posiciones.append((round(lo, 2), round(hi, 2), idx_lo, idx_hi))
        lo = round(lo + STEP_SCAN, 2)
    return posiciones


def _mejor_ventana(pnl_sorted, posiciones, cumsum, total_sum, n_total):
    """Devuelve (idx_posicion_ganadora, diff_real) maximizando |diff| =
    |media_ventana - media_resto| entre las posiciones válidas."""
    mejor_i, mejor_abs_diff, mejor_diff = None, -1.0, 0.0
    for i, (lo, hi, idx_lo, idx_hi) in enumerate(posiciones):
        n_v = idx_hi - idx_lo
        suma_v = cumsum[idx_hi] - cumsum[idx_lo]
        media_v = suma_v / n_v
        n_resto = n_total - n_v
        if n_resto <= 0:
            continue
        media_resto = (total_sum - suma_v) / n_resto
        diff = media_v - media_resto
        if abs(diff) > mejor_abs_diff:
            mejor_abs_diff, mejor_diff, mejor_i = abs(diff), diff, i
    return mejor_i, mejor_diff


def evaluar_tupla(filas):
    """filas: [(ts, py, pnl), ...]. Devuelve dict con la ventana ganadora
    y su rigor, o {} si no hay suficiente n o ninguna ventana válida."""
    n_total = len(filas)
    if n_total < N_MIN_TUPLA:
        return {}
    orden = sorted(range(n_total), key=lambda i: filas[i][1])
    py_sorted = np.array([filas[i][1] for i in orden], dtype=np.float64)
    pnl_sorted_real = np.array([filas[i][2] for i in orden], dtype=np.float64)
    ts_sorted_real = [filas[i][0] for i in orden]

    posiciones = _posiciones_validas(py_sorted, n_total)
    if not posiciones:
        return {}

    cumsum_real = np.concatenate([[0.0], np.cumsum(pnl_sorted_real)])
    total_sum = float(pnl_sorted_real.sum())
    idx_gan, diff_real = _mejor_ventana(pnl_sorted_real, posiciones, cumsum_real, total_sum, n_total)
    if idx_gan is None:
        return {}
    lo, hi, idx_lo, idx_hi = posiciones[idx_gan]
    n_v = idx_hi - idx_lo
    pnl_medio = float(pnl_sorted_real[idx_lo:idx_hi].mean())

    # Robustez leave-one-out frente a outliers de payout extremo (21-Ago):
    # con paso 0.01 y N_MIN_VENTANA=15, una ventana ganadora puede depender
    # de 1-2 trades con pago muy asimétrico (longshot: BUY_NO a precio
    # extremo, pocos aciertos que pagan 30-50x el resto) -- el shuffle
    # max-statistic es válido estadísticamente (reproduce la misma cola
    # gorda bajo la nula), pero eso no implica que el EDICTO sea fiable
    # económicamente: quitar un solo trade puede cambiar el signo. Hallazgo
    # real que motivó esto: UPDOWN_GBM_15M_TARDIO#SOL#15min#BUY_NO
    # [0.95,1.00) n=16, hit=25%, pnl/tr=+9.87 -- 4 aciertos de 16 pagando
    # 30x-50x el resto; sin este check habría pasado el gate igual.
    pnl_ventana = pnl_sorted_real[idx_lo:idx_hi]
    idx_extremo = int(np.argmax(np.abs(pnl_ventana - pnl_medio)))
    pnl_loo = np.delete(pnl_ventana, idx_extremo)
    pnl_medio_loo = float(pnl_loo.mean()) if len(pnl_loo) else 0.0
    robusto_loo = bool(len(pnl_loo) > 0 and (pnl_medio_loo > 0) == (pnl_medio > 0)
                        and abs(pnl_medio_loo) > 0.05 * abs(pnl_medio))

    # Bootstrap CI90% dentro de la propia ventana (complementa al LOO):
    # captura el caso donde el edge no depende de UN trade concreto sino de
    # que pocos aciertos con pago grande dominan un hit-rate bajo (ej. n=16
    # con 4 aciertos pagando 30x-50x -- quitar cualquier trade individual
    # sigue positivo, pero el CI de remuestreo sí se acerca a/cruza cero
    # porque la mayoría de remuestreos con reemplazo caen en réplicas de
    # las 12 pérdidas). Semilla fija (misma _rng que el max-statistic) para
    # reproducibilidad dentro de la corrida.
    boots_idx = _rng.integers(0, n_v, size=(2000, n_v))
    boots_medias = pnl_ventana[boots_idx].mean(axis=1)
    boots_medias.sort()
    ci_lo90 = float(boots_medias[int(0.05 * len(boots_medias))])
    ci_hi90 = float(boots_medias[int(0.95 * len(boots_medias))])
    robusto_bootstrap = bool(ci_lo90 > 0 if pnl_medio > 0 else ci_hi90 < 0)

    # Test de permutación max-statistic: barajar pnl (py fijo), rehacer el
    # MISMO barrido de posiciones, guardar el mejor |diff| bajo la nula.
    idx_los = np.array([p[2] for p in posiciones])
    idx_his = np.array([p[3] for p in posiciones])
    n_vs = idx_his - idx_los
    mejores_null = np.empty(ITERS, dtype=np.float64)
    for it in range(ITERS):
        perm = _rng.permutation(pnl_sorted_real)
        cs = np.concatenate([[0.0], np.cumsum(perm)])
        sumas_v = cs[idx_his] - cs[idx_los]
        medias_v = sumas_v / n_vs
        medias_resto = (total_sum - sumas_v) / (n_total - n_vs)
        diffs = np.abs(medias_v - medias_resto)
        mejores_null[it] = diffs.max()
    p_valor = float(np.mean(mejores_null >= abs(diff_real)))

    # split-half cronológico de la ventana ganadora (mismo criterio que
    # analisis_gate_bucket_propio_28jul.py)
    ts_py_pnl = list(zip(ts_sorted_real[idx_lo:idx_hi], pnl_sorted_real[idx_lo:idx_hi]))
    ts_py_pnl.sort(key=lambda x: x[0])
    mid = n_v // 2
    m1, m2 = ts_py_pnl[:mid], ts_py_pnl[mid:]
    split_half_diff = None
    consistente = False
    if len(m1) >= 5 and len(m2) >= 5:
        media_resto_total = (total_sum - (cumsum_real[idx_hi] - cumsum_real[idx_lo])) / (n_total - n_v)
        d1 = sum(p for _, p in m1) / len(m1) - media_resto_total
        d2 = sum(p for _, p in m2) / len(m2) - media_resto_total
        split_half_diff = [round(float(d1), 4), round(float(d2), 4)]
        consistente = (d1 < 0 and d2 < 0) or (d1 > 0 and d2 > 0)

    return {
        "lo": lo, "hi": hi, "n": n_v, "pnl_medio": round(pnl_medio, 4),
        "diff_vs_resto": round(float(diff_real), 4), "p_valor": round(p_valor, 4),
        "split_half_diff": split_half_diff, "split_half_ok": bool(consistente),
        "pnl_medio_loo": round(pnl_medio_loo, 4), "robusto_loo": robusto_loo,
        "ci90_bootstrap": [round(ci_lo90, 4), round(ci_hi90, 4)],
        "robusto_bootstrap": robusto_bootstrap,
        "n_posiciones_buscadas": len(posiciones),
    }


def main() -> int:
    tuplas = cargar_tuplas_live()
    filas_por_tupla = cargar_filas(tuplas)
    n_live = sum(1 for *_, es_live in tuplas if es_live)
    print(f"Tuplas a evaluar: {len(tuplas)} ({n_live} live, {len(tuplas) - n_live} candidatos)")
    historial_previo = cargar_historial_previo(Path(OUT), anidado_por_bucket=False)
    salida_final = {}

    def _preservar_historial(tupla_str: str) -> None:
        """/code-review 01-Sep: si el bucket no sobrevive hoy (sin datos
        suficientes para ventana, BH-FDR, o piso absoluto), salida_final se
        guarda SIN su entrada -- y como json.dump sobreescribe el fichero
        entero, el historial_crudo acumulado desaparecía sin que hubiera
        pasado ningún día MALO, el mismo problema que este fix del 01-Sep
        quería evitar. Preserva un placeholder con el historial intacto
        (sin_concluir, sin stats frescas) para que una futura corrida que
        SÍ sobreviva pueda seguir sumando desde donde se quedó."""
        hist = historial_previo.get(tupla_str)
        if hist and tupla_str not in salida_final:
            salida_final[tupla_str] = {"veredicto": "sin_concluir", "historial_crudo": hist}

    pendientes = []
    resultado = {}
    for i, (strategy, subtype, decision, tupla_str, es_live) in enumerate(tuplas):
        if i % 25 == 0:
            print(f"  ... {i}/{len(tuplas)} tuplas (ventana deslizante)", flush=True)
        filas = filas_por_tupla.get(tupla_str, [])
        info = evaluar_tupla(filas)
        if not info:
            _preservar_historial(tupla_str)
            continue
        resultado[tupla_str] = info
        if info["split_half_ok"] and info["robusto_loo"] and info["robusto_bootstrap"]:
            pendientes.append({"tupla_str": tupla_str, "info": info,
                                "p": info["p_valor"], "diff": info["diff_vs_resto"], "es_live": es_live})

    por_familia_moneda = {}
    for idx, p in enumerate(pendientes):
        partes = p["tupla_str"].split("#")
        strategy = partes[0]
        activo = partes[1] if len(partes) > 1 else "?"
        clave = (_familia(strategy), activo)
        por_familia_moneda.setdefault(clave, []).append(idx)

    sobreviven = set()
    for (familia, activo), indices in por_familia_moneda.items():
        p_valores_grupo = [pendientes[i]["p"] for i in indices]
        sobreviven_grupo = bh_fdr_signif(p_valores_grupo, q=P_MAX)
        sobreviven |= {indices[j] for j in sobreviven_grupo}

    print(f"\nVentanas candidatas: {len(pendientes)} | sobreviven BH-FDR: {len(sobreviven)}")

    veredictos_nuevos = []
    veredictos_pendientes_confirmacion = []

    for idx, p in enumerate(pendientes):
        if idx not in sobreviven:
            _preservar_historial(p["tupla_str"])
            continue
        info = p["info"]
        if p["diff"] < 0:
            veredicto_crudo = "malo_confirmado"
        elif info["pnl_medio"] >= 0:
            veredicto_crudo = "bueno_confirmado"
        else:
            _preservar_historial(p["tupla_str"])
            continue  # mismo piso absoluto que gate_bucket_propio (08-Ago)

        info["veredicto_crudo_hoy"] = veredicto_crudo
        # 01-Sep (petición explícita Javi, "un día de mala racha no puede
        # entorpecer esto"): antes exigía que la corrida INMEDIATAMENTE
        # anterior también diera bueno_confirmado -- un solo día flojo
        # reiniciaba el progreso a cero. Ahora exige 2 de los últimos 3 días
        # (incluido hoy), tolerando un día suelto sin perder la evidencia
        # acumulada. malo_confirmado sigue siendo inmediato (ver
        # gate_confirmacion_historial.py).
        veredicto, info["historial_crudo"] = veredicto_con_tolerancia(
            veredicto_crudo, historial_previo.get(p["tupla_str"]))
        if veredicto == "sin_concluir" and veredicto_crudo == "bueno_confirmado":
            veredictos_pendientes_confirmacion.append(
                f"⏳ [{'LIVE' if p['es_live'] else 'candidato'}] {p['tupla_str']} "
                f"[{info['lo']:.2f},{info['hi']:.2f}) n={info['n']} "
                f"pnl_medio={info['pnl_medio']:+.3f} bueno_confirmado HOY, esperando confirmación de mañana"
            )

        info["veredicto"] = veredicto
        salida_final[p["tupla_str"]] = info
        if veredicto == "sin_concluir":
            continue
        marca = "🔴" if veredicto == "malo_confirmado" else "🟢"
        etiqueta = "LIVE" if p["es_live"] else "candidato"
        veredictos_nuevos.append(
            f"{marca} [{etiqueta}] {p['tupla_str']} [{info['lo']:.2f},{info['hi']:.2f}) "
            f"n={info['n']} pnl_medio={info['pnl_medio']:+.3f} p={info['p_valor']:.4f} {veredicto}"
        )

    print(f"\n{len(veredictos_nuevos)} ventana(s) con veredicto final:")
    for linea in veredictos_nuevos:
        print(f"  {linea}")
    if veredictos_pendientes_confirmacion:
        print(f"\n{len(veredictos_pendientes_confirmacion)} ventana(s) pendientes de 2ª confirmación mañana:")
        for linea in veredictos_pendientes_confirmacion:
            print(f"  {linea}")

    # /code-review 01-Sep, ronda 2: barrido final de seguridad centralizado
    # (antes duplicado inline en los 3 ficheros "_fino") -- cualquier tupla
    # con historial_crudo previo que no haya sido preservada por ninguno de
    # los puntos de salida de arriba (p.ej. info truthy pero sin pasar
    # split_half_ok/robusto_loo/robusto_bootstrap, así que nunca entra en
    # `pendientes`) igualmente conserva su historial en vez de perderlo.
    sembrar_no_confirmados(historial_previo, salida_final)

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(salida_final, f, indent=2, ensure_ascii=False)
    print(f"\nGuardado en {OUT} ({len(salida_final)} tuplas con veredicto)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
