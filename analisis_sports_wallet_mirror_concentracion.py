#!/usr/bin/env python3
"""
analisis_sports_wallet_mirror_concentracion.py — 26-Ago, mismo chequeo
que analisis_wallet_mirror_concentracion.py (cripto, 13-Ago) aplicado a
Sports Wallet Mirror: petición explícita Javi ("sports tiene que tener
todo lo que tiene cripto para que funcione").

Sports no tiene `pares_permitidos_live` (nada es dinero real todavía),
así que en vez de auditar la whitelist live, audita CUALQUIER bucket
`bueno_confirmado`/`malo_confirmado` -- grid fijo
(wallet_mirror_gate_bucket.json) o ventana fina
(wallet_mirror_gate_bucket_fino.json) -- antes de que nadie proponga
promocionarlo: ¿el edge depende de 1-2 wallets o de 1-2 mercados
concretos, o es un patrón robusto de smart money distribuido?

Solo lectura. Salida: data/sports/wallet_mirror_concentracion.json
"""
import csv
import json
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
DRY_RUN = REPO / "data/sports/wallet_mirror_sniper_dry_run.csv"
GATE_GRID = REPO / "data/sports/wallet_mirror_gate_bucket.json"
GATE_FINO = REPO / "data/sports/wallet_mirror_gate_bucket_fino.json"
OUT_JSON = REPO / "data/sports/wallet_mirror_concentracion.json"

TOP1_WALLET_ALERTA_PCT = 30.0
TOP1_MERCADO_ALERTA_PCT = 20.0


def _buckets_confirmados() -> list[dict]:
    """[{categoria, tipo, lo, hi, veredicto, fuente}, ...] de cualquier
    bucket bueno_confirmado/malo_confirmado en cualquiera de las 2
    fuentes (grid fijo + ventana fina)."""
    out = []
    if GATE_GRID.exists():
        d = json.loads(GATE_GRID.read_text(encoding="utf-8"))
        for tupla_str, buckets in d.items():
            categoria, tipo = tupla_str.split("#")
            for b, info in buckets.items():
                if info.get("veredicto") in ("bueno_confirmado", "malo_confirmado"):
                    out.append({"categoria": categoria, "tipo": tipo,
                                "lo": float(b), "hi": float(b) + 0.05,
                                "veredicto": info["veredicto"], "fuente": "grid_fijo"})
    if GATE_FINO.exists():
        d = json.loads(GATE_FINO.read_text(encoding="utf-8"))
        for tupla_str, info in d.items():
            categoria, tipo = tupla_str.split("#")
            out.append({"categoria": categoria, "tipo": tipo,
                        "lo": info["lo"], "hi": info["hi"],
                        "veredicto": info["veredicto"], "fuente": "ventana_fina"})
    return out


def analizar(categoria: str, tipo: str, lo: float, hi: float) -> dict | None:
    filas = []
    with open(DRY_RUN, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r.get("categoria") != categoria or r.get("tipo") != tipo:
                continue
            try:
                ask = float(r["mejor_ask_mirror"])
            except (TypeError, ValueError, KeyError):
                continue
            if not (lo <= ask < hi):
                continue
            filas.append(r)
    n = len(filas)
    if n == 0:
        return None

    por_wallet = Counter(r["wallet"] for r in filas)
    por_mercado = Counter(r["condition_id"] for r in filas)
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
        "top1_wallet_pct": top1_wallet_pct,
        "top1_mercado_pct": top1_mercado_pct,
        "alerta_wallet": top1_wallet_pct > TOP1_WALLET_ALERTA_PCT,
        "alerta_mercado": top1_mercado_pct > TOP1_MERCADO_ALERTA_PCT,
    }


def main() -> int:
    buckets = _buckets_confirmados()
    if not buckets:
        print("Sin buckets bueno_confirmado/malo_confirmado todavía -- nada que auditar")
        return 0

    resultado = {"generado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "buckets": {}}
    for b in buckets:
        clave = f"{b['categoria']}#{b['tipo']}[{b['lo']:.2f},{b['hi']:.2f})#{b['fuente']}"
        r = analizar(b["categoria"], b["tipo"], b["lo"], b["hi"])
        if r is None:
            continue
        r["veredicto_gate"] = b["veredicto"]
        resultado["buckets"][clave] = r
        print(f"\n=== {clave} ({b['veredicto']}, n={r['n_senales']}) ===")
        print(f"nº wallets distintas: {r['n_wallets_distintas']} | nº mercados distintos: {r['n_mercados_distintos']}")
        for w in r["top5_wallets"]:
            print(f"  {w['wallet']}: {w['n']} ({w['pct']}%)")
        if r["alerta_wallet"]:
            print(f"⚠️ concentración de wallet alta ({r['top1_wallet_pct']}%>{TOP1_WALLET_ALERTA_PCT}%) "
                  f"-- el edge medido puede depender de 1 sola wallet, no de smart money distribuido")
        if r["alerta_mercado"]:
            print(f"⚠️ concentración de mercado alta ({r['top1_mercado_pct']}%>{TOP1_MERCADO_ALERTA_PCT}%) "
                  f"-- posible sesgo a un evento concreto")

    OUT_JSON.write_text(json.dumps(resultado, ensure_ascii=False, indent=1), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
