#!/usr/bin/env python3
"""
fade_depth_universal_fase0.py — FASE 0 (SOLO OBSERVACIÓN), 14-Ago,
petición explícita Javi tras el hallazgo de sesión (Stage 0, barrido de
candidatos_evaluacion_live): la selección adversa que motivó
gbmlate_fade_depth_fase0.py (12-Ago, solo familia GBM_LATE) NO es un
caso aislado -- es sistémica. Diagnóstico nuevo aplicado a los 82
candidatos que pasan el gate IC básico (n>=40, ic>=0.08): para cada uno,
`gap = hit_real_en_subconjunto_fillable - calibración_esperada_por_precio`
(colapsado por market_id, ratio_vs_stake>=5x, mismo criterio que
analisis_fills.py). Resultado: **79 de 82 candidatos tienen gap NEGATIVO**
(-1% a -26.6%) -- cuando el libro del lado propio está lleno, el acierto
real se desploma muy por debajo de lo que el precio implica, en casi
TODA la familia FAVORITO_CONFIRMADO (todas sus variantes) y GBM_LATE
(todas sus variantes), no solo GBM_LATE. Los 3 únicos con gap ~0/positivo
coinciden con las tuplas que YA funcionan en vivo (FAVORITO_CONFIRMADO#
BTC#60min#BUY_NO, +2.2%) -- confirma que el gap es el mecanismo real
detrás de por qué unas tuplas ganan y otras no.

Verificado con rigor completo en el candidato más fuerte
(FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES, n=1658):
hit real=53.1% vs calibración=77.1% (gap -24%), fade simulado con precio
complementario: pnl total +3.379€, bootstrap CI90%=[3018€,3744€] (no
cruza cero), shuffle p=0.0000 contra el nulo calibrado, split-half
consistente en ambas mitades (+0.934€/tr y +3.141€/tr). Ver memoria
idea_fade_universal_gap_sistemico_14ago para el barrido completo (79
tuplas, gap por tupla) y el detalle de la verificación.

Lo que falta, igual que en el caso GBM_LATE original: esa simulación
asume que el lado CONTRARIO (barato, minoritario) también tiene
profundidad ejecutable -- dato que HOY no se mide para ninguna
estrategia salvo GBM_LATE (gbmlate_fade_depth_fase0.py, 12-Ago) y
WEEKLY_PRICE (weeklyprice_fade_depth_fase0.py, 13-Ago, mecanismo
distinto por duración de mercado semanal). Este script GENERALIZA el
mecanismo de gbmlate_fade_depth_fase0.py (mismo código, mismo umbral,
mismo patrón de polling) a CUALQUIER estrategia -- no se clona un
fichero por familia (79 candidatos harían inmanejable el mantenimiento),
se quita el filtro `FAMILIAS_PREFIJO` y se deja pasar cualquier señal
"candidato_evaluacion" con ratio_vs_stake>=5x, EXCEPTO WEEKLY_PRICE (ya
cubierta por su propio mecanismo, evita doble consulta al mismo evento).

SUSTITUYE a gbmlate_fade_depth_fase0.py (que queda retirado de
observadores_fase0.py el mismo día -- este script es un superset
estricto, mantener ambos duplicaría consultas al libro sobre los MISMOS
eventos GBM_LATE). gbmlate_fade_depth_fase0.csv NO se borra (histórico
válido), pero deja de crecer -- fade_depth_universal_fase0.csv es la
fuente de verdad desde hoy.

Mecanismo (idéntico a gbmlate_fade_depth_fase0.py, reusa
`lt._consultar_profundidad_libro`, solo lectura, nunca ordena):
  1. Vigila data/live/libro_snapshots.csv por filas NUEVAS de CUALQUIER
     estrategia (salvo WEEKLY_PRICE) con motivo=candidato_evaluacion Y
     ratio_vs_stake>=RATIO_OBJETIVO -- la población "fillable" en el lado
     propio, exactamente la que el diagnóstico de gap señala como
     sistemáticamente adversa.
  2. Para cada evento nuevo, consulta el libro público del lado
     CONTRARIO cada POLL_INTERVAL_S durante VENTANA_S.
  3. Persiste en data/shadow/fade_depth_universal_fase0.csv: identidad
     de la señal, ratio/precio del lado original, y la serie temporal de
     ratio/ask del lado contrario. Un análisis posterior (desagregado por
     estrategia/activo/marco, CLAUDE.md pt.17) cruza con outcome_real
     para responder, tupla a tupla: el lado contrario ¿tenía profundidad
     ejecutable, o esconde el mismo libro vacío que el resto del
     proyecto?

NO coloca, cancela ni modifica ninguna orden real, no llama a ninguna
función de ejecución de live_trade.py, no toca pares_permitidos_live ni
candidatos_evaluacion_live -- puramente observacional, mismo criterio de
riesgo que el resto de la familia *_fase0.py.

Se fusiona en observadores_fase0.py (screen "observadores") como los
demás -- NUNCA lanzar una screen suelta para este script.
"""
import csv
import json
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

