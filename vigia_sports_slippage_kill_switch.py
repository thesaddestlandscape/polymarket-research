#!/usr/bin/env python3
"""vigia_sports_slippage_kill_switch.py — mismo mecanismo EXACTO que
vigia_slippage_kill_switch.py (cripto, 29-Jul) aplicado a
`pares_permitidos_live` de config_live_sports.json (CATEGORIA#TIPO,
08-Sep: sin banda de precio -- ver sports_live_guard.py para el porqué).

08-Sep, /code-review sobre el rediseño de arriba: agregar por
categoria#tipo a secas (como se hizo en el primer intento) mezclaba
micro-buckets de precio DISTINTOS de una misma tupla -- CS#SEGUIR opera
en dos zonas ([0.45,0.50) desde 01-Sep y [0.25,0.30) desde 05-Sep) y un
slippage malo en una podía quedar diluido/oculto por la otra en el
agregado, violando CLAUDE.md pt.17 (desagregar SIEMPRE por micro-bucket
de precio). Corregido: se segmenta por bucket de 0.05 sobre el
`entry_price` REAL de cada trade (mismo grid que gate_bucket_propio.py
en cripto), no por ninguna banda de config -- así el chequeo sigue
siendo por micro-bucket exacto sin depender de una whitelist que puede
quedar desalineada con los buckets reales.

27-Ago noche (petición explícita Javi: auditoría de paridad de
funcionalidades cripto↔sports). Solo alerta, nunca pausa nada -- la
decisión sigue siendo de Javi.

Usa la columna `slip_real` de data/sports/trades.csv (añadida hoy mismo
en sports_live_trade.py::TRADES_COLS, ver también sports_wallet_mirror_
sniper.py::registrar_trade()).

Cron sugerido: diario, mismo bloque que el resto de vigías de sports.
"""
import csv
import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from sports_wallet_mirror_gate_bucket import bucket as _bucket  # único punto de verdad del bucketing (STEP=0.05)
from sports_live_guard import categorias_tipos_live as _categorias_tipos_live  # único punto de verdad de la whitelist

TRADES = REPO / "data/sports/trades.csv"
CONFIG_LIVE = REPO / "data/sports/config_live_sports.json"
LATCH = REPO / "data/sports/vigia_slippage_kill_switch_latch.json"

N_MIN = 15
Z_90 = 1.645
SLIPPAGE_ESTIMADO = 0.02  # mismo valor fallback que el hermano de cripto
MARGEN_RECUPERACION = 0.005


def _log(msg: str) -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts}] {msg}", flush=True)


def _slips_por_bucket() -> dict[tuple[str, str, float], list[float]]:
    """Agrupa slip_real por (categoria, tipo, bucket de 0.05 sobre
    entry_price) -- nunca por categoria#tipo agregado (CLAUDE.md pt.17,
    ver docstring del módulo)."""
    resultado: dict[tuple[str, str, float], list[float]] = {}
    if not TRADES.exists():
        return resultado
    permitidas = _categorias_tipos_live()
    with open(TRADES, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            categoria, tipo = row.get("categoria"), row.get("tipo")
            if (categoria, tipo) not in permitidas or row.get("status") != "CLOSED":
                continue
            try:
                entry = float(row.get("entry_price") or 0)
            except (TypeError, ValueError):
                continue
            bucket = _bucket(entry)
            raw = row.get("slip_real", "")
            if raw in ("", None):
                continue
            try:
                slip = float(raw)
            except (TypeError, ValueError):
                continue
            resultado.setdefault((categoria, tipo, bucket), []).append(slip)
    return resultado


def _media_ci90(vals: list[float]) -> tuple[float, float, float]:
    n = len(vals)
    media = sum(vals) / n
    if n < 2:
        return media, media, media
    var = sum((v - media) ** 2 for v in vals) / (n - 1)
    se = math.sqrt(var / n)
    return media, media - Z_90 * se, media + Z_90 * se


def main() -> int:
    from shadow_digest import enviar_telegram

    try:
        latch = json.loads(LATCH.read_text(encoding="utf-8")) if LATCH.exists() else {}
    except Exception:
        latch = {}

    por_bucket = _slips_por_bucket()
    _log(f"buckets (categoria,tipo,precio) a revisar: {len(por_bucket)}")

    cambios = False
    for (categoria, tipo, bucket), slips in sorted(por_bucket.items()):
        clave = f"{categoria}#{tipo}#{bucket:.2f}"
        n = len(slips)
        if n < N_MIN:
            _log(f"{clave}: n={n} < {N_MIN}, sin concluir")
            continue

        media, ci_lo, ci_hi = _media_ci90(slips)
        peor_que_asumido = ci_lo > SLIPPAGE_ESTIMADO
        estado = latch.get(clave, {})
        avisado = estado.get("avisado", False)

        _log(f"{clave}: n={n} slip_medio={media:+.4f} CI90%=[{ci_lo:+.4f},{ci_hi:+.4f}] "
             f"asumido={SLIPPAGE_ESTIMADO} {'⚠️ PEOR' if peor_que_asumido else 'ok'}")

        if peor_que_asumido and not avisado:
            msg = (
                f"🔻 *Slippage real peor de lo asumido (SPORTS)* — {clave}\n"
                f"n={n} trades reales cerrados\n"
                f"slip_real medio={media:+.4f}€ (CI90%=[{ci_lo:+.4f},{ci_hi:+.4f}])\n"
                f"asumido={SLIPPAGE_ESTIMADO:+.4f}€\n"
                f"El edge neto real de esta tupla es probablemente MENOR de lo que "
                f"el modelo asume — revisar manualmente, esto es solo un aviso."
            )
            enviar_telegram(msg, bot="sports")
            latch[clave] = {"avisado": True, "n": n, "slip_medio": round(media, 4)}
            cambios = True
        elif not peor_que_asumido and avisado and ci_hi < SLIPPAGE_ESTIMADO - MARGEN_RECUPERACION:
            latch[clave] = {"avisado": False, "n": n, "slip_medio": round(media, 4)}
            cambios = True

    if cambios:
        LATCH.write_text(json.dumps(latch, indent=2), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
