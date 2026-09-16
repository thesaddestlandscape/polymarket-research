#!/usr/bin/env python3
"""analisis_sniper_ventana_tiempo_16sep.py — gate riguroso por CELDA
(precio × tiempo-restante-hasta-resolución) para el arquetipo SNIPER,
COMPLEMENTO del gate de precio ya vivo (bot_wallets_gate_bucket.py),
nunca lo sustituye.

Origen (16-Sep, petición explícita Javi, "vamos con el sniper"): dose-
response real encontrado en bot_wallets_gate_bucket_fase0.csv -- SNIPER
que entra 120-300s antes de resolución en ciertas bandas de precio ALTAS
(ya cerca de certeza, 0.70-0.95) acierta muy por encima de su baseline
del propio marco (5min: n=803, hit=86.4% vs baseline 62.6%, shuffle
p=0.00000; 15min: n=170, hit=97.1% vs baseline 70.6%, shuffle p=0.00000).
Verificado que el efecto NO es uniforme por precio -- bandas <0.70 dan
EV negativo en TODAS las ventanas de tiempo probadas (Javi, "diría que
no [afecta a todos los buckets] porque las entradas tempranas a precios
bajos..." -- confirmado con datos, ver idea_sniper_ventanas_tiempo_
confirmado_marco_16sep). Por eso la celda de gate es SIEMPRE conjunta
(precio Y tiempo a la vez), nunca un corte de tiempo aplicado a todo el
rango de precio.

Diseño (petición explícita Javi): "conforme vayan entrando buckets de
precio altos se irá integrando solo este efecto de forma automática" --
por eso este script escanea TODA la rejilla (activo,marco,bucket_precio,
bucket_tiempo) con datos suficientes, no solo las 2 celdas encontradas
hoy a mano. Cualquier celda nueva que cruce el mismo rigor se confirma
sola en el próximo ciclo del cron, sin tocar código (mismo criterio que
gate_bucket_propio.py: "NO crear tablas de zonas hardcodeadas").

Reusa TAL CUAL (decisión ladder, nunca duplicar la fórmula) de
analisis_bot_wallets_gate_bucket_25ago.py: pnl_neto() (ask real, NUNCA
precio_wallet -- ya refutado como aproximación optimista el 10-Ago),
shuffle_test(), bh_fdr_signif(). Reusa de gate_confirmacion_historial.py
la tolerancia multi-día (2 de los últimos 3 días para bueno_confirmado,
inmediato para malo_confirmado) -- mismo patrón que TODOS los hermanos
de esta familia desde el 01/10-Sep.

16-Sep (corrección en caliente, verificado con datos reales): el shuffle
"celda vs resto del marco" NO detecta esta celda pese a que el hit-rate
es claramente superior a su propio breakeven (Wilson manual 82-92% vs
breakeven ~55-65%) -- el "resto" mezcla zonas pésimas (precio<0.70,
pnl~-1.0) con zonas decentes, diluye la varianza. Se añadió la vía
ABSOLUTA (bootstrap_absoluto/UMBRAL_ABSOLUTO_EUR, reusada TAL CUAL de
analisis_gate_bucket_propio_28jul.py, mismo mecanismo que ya rescata
casos así en el hermano de precio-solo) como RESCATE: si la vía relativa
deja una celda en sin_concluir pero su media supera 0,10€ con bootstrap
significativo Y ambas mitades del split-half superan igual el umbral,
se confirma por esta vía. Nunca pisa un veredicto ya resuelto por la vía
relativa. Cruce informativo con ballenas SIGUE sin incluir en esta v1
(defer real, no bloqueante).

Rigor: n_min=15 por celda para generar candidato, shuffle test celda vs
RESTO del marco (vía relativa) + bootstrap contra 0,10€ (vía absoluta,
rescate), BH-FDR por marco en cada vía por separado, split-half
cronológico en ambas, concentración top1-wallet auto-degradante (>50%
degrada bueno_confirmado→sin_concluir, mismo umbral que el hermano de
precio), g_kelly(f=10%) informativo.

Solo lectura. Escribe data/shadow/sniper_ventana_tiempo_gate.json.
No conectado a pares_permitidos_live -- FASE 0.
"""
import csv
import json
import math
import sys
import zlib
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

