#!/usr/bin/env python3
"""
wallet_mirror_tracker.py — Arquetipo C ("Wallet Mirror", P24), petición
Javi 23-Jul, retomado y CERRADO a nivel de investigación 29-Jul: mide si
replicar (SEGUIR) o desvanecer (FADE) el trade de wallets validadas
(BH-FDR, n≥30) en la zona de precio medio/bajo (0.1-0.6, donde nuestro
propio modelo GBM tiene edge teórico pero fill-ability ~0%) captura un
edge real, ANTES de construir ningún ejecutor de dinero real.

Fuente de detección: `fetch_polymarket_activity_ws.py` (screen
`polyactivity`, construido 28-Jul, sin conectar a nada hasta hoy) — ya
captura wallet/precio/mercado/timestamp de CADA trade real en tiempo
real vía el firehose RTDS, exactamente lo que este mecanismo necesita
(cierra el "punto 2" pendiente de idea_wallet_mirror_arquetipo_c_23jul:
medir el lag de detección — aquí la detección es casi instantánea,
mismo pipeline ya verificado con 1288 trades/25s).

Metodología (solo lectura, NO ejecuta nada, NO toca dinero):
1. Carga las wallets validadas (`sig_bhfdr=True`, n>=30) de
   `wallet_edge_score_por_activo_marco.json`, clasificadas SEGUIR
   (edge_pp>0) / FADE (edge_pp<0), cada una atada a SU (activo,marco)
   validado exacto -- no se generaliza a otros mercados de la misma
   wallet.
2. Lee `data/shadow/polymarket_activity_YYYY-MM-DD.csv` (hoy + ayer, para
   no perder trades cerca de medianoche) buscando filas cuyo `wallet`
   coincida (case-insensitive) Y cuyo (activo,marco) coincida con el de
   la validación de esa wallet.
3. Por cada match nuevo (dedup por `transaction_hash`), registra qué
   habría hecho Wallet Mirror: mismo lado que la wallet si es SEGUIR,
   lado contrario si es FADE. Precio de referencia = el precio real al
   que la wallet operó (mismo instante, no hay slippage de detección
   que estimar aparte -- eso se mide en el gate de fill-ability real,
   pendiente, no en este tracker).
4. Resuelve contra el outcome oficial (gamma-api, vía `market_slug` --
   `polymarket_activity` no loguea el market_id numérico de Gamma, solo
   `condition_id`/slugs) cuando el mercado ya haya cerrado.

Cron sugerido: cada 5-10min (no necesita ser un screen persistente --
esto es un catch-up sobre un CSV que ya se está escribiendo solo, no una
decisión en tiempo real todavía).
"""
import csv
import fcntl
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

import requests  # noqa: E402

DIR_SHADOW = REPO / "data" / "shadow"
# 29-Jul: polymarket_activity_*.csv vive fuera del repo (fix fetch_polymarket_activity_ws.py).
DIR_DATALOGS = Path("/root/polymarket-research-datalogs")
WALLET_SCORES = DIR_SHADOW / "wallet_edge_score_por_activo_marco.json"
OUT = DIR_SHADOW / "wallet_mirror_dry_run.csv"
OUT_LOCK = DIR_SHADOW / "wallet_mirror_dry_run.csv.lock"
VISTOS_PATH = DIR_SHADOW / "wallet_mirror_vistos.json"  # transaction_hash ya procesados

N_MIN_WALLET = 30
GAMMA = "https://gamma-api.polymarket.com"
UMBRAL_RESUELTO = 0.98

# 29-Jul (bug real encontrado en el primer smoke test, 0 matches pese a
# haber decenas en los datos crudos): wallet_edge_score_por_activo_marco.json
# usa "5m"/"15m"/"60m"/"240m"/"weekly", polymarket_activity_*.csv usa
# "5min"/"15min"/"60min"/"240min" -- sin normalizar, el join nunca cruzaba
# nada. "weekly" no tiene equivalente en el feed de activity (no se
# trackea ese marco ahí) -- esas wallets quedan fuera, no es un bug, es
# que la fuente no cubre ese marco.
MARCO_A_ACTIVITY = {"5m": "5min", "15m": "15min", "60m": "60min", "240m": "240min"}


