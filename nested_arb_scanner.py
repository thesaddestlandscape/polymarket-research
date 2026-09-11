"""
nested_arb_scanner.py — Scanner OBSERVACIONAL de arbitraje de contención
entre ventanas anidadas de Polymarket (2026-07-02). NO ejecuta trades.

Mecanismo: el último slot corto (5m/15m) y la ventana que lo contiene
(15m/60m) comparten el MISMO cierre pero tienen aperturas distintas — y
durante la fase ejecutable ambas aperturas ya ocurrieron (klines propios).
Eso impone una relación lógica dura entre los dos precios:

  Si o_inner >= o_outer:  {close > o_inner} ⊆ {close > o_outer}
    → comprar YES_outer + NO_inner paga siempre >= $1
      (y $2 si el cierre cae entre ambas aperturas).
  Si o_inner <= o_outer:  combo espejo NO_outer + YES_inner, misma garantía.

Si el coste de la pareja (asks reales) < $1 → beneficio mínimo garantizado
sin dirección ni modelo. La versión ingenua SIN comprobar el orden de las
aperturas compra la "zona muerta" y pierde (77% de los candidatos del
backtest del 2026-07-02 eran esa trampa) — de ahí que nadie lo explote.

CRÍTICO anti-lookahead: solo se evalúa cuando now >= inicio del slot
interior (su apertura tiene que ser conocida al tradear). Validado sobre
snapshots del 2026-07-02: clusters ejecutables reales en :56-:59 con coste
0.97-0.98.

Corre por cron cada minuto (flock). Fuera de fase activa sale al instante.
Salida: data/shadow/nested_arb_YYYY-MM-DD.csv (todas las mediciones, no
solo oportunidades — la distribución del coste también es dato).
"""
import csv
import json
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

import requests

REPO = Path(__file__).parent
DIR_PRICES = REPO / "data" / "prices"
DIR_SHADOW = REPO / "data" / "shadow"

GAMMA = "https://gamma-api.polymarket.com"
CLOB = "https://clob.polymarket.com"
H = {"User-Agent": "Mozilla/5.0 (compatible; polymarket-research/1.0)"}
TIMEOUT = 10

ACTIVOS = {
    "BTC": ("btc", "bitcoin"),
    "ETH": ("eth", "ethereum"),
    "SOL": ("sol", "solana"),
    "XRP": ("xrp", "xrp"),
}
MARGEN_FIN_S = 25       # no evaluar en los últimos ~25s (sin tiempo de ejecutar)
COSTE_LOG_MAX = 9.9     # registrar TODA medición en fase activa (~140 filas/día);
                        # la distribución completa del coste también es dato

# --- Sim de ejecución (2026-07-05): valida si el arb sobrevive a fills FOK
# reales y si la garantía de contención aguanta contra el outcome OFICIAL
# (el riesgo es que o_inner/o_outer vengan de nuestros precios con tolerancia
# ±3min y discrepen del strike real con gaps pequeños). Criterio de paso a
# live: n>=30 cerradas con garantia_ok~100% y pnl medio ≈ profit_min.
SIM_CSV = DIR_SHADOW / "nested_arb_sim.csv"
SIM_MIN_DEPTH_USD = 10.0   # mismo listón que el análisis del 05-Jul
SIM_CAP_COSTE_USD = 10.0   # coste máximo por oportunidad simulada
# Filtro pre-entrada validado 2026-07-07 (analisis re-medición n=28 cerradas):
# las 4 que ROMPIERON la garantía (−40€, borraron las 23 buenas) tenían gap 3× más
# ancho (0.051% vs 0.017%) y libro ½ ($11.7 vs $21). Ambos observables A LA ENTRADA.
# gap<0.04% & depth>$15 → 100% garantía y +8.48$ en el subconjunto (n=7, aún <30).
# NO gatea la entrada (se sigue midiendo todo); solo TAGUEA para acumular garantía
# forward del subconjunto filtrado. Paso a live: pasa_filtro con n≥30 y garantía~100%.
NESTED_GAP_MAX_PCT = 0.04    # |gap_opens_pct| máximo para el subconjunto de confianza
NESTED_DEPTH_MIN_USD = 15.0  # profundidad mínima del libro ($) para el subconjunto
SIM_CAMPOS = ["ts_entrada", "activo", "nesting", "combo", "coste", "n_shares",
              "coste_total_usd", "ask_leg1", "ask_leg2", "gap_opens_pct",
              "depth_usd", "min_orden_ok", "end_utc", "inner_slug",
              "outer_slug", "status", "ts_cierre", "gano_leg1", "gano_leg2",
              "payout_por_share", "pnl_usd", "garantia_ok", "pasa_filtro",
              "persistio_ciclo_anterior"]

