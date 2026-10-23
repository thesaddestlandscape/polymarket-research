#!/usr/bin/env python3
"""vigia_cadena_forward.py -- 23-Oct (Javi: "encargate de que R1 no falle"). Solo lectura. Cron 13:40Z.
Comprueba que la cadena R1 -> L1b-A (poblacion) -> L1b-B (retirada) produjo el dia D-1 y avisa por Telegram si no.
Latch por (dia, pieza) en un JSON: un aviso por fallo, no spam."""
import gzip, json, os, sys, time
from datetime import datetime, timedelta, timezone
DL = "/root/polymarket-research-datalogs"
LATCH = f"{DL}/etiquetado_pasivo_B/vigia_cadena_forward_latch.json"
d1 = (datetime.now(timezone.utc) - timedelta(days=1)).strftime("%F")
CHK = {
    "R1 units": f"{DL}/sa_r1/units_{d1}.csv.gz",
    "R1 units2 (rasgos ms)": f"{DL}/sa_r1/units2_{d1}.csv.gz",
    "L1b-A poblacion": f"{DL}/etiquetado_pasivo_B/poblacion/pob_{d1}.csv.gz",
    "L1b-B retirada": f"{DL}/etiquetado_pasivo_B/retirada/ret_{d1}.csv.gz",
    "L1 etiquetas B": f"{DL}/etiquetado_pasivo_B/etiquetado_B_{d1}.csv.gz",
}
def filas(p):
    try:
        with gzip.open(p, "rt") as f: return sum(1 for _ in f) - 1
    except Exception: return -1
mal = []
for k, p in CHK.items():
    n = filas(p) if os.path.exists(p) else -1
    if n <= 0: mal.append(f"{k}: {'falta' if n < 0 else '0 filas'} ({os.path.basename(p)})")
try: lat = json.load(open(LATCH))
except Exception: lat = {}
nuevos = [m for m in mal if lat.get(f"{d1}|{m.split(':')[0]}") is None]
for m in mal: lat[f"{d1}|{m.split(':')[0]}"] = time.time()
os.makedirs(os.path.dirname(LATCH), exist_ok=True)
json.dump(lat, open(LATCH, "w"))
print(d1, "OK" if not mal else "FALLOS: " + "; ".join(mal))
if nuevos:
    sys.path.insert(0, "/root/polymarket-research")
    from shadow_digest import enviar_telegram
    enviar_telegram(f"🚨 Cadena forward L1/R1 incompleta para {d1}: " + "; ".join(nuevos) + ". Reloj de 10 días en riesgo; ver sa_r1/cron.log y etiquetado_pasivo_B/cron_l1b.log")
