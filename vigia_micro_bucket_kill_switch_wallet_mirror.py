#!/usr/bin/env python3
"""
vigia_micro_bucket_kill_switch_wallet_mirror.py — cortacircuitos de dinero
real sobre el veto de micro-bucket de WALLET_MIRROR (wallet_mirror_gate_
bucket.py). Mismo mecanismo EXACTO que vigia_micro_bucket_kill_switch.py
(05-Ago) aplicado a la familia paralela de gate que usa WALLET_MIRROR
(evaluar(tipo, activo, marco, ask, jugada_grande), API distinta a
gate_bucket_propio.evaluar(tupla_str, py) -- por eso vive en su propio
fichero en vez de fundirse en el original).

Origen (24-Ago, petición explícita Javi tras revisar el kill switch
original: "sigue con el hueco de WALLET_MIRROR en el kill-switch, mismo
patrón que para el resto"): las 6 tuplas WALLET_MIRROR mueven dinero real
desde 10/11/12-Ago y no tenían NINGÚN backstop -- ni este mecanismo, ni
override manual (arreglado hoy mismo en wallet_mirror_gate_bucket.py).

Requiere que trades.csv tenga "grande=0|1" en notas (añadido hoy en
wallet_mirror_executor_dryrun.py, commit del mismo día) -- trades
anteriores a ese cambio no llevan el dato y se excluyen (fail-closed: sin
jugada_grande no se puede reconstruir la clave exacta del gate, mejor no
vigilar ese trade que vigilarlo mal). El bucket se calcula sobre
signal_ask (columna propia de trades.csv, MISMO valor que se pasó a
wmgb.evaluar() en el momento de la decisión real -- no entry_price, que
ya incluye slippage de fill).

Mecanismo: agrupa trades reales CERRADOS de WALLET_MIRROR por
(tipo,activo,marco,grande,bucket). Si un bucket que el gate dice
"bueno_confirmado" lleva n>=3 trades reales con PnL neto agregado
NEGATIVO, escribe override en data/live/wallet_mirror_gate_bucket_
override.json (gana sobre cualquier otro veredicto) + aviso Telegram
(latch, una vez por clave+bucket).

Cron/scheduler: consolidado en vigias_frecuentes_fase0.py junto al resto
de vigías de micro-bucket, mismo intervalo (1800s).
"""
import csv
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from scipy.stats import binom

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

import wallet_mirror_gate_bucket as wmgb

TRADES = REPO / "data/live/trades.csv"
OVERRIDE_PATH = wmgb.OVERRIDE_PATH
LATCH = REPO / "data/live/vigia_micro_bucket_kill_switch_wallet_mirror_latch.json"
STEP = 0.05
N_MIN_ALERTA = 5
FEE = 0.07  # mismo FEE_RATE_TAKER_CRYPTO que el resto del proyecto (CLAUDE.md P21)
# 07-Sep (Javi, tras el falso positivo real de SEGUIR#BTC#15min#0#0.80,
# n=3, PnL=-0,61€ -- "pierde dinero porque perdemos todo el stake, pero
# ganamos en general"): el trigger anterior (PnL agregado<0 con n>=3) no
# distingue ruido de payout asimétrico (perder SIEMPRE cuesta -1.0, ganar
# cuesta solo gross_win -- en buckets de precio alto tipo [0.80,0.85) el
# breakeven ya exige hit-rate ~82%, así que CUALQUIER único fallo entre
# 3-4 trades tira el agregado a negativo aunque el hit-rate real siga
# igual o por encima del breakeven) de una señal genuinamente rota.
# Verificado con los datos reales de esta alerta: con n=3 hits=2 el
# p-valor exacto es 0,44 (nada sorprendente, pura varianza); con el 4º
# trade ya resuelto (n=4 hits=3) el agregado ya es POSITIVO. Fix: test
# binomial de una cola contra el hit-rate de breakeven del propio bucket
# (punto medio, mismo precio que ya usa evaluar() más abajo) en vez de
# comparar el PnL en euros -- dispara solo si el resultado observado es
# estadísticamente sorprendente dado ese breakeven, no por la asimetría
# de payout de una apuesta binaria.
P_MAX_ALERTA = 0.15  # más laxo que el 0.05 estándar del proyecto -- es un
# cortacircuito de protección rápida de dinero real, no un gate de
# promoción; prefiere pecar de precavido (más falsos positivos que un
# gate riguroso) sobre dejar sangrar una tupla realmente rota.


def _breakeven_hitrate(ask: float) -> float:
    """Hit-rate p* tal que EV neto=0 a este ask (mismo FEE/fórmula que
    wmgb.pnl_neto): p*·gross_win·(1-FEE) - (1-p*)·1 = 0."""
    gross_win = (1 - ask) / ask
    return 1.0 / (1.0 + gross_win * (1 - FEE))

_RE_NOTAS = re.compile(r"tipo=(SEGUIR|FADE)\s+grande=([01])")


