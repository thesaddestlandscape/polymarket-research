#!/usr/bin/env python3
"""vigia_loggers_silenciosos.py -- avisa cuando un logger/observador DEJA DE ESCRIBIR (30-Sep, Javi: "no podemos
permitirnos huecos de datos").

Motivo: `wallet_mirror_executor_dryrun.csv` estuvo del 8 al 22 de septiembre sin registrar nada y se descubrió
después, al ir a usarlo. Los avisos existentes miran screens caídas y logs, no si el FICHERO de datos sigue
creciendo: un hilo puede seguir vivo y no escribir.

Cómo funciona (coste: un stat por fichero, cada hora, dentro de vigias_horarios_fase0):
  - Familias: data/shadow/*.csv, data/sports/*.csv, data/live/*.csv y /root/polymarket-research-datalogs/*.csv*;
    los ficheros con fecha en el nombre (xxx_YYYY-MM-DD.csv) cuentan como UNA familia.
  - Aprende el ritmo de cada familia: el mayor hueco entre escrituras visto en los últimos días (un logger que solo
    escribe de 13 a 17 UTC, o una vez al día, no dispara en falso).
  - Avisa por Telegram si una familia lleva callada más de max(3 h, 2 x su mayor hueco conocido) y ya tiene al
    menos 48 h de historial. Un aviso por episodio; al volver a escribir se rearma y lo dice.
  - Familia sin escribir 10 días: se da por retirada y sale del estado.
Estado: data/live/vigia_loggers_silenciosos_estado.json.  Uso manual: vigia_loggers_silenciosos.py [--sin-telegram]
"""
import glob
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
ESTADO = REPO / "data" / "live" / "vigia_loggers_silenciosos_estado.json"
PATRONES = [str(REPO / "data/shadow/*.csv"), str(REPO / "data/sports/*.csv"), str(REPO / "data/live/*.csv"),
            "/root/polymarket-research-datalogs/*.csv", "/root/polymarket-research-datalogs/*.csv.gz"]
MIN_H, FACTOR, HIST_MIN_H, RETIRO_DIAS, GAP_OLVIDO = 3.0, 2.0, 48.0, 10, 0.98
_FECHA = re.compile(r"[_-]?\d{4}-\d{2}-\d{2}")


def _familias() -> dict:
    fam = {}
    for pat in PATRONES:
        for f in glob.glob(pat):
            base = os.path.basename(f)
            if "_antes_" in base or "reconstruido" in base or base.endswith(".bak"):
                continue
            clave = os.path.join(os.path.dirname(f), _FECHA.sub("", base).replace(".gz", ""))
            try:
                mt = os.path.getmtime(f)
            except OSError:
                continue
            if mt > fam.get(clave, 0):
                fam[clave] = mt
    return fam


def main() -> int:
    ahora = time.time()
    try:
        est = json.loads(ESTADO.read_text(encoding="utf-8"))
    except Exception:
        est = {}
    avisos, vuelven = [], []
    for clave, mt in _familias().items():
        e = est.get(clave)
        if e is None:
            if ahora - mt < 2 * 86400:                     # solo se empieza a seguir lo que está vivo
                est[clave] = {"primera_vez": ahora, "ultimo_mtime": mt, "gap_max_h": 0.0, "avisado": False}
            continue
        if mt > e["ultimo_mtime"] + 1:
            gap = (mt - e["ultimo_mtime"]) / 3600
            # el mayor hueco conocido decae despacio para adaptarse si el logger cambia de ritmo
            e["gap_max_h"] = round(max(gap, e["gap_max_h"] * GAP_OLVIDO), 2)
            e["ultimo_mtime"] = mt
            if e.get("avisado"):
                vuelven.append(f"· {os.path.relpath(clave, REPO) if clave.startswith(str(REPO)) else clave}: vuelve a escribir tras {gap:.1f} h")
                e["avisado"] = False
            continue
        callado = (ahora - e["ultimo_mtime"]) / 3600
        umbral = max(MIN_H, FACTOR * e["gap_max_h"])
        if callado > RETIRO_DIAS * 24:
            est.pop(clave, None)
        elif not e.get("avisado") and (ahora - e["primera_vez"]) / 3600 >= HIST_MIN_H and callado > umbral:
            e["avisado"] = True
            avisos.append(f"· {os.path.relpath(clave, REPO) if clave.startswith(str(REPO)) else clave}: {callado:.1f} h sin escribir "
                          f"(su mayor hueco habitual: {e['gap_max_h']:.1f} h)")
    for clave in [c for c in est if c not in _familias() and (ahora - est[c]["ultimo_mtime"]) > RETIRO_DIAS * 86400]:
        est.pop(clave, None)
    tmp = ESTADO.with_name(ESTADO.name + f".tmp{os.getpid()}")
    tmp.write_text(json.dumps(est, indent=0), encoding="utf-8")
    tmp.replace(ESTADO)
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {len(est)} familias seguidas, {len(avisos)} calladas, {len(vuelven)} vuelven")
    for a in avisos + vuelven:
        print(a)
    if (avisos or vuelven) and "--sin-telegram" not in sys.argv:
        try:
            from shadow_digest import enviar_telegram
            msg = ""
            if avisos:
                msg += "🔇 *Loggers que han dejado de escribir* (hueco de datos en curso: mirar el hilo/cron que los alimenta)\n" + "\n".join(avisos[:20])
            if vuelven:
                msg += ("\n" if msg else "") + "🔊 Vuelven a escribir:\n" + "\n".join(vuelven[:20])
            enviar_telegram(msg, bot="cripto")
        except Exception as e:
            print(f"telegram falló: {e}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
