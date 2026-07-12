#!/usr/bin/env python3
"""Verifica el sesgo de redención en las 47-55 wallets completas (P16,
CLAUDE.md pendiente: "verificar sesgo de redención en las 47 wallets
completas, no solo la muestra").

Contexto: el hallazgo de baseline-per-wallet (11-Jul, ver
project_bloque_b_backlog_11jul) etiqueta cada posición como GANADA si la
wallet la REDEEM (cobra) o PERDIDA si nunca la redime. El riesgo (mismo
bug que ya rompió /positions el 02-Jul): si una wallet vende una posición
ganadora en el mercado secundario ANTES de que resuelva (en vez de
esperar a redimir), esta posición se etiquetaría como "perdida" cuando en
realidad fue una venta con beneficio — sesgaría el hallazgo. La
comprobación original solo miró 1 wallet muestreada; esto la repite sobre
el universo completo (WALLETS_SEED + wallets clasificadas "smart" hoy en
smart_money_wallets.json).

Método por wallet: agrupa TRADE(BUY/SELL)+REDEEM por conditionId. Para
cada mercado donde la wallet compró, clasifica:
  - REDEEMED: hay >=1 evento REDEEM en ese mercado
  - VENDIDO_SIN_REDIMIR: hay SELL pero nunca REDEEM en ese mercado
  - NI_VENDIDO_NI_REDIMIDO: ni SELL ni REDEEM (posición "abandonada" bajo
    el heurístico actual = tratada como pérdida)
Reporta % VENDIDO_SIN_REDIMIR (el que contaminaría el heurístico) y, de
ese subconjunto, qué fracción se vendió a precio alto (>=0.70, indicio de
que probablemente iba a ganar y se vendió por caja en vez de esperar).

Solo lectura, mismo endpoint ya usado en producción (wallet_pnl_diario.py
fetch_activity). No toca dinero ni config.
"""
import json
import sys
import time
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from wallet_pnl_diario import WALLETS_SEED, fetch_activity  # noqa: E402

DIR_SHADOW = Path("data/shadow")
WALLETS_DB = DIR_SHADOW / "smart_money_wallets.json"
UMBRAL_PRECIO_ALTO = 0.70
EDAD_MIN_S = 24 * 3600  # excluir mercados con última compra hace <24h: casi
                         # seguro siguen abiertos (mercados 5/15/60min) y su
                         # ausencia de REDEEM/SELL no es "abandono", es que
                         # todavía no ha dado tiempo. Mismo filtro edad>3h
                         # del hallazgo original, con margen extra porque
                         # aquí no confirmamos resolución market a market.


def universo() -> dict:
    out = dict(WALLETS_SEED)
    try:
        db = json.loads(WALLETS_DB.read_text())
    except Exception:
        db = {}
    for w, v in db.items():
        if v.get("clasificacion") == "smart":
            out.setdefault(w, v.get("nombre", w[:10]))
    return out


def analizar_wallet(wallet: str, eventos: list, ahora_ts: float) -> dict:
    por_mercado = defaultdict(lambda: {"buy": 0.0, "sell": 0.0, "redeem": 0.0,
                                        "sell_precios": [], "ultima_buy_ts": 0})
    for e in eventos:
        cid = e.get("conditionId")
        if not cid:
            continue
        t = e.get("type")
        if t == "TRADE":
            u = float(e.get("usdcSize", 0) or 0)
            if e.get("side") == "BUY":
                por_mercado[cid]["buy"] += u
                por_mercado[cid]["ultima_buy_ts"] = max(
                    por_mercado[cid]["ultima_buy_ts"], e.get("timestamp", 0) or 0)
            else:
                por_mercado[cid]["sell"] += u
                p = e.get("price")
                if p is not None:
                    por_mercado[cid]["sell_precios"].append(float(p))
        elif t == "REDEEM":
            por_mercado[cid]["redeem"] += float(e.get("usdcSize", 0) or 0)

    redeemed = vendido_sin_redimir = ni_uno_ni_otro = 0
    vendido_alto = 0
    excluidos_recientes = 0
    for cid, d in por_mercado.items():
        if d["buy"] <= 0:
            continue  # no fue comprador en este mercado (solo vendió posición heredada, etc.)
        if (ahora_ts - d["ultima_buy_ts"]) < EDAD_MIN_S:
            excluidos_recientes += 1
            continue  # probablemente sigue abierto, no cuenta como "abandonado"
        if d["redeem"] > 0:
            redeemed += 1
        elif d["sell"] > 0:
            vendido_sin_redimir += 1
            if d["sell_precios"] and max(d["sell_precios"]) >= UMBRAL_PRECIO_ALTO:
                vendido_alto += 1
        else:
            ni_uno_ni_otro += 1
    total = redeemed + vendido_sin_redimir + ni_uno_ni_otro
    return dict(wallet=wallet, n_mercados=total, redeemed=redeemed,
                vendido_sin_redimir=vendido_sin_redimir,
                vendido_alto_precio=vendido_alto,
                ni_uno_ni_otro=ni_uno_ni_otro,
                excluidos_recientes=excluidos_recientes)


