#!/usr/bin/env python3
"""
analisis_sports_wallet_mirror_gate_bucket_26ago.py — 26-Ago, petición
explícita Javi: "tenemos que instrumentar lo de sports con los
hallazgos de hoy de LoL". Wallet Mirror#LoL cruzó significancia en
agregado (n=946, pnl+0.166€/tr, p=0.0398, fill 73%) pero CLAUDE.md
pt.17 exige desagregar por micro-bucket de precio ANTES de dar nada por
bueno -- un agregado positivo puede (como ha pasado 5 veces hoy en
cripto) estar diluido o directamente ser negativo en la mayoría de
buckets y positivo solo en uno estrecho.

Mismo patrón que gate_bucket_propio.py (cripto): bucketiza por
(categoria, tipo, bucket_precio 0.05), exige fill-ability real
(ratio_vs_stake_mirror>=5x) desde el principio, rigor Wilson90 +
binomial + split-half. Generaliza a TODAS las categorías de sports, no
solo LoL -- mismo criterio "nunca hardcodear una tupla" ya aplicado
hoy en cripto.

Salida: data/sports/wallet_mirror_gate_bucket.json. Solo lectura, no
coloca ninguna orden -- pero SÍ conecta a dinero real desde 31-Ago
(sports_wallet_mirror_sniper.py, DRY_RUN=False, LoL#SEGUIR[0.45,0.50)
primera promoción real de sports): sports_live_guard.puede_operar_live()
exige veredicto=="bueno_confirmado" de este mismo gate como segundo
guardián fail-closed, además de la whitelist estática
pares_permitidos_live. Este generador dejó de ser puramente shadow.
"""
import csv
import json
import math
import sys
from collections import defaultdict
from math import comb
from pathlib import Path

from gate_confirmacion_historial import cargar_historial_previo, veredicto_con_tolerancia
from analisis_gate_bucket_propio_28jul import (
    UMBRAL_ABSOLUTO_EUR, bootstrap_absoluto, rescatar_via_absoluta,
)

csv.field_size_limit(sys.maxsize)

REPO = Path(__file__).resolve().parent
DRY_RUN = REPO / "data/sports/wallet_mirror_sniper_dry_run.csv"
OUT_PATH = REPO / "data/sports/wallet_mirror_gate_bucket.json"

N_MIN = 40  # 01-Sep: subido de 15->40, mismo fix que WALLET_MIRROR cripto
# (config_live.json::_pares_walletmirror_pausa_nota_2026-09-01 -- buckets
# confirmados con n=15-65 disparaban dinero real y revertian con mas
# datos). Sports ya tiene dinero real desde 31-Ago (WALLET_MIRROR#LoL),
# mismo riesgo exacto -- verificado 01-Sep noche que este generador seguia
# en 15 sin el fix.
F_KELLY = 0.10  # 29-Ago: mismo default que analisis_log_growth.py/gate_bucket_propio.py (P28/CLAUDE.md pt.14)
RATIO_MIN = 5.0
# FEE verificado 26-Ago con condition_ids reales del propio dataset contra gamma-api
# (feeType/feeSchedule): sports usa "sports_fees_v3" rate=0.05 en CS/LoL/Tennis/Dota/
# Valorant/Cricket/UFC/ATP/EPL (9/10 categorías muestreadas) -- NO el 0.07 de cripto,
# que es un supuesto copiado sin verificar (mismo aviso ya dejado en el fichero gemelo
# de weather). Único outlier visto: F1 usa "sports_fees_v2" rate=0.03 (volumen
# despreciable hoy, 1 señal). 0.05 es la mejor aproximación única disponible; no cambia
# qué buckets se confirman (breakeven/hit no dependen de FEE aquí) pero corrige el
# pnl_medio reportado, que con 0.07 estaba sistemáticamente infravalorado.
FEE = 0.05
STAKE = 1.0
Z90 = 1.645
STEP = 0.05


