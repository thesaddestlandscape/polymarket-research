#!/usr/bin/env python3
"""perps_consenso_dryrun.py -- (22-Sep, PLAN 22-Sep paso 2, directiva
explícita Javi 21-Sep: "replicaremos consensum wallets para perps y lo
ponemos en dry_run"). MODO DRY-RUN: nunca envía ninguna orden, no hay cuenta
de Perps configurada, no toca dinero. Ver [[project_perps_estado_y_plan_22sep]].

## Mecanismo (mismo patrón que _bots_consenso() en bot_consenso_lib.py,
## replicado para Perps -- consenso MAYORITARIO simple, sin ponderar)
1. Wallets cualificadas: usando `perps_posiciones.csv` (perps_rastreador_
   posiciones.py, unidad = POSICIÓN cerrada, no fill -- ver ese script para
   el porqué), una wallet cualifica si tiene >=MIN_POSICIONES posiciones
   CERRADAS con pnl_total medio > 0. Con los datos de hoy esto es un
   conjunto MUY pequeño (memoria 21-Sep: solo 2 wallets con >=20 posiciones
   independientes) -- se documenta explícitamente en el log cada corrida,
   no se oculta la escasez.
2. Voto por instrumento: de las wallets cualificadas, las que tienen una
   posición ABIERTA ahora mismo en ese instrumento votan por su lado
   (long/short). Consenso = lado mayoritario, n_votos = nº de wallets
   distintas votando, pct = mayoría/n_votos.
3. Señal DRY-RUN: si n_votos>=MIN_VOTOS y pct>=MIN_PCT Y es una señal NUEVA
   (no se repite mientras el consenso no cambie -- dedup por (instrument_id,
   lado)), se loguea con el precio de mercado más reciente (`open_price` de
   polymarket_perps_market_*.csv) como precio de entrada simulado.
4. `--resolver`: para señales con más de HORIZONTE_H horas, busca el precio
   de mercado en ese horizonte (o el más cercano posterior) y calcula PnL
   simulado neto de fee taker (0,04%) -- funding NO incluido en V1 (Perps
   cobra funding por hora, requiere integrar la serie completa entre
   apertura y cierre; documentado como limitación explícita, no fingida).

## Limitaciones explícitas (no ocultar)
- Conjunto de wallets cualificadas hoy es pequeño y basado en poca historia
  -- esto es exploratorio, NO un gate riguroso (ver gate_dias_independientes.
  py / shuffle+BH-FDR de los demás gates del proyecto, que aquí NO se
  aplican todavía por falta de n).
- No incluye funding ni slippage del libro real, solo el precio de
  referencia `open_price` del snapshot cada 15min.
- Nunca ejecuta nada real -- sin credenciales de Perps en absoluto.
"""
import csv
import glob
import json
import sys
from bisect import bisect_left
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
from perps_rastreador_posiciones import cargar_fills, segmentar_posiciones  # noqa: E402

OUT = REPO / "data/shadow/perps_consenso_dryrun.csv"
STATS = REPO / "data/shadow/perps_consenso_stats.json"
GLOB_MARKET = str(REPO / "data/shadow/polymarket_perps_market_*.csv")

MIN_POSICIONES = 3       # posiciones CERRADAS mínimas para cualificar una wallet
MIN_VOTOS = 3             # wallets distintas votando el mismo lado
MIN_PCT = 0.66            # mayoría mínima (2/3)
HORIZONTE_H = 4           # horizonte de resolución del dry-run
FEE_TAKER = 0.0004

COLUMNS = ["ts_senal", "instrument_id", "symbol", "lado_consenso", "n_votos",
          "n_cualificadas_total", "pct_mayoria", "wallets_votantes",
          "precio_entrada", "ts_resuelto", "precio_salida", "horas_reales",
          "pnl_pct_neto", "resuelto"]


def _wallets_cualificadas(posiciones: list) -> dict:
    """address -> {"n": int, "pnl_medio": float}. Solo posiciones cerradas."""
    por_wallet = {}
    agg = {}
    for p in posiciones:
        if p["abierta"]:
            continue
        agg.setdefault(p["address"], []).append(p["pnl_total"])
    for w, pnls in agg.items():
        n = len(pnls)
        if n < MIN_POSICIONES:
            continue
        pnl_medio = sum(pnls) / n
        if pnl_medio <= 0:
            continue
        por_wallet[w] = {"n": n, "pnl_medio": round(pnl_medio, 4)}
    return por_wallet


