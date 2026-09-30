#!/usr/bin/env python3
"""resolver_bot_wallets_gate_bucket_lote.py -- resolver POR LOTES de bot_wallets_gate_bucket_fase0.csv (30-Sep).

Por qué existe: `bot_wallets_gate_bucket_fase0.py --resolver` ordenaba los slugs pendientes alfabéticamente y
resolvía los 150 primeros, uno a uno. La cabeza de la cola se llenó de slugs que nunca resuelven
("bitcoin-above-..." y similares) y de BNB/BTC, y el resto quedó en inanición: desde el 28-Sep ETH 0 de 6.673
filas resueltas, SOL 0 de 4.257, XRP 0 de 2.912 (34 % resuelto en total). El gate de SNIPER/DISPERSO
(`bot_wallets_gate_bucket.json`, que decide dinero real) se calculaba sobre esa muestra.

Aquí: gamma `/markets?slug=...&closed=true` en lotes de 40 (todos los pendientes caben en ~2 min), sin tope que
pueda atascarse, y los slugs MÁS RECIENTES primero. Mismo candado y misma reescritura en streaming que el
resolver original; NO se toca bot_wallets_gate_bucket_fase0.py (lo importa la screen `observadores`: editarlo
la reinicia y se pierde el histórico ms en memoria). Lo que gamma no devuelva por lote queda para el camino
antiguo (`outcome_por_slug`), acotado y al final.
Cron: */10 (sustituye a `bot_wallets_gate_bucket_fase0.py --resolver`).
"""
import csv
import fcntl
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import requests

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
import bot_wallets_gate_bucket_fase0 as B  # noqa: E402
from wallet_mirror_tracker import GAMMA, UMBRAL_RESUELTO, outcome_por_slug  # noqa: E402

LOTE, MAX_SUELTOS = 40, 40


def _log(msg: str) -> None:
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _epoch(slug: str) -> int:
    m = re.search(r"-(\d{10})$", slug)
    return int(m.group(1)) if m else 0


def _por_lotes(slugs: list) -> dict:
    out, ses = {}, requests.Session()
    for k in range(0, len(slugs), LOTE):
        trozo = slugs[k:k + LOTE]
        try:
            r = ses.get(f"{GAMMA}/markets", timeout=20,
                        params=[("slug", s) for s in trozo] + [("closed", "true"), ("limit", str(LOTE))])
            if r.status_code != 200:
                continue
            for m in r.json() or []:
                pr, oc = m.get("outcomePrices"), m.get("outcomes")
                pr = json.loads(pr) if isinstance(pr, str) else pr
                oc = json.loads(oc) if isinstance(oc, str) else oc
                if not pr or not oc or len(pr) != len(oc):
                    continue
                for o, p in zip(oc, pr):
                    if float(p) >= UMBRAL_RESUELTO:
                        out[m["slug"]] = o
        except Exception as e:
            _log(f"lote {k // LOTE} falló: {type(e).__name__}")
    return out


def main() -> int:
    if not B.OUT.exists():
        return 0
    csv.field_size_limit(10 ** 8)
    ahora = datetime.now(timezone.utc).timestamp()
    with open(B.OUT, newline="", encoding="utf-8") as f:
        pend = {r["market_slug"] for r in csv.DictReader(f) if not r.get("outcome_real") and r.get("market_slug")}
    # solo lo que ya debería haber cerrado (los up/down llevan la apertura en el slug); más reciente primero
    con_fecha = sorted((s for s in pend if 0 < _epoch(s) < ahora - 120), key=_epoch, reverse=True)
    sin_fecha = sorted(s for s in pend if _epoch(s) == 0)
    # los slugs sin fecha (diarios, escaleras "bitcoin-above-...") son slugs de MERCADO: `/events?slug=` (camino
    # antiguo) no los encuentra nunca; `/markets?slug=&closed=true` sí, en cuanto cierran
    outcomes = _por_lotes(con_fecha + sin_fecha)
    for s in [x for x in sin_fecha if x not in outcomes][:MAX_SUELTOS]:   # camino antiguo, acotado y al final
        o = outcome_por_slug(s)
        if o is not None:
            outcomes[s] = o
    if not outcomes:
        _log(f"nada que resolver ({len(con_fecha)} con fecha, {len(sin_fecha)} sin fecha pendientes)")
        return 0
    lock_f = open(B.OUT_LOCK, "w")
    try:
        fcntl.flock(lock_f, fcntl.LOCK_EX)
        marca = datetime.now(timezone.utc).isoformat(timespec="seconds")

        def _resolver(r: dict) -> bool:
            if r.get("outcome_real"):
                return False
            o = outcomes.get(r.get("market_slug"))
            if o is None:
                return False
            r["outcome_real"], r["acierto"], r["resolved_ts"] = o, ("1" if o == r.get("lado_wallet") else "0"), marca
            return True
        n = B.reescribir_csv_streaming(B.OUT, B.COLUMNS, _resolver)
    finally:
        fcntl.flock(lock_f, fcntl.LOCK_UN)
        lock_f.close()
    _log(f"resueltas: {n} filas ({len(outcomes)} mercados; pendientes antes: {len(con_fecha)} con fecha, {len(sin_fecha)} sin fecha)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
