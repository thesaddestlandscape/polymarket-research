#!/usr/bin/env python3
"""
dryrun_mejora_contraria_02sep.py — DRY_RUN de decisión forward (sin
dinero real) para los 2 candidatos con doble confirmación de la sesión
02-Sep (pnl_fiel_v2 positivo + gate mejora_contraria>=2x significativo):
BALLENAS_TARDIAS#BTC#15min#BUY_YES y LIQUIDACIONES_5M#ETH#5min#BUY_YES.

Petición explícita Javi (02-Sep, "se podría hacer un dry-run para ver
cómo se comportan"): antes de tocar pares_permitidos_live, medir hacia
ADELANTE (no retrospectivo como el análisis de sesión que encontró el
patrón) si el filtro habría acertado, sin arriesgar ni un céntimo.

Diseño deliberado -- NO duplica el polling del libro contrario: ese
trabajo YA lo hace fade_depth_universal_fase0.py (screen "observadores")
para CUALQUIER estrategia con ratio_vs_stake>=5x, incluidas estas 2 (ya
verificado: 429 y 92 filas respectivamente en fade_depth_universal_
fase0.csv). Este script solo TAIL-ea ese CSV, filtra las 2 tuplas
objetivo, decide "habría_operado" = mejora_contraria(ratio_max/ratio_
inicial>=2) -- exactamente la misma condición usada en el hallazgo de
sesión, pero evaluada AL VUELO según van llegando filas nuevas, nunca
mirando el futuro de la señal. El resolver (--resolver, cron aparte)
rellena el outcome real después, cuando el mercado resuelve -- la
DECISIÓN queda registrada antes de conocer el resultado, así que no hay
look-ahead bias pese a que el join final ocurra más tarde.

Puramente observacional: NO coloca, cancela ni modifica ninguna orden
real, no importa ninguna función de ejecución de live_trade.py, no toca
pares_permitidos_live. Mismo criterio de riesgo que el resto de *_fase0.py.

Uso:
  .venv/bin/python dryrun_mejora_contraria_02sep.py            # loop tail (screen)
  .venv/bin/python dryrun_mejora_contraria_02sep.py --resolver # cron, rellena outcomes
"""
import csv
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
FADE = REPO / "data" / "shadow" / "fade_depth_universal_fase0.csv"
RESULTS = REPO / "data" / "shadow" / "results.csv"
OUT = REPO / "data" / "shadow" / "dryrun_mejora_contraria.csv"

UMBRAL_MEJORA = 2.0
CICLO_TAIL_S = 15.0
STAKE_SIMULADO = 1.05

OBJETIVOS = {
    ("BALLENAS_TARDIAS", "BTC#15min", "BUY_YES"),
    ("LIQUIDACIONES_5M", "ETH#5min", "BUY_YES"),
}

COLUMNS = [
    "evento_timestamp_utc", "market_id", "strategy", "subtype", "direction",
    "precio_original", "ratio_original", "ratio_contrario_inicial",
    "ratio_contrario_max", "mejora_contraria", "habria_operado",
    "acierto", "pnl_neto_dryrun", "resolved_ts",
]


def _log(msg: str) -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts}] {msg}", flush=True)


def _cargar_vistos() -> set:
    if not OUT.exists():
        return set()
    with open(OUT, encoding="utf-8") as f:
        return {(r["evento_timestamp_utc"], r["market_id"]) for r in csv.DictReader(f)}


