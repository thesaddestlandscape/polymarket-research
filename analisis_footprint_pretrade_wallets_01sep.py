#!/usr/bin/env python3
"""analisis_footprint_pretrade_wallets_01sep.py — footprint pre-trade:
¿se mueve el libro de órdenes (fetch_libro_book_ws.py) de forma
detectable, en la dirección correcta, en los ~60s ANTES de que una
wallet informada (watchlist de wallet_mirror_sniper_dry_run.csv,
edge_pp_validado ya filtrado por el propio pipeline) ejecute su trade?

Solo lectura. NO toca fetch_libro_book_ws.py ni ningún fichero de
producción -- lee /root/polymarket-research-datalogs/libro_book_ws_*.csv
(datalog externo, fuera del repo) y data/shadow/wallet_mirror_sniper_dry_run.csv.

Metodología:
  Para cada trade de wallet en la ventana temporal donde el libro tiene
  datos (hoy, 01-Sep, desplegado ~15:37 UTC), busca la fila de libro más
  reciente del MISMO market_id (`market` = condition_id) con
  timestamp_utc <= trade_timestamp y timestamp_utc >= trade_timestamp-60s.
  Esa fila trae best_ask_inicio/best_ask_ultimo de esa ventana de 20s --
  mide cuánto se movió el ask en la ventana ANTES de que la wallet operara.

  Señal = movimiento del ask proyectado en la dirección de la apuesta de
  la wallet (lado_wallet/mirror_lado "Up"→ask subiendo es a favor,
  "Down"→ask bajando es a favor). Si el libro "sabe" algo antes de que la
  wallet opere, esta señal debería ser positiva en promedio.

  Rigor: test de permutación (2000 iters) barajando la dirección
  (Up/Down) asignada a cada observación -- compara la media observada
  contra la distribución nula de "cualquier dirección al azar", no contra
  cero a secas (evita colar un sesgo estructural del mercado que no tenga
  nada que ver con la wallet).
"""
import csv
import json
import random
import statistics
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
LIBRO_DIR = Path("/root/polymarket-research-datalogs")
WALLET_MIRROR = REPO / "data/shadow/wallet_mirror_sniper_dry_run.csv"
OUT = REPO / "data/shadow/footprint_pretrade_analisis.json"

VENTANA_PREVIA_S = 60
N_MIN = 40
ITERS = 2000


def parse_ts(s: str):
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except Exception:
        return None


