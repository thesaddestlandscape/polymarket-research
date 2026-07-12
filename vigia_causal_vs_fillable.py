#!/usr/bin/env python3
"""Vigía: automatiza el cruce causal×fill-ability (antes manual, vía
`analisis_causal_fillability_general.py`) para que corra solo y avise.

Mandato de Javi (12-Jul tarde): "hay que conectar el aprendizaje causal a
la realidad de ejecución, ajustar el shadow a live". El caso que lo motivó
(PYBAJO_LONGSHOT, GBM_LATE_15M BUY_YES): shadow decía "zona mala" en los 4
activos, pero SOL — el único con n≥15 tanto en shadow como en el cruce con
ejecución real — resultó ser rentable de verdad. El shadow "de papel" no
modela el veto de profundidad/re-quote que sí aplica `live_trade.py`; el
libro_snapshots.csv con motivo=candidato_evaluacion + ratio_vs_stake≥5x SÍ
lo aplica (mismo umbral que el veto real), así que cruzarlo contra el
resultado real del mercado (`results.csv`) es la mejor aproximación barata
a "qué habría pasado si esto fuera ejecutable" — sin esperar fills reales
uno a uno.

Regla de n por capa (ver memoria feedback_n_por_capa_y_activo): cada corte
activo×dirección necesita n≥15 EN LA CAPA FILLABLE (no solo en shadow) para
contar como evaluado. Se persiste todo en
data/shadow/causal_fillability_real.json (histórico de la última corrida,
sobrescribe) y se avisa por Telegram (con latch, sin repetir) cuando un
patron_ganador vigente muestra signo CONTRARIO entre shadow e ejecutable
con n≥15 en ambas capas — la misma señal que habría cazado el caso SOL
automáticamente en vez de a mano.

12-Jul (petición Javi: "esta es la lógica que hay que seguir en todo el
modelo"): añadido el espejo — también cruza `filtros_causales` (las
reglas que SALTAN una operación). Si la zona que shadow marca "mala" no
rinde peor de verdad en el subconjunto ejecutable, el filtro puede estar
descartando señal rentable en vez de protegiendo — mismo n≥15 por capa.

Solo lectura sobre resultados/config; no toca pares_permitidos_live ni
ninguna decisión de trading. Pensado para cron cada ~30-60min.
"""
import csv
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

RESULTS = REPO / "data/shadow/results.csv"
LIBRO = REPO / "data/live/libro_snapshots.csv"
TRADES = REPO / "data/live/trades.csv"
CONFIG_LIVE = REPO / "data/live/config_live.json"
STRATEGY_PARAMS = REPO / "data/shadow/strategy_params.json"
OUT = REPO / "data/shadow/causal_fillability_real.json"
LATCH = REPO / "data/shadow/vigia_causal_fillable_latch.json"
RATIO_MIN = 5.0
N_MIN_CAPA = 15  # regla n-por-capa: cada corte necesita esto en CADA capa