def _escribir_fila(fila: dict) -> None:
    nuevo = not OUT.exists()
    with open(OUT, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        if nuevo:
            w.writeheader()
        w.writerow(fila)


def modo_loop() -> None:
    pos = FADE.stat().st_size if FADE.exists() else 0
    header = None
    if FADE.exists():
        with open(FADE, encoding="utf-8") as f:
            primera = f.readline()
            if primera:
                header = next(csv.reader([primera]))
    vistos = _cargar_vistos()
    _log(f"arrancado -- tail desde byte {pos}, {len(vistos)} eventos ya registrados, "
         f"objetivos: {sorted(OBJETIVOS)}")

    while True:
        try:
            if FADE.exists():
                tam = FADE.stat().st_size
                if tam < pos:
                    pos, header = 0, None
                if tam > pos:
                    with open(FADE, encoding="utf-8") as f:
                        f.seek(pos)
                        nuevas = f.readlines()
                        pos = f.tell()
                    if header is None and nuevas:
                        header = next(csv.reader([nuevas[0]]))
                        nuevas = nuevas[1:]
                    for row in csv.DictReader(nuevas, fieldnames=header):
                        clave_obj = (row.get("strategy"), row.get("subtype"), row.get("direction"))
                        if clave_obj not in OBJETIVOS:
                            continue
                        clave = (row.get("evento_timestamp_utc"), row.get("market_id"))
                        if clave in vistos:
                            continue
                        vistos.add(clave)
                        try:
                            ini = float(row["ratio_contrario_inicial"])
                            mx = float(row["ratio_contrario_max"])
                        except (TypeError, ValueError):
                            continue
                        mejora = (mx / ini >= UMBRAL_MEJORA) if ini > 0 else (mx > 0)
                        fila = {
                            "evento_timestamp_utc": row["evento_timestamp_utc"],
                            "market_id": row["market_id"], "strategy": row["strategy"],
                            "subtype": row["subtype"], "direction": row["direction"],
                            "precio_original": row["precio_original"],
                            "ratio_original": row["ratio_original"],
                            "ratio_contrario_inicial": ini, "ratio_contrario_max": mx,
                            "mejora_contraria": mejora, "habria_operado": mejora,
                            "acierto": "", "pnl_neto_dryrun": "", "resolved_ts": "",
                        }
                        _escribir_fila(fila)
                        _log(f"[{row['market_id']}] {row['strategy']}#{row['subtype']} "
                             f"mejora_contraria={mejora} habria_operado={mejora}")
        except Exception as e:
            _log(f"error en ciclo: {e}")
        time.sleep(CICLO_TAIL_S)


def modo_resolver() -> None:
    """Rellena acierto/pnl_neto_dryrun para filas ya resueltas en results.csv."""
    if not OUT.exists():
        _log("nada que resolver -- fichero de salida no existe todavía")
        return
    with open(OUT, encoding="utf-8") as f:
        filas = list(csv.DictReader(f))
    pendientes = {(r["strategy"], r["subtype"], r["market_id"]) for r in filas if not r.get("acierto")}
    if not pendientes:
        _log("nada pendiente de resolver")
        return
    resueltos = {}
    with open(RESULTS, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            clave = (row.get("strategy"), row.get("subtype"), row.get("market_id"))
            if clave in pendientes and row.get("acierto") in ("0", "1"):
                resueltos[clave] = (row.get("acierto"), row.get("pnl_neto"))

    n_actualizados = 0
    for r in filas:
        clave = (r["strategy"], r["subtype"], r["market_id"])
        if clave in resueltos and not r.get("acierto"):
            acierto, pnl = resueltos[clave]
            r["acierto"] = acierto
            r["pnl_neto_dryrun"] = pnl
            r["resolved_ts"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
            n_actualizados += 1

    if n_actualizados:
        with open(OUT, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=COLUMNS)
            w.writeheader()
            w.writerows(filas)
    _log(f"resueltas {n_actualizados} filas nuevas ({len(pendientes) - n_actualizados} siguen pendientes)")

    # resumen rápido, separado por habria_operado
    for objetivo in OBJETIVOS:
        key = f"{objetivo[0]}#{objetivo[1]}"
        subset = [r for r in filas if f"{r['strategy']}#{r['subtype']}" == key and r.get("acierto")]
        for grupo, etiqueta in ((True, "habria_operado"), (False, "no_habria_operado")):
            vals = [r for r in subset if r["habria_operado"] == str(grupo)]
            n = len(vals)
            if n == 0:
                continue
            hits = sum(1 for r in vals if r["acierto"] == "1")
            pnls = [float(r["pnl_neto_dryrun"]) for r in vals if r.get("pnl_neto_dryrun")]
            pnl_m = sum(pnls) / len(pnls) if pnls else None
            print(f"  {key:35s} {etiqueta:18s} n={n:4d} hit={hits/n*100:5.1f}% "
                  f"pnl_medio={f'{pnl_m:+.4f}' if pnl_m is not None else 'n/d'}")


if __name__ == "__main__":
    if "--resolver" in sys.argv:
        modo_resolver()
    else:
        modo_loop()