# --- Duración de episodio + sondeo ráfaga (08-Jul, tras leer Cheng/Yang/Zou
# arXiv:2605.00864 — arbitraje NBA en Polymarket vía 75M snapshots de libro).
# Su hallazgo clave: mediana de episodio combinatorio = 16s (17.2% <=4s) con
# un polling de 3.6-5.5s — MÁS RÁPIDO que nuestro cron de 1min. Si el patrón
# se repite aquí, 1min/scan puede estar subcontando episodios reales que
# abren y cierran entre dos sondeos. Dos medidas puramente observacionales,
# NO gatean sim ni live:
#   (a) trackear inicio/fin de cada racha (inner,outer,combo) con coste<1
#       entre sondeos consecutivos -> duración real medida, no asumida.
#   (b) sondeo en ráfaga (varias pasadas internas, no solo 1) SOLO en los
#       últimos UMBRAL_BURST_S de la ventana más ajustada -> igual que su
#       hallazgo de concentración en "los últimos minutos", sin subir el
#       coste el resto del día. flock -n del cron ya evita solapes: si la
#       ráfaga se alarga más de 1min, el siguiente tick simplemente no entra.
DURACIONES_CSV   = DIR_SHADOW / "nested_arb_duraciones.csv"
RACHA_STATE_PATH = DIR_SHADOW / "nested_arb_racha_state.json"
UMBRAL_BURST_S   = 150   # si la tarea más ajustada tiene menos de esto, ráfaga
BURST_ITERACIONES = 4    # pasadas internas en modo ráfaga
BURST_SLEEP_S      = 10  # separación entre pasadas (4×10s ≈ 40s, cabe en el minuto)
DURACIONES_CAMPOS = ["activo", "nesting", "combo", "inicio", "fin",
                     "duracion_s", "coste_min", "depth_max_usd", "n_sondeos"]


def _log(msg):
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}")


def _precios_minuto() -> dict:
    """{asset: {epoch_min: precio}} del fichero de precios de hoy (y ayer por bordes)."""
    out = {}
    hoy = datetime.now(timezone.utc).date()
    for d in (hoy - timedelta(days=1), hoy):
        p = DIR_PRICES / f"{d}.csv"
        if not p.exists():
            continue
        try:
            with open(p, encoding="utf-8") as f:
                for r in csv.DictReader(f):
                    try:
                        ep = int(datetime.fromisoformat(r["timestamp_utc"].replace("Z", "+00:00")).timestamp()) // 60
                        out.setdefault(r["asset"].upper(), {})[ep] = float(r["price_usd"])
                    except Exception:
                        continue
        except Exception:
            continue
    return out


def _precio_en(precios, act, dt, tol_min=3):
    ep = int(dt.timestamp()) // 60
    serie = precios.get(act, {})
    for d in range(tol_min + 1):
        for e in (ep - d, ep + d):
            if e in serie:
                return serie[e]
    return None


def _gamma_market(slug: str) -> dict | None:
    try:
        r = requests.get(f"{GAMMA}/markets", params={"slug": slug}, headers=H, timeout=TIMEOUT)
        data = r.json()
        if isinstance(data, list) and data:
            return data[0]
    except Exception:
        pass
    return None