def cargar_results_idx(strategy):
    idx = {}
    with open(RESULTS, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["strategy"] != strategy:
                continue
            try:
                feats = json.loads(r.get("features") or "{}")
            except Exception:
                feats = {}
            idx[(r["market_id"], r["decision"])] = {
                "pnl_neto": r.get("pnl_neto"), "acierto": r.get("acierto"), "feats": feats,
            }
    return idx


def estrategias_con_candidatos() -> list:
    """Deriva la lista de estrategias a vigilar desde libro_snapshots.csv en
    vez de hardcodear — así cubre automáticamente nuevas altas en
    candidatos_evaluacion_live (ej. WEEKLY_PRICE, ESPACIO_ATR#XRP/SOL,
    TARDIO#BTC/ETH/SOL añadidas 12-Jul tarde)."""
    vistas = set()
    with open(LIBRO, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r.get("motivo") == "candidato_evaluacion" and r.get("strategy"):
                vistas.add(r["strategy"])
    return sorted(vistas)


def cargar_fillable(strategy, idx):
    fillable = []
    with open(LIBRO, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r.get("motivo") != "candidato_evaluacion" or r["strategy"] != strategy:
                continue
            try:
                ratio = float(r.get("ratio_vs_stake") or 0)
            except ValueError:
                ratio = 0
            if ratio < RATIO_MIN:
                continue
            info = idx.get((r["market_id"], r["direction"]))
            if not info or info["pnl_neto"] in (None, ""):
                continue
            activo = (r.get("subtype") or "").split("#", 1)[0]
            fillable.append((r["direction"], activo, info))
    return fillable


def cargar_ejecutado_real(strategy, idx):
    """Igual que cargar_fillable pero para tuplas YA live: en vez de filtrar
    por ratio_vs_stake sobre snapshots candidato_evaluacion, usa trades.csv
    directamente (ya son ejecuciones reales, no hace falta el proxy de
    profundidad). Excluye maker_pilot (modo de ejecución distinto, mismo
    criterio que vigia_degradacion_live.py) y ERROR/OPEN (solo CLOSED)."""
    ejecutado = []
    if not TRADES.exists():
        return ejecutado
    with open(TRADES, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r.get("strategy") != strategy or r.get("status") != "CLOSED":
                continue
            if "maker_pilot=1" in (r.get("notas") or ""):
                continue
            direccion = r.get("direction")
            activo = (r.get("subtype") or "").split("#", 1)[0]
            info = idx.get((r.get("market_id"), direccion))
            if not info or info["pnl_neto"] in (None, ""):
                continue
            ejecutado.append((direccion, activo, info))
    return ejecutado


def _tuplas_live() -> set:
    """Estrategias con al menos una tupla en pares_permitidos_live — para
    estas se cruza contra trades.csv real, no solo contra el proxy de
    profundidad de candidatos_evaluacion_live."""
    try:
        cfg = json.loads(CONFIG_LIVE.read_text(encoding="utf-8"))
        return {p.split("#")[0] for p in cfg.get("pares_permitidos_live", []) if p}
    except Exception:
        return set()


def _eval(feats, feature, condicion, umbral):
    v = feats.get(feature)
    if v is None:
        return None
    try:
        v = float(v)
    except (TypeError, ValueError):
        return None
    if condicion == "gt": return v > umbral
    if condicion == "lt": return v < umbral
    if condicion == "abs_gt": return abs(v) > umbral
    if condicion == "abs_lt": return abs(v) < umbral
    return None


def _clave_aplica_a_activo(clave, strategy, activo):
    """Evita cruzar un patrón descubierto para UN activo contra el fillable
    de OTRO (bug encontrado 12-Jul en analisis_causal_fillability_general.py,
    del que este vigía parte: probaba p.ej. FAVORITO_CONFIRMADO#ETH#15min
    contra el subconjunto fillable de BTC). Solo aplica si la clave es la
    estrategia entera (patrón base, válido para cualquier activo) o si el
    activo aparece como segmento exacto de la clave."""
    if clave == strategy:
        return True
    return activo in clave.split("#")


def _particiona(subset, feature, condicion, umbral):
    """Divide subset en (malo, bueno) según el filtro — a diferencia de
    `_eval` solo, excluye explícitamente filas sin la feature de AMBOS
    lados (None no cuenta ni como malo ni como bueno)."""
    malo, bueno = [], []
    for row in subset:
        v = _eval(row[-1]["feats"], feature, condicion, umbral)
        if v is True:
            malo.append(row)
        elif v is False:
            bueno.append(row)
    return malo, bueno


def stats(rows):
    n = len(rows)
    if n == 0:
        return None
    pnl = sum(float(row[-1]["pnl_neto"]) for row in rows)
    hit = sum(int(row[-1]["acierto"]) for row in rows) / n
    return {"n": n, "hit_pct": round(hit * 100, 1), "pnl_trade": round(pnl / n, 4)}


def _evaluar_estrategia(strategy, fuente_rows, est, latch, avisos, fuente_label):
    """Núcleo compartido: dado el conjunto de filas ya restringidas a lo
    ejecutable (candidato_evaluacion+ratio>=5x, o trades.csv real), calcula
    fillable_total, por activo×dirección, y cruza cada patron_ganador
    vigente aplicando la regla n-por-capa. `fuente_label` distingue en el
    JSON persistido y en los avisos si viene del proxy de profundidad
    (candidatos) o de ejecución real (live)."""
    base = stats(fuente_rows)
    entry = {"fuente": fuente_label, "fillable_total": base, "activos": {}}
    if not base or base["n"] < N_MIN_CAPA:
        return entry

    patrones = []
    filtros = []
    for clave, v in est.items():
        if clave != strategy and not clave.startswith(f"{strategy}#"):
            continue
        for p in v.get("patrones_ganadores", []) or []:
            patrones.append((clave, p))
        for f in v.get("filtros_causales", []) or []:
            filtros.append((clave, f))

    activos = sorted({a for _, a, _ in fuente_rows})
    for activo in activos:
        for direccion in ("BUY_YES", "BUY_NO"):
            subset = [(d, a, x) for d, a, x in fuente_rows if d == direccion and a == activo]
            sb = stats(subset)
            if not sb or sb["n"] < N_MIN_CAPA:
                continue  # regla n-por-capa: sin n suficiente en esta capa, no se evalúa este corte
            clave_activo = f"{activo}#{direccion}"
            entry["activos"][clave_activo] = {"fillable": sb, "patrones": []}

            for clave, p in patrones:
                if p.get("direccion") != direccion:
                    continue
                if not _clave_aplica_a_activo(clave, strategy, activo):
                    continue
                filtrado = [(d, a, x) for d, a, x in subset
                            if _eval(x["feats"], p["feature"], p["condicion"], p["umbral"])]
                sf = stats(filtrado)
                if not sf or sf["n"] < N_MIN_CAPA:
                    continue  # n-por-capa también en el subconjunto filtrado por el patrón
                uplift_shadow = p["ic_patron"] - p["ic_base"]
                uplift_fillable = sf["pnl_trade"] - sb["pnl_trade"]
                contrario = (uplift_shadow > 0) != (uplift_fillable > 0)
                reg = {
                    "clave": clave, "feature": p["feature"], "condicion": p["condicion"],
                    "umbral": p["umbral"], "ic_patron_shadow": p["ic_patron"],
                    "ic_base_shadow": p["ic_base"], "n_fillable_filtrado": sf["n"],
                    "pnl_trade_fillable_filtrado": sf["pnl_trade"],
                    "pnl_trade_fillable_base": sb["pnl_trade"], "contrario": contrario,
                }
                entry["activos"][clave_activo]["patrones"].append(reg)

                latch_key = f"{fuente_label}#{clave}#{clave_activo}#{p['feature']}{p['condicion']}{p['umbral']}"
                if contrario:
                    if not latch.get(latch_key):
                        etiqueta = "🔴 LIVE" if fuente_label == "live_real" else "candidata"
                        avisos.append(
                            f"[{etiqueta}] {clave} {clave_activo} {p['feature']}{p['condicion']}{p['umbral']}: "
                            f"shadow uplift={uplift_shadow:+.3f} (n_patron={p['n_patron']}) pero "
                            f"{fuente_label} uplift={uplift_fillable:+.3f}€/trade (n={sf['n']}) — signo CONTRARIO"
                        )
                        latch[latch_key] = True
                else:
                    latch[latch_key] = False

            # Espejo: filtros_causales — ¿la zona que shadow marca "mala" (skip)
            # de verdad rinde peor en ejecución real, o estamos saltando
            # oportunidades rentables? A diferencia del patrón (donde shadow
            # siempre dice "malo" por construcción, ic_malo<0), aquí se compara
            # directamente malo vs bueno DENTRO de lo ejecutable — no hace
            # falta comparar signos de shadow.
            entry["activos"][clave_activo]["filtros"] = []
            for clave, f in filtros:
                if f.get("direccion") != direccion:
                    continue
                if not _clave_aplica_a_activo(clave, strategy, activo):
                    continue
                malo, bueno = _particiona(subset, f["feature"], f["condicion"], f["umbral"])
                sm, sg = stats(malo), stats(bueno)
                if not sm or sm["n"] < N_MIN_CAPA or not sg or sg["n"] < N_MIN_CAPA:
                    continue  # n-por-capa en AMBOS lados de la partición
                injustificado = sm["pnl_trade"] >= sg["pnl_trade"]
                reg_f = {
                    "clave": clave, "feature": f["feature"], "condicion": f["condicion"],
                    "umbral": f["umbral"], "ic_malo_shadow": f["ic_malo"],
                    "n_malo_fillable": sm["n"], "pnl_trade_malo_fillable": sm["pnl_trade"],
                    "n_bueno_fillable": sg["n"], "pnl_trade_bueno_fillable": sg["pnl_trade"],
                    "injustificado": injustificado,
                }
                entry["activos"][clave_activo]["filtros"].append(reg_f)

                latch_key = f"FILTRO#{fuente_label}#{clave}#{clave_activo}#{f['feature']}{f['condicion']}{f['umbral']}"
                if injustificado:
                    if not latch.get(latch_key):
                        etiqueta = "🔴 LIVE" if fuente_label == "live_real" else "candidata"
                        avisos.append(
                            f"[{etiqueta}][FILTRO] {clave} {clave_activo} {f['feature']}{f['condicion']}{f['umbral']}: "
                            f"shadow ic_malo={f['ic_malo']:+.3f} pero en ejecutable la zona 'mala' "
                            f"(n={sm['n']}) rinde {sm['pnl_trade']:+.4f}€/trade vs {sg['pnl_trade']:+.4f}€/trade "
                            f"de la zona 'buena' (n={sg['n']}) — el filtro puede estar saltando señal rentable"
                        )
                        latch[latch_key] = True
                else:
                    latch[latch_key] = False

    return entry


def main() -> int:
    try:
        params = json.loads(STRATEGY_PARAMS.read_text())
    except Exception as e:
        print(f"[vigia_causal_fillable] ERROR leyendo strategy_params: {e}")
        return 1
    est = params.get("estrategias", params)

    try:
        latch = json.loads(LATCH.read_text()) if LATCH.exists() else {}
    except Exception:
        latch = {}

    resultado = {"fecha": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                 "n_min_capa": N_MIN_CAPA, "ratio_min": RATIO_MIN, "estrategias": {}}
    avisos = []

    # Cada estrategia puede tener dos fuentes independientes (una tupla puede
    # estar en candidatos_evaluacion_live para una dirección y en
    # pares_permitidos_live para otra, ej. GBM_LATE_15M: BUY_NO candidata,
    # BUY_YES SOL/ETH live) — siempre se anidan por separado, nunca se mezclan.
    todas = set(estrategias_con_candidatos()) | _tuplas_live()
    for strategy in sorted(todas):
        resultado["estrategias"][strategy] = {}
        idx = cargar_results_idx(strategy)

        if strategy in estrategias_con_candidatos():
            fillable = cargar_fillable(strategy, idx)
            resultado["estrategias"][strategy]["candidato_proxy"] = _evaluar_estrategia(
                strategy, fillable, est, latch, avisos, "candidato_proxy")

        if strategy in _tuplas_live():
            ejecutado = cargar_ejecutado_real(strategy, idx)
            resultado["estrategias"][strategy]["live_real"] = _evaluar_estrategia(
                strategy, ejecutado, est, latch, avisos, "live_real")

    OUT.write_text(json.dumps(resultado, indent=2, ensure_ascii=False), encoding="utf-8")
    LATCH.write_text(json.dumps(latch, indent=1, ensure_ascii=False), encoding="utf-8")

    if avisos:
        try:
            from shadow_digest import enviar_telegram
            TOPE = 15  # Telegram tiene límite de 4096 chars; con muchos avisos, resumir
            cuerpo = avisos[:TOPE]
            resto = f"\n  ... y {len(avisos) - TOPE} más (ver {OUT.name})" if len(avisos) > TOPE else ""
            msg = ("⚠️ VIGÍA causal×fillable: patrón shadow contradicho por ejecución real\n"
                   + "\n".join(f"  {a}" for a in cuerpo) + resto
                   + "\nMismo mecanismo que el caso SOL/PYBAJO_LONGSHOT (12-Jul): shadow no "
                     "modela el veto de profundidad. Revisar antes de fiarse del boost de Kelly.")
            ok = enviar_telegram(msg)
            print(f"[vigia_causal_fillable] {len(avisos)} aviso(s), telegram={ok}")
        except Exception as e:
            print(f"[vigia_causal_fillable] no se pudo notificar Telegram: {e}")
    else:
        print("[vigia_causal_fillable] sin contradicciones nuevas")

    print(f"[vigia_causal_fillable] {len(todas)} estrategias evaluadas, guardado en {OUT}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"[vigia_causal_fillable] ERROR {type(e).__name__}: {e}")
        sys.exit(1)
