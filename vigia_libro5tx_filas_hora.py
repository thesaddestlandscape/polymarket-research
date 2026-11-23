#!/usr/bin/env python3
"""vigia_libro5tx_filas_hora.py (04-Nov, Javi): filas/hora del feed libro5_tx (instante WS por hash de tx). Q4 04-Nov: el feed se degradó tras los reinicios de 03:20Z
(02-Nov h3-15: 2-3 k/h frente a ~20 k/h) sin que ningún vigía lo viera. Aviso Telegram (latch por hora) si la última hora COMPLETA tiene < FRAC de la mediana de las
horas sanas previas. Solo lectura de /mnt/HC_Volume_106538179/libro5_tx/*; salida data/shadow/libro5tx_filas_hora.json. Cron `5 * * * *`."""
import glob
import gzip
import json
import os
import statistics
import sys
import time
from collections import Counter
from datetime import datetime, timezone

DIR = "/mnt/HC_Volume_106538179/libro5_tx"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/shadow/libro5tx_filas_hora.json")
FRAC = 0.35          # alerta si filas_hora < FRAC * mediana(horas previas sanas)
MIN_MED = 3000       # mediana mínima para creer en la línea base (si no, el mercado está dormido, no el feed)
HORAS_BASE = 48
SUELO_ABS = 3000     # 23-Nov: suelo absoluto (sano 16-18 Nov: ~20 k/h, minimo ~7 k/h). La mediana de 48 h se autosilenciaba con el feed en pausa
                     # (20-23 Nov, volumen <10 GB: mediana 1.614 < MIN_MED y 0 filas/h marcadas "no degradado").


def _abrir(p):
    return gzip.open(p, "rt") if p.endswith(".gz") else open(p)


def contar(horas_dias):
    """-> Counter {epoch_hora_utc: filas} para los ficheros de los días dados (YYYY-MM-DD)."""
    c = Counter()
    for dia in horas_dias:
        for p in glob.glob(f"{DIR}/libro5_tx_{dia}_*"):
            try:
                with _abrir(p) as f:
                    for l in f:
                        try:
                            c[int(l.split(",", 1)[0]) // 3600000] += 1
                        except ValueError:
                            continue
            except (OSError, EOFError):
                continue          # gz a medio escribir/rotar: se ignora ese fichero esta vez
    return c


def main():
    ahora = int(time.time() // 3600)
    dias = sorted({datetime.fromtimestamp((ahora - k) * 3600, timezone.utc).strftime("%Y-%m-%d") for k in range(0, HORAS_BASE + 2)})
    c = contar(dias)
    ult = ahora - 1                                        # última hora completa
    base = [c.get(h, 0) for h in range(ult - HORAS_BASE, ult) if c.get(h, 0) > 0]
    med = statistics.median(base) if len(base) >= 6 else None
    n = c.get(ult, 0)
    estado = {"hora_utc": datetime.fromtimestamp(ult * 3600, timezone.utc).strftime("%Y-%m-%dT%H"), "filas": n, "mediana_base": med,
              "base_horas": len(base), "frac": FRAC, "ts": int(time.time()),
              "ultimas_24h": {datetime.fromtimestamp(h * 3600, timezone.utc).strftime("%d-%H"): c.get(h, 0) for h in range(ult - 23, ult + 1)}}
    prev = {}
    try:
        prev = json.load(open(OUT))
    except (OSError, ValueError):
        pass
    mal = n < SUELO_ABS or (med is not None and med >= MIN_MED and n < FRAC * med)
    estado["degradado"] = bool(mal)
    estado["avisado_hora"] = prev.get("avisado_hora")
    def _h(x):
        try:
            return int(datetime.strptime(x, "%Y-%m-%dT%H").replace(tzinfo=timezone.utc).timestamp() // 3600)
        except (TypeError, ValueError):
            return None
    ult_aviso = _h(prev.get("avisado_hora"))
    if mal and (not prev.get("degradado") or ult_aviso is None or ult - ult_aviso >= 6):   # 23-Nov: transicion + recordatorio cada 6 h (no 24 avisos/dia)
        msg = f"⚠️ libro5_tx degradado: {estado['hora_utc']}Z {n} filas (suelo {SUELO_ABS}/h; mediana 48 h {med or 0:.0f}). ¿registro_libro5 EN PAUSA por volumen <10 GB? (logs/observadores_fase0.log). Joins por hash de tx inservibles esas horas; no cuentan como horas sanas."
        try:
            sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
            from shadow_digest import enviar_telegram
            enviar_telegram(msg, bot="cripto")
        except Exception as e:                              # el aviso nunca debe romper el vigía
            print(f"telegram falló: {type(e).__name__}: {e}", file=sys.stderr)
        estado["avisado_hora"] = estado["hora_utc"]
    # 23-Nov: causa raiz de las pausas = volumen HC < 10 GB libres (libro_estado_ws pausa libro5 + libro5_tx). Avisar ANTES, a <15 GB.
    import shutil
    libre_gb = shutil.disk_usage("/mnt/HC_Volume_106538179").free / 1e9
    estado["hc_libre_gb"], estado["avisado_disco_hora"] = round(libre_gb, 1), prev.get("avisado_disco_hora")
    ult_disco = _h(prev.get("avisado_disco_hora"))
    if libre_gb < 15 and (ult_disco is None or ult - ult_disco >= 6):
        try:
            sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
            from shadow_digest import enviar_telegram
            enviar_telegram(f"⚠️ Volumen HC con {libre_gb:.1f} GB libres: a <10 GB libro_estado_ws PAUSA libro5/libro5_tx (forwards 5m barato, A3-CANCEL, joins por tx). Liberar espacio.", bot="cripto")
        except Exception as e:
            print(f"telegram falló: {type(e).__name__}: {e}", file=sys.stderr)
        estado["avisado_disco_hora"] = estado["hora_utc"]
    tmp = OUT + ".tmp"
    json.dump(estado, open(tmp, "w"), indent=1)
    os.replace(tmp, OUT)
    print(json.dumps({k: estado[k] for k in ("hora_utc", "filas", "mediana_base", "degradado")}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
