#!/usr/bin/env python3
"""
resolution_sniper_naive_depth_fase0.py — FASE 0 (SOLO OBSERVACIÓN), 19-Ago.

Reacción inmediata al gate riguroso de hoy (analisis_gate_riguroso_
resolution_sniper_fade_depth_19ago.py, ver idea_resolution_sniper_fade_
refutado_19ago): el hallazgo de fade del 14-Ago (fadear la dirección
implícita de Chainlink, hit=80%) se REFUTÓ con datos frescos -- el régimen
se invirtió. Restringiendo a >=13-Ago (offset<=2s, ask accionable en
[0.05,0.95]): la dirección NAIVE (NO fade, apostar CON chainlink_
direccion_implicita) acierta 70-100% en las 12 combinaciones (activo,
marco), 9/12 pasan gate riguroso completo (Wilson90+shuffle+split-half+
BH-FDR, p_shuffle<0.05 en las 9, split-half consistente en TODAS las 12).
pnl/tr (sin fee ni profundidad) hasta +0.71€ por cada 1€ de stake.

Nadie sabe todavía si ese precio es EJECUTABLE -- resolution_sniper_fade_
depth_fase0.py solo mide profundidad del lado FADE (contrario), nunca del
lado implícito/naive. Este observador cierra ese hueco: mismo mecanismo
exacto que resolution_sniper_fade_depth_fase0.py (offsets 0-3s, activo/
marco de resolution_sniper_observer.py, `lt._consultar_profundidad_libro`
con stake de referencia 1.05€), pero consulta profundidad del lado
IMPLÍCITO (el que gana), no del contrario.

Decisión ladder (CLAUDE.md): reusa TODO lo de resolution_sniper_fade_
depth_fase0.py salvo qué lado se consulta -- no se duplica lógica de
descubrimiento de mercado / reloj de ventanas / Chainlink tail.

NO coloca, cancela ni modifica ninguna orden real -- puramente
observacional, mismo criterio de riesgo que el resto de *_fase0.py.
Objetivo: acumular n>=40 CON profundidad antes de plantear ningún
ejecutor -- ninguna promoción a pares_permitidos_live sin esto.

19-Ago (mismo día, hallazgo de sobresuscripción de CPU vía py-spy: 85 hilos
vivos en observadores_fase0.py, load5/nproc>2.9x, swap activo en vivo):
este módulo YA NO corre su propio hilo/pool -- resolution_sniper_fade_
depth_fase0.py consulta la MISMA ventana/mercado en el MISMO instante
(mismos offsets), así que se fusionó ahí (1 descubrimiento de mercado +
1 libro() por offset en vez de 2, profundidad de ambos lados en la misma
iteración). Este fichero se conserva solo por sus constantes (OUT, COLUMNS,
_guardar) que resolution_sniper_fade_depth_fase0.py importa y reutiliza --
NO se registra en observadores_fase0.py, NO tiene worker()/main() propios.
"""
import csv
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
DIR_SHADOW = REPO / "data" / "shadow"
OUT = DIR_SHADOW / "resolution_sniper_naive_depth_fase0.csv"

OFFSETS_S = [0, 1, 2, 3]  # mismo rango accionable que resolution_sniper_fade_depth_fase0
STAKE_REF_EUR = 1.05  # suelo real del proyecto (CLOB min size)
ASK_MIN, ASK_MAX = 0.05, 0.95  # subconjunto "accionable" (no obvio todavía)

COLUMNS = [
    "timestamp_utc", "activo", "marco", "slug", "market_id", "condition_id",
    "ts_end", "offset_s", "direccion_implicita", "ask_implicita",
    "profundidad_implicita_eur", "ratio_implicita_vs_stake",
    "mejor_ask_implicita", "n_niveles_implicita",
]


def _log(msg: str):
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _guardar(filas: list):
    if not filas:
        return
    nuevo = not OUT.exists()
    with open(OUT, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if nuevo:
            w.writerow(COLUMNS)
        for fila in filas:
            w.writerow([fila.get(c, "") for c in COLUMNS])


# observar_ventana()/worker()/main() vivían aquí -- eliminados 19-Ago,
# la lógica se fusionó en resolution_sniper_fade_depth_fase0.py::
# observar_ventana() (ver docstring arriba). Este módulo solo aporta
# OUT/COLUMNS/_guardar() de aquí en adelante.
