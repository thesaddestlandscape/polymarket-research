"""
cross_platform_arb.py — Scanner de arbitraje cross-platform (SOLO OBSERVACIÓN).

Detecta mercados semánticamente equivalentes entre Polymarket y otras plataformas
(Kalshi, Limitless, Manifold) y calcula el gap de precio potencial.

NO ejecuta trades. Output: data/shadow/cross_arb_YYYY-MM-DD.csv

Basado en: "Semantic Non-Fungibility and Violations of the Law of One Price
in Prediction Markets" (arXiv 2601.01706)

Activación para trading real: ≥500€ bankroll + validación resolución en ≥20 eventos.
"""
import csv
import datetime as dt
import re
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

# ---------------------------------------------------------------------------
# Configuración
# ---------------------------------------------------------------------------
DIR_SHADOW  = Path("data/shadow")
DIR_MARKETS = Path("data/markets")
DIR_SHADOW.mkdir(parents=True, exist_ok=True)

TIMEOUT      = 10     # segundos por request
MIN_LIQ_POLY = 50     # liquidez mínima USD en Polymarket
MIN_GAP_PCT  = 2.0    # gap mínimo para loguear (%)
WINDOW_DAYS  = 14     # solo mercados que vencen en los próximos 14 días

ACTIVOS = ["BTC", "ETH", "SOL", "BNB", "XRP"]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; polymarket-research-bot/1.0)",
    "Accept": "application/json",
}

_MESES = {
    "JAN": 1, "FEB": 2, "MAR": 3, "APR": 4, "MAY": 5, "JUN": 6,
    "JUL": 7, "AUG": 8, "SEP": 9, "OCT": 10, "NOV": 11, "DEC": 12,
}


# ---------------------------------------------------------------------------
# Helpers semánticos
# ---------------------------------------------------------------------------

_RE_ACTIVO = re.compile(r"\b(BTC|ETH|SOL|BNB|XRP|BITCOIN|ETHEREUM|SOLANA)\b", re.I)
_RE_PRECIO = re.compile(r"\$?([\d,]+(?:\.\d+)?)k?", re.I)
_ALIAS     = {"BITCOIN": "BTC", "ETHEREUM": "ETH", "SOLANA": "SOL"}


def _activo_texto(texto: str) -> str | None:
    m = _RE_ACTIVO.search(texto)
    if not m:
        return None
    return _ALIAS.get(m.group(1).upper(), m.group(1).upper())


def _precio_umbral(texto: str) -> float | None:
    """Extrae el umbral de precio más grande del título (ignora porcentajes)."""
    texto_limpio = texto.replace(",", "")
    nums = []
    for m in _RE_PRECIO.finditer(texto_limpio):
        try:
            v = float(m.group(1))
            # 'k' suffix
            if "k" in texto_limpio[m.start():m.end()].lower():
                v *= 1000
            if v > 100:
                nums.append(v)
        except ValueError:
            pass
    return max(nums) if nums else None


def _es_arriba(texto: str) -> bool | None:
    t = texto.lower()
    if any(w in t for w in ["above", "higher", "exceed", "over", " up ", "≥", ">="]):
        return True
    if any(w in t for w in ["below", "lower", "under", " down ", "≤", "<="]):
        return False
    return None


def _fecha_str(iso: str) -> str:
    return iso[:10] if iso else ""


