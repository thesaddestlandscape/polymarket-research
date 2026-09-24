#!/usr/bin/env python3
"""vigia_predicciones_twap.py -- informe DIARIO de cómo mejoran las predicciones de los
modelos de precio tras corregir la referencia a la regla real de resolución (TWAP
Chainlink), y de si esa mejora se convierte en dinero o sigue siendo ARQUETIPO A
(24-Sep, petición Javi: "me vas avisando diariamente de cómo mejoran nuestras
predicciones. El problema de estas es que tienen arquetipo A").

Familias: UPDOWN_GBM* y GBM_LATE* en 5/15min. Compara, por estrategia:
  NUEVA = predicciones con features.ref_es_twap == 1 (desde 24-Sep ~12:00 UTC)
  VIEJA = mismas estrategias, 7 días previos al cambio (sin la feature)
Plano 1 (¿predecimos mejor?): n, acierto, Brier, PnL a 1 EUR al precio de mercado de
  la señal (fee cripto 7 % sobre la ganancia; NUNCA pnl_neto, que es stake Kelly).
Plano 2 (¿arquetipo A?): primer snapshot de libro_snapshots.csv del mismo
  (strategy, market_id) POSTERIOR a la predicción (<=180 s; orden temporal estricto,
  lección del look-ahead del 23-Sep): % fillable (ratio_vs_stake>=5) y PnL a 1 EUR
  al mejor_ask real de ese snapshot, solo sobre las fillables.
Telegram diario (resumen); detalle en data/shadow/vigia_predicciones_twap.json.
Streaming (results.csv >600 MB): solo se guardan las filas de las familias GBM.
"""
import csv
import json
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
RESULTS = REPO / "data/shadow/results.csv"
LIBRO = REPO / "data/live/libro_snapshots.csv"
OUT = REPO / "data/shadow/vigia_predicciones_twap.json"
CAMBIO = "2026-09-24T12:00:00"
DIAS_VIEJA = 7
FEE = 0.07
VENTANA_LIBRO_S = 180
csv.field_size_limit(10_000_000)


def _familia(strategy: str) -> bool:
    return strategy.startswith("UPDOWN_GBM") or strategy.startswith("GBM_LATE")


def _pnl(entry: float, acierto: int) -> float:
    return (1 - entry) / entry - FEE * (1 - entry) if acierto else -1.0


def _ts(s: str) -> float:
    try:
        d = datetime.fromisoformat(s.replace("Z", "+00:00"))
        return (d if d.tzinfo else d.replace(tzinfo=timezone.utc)).timestamp()
    except (ValueError, AttributeError):
        return 0.0