def _book_top(token_id: str) -> tuple:
    """(mejor_ask, size_ask, mejor_bid, size_bid) del libro CLOB, o Nones."""
    try:
        r = requests.get(f"{CLOB}/book", params={"token_id": token_id}, headers=H, timeout=TIMEOUT)
        b = r.json()
        asks = b.get("asks") or []
        bids = b.get("bids") or []
        # CLOB devuelve niveles ordenados; el mejor ask es el de precio mínimo
        best_ask = min(asks, key=lambda x: float(x["price"])) if asks else None
        best_bid = max(bids, key=lambda x: float(x["price"])) if bids else None
        return (
            float(best_ask["price"]) if best_ask else None,
            float(best_ask["size"]) if best_ask else None,
            float(best_bid["price"]) if best_bid else None,
            float(best_bid["size"]) if best_bid else None,
        )
    except Exception:
        return (None, None, None, None)


def _slug_hourly(nombre_largo: str, end_utc: datetime) -> str:
    """Slug de la ventana horaria etiquetada por su hora de INICIO en ET."""
    ini_et = (end_utc - timedelta(hours=1)).astimezone(ZoneInfo("America/New_York"))
    h12 = ini_et.strftime("%I").lstrip("0")
    ampm = ini_et.strftime("%p").lower()
    mes = ini_et.strftime("%B").lower()
    return f"{nombre_largo}-up-or-down-{mes}-{ini_et.day}-{ini_et.year}-{h12}{ampm}-et"


def _tokens(mkt: dict) -> tuple:
    """(token_yes, token_no) del payload de gamma."""
    try:
        toks = json.loads(mkt.get("clobTokenIds") or "[]")
        if len(toks) == 2:
            return toks[0], toks[1]
    except Exception:
        pass
    return None, None


def evaluar_par(act, inner_slug, outer_slug, end_utc, inner_ini, outer_ini, precios, filas):
    o_in = _precio_en(precios, act, inner_ini)
    o_out = _precio_en(precios, act, outer_ini)
    if o_in is None or o_out is None:
        return

    m_in = _gamma_market(inner_slug)
    m_out = _gamma_market(outer_slug)
    if not m_in or not m_out:
        return
    yes_in, no_in = _tokens(m_in)
    yes_out, no_out = _tokens(m_out)
    if not all((yes_in, no_in, yes_out, no_out)):
        return

    ahora = datetime.now(timezone.utc)
    restante_s = (end_utc - ahora).total_seconds()

    # Combo válido según orden de aperturas (la otra dirección es la trampa)
    if o_in >= o_out:
        combo = "YESout+NOin"
        ask1, sz1, _, _ = _book_top(yes_out)
        ask2, sz2, _, _ = _book_top(no_in)
    else:
        combo = "NOout+YESin"
        ask1, sz1, _, _ = _book_top(no_out)
        ask2, sz2, _, _ = _book_top(yes_in)

    if ask1 is None or ask2 is None:
        return
    coste = round(ask1 + ask2, 4)
    depth_usd = round(min((sz1 or 0) * ask1, (sz2 or 0) * ask2), 2)
    gap_opens_pct = round((o_in / o_out - 1) * 100, 4)

    if coste <= COSTE_LOG_MAX:
        filas.append({
            "timestamp_utc": ahora.isoformat(timespec="seconds"),
            "activo": act,
            "nesting": f"{inner_slug.split('-updown-')[1].split('-')[0]}in{'60m' if 'up-or-down' in outer_slug else '15m'}",
            "combo": combo,
            "coste": coste,
            "profit_min_pct": round((1 - coste) * 100, 2),
            "gap_opens_pct": gap_opens_pct,
            "depth_usd": depth_usd,
            "restante_s": int(restante_s),
            "ask_leg1": ask1, "ask_leg2": ask2,
            "o_inner": o_in, "o_outer": o_out,
            "inner_slug": inner_slug, "outer_slug": outer_slug,
        })
        if coste < 1.0:
            _log(f"  🎯 ARB {act} {combo} coste={coste} (min +{(1-coste)*100:.1f}%, "
                 f"gap={gap_opens_pct:+.2f}%, depth=${depth_usd}, quedan {int(restante_s)}s)")


def _racha_cargar() -> dict:
    if not RACHA_STATE_PATH.exists():
        return {}
    try:
        return json.loads(RACHA_STATE_PATH.read_text())
    except Exception:
        return {}


def _racha_guardar(state: dict):
    RACHA_STATE_PATH.write_text(json.dumps(state))