def _kalshi_parse_ticker(ticker: str) -> dict:
    """
    Extrae semántica del ticker Kalshi.
    Formato: KXBTC-26JUL0200-T68299.99
      - KXBTC     → BTC
      - 26JUL0200 → 2026-07-02 (YY + MON + DD + HH ignorado)
      - T68299.99 → above $68299.99   (T = threshold above)
      - B68750    → below $68750      (B = below)
    """
    out = {"activo": None, "umbral": None, "direccion": None, "fecha": None}
    parts = ticker.split("-")
    if len(parts) < 3:
        return out

    # Activo del prefix
    series = parts[0]
    for a in ACTIVOS:
        if a in series.upper():
            out["activo"] = a
            break

    # Fecha de parts[1]
    date_p = parts[1]
    for mon, num in _MESES.items():
        if mon in date_p:
            idx = date_p.index(mon)
            try:
                year = 2000 + int(date_p[:idx])
                day  = int(date_p[idx + 3: idx + 5])
                out["fecha"] = f"{year:04d}-{num:02d}-{day:02d}"
            except (ValueError, IndexError):
                pass
            break

    # Dirección y umbral de parts[2+]
    tb = "-".join(parts[2:])
    if tb.startswith("T"):
        out["direccion"] = True
        try:
            out["umbral"] = float(tb[1:].replace(",", ""))
        except ValueError:
            pass
    elif tb.startswith("B"):
        out["direccion"] = False
        try:
            out["umbral"] = float(tb[1:].replace(",", ""))
        except ValueError:
            pass

    return out


def semantica_poly(question: str, end_date: str) -> dict:
    return {
        "activo":    _activo_texto(question),
        "umbral":    _precio_umbral(question),
        "direccion": _es_arriba(question),
        "fecha":     _fecha_str(end_date),
    }


def semantica_kalshi(ticker: str, title: str, close_time: str) -> dict:
    s = _kalshi_parse_ticker(ticker)
    # Si el ticker no tiene activo, intentar título
    if not s["activo"]:
        s["activo"] = _activo_texto(title)
    # Si el ticker no tiene fecha, usar close_time
    if not s["fecha"]:
        s["fecha"] = _fecha_str(close_time)
    return s


def similitud(a: dict, b: dict) -> float:
    """Score 0-1 de equivalencia semántica."""
    if not a["activo"] or not b["activo"]:
        return 0.0
    if a["activo"] != b["activo"]:
        return 0.0
    score = 0.4  # mismo activo

    # Dirección obligatoria: ambas deben estar definidas y coincidir
    if a["direccion"] is None or b["direccion"] is None:
        return 0.0   # pregunta sin dirección clara → no comparable
    if a["direccion"] != b["direccion"]:
        return 0.0   # direcciones opuestas → preguntas distintas
    score += 0.2

    # Umbral: si alguno lo tiene, ambos deben tenerlo y coincidir (±2%)
    if a["umbral"] or b["umbral"]:
        if not (a["umbral"] and b["umbral"]):
            return 0.0  # uno tiene umbral y el otro no → preguntas distintas
        ratio = min(a["umbral"], b["umbral"]) / max(a["umbral"], b["umbral"])
        if ratio < 0.98:
            return 0.0  # umbral diferente → preguntas distintas
        if ratio >= 0.995:
            score += 0.3
        else:  # 0.98 ≤ ratio < 0.995
            score += 0.1

    if a["fecha"] and b["fecha"]:
        if a["fecha"] == b["fecha"]:
            score += 0.1
        elif abs(int(a["fecha"].replace("-", "")) - int(b["fecha"].replace("-", ""))) <= 1:
            score += 0.05

    return round(score, 3)


# ---------------------------------------------------------------------------
# Fuente 1: Polymarket (snapshot local más reciente)
# ---------------------------------------------------------------------------