def main():
    import datetime as _dt
    univ = universo()
    ahora_ts = _dt.datetime.now(_dt.timezone.utc).timestamp()
    print(f"Universo: {len(univ)} wallets (seed + smart)")
    filas = []
    for i, (w, nombre) in enumerate(univ.items(), 1):
        evs = fetch_activity(w)
        r = analizar_wallet(w, evs, ahora_ts)
        r["nombre"] = nombre
        filas.append(r)
        print(f"  [{i}/{len(univ)}] {nombre[:20]:20s} mercados={r['n_mercados']:4d} "
              f"redeemed={r['redeemed']:4d} vendido_sin_redimir={r['vendido_sin_redimir']:3d} "
              f"(alto={r['vendido_alto_precio']}) ni_uno_ni_otro={r['ni_uno_ni_otro']} "
              f"excl_recientes={r['excluidos_recientes']}")
        time.sleep(0.2)

    tot_mercados = sum(r["n_mercados"] for r in filas)
    tot_redeemed = sum(r["redeemed"] for r in filas)
    tot_vsr = sum(r["vendido_sin_redimir"] for r in filas)
    tot_vsr_alto = sum(r["vendido_alto_precio"] for r in filas)
    tot_nn = sum(r["ni_uno_ni_otro"] for r in filas)
    print()
    print(f"=== TOTAL {len(filas)} wallets, {tot_mercados} posiciones-mercado ===")
    print(f"  redeemed:              {tot_redeemed} ({100*tot_redeemed/tot_mercados:.1f}%)")
    pct_vsr_alto = (100 * tot_vsr_alto / tot_vsr) if tot_vsr else 0
    print(f"  vendido sin redimir:   {tot_vsr} ({100*tot_vsr/tot_mercados:.1f}%) "
          f"— de estas, {tot_vsr_alto} ({pct_vsr_alto:.1f}%) vendidas a precio>={UMBRAL_PRECIO_ALTO}")
    print(f"  ni vendido ni redimido:{tot_nn} ({100*tot_nn/tot_mercados:.1f}%)")

    out = DIR_SHADOW / "sesgo_redencion_47wallets.json"
    out.write_text(json.dumps({
        "fecha": __import__("datetime").datetime.now(__import__("datetime").timezone.utc).isoformat(timespec="seconds"),
        "n_wallets": len(filas),
        "n_posiciones_totales": tot_mercados,
        "pct_redeemed": round(100 * tot_redeemed / tot_mercados, 2) if tot_mercados else None,
        "pct_vendido_sin_redimir": round(100 * tot_vsr / tot_mercados, 2) if tot_mercados else None,
        "pct_vendido_sin_redimir_precio_alto": round(100 * tot_vsr_alto / tot_vsr, 2) if tot_vsr else None,
        "pct_ni_vendido_ni_redimido": round(100 * tot_nn / tot_mercados, 2) if tot_mercados else None,
        "por_wallet": filas,
    }, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nGuardado en {out}")


if __name__ == "__main__":
    main()
