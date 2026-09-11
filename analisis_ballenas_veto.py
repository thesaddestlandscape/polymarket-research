"""
analisis_ballenas_veto.py — ¿el flujo grande de otros traders explica nuestros
vetos de profundidad, o es solo el mismo libro fino que afecta a todos?

Hipótesis (H-CUSTOM-BALLENAS-VETO, propuesta 08-Jul tras estudiar ejecución de
wowitsamazing/Bonereaper): si un trade grande (consumidor de liquidez del MISMO
lado que intentamos comprar) aparece justo antes de nuestra señal, es más
probable que el libro esté vacío cuando llegamos → correlación causal, no solo
coincidencia de "libros finos en general".

Metodología (read-only, sin tocar producción):
  1. Señales únicas de libro_snapshots.csv con motivo ejecutada/veto_profundidad
     (misma dedup por prioridad que analisis_fills.py: 1 señal = 1 fila).
  2. market_id -> condition_id + end_date via data/markets/*.csv (grep dirigido,
     no parseo completo — los CSV son >600MB/día).
  3. Para cada señal: prints públicos de trades del mercado (data-api /trades),
     filtrados al mismo lado (outcome) que intentamos comprar, en la ventana
     [-LOOKBACK_S, ts_señal].
  4. Comparar volumen/clip máximo pre-señal entre ejecutada vs veto_profundidad
     con Mann-Whitney U (implementación propia, sin scipy) + medianas/IQR.
  5. Control de confound: GBM_LATE_15M solo dispara con restante_min∈[3,12] —
     se reporta la distribución de restante_min por grupo para confirmar que
     no es solo "veto pasa más tarde en la ventana".

Umbral de conclusión (CLAUDE.md): n≥15 por grupo mínimo para cualquier lectura;
n≥30 para una decisión. Con n<15 el script imprime los números y para ahí.
"""
import csv
import glob
import json
import math
import statistics
import subprocess
import time
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests

DIR = Path(__file__).parent
SNAPSHOTS = DIR / "data/live/libro_snapshots.csv"
MARKETS_GLOB = str(DIR / "data/markets/*.csv")
OUT_CSV = DIR / "data/shadow/ballenas_veto_analisis.csv"
DATA_API = "https://data-api.polymarket.com"
LOOKBACK_S = 90       # ventana antes de la señal para contar flujo grande
CLIP_GRANDE_USD = 20  # umbral "clip grande": mediana observada de wowitsamazing ~28$
N_MIN_LECTURA = 15
N_MIN_DECISION = 30

PRIORIDAD = ["ejecutada", "fok_kill", "abort_requote", "veto_profundidad",
             "veto_sin_datos", "no_viable_stake", "fuera_ventana"]


def _prio(motivo: str) -> int:
    try:
        return PRIORIDAD.index(motivo)
    except ValueError:
        return len(PRIORIDAD)


