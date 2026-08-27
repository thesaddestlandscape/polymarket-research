#!/usr/bin/env python3
"""vigia_sports_log_growth.py — Vigía del gate de crecimiento logarítmico
(Kelly) para sports, mismo patrón EXACTO que vigia_log_growth.py (cripto,
21-Jul) aplicado a `pares_permitidos_live` de config_live_sports.json.

27-Ago noche (petición explícita Javi: "sports tiene todas las
funcionalidades de cripto que podemos explotar a nuestro favor?"): un
IC/hit-rate alto puede convivir con crecimiento compuesto NEGATIVO
("payout inverso" -- hit-rate alto, pérdidas grandes y poco frecuentes se
comen el compounding), mismo hallazgo que motivó este vigía en cripto
21-Jul (FAVORITO_CONFIRMADO#*#BUY_NO). Sports no tiene resultados en
results.csv (Wallet Mirror es un pipeline paralelo, solo trades.csv) --
usa directamente el retorno REALIZADO (pnl_neto_eur/stake_eur) de cada
trade CLOSED, ya incluye fee+slippage reales.

Whitelist de sports tiene formato distinto a cripto (CATEGORIA#TIPO#lo:hi,
el micro-bucket va embebido en la propia entrada, no como decision
separada) -- se matchea por categoria+tipo+entry_price cayendo en [lo,hi).

Cron diario, mismo horario que el resto de vigías de sports (07:xx UTC) o
vigias_frecuentes_fase0.py si se prefiere consolidar más adelante.
"""
import csv
import json
import math
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

CONFIG_LIVE = REPO / "data/sports/config_live_sports.json"
TRADES = REPO / "data/sports/trades.csv"
LATCH = REPO / "data/sports/vigia_log_growth_latch.json"
F_KELLY = 0.10
N_MIN = 15


def _log(msg: str) -> None:
    print(msg, flush=True)


def _tuplas_live() -> list[tuple[str, str, float, float]]:
    try:
        config = json.loads(CONFIG_LIVE.read_text(encoding="utf-8"))
    except Exception:
        return []
    tuplas = []
    for entrada in config.get("pares_permitidos_live", []):
        partes = entrada.split("#")
        if len(partes) != 3:
            continue
        categoria, tipo, ventana = partes
        try:
            lo_str, hi_str = ventana.split(":")
            tuplas.append((categoria, tipo, float(lo_str), float(hi_str)))
        except (ValueError, TypeError):
            continue
    return tuplas


def gate(categoria: str, tipo: str, lo: float, hi: float, f: float = F_KELLY) -> dict:
    if not TRADES.exists():
        return {"n": 0}
    rs = []
    with open(TRADES, encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            if (row.get("categoria") != categoria or row.get("tipo") != tipo
                    or row.get("status") != "CLOSED"):
                continue
            try:
                entry = float(row.get("entry_price") or 0)
                stake = float(row.get("stake_eur") or 0)
                pnl = float(row.get("pnl_neto_eur") or 0)
            except (TypeError, ValueError):
                continue
            if not (lo <= entry < hi) or stake <= 0:
                continue
            rs.append(pnl / stake)
    n = len(rs)
    if n == 0:
        return {"n": 0}
    hit = 100 * sum(1 for x in rs if x > 0) / n
    ev = sum(rs) / n
    g = sum(math.log(1 + f * x) for x in rs) / n
    return {"n": n, "hit_pct": hit, "ev_por_dolar": ev, "growth": g, "pasa": n >= N_MIN and g > 0}


def main() -> int:
    from shadow_digest import enviar_telegram

    try:
        vistos = json.loads(LATCH.read_text()) if LATCH.exists() else {}
    except Exception:
        vistos = {}

    tuplas = _tuplas_live()
    if not tuplas:
        _log("[vigia_sports_log_growth] pares_permitidos_live vacío -- nada que vigilar")
        return 0

    avisos = []
    for categoria, tipo, lo, hi in tuplas:
        r = gate(categoria, tipo, lo, hi)
        clave = f"{categoria}#{tipo}#{lo:.2f}:{hi:.2f}"
        if r["n"] < N_MIN:
            continue
        payout_inverso = r["growth"] < 0
        estado_anterior = vistos.get(clave, {}).get("payout_inverso")
        vistos[clave] = {"n": r["n"], "growth": round(r["growth"], 6),
                          "hit_pct": round(r["hit_pct"], 1), "payout_inverso": payout_inverso}
        if payout_inverso and estado_anterior is not True:
            avisos.append((clave, r))
        _log(f"[vigia_sports_log_growth] {clave}: n={r['n']} hit={r['hit_pct']:.1f}% "
             f"g(f={F_KELLY})={r['growth']:+.5f} {'⚠️ PAYOUT INVERSO' if payout_inverso else 'OK'}")

    if avisos:
        detalle = "\n".join(
            f"  {clave}: n={r['n']} hit={r['hit_pct']:.1f}% g(f={F_KELLY})={r['growth']:+.5f}"
            for clave, r in avisos
        )
        enviar_telegram(
            f"⚠️ PAYOUT INVERSO detectado en SPORTS (Kelly g<0 pese a hit-rate, "
            f"n≥{N_MIN}):\n{detalle}\nRevisar antes de aumentar exposición -- decisión de pausar es tuya.",
            bot="sports",
        )

    LATCH.write_text(json.dumps(vistos, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
