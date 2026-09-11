#!/usr/bin/env python3
"""
cluster_wallets_fillability_fase0.py — FASE 0 (SOLO OBSERVACIÓN) del
hallazgo P32 (12-Ago, idea_cluster_wallets_evento_hallazgo_fuerte_12ago):
cuando 3+ wallets con edge YA VALIDADO (wallet_edge_score_por_activo_
marco.json, sig_bhfdr=True) convergen en el MISMO mercado con precio del
clúster en [0.55,0.70), el voto mayoritario acierta 72-89% (BTC/SOL/ETH/
XRP #15min, BTC#5min), muy por encima de lo que el propio precio ya
implica, con split-half consistente, p_shuffle=0.0000 y TWAP filtrado.
Pendiente: fill-ability real — nunca medida. Ver memoria para el detalle
completo del hallazgo retrospectivo.

Solape verificado con WALLET_MIRROR (12-Ago, mismo turno, petición Javi
"verifica el solape"): el universo de wallets se solapa un 83%
(329/397, mismo `wallet_edge_score_por_activo_marco.json` como fuente,
`wallet_mirror_tracker.cargar_wallets_validadas` exige además n>=30) —
pero el MECANISMO es distinto: WALLET_MIRROR actúa sobre CADA trade de
UNA wallet individual; este detector exige la CONVERGENCIA de 3+ wallets
DISTINTAS en el MISMO mercado antes de disparar, señal de confirmación
más rara y con hit-rate medido más alto (72-89% vs ~63% del segmento
mejor medido de WALLET_MIRROR) — no es una redundancia, es un filtro de
consenso construido sobre el mismo pool de wallets ya validadas.

Mecanismo (conexión WebSocket PROPIA a RTDS, mismo patrón que
wallet_mirror_sniper.py — decisión deliberada de NO reutilizar
ballenas_firehose_cache.py: ese módulo alimenta directamente
BALLENAS_TARDIAS#ETH#5min, LIVE, y CLAUDE.md exige no tocar el motor de
decisión compartido sin diseño cuidadoso + code-review; una conexión
independiente evita cualquier riesgo de romper esa tupla):
  1. Escucha activity/trades en tiempo real, filtra por wallets
     validadas (mismo criterio que wallet_mirror_tracker.cargar_wallets_
     validadas: sig_bhfdr=True, n>=30) por (wallet,activo,marco).
  2. Mantiene en memoria, por mercado (condition_id), las wallets
     validadas distintas vistas y su voto (compro_yes = outcome en
     {"up","yes"}, MISMA definición que analisis_ballenas_dosis_
     respuesta_16jul.py, para que el dato nuevo sea comparable al
     histórico).
  3. Al llegar a 3 wallets distintas (una sola vez por mercado), calcula
     el voto mayoritario y consulta el libro real del token mayoritario
     (`lt._consultar_profundidad_libro`, solo lectura, nunca ordena) —
     resuelve tokens/end_date vía `wallet_mirror_tracker._mercado_para_
     slug` (mismo endpoint ya usado por Wallet Mirror, sin duplicar
     lógica).
  4. Persiste en data/shadow/cluster_wallets_fillability_fase0.csv.

NO coloca, cancela ni modifica ninguna orden real, no llama a ninguna
función de ejecución de live_trade.py, no toca pares_permitidos_live ni
candidatos_evaluacion_live — puramente observacional.

Se fusiona en observadores_fase0.py (screen "observadores") como los
demás — NUNCA lanzar una screen suelta para este script.
"""
import asyncio
import csv
import json
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import websockets

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

import live_trade as lt  # noqa: E402
from wallet_mirror_tracker import _mercado_para_slug  # noqa: E402
from fetch_polymarket_activity_ws import _parse_updown  # noqa: E402

DIR_SHADOW = REPO / "data" / "shadow"
EDGE_SCORE = DIR_SHADOW / "wallet_edge_score_por_activo_marco.json"
OUT = DIR_SHADOW / "cluster_wallets_fillability_fase0.csv"

WS_URL = "wss://ws-live-data.polymarket.com"
PING_INTERVAL_S = 5
RECONNECT_ESPERA_S = 5
RECV_TIMEOUT_S = 30

REFRESCO_WALLETS_S = 1800  # wallet_edge_score_por_activo_marco.json se
# regenera cada hora (cron wallet_edge_tracker.py) — 30min de margen.
RETENCION_MERCADO_S = 3600 * 2  # purga mercados sin actividad >2h
MIN_WALLETS_CLUSTER = 3
N_MIN_WALLET = 30  # mismo umbral que wallet_mirror_tracker.cargar_wallets_validadas
STAKE_REF_EUR = 1.05
MARCOS_LARGO_A_CORTO = {"5min": "5m", "15min": "15m", "60min": "60m", "240min": "240m"}

