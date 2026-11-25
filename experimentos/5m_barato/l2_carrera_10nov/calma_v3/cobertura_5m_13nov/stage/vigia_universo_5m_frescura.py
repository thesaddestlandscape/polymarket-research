#!/usr/bin/env python3
"""
vigia_universo_5m_frescura.py -- vigia MINIMO de frescura del universo 5m con tokens (13-Nov, staging; NO instalado).

Lee datalogs/universo_5m/new_market_universo_<dia>.csv.gz (hoy+ayer, via universo_5m_io) y avisa por Telegram (una vez por episodio, y
otra al recuperarse) si:
  - FRESCURA: no ha llegado NINGUNA fila 5m nueva (ni por WS ni por relleno de gamma/capture) en > UMBRAL_S (600 s) estando armado;
  - WS: no ha llegado ningun new_market por WS en > UMBRAL_WS_S (900 s) aunque haya filas de relleno (el listener esta caido/mudo);
  - COBERTURA: alguna de las 6 monedas tiene el 5m mas lejano por menos de COBERTURA_MIN_MIN (60 min) por delante;
  - DESFASE DE RELOJ: |recepcion - evento| mediano (filas WS de la ultima hora) > 5 s;
  - FICHERO: ilegible/truncado/conflictos de tokens.
Se arma en cuanto ve datos por primera vez (antes de eso no avisa: la funcion aun no esta desplegada). Estado y latch en
datalogs/universo_5m/vigia_frescura_estado.json (subdirectorio: ningun glob de datalogs lo ve; el latch NO incluye valores recalculados:
solo el conjunto de problemas activos). No escribe nada mas, no toca red salvo Telegram.
Despliegue propuesto (sin screen nueva): cron `*/5 * * * *  cd /root/polymarket-research && python3 vigia_universo_5m_frescura.py`
(coste < 1 s; lee un .gz de ~0,5 MB con cache). Alternativa: hilo en vigias_frecuentes_fase0 (editarlo reinicia esa screen).
Uso manual: vigia_universo_5m_frescura.py [--sin-telegram]
"""
import json, os, sys, time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import universo_5m_io as U

UMBRAL_S = 600
UMBRAL_WS_S = 900
COBERTURA_MIN_MIN = 60
DESFASE_MS = 5000
ESTADO_NOMBRE = "vigia_frescura_estado.json"


def evaluar(ahora, directorio=None):
    """-> (problemas: dict {clave: texto}, info: dict). Solo lectura."""
    mk, st = U.leer(ahora, directorio)
    info = {"ficheros": st["ficheros"], "filas": st["filas"]}
    prob = {}
    if st["ficheros"] == 0:
        return {"sin_fichero": "no hay fichero de universo de hoy ni de ayer"}, info
    if st["truncados"]:
        prob["fichero_truncado"] = f"{st['truncados']} fichero(s) ilegible(s)/truncado(s) (se lee lo legible)"
    if st["conflictos"]:
        prob["conflictos_tokens"] = f"{st['conflictos']} mercado(s) con tokens/condition_id distintos entre filas (excluidos)"
    f5 = [r for r in mk.values() if r["marco"] == "5m"]
    if not f5:
        prob["sin_5m"] = "ninguna fila 5m"
        return prob, info
    ult = max(int(r["t_recv_ms"]) for r in f5) / 1000
    ult_ws = max([int(r["t_recv_ms"]) for r in f5 if r["fuente"] == "ws"] or [0]) / 1000
    info["ultima_fila_hace_s"] = round(ahora - ult)
    info["ultimo_ws_hace_s"] = round(ahora - ult_ws) if ult_ws else None
    if ahora - ult > UMBRAL_S:
        prob["sin_5m_nuevos"] = f"sin filas 5m nuevas hace {int((ahora - ult) / 60)} min (> {UMBRAL_S // 60})"
    if ahora - ult_ws > UMBRAL_WS_S:
        prob["ws_mudo"] = ("el listener new_market no ha recibido ningun evento por WS hace "
                           + (f"{int((ahora - ult_ws) / 60)} min" if ult_ws else "todo el periodo") + f" (> {UMBRAL_WS_S // 60})")
    lejos = {}
    for r in f5:
        a = r["activo"]
        lejos[a] = max(lejos.get(a, 0), r["_cierre"])
    cob = {a: round((lejos.get(a, 0) - ahora) / 60) for a in sorted(x.upper() for x in U.ACTIVOS)}
    info["cobertura_min"] = cob
    flojas = {a: m for a, m in cob.items() if m < COBERTURA_MIN_MIN}
    if flojas:
        prob["cobertura"] = "5m por delante < %d min en %s" % (COBERTURA_MIN_MIN, ", ".join(f"{a}={m}" for a, m in flojas.items()))
    lag = sorted(int(r["t_recv_ms"]) - int(r["t_evento_ms"]) for r in f5
                 if r["fuente"] == "ws" and r["t_evento_ms"] not in ("", None) and ahora - int(r["t_recv_ms"]) / 1000 < 3600)
    if lag and abs(lag[len(lag) // 2]) > DESFASE_MS:
        prob["desfase_reloj"] = f"desfase de reloj recepcion-evento mediano {lag[len(lag) // 2]} ms (> {DESFASE_MS})"
    return prob, info


def ejecutar(ahora=None, directorio=None, telegram=True, enviar=None):
    ahora = time.time() if ahora is None else ahora
    d = Path(directorio or U.UNIV_DIR)
    ep = d / ESTADO_NOMBRE
    try:
        est = json.loads(ep.read_text())
    except (OSError, ValueError):
        est = {"armado": False, "activos": []}
    prob, info = evaluar(ahora, d)
    if not est.get("armado") and "sin_fichero" not in prob and "sin_5m" not in prob and info.get("filas"):
        est["armado"] = True
    activos = sorted(prob) if est.get("armado") else []
    previos = set(est.get("activos", []))
    nuevos = [k for k in activos if k not in previos]
    resueltos = sorted(previos - set(activos))
    msgs = []
    if nuevos:
        msgs.append("Universo 5m: " + "; ".join(prob[k] for k in nuevos))
    if resueltos and not activos:
        msgs.append("Universo 5m: recuperado (" + ", ".join(resueltos) + ")")
    est["activos"] = activos                         # el latch es solo el CONJUNTO de problemas activos, sin valores recalculados
    try:
        d.mkdir(parents=True, exist_ok=True)
        tmp = ep.with_suffix(".tmp")
        tmp.write_text(json.dumps(est))
        os.replace(tmp, ep)
    except OSError:
        pass
    for m in msgs:
        print(m, flush=True)
        if telegram:
            try:
                if enviar is None:
                    from shadow_digest import enviar_telegram as enviar_fn
                else:
                    enviar_fn = enviar
                enviar_fn(m, bot="cripto")
            except Exception as e:
                print(f"no se pudo enviar a Telegram: {type(e).__name__}: {e}", flush=True)
    return prob, info, msgs


if __name__ == "__main__":
    sys.path.insert(0, "/root/polymarket-research")
    prob, info, _ = ejecutar(telegram="--sin-telegram" not in sys.argv)
    print(json.dumps({"problemas": prob, "info": info}, ensure_ascii=False))