import numpy as np

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from analisis_bot_wallets_gate_bucket_25ago import (  # noqa: E402
    pnl_neto, shuffle_test, bh_fdr_signif, F_KELLY, RATIO_MIN, FEE,
)
from analisis_gate_bucket_propio_28jul import (  # noqa: E402
    UMBRAL_ABSOLUTO_EUR, bootstrap_absoluto,
)
from gate_confirmacion_historial import cargar_historial_previo, veredicto_con_tolerancia  # noqa: E402
import shadow_postmortem as sp  # noqa: E402 -- reusa es_pre_twap

IN = REPO / "data/shadow/bot_wallets_gate_bucket_fase0.csv"
OUT = REPO / "data/shadow/sniper_ventana_tiempo_gate.json"

STEP_PRECIO = 0.05
# Ventanas de tiempo probadas hoy con n suficiente (120-300s) -- el resto
# de cortes (<30s/30-60s/60-120s) también se escanean por si acumulan n,
# pero el hallazgo de hoy vive en 120-300s.
CORTES_TIEMPO = [(0, 30), (30, 60), (60, 120), (120, 300), (300, 3600)]
N_MIN = 15
P_MAX = 0.05
CONCENTRACION_TOP1_MAX = 0.50  # mismo umbral que el hermano de precio-solo


def bucket_precio(p):
    return round(math.floor(p / STEP_PRECIO + 1e-9) * STEP_PRECIO, 4)


def bucket_tiempo(seg):
    for lo, hi in CORTES_TIEMPO:
        if lo <= seg < hi:
            return f"{lo}-{hi}s"
    return None


def _parse_ts(s):
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except Exception:
        return None


