#!/usr/bin/env python3
"""vigia_micro_bucket_kill_switch.py — cortacircuitos de dinero real sobre
el veto de micro-bucket (gate_bucket_propio.py).

Origen (05-Ago, petición explícita Javi tras el incidente del mismo día
con el veto de FAVORITO_CONFIRMADO -- ver feedback_lookahead_bias_
precio_final_no_es_edge_05ago): "asegúrate que el mecanismo autoaprendiente
tenga un backup que lo proteja siempre y no nos haga perder pasta, ni
cagarla". El mecanismo (gate_bucket_propio.py + su extensión de validación
externa) puede confirmar un bucket como bueno_confirmado a partir de un
análisis con un fallo metodológico no detectado -- ya pasó una vez el
mismo día. Este vigía es el backup: compara el veredicto CONTRA el dinero
real, no se fía solo del análisis.

Mecanismo: para cada tupla live con veto de micro-bucket activo, agrupa
los trades reales CERRADOS (trades.csv) por el mismo bucket de 0.05 que
usa gate_bucket_propio.evaluar(). Si un bucket que el gate dice
"bueno_confirmado" (por dato propio O por la extensión de validación
externa) lleva n>=3 trades reales con PnL neto agregado NEGATIVO, se
considera un bucket confirmado por el análisis pero desmentido por la
realidad -- dispara:
  1. Aviso por Telegram siempre (latch: una vez por tupla+bucket, se
     resetea solo si el bucket deja de estar en gate_bucket_propio_
     override.json).
  2. Escribe un override AUTOMÁTICO en data/live/gate_bucket_propio_
     override.json (fuerza malo_confirmado ahí, gana sobre cualquier
     otro veredicto -- ver evaluar() en gate_bucket_propio.py) -- para
     esa combinación tupla+bucket exacta, no toda la tupla ni el resto
     del sistema. Reversible a mano (borrar la entrada del override) tras
     revisar por qué el análisis se equivocó.

Umbral deliberadamente bajo (n>=3) -- mismo espíritu que los circuit
breakers de live_stake.py: proteger primero, investigar después. Un
bucket recién confirmado con muy poco volumen real puede activarlo por
varianza normal -- el aviso de Telegram deja claro que es un umbral
exploratorio, no una sentencia definitiva, y queda registrado para
revisión humana.

Cron sugerido (frecuente, el dinero real no espera a mañana):
  */30 * * * * flock -n /tmp/vigia_micro_bucket_kill_switch.lock /root/polymarket-research/.venv/bin/python /root/polymarket-research/vigia_micro_bucket_kill_switch.py >> /root/polymarket-research/logs/vigia_micro_bucket_kill_switch.log 2>&1
"""
import csv
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

import gate_bucket_propio as gbp

TRADES = REPO / "data/live/trades.csv"
CONFIG_LIVE = REPO / "data/live/config_live.json"
OVERRIDE_PATH = gbp.OVERRIDE_PATH
LATCH = REPO / "data/live/vigia_micro_bucket_kill_switch_latch.json"
STEP = 0.05
N_MIN_ALERTA = 3


def cargar_tuplas_vigiladas() -> list[tuple[str, str, str]]:
    """24-Ago (hallazgo real, barrido de salud a petición de Javi: "no hay
    más margen para cagadas"): esta lista era ESTÁTICA desde el 05-Ago --
    de las 10 tuplas en pares_permitidos_live hoy, solo cubría 3. Las 6
    tuplas WALLET_MIRROR (dinero real desde 10/11/12-Ago) y
    BALLENAS_CONFIRMADAS_15M#ETH#15min (dinero real desde 20-Ago) llevaban
    semanas sin ningún backstop de kill-switch -- si su gate confirmara un
    bucket malo por un fallo metodológico (el mismo tipo de incidente que
    motivó crear este vigía el 05-Ago), nada lo habría detectado.

    Ahora se auto-descubre desde config_live.json::pares_permitidos_live,
    mismo patrón que cargar_tuplas_live() en analisis_gate_bucket_propio_
    28jul.py -- nunca vuelve a quedar desactualizada sola. Excluye
    WALLET_MIRROR a propósito: su veto vive en wallet_mirror_gate_bucket.py
    (evaluar(tipo, activo, marco, ask, jugada_grande), firma DISTINTA a
    gate_bucket_propio.evaluar(tupla_str, py)) y trades.csv no guarda
    jugada_grande por trade -- necesita su propio kill-switch con un join
    contra wallet_mirror_executor_dryrun.csv para recuperar ese dato, no
    algo para improvisar aquí. Ver idea_kill_switch_wallet_mirror_pendiente_
    24ago en memoria -- pendiente, no resuelto por esta fix."""
    try:
        pares = json.loads(CONFIG_LIVE.read_text(encoding="utf-8")).get("pares_permitidos_live", [])
    except Exception:
        return []
    out = []
    for t in pares:
        partes = t.split("#")
        if len(partes) != 4 or partes[0] == "WALLET_MIRROR":
            continue
        strategy, activo, marco, decision = partes
        out.append((strategy, f"{activo}#{marco}", decision))
    return out


