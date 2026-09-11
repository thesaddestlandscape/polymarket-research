#!/usr/bin/env python3
"""vigia_ritmo_predicciones.py — Vigía genérico de "cable desconectado
silencioso" en la generación de predicciones (25-Ago, propuesto tras el
bug de `_cargar_spot()` que dejó a WEEKLY_PRICE y UPDOWN_OU_5M en CERO
predicciones/día durante 5-6 días seguidos sin que ningún vigía lo
notara — ver idea_bug_cargar_spot_kalshi_weekly_price_25ago).

Ningún vigía existente cubre este caso: `analisis_diario_salud_
sistema.py` mira duración de pipeline/procesos colgados/disco/RAM, no
la TASA de generación por estrategia. Este vigía compara el conteo de
predicciones del día ANTERIOR completo (ayer, no hoy — hoy está a
medias cuando corre el cron de madrugada) contra la mediana de los 7
días previos a ese, por estrategia — y avisa por Telegram (latch, una
vez por racha) si una estrategia con historial sólido (mediana≥20/día)
cae por debajo del 15% de su propia mediana.

Deliberadamente NO usa un umbral fijo en valor absoluto (una estrategia
de 5/día es normal para otra, anómala para GBM_LATE_15M) — cada
estrategia es su propio control, mismo principio que el resto del
proyecto (nunca agregado, CLAUDE.md pt.17).

Solo lectura. No toca dinero ni ninguna decisión — igual que
vigia_log_growth.py/vigia_gate_bucket_propio.py, solo informa.
"""
import csv
import glob
import json
import statistics
import sys
from datetime import date, timedelta
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

DIR_SHADOW = REPO / "data" / "shadow"
LATCH = DIR_SHADOW / "vigia_ritmo_predicciones_latch.json"

N_DIAS_BASELINE = 7  # días previos al día evaluado, para la mediana
MEDIANA_MIN = 20     # solo vigila estrategias con historial sólido
RATIO_ALARMA = 0.15  # cae por debajo del 15% de su mediana -> aviso


def _conteo_por_estrategia(fecha: date) -> dict:
    f = DIR_SHADOW / f"predictions_{fecha.isoformat()}.csv"
    if not f.exists():
        return {}
    c: dict = {}
    try:
        with open(f, encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                s = row.get("strategy", "")
                if s:
                    c[s] = c.get(s, 0) + 1
    except Exception as e:
        print(f"[vigia_ritmo_predicciones] WARN no se pudo leer {f.name}: "
              f"{type(e).__name__}: {e}")
    return c


def main() -> int:
    from shadow_digest import enviar_telegram

    hoy = date.today()
    ayer = hoy - timedelta(days=1)
    conteo_ayer = _conteo_por_estrategia(ayer)

    conteos_previos: dict = {}
    for i in range(2, 2 + N_DIAS_BASELINE):
        d = hoy - timedelta(days=i)
        for s, n in _conteo_por_estrategia(d).items():
            conteos_previos.setdefault(s, []).append(n)

    todas = set(conteos_previos) | set(conteo_ayer)

    latch = {}
    if LATCH.exists():
        try:
            latch = json.loads(LATCH.read_text())
        except Exception:
            latch = {}

    cambiado = False
    avisos = []
    for s in sorted(todas):
        historico = conteos_previos.get(s, [])
        if len(historico) < N_DIAS_BASELINE:
            continue
        mediana = statistics.median(historico)
        if mediana < MEDIANA_MIN:
            continue
        n_ayer = conteo_ayer.get(s, 0)
        ratio = n_ayer / mediana if mediana else 0.0

        if ratio < RATIO_ALARMA:
            if not latch.get(s, {}).get("avisado"):
                msg = (f"🔴 [vigia_ritmo_predicciones] {s}: {n_ayer} "
                       f"predicciones ayer ({ayer.isoformat()}) vs "
                       f"mediana {mediana:.0f}/día (últimos {N_DIAS_BASELINE} "
                       f"días) — cayó a {ratio*100:.1f}% de su ritmo normal. "
                       f"Posible cable desconectado (fuente de datos rota, "
                       f"filtro degenerado, excepción silenciosa).")
                avisos.append(msg)
                latch[s] = {"avisado": True, "fecha": ayer.isoformat(),
                             "n_ayer": n_ayer, "mediana": mediana}
                cambiado = True
        else:
            if latch.get(s, {}).get("avisado"):
                print(f"[vigia_ritmo_predicciones] {s} se recuperó "
                      f"({n_ayer} vs mediana {mediana:.0f}) — rearmando latch")
                latch.pop(s, None)
                cambiado = True

    for msg in avisos:
        print(msg)
        enviar_telegram(msg)

    if not avisos:
        print(f"[vigia_ritmo_predicciones] sin anomalías — {len(todas)} "
              f"estrategias revisadas, {sum(1 for s in todas if conteos_previos.get(s, []) and statistics.median(conteos_previos[s]) >= MEDIANA_MIN)} con historial suficiente")

    if cambiado:
        LATCH.write_text(json.dumps(latch, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"[vigia_ritmo_predicciones] ERROR {type(e).__name__}: {e}")
        sys.exit(0)