def cargar_polymarket() -> list[dict]:
    import glob
    archivos = sorted(glob.glob(str(DIR_MARKETS / "*.csv")))
    if not archivos:
        return []

    now       = datetime.now(timezone.utc)
    date_lo   = now.date()
    date_hi   = (now + dt.timedelta(days=WINDOW_DAYS)).date()
    mercados  = []

    with open(archivos[-1], encoding="utf-8") as f:
        for row in csv.DictReader(f):
            q = row.get("question", "")
            activo = _activo_texto(q)
            if activo not in ACTIVOS:
                continue

            # Solo mercados activos en la ventana de 14 días
            end_str = row.get("end_date", "")[:10]
            try:
                end_d = dt.date.fromisoformat(end_str)
                if end_d < date_lo or end_d > date_hi:
                    continue
            except ValueError:
                continue

            try:
                py  = float(row.get("price_yes") or 0)
                liq = float(row.get("liquidity") or 0)
            except (ValueError, TypeError):
                continue

            # Filtros de calidad
            if py < 0.03 or py > 0.97:  # ya casi resuelto
                continue
            if liq < MIN_LIQ_POLY:
                continue
            umbral = _precio_umbral(q)
            if not umbral:              # solo mercados con precio umbral
                continue

            sem = semantica_poly(q, row.get("end_date", ""))
            mercados.append({
                "plataforma": "Polymarket",
                "market_id":  row.get("market_id", ""),
                "titulo":     q,
                "price_yes":  round(py, 4),
                "price_no":   round(1 - py, 4),
                "liquidez":   liq,
                "close":      end_str,
                "url":        f"https://polymarket.com/event/{row.get('market_id','')}",
                "sem":        sem,
            })

    return mercados


# ---------------------------------------------------------------------------
# Fuente 2: Kalshi
# ---------------------------------------------------------------------------

_KALSHI_SERIES = ["KXBTC", "KXETH", "KXBTCD", "KXETHD", "KXSOL"]


def cargar_kalshi() -> list[dict]:
    mercados = []
    now_utc  = datetime.now(timezone.utc)
    date_hi  = (now_utc + dt.timedelta(days=WINDOW_DAYS)).date()

    for series in _KALSHI_SERIES:
        try:
            cursor  = None
            paginas = 0
            while paginas < 5:
                paginas += 1
                params = {"series_ticker": series, "status": "open", "limit": 200}
                if cursor:
                    params["cursor"] = cursor
                r = requests.get(
                    "https://api.elections.kalshi.com/trade-api/v2/markets",
                    params=params, headers=HEADERS, timeout=TIMEOUT
                )
                if not r.ok:
                    break
                d     = r.json()
                batch = d.get("markets", [])
                for m in batch:
                    ticker = m.get("ticker", "")
                    sem    = semantica_kalshi(ticker, m.get("title", ""), m.get("close_time", ""))
                    if sem["activo"] not in ACTIVOS:
                        continue
                    # Filtro fecha
                    if sem["fecha"]:
                        try:
                            fd = dt.date.fromisoformat(sem["fecha"])
                            if fd < now_utc.date() or fd > date_hi:
                                continue
                        except ValueError:
                            pass

                    try:
                        yes_bid = float(m.get("yes_bid_dollars") or 0)
                        yes_ask = float(m.get("yes_ask_dollars") or 0)
                    except (ValueError, TypeError):
                        continue

                    # Solo mercados con precio significativo (no dead markets)
                    if yes_ask <= 0.02 or yes_ask >= 0.98:
                        continue

                    price_yes = round((yes_bid + yes_ask) / 2, 4)
                    if price_yes < 0.03 or price_yes > 0.97:
                        continue

                    liq = float(m.get("liquidity_dollars") or 0)
                    mercados.append({
                        "plataforma": "Kalshi",
                        "market_id":  ticker,
                        "titulo":     m.get("title", ""),
                        "price_yes":  price_yes,
                        "price_no":   round(1 - price_yes, 4),
                        "liquidez":   liq,
                        "close":      sem["fecha"],
                        "url":        f"https://kalshi.com/markets/{ticker}",
                        "sem":        sem,
                    })
                cursor = d.get("cursor")
                if not cursor or len(batch) < 200:
                    break
        except Exception as e:
            print(f"  [Kalshi/{series}] error: {e}")

    return mercados


# ---------------------------------------------------------------------------
# Fuente 3: Limitless Exchange
# ---------------------------------------------------------------------------

