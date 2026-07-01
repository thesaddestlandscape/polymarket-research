"""
arb_scanner.py — Escáner de arbitraje en mercados de Polymarket.

Detecta dos tipos de oportunidad:

  TIPO 1 — Bracket Arb (semi-garantizado):
    Mercados de precio-rango mutuamente excluyentes dentro de un mismo evento.
    Ej: "Will ETH be between $1600-$1700?" + "$1700-$1800?" + ... (8 brackets).
    Si compras TODOS los brackets y la suma < 1.0, profit garantizado solo si
    el precio cae dentro de algún bracket. Riesgo = precio fuera del rango total.
    Califica si: suma_YES < 0.97 Y liq_min >= 500 Y n_brackets >= 3.

  TIPO 2 — Overround Sell (vender mercado sobrevalorado):
    Mercados donde suma_YES > 1.02 → el mercado sobrestima la suma.
    Requeriría vender (no disponible en Polymarket sin posición previa).
    Se registra como observación.

Corre en el slow loop. Escribe data/shadow/arb_scan_YYYY-MM-DD.csv
y loguea las oportunidades encontradas.
"""
import csv
import glob
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

DIR_MARKETS = Path("data/markets")
DIR_SHADOW  = Path("data/shadow")
DIR_SHADOW.mkdir(parents=True, exist_ok=True)

# Fees estimadas de Polymarket: 2% sobre el payout del leg ganador
FEE_PAYOUT = 0.02
# Umbral: suma de YES < esto para considerar oportunidad (incluye margen fees)
UMBRAL_ARB  = 0.97
# Umbral overround: suma > esto → mercado sobrevalorado
UMBRAL_OVER = 1.02
# Liquidez mínima en el bracket más pequeño
LIQ_MIN = 200   # liq mínima del bracket más pequeño; limita el tamaño máximo de la posición
# Mínimo de brackets para que el análisis tenga sentido
N_MIN   = 3

# Skip si algún bracket tiene YES > este umbral (mercado casi resuelto, no es arb real)
NEAR_RESOLVED_THRESHOLD = 0.90
# Gap mínimo para ser ACCIONABLE (5 cents) vs solo DETECTABLE (3 cents con UMBRAL_ARB)
UMBRAL_ACCIONABLE = 0.95

BRACKET_PATTERNS = [
    re.compile(r'between\s+\$[\d,]+\s+and\s+\$[\d,]+', re.I),
    re.compile(r'between\s+[\d,]+\s+and\s+[\d,]+', re.I),
    re.compile(r'\$[\d,]+\s*[-–]\s*\$[\d,]+', re.I),
]

def es_bracket(pregunta: str) -> bool:
    for p in BRACKET_PATTERNS:
        if p.search(pregunta):
            return True
    return False


def cargar_snapshot_reciente() -> dict:
    """Carga el snapshot más reciente de cada market_id."""
    archivos = sorted(glob.glob(str(DIR_MARKETS / "*.csv")))
    if not archivos:
        return {}
    por_id = {}
    with open(archivos[-1], encoding="utf-8") as f:
        for row in csv.DictReader(f):
            mid = row.get("market_id", "")
            ts  = row.get("timestamp_utc", "")
            if not mid:
                continue
            if mid not in por_id or ts > por_id[mid]["timestamp_utc"]:
                por_id[mid] = row
    return por_id