def _consenso_actual(posiciones: list, cualificadas: dict) -> dict:
    """instrument_id -> {"symbol", "lado", "n_votos", "n_total", "pct", "wallets"}"""
    votos_por_instrumento: dict = {}
    for p in posiciones:
        if not p["abierta"]:
            continue
        w = p["address"]
        if w not in cualificadas:
            continue
        inst = p["instrument_id"]
        votos_por_instrumento.setdefault(inst, {"symbol": p["symbol"], "votos": {}, "wallets": {}})
        lado = p["lado_apertura"]
        entry = votos_por_instrumento[inst]
        entry["votos"][lado] = entry["votos"].get(lado, 0) + 1
        entry["wallets"].setdefault(lado, []).append(w)

    resultado = {}
    for inst, d in votos_por_instrumento.items():
        n_total = sum(d["votos"].values())
        if n_total == 0:
            continue
        lado_mayoria = max(d["votos"], key=d["votos"].get)
        n_votos = d["votos"][lado_mayoria]
        resultado[inst] = {
            "symbol": d["symbol"], "lado": lado_mayoria, "n_votos": n_votos,
            "n_total": n_total, "pct": round(n_votos / n_total, 4),
            "wallets": d["wallets"][lado_mayoria],
        }
    return resultado


def _ultimo_precio_por_instrumento() -> dict:
    """instrument_id (str) -> (ts, open_price) del snapshot más reciente."""
    precios = {}
    for arch in sorted(glob.glob(GLOB_MARKET)):
        with open(arch, encoding="utf-8") as f:
            for r in csv.DictReader(f):
                inst = r.get("instrument_id", "")
                ts = r.get("timestamp_utc", "")
                try:
                    p = float(r.get("open_price") or "")
                except (TypeError, ValueError):
                    continue
                actual = precios.get(inst)
                if actual is None or ts > actual[0]:
                    precios[inst] = (ts, p)
    return precios


def _indice_precios_por_instrumento() -> dict:
    """instrument_id -> [(ts, price), ...] ordenado, UNA sola pasada por
    todos los ficheros de mercado. /code-review 22-Sep: la versión anterior
    (_precio_en_horizonte) re-escaneaba TODOS los CSV de mercado por cada
    señal sin resolver -- O(n_señales x n_filas_mercado), mismo patrón de
    timeout por crecimiento ya visto 3 veces en este proyecto (vigia_gate_
    bucket_propio/calibracion/wallet_mirror, CLAUDE.md pt.18)."""
    idx = defaultdict(list)
    for arch in sorted(glob.glob(GLOB_MARKET)):
        with open(arch, encoding="utf-8") as f:
            for r in csv.DictReader(f):
                inst = r.get("instrument_id", "")
                ts = r.get("timestamp_utc", "")
                try:
                    p = float(r.get("open_price") or "")
                except (TypeError, ValueError):
                    continue
                idx[inst].append((ts, p))
    for inst in idx:
        idx[inst].sort(key=lambda x: x[0])
    return idx


def _precio_en_horizonte(indice: dict, instrument_id: str, ts_objetivo: str) -> tuple:
    """Primer (ts, price) con ts >= ts_objetivo para ese instrumento, vía
    bisect sobre el índice ya construido. None si el horizonte aún no se
    alcanzó en los datos capturados."""
    serie = indice.get(instrument_id)
    if not serie:
        return None
    tss = [x[0] for x in serie]
    i = bisect_left(tss, ts_objetivo)
    return serie[i] if i < len(serie) else None


