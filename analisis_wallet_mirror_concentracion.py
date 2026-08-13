#!/usr/bin/env python3
"""
analisis_wallet_mirror_concentracion.py -- P24, punto 5 del barrido de
huecos de Wallet Mirror (13-Ago, petición explícita Javi).

Pregunta: ¿cuánto del volumen de señales SEGUIR-BTC (las únicas tuplas
hoy en pares_permitidos_live, #5min/#15min) está concentrado en pocas
wallets o pocos mercados? Si 1-2 wallets dominan, el "edge" medido puede
ser la suerte/ventaja de esa wallet concreta, no un patrón robusto de
smart money -- mismo patrón ya confirmado en P31 (ETH#15m#fade, 62.8%
del volumen de una sola wallet).

Solo lectura -- reporta, no vetea ni pausa nada. Pensado para correr a
mano cada sesión (o cron diario junto al resto de auditorías de madurez,
CLAUDE.md pt.16).
"""
import csv
import json
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
DRY_RUN = REPO / "data/shadow/wallet_mirror_dry_run.csv"
CONFIG_LIVE = REPO / "data/live/config_live.json"
OUT_JSON = REPO / "data/shadow/wallet_mirror_concentracion.json"

TOP1_WALLET_ALERTA_PCT = 30.0
TOP1_MERCADO_ALERTA_PCT = 20.0


def _tuplas_wallet_mirror_live() -> set[tuple[str, str]]:
    """(activo, marco) de las tuplas WALLET_MIRROR realmente en
    pares_permitidos_live -- no hardcodear BTC/5min/15min, leer la
    whitelist real por si se amplía."""
    try:
        c = json.loads(CONFIG_LIVE.read_text(encoding="utf-8"))
    except Exception:
        return set()
    out = set()
    for t in c.get("pares_permitidos_live", []):
        if not t.startswith("WALLET_MIRROR#"):
            continue
        partes = t.split("#")
        if len(partes) == 4:
            out.add((partes[1], partes[2]))
    return out


def analizar(activo: str, marco: str) -> dict | None:
    if not DRY_RUN.exists():
        return None
    filas = [r for r in csv.DictReader(open(DRY_RUN, encoding="utf-8"))
             if r.get("tipo") == "SEGUIR" and r.get("activo") == activo and r.get("marco") == marco]
    n = len(filas)
    if n == 0:
        return None

    por_wallet = Counter(r["wallet"] for r in filas)
    por_mercado = Counter(r["market_slug"] for r in filas)
    top1_wallet, top1_wallet_n = por_wallet.most_common(1)[0]
    top1_mercado, top1_mercado_n = por_mercado.most_common(1)[0]
    top1_wallet_pct = round(100 * top1_wallet_n / n, 1)
    top1_mercado_pct = round(100 * top1_mercado_n / n, 1)

    return {
        "n_senales": n,
        "n_wallets_distintas": len(por_wallet),
        "n_mercados_distintos": len(por_mercado),
        "top5_wallets": [{"wallet": w, "n": c, "pct": round(100 * c / n, 1)}
                          for w, c in por_wallet.most_common(5)],
        "top5_mercados": [{"market_slug": m, "n": c, "pct": round(100 * c / n, 1)}
                           for m, c in por_mercado.most_common(5)],
        "top1_wallet_pct": top1_wallet_pct,
        "top1_mercado_pct": top1_mercado_pct,
        "alerta_wallet": top1_wallet_pct > TOP1_WALLET_ALERTA_PCT,
        "alerta_mercado": top1_mercado_pct > TOP1_MERCADO_ALERTA_PCT,
    }


def main() -> int:
    tuplas = _tuplas_wallet_mirror_live()
    if not tuplas:
        print("Sin tuplas WALLET_MIRROR en pares_permitidos_live -- nada que auditar")
        return 0

    resultado = {"generado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "tuplas": {}}
    for activo, marco in sorted(tuplas):
        r = analizar(activo, marco)
        clave = f"{activo}#{marco}"
        if r is None:
            print(f"=== {clave}: sin señales SEGUIR ===")
            continue
        resultado["tuplas"][clave] = r
        print(f"\n=== Concentración Wallet Mirror {clave} SEGUIR (n={r['n_senales']} señales) ===")
        print(f"nº wallets distintas: {r['n_wallets_distintas']} | nº mercados distintos: {r['n_mercados_distintos']}")
        print("Top 5 wallets:")
        for w in r["top5_wallets"]:
            print(f"  {w['wallet']}: {w['n']} ({w['pct']}%)")
        print("Top 5 mercados:")
        for m in r["top5_mercados"]:
            print(f"  {m['market_slug']}: {m['n']} ({m['pct']}%)")
        if r["alerta_wallet"]:
            print(f"⚠️ concentración de wallet alta ({r['top1_wallet_pct']}%>{TOP1_WALLET_ALERTA_PCT}%) "
                  f"-- el edge medido puede depender de 1 sola wallet")
        if r["alerta_mercado"]:
            print(f"⚠️ concentración de mercado alta ({r['top1_mercado_pct']}%>{TOP1_MERCADO_ALERTA_PCT}%) "
                  f"-- posible sesgo a un evento concreto, no un patrón general")

    OUT_JSON.write_text(json.dumps(resultado, ensure_ascii=False, indent=1), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
