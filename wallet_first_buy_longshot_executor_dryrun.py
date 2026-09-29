#!/usr/bin/env python3
"""wallet_first_buy_longshot_executor_dryrun.py -- ejecutor DRY_RUN (29-Sep),
único segmento CONFIRMADO por el gate riguroso completo de
wallet_first_buy_fwd_tracker.py: longshot (p_wallet<0,3), n=1.679, EV/€=+0,37,
t_cluster=2,6 (>2,5), IC90_dias=[0,28,0,46] sin cruzar cero, mitades
consistentes -- veredicto "CANDIDATA robusta" (29-Sep, ver
project_wallet_first_buy_resto_pendiente_28sep en memoria).

Reusa el MISMO mecanismo de detección/seguimiento que
wallet_first_buy_follow_fase0.py (tail del firehose, primera compra de la
watchlist congelada, consulta de libro al offset) -- añade sobre eso:
  1. Filtro a longshot (p_wallet<PF_MAX) -- el único segmento con edge real,
     "resto" está confirmado NEGATIVO, nunca seguirlo.
  2. Offset ÚNICO L=1,0s (LSEL, mismo valor que usa el tracker diario para
     seleccionar wallets -- "más equilibrado" entre EV y robustez según el
     hallazgo de velocidad del 28-Sep: 0,3s da más EV pero menos robustez,
     1,0s es el punto medio documentado).
  3. Decisión de fill-ability real (ratio_vs_stake>=RATIO_MIN, mismo umbral
     que el resto del proyecto) -- solo si pasa se registra
     decision_dry_run=EJECUTADO_DRY_RUN, simulando el stake al ASK real
     leído (nunca al precio de la wallet).

⚠️ DRY_RUN=True por defecto -- OBLIGATORIO, mismo patrón de guardianes que
wallet_mirror_executor_dryrun.py:
  1. DRY_RUN=True es el primer guardián -- con DRY_RUN=True el tramo de
     envío real ni se evalúa (no existe en este fichero, ver abajo).
  2. La tupla sintética "WALLET_FIRST_BUY_LONGSHOT#<activo>#<marco>#BUY_<lado>"
     NUNCA puede estar en `pares_permitidos_live` -- no es una estrategia
     que shadow_predict.py/live_trade.py reconozcan, verificado y logueado.
  3. Activar esto de verdad exige: gate propio de fill-ability (este mismo
     CSV, con n suficiente) + checklist de 6 categorías + `/code-review`
     adversarial + decisión explícita de Javi. Ninguno de los tres ha
     pasado todavía -- esto es FASE 1 de acumulación, no un ejecutor real.

Salida: data/shadow/wallet_first_buy_longshot_executor_dryrun.csv.
Corre en su propio hilo daemon (screen `ejecdryrun`, mismo patrón que el
resto de ejecutores DRY_RUN del proyecto).
"""
import csv
import fcntl
import json
import re
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

import live_trade as lt  # noqa: E402
from resolution_sniper_observer import mercado_slot, token_ids  # noqa: E402

DRY_RUN = True  # ⚠️ guardián #1 -- ver docstring

DATALOGS = Path("/root/polymarket-research-datalogs")
WATCHLIST = REPO / "data" / "shadow" / "wallet_first_buy" / "watchlist.json"
OUT = REPO / "data" / "shadow" / "wallet_first_buy_longshot_executor_dryrun.csv"
LOCK_PATH = REPO / "data" / "shadow" / "wallet_first_buy_longshot_executor_dryrun.csv.lock"

PF_MAX = 0.30       # longshot: p_wallet < 0.30, único segmento confirmado (resto está confirmado negativo)
LSEL = 1.0          # offset único, mismo valor "equilibrado" que usa el tracker diario para seleccionar wallets
STAKE_REF = 1.05
RATIO_MIN = 5.0      # mismo umbral de fill-ability que min_profundidad_ratio_libro del resto del proyecto
TTE_MIN = 20
POLL_S = 0.2

CAMPOS = ["ts_trade", "wallet", "slug", "market_id", "condition_id", "activo", "marco", "outcome",
          "p_wallet", "usd", "tte_s", "lag_deteccion_s", "offset_s", "t_real_s",
          "ask", "bid", "profundidad_eur", "ratio_vs_stake", "lat_libro_ms",
          "decision_dry_run", "stake_sim_eur", "error", "outcome_real", "resolved_ts"]

_lock = threading.Lock()
_pool = ThreadPoolExecutor(max_workers=8)
_vistos = set()


def _log(msg):
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _escribir(fila):
    lock_f = open(LOCK_PATH, "w")
    try:
        fcntl.flock(lock_f, fcntl.LOCK_EX)
        nuevo = not OUT.exists()
        with open(OUT, "a", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=CAMPOS)
            if nuevo:
                w.writeheader()
            w.writerow(fila)
    finally:
        fcntl.flock(lock_f, fcntl.LOCK_UN)
        lock_f.close()


def _libro(token_id):
    book = lt._fetch_book_publico(token_id)
    if book is None:
        return None, None, None, None, "sin respuesta del libro"
    try:
        asks = [(float(l["price"]), float(l["size"])) for l in (book.get("asks") or [])]
        bids = [(float(l["price"]), float(l["size"])) for l in (book.get("bids") or [])]
    except (TypeError, ValueError, KeyError):
        return None, None, None, None, "libro ilegible"
    ask = min((p for p, _ in asks), default=None)
    bid = max((p for p, _ in bids), default=None)
    prof = sum(p * s for p, s in asks if ask is not None and p <= ask * 1.05) if ask is not None else 0.0
    ratio = round(prof / STAKE_REF, 1) if ask is not None else None
    return ask, bid, round(prof, 2), ratio, ""


