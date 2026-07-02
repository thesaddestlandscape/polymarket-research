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

    if not tareas:
        return  # fuera de fase activa — salida silenciosa

    precios = _precios_minuto()
    filas = []
    for t in tareas:
        try:
            evaluar_par(*t, precios, filas)
        except Exception as e:
            _log(f"  [warn] {t[0]}: {type(e).__name__}: {e}")
        time.sleep(0.15)

    if filas:
        out = DIR_SHADOW / f"nested_arb_{ahora.date()}.csv"
        nuevo = not out.exists()
        with open(out, "a", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(filas[0].keys()))
            if nuevo:
                w.writeheader()
            w.writerows(filas)
        n_arb = sum(1 for r in filas if r["coste"] < 1.0)
        _log(f"nested_arb: {len(filas)} mediciones, {n_arb} con coste<1")


if __name__ == "__main__":
    main()
