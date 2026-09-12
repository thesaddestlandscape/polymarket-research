#!/usr/bin/env python3
"""vigia_candidata9_10_gate_bucket_26ago.py — Vigía diario del gate por
micro-bucket de las candidatas 9 (consenso mayoritario bot wallets) y 10
(cross-activo BTC), confirmadas con rigor completo 26-Ago (no-lookahead,
split-half, no-redundancia con bot_consenso/WALLET_MIRROR, cobertura
incremental vs ballenas — ver idea_candidata9_10_edge_precio_confirmado_
26ago). Mismo patrón EXACTO que vigia_bot_wallets_gate_bucket.py (25-Ago):

1. Re-corre analisis_candidata9_10_gate_bucket_26ago.py (regenera el JSON
   con el n de hoy, bot_wallets_gate_bucket_fase0.csv crece solo vía
   bot_wallets_gate_bucket_fase0.py).
2. Diffea contra el estado de AYER (latch) — avisa por Telegram SOLO
   veredictos NUEVOS.
3. Añade una fila por bucket a data/shadow/candidata9_10_gate_bucket_
   historico.csv cada día (serie temporal).

FASE 0 -- solo observación, no conectado a ninguna decisión real.
Cron diario 07:00 UTC (después de bot_wallets_gate_bucket, 06:59).
"""
import csv
import json
import subprocess
import sys
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

DATA_PATH = REPO / "data/shadow/candidata9_10_gate_bucket.json"
LATCH = REPO / "data/shadow/vigia_candidata9_10_gate_bucket_latch.json"
HISTORICO = REPO / "data/shadow/candidata9_10_gate_bucket_historico.csv"
COLUMNS = ["fecha", "clave", "bucket", "n", "pnl_medio", "shuffle_p", "veredicto"]


def _append_historico(nuevo: dict) -> None:
    hoy = date.today().isoformat()
    nuevo_archivo = not HISTORICO.exists()
    filas = []
    for clave_str, tabla in nuevo.items():
        for b, info in tabla.items():
            filas.append([hoy, clave_str, b, info.get("n"), info.get("pnl_medio"),
                          info.get("shuffle_p"), info.get("veredicto")])
    if not filas:
        return
    with open(HISTORICO, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if nuevo_archivo:
            w.writerow(COLUMNS)
        w.writerows(filas)


def main() -> int:
    from shadow_digest import enviar_telegram

    # 11-Sep (barrido de salud, vigía roto por TimeoutExpired): el script
    # ya tarda ~370s con el crecimiento de results.csv/candidata9_10 CSVs
    # derivados, por encima del timeout=300 original -- mismo patrón ya
    # arreglado 07-Sep en vigia_gate_bucket_propio.py/vigia_gate_calibracion.py/
    # vigia_gate_bucket_wallet_mirror.py (timeout fijo no escala con datos
    # que crecen). Subido a 900s, margen de sobra sobre el tiempo medido.
    # 12-Sep: volvió a fallar a los 900s -- no es que el script se haya
    # vuelto mas lento por si solo, es contencion real de RAM/CPU del VPS
    # (causa raiz sin resolver: shadow_postmortem.py::calcular_params()
    # relee results.csv completo -509k filas/428MB hoy- cada ciclo, ver
    # memoria project_dia_dedicado_rediseno_postmortem_11sep, rediseño
    # aplazado por la crisis de disco del mismo dia). Subido otra vez a
    # 1800s como parche de contencion (este vigia es solo informativo,
    # NO conectado a ningun ejecutor real) + nice para no competir por CPU
    # con el motor de decision compartido mientras dura.
    r = subprocess.run(["nice", "-n", "15", sys.executable,
                         str(REPO / "analisis_candidata9_10_gate_bucket_26ago.py")],
                        capture_output=True, text=True, timeout=1800, cwd=str(REPO))
    if r.returncode != 0:
        print(f"ERROR ejecutando analisis_candidata9_10_gate_bucket_26ago.py: {r.stderr[-2000:]}")
        return 1

    nuevo = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    try:
        previo = json.loads(LATCH.read_text(encoding="utf-8")) if LATCH.exists() else {}
    except Exception:
        previo = {}

    avisos = []
    cobertura = []
    for clave_str, tabla in nuevo.items():
        veredictos_antes = previo.get(clave_str, {})
        n_sin_concluir = 0
        n_total_buckets = len(tabla)
        for b, info in tabla.items():
            v_nuevo = info.get("veredicto", "sin_concluir")
            v_antes = veredictos_antes.get(b, {}).get("veredicto", "sin_concluir")
            if v_nuevo != "sin_concluir":
                if v_antes != v_nuevo:
                    avisos.append(
                        f"{'🔴' if v_nuevo == 'malo_confirmado' else '🟢'} {clave_str} "
                        f"[{b},{float(b)+0.05:.2f}) -> {v_nuevo} "
                        f"(n={info['n']} pnl/tr={info['pnl_medio']:+.3f} p={info.get('shuffle_p')})"
                    )
            else:
                n_sin_concluir += 1
        if n_total_buckets:
            cobertura.append(f"{clave_str}: {n_total_buckets - n_sin_concluir}/{n_total_buckets} buckets con veredicto")

    print("\n".join(cobertura))
    _append_historico(nuevo)

    if avisos:
        msg = "🤖 Candidata 9/10 (bot consenso / cross-activo) gate bucket — nuevos veredictos hoy:\n" + "\n".join(avisos)
        print(msg)
        enviar_telegram(msg)
    else:
        print("Sin veredictos nuevos hoy.")

    LATCH.write_text(json.dumps(nuevo, ensure_ascii=False, indent=1), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
