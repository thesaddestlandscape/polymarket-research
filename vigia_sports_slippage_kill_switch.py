#!/usr/bin/env python3
"""vigia_sports_slippage_kill_switch.py — mismo mecanismo EXACTO que
vigia_slippage_kill_switch.py (cripto, 29-Jul) aplicado a
`pares_permitidos_live` de config_live_sports.json (CATEGORIA#TIPO#lo:hi).

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


def _tuplas_live() -> list[tuple[str, str, float, float]]:
    try:
        cfg = json.loads(CONFIG_LIVE.read_text(encoding="utf-8"))
    except Exception:
        return []
    out = []
    for entrada in cfg.get("pares_permitidos_live", []):
        partes = entrada.split("#")
        if len(partes) != 3:
            continue
        categoria, tipo, ventana = partes
        try:
            lo_str, hi_str = ventana.split(":")
            out.append((categoria, tipo, float(lo_str), float(hi_str)))
        except (ValueError, TypeError):
            continue
    return out


def _slips_tupla(categoria: str, tipo: str, lo: float, hi: float) -> list[float]:
    slips = []
    if not TRADES.exists():
        return slips
    with open(TRADES, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("categoria") != categoria or row.get("tipo") != tipo or row.get("status") != "CLOSED":
                continue
            try:
                entry = float(row.get("entry_price") or 0)
            except (TypeError, ValueError):
                continue
            if not (lo <= entry < hi):
                continue
            raw = row.get("slip_real", "")
            if raw not in ("", None):
                try:
                    slips.append(float(raw))
                except (TypeError, ValueError):
                    pass
    return slips


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

    tuplas = _tuplas_live()
    _log(f"tuplas live a revisar: {len(tuplas)}")

    cambios = False
    for categoria, tipo, lo, hi in tuplas:
        clave = f"{categoria}#{tipo}#{lo:.2f}:{hi:.2f}"
        slips = _slips_tupla(categoria, tipo, lo, hi)
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
