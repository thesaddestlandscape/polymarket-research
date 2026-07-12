#!/usr/bin/env python3
"""Cierra el caveat de P16 (CLAUDE.md): el hallazgo baseline-per-wallet
(11-Jul, ver project_bloque_b_backlog_11jul) etiquetaba GANADA=redeem,
PERDIDA=no-redeem. `analisis_sesgo_redencion_wallets.py` (12-Jul) ya midio
la contaminacion global: 9.25% de posiciones se venden sin redimir, y de
esas el 62.32% a precio>=0.70 (probable ganadora mal etiquetada como
perdida) -- ~5.8% del total, mas del doble del 2.5% que estimo el chequeo
parcial de 1 sola wallet.

Pregunta que NO respondia ese script: la contaminacion es GLOBAL, pero el
hallazgo original depende de si esta contaminacion esta REPARTIDA POR IGUAL
entre los cortes (tamano relativo, activo habitual) o concentrada en uno.
Este script reconstruye los mismos cortes del 11-Jul (tamano >=2x/0.5x-2x/
<=0.5x mediana propia; activo dentro/fuera de sus 2 habituales) con DOS
heuristicos de outcome:
  - ANTIGUO: redeem>0 -> WIN, si no -> LOSS (lo que uso el hallazgo 11-Jul)
  - CORREGIDO: redeem>0 -> WIN; vendido sin redimir a precio>=0.70 -> WIN
    (probable ganadora cobrada en el secundario); resto -> LOSS
Si los gaps de win-rate sobreviven casi iguales bajo ambos heuristicos, el
hallazgo esta limpio. Si se contraen o invierten, el sesgo de redencion
explicaba (parte de) el hallazgo.

Solo lectura, mismo endpoint publico ya usado en produccion.
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
EDAD_MIN_S = 3 * 3600  # mismo filtro edad>3h que el hallazgo original 11-Jul


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


def ticker_de_slug(slug: str, title: str) -> str:
    s = (slug or "").lower()
    if s.startswith("btc") or s.startswith("bitcoin"):
        return "BTC"
    if s.startswith("eth") or s.startswith("ethereum"):
        return "ETH"
    if s.startswith("sol") or s.startswith("solana"):
        return "SOL"
    if s.startswith("xrp") or s.startswith("ripple"):
        return "XRP"
    t = (title or "").split()[0].upper() if title else ""
    return t or "OTRO"


def mercados_de_wallet(eventos: list, ahora_ts: float) -> dict:
    por_mercado = defaultdict(lambda: {"buy": 0.0, "sell": 0.0, "redeem": 0.0,
                                        "sell_precios": [], "ultima_buy_ts": 0,
                                        "primera_buy_ts": None, "ticker": "OTRO"})
    for e in eventos:
        cid = e.get("conditionId")
        if not cid:
            continue
        t = e.get("type")
        d = por_mercado[cid]
        if t == "TRADE":
            u = float(e.get("usdcSize", 0) or 0)
            ts = e.get("timestamp", 0) or 0
            if d["ticker"] == "OTRO":
                d["ticker"] = ticker_de_slug(e.get("slug", ""), e.get("title", ""))
            if e.get("side") == "BUY":
                d["buy"] += u
                d["ultima_buy_ts"] = max(d["ultima_buy_ts"], ts)
                if d["primera_buy_ts"] is None or ts < d["primera_buy_ts"]:
                    d["primera_buy_ts"] = ts
            else:
                d["sell"] += u
                p = e.get("price")
                if p is not None:
                    d["sell_precios"].append(float(p))
        elif t == "REDEEM":
            d["redeem"] += float(e.get("usdcSize", 0) or 0)

    cerrados = {}
    for cid, d in por_mercado.items():
        if d["buy"] <= 0:
            continue
        if (ahora_ts - d["ultima_buy_ts"]) < EDAD_MIN_S:
            continue
        cerrados[cid] = d
    return cerrados


def clasificar_outcomes(cerrados: dict) -> dict:
    """Devuelve {cid: (win_antiguo, win_corregido)}."""
    out = {}
    for cid, d in cerrados.items():
        if d["redeem"] > 0:
            out[cid] = (True, True)
        elif d["sell"] > 0 and d["sell_precios"] and max(d["sell_precios"]) >= UMBRAL_PRECIO_ALTO:
            out[cid] = (False, True)  # aqui es donde antiguo y corregido difieren
        else:
            out[cid] = (False, False)
    return out


def bucket_tamano(buy: float, mediana: float) -> str:
    if mediana <= 0:
        return "sin_mediana"
    r = buy / mediana
    if r >= 2.0:
        return ">=2x_mediana"
    if r <= 0.5:
        return "<=0.5x_mediana"
    return "0.5x-2x_mediana"


def main():
    import statistics as st
    import datetime as _dt
    univ = universo()
    ahora_ts = _dt.datetime.now(_dt.timezone.utc).timestamp()
    print(f"Universo: {len(univ)} wallets (seed + smart)")

    filas = []  # una fila por (wallet, mercado cerrado)
    for i, (w, nombre) in enumerate(univ.items(), 1):
        evs = fetch_activity(w)
        cerrados = mercados_de_wallet(evs, ahora_ts)
        outcomes = clasificar_outcomes(cerrados)
        if not cerrados:
            print(f"  [{i}/{len(univ)}] {nombre[:20]:20s} sin mercados cerrados")
            time.sleep(0.2)
            continue
        buys = [d["buy"] for d in cerrados.values()]
        mediana = st.median(buys)
        cont_ticker = defaultdict(int)
        for d in cerrados.values():
            cont_ticker[d["ticker"]] += 1
        habituales = {t for t, _ in sorted(cont_ticker.items(), key=lambda kv: -kv[1])[:2]}
        for cid, d in cerrados.items():
            win_old, win_new = outcomes[cid]
            filas.append({
                "wallet": w, "nombre": nombre, "cid": cid,
                "buy": d["buy"], "ticker": d["ticker"],
                "bucket_tamano": bucket_tamano(d["buy"], mediana),
                "activo_habitual": d["ticker"] in habituales,
                "win_antiguo": win_old, "win_corregido": win_new,
            })
        print(f"  [{i}/{len(univ)}] {nombre[:20]:20s} mercados_cerrados={len(cerrados)}")
        time.sleep(0.2)

    def resumen(campo, valor, heur):
        sub = [f for f in filas if f[campo] == valor]
        if not sub:
            return (0, None)
        wins = sum(1 for f in sub if f[heur])
        return (len(sub), 100 * wins / len(sub))

    print()
    print(f"=== TOTAL {len(filas)} posiciones-mercado cerradas, {len(univ)} wallets ===")
    resultado = {"fecha": _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"),
                 "n_wallets": len(univ), "n_posiciones": len(filas), "cortes": {}}

    for campo, valores, etiqueta in [
        ("bucket_tamano", [">=2x_mediana", "0.5x-2x_mediana", "<=0.5x_mediana"], "Tamano vs mediana propia"),
        ("activo_habitual", [True, False], "Activo habitual (top2) vs novedad"),
    ]:
        print(f"\n--- {etiqueta} ---")
        resultado["cortes"][campo] = {}
        for v in valores:
            n_old, wr_old = resumen(campo, v, "win_antiguo")
            n_new, wr_new = resumen(campo, v, "win_corregido")
            print(f"  {str(v):20s} n={n_old:5d}  win_antiguo={wr_old if wr_old is None else round(wr_old,1)}%  "
                  f"win_corregido={wr_new if wr_new is None else round(wr_new,1)}%")
            resultado["cortes"][campo][str(v)] = {
                "n": n_old, "win_rate_antiguo": round(wr_old, 2) if wr_old is not None else None,
                "win_rate_corregido": round(wr_new, 2) if wr_new is not None else None,
            }

    out = DIR_SHADOW / "p16_redencion_corregido.json"
    out.write_text(json.dumps(resultado, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nGuardado en {out}")


if __name__ == "__main__":
    main()