def analizar_oportunidades(por_id: dict) -> list:
    """Agrupa brackets por evento y detecta oportunidades."""
    by_event = defaultdict(list)

    for mid, r in por_id.items():
        if not es_bracket(r.get("question", "")):
            continue
        eid = r.get("event_id", "")
        if not eid:
            continue
        try:
            yes = float(r.get("price_yes") or 0)
            # Coste real de comprar el bracket es el ASK, no el precio medio
            # (price_yes) — con 2026-07-01 verificado que el ask medio está
            # ~0.025 por encima del mid, y con N_MIN=3-9 patas el spread
            # acumulado puede superar el gap de 3-5% que dispara el arb,
            # convirtiendo una oportunidad "detectada" en pérdida garantizada
            # si se ejecutara al precio real. Fallback a price_yes solo si
            # best_ask no viene informado (no observado en la práctica).
            ask = float(r.get("best_ask") or 0) or yes
            liq = float(r.get("liquidity") or 0)
            if yes <= 0 or ask <= 0:
                continue
        except (ValueError, TypeError):
            continue

        by_event[eid].append({
            "mid":        mid,
            "question":   r.get("question", ""),
            "yes":        yes,
            "ask":        ask,
            "liquidity":  liq,
            "end_date":   r.get("end_date", "")[:10],
            "event":      r.get("event_title", ""),
        })

    oportunidades = []
    for eid, mercados in by_event.items():
        if len(mercados) < N_MIN:
            continue

        # Skip eventos donde algún bracket ya está casi resuelto (YES > 90%)
        # Esos precios no representan arb real, solo el mercado convergiendo a 1
        if any(m["yes"] > NEAR_RESOLVED_THRESHOLD for m in mercados):
            continue

        # Coste real de ejecutar el bracket completo = suma de ASKs, no de mids.
        suma_yes  = sum(m["yes"] for m in mercados)   # referencia/display
        suma_ask  = sum(m["ask"] for m in mercados)   # coste ejecutable real
        liq_min   = min(m["liquidity"] for m in mercados)
        liq_total = sum(m["liquidity"] for m in mercados)

        # Payout neto si gana un bracket: 1 × (1 - FEE_PAYOUT)
        payout_neto = 1.0 - FEE_PAYOUT
        # Profit real = payout_neto - suma_invertida (al precio que realmente se paga)
        profit_neto = payout_neto - suma_ask
        profit_pct  = profit_neto * 100

        if suma_ask < UMBRAL_ARB and liq_min >= LIQ_MIN:
            tipo = "BRACKET_ARB"
        elif suma_yes > UMBRAL_OVER:
            tipo = "OVERROUND"
        else:
            continue

        # Accionable: gap ≥ 5% (suma < 0.95) sobre el coste ejecutable real
        accionable = (tipo == "BRACKET_ARB" and suma_ask < UMBRAL_ACCIONABLE)

        # Rango cubierto por los brackets (para estimar el riesgo de cola)
        preguntas = [m["question"] for m in mercados]
        precios_nums = []
        for q in preguntas:
            nums = re.findall(r'[\d,]+', q.replace("$", "").replace(",", ""))
            precios_nums.extend(int(n) for n in nums if int(n) > 100)
        rango_min = min(precios_nums) if precios_nums else None
        rango_max = max(precios_nums) if precios_nums else None

        oportunidades.append({
            "tipo":        tipo,
            "accionable":  accionable,
            "event_id":    eid,
            "event":       mercados[0]["event"][:60],
            "end_date":    mercados[0]["end_date"],
            "n_brackets":  len(mercados),
            "suma_yes":    round(suma_yes, 4),
            "suma_ask":    round(suma_ask, 4),
            "gap_pct":     round((1.0 - suma_ask) * 100, 2),
            "profit_pct":  round(profit_pct, 2),
            "liq_min":     round(liq_min, 0),
            "liq_total":   round(liq_total, 0),
            "rango_min":   rango_min,
            "rango_max":   rango_max,
            "mercados":    sorted(mercados, key=lambda x: x["yes"], reverse=True),
        })

    oportunidades.sort(key=lambda x: (-abs(x["profit_pct"])))
    return oportunidades


def guardar_csv(oportunidades: list, fecha: str):
    """Guarda las oportunidades en CSV para seguimiento."""
    path = DIR_SHADOW / f"arb_scan_{fecha}.csv"
    columnas = [
        "timestamp_utc", "tipo", "accionable", "event", "end_date",
        "n_brackets", "suma_yes", "gap_pct", "profit_pct",
        "liq_min", "liq_total", "rango_min", "rango_max",
    ]
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    nuevo = not path.exists()
    with open(path, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=columnas, extrasaction="ignore")
        if nuevo:
            w.writeheader()
        for op in oportunidades:
            w.writerow({**op, "timestamp_utc": ts})
    return path


def main():
    ts    = datetime.now(timezone.utc).isoformat(timespec="seconds")
    fecha = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    print(f"[{ts}] === Arb Scanner ===")

    por_id = cargar_snapshot_reciente()
    if not por_id:
        print("  Sin datos de mercados disponibles.")
        return

    print(f"  Mercados en snapshot: {len(por_id)}")
    oportunidades = analizar_oportunidades(por_id)

    arb        = [o for o in oportunidades if o["tipo"] == "BRACKET_ARB"]
    accionable = [o for o in arb if o["accionable"]]
    detectable = [o for o in arb if not o["accionable"]]
    over       = [o for o in oportunidades if o["tipo"] == "OVERROUND"]

    print(f"  BRACKET_ARB detectable (gap>3%, suma<0.97): {len(arb)}")
    print(f"    → ACCIONABLE (gap≥5%, suma<0.95):         {len(accionable)}")
    print(f"    → solo detectable (gap 3-5%):             {len(detectable)}")
    print(f"  OVERROUND (suma>1.02):                      {len(over)}")

    for op in accionable:
        print(f"\n  🎯 ACCIONABLE | {op['event']} ({op['n_brackets']} brackets)")
        print(f"     suma={op['suma_yes']:.3f}  gap={op['gap_pct']:+.1f}%  profit_neto={op['profit_pct']:+.1f}%"
              f"  liq_min={op['liq_min']:.0f}  vence={op['end_date']}")
        if op["rango_min"] and op["rango_max"]:
            print(f"     Rango cubierto: ${op['rango_min']:,} – ${op['rango_max']:,}")
        for m in op["mercados"][:5]:
            print(f"     YES={m['yes']:.3f} liq={m['liquidity']:.0f} | {m['question'][:65]}")

    for op in detectable:
        print(f"\n  👀 detectable | {op['event']} ({op['n_brackets']} brackets)"
              f"  suma={op['suma_yes']:.3f}  gap={op['gap_pct']:+.1f}%  liq_min={op['liq_min']:.0f}")

    if oportunidades:
        path = guardar_csv(oportunidades, fecha)
        print(f"\n  Guardado: {path}")

    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] === Fin Arb Scanner ===")


if __name__ == "__main__":
    main()
