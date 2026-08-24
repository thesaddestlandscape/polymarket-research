#!/usr/bin/env python3
"""
vigia_wallet_mirror_degradacion.py -- P24, punto 4 del barrido de huecos
de Wallet Mirror (13-Ago, petición explícita Javi).

Hueco real: `wallet_edge_score_por_activo_marco.json` valida cada wallet
con su HISTÓRICO completo (n>=30, sig_bhfdr), regenerado cada hora por
wallet_edge_tracker.py -- pero es un agregado que crece sin parar. Si una
wallet concreta deja de acertar (cambia de estrategia, pierde su ventaja
informativa, o simplemente empieza a ser copiada por más gente y su edge
se satura), el agregado histórico tarda mucho en arrastrarse hacia abajo
-- con miles de trades históricos, 20-30 fallos recientes apenas mueven
la media. Nada vigilaba el rendimiento RECIENTE de cada wallet usada de
verdad por wallet_mirror_executor_dryrun.py (dinero real).

Método: para cada wallet SEGUIR ya validada, compara su hit-rate
histórico (`v['hit']`, del JSON) contra el hit-rate de sus últimos
N_RECIENTE trades resueltos en wallet_mirror_sniper_dry_run.csv (fuente
con resolución de outcome completa, el CSV que de verdad escribe
wallet_mirror_sniper.py hoy -- wallet_mirror_dry_run.csv lleva muerto
desde el 04-Ago, ver fix 13-Ago).
Alerta si el límite SUPERIOR del Wilson90% reciente ya no alcanza el
hit histórico menos un margen -- es decir, incluso en el escenario más
favorable dentro del intervalo, el rendimiento reciente es peor.

Solo alerta -- no toca wallet_edge_score_por_activo_marco.json ni la
lista que consulta cargar_wallets_validadas(). 13-Ago: el filtro real
para dinero real vive ahora en wallet_mirror_tracker.py::
wallets_operativas_recientes() (mismo criterio, convertido de alerta a
exclusión fail-closed para wallet_mirror_executor_dryrun.py) -- esta
vigía sigue avisando por Telegram en paralelo, mismo patrón que
vigia_log_growth.py/vigia_slippage_kill_switch.py.

Cron sugerido: diario, mismo bloque que el resto de vigías de análisis.
"""
import csv
import json
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from analisis_gate_riguroso import wilson_ci  # noqa: E402
from wallet_mirror_tracker import MARCO_A_ACTIVITY  # noqa: E402

WALLET_SCORES = REPO / "data/shadow/wallet_edge_score_por_activo_marco.json"
# 13-Ago (fix, mismo bug encontrado diseñando wallets_operativas_recientes()
# en wallet_mirror_tracker.py): wallet_mirror_dry_run.csv lleva muerto desde
# el 04-Ago -- wallet_mirror_tracker.py::main() dejó de ser el proceso real,
# sustituido por wallet_mirror_sniper.py, que escribe a su propio CSV. Esta
# vigía llevaba desde su creación (13-Ago) leyendo un histórico "reciente"
# en realidad congelado hace 9+ días.
DRY_RUN = REPO / "data/shadow/wallet_mirror_sniper_dry_run.csv"
LATCH = REPO / "data/live/vigia_wallet_mirror_degradacion_latch.json"

N_MIN_VALIDACION = 30   # mismo umbral que cargar_wallets_validadas()
N_RECIENTE = 15         # ventana de trades más recientes a evaluar -- 25-Ago:
# sincronizado con wallet_mirror_tracker.py::N_RECIENTE_OPERAR (bajado de 18)
MARGEN_DEGRADACION_PP = 15  # caída (en puntos porcentuales) para alertar


def _log(msg: str) -> None:
    from datetime import datetime, timezone
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts}] {msg}", flush=True)


def _wallets_seguir() -> dict:
    try:
        datos = json.loads(WALLET_SCORES.read_text(encoding="utf-8"))
    except Exception:
        return {}
    out = {}
    for v in datos.values():
        if v.get("sig_bhfdr") and v.get("n", 0) >= N_MIN_VALIDACION and v.get("edge_pp", 0) > 0:
            w = (v.get("wallet") or "").lower()
            marco_csv = MARCO_A_ACTIVITY.get(v.get("marco"))
            if w and marco_csv:
                out[(w, v["activo"], marco_csv)] = v
    return out


def _historial_por_wallet() -> dict:
    hist = defaultdict(list)
    if not DRY_RUN.exists():
        return hist
    with open(DRY_RUN, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("tipo") != "SEGUIR" or row.get("acierto") not in ("0", "1"):
                continue
            clave = (row.get("wallet", ""), row.get("activo", ""), row.get("marco", ""))
            hist[clave].append((row.get("trade_timestamp", ""), int(row["acierto"])))
    for clave in hist:
        hist[clave].sort(key=lambda x: x[0])
    return hist


def main() -> int:
    from shadow_digest import enviar_telegram

    try:
        latch = json.loads(LATCH.read_text(encoding="utf-8")) if LATCH.exists() else {}
    except Exception:
        latch = {}

    wallets = _wallets_seguir()
    hist = _historial_por_wallet()
    _log(f"wallets SEGUIR validadas: {len(wallets)} | historial cargado: {len(hist)} claves")

    cambios = False
    for (w, activo, marco), info in wallets.items():
        aciertos = hist.get((w, activo, marco), [])
        if len(aciertos) < N_RECIENTE:
            continue
        recientes = [a for _, a in aciertos[-N_RECIENTE:]]
        k, n = sum(recientes), len(recientes)
        hit_reciente = 100 * k / n
        _, ci_hi = wilson_ci(k, n)
        ci_hi_pct = ci_hi * 100
        hit_hist = info["hit"] * 100
        clave = f"{w}#{activo}#{marco}"
        degradado = ci_hi_pct < (hit_hist - MARGEN_DEGRADACION_PP)
        avisado = latch.get(clave, {}).get("avisado", False)

        _log(f"{clave}: hist={hit_hist:.1f}% reciente(n={n})={hit_reciente:.1f}% "
             f"Wilson90hi={ci_hi_pct:.1f}% {'DEGRADADA' if degradado else 'ok'}")

        if degradado and not avisado:
            msg = (
                f"📉 *Wallet Mirror -- wallet degradada* -- {clave}\n"
                f"Hit histórico validado: {hit_hist:.1f}%\n"
                f"Hit reciente (últimos {n} trades): {hit_reciente:.1f}% "
                f"(Wilson90% superior={ci_hi_pct:.1f}%)\n"
                f"El límite superior del intervalo reciente ya no alcanza el "
                f"histórico -- posible pérdida de ventaja de esta wallet. "
                f"Solo aviso, no se pausa nada automáticamente."
            )
            ok = enviar_telegram(msg)
            latch[clave] = {"avisado": True, "hit_hist": round(hit_hist, 1),
                             "hit_reciente": round(hit_reciente, 1), "n_reciente": n,
                             "telegram_ok": ok}
            cambios = True
            _log(f"aviso enviado {clave} (telegram={ok})")
        elif not degradado and avisado:
            latch[clave] = {"avisado": False}
            cambios = True
            _log(f"{clave}: recuperada, reseteando latch")

    if cambios:
        LATCH.write_text(json.dumps(latch, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"[vigia_wallet_mirror_degradacion] ERROR {type(e).__name__}: {e}")
        sys.exit(0)