def cargar_limitless() -> list[dict]:
    mercados = []
    try:
        # /markets/active puede dar timeout; usamos 15s
        r = requests.get(
            "https://api.limitless.exchange/markets/active",
            params={"limit": 100, "page": 1},
            headers=HEADERS, timeout=15
        )
        if not r.ok:
            return []
        d = r.json()
        batch = d.get("data", []) if isinstance(d, dict) else (d if isinstance(d, list) else [])
        for m in batch:
            titulo = m.get("title", "") or m.get("question", "")
            activo = _activo_texto(titulo)
            if activo not in ACTIVOS:
                continue

            # Estructura de precios AMM
            prices = m.get("prices") or m.get("outcomeTokenPrices") or []
            if isinstance(prices, list) and len(prices) >= 1:
                try:
                    price_yes = float(prices[0])
                except (ValueError, TypeError):
                    continue
            elif isinstance(prices, dict):
                pv = prices.get("Yes") or prices.get("YES") or prices.get("1")
                price_yes = float(pv) if pv else 0
            else:
                continue

            if price_yes < 0.03 or price_yes > 0.97:
                continue

            umbral = _precio_umbral(titulo)
            if not umbral:
                continue

            liq = float(m.get("liquidityFormatted") or m.get("liquidity") or 0)
            deadline = m.get("deadline") or m.get("expirationTime") or ""
            sem = {
                "activo":    activo,
                "umbral":    umbral,
                "direccion": _es_arriba(titulo),
                "fecha":     _fecha_str(deadline),
            }
            mercados.append({
                "plataforma": "Limitless",
                "market_id":  str(m.get("id") or m.get("conditionId", "")),
                "titulo":     titulo,
                "price_yes":  round(price_yes, 4),
                "price_no":   round(1 - price_yes, 4),
                "liquidez":   liq,
                "close":      sem["fecha"],
                "url":        f"https://limitless.exchange/markets/{m.get('slug','')}",
                "sem":        sem,
            })
    except requests.exceptions.Timeout:
        print("  [Limitless] timeout")
    except Exception as e:
        print(f"  [Limitless] error: {e}")
    return mercados


# ---------------------------------------------------------------------------
# Fuente 4: Manifold Markets
# ---------------------------------------------------------------------------

def cargar_manifold() -> list[dict]:
    mercados = []
    try:
        r = requests.get(
            "https://api.manifold.markets/v0/markets",
            params={"limit": 500, "sort": "liquidity", "isResolved": "false"},
            headers=HEADERS, timeout=TIMEOUT
        )
        if not r.ok:
            return []
        for m in r.json():
            if m.get("outcomeType") != "BINARY":
                continue
            titulo = m.get("question", "")
            activo = _activo_texto(titulo)
            if activo not in ACTIVOS:
                continue
            umbral = _precio_umbral(titulo)
            if not umbral:
                continue
            prob = m.get("probability")
            if not prob:
                continue
            py = float(prob)
            if py < 0.03 or py > 0.97:
                continue
            liq = float(m.get("totalLiquidity") or 0)
            if liq < 50:
                continue
            close_ts = m.get("closeTime")
            close_iso = (
                datetime.fromtimestamp(close_ts / 1000, tz=timezone.utc).isoformat()
                if close_ts else ""
            )
            sem = {
                "activo":    activo,
                "umbral":    umbral,
                "direccion": _es_arriba(titulo),
                "fecha":     _fecha_str(close_iso),
            }
            mercados.append({
                "plataforma": "Manifold",
                "market_id":  m.get("id", ""),
                "titulo":     titulo,
                "price_yes":  round(py, 4),
                "price_no":   round(1 - py, 4),
                "liquidez":   liq,
                "close":      sem["fecha"],
                "url":        m.get("url", ""),
                "sem":        sem,
            })
    except Exception as e:
        print(f"  [Manifold] error: {e}")
    return mercados


# ---------------------------------------------------------------------------
# Motor de matching (indexado por activo+fecha para evitar O(N×M))
# ---------------------------------------------------------------------------

