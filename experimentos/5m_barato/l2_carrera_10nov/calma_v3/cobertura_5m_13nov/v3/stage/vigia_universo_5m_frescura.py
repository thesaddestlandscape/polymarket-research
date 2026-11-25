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
  - LEAD: menos del 95 % de las filas 5m de las ultimas 24 h (n >= 50) se vieron >= 30 min antes de su inicio (criterio medible de que
    capture_markets (A) basta sin el listener (B): si A cubre, B es solo respaldo);
  - VIGIA: error interno del propio vigia (se avisa, no muere en silencio).
Sin ninguna fila WS en 24 h (listener no desplegado) no se exige `ws_mudo` y la frescura admite 25 min (pausa 429 de hasta ~22 min).
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
UMBRAL_SIN_WS_S = 1500
LEAD_MIN_S = 1800
LEAD_FRAC_MIN = 0.95
LEAD_N_MIN = 50
UMBRAL_WS_S = 900
COBERTURA_MIN_MIN = 60
DESFASE_MS = 5000
ESTADO_NOMBRE = "vigia_frescura_estado.json"


def _evaluar(ahora, directorio=None):
    mk, st = U.leer(ahora, directorio)
    info = {"ficheros": st["ficheros"], "filas": st["filas"], "invalidas": st["invalidas"]}
    prob = {}
    if st["ficheros"] == 0:
        return {"sin_fichero": "no hay fichero de universo de hoy ni de ayer"}, info
    if st["truncados"]:
        prob["fichero_truncado"] = f"{st['truncados']} fichero(s) ilegible(s)/truncado(s) (se lee lo legible)"
    if st["conflictos"]:
        prob["conflictos_tokens"] = f"{st['conflictos']} mercado(s) con tokens/condition_id distintos entre filas (excluidos)"
    if st["invalidas"]:
        info["filas_invalidas"] = st["invalidas"]               # informativo: filas con campos corruptos (descartadas por leer())
    f5 = [r for r in mk.values() if r["marco"] == "5m"]
    if not f5:
        prob["sin_5m"] = "ninguna fila 5m"
        return prob, info
    ult = max(r["_t_recv"] for r in f5) / 1000
    ws = [r["_t_recv"] for r in f5 if r["fuente"] == "ws"]
    hay_ws = any(ahora - t / 1000 < 86400 for t in ws)
    ult_ws = max(ws or [0]) / 1000
    umbral = UMBRAL_S if hay_ws else UMBRAL_SIN_WS_S
    info["ultima_fila_hace_s"] = round(ahora - ult)
    info["ultimo_ws_hace_s"] = round(ahora - ult_ws) if ult_ws else None
    if ahora - ult > umbral:
        prob["sin_5m_nuevos"] = f"sin filas 5m nuevas hace {int((ahora - ult) / 60)} min (> {umbral // 60})"
    if hay_ws and ahora - ult_ws > UMBRAL_WS_S:
        prob["ws_mudo"] = f"el listener new_market no ha recibido ningun evento por WS hace {int((ahora - ult_ws) / 60)} min (> {UMBRAL_WS_S // 60})"
    lejos = {}
    for r in f5:
        a = r["activo"]
        lejos[a] = max(lejos.get(a, 0), r["_cierre"])
    cob = {a: round((lejos.get(a, 0) - ahora) / 60) for a in sorted(x.upper() for x in U.ACTIVOS)}
    info["cobertura_min"] = cob
    flojas = {a: m for a, m in cob.items() if m < COBERTURA_MIN_MIN}
    if flojas:
        prob["cobertura"] = "5m por delante < %d min en %s" % (COBERTURA_MIN_MIN, ", ".join(f"{a}={m}" for a, m in flojas.items()))
    lag = sorted(r["_t_recv"] - r["_t_ev"] for r in f5
                 if r["fuente"] == "ws" and r["_t_ev"] is not None and ahora - r["_t_recv"] / 1000 < 3600)
    if lag and abs(lag[len(lag) // 2]) > DESFASE_MS:
        prob["desfase_reloj"] = f"desfase de reloj recepcion-evento mediano {lag[len(lag) // 2]} ms (> {DESFASE_MS})"
    rec = [r for r in f5 if ahora - r["_t_recv"] / 1000 < 86400]
    if len(rec) >= LEAD_N_MIN:
        buenos = sum(1 for r in rec if int(r["inicio_ts"]) - r["_t_recv"] / 1000 >= LEAD_MIN_S)
        info["lead_ok_frac_24h"] = round(buenos / len(rec), 3)
        if buenos / len(rec) < LEAD_FRAC_MIN:
            prob["lead_corto"] = (f"solo {100 * buenos / len(rec):.0f} % de los 5m de 24 h se vieron >= {LEAD_MIN_S // 60} min antes de su inicio "
                                  f"(n={len(rec)}, minimo {100 * LEAD_FRAC_MIN:.0f} %): A no basta, hace falta B")
    return prob, info


def evaluar(ahora, directorio=None):
    """-> (problemas, info). Nunca lanza: un error interno se convierte en el problema `vigia_error` (fail-loud)."""
    try:
        return _evaluar(ahora, directorio)
    except Exception as e:
        return {"vigia_error": f"error interno del vigia: {type(e).__name__}: {str(e)[:120]}"}, {}


def _enviar(msg, enviar):
    try:
        if enviar is None:
            from shadow_digest import enviar_telegram as enviar
        enviar(msg, bot="cripto")
        return True
    except Exception as e:
        print(f"no se pudo enviar a Telegram: {type(e).__name__}: {e}", flush=True)
        return False


def ejecutar(ahora=None, directorio=None, telegram=True, enviar=None):
    """El latch (`avisados`) solo se actualiza tras un envio OK: si Telegram falla, el aviso se REINTENTA en la siguiente pasada.
    Con telegram=False (uso manual) no se toca el estado."""
    ahora = time.time() if ahora is None else ahora
    d = Path(directorio or U.UNIV_DIR)
    ep = d / ESTADO_NOMBRE
    try:
        est = json.loads(ep.read_text())
    except (OSError, ValueError):
        est = {}
    est.setdefault("armado", False)
    est.setdefault("avisados", [])
    prob, info = evaluar(ahora, d)
    if not est["armado"] and "sin_fichero" not in prob and "sin_5m" not in prob and info.get("filas"):
        est["armado"] = True
    activos = sorted(prob) if (est["armado"] or "vigia_error" in prob) else []      # un fallo del propio vigia avisa siempre
    avisados = set(est["avisados"])
    nuevos = [k for k in activos if k not in avisados]
    msgs = []
    if nuevos:
        m = "Universo 5m: " + "; ".join(prob[k] for k in nuevos)
        msgs.append(m)
        if not telegram or _enviar(m, enviar):
            avisados |= set(nuevos)
    resueltos = sorted(avisados - set(activos))
    if resueltos:
        if not activos:
            m = "Universo 5m: recuperado (" + ", ".join(resueltos) + ")"
            msgs.append(m)
            if not telegram or _enviar(m, enviar):
                avisados -= set(resueltos)
        else:
            avisados -= set(resueltos)                      # un problema resuelto con otros aun activos: se rearma sin mensaje
    for m in msgs:
        print(m, flush=True)
    if telegram:
        est["avisados"] = sorted(avisados)               # el latch es solo el CONJUNTO de problemas ya notificados, sin valores recalculados
        try:
            d.mkdir(parents=True, exist_ok=True)
            tmp = ep.with_suffix(".tmp")
            tmp.write_text(json.dumps(est))
            os.replace(tmp, ep)
        except OSError:
            pass
    return prob, info, msgs


if __name__ == "__main__":
    sys.path.insert(0, "/root/polymarket-research")
    prob, info, _ = ejecutar(telegram="--sin-telegram" not in sys.argv)
    print(json.dumps({"problemas": prob, "info": info}, ensure_ascii=False))