def _log(msg: str) -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts}] {msg}", flush=True)


def cargar_wallets_validadas() -> dict:
    """(wallet_lower, activo, marco) -> {"tipo": "SEGUIR"|"FADE", "edge_pp": float, "n": int}"""
    try:
        datos = json.loads(WALLET_SCORES.read_text(encoding="utf-8"))
    except Exception:
        return {}
    out = {}
    for v in datos.values():
        if not v.get("sig_bhfdr") or v.get("n", 0) < N_MIN_WALLET:
            continue
        w = (v.get("wallet") or "").lower()
        if not w:
            continue
        marco_activity = MARCO_A_ACTIVITY.get(v["marco"])
        if marco_activity is None:
            continue  # "weekly" -- sin equivalente en el feed de activity
        # 29-Jul: gate riguroso sobre wallet_mirror_dry_run.csv encontró
        # BTC#5min#FADE (n=271) invertido -- hit=33.2% (Wilson90_lo=28.7%),
        # consistente en ~20 wallets distintas, no un caso aislado. Causa
        # diagnosticada: edge_pp=(hit-precio_medio)*100 es EV/calibración,
        # no dirección -- una wallet puede tener edge_pp<0 (mal EV) con
        # hit>50% si sistemáticamente sobrepaga por el favorito (mismo
        # patrón payout-asimétrico que FAVORITO_CONFIRMADO). Fadear a esa
        # wallet significa apostar por el lado underdog de SU apuesta, que
        # tiene hit-rate BAJO por definición (ella gana la mayoría) --
        # invertir dirección de una wallet con hit>50% garantiza que el
        # mirror pierda la mayoría de las veces, aunque el EV en teoría
        # compense. Confirmado: 29-Jul, 52 wallets FADE validadas
        # globalmente, 15 (29%) tenían hit>50% -- exactamente el patrón.
        # FADE ahora exige TAMBIÉN hit<50% (wallet que se equivoca de
        # lado más de la mitad de las veces, no solo mal EV) -- las
        # excluidas (edge_pp<0 pero hit>=50%) se descartan por ahora, sin
        # estrategia validada para ese caso todavía.
        if v["edge_pp"] > 0:
            tipo = "SEGUIR"
        elif v["hit"] < 0.5:
            tipo = "FADE"
        else:
            continue  # edge_pp<0 pero hit>=50% -- payout asimétrico, no dirección; sin mirror validado
        out[(w, v["activo"], marco_activity)] = {
            "tipo": tipo, "edge_pp": v["edge_pp"], "n": v["n"],
            "size_mediana": v.get("size_mediana"),
        }
    return out


def _archivos_activity(dias: int = 2) -> list[Path]:
    hoy = datetime.now(timezone.utc)
    out = []
    for d in range(dias):
        fecha = (hoy - timedelta(days=d)).strftime("%Y-%m-%d")
        p = DIR_DATALOGS / f"polymarket_activity_{fecha}.csv"
        if p.exists():
            out.append(p)
    return out


def _vistos_cargar() -> set:
    try:
        return set(json.loads(VISTOS_PATH.read_text(encoding="utf-8")))
    except Exception:
        return set()


def _vistos_guardar(vistos: set) -> None:
    # Cap razonable -- solo necesitamos dedup reciente, no un histórico infinito.
    lista = list(vistos)[-50000:]
    VISTOS_PATH.write_text(json.dumps(lista), encoding="utf-8")