def bucket(p: float) -> str:
    b = round((p // STEP) * STEP, 2)
    return f"{b:.2f}"


def wilson_lo(p: float, n: int, z: float = Z90) -> float:
    if n == 0:
        return 0.0
    denom = 1 + z * z / n
    center = p + z * z / (2 * n)
    adj = z * math.sqrt(max(p * (1 - p) / n, 0) + z * z / (4 * n * n))
    return (center - adj) / denom


def binom_sf(k: int, n: int, p: float) -> float:
    p = min(max(p, 1e-9), 1 - 1e-9)
    return sum(comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(k, n + 1))


def payout_win(precio: float) -> float:
    return STAKE * (1 - precio) / precio - STAKE * FEE * (1 - precio)


def main() -> int:
    historial_previo = cargar_historial_previo(OUT_PATH, anidado_por_bucket=True)
    grupos = defaultdict(list)
    with open(DRY_RUN, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("acierto") not in ("0", "1"):
                continue
            try:
                ratio = float(row["ratio_vs_stake_mirror"])
                ask = float(row["mejor_ask_mirror"])
            except (TypeError, ValueError, KeyError):
                continue
            if ratio < RATIO_MIN:
                continue
            if not (0.01 < ask < 0.99):
                continue
            key = (row["categoria"], row["tipo"], bucket(ask))
            acierto = int(row["acierto"])
            pnl = payout_win(ask) if acierto == 1 else -STAKE
            grupos[key].append((acierto, pnl, ask, row.get("resolved_ts") or row.get("timestamp_utc", "")))

    salida = {}
    n_confirmados_buenos = 0
    n_confirmados_malos = 0
    pvals = []
    g_kelly_raw = {}  # (tupla_str, b) -> g_kelly SIN redondear, para el veto de abajo
    candidatos_abs = []  # vía absoluta (12-Sep), ver UMBRAL_ABSOLUTO_EUR
    for (categoria, tipo, b), items in grupos.items():
        n = len(items)
        tupla_str = f"{categoria}#{tipo}"
        salida.setdefault(tupla_str, {})
        if n < N_MIN:
            entrada = {"n": n, "veredicto": "n_insuficiente"}
            # /code-review 01-Sep (mismo patrón que los 5 ficheros gemelos):
            # si el bucket tenía historial_crudo acumulado y hoy cae por
            # debajo de N_MIN (día flojo, no un veto real), preservarlo en
            # vez de perderlo -- n_insuficiente no es un día MALO.
            hist = historial_previo.get(tupla_str, {}).get(b)
            if hist:
                entrada["historial_crudo"] = hist
            # /code-review 01-Sep (hallazgo real, segunda ronda): la
            # confluencia suave de sports_wallet_mirror_gate_bucket.py
            # necesita pnl_medio para comparar contra el fino incluso con
            # n insuficiente (15<=n<40) -- sin esto, el chequeo quedaba
            # estructuralmente inerte justo en el rango de n que existe
            # para proteger. Mismo criterio que el grid gemelo de cripto
            # (analisis_gate_bucket_propio_28jul.py): reportar pnl_medio
            # para todo bucket presente en `grupos` (n>=1 siempre, ya que
            # solo se crea la clave cuando hay filas -- no es un guardián
            # real, solo documenta la garantía).
            entrada["pnl_medio"] = round(sum(x[1] for x in items) / n, 4)
            salida[tupla_str][b] = entrada
            continue
        hit = sum(x[0] for x in items) / n
        pnl_medio = sum(x[1] for x in items) / n
        # 29-Ago (paridad con el mismo hueco cerrado en WALLET_MIRROR cripto,
        # ver analisis_wallet_mirror_gate_bucket_10ago.py): payout asimétrico
        # (Kelly g(f)) -- pnl_medio lineal positivo puede convivir con
        # crecimiento compuesto negativo (hit-rate alto, pérdidas grandes
        # raras). Misma fórmula g(f)=mean(ln(1+f*x)), reusando x=pnl ya
        # calculado por trade (items[i][1], mismo concepto normalizado que
        # analisis_log_growth.py::_retorno()).
        g_kelly = sum(math.log(1 + F_KELLY * x[1]) for x in items) / n
        g_kelly_raw[(tupla_str, b)] = g_kelly
        ask_medio = sum(x[2] for x in items) / n
        breakeven = ask_medio
        wlo = wilson_lo(hit, n)
        k = sum(x[0] for x in items)
        p_binom = binom_sf(k, n, breakeven)
        items_sorted = sorted(items, key=lambda x: x[3])
        half = n // 2
        m1 = sum(x[1] for x in items_sorted[:half]) / half
        m2 = sum(x[1] for x in items_sorted[half:]) / (n - half)
        pvals.append(((tupla_str, b), p_binom, hit > breakeven))
        entrada = {
            "n": n, "hit": round(hit, 4), "pnl_medio": round(pnl_medio, 4),
            "g_kelly_f10": round(g_kelly, 5),
            "ask_medio": round(ask_medio, 4), "wilson90lo": round(wlo, 4),
            "p_binomial": round(p_binom, 4), "split_half": [round(m1, 4), round(m2, 4)],
        }
        salida[tupla_str][b] = entrada
        # 12-Sep (decisión explícita Javi, ver UMBRAL_ABSOLUTO_EUR en
        # analisis_gate_bucket_propio_28jul.py, extensión pedida por Javi
        # al ver el mismo fix en cripto: "¿tiene sentido hacerlo en
        # sports? lleva mucho tiempo sin operar nada"): vía absoluta,
        # candidatos con n>=N_MIN independientemente del test hit-vs-
        # breakeven de arriba -- ese test YA es "absoluto" en espíritu
        # (hit vs breakeven, no bucket-vs-vecino como en cripto) pero
        # corrige BH-FDR sobre TODA la familia sports junta (m puede ser
        # grande, penaliza mucho), y exige split-half del MISMO signo que
        # el test binomial. La vía absoluta corrige por CATEGORÍA (grupo
        # mucho más pequeño) y con un piso en euros directo, independiente
        # de si esta tupla le gana o no a su breakeven -- rescata
        # candidatos como Dota#SEGUIR[0.45,0.50) o CS#SEGUIR[0.25,0.30)
        # que hoy quedan "sin_concluir" pese a pnl/tr>=0.10€ con n=41-154.
        # m1/m2 ya son medias ABSOLUTAS por mitad (no diff vs resto, a
        # diferencia de cripto) -- reusar directamente como split_half_abs.
        pnl_d = [x[1] for x in items]
        _, _, p_valor_abs = bootstrap_absoluto(pnl_d, seed_key=f"abs#{tupla_str}#{b}")
        entrada["p_valor_abs"] = round(p_valor_abs, 4)
        entrada["split_half_absoluto"] = [round(m1, 4), round(m2, 4)]
        candidatos_abs.append({"clave_str": tupla_str, "bucket": b, "entrada": entrada,
                                "p_valor_abs": p_valor_abs, "split_half_abs": (m1, m2)})

    # BH-FDR sobre la familia completa de buckets con n>=N_MIN
    m = len(pvals)
    if m:
        pvals_sorted = sorted(pvals, key=lambda x: x[1])
        prev_min = 1.0
        bh = {}
        for i in range(len(pvals_sorted) - 1, -1, -1):
            (key, p, mejor) = pvals_sorted[i]
            q = min(p * m / (i + 1), prev_min)
            prev_min = q
            bh[key] = q
        for tupla_str, buckets_dict in salida.items():
            for b, info in buckets_dict.items():
                if "p_binomial" not in info:
                    continue
                key = (tupla_str, b)
                q = bh.get(key, 1.0)
                info["p_bh"] = round(q, 4)
                m1, m2 = info["split_half"]
                mejor = info["hit"] > info["ask_medio"]
                if q < 0.05 and mejor and m1 > 0 and m2 > 0:
                    veredicto_crudo = "bueno_confirmado"
                elif q < 0.05 and not mejor and m1 < 0 and m2 < 0:
                    veredicto_crudo = "malo_confirmado"
                else:
                    veredicto_crudo = "sin_concluir"
                # 29-Ago: veto de payout asimétrico -- degrada bueno_confirmado
                # si g_kelly(f=10%)<=0 pese a pnl_medio lineal positivo. Solo
                # puede degradar, nunca promover (mismo invariante que
                # gate_bucket_propio.py::_veto_fillable() señal #2 y su
                # gemelo en analisis_wallet_mirror_gate_bucket_10ago.py).
                # /code-review 29-Ago: comparar SIEMPRE contra g_kelly_raw
                # (sin redondear) -- info["g_kelly_f10"] redondeado a 5
                # decimales puede aplastar un valor positivo minúsculo a
                # 0.00000 y disparar el veto por error de redondeo, no por
                # payout asimétrico real.
                g_raw = g_kelly_raw.get(key)
                if veredicto_crudo == "bueno_confirmado" and g_raw is not None and g_raw <= 0:
                    veredicto_crudo = "malo_confirmado"

                info["veredicto_crudo_hoy"] = veredicto_crudo
                # 31-Ago: guard de estabilidad (mismo criterio que
                # gate_bucket_propio.py/wallet_mirror cripto) --
                # "malo_confirmado" sigue inmediato (dirección segura, no
                # hace falta esperar), solo "bueno_confirmado" exige
                # consistencia. 01-Sep (petición explícita Javi, "un día de
                # mala racha no puede entorpecer esto"): 2 de los últimos 3
                # días (incluido hoy), no solo el inmediatamente anterior --
                # ver gate_confirmacion_historial.py.
                historial_bucket = historial_previo.get(tupla_str, {}).get(b)
                if veredicto_crudo == "sin_concluir":
                    # sin evidencia hoy (n<N_MIN u otro motivo) -- no consume
                    # ni rompe el historial de días con datos reales.
                    veredicto = "sin_concluir"
                    if historial_bucket:
                        info["historial_crudo"] = historial_bucket
                else:
                    veredicto, info["historial_crudo"] = veredicto_con_tolerancia(
                        veredicto_crudo, historial_bucket)
                info["veredicto"] = veredicto
                if veredicto == "bueno_confirmado":
                    n_confirmados_buenos += 1
                elif veredicto == "malo_confirmado":
                    n_confirmados_malos += 1

    # 12-Sep, vía absoluta (decisión explícita Javi, ver UMBRAL_ABSOLUTO_EUR
    # en analisis_gate_bucket_propio_28jul.py): rescata buckets rentables de
    # sobra (pnl_medio>=0.10€/tr robusto) que el test hit-vs-breakeven+BH-FDR
    # sobre TODA la familia sports dejó en sin_concluir/malo_confirmado --
    # agrupa por CATEGORÍA (mucho más estrecho que "toda la familia junta",
    # menos penalización de multiple-testing). Namespace de historial
    # INDEPENDIENTE (historial_crudo_abs, mismo fix de /code-review 12-Sep
    # aplicado al gemelo cripto -- nunca reusar el ledger de "2 de 3 días"
    # del test hit-vs-breakeven, mezclaría dos tests distintos).
    historial_abs_previo = {}
    try:
        _prev = json.loads(OUT_PATH.read_text(encoding="utf-8"))
        for tupla_str, tabla in _prev.items():
            if isinstance(tabla, dict):
                historial_abs_previo[tupla_str] = {
                    b: v.get("historial_crudo_abs", []) for b, v in tabla.items() if isinstance(v, dict)}
    except Exception:
        pass
    rescatados = rescatar_via_absoluta(
        candidatos_abs, agrupador_fn=lambda tupla_str: tupla_str.split("#")[0])
    for c in rescatados:
        b = c["bucket"]
        veredicto_crudo_abs = "bueno_confirmado"
        g_raw = g_kelly_raw.get((c["clave_str"], b))
        if g_raw is not None and g_raw <= 0:
            veredicto_crudo_abs = "malo_confirmado"  # mismo veto payout asimétrico que la vía normal
        historial_bucket = historial_abs_previo.get(c["clave_str"], {}).get(b)
        veredicto, c["entrada"]["historial_crudo_abs"] = veredicto_con_tolerancia(
            veredicto_crudo_abs, historial_bucket)
        c["entrada"]["veredicto_crudo_hoy_abs"] = veredicto_crudo_abs
        c["entrada"]["via"] = "absoluta"
        if veredicto == "sin_concluir":
            continue  # nunca pisa el veredicto ya decidido por el test hit-vs-breakeven
        # /code-review 12-Sep: veredicto aquí puede ser malo_confirmado (si
        # el veto de payout asimétrico degradó el rescate) -- contar/marcar
        # según el veredicto FINAL, no asumir bueno. Si el bucket ya estaba
        # malo_confirmado por la vía normal y sigue malo aquí, no duplicar
        # el conteo (ya se contó arriba); si venía de sin_concluir, sí suma.
        venia_de_malo = c["entrada"].get("veredicto") == "malo_confirmado"
        c["entrada"]["veredicto"] = veredicto
        if veredicto == "bueno_confirmado":
            n_confirmados_buenos += 1
        elif veredicto == "malo_confirmado" and not venia_de_malo:
            n_confirmados_malos += 1
        marca = "🟢" if veredicto == "bueno_confirmado" else "🔴"
        print(f"  {marca} [vía absoluta] {c['clave_str']} [{b},{float(b)+STEP:.2f}) "
              f"n={c['entrada']['n']} pnl_medio={c['entrada']['pnl_medio']:+.3f} "
              f"p_abs={c['p_valor_abs']:.4f} {veredicto}")

    OUT_PATH.write_text(json.dumps(salida, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Categorías#tipo con datos: {len(salida)}")
    print(f"Tests con n>={N_MIN}: {m}")
    print(f"bueno_confirmado (BH-FDR): {n_confirmados_buenos} | malo_confirmado: {n_confirmados_malos}")
    print(f"Guardado en {OUT_PATH}")

    lol = {k: v for k, v in salida.items() if k.startswith("LoL#")}
    print("\n=== Detalle LoL ===")
    for tupla, buckets_dict in lol.items():
        for b, info in sorted(buckets_dict.items()):
            if info.get("n", 0) >= N_MIN:
                print(f"  {tupla} [{b},{float(b)+STEP:.2f}) n={info['n']} hit={info['hit']:.1%} "
                      f"pnl/tr={info['pnl_medio']:+.3f} p_bh={info.get('p_bh')} -> {info.get('veredicto')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
