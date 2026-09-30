#!/usr/bin/env python3
"""vigia_cobertura_desenlaces.py -- ¿qué fracción de cada CSV de observador/dry-run tiene DESENLACE? (30-Sep)

Por qué: el mismo día aparecieron tres resolvers que dejaban la mayoría de las filas sin desenlace sin que nada
avisara, y la muestra "resuelta" estaba sesgada: longshot de primera compra (307 de 12.802; el "+0,37 por €" era
eso más un filtro de supervivencia), mean reversion/penny clipper (4-9 %) y el gate de bot wallets (34 %; ETH,
SOL y XRP con 0 filas resueltas desde el 28-Sep por una cola alfabética con tope). Un análisis sobre una muestra
resuelta parcial no mide nada.

Qué hace: para cada data/shadow/*.csv y data/sports/*.csv tocado en los últimos 3 días, con columna de desenlace
y de fecha, cuenta las filas de entre 6 h y 4 días de antigüedad y cuántas están resueltas; también por ACTIVO
(una cobertura global del 60 % puede ser 100 % de BTC y 0 % de ETH). Lectura en streaming. Avisa por Telegram
(bot cripto) solo si algo baja del umbral. Salida: data/shadow/cobertura_desenlaces.json.
Cron diario 07:58. Uso manual: vigia_cobertura_desenlaces.py [--sin-telegram]
"""
import csv
import glob
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
OUT = REPO / "data" / "shadow" / "cobertura_desenlaces.json"
UMBRAL, UMBRAL_ACTIVO, N_MIN, N_MIN_ACTIVO = 0.90, 0.80, 50, 100
COL_DESENLACE = ("outcome_real", "resultado_real", "outcome_final", "acierto")
COL_FECHA = ("timestamp_utc", "ts_trade", "ts", "timestamp", "ts_utc", "ts_deteccion")
# deportes tarda días en resolver algunos mercados: umbral propio para no avisar en falso
UMBRAL_POR_FICHERO = {"wallet_mirror_sniper_dry_run.csv": 0.80}


def _ts(t: str):
    try:
        v = float(t) if t.replace(".", "", 1).isdigit() else datetime.fromisoformat(t.replace("Z", "+00:00")).timestamp()
        return v / 1000 if v > 1e12 else v
    except (ValueError, AttributeError):
        return None


def medir() -> list:
    csv.field_size_limit(10 ** 8)
    ahora, out = time.time(), []
    for f in sorted(glob.glob(str(REPO / "data/shadow/*.csv")) + glob.glob(str(REPO / "data/sports/*.csv"))):
        if os.path.getsize(f) > 600e6 or ahora - os.path.getmtime(f) > 3 * 86400:
            continue
        try:
            with open(f, encoding="utf-8", errors="replace", newline="") as fh:
                rd = csv.reader(fh)
                cab = next(rd, None) or []
                col = next((c for c in COL_DESENLACE if c in cab), None)
                tcol = next((c for c in COL_FECHA if c in cab), None)
                if not col or not tcol:
                    continue
                i, j, k = cab.index(col), cab.index(tcol), cab.index("activo") if "activo" in cab else None
                n = r = 0
                act = {}
                for row in rd:
                    if len(row) <= max(i, j):
                        continue
                    ts = _ts(row[j])
                    if ts is None or ts > ahora - 6 * 3600 or ts < ahora - 4 * 86400:
                        continue
                    ok = row[i] not in ("", "None", "nan")
                    n += 1
                    r += ok
                    if k is not None and len(row) > k and row[k]:
                        a = act.setdefault(row[k], [0, 0])
                        a[0] += 1
                        a[1] += ok
            if n >= N_MIN:
                out.append({"fichero": os.path.relpath(f, REPO), "n": n, "resueltas": r, "cobertura": round(r / n, 4),
                            "por_activo": {a: [v[1], v[0]] for a, v in sorted(act.items())}})
        except Exception as e:                                  # un CSV raro no debe tumbar la auditoría
            out.append({"fichero": os.path.relpath(f, REPO), "error": f"{type(e).__name__}: {e}"[:160]})
    return out


def main() -> int:
    res = medir()
    avisos = []
    for x in res:
        if "error" in x:
            continue
        um = UMBRAL_POR_FICHERO.get(os.path.basename(x["fichero"]), UMBRAL)
        if x["cobertura"] < um:
            avisos.append(f"· {x['fichero']}: {x['resueltas']}/{x['n']} resueltas ({x['cobertura']:.0%})")
        else:
            flojos = [f"{a} {v[0]}/{v[1]}" for a, v in x["por_activo"].items() if v[1] >= N_MIN_ACTIVO and v[0] / v[1] < UMBRAL_ACTIVO]
            if flojos:
                avisos.append(f"· {x['fichero']}: global {x['cobertura']:.0%} pero por activo: {', '.join(flojos)}")
    tmp = OUT.with_name(OUT.name + f".tmp{os.getpid()}")
    tmp.write_text(json.dumps({"generado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                               "umbral": UMBRAL, "avisos": avisos, "ficheros": res}, ensure_ascii=False, indent=1))
    tmp.replace(OUT)
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {len(res)} ficheros auditados, {len(avisos)} por debajo del umbral")
    for a in avisos:
        print(a)
    if avisos and "--sin-telegram" not in sys.argv:
        try:
            from shadow_digest import enviar_telegram
            enviar_telegram("🩺 *Cobertura de desenlaces baja* (filas de 6 h a 4 días sin resolver: la muestra resuelta "
                            "puede estar sesgada, no concluir nada con ella)\n" + "\n".join(avisos[:15]), bot="cripto")
        except Exception as e:
            print(f"telegram falló: {e}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
