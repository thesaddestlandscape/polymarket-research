#!/usr/bin/env python3
"""Read-only: ¿alguna estrategia/par DESACTIVADO o BLACKLISTEADO tiene un buen window
horario que el kill AGREGADO nos hizo tirar? El criterio de desactivación
(UMBRAL_DESACTIVAR) y los blacklists horarios son hora-ciegos por diseño, así que una
estrategia con IC global negativo puede ser positiva en franjas concretas.

Hora desde prediction_timestamp (UTC, universal — no depende de features.hora_utc, que
falta en OF/PT). edge_real = |edge_neto| con signo del acierto (proxy, NO es ic_bayes).
Disciplina: n≥15 por bucket para concluir; resultado espectacular → sospechar bug primero.
NO toca producción. Correr desde la raíz del repo:  python3 scan_blacklist_hours.py

Hallazgo 2026-07-07 (ver [[project ... ]] / CLAUDE.md): el blacklist horario de OF BUY_NO
estaba parcialmente invertido (h10/h11 buenas y bloqueadas) → recalibrado a {2,7,9,22}.
"""
import csv, os
from collections import defaultdict

BASE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(BASE, "data", "shadow", "results.csv")
ROWS = list(csv.DictReader(open(RES)))
OF_BL_HOURS = {2, 7, 9, 22}          # tras recalibración 2026-07-07
OF_BL_PAIRS = {"ETH", "BNB", "XRP", "DOGE"}


def hour(r):
    ts = r["prediction_timestamp"]
    return int(ts[11:13]) if len(ts) >= 13 else None

def pair(r):
    s = r["subtype"]
    return s.split("#")[0] if "#" in s else ""

def sedge(r):
    try:
        e = abs(float(r["edge_neto"]))
        return e if r["acierto"] == "1" else -e
    except Exception:
        return None

def agg(rows):
    n = len(rows)
    if not n:
        return (0, 0.0, 0.0)
    hit = sum(1 for r in rows if r["acierto"] == "1") / n
    ses = [x for x in (sedge(r) for r in rows) if x is not None]
    return (n, hit, sum(ses)/len(ses) if ses else 0.0)

def scan(label, rows, blacklist_hours=None):
    n, hit, me = agg(rows)
    if n < 10:
        print(f"\n### {label}: n={n} (insuficiente, skip)")
        return
    by = defaultdict(list)
    for r in rows:
        h = hour(r)
        if h is not None:
            by[h].append(r)
    print(f"\n### {label}: n={n}  hit={hit*100:.1f}%  edge_real={me:+.4f}")
    hs = [(h, *agg(by[h])) for h in sorted(by)]
    val = sorted([x for x in hs if x[1] >= 8], key=lambda x: -x[3])
    if val:
        print("   mejores (n>=8):", " ".join(f"h{h}(n{n},{me:+.3f})" for h, n, _, me in val[:4]))
        print("   peores  (n>=8):", " ".join(f"h{h}(n{n},{me:+.3f})" for h, n, _, me in val[-4:]))
    for h, hn, hh, hme in hs:
        if hme > 0.05 and hn >= 12:          # candidata: n suficiente + edge claro
            tag = " [BLACKLISTEADA]" if blacklist_hours and h in blacklist_hours else ""
            print(f"   ⭐ CANDIDATA h{h}: n={hn} hit={hh*100:.0f}% edge={hme:+.3f}{tag}")
    if blacklist_hours:
        bl = [r for r in rows if hour(r) in blacklist_hours]
        ok = [r for r in rows if hour(r) not in blacklist_hours]
        bn, _, bme = agg(bl); on, _, ome = agg(ok)
        verdict = "JUSTIFICADA" if bme < ome else "⚠️REVISAR (blacklist NO peor)"
        print(f"   BLACKLIST {sorted(blacklist_hours)}: n={bn} edge={bme:+.4f} | "
              f"resto: n={on} edge={ome:+.4f} → {verdict}")

def rows_of(strategy=None, direction=None, pairs=None, subtype_contains=None):
    out = []
    for r in ROWS:
        if strategy and r["strategy"] != strategy: continue
        if direction and r["decision"] != direction: continue
        if pairs and pair(r) not in pairs: continue
        if subtype_contains and subtype_contains not in r["subtype"]: continue
        out.append(r)
    return out

if __name__ == "__main__":
    print("="*70)
    print("SCAN: ¿kills agregados esconden windows horarios buenos? (read-only)")
    print("="*70)
    scan("ORDER_FLOW_5M BUY_NO", rows_of("ORDER_FLOW_5M", "BUY_NO"), OF_BL_HOURS)
    scan("ORDER_FLOW_5M BUY_NO (BTC+SOL, lo que gobierna el blacklist)",
         rows_of("ORDER_FLOW_5M", "BUY_NO", {"BTC", "SOL"}), OF_BL_HOURS)
    scan("ORDER_FLOW_5M BUY_YES", rows_of("ORDER_FLOW_5M", "BUY_YES"), OF_BL_HOURS)
    for p in sorted(OF_BL_PAIRS):
        scan(f"ORDER_FLOW_5M {p} BUY_NO (par blacklisteado)", rows_of("ORDER_FLOW_5M", "BUY_NO", {p}))
    scan("UPDOWN_OU_5M BUY_NO", rows_of("UPDOWN_OU_5M", "BUY_NO"))
    scan("UPDOWN_OU_5M BUY_YES", rows_of("UPDOWN_OU_5M", "BUY_YES"))
    scan("PRICE_TARGET_GBM BUY_NO", rows_of("PRICE_TARGET_GBM", "BUY_NO"))
    scan("PRICE_TARGET_GBM BUY_YES", rows_of("PRICE_TARGET_GBM", "BUY_YES"))
    scan("GBM_LATE_60M BUY_NO", rows_of("GBM_LATE_60M", "BUY_NO"))
    scan("GBM_LATE_60M BUY_YES", rows_of("GBM_LATE_60M", "BUY_YES"))
    scan("SMART_FLOW_1H BUY_YES", rows_of("SMART_FLOW_1H", "BUY_YES"))
    scan("UPDOWN_GBM 5min BUY_YES (desactivada)", rows_of("UPDOWN_GBM", "BUY_YES", subtype_contains="5min"))
    scan("UPDOWN_GBM 5min BUY_NO (desactivada)", rows_of("UPDOWN_GBM", "BUY_NO", subtype_contains="5min"))
    scan("STREAK_MOM_5M BUY_YES (desactivada, ACUMULAR_SHADOW)", rows_of("STREAK_MOM_5M", "BUY_YES"))
    scan("STREAK_MOM_5M BUY_NO (desactivada, ACUMULAR_SHADOW)", rows_of("STREAK_MOM_5M", "BUY_NO"))
