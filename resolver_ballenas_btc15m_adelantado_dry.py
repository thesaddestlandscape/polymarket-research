#!/usr/bin/env python3
"""resolver_ballenas_btc15m_adelantado_dry.py -- rellena outcome_real/acierto en
ballenas_btc15m_adelantado_dry.csv (12-Oct). ballenas_executor_btc15m.py escribe ese CSV desde
el 28-Jul con las columnas de desenlace vacías y nadie las rellenaba (1.316 filas, 0 resueltas;
lo cazó vigia_cobertura_desenlaces). Mismo patrón que resolver_wallet_first_buy_longshot_dryrun.py
(condition_id vía gamma-api con closed=true, desenlace OFICIAL).

La señal es BUY_YES (consenso de ballenas YES; py = best_ask del YES): acierto = 1 si gana Up.
El escritor (ejecutor live) no toma candado; para no perder una fila añadida entre la lectura y
el replace, se aborta la reescritura si el fichero cambió de tamaño mientras se resolvía.
Cron: */10.
"""
import csv
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
from resolver_mean_reversion_penny_clipper_fase0 import (  # noqa: E402
    _CACHE, _cids_vencidos, _log, precargar_desenlaces)

OUT = REPO / "data" / "shadow" / "ballenas_btc15m_adelantado_dry.csv"
COLUMNAS = ["timestamp_utc", "market_id", "condition_id", "end_date",
            "restante_s", "py", "concentracion_ponderada", "n_ballenas",
            "n_yes_total", "profundidad_eur", "ratio_vs_stake", "n_niveles_libro",
            "outcome_real", "acierto"]


def _fin(r) -> float:
    return datetime.fromisoformat(r["end_date"].replace("Z", "+00:00")).timestamp()


def main() -> int:
    if not OUT.exists():
        return 0
    precargar_desenlaces(_cids_vencidos(OUT, _fin))
    tam = OUT.stat().st_size
    with open(OUT, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != COLUMNAS:
            _log(f"⚠️ {OUT.name} cabecera inesperada ({reader.fieldnames}) -- saltado")
            return 1
        rows = list(reader)
    cambiado = 0
    for r in rows:
        out = None if r.get("outcome_real") else _CACHE.get(r.get("condition_id"))
        if out:
            r["outcome_real"] = "YES" if out == "Up" else "NO"
            r["acierto"] = "1" if out == "Up" else "0"
            cambiado += 1
    if not cambiado:
        return 0
    tmp = OUT.with_name(OUT.name + ".resolver.tmp")
    with open(tmp, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNAS)
        w.writeheader()
        w.writerows(rows)
    if OUT.stat().st_size != tam:   # el ejecutor añadió una fila: reintentar en el próximo ciclo
        os.unlink(tmp)
        _log(f"{OUT.name}: cambió durante la resolución, se reintenta en el próximo ciclo")
        return 0
    tmp.replace(OUT)
    _log(f"{OUT.name}: +{cambiado} resueltas, {sum(1 for r in rows if r.get('outcome_real'))}/{len(rows)} en total")
    return 0


if __name__ == "__main__":
    sys.exit(main())
