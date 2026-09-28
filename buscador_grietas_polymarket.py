#!/usr/bin/env python3
"""buscador_grietas_polymarket.py -- (28-Sep, petición explícita Javi: "una
estrategia que se dedique exclusivamente a explotar fallas, zonas grises,
bugs, grietas, brechas, por pequeñas que sean, de Polymarket... hay mucho
dinero encima de la mesa"). MODO LECTURA -- no toca dinero, no conecta
nada solo.

Distinto de buscador_edge_perdido.py (busca dónde se fue el edge de
NUESTRAS estrategias) y de director_200k.py (dirige el portfolio) -- este
es Parte A pura: caza estructural en la PLATAFORMA misma (mecánica del
CLOB, resolución, fees, ventanas anidadas), no en wallets/ballenas. Ya
existen 2 grietas explotadas con éxito (RESOLUTION_SNIPER_PRECIERRE/NAIVE,
live) -- este script es el sitio único donde viven TODAS las candidatas,
probadas o pendientes, para que "cuánto dinero hay sobre la mesa" tenga
una respuesta con datos, no de memoria.

Cada categoría es una función `_grieta_*()` que devuelve un dict con
{nombre, estado, evidencia, accion} -- MISMO patrón que DIMENSIONES en
buscador_edge_perdido.py, pensado para crecer sin reescribir el core.
Estados: "explotada_live" | "investigando" | "refutada" | "pendiente_diseno".

Salida: data/shadow/buscador_grietas_polymarket.json + Telegram (vigía
propio, pendiente de decidir cadencia con Javi)."""
import collections
import csv
import json
import random
import sys
from datetime import datetime, timezone
from pathlib import Path

from bootstrap_dias import bootstrap_ic90_dias as _bootstrap_ic90_dias  # noqa: E402
# /code-review 28-Sep: extraído a bootstrap_dias.py -- vivía duplicada byte a
# byte en wallet_first_buy_fwd_tracker.py, riesgo real de divergencia silenciosa.

REPO = Path(__file__).resolve().parent
OUT = REPO / "data/shadow/buscador_grietas_polymarket.json"
NESTED_ARB_SIM = REPO / "data/shadow/nested_arb_sim.csv"