def detectar_matches(wallets: dict, vistos: set) -> tuple[list[dict], set]:
    """Una señal por (wallet, market_slug) -- no por transaction_hash. Una
    wallet activa puede rellenar la misma posición en decenas de fills
    (visto en el primer smoke test: 3135 "matches" en un solo día, la
    inmensa mayoría re-fills del mismo mercado) -- eso no son señales
    independientes, es ruido que infla n artificialmente. Se queda con el
    PRIMER fill BUY de cada (wallet, mercado): esa es "la wallet abrió
    posición aquí", el resto es solo tamaño acumulado de la misma apuesta."""
    nuevos = []
    vistos_nuevo = set(vistos)
    for path in _archivos_activity():
        with open(path, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if (row.get("side") or "").strip().upper() != "BUY":
                    continue  # solo aperturas de posición, no ventas/cierres
                w = (row.get("wallet") or "").lower()
                clave = (w, row.get("activo", ""), row.get("marco", ""))
                info = wallets.get(clave)
                if info is None:
                    continue
                dedup_key = f"{w}|{row.get('market_slug','')}"
                if dedup_key in vistos_nuevo:
                    continue
                vistos_nuevo.add(dedup_key)
                lado_wallet = row.get("outcome", "")  # "Up"/"Down"
                mirror_lado = lado_wallet if info["tipo"] == "SEGUIR" else _opuesto(lado_wallet)
                th = row.get("transaction_hash", "")
                fill = _fillability_mirror(row.get("market_slug", ""), mirror_lado, row.get("price", ""))
                # 29-Jul (idea_grandes_jugadas_wallets_validadas_29jul, petición
                # Javi): tamaño de ESTA apuesta relativo a la mediana propia de
                # la wallet en esta (activo,marco) -- confirmado con gate
                # riguroso (shuffle p=0.0000, split-half estable) sobre las 70
                # wallets ya validadas: >=2x mediana propia hit=79.2% (n=1200)
                # vs <=0.5x hit=48.7% (n=1537). Tamaño RELATIVO, no USD absoluto
                # (eso solo refleja capital disponible). size_mediana viene de
                # wallet_edge_score_por_activo_marco.json (wallet_edge_tracker.py).
                ratio_size = None
                size_mediana = info.get("size_mediana")
                try:
                    usd_trade = float(row.get("usd_value") or 0)
                except (TypeError, ValueError):
                    usd_trade = 0.0
                if size_mediana and usd_trade > 0:
                    ratio_size = round(usd_trade / size_mediana, 2)
                nuevos.append({
                    "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                    "trade_timestamp": row.get("timestamp_utc", ""),
                    "wallet": w,
                    "tipo": info["tipo"],
                    "edge_pp_validado": info["edge_pp"],
                    "n_validado": info["n"],
                    "activo": row.get("activo", ""),
                    "marco": row.get("marco", ""),
                    "condition_id": row.get("condition_id", ""),
                    "market_slug": row.get("market_slug", ""),
                    "lado_wallet": lado_wallet,
                    "precio_wallet": row.get("price", ""),
                    "mirror_lado": mirror_lado,
                    "transaction_hash": th,
                    "outcome_real": "",
                    "acierto": "",
                    "resolved_ts": "",
                    "ratio_vs_stake_deteccion": fill.get("ratio_vs_stake", "") if fill.get("ok") else "",
                    "mejor_ask_deteccion": fill.get("mejor_ask", "") if fill.get("ok") else "",
                    "usd_trade": usd_trade if usd_trade > 0 else "",
                    "size_mediana_wallet": size_mediana if size_mediana else "",
                    "ratio_vs_mediana_propia": ratio_size if ratio_size is not None else "",
                    "es_jugada_grande": int(ratio_size >= 2.0) if ratio_size is not None else "",
                })
    return nuevos, vistos_nuevo


def _opuesto(lado: str) -> str:
    l = (lado or "").strip().lower()
    if l in ("up", "yes"):
        return "Down"
    if l in ("down", "no"):
        return "Up"
    return ""


STAKE_REF_EUR = 1.05  # mismo suelo que min_stake_eur en config_live.json
RATIO_OBJETIVO = 5.0  # mismo umbral que veto_profundidad/analisis_fills.py/P22


def _token_para_lado(market_slug: str, lado: str) -> str | None:
    """29-Jul: fill-ability -- ninguna señal de wallet_mirror medía si
    el libro real habría dejado ejecutar el mirror. wallet_mirror_dry_run.csv
    solo trae market_slug/condition_id (no market_id numérico de Gamma), así
    que en vez de _get_token_ids(market_id) (live_trade.py) se resuelve por
    slug vía /events -- mismo endpoint que ya usa outcome_por_slug() en este
    fichero. Valida el orden real contra `outcomes` en vez de asumir
    clobTokenIds[0]=primer outcome (mismo criterio que _get_token_ids)."""
    try:
        r = requests.get(f"{GAMMA}/events", params={"slug": market_slug}, timeout=8)
        if r.status_code != 200:
            return None
        ev = r.json()
        if not ev or not ev[0].get("markets"):
            return None
        mkt = ev[0]["markets"][0]
        outcomes = mkt.get("outcomes")
        outcomes = json.loads(outcomes) if isinstance(outcomes, str) else outcomes
        tokens = mkt.get("clobTokenIds")
        tokens = json.loads(tokens) if isinstance(tokens, str) else tokens
        if not outcomes or not tokens or len(outcomes) != len(tokens):
            return None
        lado_l = (lado or "").strip().lower()
        for o, t in zip(outcomes, tokens):
            if (o or "").strip().lower() == lado_l:
                return t
        return None
    except Exception:
        return None


def _fillability_mirror(market_slug: str, mirror_lado: str, precio_wallet: str) -> dict:
    """Consulta el libro PÚBLICO (solo lectura, nunca ordena) para el token
    del lado que Wallet Mirror habría comprado, en el instante de detección
    (no en el instante original del trade de la wallet -- mismo desfase que
    ya acepta P22/candidato_evaluacion, aceptable dado el cron de 10min).
    precio de referencia: si mirror_lado==lado_wallet (SEGUIR), el mismo
    precio que pagó la wallet; si es el lado contrario (FADE), 1-precio."""
    try:
        precio_w = float(precio_wallet)
    except (TypeError, ValueError):
        return {"ok": False}
    token_id = _token_para_lado(market_slug, mirror_lado)
    if token_id is None:
        return {"ok": False}
    precio_entrada = precio_w  # aproximación -- ver docstring
    return lt._consultar_profundidad_libro(None, token_id, precio_entrada, STAKE_REF_EUR)


COLUMNS = ["timestamp_utc", "trade_timestamp", "wallet", "tipo", "edge_pp_validado",
           "n_validado", "activo", "marco", "condition_id", "market_slug",
           "lado_wallet", "precio_wallet", "mirror_lado", "transaction_hash",
           "outcome_real", "acierto", "resolved_ts",
           "ratio_vs_stake_deteccion", "mejor_ask_deteccion",
           "usd_trade", "size_mediana_wallet", "ratio_vs_mediana_propia", "es_jugada_grande"]


def guardar(filas: list) -> None:
    if not filas:
        return
    lock_f = open(OUT_LOCK, "w")
    try:
        fcntl.flock(lock_f, fcntl.LOCK_EX)
        try:
            nuevo = not OUT.exists()
            with open(OUT, "a", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=COLUMNS)
                if nuevo:
                    w.writeheader()
                for fila in filas:
                    w.writerow(fila)
        finally:
            fcntl.flock(lock_f, fcntl.LOCK_UN)
    finally:
        lock_f.close()


def outcome_por_slug(market_slug: str) -> str | None:
    try:
        r = requests.get(f"{GAMMA}/events", params={"slug": market_slug}, timeout=8)
        if r.status_code != 200:
            return None
        ev = r.json()
        if not ev or not ev[0].get("markets"):
            return None
        mkt = ev[0]["markets"][0]
        pr = mkt.get("outcomePrices")
        pr = json.loads(pr) if isinstance(pr, str) else pr
        if not pr or len(pr) < 2:
            return None
        if float(pr[0]) >= UMBRAL_RESUELTO:
            return "Up"
        if float(pr[1]) >= UMBRAL_RESUELTO:
            return "Down"
    except Exception:
        pass
    return None


MAX_SLUGS_POR_CICLO = 150  # cap por ciclo -- muchas filas comparten market_slug
                            # (varias wallets en el mismo mercado), resolver por
                            # slug único evita pedir lo mismo N veces y acota el
                            # tiempo de ejecución (llamadas de red secuenciales).


def resolver_pendientes() -> int:
    """Mismo diseño que resuelve_ballenas_5min.py (/code-review 27-Jul): leer
    sin lock, resolver TODAS las llamadas de red sin lock, adquirir el lock
    solo para el tramo final de escritura (releer fresco por si el tracker
    añadió filas mientras tanto)."""
    if not OUT.exists():
        return 0
    with open(OUT, newline="", encoding="utf-8") as f:
        filas = list(csv.DictReader(f))

    slugs_pendientes = sorted({r["market_slug"] for r in filas
                                if not r.get("outcome_real") and r.get("market_slug")})
    outcomes_por_slug = {}
    for slug in slugs_pendientes[:MAX_SLUGS_POR_CICLO]:
        outcome = outcome_por_slug(slug)
        if outcome is not None:
            outcomes_por_slug[slug] = outcome

    if not outcomes_por_slug:
        return 0

    lock_f = open(OUT_LOCK, "w")
    try:
        fcntl.flock(lock_f, fcntl.LOCK_EX)
        try:
            with open(OUT, newline="", encoding="utf-8") as f:
                filas = list(csv.DictReader(f))
            resueltas = 0
            for r in filas:
                if r.get("outcome_real"):
                    continue
                outcome = outcomes_por_slug.get(r.get("market_slug"))
                if outcome is None:
                    continue
                r["outcome_real"] = outcome
                r["acierto"] = "1" if outcome == r.get("mirror_lado") else "0"
                r["resolved_ts"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
                resueltas += 1
            if resueltas:
                with open(OUT, "w", newline="", encoding="utf-8") as f:
                    w = csv.DictWriter(f, fieldnames=COLUMNS)
                    w.writeheader()
                    w.writerows(filas)
            return resueltas
        finally:
            fcntl.flock(lock_f, fcntl.LOCK_UN)
    finally:
        lock_f.close()


def main() -> int:
    wallets = cargar_wallets_validadas()
    _log(f"wallets validadas cargadas: {len(wallets)} (SEGUIR="
         f"{sum(1 for v in wallets.values() if v['tipo']=='SEGUIR')}, "
         f"FADE={sum(1 for v in wallets.values() if v['tipo']=='FADE')})")

    vistos = _vistos_cargar()
    nuevos, vistos = detectar_matches(wallets, vistos)
    _log(f"matches nuevos detectados: {len(nuevos)}")
    guardar(nuevos)
    _vistos_guardar(vistos)

    resueltas = resolver_pendientes()
    _log(f"resueltas este ciclo: {resueltas}")

    if OUT.exists():
        with open(OUT, newline="", encoding="utf-8") as f:
            filas = [r for r in csv.DictReader(f) if r.get("outcome_real")]
        if filas:
            n = len(filas)
            aciertos = sum(1 for r in filas if r["acierto"] == "1")
            n_seguir = sum(1 for r in filas if r["tipo"] == "SEGUIR")
            n_fade = n - n_seguir
            _log(f"acumulado resuelto: n={n} hit={aciertos/n*100:.1f}% "
                 f"(SEGUIR n={n_seguir}, FADE n={n_fade})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