def _indexar(mercados: list[dict]) -> dict:
    """Crea índice por (activo, fecha) → lista de mercados."""
    idx: dict[tuple, list] = {}
    for m in mercados:
        k = (m["sem"]["activo"], m["sem"]["fecha"])
        idx.setdefault(k, []).append(m)
    return idx


def encontrar_pares(fuente_a: list[dict], fuente_b: list[dict],
                    umbral_sim: float = 0.7) -> list[dict]:
    idx_b = _indexar(fuente_b)
    pares = []
    vistos: set[tuple] = set()  # dedup (id_a, id_b)

    for a in fuente_a:
        s_a = a["sem"]
        if not s_a["activo"]:
            continue

        # Candidatos en fuente_b con mismo activo (fecha exacta o ±1 día)
        candidatos: list[dict] = []
        for fecha_b in [s_a["fecha"]] + _fechas_adyacentes(s_a["fecha"]):
            candidatos.extend(idx_b.get((s_a["activo"], fecha_b), []))

        for b in candidatos:
            clave = (a["market_id"], b["market_id"])
            if clave in vistos:
                continue
            vistos.add(clave)
            sim = similitud(s_a, b["sem"])
            if sim < umbral_sim:
                continue

            gap     = a["price_yes"] - b["price_yes"]
            gap_pct = abs(gap) * 100
            if gap_pct < MIN_GAP_PCT:
                continue

            if gap > 0:
                coste    = b["price_yes"] + a["price_no"]
                plat_yes = b["plataforma"]
                plat_no  = a["plataforma"]
            else:
                coste    = a["price_yes"] + b["price_no"]
                plat_yes = a["plataforma"]
                plat_no  = b["plataforma"]

            profit_bruto = 1.0 - coste
            fee_poly = 0.02 if "Polymarket" in (a["plataforma"], b["plataforma"]) else 0
            profit_neto = profit_bruto - fee_poly

            pares.append({
                "plataforma_a":    a["plataforma"],
                "plataforma_b":    b["plataforma"],
                "activo":          s_a["activo"],
                "similitud":       sim,
                "titulo_a":        a["titulo"][:80],
                "titulo_b":        b["titulo"][:80],
                "price_yes_a":     a["price_yes"],
                "price_yes_b":     b["price_yes"],
                "gap_pct":         round(gap_pct, 2),
                "coste_arb":       round(coste, 4),
                "profit_bruto":    round(profit_bruto * 100, 2),
                "profit_neto":     round(profit_neto * 100, 2),
                "accionable":      profit_neto > 0,
                "plat_compra_yes": plat_yes,
                "plat_compra_no":  plat_no,
                "liq_a":           a["liquidez"],
                "liq_b":           b["liquidez"],
                "fecha_a":         s_a["fecha"],
                "fecha_b":         b["sem"]["fecha"],
                "url_a":           a["url"],
                "url_b":           b["url"],
                "AVISO":           "SOLO OBSERVACION — validar resolucion antes de operar",
            })

    pares.sort(key=lambda x: (-x["accionable"], -x["profit_neto"]))
    return pares


def _fechas_adyacentes(fecha: str) -> list[str]:
    """Devuelve fecha-1 y fecha+1 para matching tolerante."""
    if not fecha:
        return []
    try:
        d = dt.date.fromisoformat(fecha)
        return [
            (d - dt.timedelta(days=1)).isoformat(),
            (d + dt.timedelta(days=1)).isoformat(),
        ]
    except ValueError:
        return []


# ---------------------------------------------------------------------------
# CSV output
# ---------------------------------------------------------------------------

COLS = [
    "timestamp_utc", "plataforma_a", "plataforma_b", "activo", "similitud",
    "titulo_a", "titulo_b", "price_yes_a", "price_yes_b",
    "gap_pct", "coste_arb", "profit_bruto", "profit_neto", "accionable",
    "plat_compra_yes", "plat_compra_no", "liq_a", "liq_b",
    "fecha_a", "fecha_b", "url_a", "url_b", "AVISO",
]


