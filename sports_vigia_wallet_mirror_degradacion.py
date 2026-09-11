#!/usr/bin/env python3
"""
sports_vigia_wallet_mirror_degradacion.py -- port directo de
vigia_wallet_mirror_degradacion.py (cripto, 13-Ago) a sports/esports,
petición explícita Javi 18-Ago tras el repaso a fondo del Wallet Mirror
de sports: "lo que hay que mirar es el histórico como base, pero su hit
rate y pnl por trade reciente, porque el agregado histórico puede
esconder pérdidas recientes... desagregar siempre".

Mismo hueco que en cripto: `wallet_edge_score_por_categoria.json` valida
cada wallet con su HISTÓRICO completo -- si una wallet deja de acertar
(cambia de estrategia, su ventaja se satura, empieza a ser copiada), el
agregado histórico tarda en reflejarlo. Compara el hit-rate histórico
contra el de los últimos N_RECIENTE trades RESUELTOS en
sports_wallet_mirror_sniper_dry_run.csv.

Fail-safe por diseño: con el sniper recién desplegado (18-Ago), casi
ninguna wallet tendrá N_RECIENTE=20 trades resueltos todavía -- este
vigía simplemente no avisará de nada hasta que haya datos reales, sin
coste de mantenerlo desplegado desde ya (mismo razonamiento que crypto:
mejor tener la red de seguridad puesta desde el día 1 que añadirla
"cuando haga falta" y arriesgarse a olvidarla).

Solo alerta -- no toca wallet_edge_score_por_categoria.json ni pausa
nada. Separación estricta: solo lee/escribe data/sports/.

Cron sugerido: diario.
"""
import csv
import json
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from analisis_gate_riguroso import wilson_ci  # noqa: E402 -- reutilizado, mismo repo
from shadow_digest import enviar_telegram  # noqa: E402 -- reutilizado, mismo repo

DIR_SPORTS = REPO / "data" / "sports"
WALLET_SCORES = DIR_SPORTS / "wallet_edge_score_por_categoria.json"
DRY_RUN = DIR_SPORTS / "wallet_mirror_sniper_dry_run.csv"
LATCH = DIR_SPORTS / "vigia_wallet_mirror_degradacion_latch.json"

N_MIN_VALIDACION = 15   # mismo umbral que sports_wallet_edge_tracker.py (N_MIN)
N_RECIENTE = 20
MARGEN_DEGRADACION_PP = 15


def _log(msg: str) -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts}] {msg}", flush=True)


def _wallets_seguir() -> dict:
    if not WALLET_SCORES.exists():
        return {}
    try:
        datos = json.loads(WALLET_SCORES.read_text(encoding="utf-8"))
    except Exception:
        return {}
    out = {}
    for w in datos.get("wallets_validadas", []):
        if w.get("n", 0) >= N_MIN_VALIDACION and w.get("edge_pp", 0) > 0:
            wallet = (w.get("wallet") or "").lower()
            cat = w.get("categoria")
            if wallet and cat:
                out[(wallet, cat)] = w
    return out


def _historial_por_wallet() -> dict:
    hist = defaultdict(list)
    if not DRY_RUN.exists():
        return hist
    with open(DRY_RUN, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("tipo") != "SEGUIR" or row.get("acierto") not in ("0", "1"):
                continue
            clave = (row.get("wallet", ""), row.get("categoria", ""))
            hist[clave].append((row.get("trade_timestamp", ""), int(row["acierto"])))
    for clave in hist:
        hist[clave].sort(key=lambda x: x[0])
    return hist


def main() -> int:
    try:
        latch = json.loads(LATCH.read_text(encoding="utf-8")) if LATCH.exists() else {}
    except Exception:
        latch = {}

    wallets = _wallets_seguir()
    hist = _historial_por_wallet()
    _log(f"wallets SEGUIR validadas: {len(wallets)} | historial cargado: {len(hist)} claves")

    cambios = False
    for (w, categoria), info in wallets.items():
        aciertos = hist.get((w, categoria), [])
        if len(aciertos) < N_RECIENTE:
            continue
        recientes = [a for _, a in aciertos[-N_RECIENTE:]]
        k, n = sum(recientes), len(recientes)
        hit_reciente = 100 * k / n
        _, ci_hi = wilson_ci(k, n)
        ci_hi_pct = ci_hi * 100
        hit_hist = info["hit"] * 100
        clave = f"{w}#{categoria}"
        degradado = ci_hi_pct < (hit_hist - MARGEN_DEGRADACION_PP)
        avisado = latch.get(clave, {}).get("avisado", False)

        _log(f"{clave}: hist={hit_hist:.1f}% reciente(n={n})={hit_reciente:.1f}% "
             f"Wilson90hi={ci_hi_pct:.1f}% {'DEGRADADA' if degradado else 'ok'}")

        if degradado and not avisado:
            msg = (
                f"📉 *Sports Wallet Mirror -- wallet degradada* -- {clave}\n"
                f"Hit histórico validado: {hit_hist:.1f}%\n"
                f"Hit reciente (últimos {n} trades): {hit_reciente:.1f}% "
                f"(Wilson90% superior={ci_hi_pct:.1f}%)\n"
                f"El límite superior del intervalo reciente ya no alcanza el "
                f"histórico -- posible pérdida de ventaja de esta wallet. "
                f"Solo aviso (DRY_RUN, sin dinero real), no se pausa nada."
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
        print(f"[sports_vigia_wallet_mirror_degradacion] ERROR {type(e).__name__}: {e}")
        sys.exit(0)