COLUMNS = [
    "timestamp_utc", "condition_id", "market_slug", "activo", "marco",
    "n_wallets", "votos_yes", "votos_no", "mayoria_yes", "precio_medio",
    "token_mayoria", "ratio_vs_stake", "mejor_ask", "restante_min",
]


def _log(msg: str) -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts}] {msg}", flush=True)


def _cargar_wallets_validadas() -> dict:
    """(wallet_lower, activo, marco_corto) -> edge_pp. Mismo filtro que
    wallet_mirror_tracker.cargar_wallets_validadas (sig_bhfdr, n>=30) —
    reusar el criterio exacto, no reinventar uno ligeramente distinto."""
    try:
        datos = json.loads(EDGE_SCORE.read_text(encoding="utf-8"))
    except Exception:
        return {}
    out = {}
    for v in datos.values():
        if not v.get("sig_bhfdr") or v.get("n", 0) < N_MIN_WALLET:
            continue
        w = (v.get("wallet") or "").lower()
        if not w:
            continue
        out[(w, v["activo"], v["marco"])] = v["edge_pp"]
    return out


def _cargar_vistos_previos() -> set:
    if not OUT.exists():
        return set()
    with open(OUT, encoding="utf-8") as f:
        return {r["condition_id"] for r in csv.DictReader(f)}


_lock_out = None  # se inicializa en main() -- threading no aplica aquí (todo async, un solo hilo)