def _duracion_registrar(row: dict):
    nuevo = not DURACIONES_CSV.exists()
    with open(DURACIONES_CSV, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=DURACIONES_CAMPOS)
        if nuevo:
            w.writeheader()
        w.writerow(row)


def _actualizar_rachas(filas: list, state: dict, ahora: datetime) -> tuple[set, dict]:
    """
    Actualiza el estado de rachas (inner,outer,combo) con coste<1 entre
    sondeos. Cierra (mide duración real y la loguea) las rachas vistas en el
    estado previo que NO aparecen en este sondeo. Devuelve (persistentes,
    nuevo_state): persistentes = claves YA activas en el estado previo (para
    taguear sim_entrar sin gatear nada); nuevo_state = estado a pasar a la
    siguiente pasada/ejecución.
    """
    vistas_ahora = {}
    for f in filas:
        if f["coste"] >= 1.0:
            continue
        key = f"{f['inner_slug']}|{f['outer_slug']}|{f['combo']}"
        vistas_ahora[key] = f

    persistentes = set(state.keys()) & set(vistas_ahora.keys())

    nuevo_state = {}
    for key, f in vistas_ahora.items():
        if key in state:
            prev = state[key]
            nuevo_state[key] = {
                "activo": f["activo"], "nesting": f["nesting"], "combo": f["combo"],
                "inicio": prev["inicio"],
                "coste_min": min(prev["coste_min"], f["coste"]),
                "depth_max_usd": max(prev["depth_max_usd"], f["depth_usd"]),
                "n_sondeos": prev["n_sondeos"] + 1,
            }
        else:
            nuevo_state[key] = {
                "activo": f["activo"], "nesting": f["nesting"], "combo": f["combo"],
                "inicio": ahora.isoformat(timespec="seconds"),
                "coste_min": f["coste"], "depth_max_usd": f["depth_usd"],
                "n_sondeos": 1,
            }

    for key, prev in state.items():
        if key in vistas_ahora:
            continue
        try:
            inicio_dt = datetime.fromisoformat(prev["inicio"])
        except Exception:
            continue
        _duracion_registrar({
            "activo": prev["activo"], "nesting": prev["nesting"], "combo": prev["combo"],
            "inicio": prev["inicio"], "fin": ahora.isoformat(timespec="seconds"),
            "duracion_s": round((ahora - inicio_dt).total_seconds(), 1),
            "coste_min": prev["coste_min"], "depth_max_usd": prev["depth_max_usd"],
            "n_sondeos": prev["n_sondeos"],
        })

    return persistentes, nuevo_state


