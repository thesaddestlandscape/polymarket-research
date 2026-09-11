#!/usr/bin/env python3
"""
combi_arb_prep.py — Prepara candidatos para análisis LLM de arbitraje combinatorio.

Extrae de los mercados activos grupos que tienen alta probabilidad de contener
dependencias lógicas no triviales (no detectables por reglas simples), y los
escribe en data/shadow/combi_candidates.json para que el trigger CCR los analice.
"""

import csv, json, re, sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO_DIR  = Path(__file__).parent
DATA_DIR  = REPO_DIR / "data"
OUT_FILE  = DATA_DIR / "shadow" / "combi_candidates.json"
MARKETS_DIR = DATA_DIR / "markets"

MAX_CANDIDATES = 60   # pares a enviar al LLM
MIN_LIQ        = 100  # liquidez mínima USD por mercado
MIN_PRICE      = 0.04
MAX_PRICE      = 0.96

# ─── utilidades ───────────────────────────────────────────────────────────────

def latest_markets_file():
    csvs = sorted(MARKETS_DIR.glob("*.csv"))
    return csvs[-1] if csvs else None

def load_markets(path):
    rows = list(csv.DictReader(open(path)))
    latest = {}
    for r in rows:
        mid = r.get("market_id", "")
        if mid:
            latest[mid] = r
    return list(latest.values())

def price(m):
    try:
        py = float(m.get("price_yes", "") or 0.5)
        return py if 0 < py < 1 else 0.5
    except:
        return 0.5

def liq(m):
    try:
        return float(m.get("liquidity", "") or 0)
    except:
        return 0

def strip_dates(q):
    q = re.sub(r'\b\d{1,2}/\d{1,2}/\d{2,4}\b', '', q)
    q = re.sub(r'\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\w*\s+\d{1,2},?\s*\d{2,4}', '', q, flags=re.I)
    q = re.sub(r'\bby\s+(Q[1-4]\s+)?\d{4}\b', '', q, flags=re.I)
    q = re.sub(r'\bby\s+\w+\s+\d{1,2}\b', '', q, flags=re.I)
    q = re.sub(r'\bin\s+\d{4}\b', '', q, flags=re.I)
    q = re.sub(r'\s+', ' ', q).strip()
    return q.rstrip('?').strip()

def strip_amounts(q):
    q = re.sub(r'\$[\d,.]+[BMK]?', '$X', q, flags=re.I)
    q = re.sub(r'\b\d+[BMK]?\s*(USD|USDC|dollars?)\b', '$X', q, flags=re.I)
    return q

# ─── agrupaciones heurísticas ─────────────────────────────────────────────────

def groups_by_entity(markets):
    """Agrupa mercados por entidad principal (empresa/token/persona)."""
    buckets = defaultdict(list)
    for m in markets:
        q  = m["question"].lower()
        eid = m.get("event_id", "")
        if eid:
            buckets[f"event_{eid}"].append(m)
    return {k: v for k, v in buckets.items() if 2 <= len(v) <= 20}

def groups_by_template(markets):
    """Agrupa por template (pregunta sin fechas ni cantidades)."""
    buckets = defaultdict(list)
    for m in markets:
        tpl = strip_amounts(strip_dates(m["question"]))
        tpl = tpl.lower()[:80]
        buckets[tpl].append(m)
    return {k: v for k, v in buckets.items() if 2 <= len(v) <= 8}

def candidate_pairs_from_group(group):
    """Genera todos los pares dentro de un grupo."""
    pairs = []
    for i in range(len(group)):
        for j in range(i+1, len(group)):
            a, b = group[i], group[j]
            pairs.append({
                "market_id_a": a["market_id"],
                "question_a":  a["question"],
                "price_yes_a": round(price(a), 4),
                "liq_a":       round(liq(a), 0),
                "market_id_b": b["market_id"],
                "question_b":  b["question"],
                "price_yes_b": round(price(b), 4),
                "liq_b":       round(liq(b), 0),
            })
    return pairs

# ─── main ─────────────────────────────────────────────────────────────────────

def main():
    f = latest_markets_file()
    if not f:
        print("ERROR: no hay CSV de mercados", file=sys.stderr)
        sys.exit(1)

    all_markets = load_markets(f)
    # filtro base: precio razonable y algo de liquidez
    filtered = [m for m in all_markets
                if MIN_PRICE < price(m) < MAX_PRICE
                and liq(m) >= MIN_LIQ]

    print(f"Mercados después de filtros: {len(filtered)}")

    # Candidatos de event_id (mercados bajo mismo evento)
    entity_groups = groups_by_entity(filtered)
    # Candidatos de template (preguntas similares sin fecha/monto)
    tpl_groups    = groups_by_template(filtered)

    all_pairs = []
    seen = set()

    def add_pairs(pairs):
        for p in pairs:
            key = tuple(sorted([p["market_id_a"], p["market_id_b"]]))
            if key not in seen:
                seen.add(key)
                all_pairs.append(p)

    # event_id groups primero (más relevantes — misma entidad, diferente condición)
    for g in entity_groups.values():
        add_pairs(candidate_pairs_from_group(g))

    # template groups después
    for g in tpl_groups.values():
        add_pairs(candidate_pairs_from_group(g))

    # Ordenar por liquidez combinada
    all_pairs.sort(key=lambda p: p["liq_a"] + p["liq_b"], reverse=True)
    top = all_pairs[:MAX_CANDIDATES]

    out = {
        "generated_at":   datetime.now(timezone.utc).isoformat(),
        "markets_file":   str(f.name),
        "total_filtered": len(filtered),
        "total_pairs":    len(all_pairs),
        "candidates":     top,
    }

    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"Candidatos escritos: {len(top)} → {OUT_FILE}")

if __name__ == "__main__":
    main()