def cargar_libro_por_mercado(fecha_str: str) -> dict:
    """market (condition_id) -> lista ordenada de (ts, best_ask_inicio, best_ask_ultimo)."""
    p = LIBRO_DIR / f"libro_book_ws_{fecha_str}.csv"
    por_mercado: dict[str, list] = {}
    if not p.exists():
        return por_mercado
    with open(p, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            ts = parse_ts(r.get("timestamp_utc", ""))
            if ts is None:
                continue
            try:
                ai = float(r.get("best_ask_inicio"))
                au = float(r.get("best_ask_ultimo"))
            except (TypeError, ValueError):
                continue
            por_mercado.setdefault(r["market"], []).append((ts, ai, au))
    for m in por_mercado:
        por_mercado[m].sort(key=lambda x: x[0])
    return por_mercado


def buscar_ventana_previa(filas: list, t_trade: datetime):
    """Última fila de libro con ts <= t_trade y ts >= t_trade - VENTANA_PREVIA_S."""
    limite_inf = t_trade - timedelta(seconds=VENTANA_PREVIA_S)
    candidata = None
    for ts, ai, au in filas:
        if ts > t_trade:
            break
        if ts >= limite_inf:
            candidata = (ts, ai, au)
    return candidata


def signo_lado(lado: str) -> int:
    if lado == "Up":
        return 1
    if lado == "Down":
        return -1
    return 0


def main() -> int:
    # Rango de fechas real de los datalogs disponibles
    fechas = sorted({p.stem.replace("libro_book_ws_", "") for p in LIBRO_DIR.glob("libro_book_ws_*.csv")})
    print(f"Datalogs de libro disponibles: {fechas}")
    if not fechas:
        print("Sin datalogs de libro -- nada que cruzar.")
        json.dump({"n": 0, "veredicto": "sin_datos"}, open(OUT, "w", encoding="utf-8"), indent=2)
        return 0

    libro_por_fecha = {f: cargar_libro_por_mercado(f) for f in fechas}
    rango_min = min(
        min(ts for filas in libro_por_fecha[f].values() for ts, *_ in filas)
        for f in fechas if libro_por_fecha[f]
    )
    rango_max = max(
        max(ts for filas in libro_por_fecha[f].values() for ts, *_ in filas)
        for f in fechas if libro_por_fecha[f]
    )
    print(f"Rango temporal del libro: {rango_min} -> {rango_max}")

    observaciones = []  # (senal_cruda, lado_signo)
    n_trades_en_rango = 0
    n_con_libro_cercano = 0
    vistos_hash = set()

    with open(WALLET_MIRROR, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            t = parse_ts(r.get("trade_timestamp", ""))
            if t is None or not (rango_min <= t <= rango_max):
                continue
            n_trades_en_rango += 1
            h = r.get("transaction_hash", "")
            if h and h in vistos_hash:
                continue  # dedup: varias filas pueden compartir el mismo trade real (varias wallets/mismo evento)
            fecha_str = t.strftime("%Y-%m-%d")
            filas = libro_por_fecha.get(fecha_str, {}).get(r.get("condition_id", ""))
            if not filas:
                continue
            ventana = buscar_ventana_previa(filas, t)
            if ventana is None:
                continue
            n_con_libro_cercano += 1
            if h:
                vistos_hash.add(h)
            _, ai, au = ventana
            lado = r.get("lado_wallet") or r.get("mirror_lado") or ""
            s = signo_lado(lado)
            if s == 0:
                continue
            senal = (au - ai) * s  # movimiento del ask proyectado a favor del lado de la wallet
            observaciones.append(senal)

    n = len(observaciones)
    print(f"Trades de wallet en rango temporal del libro: {n_trades_en_rango}")
    print(f"De esos, con ventana de libro cercana (<={VENTANA_PREVIA_S}s antes, dedup por tx_hash): {n_con_libro_cercano}")
    print(f"Observaciones finales (lado válido Up/Down): {n}")

    if n < N_MIN:
        print(f"n={n} < N_MIN={N_MIN} -- insuficiente para concluir nada, dataset demasiado nuevo.")
        json.dump({
            "n": n, "n_trades_en_rango": n_trades_en_rango,
            "n_con_libro_cercano": n_con_libro_cercano,
            "veredicto": "n_insuficiente",
            "nota": "libro_book_ws.py desplegado hoy mismo (~15:37 UTC), solo ~2.5h de datos -- "
                    "repetir este analisis en proximas sesiones conforme se acumule mas historia.",
        }, open(OUT, "w", encoding="utf-8"), indent=2)
        return 0

    media_obs = statistics.fmean(observaciones)
    sd = statistics.pstdev(observaciones) or 1e-9

    # Test de permutacion: barajar el signo (lado) asignado a cada magnitud
    magnitudes = [abs(o) for o in observaciones]
    signos_reales = [1 if o >= 0 else -1 for o in observaciones]
    rng = random.Random(11)
    boot = []
    for _ in range(ITERS):
        signos_barajados = signos_reales[:]
        rng.shuffle(signos_barajados)
        muestra = [m * s for m, s in zip(magnitudes, signos_barajados)]
        boot.append(statistics.fmean(muestra))
    p_valor = sum(1 for b in boot if b >= media_obs) / ITERS if media_obs >= 0 else sum(1 for b in boot if b <= media_obs) / ITERS

    veredicto = "confirmado" if p_valor < 0.05 and media_obs > 0 else "sin_concluir"

    resultado = {
        "n": n,
        "n_trades_en_rango": n_trades_en_rango,
        "n_con_libro_cercano": n_con_libro_cercano,
        "senal_media": round(media_obs, 5),
        "senal_sd": round(sd, 5),
        "p_valor_permutacion": round(p_valor, 4),
        "veredicto": veredicto,
        "ventana_previa_s": VENTANA_PREVIA_S,
        "rango_datalog": [rango_min.isoformat(), rango_max.isoformat()],
        "nota": "libro_book_ws.py desplegado hoy mismo, dataset de ~2.5h -- resultado orientativo, "
                "repetir con mas historia antes de construir cualquier ejecutor sobre esto.",
    }
    print(json.dumps(resultado, indent=2, ensure_ascii=False))
    json.dump(resultado, open(OUT, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    return 0


if __name__ == "__main__":
    main()