import live_trade as lt

REPO = Path(__file__).resolve().parent
DIR_SHADOW = REPO / "data" / "shadow"
LIBRO_SNAPSHOTS = REPO / "data" / "live" / "libro_snapshots.csv"
OUT = DIR_SHADOW / "fade_depth_universal_fase0.csv"

POLL_INTERVAL_S = 5.0
VENTANA_S = 30.0
RATIO_OBJETIVO = 5.0       # mismo umbral "fillable" que veto_profundidad/analisis_fills.py
CICLO_TAIL_S = 3.0
MAX_HILOS_CONCURRENTES = 12  # 14-Ago: subido de 8 (solo-GBM_LATE) a 12 -- volumen
                             # universal ~5x mayor (1458 eventos/día vs 301 solo GBM_LATE,
                             # medido 14-Ago), pero cada evento solo ocupa el hilo 30s.
ESTRATEGIAS_EXCLUIDAS = ("WEEKLY_PRICE",)  # ya cubierta por weeklyprice_fade_depth_fase0.py
                                            # (mecanismo distinto, mercados semanales)

COLUMNS = [
    "evento_timestamp_utc", "market_id", "strategy", "subtype", "direction",
    "precio_original", "stake_eur", "ratio_original",
    "precio_contrario", "muestras_json",  # [[t_offset_s, ratio_contrario, ask_contrario], ...]
    "ratio_contrario_inicial", "ratio_contrario_max", "ratio_contrario_min",
]


def _es_evento_relevante(fila: dict) -> bool:
    if fila.get("motivo") != "candidato_evaluacion":
        return False
    if str(fila.get("strategy", "")).startswith(ESTRATEGIAS_EXCLUIDAS):
        return False
    try:
        return float(fila.get("ratio_vs_stake") or 0.0) >= RATIO_OBJETIVO
    except (TypeError, ValueError):
        return False


_lock_out = threading.Lock()
_vistos = set()
_sem = threading.Semaphore(MAX_HILOS_CONCURRENTES)
_libro_pos = 0
_libro_header: list[str] | None = None


def _log(msg: str) -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts}] {msg}", flush=True)


def _iniciar_tail_libro() -> None:
    global _libro_pos, _libro_header
    if not LIBRO_SNAPSHOTS.exists():
        return
    with open(LIBRO_SNAPSHOTS, encoding="utf-8") as f:
        primera = f.readline()
        if primera:
            _libro_header = next(csv.reader([primera]))
    _libro_pos = LIBRO_SNAPSHOTS.stat().st_size


def _leer_filas_nuevas() -> list:
    global _libro_pos, _libro_header
    if not LIBRO_SNAPSHOTS.exists() or _libro_header is None:
        return []
    tam = LIBRO_SNAPSHOTS.stat().st_size
    if tam < _libro_pos:
        _libro_pos = 0
        _libro_header = None
        return []
    if tam == _libro_pos:
        return []
    with open(LIBRO_SNAPSHOTS, encoding="utf-8") as f:
        f.seek(_libro_pos)
        nuevas = f.readlines()
        _libro_pos = f.tell()
    if not nuevas:
        return []
    return list(csv.DictReader(nuevas, fieldnames=_libro_header))


def _cargar_vistos_previos() -> set:
    if not OUT.exists():
        return set()
    with open(OUT, encoding="utf-8") as f:
        return {(r["evento_timestamp_utc"], r["market_id"]) for r in csv.DictReader(f)}


def _escribir_fila(fila: dict) -> None:
    with _lock_out:
        nuevo = not OUT.exists()
        with open(OUT, "a", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=COLUMNS)
            if nuevo:
                w.writeheader()
            w.writerow(fila)