def _bucket(py: float) -> float:
    import math
    # 06-Ago fix: +1e-9 evita mal-clasificar precios EXACTOS en un múltiplo
    # de STEP al bucket inferior (coma flotante) -- ver idea_bug_bucketing_
    # float_precision_micro_buckets_06ago.
    return round(math.floor(py / STEP + 1e-9) * STEP, 4)


def _py_real(direction: str, entry_price: float) -> float:
    """Mismo criterio que usan los ejecutores al llamar a gate_bucket_
    propio.evaluar(): py es SIEMPRE el precio YES. Para BUY_NO,
    entry_price es el precio pagado por NO -- py = 1 - entry_price."""
    return 1 - entry_price if direction == "BUY_NO" else entry_price


def main() -> int:
    from shadow_digest import enviar_telegram

    TUPLAS_VIGILADAS = cargar_tuplas_vigiladas()

    try:
        vistos = json.loads(LATCH.read_text()) if LATCH.exists() else {}
    except Exception:
        vistos = {}

    try:
        override = json.loads(OVERRIDE_PATH.read_text()) if OVERRIDE_PATH.exists() else {}
    except Exception:
        override = {}

    trades_por_tupla = {t: [] for t in TUPLAS_VIGILADAS}
    if TRADES.exists():
        with open(TRADES, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if row.get("status") != "CLOSED":
                    continue
                clave = (row.get("strategy"), row.get("subtype"), row.get("direction"))
                if clave not in trades_por_tupla:
                    continue
                try:
                    entry = float(row["entry_price"])
                    pnl = float(row["pnl_neto_eur"])
                except Exception:
                    continue
                trades_por_tupla[clave].append((entry, pnl))

    alertas = []
    nuevos_override = {}
    for strategy, subtype, direction in TUPLAS_VIGILADAS:
        tupla_str = f"{strategy}#{subtype}#{direction}"
        trades = trades_por_tupla[(strategy, subtype, direction)]
        por_bucket = {}
        for entry, pnl in trades:
            py = _py_real(direction, entry)
            b = _bucket(py)
            por_bucket.setdefault(b, []).append(pnl)

        for b, pnls in por_bucket.items():
            n = len(pnls)
            if n < N_MIN_ALERTA:
                continue
            pnl_total = sum(pnls)
            if pnl_total >= 0:
                continue  # bucket real en positivo -- nada que hacer

            py_representativo = b + STEP / 2
            veredicto = gbp.evaluar(tupla_str, py_representativo)["veredicto"]
            if veredicto != "bueno_confirmado":
                continue  # ya vetado o sin_concluir -- el gate ya está protegiendo, no hace falta el kill switch

            clave_latch = f"{tupla_str}#{b:.2f}"
            clave_override = f"{tupla_str}#{b:.2f}"
            ya_override = clave_override in override
            if clave_latch in vistos and ya_override:
                continue  # ya avisado y ya bloqueado -- no repetir

            alertas.append((tupla_str, b, n, pnl_total))
            if not ya_override:
                nuevos_override[clave_override] = {
                    "motivo": f"kill_switch automático: {n} trades reales en este bucket, "
                              f"PnL neto agregado {pnl_total:+.2f}€, pese a veredicto bueno_confirmado",
                    "desde": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                }
            vistos[clave_latch] = {"n": n, "pnl_total": round(pnl_total, 2)}

    print(f"[vigia_micro_bucket_kill_switch] {len(TUPLAS_VIGILADAS)} tuplas vigiladas, "
          f"{len(alertas)} bucket(s) confirmado(s)-pero-sangrando")

    if nuevos_override:
        override.update(nuevos_override)
        OVERRIDE_PATH.write_text(json.dumps(override, ensure_ascii=False, indent=1))
        print(f"[vigia_micro_bucket_kill_switch] 🚨 override AUTOMÁTICO escrito para: "
              f"{list(nuevos_override.keys())}")

    if alertas:
        detalle = "\n".join(
            f"  {tupla}: bucket [{b:.2f},{b+STEP:.2f}) n={n} PnL real={pnl:+.2f}€"
            for tupla, b, n, pnl in alertas
        )
        msg = (
            "🚨🔒 KILL SWITCH micro-bucket: el gate confirma 'bueno_confirmado' pero "
            "el dinero real está perdiendo ahí:\n"
            f"{detalle}\n"
            "Override automático aplicado (data/live/gate_bucket_propio_override.json) -- "
            "esa combinación tupla+bucket queda vetada YA, sin esperar a nadie. "
            "Revisar por qué el gate confirmó esto y si hace falta corregir la metodología "
            "(mismo patrón que el incidente de esta sesión) antes de quitar el override a mano."
        )
        ok = enviar_telegram(msg)
        print(f"[vigia_micro_bucket_kill_switch] aviso enviado (telegram={ok})")

    LATCH.write_text(json.dumps(vistos, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"[vigia_micro_bucket_kill_switch] ERROR {type(e).__name__}: {e}")
        sys.exit(0)
