#!/usr/bin/env python3
"""wm_ejecutor_csv.py -- lector compartido del CSV de decisiones de WALLET_MIRROR (cripto) para los
ANÁLISIS de solo lectura (25-Sep, Javi "dale"; sale del /code-review de la unificación del quirúrgico).

`wallet_mirror_executor_dryrun.csv` perdió 15 días (08-22 Sep) en el OOM del 23-Sep 06:01;
`wallet_mirror_executor_dryrun_reconstruido_08_22sep.csv` (143.423 filas, validado en solape) los
recupera de forma APROXIMADA: ask_decision == ask_deteccion, sigue_fillable = (ratio_deteccion>=5),
lista de wallets aproximada (columnas `reconstruido`, `fuente_reconstruccion`, `lista_validada_aprox`).
Por eso este lector es SOLO para análisis/lectura: NO se usa en gates que autorizan dinero real
(analisis_wallet_mirror_gate_bucket_10ago.py -> wallet_mirror_gate_bucket.json), decisión tras
/code-review 25-Sep (detección frente a decisión ya fue un espejismo en bot_wallets, 22-Sep).

iter_filas(principal): filas (dict) del principal y, si `principal` es el CSV por defecto, las del
reconstruido anteriores a RECON_HASTA_TS (el principal empieza 23-Sep 06:03:48). Un reconstruido
ilegible se ignora (= comportamiento anterior). Cada fila reconstruida lleva reconstruido='1'.
"""
import csv
from pathlib import Path

REPO = Path(__file__).resolve().parent
PRINCIPAL = REPO / "data/shadow/wallet_mirror_executor_dryrun.csv"
RECON_NOMBRE = "wallet_mirror_executor_dryrun_reconstruido_08_22sep.csv"
RECON_DESDE_TS, RECON_HASTA_TS = "2026-09-08", "2026-09-23T06:03:00"
csv.field_size_limit(10_000_000)


def iter_filas(principal=PRINCIPAL):
    principal = Path(principal)
    with open(principal, encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            yield r
    recon = principal.with_name(RECON_NOMBRE)
    if principal.name != PRINCIPAL.name or not recon.exists():
        return
    try:
        with open(recon, encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f):
                ts = (r.get("timestamp_utc") or "")[:19]
                if RECON_DESDE_TS <= ts < RECON_HASTA_TS:
                    yield r
    except (OSError, csv.Error, UnicodeDecodeError) as e:
        print(f"AVISO: reconstruido WM ilegible ({type(e).__name__}: {e}); solo CSV principal")