def _parsear_notas(notas: str):
    """(tipo, jugada_grande) desde 'wallet_mirror wallet=0x... tipo=SEGUIR
    grande=1', o (None, None) si el trade es anterior al 24-Ago (sin
    'grande=') -- fail-closed, se excluye en vez de asumir."""
    m = _RE_NOTAS.search(notas or "")
    if not m:
        return None, None
    return m.group(1), m.group(2) == "1"


def main() -> int:
    from shadow_digest import enviar_telegram

    try:
        vistos = json.loads(LATCH.read_text()) if LATCH.exists() else {}
    except Exception:
        vistos = {}

    try:
        override = json.loads(OVERRIDE_PATH.read_text()) if OVERRIDE_PATH.exists() else {}
    except Exception:
        override = {}

    por_clave_bucket: dict[str, list[float]] = {}
    n_sin_grande = 0
    if TRADES.exists():
        with open(TRADES, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if row.get("status") != "CLOSED" or row.get("strategy") != "WALLET_MIRROR":
                    continue
                tipo, grande = _parsear_notas(row.get("notas", ""))
                if tipo is None:
                    n_sin_grande += 1
                    continue
                try:
                    ask = float(row["signal_ask"])
                    pnl = float(row["pnl_neto_eur"])
                except Exception:
                    continue
                activo, marco = row.get("subtype", "#").split("#", 1) if "#" in row.get("subtype", "") else (row.get("subtype", ""), "")
                clave_str = f"{tipo}#{activo}#{marco}#{'1' if grande else '0'}"
                b = wmgb.bucket(ask)
                clave_bucket = f"{clave_str}#{b:.2f}"
                por_clave_bucket.setdefault(clave_bucket, []).append(pnl)

    alertas = []
    nuevos_override = {}
    for clave_bucket, pnls in por_clave_bucket.items():
        n = len(pnls)
        if n < N_MIN_ALERTA:
            continue
        pnl_total = sum(pnls)
        if pnl_total >= 0:
            continue

        clave_str, b_str = clave_bucket.rsplit("#", 1)
        tipo, activo, marco, grande_str = clave_str.split("#")
        b = float(b_str)
        veredicto = wmgb.evaluar(tipo, activo, marco, b + STEP / 2, grande_str == "1")["veredicto"]
        if veredicto != "bueno_confirmado":
            continue  # ya vetado o sin_concluir -- el gate ya protege, no hace falta el kill switch

        # Test binomial de una cola contra el breakeven del bucket (ver
        # docstring arriba) -- no basta con "el agregado en € es negativo",
        # eso lo garantiza casi cualquier bucket de precio alto con n bajo
        # por la propia asimetría del payout binario.
        hits = sum(1 for p in pnls if p > 0)
        p0 = _breakeven_hitrate(b + STEP / 2)
        p_valor = float(binom.cdf(hits, n, p0))
        if p_valor >= P_MAX_ALERTA:
            continue  # ruido de muestra pequeña, no evidencia real contra el gate

        ya_override = clave_bucket in override
        if clave_bucket in vistos and ya_override:
            continue

        alertas.append((clave_bucket, n, pnl_total, hits, p_valor))
        if not ya_override:
            nuevos_override[clave_bucket] = {
                "motivo": f"kill_switch automático: {n} trades reales en este bucket ({hits} aciertos, "
                          f"breakeven≈{p0:.0%}, p={p_valor:.3f}), PnL neto agregado {pnl_total:+.2f}€, "
                          f"pese a veredicto bueno_confirmado",
                "desde": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            }
        vistos[clave_bucket] = {"n": n, "pnl_total": round(pnl_total, 2), "hits": hits, "p_valor": round(p_valor, 4)}

    print(f"[vigia_micro_bucket_kill_switch_wallet_mirror] {len(por_clave_bucket)} celdas con n>=1, "
          f"{n_sin_grande} trades sin 'grande=' excluidos, {len(alertas)} bucket(s) confirmado(s)-pero-sangrando")

    if nuevos_override:
        override.update(nuevos_override)
        OVERRIDE_PATH.write_text(json.dumps(override, ensure_ascii=False, indent=1))
        print(f"[vigia_micro_bucket_kill_switch_wallet_mirror] 🚨 override AUTOMÁTICO escrito para: "
              f"{list(nuevos_override.keys())}")

    if alertas:
        detalle = "\n".join(
            f"  {clave}: n={n} hits={hits} PnL real={pnl:+.2f}€ p={p_valor:.3f}"
            for clave, n, pnl, hits, p_valor in alertas
        )
        msg = (
            "🚨🔒 KILL SWITCH micro-bucket WALLET_MIRROR: el gate confirma 'bueno_confirmado' pero "
            "el dinero real está perdiendo ahí:\n"
            f"{detalle}\nOverride escrito, bloqueado hasta revisión."
        )
        enviar_telegram(msg)

    LATCH.write_text(json.dumps(vistos, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