def main() -> int:
    desde_vieja = (datetime.fromisoformat(CAMBIO) - timedelta(days=DIAS_VIEJA)).isoformat()
    filas = []
    with open(RESULTS, encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            st = r.get("strategy") or ""
            pt = r.get("prediction_timestamp") or ""
            if pt < desde_vieja or not _familia(st):
                continue
            sub = r.get("subtype") or ""
            if not sub.endswith(("5min", "15min")) or r.get("acierto") not in ("0", "1"):
                continue
            try:
                py = float(r["precio_yes_mercado"])
                ft = json.loads(r.get("features") or "{}")
            except (ValueError, KeyError, json.JSONDecodeError):
                continue
            tw = int(ft.get("ref_es_twap") or 0)
            if pt >= CAMBIO and not tw:
                continue          # post-cambio sin referencia TWAP (ventana no empezada, etc.): fuera
            regla = "NUEVA" if (tw and pt >= CAMBIO) else ("VIEJA" if pt < CAMBIO else None)
            if not regla:
                continue
            dec = r.get("decision") or ""
            entry = py if dec == "BUY_YES" else 1 - py
            if not (0.01 < entry < 0.99):
                continue
            ac = int(r["acierto"])
            try:
                br = float(r.get("brier_score") or "nan")
            except ValueError:
                br = float("nan")
            filas.append({"regla": regla, "st": st, "marco": sub.split("#")[-1], "mid": r.get("market_id"),
                          "t": _ts(pt), "dia": pt[:10], "ac": ac, "br": br, "pnl": _pnl(entry, ac),
                          "dec": dec})
    # libro posterior a la señal
    claves = {(x["st"], x["mid"]) for x in filas}
    libro = defaultdict(list)
    with open(LIBRO, encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            k = (r.get("strategy"), r.get("market_id"))
            if k not in claves:
                continue
            try:
                libro[k].append((_ts(r["timestamp_utc"]), float(r.get("ratio_vs_stake") or 0),
                                 float(r["mejor_ask"]) if r.get("mejor_ask") else None))
            except ValueError:
                continue
    for x in filas:
        snaps = sorted(s for s in libro.get((x["st"], x["mid"]), []) if 0 <= s[0] - x["t"] <= VENTANA_LIBRO_S)
        x["con_libro"] = bool(snaps)
        if snaps:
            _, ratio, ask = snaps[0]
            x["fillable"] = ratio >= 5 and ask is not None and 0.01 < ask < 0.99
            x["pnl_fill"] = _pnl(ask, x["ac"]) if x["fillable"] else None
    # agregados
    grupos = defaultdict(list)
    for x in filas:
        grupos[(x["st"], x["marco"], x["regla"])].append(x)
        grupos[("TODAS_GBM", x["marco"], x["regla"])].append(x)

    def resumen(xs):
        n = len(xs)
        brs = [x["br"] for x in xs if x["br"] == x["br"]]
        cl = [x for x in xs if x.get("con_libro")]
        fi = [x for x in cl if x.get("fillable")]
        return {"n": n, "acierto": round(sum(x["ac"] for x in xs) / n, 4),
                "brier": round(sum(brs) / len(brs), 4) if brs else None,
                "pnl_1eur_mercado": round(sum(x["pnl"] for x in xs) / n, 4),
                "n_con_libro": len(cl), "fillable_pct": round(len(fi) / len(cl), 3) if cl else None,
                "pnl_1eur_fillable": round(sum(x["pnl_fill"] for x in fi) / len(fi), 4) if fi else None,
                "n_fillable": len(fi)}

    res = {f"{st}|{marco}|{regla}": resumen(xs) for (st, marco, regla), xs in grupos.items() if len(xs) >= 10}
    por_dia = defaultdict(list)
    for x in filas:
        if x["regla"] == "NUEVA":
            por_dia[x["dia"]].append(x)
    salida = {"actualizado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "cambio": CAMBIO,
              "grupos": res, "nueva_por_dia": {d: resumen(v) for d, v in sorted(por_dia.items())}}
    OUT.write_text(json.dumps(salida, indent=1, ensure_ascii=False), encoding="utf-8")

    msg = ["📈 Predicciones modelos GBM con regla TWAP -- vieja → nueva"]
    for marco in ("5min", "15min"):
        v, nu = res.get(f"TODAS_GBM|{marco}|VIEJA"), res.get(f"TODAS_GBM|{marco}|NUEVA")
        if v and nu:
            msg.append(f"{marco}: acierto {v['acierto']:.1%}→{nu['acierto']:.1%} (n={nu['n']}) | "
                       f"€/tr mercado {v['pnl_1eur_mercado']:+.3f}→{nu['pnl_1eur_mercado']:+.3f} | "
                       f"fillable {v['fillable_pct']}→{nu['fillable_pct']} | "
                       f"€/tr fillable {v['pnl_1eur_fillable']}→{nu['pnl_1eur_fillable']} (n={nu['n_fillable']})")
        elif v:
            msg.append(f"{marco}: vieja acierto {v['acierto']:.1%} (n={v['n']}) | nueva: sin n suficiente todavía")
    mejores = sorted(((k, g) for k, g in res.items() if k.endswith("|NUEVA") and not k.startswith("TODAS")
                      and g["n_fillable"] >= 15), key=lambda kg: -(kg[1]["pnl_1eur_fillable"] or -9))[:3]
    if mejores:
        msg.append("Top estrategias (nueva, fillable n>=15): " + "; ".join(
            f"{k.split('|')[0]} {k.split('|')[1]} {g['pnl_1eur_fillable']:+.3f}€/tr fill {g['fillable_pct']:.0%}"
            for k, g in mejores))
    msg.append("Arquetipo A = acierto alto pero €/tr fillable ≤0: el libro solo deja entrar cuando nos equivocamos.")
    print("\n".join(msg))
    try:
        from shadow_digest import enviar_telegram
        enviar_telegram("\n".join(msg))
    except Exception as e:
        print(f"(Telegram falló: {e})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
