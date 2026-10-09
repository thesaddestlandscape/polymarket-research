#!/usr/bin/env python3
"""archivo_volumen.py -- 09-Oct (Javi: "que los datos de 15m puedan almacenarse 60 días, como los de 5m").
Archivos de larga retención (60 d) en el VOLUMEN /dev/sdb, que aloja también .git y los backups. Una sola guarda de
espacio para TODOS ellos: si el volumen baja de LIBRE_MIN_GB, borra el día MÁS ANTIGUO de todas las familias a la vez
(nunca los dos días más recientes) y avisa por Telegram. Así ninguna familia se come el hueco de las demás según el orden
de los crons.
Uso: from archivo_volumen import VOL, RETENCION_DIAS, retencion, guarda   (o python3 archivo_volumen.py: solo la guarda)
"""
import re
import shutil
from datetime import date, timedelta
from pathlib import Path

VOL = Path("/mnt/HC_Volume_106538179")
RETENCION_DIAS = 60
LIBRE_MIN_GB = 8.0
FAMILIAS = {                                    # carpeta del volumen -> patrón de sus ficheros diarios
    "registro_5m_barato": "maker_ms_*.csv.gz",
    "m15_registro": "m15_registro_*.csv.gz",
    "m15_onchain": "m15_onchain_*.csv.gz",
    "l2_15m": "l2_15m_*.csv.gz",
}
_FECHA = re.compile(r"(\d{4}-\d{2}-\d{2})")


def _ficheros():
    for carpeta, patron in FAMILIAS.items():
        for f in (VOL / carpeta).glob(patron):
            m = _FECHA.search(f.name)
            if m:
                yield m.group(1), f


def retencion(carpeta, dias=RETENCION_DIAS):
    """Borra de UNA familia los días con fecha (del NOMBRE, no del mtime) anterior a hoy - dias."""
    lim = (date.today() - timedelta(days=dias)).isoformat()
    patron = FAMILIAS[carpeta]
    for f in (VOL / carpeta).glob(patron):
        m = _FECHA.search(f.name)
        if m and m.group(1) < lim:
            f.unlink()
            print(f"retención {dias} d: borrado {carpeta}/{f.name}")


def guarda():
    dias = sorted({d for d, _ in _ficheros()})
    borrados = []
    while shutil.disk_usage(VOL).free / 1e9 < LIBRE_MIN_GB and len(dias) > 2:
        d = dias.pop(0)
        for dd, f in list(_ficheros()):
            if dd == d:
                f.unlink()
        borrados.append(d)
    if borrados:
        txt = (f"⚠️ Archivos 60 d del volumen (5m barato + 15m): < {LIBRE_MIN_GB} GB libres, borrados los días "
               f"{', '.join(borrados)} de todas las familias. Quedan {len(dias)} días ({dias[0]} en adelante). "
               f"Ampliar el volumen o liberar espacio para retener 60 días.")
        print(txt)
        try:
            from shadow_digest import enviar_telegram
            enviar_telegram(txt)
        except Exception as e:
            print(f"(Telegram falló: {e})")
    return borrados


if __name__ == "__main__":
    print(f"libre {shutil.disk_usage(VOL).free / 1e9:.1f} GB; borrados: {guarda()}")