def _cargar_out() -> list:
    if not OUT.exists():
        return []
    with open(OUT, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _guardar_out(filas: list) -> None:
    tmp = OUT.with_suffix(".tmp")
    with open(tmp, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        w.writeheader()
        w.writerows(filas)
    tmp.replace(OUT)


def generar_senales() -> int:
    grupos = cargar_fills()
    # segmentar_posiciones() opera por (wallet,instrumento) sola, hay que
    # re-adjuntar address/instrument_id -- se hace en el propio bucle:
    posiciones_full = []
    for (address, instrument_id), fills in grupos.items():
        for p in segmentar_posiciones(fills):
            p2 = dict(p)
            p2["address"] = address
            p2["instrument_id"] = instrument_id
            posiciones_full.append(p2)

    cualificadas = _wallets_cualificadas(posiciones_full)
    print(f"[perps_consenso_dryrun] {len(cualificadas)} wallets cualificadas "
          f"(>={MIN_POSICIONES} posiciones cerradas, pnl medio>0) de "
          f"{len({p['address'] for p in posiciones_full})} wallets totales con posiciones")

    consenso = _consenso_actual(posiciones_full, cualificadas)
    precios = _ultimo_precio_por_instrumento()

    existentes = _cargar_out()
    activas = {(f["instrument_id"], f["lado_consenso"]) for f in existentes if f["resuelto"] != "1"}

    nuevas = []
    ahora = datetime.now(timezone.utc).isoformat(timespec="seconds")
    for inst, d in consenso.items():
        if d["n_votos"] < MIN_VOTOS or d["pct"] < MIN_PCT:
            continue
        clave = (inst, d["lado"])
        if clave in activas:
            continue
        precio_ts_p = precios.get(inst)
        if precio_ts_p is None:
            continue
        nuevas.append({
            "ts_senal": ahora, "instrument_id": inst, "symbol": d["symbol"],
            "lado_consenso": d["lado"], "n_votos": d["n_votos"],
            "n_cualificadas_total": len(cualificadas), "pct_mayoria": d["pct"],
            "wallets_votantes": "|".join(sorted(d["wallets"])),
            "precio_entrada": precio_ts_p[1], "ts_resuelto": "", "precio_salida": "",
            "horas_reales": "", "pnl_pct_neto": "", "resuelto": "0",
        })

    if nuevas:
        print(f"[perps_consenso_dryrun] {len(nuevas)} señal(es) NUEVA(S) de consenso")
        for n in nuevas:
            print(f"  {n['symbol']} {n['lado_consenso']} n_votos={n['n_votos']}/"
                  f"{n['n_cualificadas_total']} pct={n['pct_mayoria']:.0%} "
                  f"precio={n['precio_entrada']}")
        _guardar_out(existentes + nuevas)
    else:
        print("[perps_consenso_dryrun] sin señales nuevas")

    # 22-Sep: snapshot de estado para vigia_perps_consenso.py -- así el
    # aviso de Telegram ("cada vez que haya una actualización de datos")
    # puede reportar deltas sin tener que releer todos los CSV otra vez.
    n_fills = sum(len(fills) for fills in grupos.values())
    STATS.write_text(json.dumps({
        "generado_utc": ahora, "n_fills": n_fills,
        "n_wallets_con_posiciones": len({p["address"] for p in posiciones_full}),
        "n_posiciones_total": len(posiciones_full),
        "n_posiciones_cerradas": sum(1 for p in posiciones_full if not p["abierta"]),
        "n_cualificadas": len(cualificadas),
        "n_instrumentos_con_consenso_parcial": len(consenso),
        "n_senales_nuevas": len(nuevas),
    }, ensure_ascii=False, indent=1), encoding="utf-8")
    return 0


def resolver() -> int:
    filas = _cargar_out()
    if not filas:
        print("[perps_consenso_dryrun --resolver] sin datos")
        return 0
    pendientes = [f for f in filas if f["resuelto"] != "1"]
    if not pendientes:
        print("[perps_consenso_dryrun --resolver] nada pendiente")
        return 0
    indice = _indice_precios_por_instrumento()
    ahora = datetime.now(timezone.utc)
    n_resueltas = 0
    for f in pendientes:
        ts_senal = datetime.fromisoformat(f["ts_senal"])
        objetivo = ts_senal + timedelta(hours=HORIZONTE_H)
        if ahora < objetivo:
            continue
        r = _precio_en_horizonte(indice, f["instrument_id"], objetivo.isoformat(timespec="seconds"))
        if r is None:
            continue
        ts_salida, precio_salida = r
        entrada = float(f["precio_entrada"])
        if entrada <= 0:
            continue
        if f["lado_consenso"] == "long":
            ret = precio_salida / entrada - 1
        else:
            ret = entrada / precio_salida - 1
        # /code-review 22-Sep: round-trip real paga 2 fees taker (entrada +
        # salida), no 1 -- ambos fills son taker en el modelo de este script.
        ret_neto = ret - 2 * FEE_TAKER  # sin funding, ver limitaciones del docstring
        horas_reales = (datetime.fromisoformat(ts_salida) - ts_senal).total_seconds() / 3600
        f.update({"ts_resuelto": ts_salida, "precio_salida": precio_salida,
                  "horas_reales": round(horas_reales, 2),
                  "pnl_pct_neto": round(ret_neto, 6), "resuelto": "1"})
        n_resueltas += 1
    if n_resueltas:
        _guardar_out(filas)
    print(f"[perps_consenso_dryrun --resolver] {n_resueltas} señal(es) resuelta(s)")
    return 0


def main() -> int:
    if "--resolver" in sys.argv:
        return resolver()
    return generar_senales()


if __name__ == "__main__":
    raise SystemExit(main())
