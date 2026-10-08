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
  - 07-Oct: el olvido del mayor hueco es por TIEMPO (x0,98 por día), no por muestra: antes decaía x0,98 cada hora
    con escrituras (~-40 %/día) y stink_bids (eventos, huecos nocturnos de 4,7 h) avisaba en falso con 2,5 h.
  - 07-Oct: CONDICIONALES = loggers que solo escriben con posiciones OPEN (smart_exit_prices): sin OPEN en su
    trades.csv el silencio es correcto, el reloj de silencio se reinicia y no se aprende ese hueco. Si no se puede
    leer trades.csv se trata como "hay posiciones" (avisa: fail-loud).
  - 07-Oct: COMPUERTAS de régimen: si el log compañero logs/<stem>.log está vivo (<30 min) y su última línea dice que
    se salta la ventana (PATRONES_COMPUERTA), el silencio del CSV es correcto (xrp15min_contrario_fase0 con XRP#15m no
    significativo en ballenas_timing_state.json).
Estado: data/live/vigia_loggers_silenciosos_estado.json.  Uso manual: vigia_loggers_silenciosos.py [--sin-telegram]
"""
import csv
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
CONDICIONALES = {str(REPO / "data/sports/smart_exit_prices.csv"): REPO / "data/sports/trades.csv",
                 str(REPO / "data/live/smart_exit_prices.csv"): REPO / "data/live/trades.csv"}
# 07-Oct: loggers con COMPUERTA de régimen (p. ej. xrp15min_contrario_fase0: solo observa si la calibración de ballenas
# dice que XRP#15m es significativo). Su log compañero logs/<stem>.log sigue escribiendo el motivo de no disparo: si ese
# log está vivo (< 30 min) y su ÚLTIMA línea dice que se salta, el silencio del CSV es correcto (como CONDICIONALES).
# Si el log también calla -> se avisa (el hilo puede estar muerto).
PATRONES_COMPUERTA = ("se salta ventana", "no significativo")
_FECHA = re.compile(r"[_-]?\d{4}-\d{2}-\d{2}")
# 08-Oct: sufijo de PID (maker_ms_<fecha>_<pid>) o de versión (arbitraje_anidado_dryrun_<fecha>_v<epoch>): es el MISMO
# logger. Sin quitarlo, cada reinicio de observadores dejaba una familia huérfana que avisaba en falso ~48 h después.
_SUFIJO_PROCESO = re.compile(r"_v?\d{6,}(?=\.csv)")
# 08-Oct: loggers por EVENTOS con latido horario en su log ("N eventos en la última hora"): el silencio del CSV es
# correcto si el log está vivo (< 2 h) y TODOS los latidos posteriores a la última escritura dicen 0 eventos. Si un
# latido cuenta eventos y el CSV no crece, o el log calla, se avisa como siempre.
EVENTOS = {"/root/polymarket-research-datalogs/arbitraje_anidado_dryrun.csv": REPO / "logs" / "arbitraje_anidado_dryrun_fase0.log"}
_LATIDO = re.compile(r"^\[([^\]]+)\] (\d+) eventos en la última hora")


def _familias() -> dict:
    fam = {}
    for pat in PATRONES:
        for f in glob.glob(pat):
            base = os.path.basename(f)
            if "_antes_" in base or "reconstruido" in base or base.endswith(".bak"):
                continue
            clave = os.path.join(os.path.dirname(f), _SUFIJO_PROCESO.sub("", _FECHA.sub("", base).replace(".gz", "")))
            try:
                mt = os.path.getmtime(f)
            except OSError:
                continue
            if mt > fam.get(clave, 0):
                fam[clave] = mt
    return fam


def _compuerta_cerrada(clave: str) -> bool:
    log = REPO / "logs" / (_FECHA.sub("", os.path.basename(clave)).replace(".gz", "").rsplit(".", 1)[0] + ".log")
    try:
        if time.time() - os.path.getmtime(log) > 1800:
            return False
        with open(log, "rb") as f:
            f.seek(max(0, os.path.getsize(log) - 2000))
            ult = [x for x in f.read().decode("utf-8", "replace").splitlines() if x.strip()]
        return bool(ult) and any(p in ult[-1] for p in PATRONES_COMPUERTA)
    except OSError:
        return False


def _sin_eventos(clave: str, ultimo_mtime: float) -> bool:
    log = EVENTOS.get(clave)
    try:
        if log is None or time.time() - os.path.getmtime(log) > 7200:
            return False
        with open(log, "rb") as f:
            f.seek(max(0, os.path.getsize(log) - 20000))
            lineas = f.read().decode("utf-8", "replace").splitlines()
        latidos = [(datetime.fromisoformat(m.group(1)).timestamp(), int(m.group(2)))
                   for m in map(_LATIDO.match, lineas) if m]
        posteriores = [n for ts, n in latidos if ts - 3600 > ultimo_mtime]   # ventana del latido = hora previa
        return bool(posteriores) and all(n == 0 for n in posteriores)
    except (OSError, ValueError):
        return False


def _hay_open(trades: Path) -> bool:
    try:
        with open(trades, encoding="utf-8", newline="") as f:
            return any(r.get("status") == "OPEN" for r in csv.DictReader(f))
    except Exception:
        return True


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
        if (clave in CONDICIONALES and not _hay_open(CONDICIONALES[clave])) or _compuerta_cerrada(clave):
            e["ultimo_mtime"] = max(e["ultimo_mtime"], mt, ahora)   # sin posiciones: callar es lo correcto
            e["avisado"] = False
            e["gap_max_h"] = 0.0                                   # el ritmo se aprende solo con posiciones abiertas
            continue
        if mt > e["ultimo_mtime"] + 1:
            gap = (mt - e["ultimo_mtime"]) / 3600
            # el mayor hueco conocido decae despacio (x GAP_OLVIDO por día) para adaptarse si el logger cambia de ritmo
            dias = (ahora - e.get("ts_olvido", ahora)) / 86400
            e["ts_olvido"] = ahora
            e["gap_max_h"] = round(max(gap, e["gap_max_h"] * GAP_OLVIDO ** dias), 2)
            e["ultimo_mtime"] = mt
            if e.get("avisado"):
                vuelven.append(f"· {os.path.relpath(clave, REPO) if clave.startswith(str(REPO)) else clave}: vuelve a escribir tras {gap:.1f} h")
                e["avisado"] = False
            continue
        if _sin_eventos(clave, e["ultimo_mtime"]):
            continue                                       # hilo vivo y sin episodios: callar es lo correcto
        callado = (ahora - e["ultimo_mtime"]) / 3600
        umbral = max(MIN_H, FACTOR * e["gap_max_h"])
        if callado > RETIRO_DIAS * 24:
            est.pop(clave, None)
        elif not e.get("avisado") and (ahora - e["primera_vez"]) / 3600 >= HIST_MIN_H and callado > umbral:
            e["avisado"] = True
            avisos.append(f"· {os.path.relpath(clave, REPO) if clave.startswith(str(REPO)) else clave}: {callado:.1f} h sin escribir "
                          f"(su mayor hueco habitual: {e['gap_max_h']:.1f} h)")
    vivas = _familias()
    for clave in [c for c in est if c not in vivas]:     # 08-Oct: claves que ya no existen (p. ej. viejas por PID) fuera
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
