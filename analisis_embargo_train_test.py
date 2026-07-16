#!/usr/bin/env python3
"""Propuesta #26 backlog quant-desk (13-jul, Financial ML Kelly&Xiu sec 3.2):
split train/validation/test con "embargo" en vez de solo "n>=40 forward".
Afina #6/#23 (ya en cola: Wilson+shuffle en analisis_gate_riguroso.py,
Deflated Sharpe en analisis_deflated_sharpe.py) con la capa de diseño
experimental que les falta: ¿la "n forward" de un candidato es de verdad
out-of-sample, o incluye datos de ANTES de que se decidiera instrumentarlo
(en cuyo caso pudo informar la propia decisión — fuga por mirar el dato)?

Metodología: para cada tupla de candidatos_evaluacion_live, usa `git log -S`
sobre config_live.json para encontrar el commit EXACTO que la introdujo por
primera vez (fecha_instrumentacion — el corte train/test real, no una fecha
de memoria). Añade un embargo de 6h (ventanas GBM 15/60min autocorrelan
dentro del mismo día/sesión; 6h cubre varias ventanas y un cambio de sesión)
y recalcula el gate Wilson+shuffle de analisis_gate_riguroso.py SOLO con
las filas resueltas después de fecha_instrumentacion+embargo. Compara
contra el gate "todo n" actual — si difieren, la n actual incluye datos
pre-instrumentación (posible fuga) y el veredicto limpio es el del embargo.

Solo lectura. No toca config_live.json ni ningún gate real.
Uso: python3 analisis_embargo_train_test.py
"""
import csv
import json
import subprocess
from collections import defaultdict
from datetime import datetime, timedelta, timezone

from analisis_gate_riguroso import RES, CONFIG_LIVE, gate

EMBARGO_HORAS = 6


def cargar_tuplas(clave_config):
    cfg = json.load(open(CONFIG_LIVE))
    tuplas = cfg.get(clave_config, [])
    claves = []
    for t in tuplas:
        partes = t.split("#")
        if len(partes) != 4:
            # p.ej. WEEKLY_PRICE#BTC#BUY_NO (sin timeframe en el nombre) —
            # fuera del alcance de este análisis (asume STRAT#PAR#TF#DEC).
            print(f"  (omitida, formato no soportado: {t})")
            continue
        strat, pair, tf, dec = partes
        claves.append((t, strat, f"{pair}#{tf}", dec))
    return claves


def fecha_instrumentacion(tupla: str):
    """Commit más antiguo que introdujo esta tupla exacta en config_live.json."""
    try:
        out = subprocess.run(
            ["git", "log", "-S", tupla, "--format=%aI", "--reverse", "--",
             "data/live/config_live.json"],
            capture_output=True, text=True, check=True, cwd=".")
        lineas = [l for l in out.stdout.splitlines() if l.strip()]
        if not lineas:
            return None
        return datetime.fromisoformat(lineas[0])
    except Exception:
        return None


def cargar_filas(claves):
    wanted = {(s, sub, d) for _, s, sub, d in claves}
    filas = defaultdict(list)
    with open(RES) as f:
        for row in csv.DictReader(f):
            if row.get("acierto") in (None, ""):
                continue
            k = (row["strategy"], row["subtype"], row["decision"])
            if k in wanted:
                filas[k].append(row)
    return filas


def _ts_pred(row):
    try:
        ts = datetime.fromisoformat(row["prediction_timestamp"].replace("Z", "+00:00"))
        if ts.tzinfo is None:
            ts = ts.replace(tzinfo=timezone.utc)
        return ts
    except Exception:
        return None


def evaluar(claves, filas_por_clave):
    for tupla, strat, sub, dec in claves:
        rows = filas_por_clave.get((strat, sub, dec), [])
        finst = fecha_instrumentacion(tupla)
        print(f"--- {tupla} ---")
        if finst is None:
            print("  fecha_instrumentacion: NO ENCONTRADA (no aparece en historial de "
                  "config_live.json) — puede que sea de otra fuente (hipotesis_custom.json "
                  "o auto-generada por hypothesis_tracker), se omite el corte de embargo.")
            g_todo = gate(rows)
            if g_todo:
                print(f"  todo-n:    n={g_todo['n']:4d} hit={g_todo['hit']*100:5.1f}% "
                      f"IC={g_todo['ic']:+.3f} → {g_todo['veredicto']}")
            print()
            continue

        corte = finst + timedelta(hours=EMBARGO_HORAS)
        print(f"  fecha_instrumentacion: {finst.isoformat()} | corte embargo: {corte.isoformat()}")

        rows_pre = [r for r in rows if (_ts_pred(r) or corte) < finst]
        rows_post = [r for r in rows if (_ts_pred(r) or finst) >= corte]
        rows_embargo_zone = len(rows) - len(rows_pre) - len(rows_post)

        g_todo = gate(rows)
        g_post = gate(rows_post)

        def _fmt_pnl(g):
            if "pnl_media" not in g:
                return "PnL=sin datos"
            return f"PnL={g['pnl_media']:+.4f}/trade CI90%=[{g['pnl_lo']:+.4f},{g['pnl_hi']:+.4f}]"

        if g_todo:
            print(f"  todo-n:         n={g_todo['n']:4d} hit={g_todo['hit']*100:5.1f}% "
                  f"IC={g_todo['ic']:+.3f} Wilson=[{g_todo['lo']:.3f},{g_todo['hi']:.3f}] "
                  f"p_shuf={g_todo['p_shuf']:.3f} {_fmt_pnl(g_todo)} → {g_todo['veredicto']}")
        else:
            print("  todo-n: sin datos")
        if len(rows_pre) > 0:
            print(f"  ⚠️  {len(rows_pre)} filas ANTERIORES a la instrumentación "
                  f"(potencial in-sample, ya incluidas en 'todo-n' arriba)")
        if g_post:
            print(f"  post-embargo:   n={g_post['n']:4d} hit={g_post['hit']*100:5.1f}% "
                  f"IC={g_post['ic']:+.3f} Wilson=[{g_post['lo']:.3f},{g_post['hi']:.3f}] "
                  f"p_shuf={g_post['p_shuf']:.3f} {_fmt_pnl(g_post)} → {g_post['veredicto']}")
        else:
            print(f"  post-embargo: sin datos limpios todavía (0 filas tras "
                  f"{EMBARGO_HORAS}h de embargo)")

        if g_todo and g_post and g_todo["veredicto"] != g_post["veredicto"]:
            print("  🚨 DIVERGEN: el veredicto 'todo-n' y el 'post-embargo' no coinciden — "
                  "usar el post-embargo (es el que de verdad es out-of-sample).")
        print()


def main():
    print(f"Embargo: {EMBARGO_HORAS}h tras la fecha de instrumentación (git log -S "
          f"sobre config_live.json, commit exacto que introdujo cada tupla)")
    print()

    print("=" * 70)
    print("DINERO REAL — pares_permitidos_live (7 tuplas)")
    print("=" * 70)
    claves_live = cargar_tuplas("pares_permitidos_live")
    evaluar(claves_live, cargar_filas(claves_live))

    print("=" * 70)
    print("CANDIDATOS — candidatos_evaluacion_live (shadow, sin riesgo)")
    print("=" * 70)
    claves_cand = cargar_tuplas("candidatos_evaluacion_live")
    evaluar(claves_cand, cargar_filas(claves_cand))


if __name__ == "__main__":
    main()