def senales_unicas() -> dict:
    """(market_id, strategy, direction) -> fila con menor prioridad (más lejos
    llegó en el pipeline). Solo interesa ejecutada / veto_profundidad."""
    senales = {}
    with open(SNAPSHOTS, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            key = (r["market_id"], r["strategy"], r["direction"])
            prev = senales.get(key)
            if prev is None or _prio(r["motivo"]) < _prio(prev["motivo"]):
                senales[key] = r
    return {k: v for k, v in senales.items()
            if v["motivo"] in ("ejecutada", "veto_profundidad")}


def mapear_condition_ids(market_ids: set) -> dict:
    """market_id -> {condition_id, end_date}. grep dirigido: los CSV de markets
    pesan >600MB/día, parsear todo con csv.DictReader sería minutos por día.
    -h suprime el prefijo "fichero:" (si no, csv.reader lo cuela como campo 0
    y desplaza todas las columnas); csv.reader real (no split(",") ingenuo)
    porque "question" lleva comas dentro de comillas — un split a pelo
    desplaza condition_id/end_date en la mayoría de las filas."""
    ids_file = "/tmp/_ballenas_ids.txt"
    Path(ids_file).write_text("\n".join(sorted(market_ids)))
    try:
        out = subprocess.run(
            ["grep", "-h", "-F", "-f", ids_file] + sorted(glob.glob(MARKETS_GLOB)),
            capture_output=True, text=True, timeout=120,
        ).stdout
    finally:
        Path(ids_file).unlink(missing_ok=True)

    mapa = {}
    for parts in csv.reader(out.splitlines()):
        if len(parts) < 6:
            continue
        mid = parts[1]
        if mid in market_ids and mid not in mapa:
            # header: timestamp_utc,market_id,condition_id,question,slug,end_date,...
            mapa[mid] = {"condition_id": parts[2], "end_date": parts[5]}
    return mapa


def fetch_trades(condition_id: str) -> list:
    try:
        r = requests.get(f"{DATA_API}/trades",
                         params={"market": condition_id, "limit": 500}, timeout=15)
        r.raise_for_status()
        return r.json() or []
    except Exception:
        return []


def flujo_previo(trades: list, lado: str, ts_senal: datetime) -> tuple:
    """(volumen_usdc_previo, clip_max_usdc, n_trades) del mismo lado en
    [ts_senal - LOOKBACK_S, ts_senal]."""
    t_ini = ts_senal - timedelta(seconds=LOOKBACK_S)
    vol = 0.0
    clip_max = 0.0
    n = 0
    for t in trades:
        if t.get("outcome") != lado:
            continue
        try:
            tt = datetime.fromtimestamp(int(t["timestamp"]), tz=timezone.utc)
            usdc = float(t.get("usdcSize") or (t.get("size", 0) * t.get("price", 0)))
        except Exception:
            continue
        if t_ini <= tt <= ts_senal:
            vol += usdc
            clip_max = max(clip_max, usdc)
            n += 1
    return vol, clip_max, n


def mann_whitney_u(a: list, b: list) -> tuple:
    """U de Mann-Whitney + aproximación normal (con corrección por empates).
    Devuelve (U, z, p_dos_colas). Sin scipy — implementación directa del
    ranking combinado, estándar (Mann & Whitney 1947)."""
    combinado = sorted([(v, 0) for v in a] + [(v, 1) for v in b])
    n1, n2 = len(a), len(b)
    ranks = [0.0] * len(combinado)
    i = 0
    while i < len(combinado):
        j = i
        while j < len(combinado) and combinado[j][0] == combinado[i][0]:
            j += 1
        rango_medio = (i + 1 + j) / 2.0  # rangos 1-indexados, promediados en empates
        for k in range(i, j):
            ranks[k] = rango_medio
        i = j
    r1 = sum(ranks[k] for k in range(len(combinado)) if combinado[k][1] == 0)
    u1 = r1 - n1 * (n1 + 1) / 2.0
    u2 = n1 * n2 - u1
    u = min(u1, u2)
    mu = n1 * n2 / 2.0
    # corrección por empates en la varianza
    empates = defaultdict(int)
    for v, _ in combinado:
        empates[v] += 1
    N = n1 + n2
    correccion = sum(t ** 3 - t for t in empates.values())
    sigma2 = (n1 * n2 / 12.0) * ((N + 1) - correccion / (N * (N - 1))) if N > 1 else 0
    if sigma2 <= 0:
        return u, 0.0, 1.0
    z = (u - mu) / math.sqrt(sigma2)
    p = 2 * (1 - _norm_cdf(abs(z)))
    return u, z, min(p, 1.0)


def _norm_cdf(z: float) -> float:
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def main():
    senales = senales_unicas()
    print(f"señales únicas ejecutada+veto_profundidad: {len(senales)}")

    ids = set(k[0] for k in senales)
    mapa_ids = mapear_condition_ids(ids)
    print(f"mapeados a condition_id: {len(mapa_ids)}/{len(ids)}")

    filas = []
    cache_trades = {}
    for (market_id, strategy, direction), r in senales.items():
        info = mapa_ids.get(market_id)
        if not info or not info["condition_id"]:
            continue
        try:
            ts_senal = datetime.fromisoformat(r["timestamp_utc"].replace("Z", "+00:00"))
            end_dt = datetime.fromisoformat(info["end_date"].replace("Z", "+00:00"))
            if end_dt.tzinfo is None:
                end_dt = end_dt.replace(tzinfo=timezone.utc)
        except Exception:
            continue
        restante_min = (end_dt - ts_senal).total_seconds() / 60.0

        cid = info["condition_id"]
        if cid not in cache_trades:
            cache_trades[cid] = fetch_trades(cid)
            time.sleep(0.15)
        trades = cache_trades[cid]

        lado = "Up" if direction == "BUY_YES" else "Down"
        vol, clip_max, n_trades = flujo_previo(trades, lado, ts_senal)

        filas.append({
            "market_id": market_id, "strategy": strategy, "direction": direction,
            "motivo": r["motivo"], "restante_min": round(restante_min, 2),
            "vol_previo_usdc": round(vol, 2), "clip_max_usdc": round(clip_max, 2),
            "n_trades_previos": n_trades,
            "ratio_vs_stake": r.get("ratio_vs_stake", ""),
        })

    if not filas:
        print("Sin filas cruzadas — no se puede concluir nada.")
        return 1

    with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0].keys()))
        w.writeheader()
        w.writerows(filas)
    print(f"guardado: {OUT_CSV} ({len(filas)} filas)")

    ejecutada = [f for f in filas if f["motivo"] == "ejecutada"]
    veto = [f for f in filas if f["motivo"] == "veto_profundidad"]
    print(f"\nn ejecutada={len(ejecutada)} | n veto_profundidad={len(veto)}")

    if len(ejecutada) < N_MIN_LECTURA or len(veto) < N_MIN_LECTURA:
        print(f"\n⚠️ n<{N_MIN_LECTURA} en algún grupo — NO SE PUEDE CONCLUIR. "
              "Solo se reportan los números crudos, sin veredicto.")

    # confound: restante_min por grupo (¿el veto pasa simplemente más tarde en la ventana?)
    rm_ej = [f["restante_min"] for f in ejecutada]
    rm_veto = [f["restante_min"] for f in veto]
    print(f"\nrestante_min ejecutada: mediana={statistics.median(rm_ej):.2f}" if rm_ej else "")
    print(f"restante_min veto_profundidad: mediana={statistics.median(rm_veto):.2f}" if rm_veto else "")

    # comparacion principal: volumen previo del mismo lado
    vol_ej = [f["vol_previo_usdc"] for f in ejecutada]
    vol_veto = [f["vol_previo_usdc"] for f in veto]
    if vol_ej and vol_veto:
        print(f"\nvol_previo_usdc (lookback {LOOKBACK_S}s, mismo lado):")
        print(f"  ejecutada:         mediana=${statistics.median(vol_ej):.2f}  "
              f"p75=${sorted(vol_ej)[3*len(vol_ej)//4]:.2f}")
        print(f"  veto_profundidad:  mediana=${statistics.median(vol_veto):.2f}  "
              f"p75=${sorted(vol_veto)[3*len(vol_veto)//4]:.2f}")
        if len(vol_ej) >= N_MIN_LECTURA and len(vol_veto) >= N_MIN_LECTURA:
            u, z, p = mann_whitney_u(vol_ej, vol_veto)
            print(f"  Mann-Whitney U={u:.1f} z={z:.2f} p={p:.4f} "
                  f"({'SIGNIFICATIVO' if p < 0.05 else 'no significativo'} a α=0.05)")

    clip_ej = [f["clip_max_usdc"] for f in ejecutada]
    clip_veto = [f["clip_max_usdc"] for f in veto]
    if clip_ej and clip_veto:
        print(f"\nclip_max_usdc previo (>={CLIP_GRANDE_USD}$ = 'clip grande'):")
        print(f"  ejecutada:         mediana=${statistics.median(clip_ej):.2f}  "
              f"con clip grande: {sum(1 for c in clip_ej if c>=CLIP_GRANDE_USD)}/{len(clip_ej)}")
        print(f"  veto_profundidad:  mediana=${statistics.median(clip_veto):.2f}  "
              f"con clip grande: {sum(1 for c in clip_veto if c>=CLIP_GRANDE_USD)}/{len(clip_veto)}")
        if len(clip_ej) >= N_MIN_LECTURA and len(clip_veto) >= N_MIN_LECTURA:
            u, z, p = mann_whitney_u(clip_ej, clip_veto)
            print(f"  Mann-Whitney U={u:.1f} z={z:.2f} p={p:.4f} "
                  f"({'SIGNIFICATIVO' if p < 0.05 else 'no significativo'} a α=0.05)")

    n_total = len(ejecutada) + len(veto)
    if n_total >= N_MIN_DECISION and len(ejecutada) >= N_MIN_LECTURA and len(veto) >= N_MIN_LECTURA:
        print(f"\n✅ n={n_total}≥{N_MIN_DECISION}: gate de decisión alcanzado, ver p-valor arriba.")
    else:
        print(f"\n⏳ n={n_total}<{N_MIN_DECISION}: acumular más antes de decidir "
              "(re-correr este script en unos días con más señales).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