def cargar_filas():
    """clave (arquetipo,marco) -> [(ts, ask, pnl, wallet, bucket_tiempo_str, activo), ...]
    Solo SNIPER (única familia con el dose-response confirmado hoy;
    DISPERSO/WEEKLY_* se dejan fuera hasta repetir este mismo análisis
    sobre ellas -- no extrapolar sin verificar cada arquetipo aparte).

    16-Sep (verificado con datos reales ANTES de decidir esto, no por
    comodidad): agrupado por MARCO, sin desagregar por activo individual
    dentro de la celda -- a diferencia del resto del proyecto (CLAUDE.md
    pt.17 exige desagregar por moneda SIEMPRE). Comprobado explícitamente
    que las 6 monedas de 5min, en la celda [0.70,0.85)+120-300s, dan
    individualmente 83-92% hit-rate (BTC n=200 83,0%, ETH n=65 86,2%, SOL
    n=41 90,2%, DOGE n=24 91,7%, BNB n=26 84,6%, XRP n=12 91,7%) -- ninguna
    arrastra a las demás, es un patrón genuinamente cross-activo. Split por
    activo INDIVIDUAL + bucket de precio de 0,05 a la vez fragmenta n por
    debajo del poder estadístico necesario (BTC solo, [0.70,0.85), 3
    sub-buckets de 0,05, ~50-80 por celda, shuffle_p>0,15 pese a pnl_medio
    positivo en las 3). Pooled por marco es la única forma de detectar con
    rigor un patrón que SÍ es real en cada moneda por separado."""
    grupos = defaultdict(list)
    with open(IN, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r.get("arquetipo") != "SNIPER":
                continue
            if not r.get("outcome_real"):
                continue
            ask_raw = r.get("mejor_ask_deteccion", "")
            if not ask_raw:
                continue
            try:
                ask = float(ask_raw)
            except (TypeError, ValueError):
                continue
            if not (0.0 < ask < 1.0):
                continue
            try:
                ratio = float(r.get("ratio_vs_stake_deteccion") or "")
            except (TypeError, ValueError):
                ratio = None
            if ratio is None or ratio < RATIO_MIN:
                continue
            tt = _parse_ts(r.get("trade_timestamp"))
            rt = _parse_ts(r.get("resolved_ts"))
            if tt is None or rt is None:
                continue
            seg = (rt - tt).total_seconds()
            if seg < 0 or seg > 3600:
                continue
            bt = bucket_tiempo(seg)
            if bt is None:
                continue
            marco = r.get("marco", "?")
            if sp.es_pre_twap(marco, r.get("timestamp_utc", "")):
                continue
            acierto = 1 if r.get("outcome_real") == r.get("lado_wallet") else 0
            pnl = pnl_neto(ask, acierto)
            clave = ("SNIPER", marco)
            grupos[clave].append((r["timestamp_utc"], ask, pnl, r.get("wallet", ""), bt, r.get("activo", "?")))
    return grupos


def main() -> int:
    grupos = cargar_filas()
    print(f"Grupos (SNIPER,marco): {len(grupos)}")

    historial_previo = cargar_historial_previo(OUT, anidado_por_bucket=True)

    resultado = {}
    pendientes = []
    candidatos_abs = []
    for clave, filas in grupos.items():
        _, marco = clave
        clave_str = f"SNIPER#{marco}"
        if len(filas) < N_MIN:
            historial_clave = historial_previo.get(clave_str, {})
            resultado[clave_str] = {
                b: {"veredicto": "sin_concluir", "historial_crudo": hist}
                for b, hist in historial_clave.items() if hist
            }
            continue

        por_celda = defaultdict(list)
        for ts, ask, pnl, wallet, bt, activo in filas:
            por_celda[(bucket_precio(ask), bt)].append((ts, pnl, wallet, activo))

        tabla = {}
        for (bp, bt) in sorted(por_celda):
            dentro = por_celda[(bp, bt)]
            fuera = [(ts, pnl) for (bb, btb), fs in por_celda.items()
                     if (bb, btb) != (bp, bt) for ts, pnl, _w, _a in fs]
            n_d = len(dentro)
            pnl_d = [pnl for _, pnl, _w, _a in dentro]
            media_d = sum(pnl_d) / n_d
            dentro_sorted = sorted(dentro, key=lambda x: x[0])

            _conteo_wallets = Counter(w for _, _, w, _a in dentro if w)
            concentracion_top1 = (max(_conteo_wallets.values()) / n_d) if (_conteo_wallets and n_d) else None
            # 16-Sep: diversidad por ACTIVO, informativa -- si algún día un
            # solo activo empieza a dominar una celda que hoy es cross-activo,
            # esto lo deja visible en el JSON sin tener que recalcular a mano.
            _conteo_activos = Counter(a for _, _, _w, a in dentro if a)

            clave_celda = f"{bp:.2f}|{bt}"
            historial_semilla = historial_previo.get(clave_str, {}).get(clave_celda, [])
            g_kelly = sum(math.log(1 + F_KELLY * x) for x in pnl_d) / n_d if n_d > 0 else None

            entrada = {
                "n": n_d, "pnl_medio": round(media_d, 4),
                "g_kelly_f10": round(g_kelly, 5) if g_kelly is not None else None,
                "concentracion_top1_wallet": round(concentracion_top1, 4) if concentracion_top1 is not None else None,
                "n_wallets": len(_conteo_wallets), "n_mercados": len(set(ts for ts, _, _w, _a in dentro)),
                "n_activos": len(_conteo_activos), "por_activo": dict(_conteo_activos),
                "shuffle_p": None, "split_half": None, "veredicto": "sin_concluir",
                "historial_crudo": historial_semilla,
            }
            tabla[clave_celda] = entrada

            if n_d >= N_MIN and fuera:
                pnl_f = [pnl for _, pnl in fuera]
                diff, p_valor = shuffle_test(pnl_d, pnl_f, seed_key=f"{clave_str}#{clave_celda}")
                entrada["shuffle_p"] = round(p_valor, 4)
                mid = n_d // 2
                m1, m2 = dentro_sorted[:mid], dentro_sorted[mid:]
                if len(m1) >= 5 and len(m2) >= 5:
                    media_fuera = sum(pnl_f) / len(pnl_f)
                    d1 = sum(pnl for _, pnl, _w, _a in m1) / len(m1) - media_fuera
                    d2 = sum(pnl for _, pnl, _w, _a in m2) / len(m2) - media_fuera
                    entrada["split_half"] = [round(d1, 4), round(d2, 4)]
                    consistente = (d1 < 0 and d2 < 0) or (d1 > 0 and d2 > 0)
                    if consistente:
                        pendientes.append({"clave_str": clave_str, "celda": clave_celda,
                                            "entrada": entrada, "p": p_valor, "diff": diff})

            # 16-Sep (añadido tras verificar en caliente que hacía falta,
            # no "por si acaso"): el shuffle vs "resto del marco" no detecta
            # esta celda -- el "resto" mezcla zonas pésimas (precio<0.70,
            # pnl~-1.0) con zonas decentes, diluye la varianza y el test de
            # medias pierde potencia pese a que el hit-rate de la celda es
            # claramente superior al breakeven de su propio precio (Wilson
            # manual: 82-92% de Wilson90lo vs ~55-65% de breakeven). Vía
            # ABSOLUTA (bootstrap_absoluto, ya usada por el hermano de
            # precio-solo para exactamente este caso, UMBRAL_ABSOLUTO_EUR=
            # 0,10€) -- prueba si la MEDIA de la celda supera 0,10€ por sí
            # sola, sin comparar contra nada heterogéneo.
            if n_d >= N_MIN:
                ci_lo90_abs, ci_hi90_abs, p_valor_abs = bootstrap_absoluto(
                    pnl_d, seed_key=f"abs#{clave_str}#{clave_celda}")
                entrada["p_valor_abs"] = round(p_valor_abs, 4)
                entrada["ci90_absoluto"] = [round(ci_lo90_abs, 4), round(ci_hi90_abs, 4)]
                mid = n_d // 2
                m1, m2 = dentro_sorted[:mid], dentro_sorted[mid:]
                if len(m1) >= 5 and len(m2) >= 5:
                    m1_abs = sum(pnl for _, pnl, _w, _a in m1) / len(m1)
                    m2_abs = sum(pnl for _, pnl, _w, _a in m2) / len(m2)
                    entrada["split_half_absoluto"] = [round(m1_abs, 4), round(m2_abs, 4)]
                    candidatos_abs.append({"clave_str": clave_str, "celda": clave_celda,
                                            "entrada": entrada, "p_valor_abs": p_valor_abs,
                                            "split_half_abs": [m1_abs, m2_abs]})
        resultado[clave_str] = tabla

    # BH-FDR por marco (ya no por activo -- ver docstring de cargar_filas).
    por_grupo = defaultdict(list)
    for idx, p in enumerate(pendientes):
        marco = p["clave_str"].split("#")[1]
        por_grupo[marco].append(idx)

    sobreviven = set()
    for grupo, indices in por_grupo.items():
        p_valores = [pendientes[i]["p"] for i in indices]
        sobreviven |= {indices[j] for j in bh_fdr_signif(p_valores, q=P_MAX)}

    veredictos_nuevos = []
    for idx, p in enumerate(pendientes):
        if idx not in sobreviven:
            continue
        if p["diff"] < 0:
            veredicto_crudo = "malo_confirmado"
        elif p["entrada"]["pnl_medio"] >= 0:
            veredicto_crudo = "bueno_confirmado"
        else:
            continue

        nota_concentracion = ""
        conc = p["entrada"].get("concentracion_top1_wallet")
        if veredicto_crudo == "bueno_confirmado" and conc is not None and conc > CONCENTRACION_TOP1_MAX:
            veredicto_crudo = "sin_concluir"
            nota_concentracion = f" -- degradado, concentración top1={conc*100:.1f}%>{CONCENTRACION_TOP1_MAX*100:.0f}%"

        p["entrada"]["veredicto_crudo_hoy"] = veredicto_crudo
        historial_celda = historial_previo.get(p["clave_str"], {}).get(p["celda"])
        veredicto, p["entrada"]["historial_crudo"] = veredicto_con_tolerancia(
            veredicto_crudo, historial_celda)
        p["entrada"]["veredicto"] = veredicto
        if veredicto == "sin_concluir":
            continue
        marca = "🔴" if veredicto == "malo_confirmado" else "🟢"
        veredictos_nuevos.append(
            f"{marca} {p['clave_str']} celda[{p['celda']}] n={p['entrada']['n']} "
            f"pnl_medio={p['entrada']['pnl_medio']:+.3f} p={p['p']:.4f} {veredicto}{nota_concentracion}"
        )

    # Vía ABSOLUTA -- solo RESCATA celdas que la vía relativa dejó en
    # sin_concluir (nunca pisa un veredicto ya resuelto por la vía
    # relativa, mismo criterio que rescatar_via_absoluta() del hermano de
    # precio-solo). BH-FDR propio, por marco.
    ya_resueltas = {(p["clave_str"], p["celda"]) for i, p in enumerate(pendientes)
                     if i in sobreviven and p["entrada"]["veredicto"] != "sin_concluir"}
    candidatos_abs_pendientes = [c for c in candidatos_abs
                                  if (c["clave_str"], c["celda"]) not in ya_resueltas]

    por_grupo_abs = defaultdict(list)
    for idx, c in enumerate(candidatos_abs_pendientes):
        marco = c["clave_str"].split("#")[1]
        por_grupo_abs[marco].append(idx)

    sobreviven_abs = set()
    for grupo, indices in por_grupo_abs.items():
        p_valores = [candidatos_abs_pendientes[i]["p_valor_abs"] for i in indices]
        sobreviven_abs |= {indices[j] for j in bh_fdr_signif(p_valores, q=P_MAX)}

    for idx, c in enumerate(candidatos_abs_pendientes):
        if idx not in sobreviven_abs:
            continue
        media_abs = c["entrada"]["pnl_medio"]
        if media_abs <= UMBRAL_ABSOLUTO_EUR:
            continue  # p_valor_abs bajo prueba H0:media<=umbral -- exige además que la media SUPERE el umbral
        m1_abs, m2_abs = c["split_half_abs"]
        if not (m1_abs > UMBRAL_ABSOLUTO_EUR and m2_abs > UMBRAL_ABSOLUTO_EUR):
            continue  # split-half absoluto: AMBAS mitades por encima del umbral, no solo la media conjunta
        veredicto_crudo = "bueno_confirmado"
        conc = c["entrada"].get("concentracion_top1_wallet")
        nota_concentracion = ""
        if conc is not None and conc > CONCENTRACION_TOP1_MAX:
            veredicto_crudo = "sin_concluir"
            nota_concentracion = f" -- degradado, concentración top1={conc*100:.1f}%>{CONCENTRACION_TOP1_MAX*100:.0f}%"
        c["entrada"]["veredicto_crudo_hoy"] = veredicto_crudo
        historial_celda = historial_previo.get(c["clave_str"], {}).get(c["celda"])
        veredicto, c["entrada"]["historial_crudo"] = veredicto_con_tolerancia(
            veredicto_crudo, historial_celda)
        c["entrada"]["veredicto"] = veredicto
        c["entrada"]["via"] = "absoluta"
        if veredicto == "sin_concluir":
            continue
        veredictos_nuevos.append(
            f"🟢 {c['clave_str']} celda[{c['celda']}] n={c['entrada']['n']} "
            f"pnl_medio={media_abs:+.3f} p_abs={c['p_valor_abs']:.4f} {veredicto} (vía absoluta){nota_concentracion}"
        )

    OUT.write_text(json.dumps(resultado, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"Guardado en {OUT} ({len(resultado)} claves)")
    if veredictos_nuevos:
        print("\nVeredictos nuevos hoy:")
        for v in veredictos_nuevos:
            print(f"  {v}")
    else:
        print("\nSin cambios de veredicto hoy.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