def guardar_csv(pares: list[dict], fecha: str) -> Path:
    path  = DIR_SHADOW / f"cross_arb_{fecha}.csv"
    ts    = datetime.now(timezone.utc).isoformat(timespec="seconds")
    nuevo = not path.exists()
    with open(path, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLS, extrasaction="ignore")
        if nuevo:
            w.writeheader()
        for p in pares:
            w.writerow({**p, "timestamp_utc": ts})
    return path


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    ts    = datetime.now(timezone.utc).isoformat(timespec="seconds")
    fecha = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    print(f"[{ts}] === Cross-Platform Arb Scanner (OBSERVACION) ===")

    print("  Cargando Polymarket (snapshot local)...")
    t0   = time.time()
    poly = cargar_polymarket()
    print(f"    {len(poly)} mercados bracket crypto ({time.time()-t0:.1f}s)")

    print("  Cargando Kalshi...")
    t0     = time.time()
    kalshi = cargar_kalshi()
    print(f"    {len(kalshi)} mercados crypto ({time.time()-t0:.1f}s)")

    print("  Cargando Limitless...")
    t0        = time.time()
    limitless = cargar_limitless()
    print(f"    {len(limitless)} mercados crypto ({time.time()-t0:.1f}s)")

    print("  Cargando Manifold...")
    t0       = time.time()
    manifold = cargar_manifold()
    print(f"    {len(manifold)} mercados crypto ({time.time()-t0:.1f}s)")

    todas = {
        "Polymarket": poly,
        "Kalshi":     kalshi,
        "Limitless":  limitless,
        "Manifold":   manifold,
    }

    pares_totales: list[dict] = []
    plataformas = list(todas.keys())
    for i, pa in enumerate(plataformas):
        for pb in plataformas[i + 1:]:
            fa, fb = todas[pa], todas[pb]
            if not fa or not fb:
                continue
            pares = encontrar_pares(fa, fb)
            if pares:
                print(f"  {pa}↔{pb}: {len(pares)} pares gap≥{MIN_GAP_PCT}%")
            pares_totales.extend(pares)

    pares_totales.sort(key=lambda x: (-x["accionable"], -x["profit_neto"]))

    accionables = [p for p in pares_totales if p["accionable"]]
    print(f"\n  Total pares: {len(pares_totales)}  |  Accionables: {len(accionables)}")

    for p in accionables[:5]:
        print(f"\n  * {p['plataforma_a']}x{p['plataforma_b']} | {p['activo']} | sim={p['similitud']}")
        print(f"    A: {p['titulo_a'][:65]}")
        print(f"    B: {p['titulo_b'][:65]}")
        print(f"    YES_a={p['price_yes_a']}  YES_b={p['price_yes_b']}  gap={p['gap_pct']:+.1f}%")
        print(f"    BUY_YES en {p['plat_compra_yes']}, BUY_NO en {p['plat_compra_no']}")
        print(f"    profit_bruto={p['profit_bruto']:+.1f}%  profit_neto={p['profit_neto']:+.1f}%")
        print(f"    !! {p['AVISO']}")

    if not accionables and pares_totales:
        print("\n  Sin arb neto positivo. Top gaps observados:")
        for p in pares_totales[:5]:
            print(f"    {p['plataforma_a']}x{p['plataforma_b']} {p['activo']} "
                  f"gap={p['gap_pct']:+.1f}% profit_neto={p['profit_neto']:+.1f}% sim={p['similitud']}")
    elif not pares_totales:
        print("\n  Sin pares comparables encontrados.")
        print(f"  Poly={len(poly)} Kalshi={len(kalshi)} Limitless={len(limitless)} Manifold={len(manifold)}")

    if pares_totales:
        path = guardar_csv(pares_totales, fecha)
        print(f"\n  Guardado: {path}")

    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] === Fin Cross Arb ===")


if __name__ == "__main__":
    main()