def _sim_cargar() -> list:
    if not SIM_CSV.exists():
        return []
    with open(SIM_CSV, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _sim_guardar(rows: list):
    with open(SIM_CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=SIM_CAMPOS)
        w.writeheader()
        w.writerows(rows)


def _outcome_yes(m: dict | None) -> bool | None:
    """True/False si el mercado resolvió YES/NO oficialmente, None si aún no."""
    try:
        op = json.loads((m or {}).get("outcomePrices") or "[]")
        if len(op) == 2:
            a, b = float(op[0]), float(op[1])
            if a > 0.99 and b < 0.01:
                return True
            if b > 0.99 and a < 0.01:
                return False
    except Exception:
        pass
    return None


def _sim_resolver(rows: list) -> bool:
    """Cierra sim trades cuya ventana terminó, contra el outcome oficial."""
    ahora = datetime.now(timezone.utc)
    cambiado = False
    for r in rows:
        if r["status"] != "OPEN":
            continue
        try:
            end = datetime.fromisoformat(r["end_utc"])
        except Exception:
            continue
        if ahora < end + timedelta(minutes=2):
            continue
        lados = r["combo"].split("+")          # ["YESout","NOin"] etc.
        ganes = []
        for slug, lado in ((r["outer_slug"], lados[0]),
                           (r["inner_slug"], lados[1])):
            yes_won = _outcome_yes(_gamma_market(slug))
            if yes_won is None:
                ganes = None
                break
            ganes.append(1 if yes_won == lado.startswith("YES") else 0)
            time.sleep(0.15)
        if ganes is None:
            continue  # aún sin resolver oficialmente — reintenta el próximo run
        payout = sum(ganes)
        n, coste = float(r["n_shares"]), float(r["coste"])
        r.update({"gano_leg1": ganes[0], "gano_leg2": ganes[1],
                  "payout_por_share": payout,
                  "pnl_usd": round(n * (payout - coste), 4),
                  "garantia_ok": 1 if payout >= 1 else 0,
                  "status": "CLOSED",
                  "ts_cierre": ahora.isoformat(timespec="seconds")})
        cambiado = True
        _log(f"  sim CLOSED {r['activo']} {r['combo']} payout={payout} "
             f"pnl={r['pnl_usd']}$ garantia={'OK' if payout >= 1 else '❌ ROTA'}")
    return cambiado


def _sim_entrar(filas: list, ends: dict, rows: list, persistentes: set) -> bool:
    """Registra entradas simuladas para oportunidades coste<1 con depth."""
    abiertos = {(r["inner_slug"], r["outer_slug"], r["combo"]) for r in rows}
    cambiado = False
    for f in filas:
        if f["coste"] >= 1.0 or f["depth_usd"] < SIM_MIN_DEPTH_USD:
            continue
        key = (f["inner_slug"], f["outer_slug"], f["combo"])
        if key in abiertos:
            continue
        # FOK conservador contra el top del libro recién leído: capacidad en
        # shares acotada por depth_usd/max(ask) (cota inferior del tamaño de
        # ambos niveles), y por el cap de coste total.
        max_ask = max(f["ask_leg1"], f["ask_leg2"])
        n = round(min(SIM_CAP_COSTE_USD / f["coste"], f["depth_usd"] / max_ask), 2)
        if n <= 0:
            continue
        rows.append({
            "ts_entrada": f["timestamp_utc"], "activo": f["activo"],
            "nesting": f["nesting"], "combo": f["combo"], "coste": f["coste"],
            "n_shares": n, "coste_total_usd": round(n * f["coste"], 4),
            "ask_leg1": f["ask_leg1"], "ask_leg2": f["ask_leg2"],
            "gap_opens_pct": f["gap_opens_pct"], "depth_usd": f["depth_usd"],
            # CLOB exige >=$1 por orden marketable — con asks de céntimos la
            # pata barata puede no llegar; se registra para no sobreestimar
            "min_orden_ok": 1 if (n * f["ask_leg1"] >= 1.0
                                  and n * f["ask_leg2"] >= 1.0) else 0,
            "end_utc": ends[f["inner_slug"]].isoformat(timespec="seconds"),
            "inner_slug": f["inner_slug"], "outer_slug": f["outer_slug"],
            "status": "OPEN", "ts_cierre": "", "gano_leg1": "",
            "gano_leg2": "", "payout_por_share": "", "pnl_usd": "",
            "garantia_ok": "",
            # Subconjunto de confianza (gap estrecho + libro profundo): las rotas
            # de la autopsia 07-Jul tenían gap ancho y libro fino. Tag, no gate.
            "pasa_filtro": 1 if (abs(f["gap_opens_pct"]) < NESTED_GAP_MAX_PCT
                                 and f["depth_usd"] > NESTED_DEPTH_MIN_USD) else 0,
            # 08-Jul (arXiv:2605.00864): ¿esta señal ya estaba activa en el
            # sondeo anterior (~1min antes), o es la primera vez que se ve?
            # No gatea entrada — solo tag para comparar garantia_ok forward
            # entre señales persistentes vs de un solo sondeo (posible
            # artefacto de micro-desincronización entre las 2 patas).
            "persistio_ciclo_anterior": 1 if f"{f['inner_slug']}|{f['outer_slug']}|{f['combo']}" in persistentes else 0,
        })
        abiertos.add(key)
        cambiado = True
        _log(f"  sim OPEN {f['activo']} {f['combo']} coste={f['coste']} "
             f"n={n} (min garantizado +{f['profit_min_pct']}%)")
    return cambiado


def main():
    ahora = datetime.now(timezone.utc)
    tareas = []

    # 15m-in-60m: activo en los minutos :45-:59 de cada hora
    fin_hora = ahora.replace(minute=0, second=0, microsecond=0) + timedelta(hours=1)
    ini_slot15 = fin_hora - timedelta(minutes=15)
    if ahora >= ini_slot15 and (fin_hora - ahora).total_seconds() > MARGEN_FIN_S:
        ep15 = int(ini_slot15.timestamp())
        for act, (corto, largo) in ACTIVOS.items():
            tareas.append((act, f"{corto}-updown-15m-{ep15}", _slug_hourly(largo, fin_hora),
                           fin_hora, ini_slot15, fin_hora - timedelta(hours=1)))

    # 5m-in-15m: activo en los últimos 5 min de cada cuarto de hora
    min_q = (ahora.minute // 15 + 1) * 15
    fin_q = ahora.replace(minute=0, second=0, microsecond=0) + timedelta(minutes=min_q)
    ini_slot5 = fin_q - timedelta(minutes=5)
    if ahora >= ini_slot5 and (fin_q - ahora).total_seconds() > MARGEN_FIN_S:
        ep5, ep15q = int(ini_slot5.timestamp()), int((fin_q - timedelta(minutes=15)).timestamp())
        for act, (corto, _largo) in ACTIVOS.items():
            tareas.append((act, f"{corto}-updown-5m-{ep5}", f"{corto}-updown-15m-{ep15q}",
                           fin_q, ini_slot5, fin_q - timedelta(minutes=15)))

    sim_rows = _sim_cargar()
    sim_dirty = _sim_resolver(sim_rows)
    racha_state = _racha_cargar()

    if not tareas:
        # Fuera de fase activa: ninguna racha puede seguir viva (la ventana
        # cambió) — cerrar cualquier resto y limpiar estado para no arrastrar
        # claves muertas a la próxima fase activa.
        if racha_state:
            _actualizar_rachas([], racha_state, ahora)
            _racha_guardar({})
        if sim_dirty:
            _sim_guardar(sim_rows)
        return  # fuera de fase activa — salida silenciosa

    # Ráfaga (08-Jul, arXiv:2605.00864 Cheng/Yang/Zou): su mediana de episodio
    # combinatorio es 16s con un polling de 3.6-5.5s — más rápido que nuestro
    # cron de 1min. Si la tarea más ajustada tiene menos de UMBRAL_BURST_S,
    # varias pasadas internas en vez de 1 sola, concentrando el sondeo justo
    # donde el paper encuentra la mayoría de episodios reales. flock -n del
    # cron ya evita solapes si la ráfaga se alarga más de 1min.
    restante_tarea = min((t[3] - ahora).total_seconds() for t in tareas)
    n_pasadas = BURST_ITERACIONES if restante_tarea < UMBRAL_BURST_S else 1
    ends = {t[1]: t[3] for t in tareas}

    for pasada in range(n_pasadas):
        ahora_pasada = datetime.now(timezone.utc)
        precios = _precios_minuto()
        filas = []
        for t in tareas:
            try:
                evaluar_par(*t, precios, filas)
            except Exception as e:
                _log(f"  [warn] {t[0]}: {type(e).__name__}: {e}")
            time.sleep(0.15)

        if filas:
            out = DIR_SHADOW / f"nested_arb_{ahora_pasada.date()}.csv"
            nuevo = not out.exists()
            with open(out, "a", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=list(filas[0].keys()))
                if nuevo:
                    w.writeheader()
                w.writerows(filas)
            n_arb = sum(1 for r in filas if r["coste"] < 1.0)
            sufijo = f" [ráfaga {pasada + 1}/{n_pasadas}]" if n_pasadas > 1 else ""
            _log(f"nested_arb: {len(filas)} mediciones, {n_arb} con coste<1{sufijo}")

        persistentes, racha_state = _actualizar_rachas(filas, racha_state, ahora_pasada)
        if _sim_entrar(filas, ends, sim_rows, persistentes):
            sim_dirty = True

        if pasada < n_pasadas - 1:
            time.sleep(BURST_SLEEP_S)

    _racha_guardar(racha_state)
    if sim_dirty:
        _sim_guardar(sim_rows)


if __name__ == "__main__":
    main()