def _seguir(base, activo, marco, ini, outcome, t_det):
    tag = "5m" if marco == "5min" else "15m"
    try:
        _, mkt = mercado_slot(activo, tag, ini)
    except Exception:
        mkt = None
    tok = None
    if mkt:
        ty, tn = token_ids(mkt)
        tok = ty if outcome == "Up" else tn
        base["market_id"] = mkt.get("id", "")
        base["condition_id"] = mkt.get("conditionId", "")

    espera = t_det + LSEL - time.time()
    if espera > 0:
        time.sleep(espera)
    t = time.perf_counter()
    ask, bid, prof, ratio, err = _libro(tok) if tok else (None, None, None, None, "sin_mercado_o_token")

    if err:
        decision, stake_sim = f"NO_dispara({err})", ""
    elif ratio is None or ratio < RATIO_MIN:
        decision, stake_sim = f"NO_dispara(fillability_baja:ratio={ratio})", ""
    else:
        # DRY_RUN=True -- guardián #1, nunca se llega a enviar una orden real
        # aunque el resto de la lógica diga "dispara". Solo se registra la
        # decisión simulada para medir fill-ability + PnL a resolución.
        decision, stake_sim = "EJECUTADO_DRY_RUN", STAKE_REF

    fila = dict(base)
    fila.update({"offset_s": LSEL, "t_real_s": round(time.time() - t_det, 3), "ask": ask, "bid": bid,
                 "profundidad_eur": prof, "ratio_vs_stake": ratio,
                 "lat_libro_ms": round((time.perf_counter() - t) * 1000),
                 "decision_dry_run": decision, "stake_sim_eur": stake_sim, "error": err,
                 "outcome_real": "", "resolved_ts": ""})
    _escribir(fila)
    if decision == "EJECUTADO_DRY_RUN":
        _log(f"🐣 EJECUTADO_DRY_RUN {activo}#{marco} {outcome} p_wallet={base['p_wallet']} "
             f"ask={ask} ratio={ratio} stake_sim={stake_sim}€")


def _cargar_watchlist(prev):
    try:
        d = json.loads(WATCHLIST.read_text(encoding="utf-8"))
        w = {k.lower() for k in d.get("wallets", {})}
        if w != prev:
            _log(f"watchlist: {len(w)} wallets (para_dia={d.get('para_dia')}, train={d.get('train_dias')})")
        return w
    except Exception:
        return prev


def _fila(linea, cab):
    try:
        r = next(csv.reader([linea]))
        return dict(zip(cab, r)) if len(r) >= len(cab) else None
    except Exception:
        return None


def main():
    assert DRY_RUN, "guardián #1: DRY_RUN debe ser True -- este ejecutor no está aprobado para dinero real"
    _log(f"wallet_first_buy_longshot_executor_dryrun arrancado (PF_MAX={PF_MAX}, LSEL={LSEL}s, "
          f"DRY_RUN={DRY_RUN}, solo simulación)")
    watch, t_watch = set(), 0.0
    arch, pos, buf, cab = None, 0, "", None
    while True:
        try:
            ahora = time.time()
            if ahora - t_watch > 300:
                watch, t_watch = _cargar_watchlist(watch), ahora
            hoy = DATALOGS / f"polymarket_activity_{datetime.now(timezone.utc):%Y-%m-%d}.csv"
            if hoy != arch:
                arch, buf, cab = hoy, "", None
                pos = hoy.stat().st_size if hoy.exists() else 0
                _vistos.clear()
            if arch.exists() and watch:
                with open(arch, encoding="utf-8", errors="replace", newline="") as f:
                    if cab is None:
                        cab = next(csv.reader([f.readline()]))
                    f.seek(pos)
                    datos = f.read()
                    pos = f.tell()
                if datos:
                    buf += datos
                    *lineas, buf = buf.split("\n")
                    for ln in lineas:
                        r = _fila(ln, cab) if ln else None
                        if not r or r.get("side") != "BUY" or r.get("marco") not in ("5min", "15min"):
                            continue
                        w = (r.get("wallet") or "").lower()
                        if w not in watch:
                            continue
                        try:
                            p_wallet = float(r.get("price", ""))
                        except (TypeError, ValueError):
                            continue
                        if p_wallet >= PF_MAX:
                            continue  # solo longshot -- "resto" está confirmado negativo, nunca seguirlo
                        m = re.search(r"-(\d{10})$", r.get("market_slug") or "")
                        if not m:
                            continue
                        key = (r["market_slug"], w, r["outcome"])
                        if key in _vistos:
                            continue
                        _vistos.add(key)
                        ini = int(m.group(1))
                        dur = 300 if r["marco"] == "5min" else 900
                        try:
                            t_tr = datetime.fromisoformat(r["timestamp_utc"].replace("Z", "+00:00")).timestamp()
                        except ValueError:
                            continue
                        tte = ini + dur - t_tr
                        if tte < TTE_MIN + LSEL:
                            continue
                        t_det = time.time()
                        base = {"ts_trade": r["timestamp_utc"], "wallet": w, "slug": r["market_slug"],
                                "market_id": "", "condition_id": "",
                                "activo": r["activo"], "marco": r["marco"], "outcome": r["outcome"],
                                "p_wallet": r["price"], "usd": r["usd_value"], "tte_s": round(tte, 1),
                                "lag_deteccion_s": round(t_det - t_tr, 3)}
                        _pool.submit(_seguir, base, r["activo"], r["marco"], ini, r["outcome"], t_det)
            time.sleep(POLL_S)
        except Exception as e:
            _log(f"error en el bucle ({type(e).__name__}: {e})")
            time.sleep(2)


if __name__ == "__main__":
    main()