def _grieta_nested_arb_chainlink_vs_binance() -> dict:
    """P13/Corridor Collector (04-Ago, ya explotable con edge real pero
    18,7% de roturas de garantía sin explicar) -- pendiente identificado
    ese mismo día: "cruzar roturas contra chainlink_*.csv en vez de los
    klines Binance/Kraken que probablemente alimentan o_inner/o_outer".
    28-Sep: nested_arb_scanner.py YA captura o_inner_chainlink/o_outer_
    chainlink desde el 19-Ago (40 días) -- pero NADIE lo había analizado
    hasta hoy. Hipótesis: si Binance/Kraken y Chainlink DISCREPAN en el
    ORDEN relativo de o_inner vs o_outer, la garantía matemática se apoya
    en el precio equivocado y rompe con más frecuencia.

    Primer resultado (28-Sep, n=189/637 cerradas con chainlink poblado):
    acuerdo Binance/Chainlink en el orden -> rotura 43,9% (n=66); desacuerdo
    -> rotura 50,4% (n=123). Señal en la dirección esperada pero débil --
    NO concluyente con este n.

    28-Sep, MISMO DÍA, diagnóstico de cobertura RESUELTO (no era un bug):
    189/189 (100%) de las filas cerradas con fecha >=19-Ago tienen chainlink
    poblado -- el 30% global venía de mezclar con ~450 filas de JULIO,
    anteriores a que esta columna existiera (añadida 19-Ago). n=189 YA ES
    la muestra completa disponible desde que la funcionalidad existe, no un
    subconjunto sesgado -- el resultado débil de arriba es la lectura
    correcta con los datos de hoy, simplemente falta que pasen más días
    para tener más n."""
    if not NESTED_ARB_SIM.exists():
        return {"nombre": "nested_arb_chainlink_vs_binance", "estado": "pendiente_diseno",
                "evidencia": "nested_arb_sim.csv no existe todavía", "accion": "esperar a que el scanner acumule"}
    with open(NESTED_ARB_SIM, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    # 28-Sep: cobertura_chainlink_pct se mide SOLO sobre filas >=19-Ago (cuando la
    # columna empezó a existir) -- mezclar con julio infla artificialmente el
    # denominador y hace parecer "baja cobertura" lo que en realidad es 100%
    # desde que la funcionalidad existe (diagnóstico ya resuelto, ver docstring).
    FECHA_INICIO_CHAINLINK = "2026-08-19"
    cerradas = [r for r in rows if r.get("garantia_ok") in ("0", "1")
                and r.get("ts_entrada", "") >= FECHA_INICIO_CHAINLINK]
    con_cl = [r for r in cerradas if r.get("o_inner_chainlink") and r.get("o_outer_chainlink")]

    por_dia_acuerdo, por_dia_desacuerdo = collections.defaultdict(list), collections.defaultdict(list)
    # 28-Sep (CLAUDE.md pt.17, "desagregar SIEMPRE por moneda"): acuerdo/desacuerdo
    # por activo, no solo el agregado -- verificado con datos reales que el
    # agregado esconde diferencias reales por moneda (ETH: 35% vs 55%; BTC/XRP:
    # planos, sin diferencia). /code-review 28-Sep (2ª ronda), hallazgo real:
    # agrupar solo por activo mezcla ventanas de nesting ESTRUCTURALMENTE
    # distintas (5min15m vs 15min60m, horizontes temporales muy diferentes) --
    # CLAUDE.md pt.17 exige desagregar por moneda Y marco temporal siempre, sin
    # excepción (el mismo error ya causó el bug real de kelly_precio_gate 29-Jul
    # mezclando monedas bajo un bucket de precio). Clave compuesta activo#nesting.
    por_activo = collections.defaultdict(lambda: {"acuerdo": [], "desacuerdo": []})
    for r in con_cl:
        try:
            oi, oo = float(r["o_inner"]), float(r["o_outer"])
            oic, ooc = float(r["o_inner_chainlink"]), float(r["o_outer_chainlink"])
        except (TypeError, ValueError):
            continue
        rotura = 1.0 if r["garantia_ok"] == "0" else 0.0
        dia = r["ts_entrada"][:10]
        clave = f"{r['activo']}#{r.get('nesting') or 'sin_nesting'}"
        act = por_activo[clave]
        if (oi >= oo) == (oic >= ooc):
            por_dia_acuerdo[dia].append(rotura)
            act["acuerdo"].append(rotura)
        else:
            por_dia_desacuerdo[dia].append(rotura)
            act["desacuerdo"].append(rotura)

    por_activo_pct = {}
    for act, d in por_activo.items():
        na, nd = len(d["acuerdo"]), len(d["desacuerdo"])
        por_activo_pct[act] = {
            "tasa_acuerdo": round(sum(d["acuerdo"]) / na, 2) if na else None, "n_acuerdo": na,
            "tasa_desacuerdo": round(sum(d["desacuerdo"]) / nd, 2) if nd else None, "n_desacuerdo": nd,
        }

    n_acuerdo = sum(len(v) for v in por_dia_acuerdo.values())
    n_desacuerdo = sum(len(v) for v in por_dia_desacuerdo.values())
    n_usado = n_acuerdo + n_desacuerdo   # /code-review 28-Sep: puede ser < len(con_cl)
    # si o_inner/o_outer (no los _chainlink) vienen vacíos/mal formados -- reportar
    # AMBOS "n" explícitamente, nunca dejar que cobertura_chainlink_pct (basado en
    # con_cl) implique más filas de las que realmente entraron en acuerdo/desacuerdo.
    ic_acuerdo = _bootstrap_ic90_dias(por_dia_acuerdo)
    ic_desacuerdo = _bootstrap_ic90_dias(por_dia_desacuerdo)
    tasa_a = round(sum(x for v in por_dia_acuerdo.values() for x in v) / n_acuerdo, 3) if n_acuerdo else None
    tasa_d = round(sum(x for v in por_dia_desacuerdo.values() for x in v) / n_desacuerdo, 3) if n_desacuerdo else None

    # /code-review 28-Sep, hallazgo real: evidencia/accion tenían los números de HOY escritos a
    # mano ("35% vs 55%, n=17/33") -- esta función corre cada sesión/cron y por_activo_pct SÍ se
    # recalcula, pero el texto se quedaba congelado en el snapshot de hoy para siempre. Generado
    # dinámicamente: el grupo activo#nesting con mayor diferencia |desacuerdo-acuerdo| entre los
    # que tienen ambos lados con n>=15 (piso mínimo del proyecto, CLAUDE.md manual operativo
    # pt.2 -- "ninguna conclusión de estrategia con n<15"; NUNCA promocionable sin n>=40/lado).
    # /code-review 28-Sep (3ª ronda), hallazgo real: elegir el argmax entre ~8 grupos sin corregir
    # por múltiples comparaciones reproduce el mismo patrón que `analisis_gate_bucket_fino.py` ya
    # tuvo que corregir con max-statistic (una ventana significativa a shuffle simple p=0.0073 no
    # sobrevivió la corrección, p=0.262) -- aquí se aplica el mismo principio: permutar las
    # etiquetas acuerdo/desacuerdo DENTRO de cada grupo (preservando n_acuerdo/n_desacuerdo) y
    # comparar la diferencia máxima observada contra la distribución de máximos permutados.
    PISO_N_DESTACAR, PROMOCION_N = 15, 40
    elegibles = {act: d for act, d in por_activo_pct.items()
                 if d["n_acuerdo"] >= PISO_N_DESTACAR and d["n_desacuerdo"] >= PISO_N_DESTACAR}
    activo_destacado, diff_max = None, -1.0
    for act, d in elegibles.items():
        diff = abs(d["tasa_desacuerdo"] - d["tasa_acuerdo"])
        if diff > diff_max:
            activo_destacado, diff_max = act, diff

    def _max_stat_pvalue(n_iter: int = 2000) -> float | None:
        if not elegibles:
            return None
        rng = random.Random(7)
        pooled = {act: por_activo[act]["acuerdo"] + por_activo[act]["desacuerdo"] for act in elegibles}
        n_mayor_igual = 0
        for _ in range(n_iter):
            max_diff_perm = 0.0
            for act in elegibles:
                vals = pooled[act][:]
                rng.shuffle(vals)
                na = elegibles[act]["n_acuerdo"]
                a_perm, d_perm = vals[:na], vals[na:]
                diff_perm = abs(sum(d_perm) / len(d_perm) - sum(a_perm) / len(a_perm))
                max_diff_perm = max(max_diff_perm, diff_perm)
            if max_diff_perm >= diff_max:
                n_mayor_igual += 1
        return round(n_mayor_igual / n_iter, 4)

    p_max_stat = _max_stat_pvalue() if activo_destacado else None
    if activo_destacado:
        d = por_activo_pct[activo_destacado]
        n_min_lado = min(d["n_acuerdo"], d["n_desacuerdo"])
        signif = p_max_stat is not None and p_max_stat < 0.05
        caveat = (f" -- p_max_stat={p_max_stat} {'(pasa max-statistic)' if signif else '⚠️ NO sobrevive corrección max-statistic, probable ruido'}"
                  + ("" if n_min_lado >= PROMOCION_N else " -- ⚠️ además n<40/lado, exploratorio"))
        evidencia = (f"señal débil en agregado; desagregado por activo#nesting: {activo_destacado} muestra la mayor "
                     f"diferencia ({d['tasa_acuerdo']:.0%} vs {d['tasa_desacuerdo']:.0%} rotura, "
                     f"n={d['n_acuerdo']}/{d['n_desacuerdo']}){caveat} -- resto plano/sin diferencia clara")
        accion = (f"vigilar específicamente {activo_destacado} conforme crezca n (objetivo n>=40/lado antes de proponer nada)"
                  if signif else f"NO actuar sobre {activo_destacado} todavía (no sobrevive max-statistic) -- dejar acumular más n y repetir")
        accion += " -- cobertura ya resuelta (100% desde 19-Ago)"
    else:
        evidencia = f"señal débil en agregado; sin n suficiente por activo#nesting todavía (piso n>={PISO_N_DESTACAR} por lado) para destacar ninguno"
        accion = "dejar acumular más días -- cobertura ya resuelta (100% desde 19-Ago)"

    return {
        "nombre": "nested_arb_chainlink_vs_binance", "estado": "investigando",
        "n_cerradas_total": len(cerradas), "n_con_chainlink_bruto": len(con_cl), "n_usado_en_gate": n_usado,
        "cobertura_chainlink_pct": round(100 * len(con_cl) / len(cerradas), 1) if cerradas else None,
        "tasa_rotura_acuerdo": tasa_a, "n_acuerdo": n_acuerdo, "ic90_dias_acuerdo": ic_acuerdo,
        "tasa_rotura_desacuerdo": tasa_d, "n_desacuerdo": n_desacuerdo, "ic90_dias_desacuerdo": ic_desacuerdo,
        "por_activo": por_activo_pct,
        "activo_destacado": activo_destacado,
        "p_max_stat": p_max_stat,
        "evidencia": evidencia,
        "accion": accion,
    }


def _grieta_box_builder() -> dict:
    """04-Ago: REFUTADO (0/62 con profundidad real en ambos lados YES+NO
    simultáneamente) -- re-chequeo periódico porque la profundidad del
    libro cambia con el tiempo (más volumen podría abrir esto)."""
    return {"nombre": "box_builder_complementario", "estado": "refutada_04ago",
            "evidencia": "0/62 con profundidad real en ambos lados (04-Ago)",
            "accion": "re-chequear cada mes si el volumen global de Polymarket crece mucho"}


def _grieta_spread_harvest_maker() -> dict:
    """11-Ago: REFUTADO (libro ancho solo 0,435% del tiempo, spread real
    0,31€ -- insuficiente para maker rentable)."""
    return {"nombre": "spread_harvest_maker", "estado": "refutada_11ago",
            "evidencia": "libro ancho solo 0,435% del tiempo (11-Ago)",
            "accion": "cerrado, no reabrir sin evidencia radicalmente nueva"}


def _grieta_resolution_freeze_instante() -> dict:
    """15-Sep: FASE 0 en marcha (resolution_sniper_freeze_estado_fase0.py,
    screen observadores) -- mapea el instante exacto (ms) en que Polymarket
    deja de aceptar órdenes cerca del cierre. Primera ventana no concluyente
    (accepting_orders=True hasta +0,27s DESPUÉS del cierre en un caso,
    contradice la prueba real de precierre que fue rechazada A ANTES del
    cierre) -- necesita más muestra antes de concluir dónde está el límite
    real, y si varía por activo/marco."""
    return {"nombre": "resolution_freeze_instante_exacto", "estado": "investigando",
            "evidencia": "FASE 0 solo observación, primera ventana (15-Sep) inconclusa",
            "accion": "revisar data/shadow/resolution_sniper_freeze_estado_fase0.csv, dejar acumular"}


def _grieta_precierre_naive() -> dict:
    """YA EXPLOTADA, live desde 23-Sep -- la grieta de referencia: el
    mercado resuelve por TWAP60 oficial (regla real, 99-99,8% acierto) pero
    el modelo naive de la mayoría de operadores usa spot/última operación,
    dejando una ventana de dirección casi cierta en los últimos segundos."""
    return {"nombre": "precierre_naive_twap", "estado": "explotada_live",
            "evidencia": "24 tuplas 5/15min live desde 23-Sep, ver CLAUDE.md",
            "accion": "ninguna -- referencia de qué tipo de grieta buscar"}


def _grieta_taker_rebate_tier() -> dict:
    """27-Ago: descubierto el programa de rebate por volumen (7 tiers,
    peso cripto 2,3x el más alto) -- estructural, viento de cola al
    escalar volumen, hoy muy por debajo del primer tier (Bronze $2000wV).
    No es una grieta a "explotar" con una operación puntual -- es un
    parámetro a vigilar conforme crezca el volumen real."""
    return {"nombre": "taker_rebate_program", "estado": "pendiente_diseno",
            "evidencia": "wV≈$174/30d hoy, Bronze=$2000wV (27-Ago)",
            "accion": "instrumentar tracking de wV/tier como KPI cuando el volumen real lo justifique"}


# Categorías NO exploradas todavía -- roadmap explícito, NO fingir que están hechas.
CATEGORIAS_PENDIENTES = [
    "listado de mercados nuevos: ¿hay ventana de precio no descubierto entre gamma-api "
    "y CLOB? (apertura_libro_fase0.py ya midió esto en 5/15min: abre cerca de 0,50, sin "
    "hueco -- pendiente probar en 60min/240min/weekly, mercados con menos ojos encima)",
    "comportamiento de fill parcial FOK vs GTC en condiciones de baja liquidez -- ¿hay un "
    "patrón explotable en CUÁNTO fillan las órdenes marketable cerca del suelo de tamaño?",
    "consistencia de tick size / redondeo entre denominaciones de precio (ya hubo un bug "
    "real de decimales en el CLOB, arreglado -- revisar si queda algún residuo)",
    "ventanas de mantenimiento/incidentes de la plataforma (vigia_actualizaciones_"
    "polymarket.py ya vigila el changelog -- falta cruzar avisos de incidentes con "
    "movimientos de precio anómalos durante esas ventanas)",
]

REGISTRO = [
    _grieta_precierre_naive,
    _grieta_nested_arb_chainlink_vs_binance,
    _grieta_resolution_freeze_instante,
    _grieta_taker_rebate_tier,
    _grieta_box_builder,
    _grieta_spread_harvest_maker,
]


def main() -> int:
    grietas = [fn() for fn in REGISTRO]
    salida = {
        "actualizado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "grietas": grietas,
        "categorias_pendientes_sin_explorar": CATEGORIAS_PENDIENTES,
    }
    OUT.write_text(json.dumps(salida, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"[buscador_grietas_polymarket] {len(grietas)} grietas registradas:")
    for g in grietas:
        print(f"  [{g['estado']}] {g['nombre']} -- {g['accion']}")
    print(f"  {len(CATEGORIAS_PENDIENTES)} categorías sin explorar todavía")
    print(f"Guardado en {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