def _escribir_fila(fila: dict) -> None:
    nuevo = not OUT.exists()
    with open(OUT, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        if nuevo:
            w.writeheader()
        w.writerow(fila)


def _procesar_cluster(cid: str, estado: dict, wallets_validadas: dict) -> None:
    """Se llama la PRIMERA vez que un mercado alcanza MIN_WALLETS_CLUSTER
    wallets validadas distintas. Consulta libro real y persiste. Nunca
    lanza -- cualquier fallo de red simplemente descarta el evento."""
    try:
        votos = estado["votos"]  # wallet -> compro_yes (bool)
        n_wallets = len(votos)
        votos_yes = sum(1 for v in votos.values() if v)
        votos_no = n_wallets - votos_yes
        if votos_yes == votos_no:
            _log(f"[{cid}] {estado['activo']}#{estado['marco']} n={n_wallets} EMPATE, sin señal")
            return
        mayoria_yes = votos_yes > votos_no
        precios = estado["precios"]
        precio_medio = round(sum(precios) / len(precios), 4) if precios else None

        info = _mercado_para_slug(estado["market_slug"])
        if info is None:
            _log(f"[{cid}] {estado['activo']}#{estado['marco']} no se pudo resolver slug={estado['market_slug']}")
            return
        lado_buscado = "yes" if mayoria_yes else "no"
        # outcomes puede venir como Yes/No o Up/Down -- mismo criterio que _opuesto/_token_para_lado
        token_mayoria = None
        for o, t in zip(info["outcomes"], info["tokens"]):
            ol = str(o).strip().lower()
            if (lado_buscado == "yes" and ol in ("yes", "up")) or \
               (lado_buscado == "no" and ol in ("no", "down")):
                token_mayoria = t
                break
        if token_mayoria is None:
            _log(f"[{cid}] no se pudo mapear lado mayoritario a token (outcomes={info['outcomes']})")
            return

        precio_ref = precio_medio if mayoria_yes else round(1.0 - precio_medio, 4) if precio_medio else 0.5
        depth = lt._consultar_profundidad_libro(None, token_mayoria, precio_ref, STAKE_REF_EUR)

        restante_min = ""
        end_date = info.get("end_date") or ""
        if end_date:
            try:
                end_dt = datetime.fromisoformat(end_date.replace("Z", "+00:00"))
                if end_dt.tzinfo is None:
                    end_dt = end_dt.replace(tzinfo=timezone.utc)
                restante_min = round((end_dt - datetime.now(timezone.utc)).total_seconds() / 60.0, 2)
            except Exception:
                restante_min = ""

        fila = {
            "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "condition_id": cid, "market_slug": estado["market_slug"],
            "activo": estado["activo"], "marco": estado["marco"],
            "n_wallets": n_wallets, "votos_yes": votos_yes, "votos_no": votos_no,
            "mayoria_yes": int(mayoria_yes), "precio_medio": precio_medio,
            "token_mayoria": token_mayoria,
            "ratio_vs_stake": depth.get("ratio_vs_stake") if depth.get("ok") else "",
            "mejor_ask": depth.get("mejor_ask") if depth.get("ok") else "",
            "restante_min": restante_min,
        }
        _escribir_fila(fila)
        _log(f"[{cid}] {estado['activo']}#{estado['marco']} n={n_wallets} "
             f"mayoria={'YES' if mayoria_yes else 'NO'} precio={precio_medio} "
             f"ratio_vs_stake={fila['ratio_vs_stake']} restante_min={restante_min}")
    except Exception as e:
        _log(f"[{cid}] error procesando clúster: {e}")


async def _mantener_ping(ws) -> None:
    try:
        while True:
            await asyncio.sleep(PING_INTERVAL_S)
            await ws.send("PING")
    except (asyncio.CancelledError, websockets.exceptions.ConnectionClosed):
        pass


async def _correr_una_conexion(wallets_validadas: dict, vistos: set,
                                estados: dict, ultima_carga_wallets: list) -> None:
    async with websockets.connect(WS_URL, open_timeout=10, close_timeout=5) as ws:
        sub = {"action": "subscribe", "subscriptions": [{"topic": "activity", "type": "trades"}]}
        await ws.send(json.dumps(sub))
        _log("conectado a RTDS, suscrito a activity/trades")
        ping_task = asyncio.create_task(_mantener_ping(ws))
        ultima_purga = time.time()
        try:
            while True:
                raw = await asyncio.wait_for(ws.recv(), timeout=RECV_TIMEOUT_S)
                if not raw:
                    continue
                try:
                    msg = json.loads(raw)
                except (json.JSONDecodeError, TypeError):
                    continue
                payload = msg.get("payload")
                if not isinstance(payload, dict) or "proxyWallet" not in payload:
                    continue

                if time.time() - ultima_carga_wallets[0] > REFRESCO_WALLETS_S:
                    wallets_validadas.clear()
                    wallets_validadas.update(_cargar_wallets_validadas())
                    ultima_carga_wallets[0] = time.time()
                    _log(f"wallets validadas refrescadas: {len(wallets_validadas)}")

                event_slug = payload.get("eventSlug", "")
                activo, marco_largo = _parse_updown(event_slug, payload.get("title", ""))
                if activo is None or marco_largo not in MARCOS_LARGO_A_CORTO:
                    continue
                marco_corto = MARCOS_LARGO_A_CORTO[marco_largo]
                wallet = (payload.get("proxyWallet") or "").lower()
                if (wallet, activo, marco_corto) not in wallets_validadas:
                    continue

                cid = payload.get("conditionId", "")
                if not cid or cid in vistos:
                    continue

                outcome = str(payload.get("outcome", "")).strip().lower()
                compro_yes = outcome in ("up", "yes")
                try:
                    precio = float(payload.get("price", 0) or 0)
                except (TypeError, ValueError):
                    continue

                est = estados[cid]
                if not est:
                    est.update({
                        "activo": activo, "marco": marco_corto,
                        "market_slug": payload.get("slug", ""),
                        "votos": {}, "precios": [], "_creado_ts": time.time(),
                    })
                est["votos"][wallet] = compro_yes
                est["precios"].append(precio)

                if len(est["votos"]) >= MIN_WALLETS_CLUSTER:
                    vistos.add(cid)
                    _procesar_cluster(cid, est, wallets_validadas)

                if time.time() - ultima_purga > 300:
                    corte = time.time() - RETENCION_MERCADO_S
                    muertos = [c for c, e in estados.items()
                               if e and e.get("_creado_ts", 0) < corte]
                    for c in muertos:
                        del estados[c]
                    ultima_purga = time.time()
        finally:
            ping_task.cancel()


async def _bucle_reconexion() -> None:
    wallets_validadas = _cargar_wallets_validadas()
    _log(f"arrancado -- {len(wallets_validadas)} wallets validadas "
         f"(sig_bhfdr, n>={N_MIN_WALLET})")
    vistos = _cargar_vistos_previos()
    _log(f"{len(vistos)} clústeres ya procesados en {OUT.name}, no se repiten")
    estados = defaultdict(dict)
    ultima_carga_wallets = [time.time()]
    while True:
        try:
            await _correr_una_conexion(wallets_validadas, vistos, estados, ultima_carga_wallets)
        except (websockets.exceptions.ConnectionClosed, OSError, asyncio.TimeoutError) as e:
            _log(f"conexión perdida ({e}), reconectando en {RECONNECT_ESPERA_S}s")
        except Exception as e:
            _log(f"error inesperado ({e}), reconectando en {RECONNECT_ESPERA_S}s")
        await asyncio.sleep(RECONNECT_ESPERA_S)


def main() -> None:
    DIR_SHADOW.mkdir(parents=True, exist_ok=True)
    asyncio.run(_bucle_reconexion())


if __name__ == "__main__":
    main()