def _seguir_evento(fila_ev: dict) -> None:
    """Hilo por evento fillable: consulta el libro del lado CONTRARIO
    cada POLL_INTERVAL_S durante VENTANA_S. Solo lectura."""
    try:
        market_id = fila_ev["market_id"]
        strategy = fila_ev["strategy"]
        subtype = fila_ev["subtype"]
        direction = fila_ev["direction"]
        precio_original = float(fila_ev["precio_plan"])
        stake_eur = float(fila_ev["stake_eur"])
        ratio_original = float(fila_ev.get("ratio_vs_stake") or 0.0)

        yes_token, no_token, _cid = lt._get_token_ids(market_id)
        token_contrario = no_token if direction == "BUY_YES" else yes_token
        precio_contrario = round(max(0.01, min(0.99, 1.0 - precio_original)), 6)

        muestras = []
        ratios_contrario = []
        t0 = time.monotonic()

        while time.monotonic() - t0 < VENTANA_S:
            t_offset = round(time.monotonic() - t0, 1)
            try:
                prof_contrario = lt._consultar_profundidad_libro(
                    None, token_contrario, precio_contrario, stake_eur)
            except Exception:
                prof_contrario = {"ok": False}

            ratio_c = prof_contrario.get("ratio_vs_stake") if prof_contrario.get("ok") else None
            ask_c = prof_contrario.get("mejor_ask") if prof_contrario.get("ok") else None
            muestras.append([t_offset, ratio_c, ask_c])
            if ratio_c is not None:
                ratios_contrario.append(ratio_c)

            time.sleep(POLL_INTERVAL_S)

        _escribir_fila({
            "evento_timestamp_utc": fila_ev["timestamp_utc"],
            "market_id": market_id, "strategy": strategy, "subtype": subtype,
            "direction": direction,
            "precio_original": precio_original, "stake_eur": stake_eur,
            "ratio_original": ratio_original,
            "precio_contrario": precio_contrario,
            "muestras_json": json.dumps(muestras, separators=(",", ":")),
            "ratio_contrario_inicial": ratios_contrario[0] if ratios_contrario else "",
            "ratio_contrario_max": max(ratios_contrario) if ratios_contrario else "",
            "ratio_contrario_min": min(ratios_contrario) if ratios_contrario else "",
        })
        rc0 = ratios_contrario[0] if ratios_contrario else None
        _log(f"[{market_id}] {strategy}#{subtype} {direction} ratio_original={ratio_original:.1f} "
             f"-- ratio_contrario_inicial={rc0}")
    except Exception as e:
        _log(f"error siguiendo evento {fila_ev.get('market_id')}: {e}")
    finally:
        _sem.release()


def _marcar_backlog_como_visto() -> set:
    vistos = set()
    if LIBRO_SNAPSHOTS.exists():
        with open(LIBRO_SNAPSHOTS, encoding="utf-8") as f:
            for fila in csv.DictReader(f):
                if _es_evento_relevante(fila):
                    vistos.add((fila["timestamp_utc"], fila["market_id"]))
    return vistos


def main() -> None:
    global _vistos
    DIR_SHADOW.mkdir(parents=True, exist_ok=True)
    ya_procesados = _cargar_vistos_previos()
    backlog = _marcar_backlog_como_visto()
    _vistos = ya_procesados | backlog
    _iniciar_tail_libro()
    _log(f"arrancado -- {len(ya_procesados)} eventos ya en {OUT.name}, "
         f"{len(backlog)} en el backlog histórico marcados como vistos (no se procesan) -- "
         f"solo se sigue lo que ocurra desde ahora (tail incremental desde byte {_libro_pos})")

    while True:
        try:
            for fila in _leer_filas_nuevas():
                if not _es_evento_relevante(fila):
                    continue
                clave = (fila["timestamp_utc"], fila["market_id"])
                if clave in _vistos:
                    continue
                _vistos.add(clave)
                if _sem.acquire(blocking=False):
                    threading.Thread(target=_seguir_evento, args=(fila,), daemon=True).start()
                else:
                    _log(f"[{fila['market_id']}] descartado -- {MAX_HILOS_CONCURRENTES} hilos ya en curso")
        except Exception as e:
            _log(f"error en ciclo principal: {e}")
        time.sleep(CICLO_TAIL_S)


if __name__ == "__main__":
    main()
