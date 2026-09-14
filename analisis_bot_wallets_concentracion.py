#!/usr/bin/env python3
"""
analisis_bot_wallets_concentracion.py -- 14-Sep, petición explícita Javi
tras cerrar (dejar en observación, nunca "cerrar" -- ver
feedback_nunca_cerrar_candidatas_dejar_cogiendo_n_25ago) varios buckets
de precio bajo (0.00-0.30) de la familia P-GALLINA
(SNIPER/DISPERSO/WEEKLY_TEMPRANO/WEEKLY_TARDIO) por concentración de
wallet: hasta hoy, comprobar top1-wallet% de un bucket exigía escribir
una consulta ad-hoc cada vez (mismo patrón que ya se automatizó para
WALLET_MIRROR con `analisis_wallet_mirror_concentracion.py` y para
Sports con `analisis_sports_wallet_mirror_concentracion.py`) -- este
script cierra el mismo hueco para bot_wallets.

A diferencia de la versión WALLET_MIRROR (que solo audita las tuplas ya
en pares_permitidos_live), este audita TODO bucket bueno_confirmado o
malo_confirmado de `bot_wallets_gate_bucket.json` -- live o candidato --
por (arquetipo,activo,marco,bucket_precio), reutilizando el mismo CSV
fuente (`dispersed_bot_executor_dryrun.csv`) que ya usa el ejecutor
DRY_RUN para medir fill-ability. Así cualquier propuesta de promoción
(por mí o por Javi) tiene el número de concentración fresco sin
recalcularlo a mano.

Solo lectura -- reporta, no vetea ni pausa nada (a diferencia de
_veto_fillable() en gate_bucket_propio.py, que SÍ está conectado al
camino de dinero real; conectar este chequeo de la misma forma es un
paso APARTE, deliberado, pendiente de decisión). Salida:
data/shadow/bot_wallets_concentracion.json.
"""
import csv
import json
import math
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
DRY_RUN = REPO / "data/shadow/dispersed_bot_executor_dryrun.csv"
GATE = REPO / "data/shadow/bot_wallets_gate_bucket.json"
OUT_JSON = REPO / "data/shadow/bot_wallets_concentracion.json"

TOP1_WALLET_ALERTA_PCT = 30.0
TOP1_MERCADO_ALERTA_PCT = 20.0
STEP = 0.05


def _bucket(precio: float) -> str:
    return f"{math.floor(precio / STEP + 1e-9) * STEP:.2f}"


def _buckets_confirmados() -> list[tuple[str, str, str, str, str]]:
    """[(arquetipo, activo, marco, bucket_str, veredicto), ...] de
    cualquier bucket con evidencia (bueno_confirmado/malo_confirmado) en
    bot_wallets_gate_bucket.json."""
    if not GATE.exists():
        return []
    d = json.loads(GATE.read_text(encoding="utf-8"))
    out = []
    for clave, tabla in d.items():
        if not isinstance(tabla, dict) or "#" not in clave:
            continue
        arquetipo, resto = clave.split("#", 1)
        if "#" not in resto:
            continue
        activo, marco = resto.split("#", 1)
        for b, info in tabla.items():
            if not isinstance(info, dict):
                continue
            v = info.get("veredicto")
            if v in ("bueno_confirmado", "malo_confirmado"):
                out.append((arquetipo, activo, marco, b, v))
    return out


def _indexar_dry_run() -> dict[tuple, list[dict]]:
    """Una sola pasada del CSV (2.6M+ filas) -- indexar por
    (arquetipo,activo,marco,bucket_str) en vez de releer el fichero
    entero por cada bucket confirmado (decenas de veces, cada una O(n))
    era demasiado lento (verificado: >2min sin terminar el primer
    bucket)."""
    idx: dict[tuple, list[dict]] = defaultdict(list)
    with open(DRY_RUN, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            try:
                bp = float(r.get("bucket_precio", ""))
            except (TypeError, ValueError):
                continue
            clave = (r.get("arquetipo"), r.get("activo"), r.get("marco"), f"{bp:.2f}")
            idx[clave].append(r)
    return idx


def analizar(idx: dict, arquetipo: str, activo: str, marco: str, bucket_str: str) -> dict | None:
    filas = idx.get((arquetipo, activo, marco, bucket_str), [])
    n = len(filas)
    if n == 0:
        return None

    por_wallet = Counter(r.get("wallet", "") for r in filas)
    por_mercado = Counter(r.get("market_slug", "") for r in filas)
    top1_wallet, top1_wallet_n = por_wallet.most_common(1)[0]
    top1_mercado, top1_mercado_n = por_mercado.most_common(1)[0]
    top1_wallet_pct = round(100 * top1_wallet_n / n, 1)
    top1_mercado_pct = round(100 * top1_mercado_n / n, 1)

    return {
        "n_senales": n,
        "n_wallets_distintas": len(por_wallet),
        "n_mercados_distintos": len(por_mercado),
        "top1_wallet": top1_wallet, "top1_wallet_pct": top1_wallet_pct,
        "top1_mercado_pct": top1_mercado_pct,
        "alerta_wallet": top1_wallet_pct > TOP1_WALLET_ALERTA_PCT,
        "alerta_mercado": top1_mercado_pct > TOP1_MERCADO_ALERTA_PCT,
    }


def main() -> int:
    combos = _buckets_confirmados()
    if not combos:
        print("Sin buckets confirmados en bot_wallets_gate_bucket.json -- nada que auditar")
        return 0

    idx = _indexar_dry_run()
    resultado = {"generado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "buckets": {}}
    n_alertas = 0
    for arquetipo, activo, marco, b, veredicto in sorted(set(combos)):
        r = analizar(idx, arquetipo, activo, marco, b)
        clave = f"{arquetipo}#{activo}#{marco}#{b}"
        if r is None:
            continue
        r["veredicto_gate"] = veredicto
        resultado["buckets"][clave] = r
        marca = ""
        if r["alerta_wallet"]:
            marca = f" ⚠️ ALERTA wallet {r['top1_wallet_pct']}%>{TOP1_WALLET_ALERTA_PCT}%"
            n_alertas += 1
        print(f"{clave} [{veredicto}] n={r['n_senales']} wallets={r['n_wallets_distintas']} "
              f"top1_wallet={r['top1_wallet_pct']}% top1_mercado={r['top1_mercado_pct']}%{marca}")

    print(f"\n{n_alertas} bucket(s) con alerta de concentración de wallet (>{TOP1_WALLET_ALERTA_PCT}%) "
          f"de {len(resultado['buckets'])} auditados")
    OUT_JSON.write_text(json.dumps(resultado, ensure_ascii=False, indent=1), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
