#!/usr/bin/env python3
"""
analisis_diario_salud_sistema.py — Auditoría diaria de salud del pipeline
completo: rendimiento (¿algún paso se ha vuelto lento?), procesos (¿algo
lleva atascado?), disco, memoria RAM, integridad de datos (¿se ha perdido
algo?) y estado de despliegue (verify_deploy.py).

Origen (04-Ago, petición explícita Javi tras el incidente del mismo día:
shadow_postmortem.py atascado >10min en un fit O(n²)-ish que nadie había
medido, bloqueando resolve/nuevas señales con dinero real, sin que ningún
vigía existente lo detectara hasta que se investigó a mano por qué 3
trades no cerraban). "Tiene que funcionar engrasado perfectamente... no
podemos permitirnos otro incidente de estos" — este script es la versión
"convertido en código que se audite solo" de esa petición (mismo
principio que el resto del proyecto: nunca prometer acordarse mejor).

Compara SIEMPRE contra una línea base persistida (data/shadow/
salud_sistema_historico.json) -- un pipeline que tarda 8s hoy y tardaba
8s ayer es sano; uno que tarda 8s hoy pero tardaba 90s hace una semana ya
merece mirarlo aunque no haya cruzado ningún umbral fijo todavía.

Cero llamadas de red -- todo se lee de logs/ficheros/ps locales. Solo
lectura, no toca dinero ni config. Avisa por Telegram SOLO si encuentra
una anomalía real (mismo patrón que el resto de vigías) -- el reporte
completo (anomalía o no) siempre se persiste en salud_sistema_diaria.json
y se loguea, para que el protocolo de arranque de sesión lo revise cada
día, encuentre o no encuentre algo.

Cron sugerido (franja tranquila, después del resto de análisis diarios
06:xx, antes de la ventana de trading 08:30 UTC):
  08 7 * * * flock -n /tmp/salud_sistema.lock /root/polymarket-research/.venv/bin/python /root/polymarket-research/analisis_diario_salud_sistema.py >> /root/polymarket-research/logs/analisis_diario_salud_sistema.log 2>&1
"""
import csv
import json
import re
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

DIR_SHADOW = REPO / "data" / "shadow"
DIR_LIVE = REPO / "data" / "live"
FAST_LOG = REPO / "logs" / "fast.log"
HIST_PATH = DIR_SHADOW / "salud_sistema_historico.json"
HOY_PATH = DIR_SHADOW / "salud_sistema_diaria.json"

# Umbrales absolutos, además de la comparación contra histórico -- ver
# docstring del módulo: ambos criterios importan, no solo uno.
UMBRAL_CICLO_LENTO_S = 120  # resolve+postmortem tardando más de esto es
# anómalo por sí solo (el incidente de hoy: 10+ min vs ~20s normal)
UMBRAL_PROCESO_COLGADO_S = 180  # un script de un solo ciclo (postmortem/
# resolve/predict/live_trade) vivo más de esto probablemente está atascado
UMBRAL_DISCO_LIBRE_PCT = 10.0
UMBRAL_TRADE_ABIERTO_TRAS_CIERRE_MIN = 20  # posición OPEN con end_date ya
# pasado hace más de esto -- exactamente el síntoma del incidente de hoy
UMBRAL_LOAD_RATIO = 3.0  # load average (5min) / nproc -- por encima de esto
# el sistema está sobresuscrito (05-Ago: load 9.6-15.4 en 2 cores, ratio
# 4.8-7.7, causó que git push fallara silenciosamente 4+ horas)
UMBRAL_PUSH_LAG_COMMITS = 15  # commits locales por delante de origin/main
# (ref local, sin fetch -- si el push lleva fallando un rato esto crece)


def _log(msg: str) -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts}] {msg}", flush=True)


def _sh(cmd: list[str]) -> str:
    try:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=15).stdout
    except Exception as e:
        return f"__error__: {e}"


def medir_ciclos_pipeline() -> dict:
    """Duración de cada tramo resolve→postmortem de las últimas 24h
    (el tramo que hoy se atascó) + huecos entre ciclos live_trade
    consecutivos (detecta un stall aunque no pase por resolve/postmortem)."""
    if not FAST_LOG.exists():
        return {"error": "fast.log no existe"}
    corte = datetime.now(timezone.utc) - timedelta(hours=24)
    resolve_ts, postmortem_ts, live_trade_ts = [], [], []
    re_resolve = re.compile(r"^\[([\d\-T:+]+)\] === Shadow resolve ===")
    re_postmortem = re.compile(r"^\[([\d\-T:+]+)\] === Fin postmortem ===")
    re_live = re.compile(r"^\[([\d\-T:+]+)\] === live_trade ciclo")
    try:
        with open(FAST_LOG, encoding="utf-8", errors="replace") as f:
            for linea in f:
                for regex, bucket in ((re_resolve, resolve_ts), (re_postmortem, postmortem_ts),
                                       (re_live, live_trade_ts)):
                    m = regex.match(linea)
                    if m:
                        try:
                            ts = datetime.fromisoformat(m.group(1))
                        except ValueError:
                            continue
                        if ts >= corte:
                            bucket.append(ts)
    except Exception as e:
        return {"error": f"no se pudo leer fast.log: {e}"}

    # Empareja cada "Shadow resolve" con el siguiente "Fin postmortem"
    duraciones = []
    j = 0
    for r in resolve_ts:
        while j < len(postmortem_ts) and postmortem_ts[j] < r:
            j += 1
        if j < len(postmortem_ts):
            duraciones.append((postmortem_ts[j] - r).total_seconds())

    huecos_live_trade = [
        (live_trade_ts[i + 1] - live_trade_ts[i]).total_seconds()
        for i in range(len(live_trade_ts) - 1)
    ]

    def _pctl(xs, p):
        if not xs:
            return None
        xs = sorted(xs)
        return xs[min(len(xs) - 1, int(len(xs) * p))]

    return {
        "n_ciclos_resolve_postmortem": len(duraciones),
        "resolve_postmortem_p50_s": round(_pctl(duraciones, 0.5), 1) if duraciones else None,
        "resolve_postmortem_p95_s": round(_pctl(duraciones, 0.95), 1) if duraciones else None,
        "resolve_postmortem_max_s": round(max(duraciones), 1) if duraciones else None,
        "n_ciclos_live_trade": len(live_trade_ts),
        "hueco_live_trade_max_s": round(max(huecos_live_trade), 1) if huecos_live_trade else None,
    }


def medir_procesos_colgados() -> list[dict]:
    """Scripts de un solo ciclo (no procesos persistentes) que llevan
    vivos más de UMBRAL_PROCESO_COLGADO_S -- mismo síntoma que
    shadow_postmortem.py hoy. Los procesos persistentes normales (fast,
    slow, screens de ejecutores) se excluyen a propósito, viven días."""
    objetivo = {"shadow_postmortem.py", "shadow_resolve.py", "shadow_predict.py",
                "live_trade.py", "fetch_binance_klines.py", "shadow_resumen.py"}
    out = _sh(["ps", "-eo", "pid,etimes,cmd", "--no-headers"])
    colgados = []
    for linea in out.splitlines():
        partes = linea.strip().split(None, 2)
        if len(partes) < 3:
            continue
        pid, etimes, cmd = partes
        if not any(obj in cmd for obj in objetivo):
            continue
        try:
            etimes_i = int(etimes)
        except ValueError:
            continue
        if etimes_i > UMBRAL_PROCESO_COLGADO_S:
            colgados.append({"pid": pid, "cmd": cmd.strip(), "segundos_vivo": etimes_i})
    return colgados


def medir_deploy_stale() -> dict:
    """Reutiliza verify_deploy.py -- que ninguna screen persistente esté
    corriendo código de disco distinto del que tiene cargado."""
    try:
        import verify_deploy
        est = verify_deploy.estado()
        stale = [n for n, d in est.items() if d["veredicto"] != "FRESH"]
        return {"n_screens": len(est), "stale": stale}
    except Exception as e:
        return {"error": str(e)}


def medir_disco() -> dict:
    df = _sh(["df", "/"]).splitlines()
    pct_usado = None
    gb_libres = None
    if len(df) >= 2:
        partes = df[1].split()
        if len(partes) >= 5:
            try:
                pct_usado = float(partes[4].rstrip("%"))
                gb_libres = round(int(partes[3]) / 1024 / 1024, 2)
            except ValueError:
                pass

    def _du(path: Path) -> float | None:
        if not path.exists():
            return None
        out = _sh(["du", "-sm", str(path)])
        try:
            return round(int(out.split()[0]) / 1024, 2)
        except (ValueError, IndexError):
            return None

    return {
        "pct_usado": pct_usado,
        "gb_libres": gb_libres,
        "git_gb": _du(REPO / ".git"),
        "data_gb": _du(REPO / "data"),
        "datalogs_gb": _du(Path("/root/polymarket-research-datalogs")),
    }


def medir_ram() -> dict:
    try:
        info = {}
        with open("/proc/meminfo", encoding="utf-8") as f:
            for linea in f:
                k, v = linea.split(":", 1)
                info[k] = int(v.strip().split()[0])  # kB
        total = info.get("MemTotal", 0)
        disponible = info.get("MemAvailable", 0)
        return {
            "ram_total_gb": round(total / 1024 / 1024, 2),
            "ram_disponible_gb": round(disponible / 1024 / 1024, 2),
            "ram_pct_libre": round(100 * disponible / total, 1) if total else None,
        }
    except Exception as e:
        return {"error": str(e)}


def medir_integridad_datos() -> dict:
    """(a) trades.csv: filas OPEN cuyo end_date ya pasó hace más de
    UMBRAL_TRADE_ABIERTO_TRAS_CIERRE_MIN -- exactamente el síntoma del
    incidente de hoy (3 trades reales sin cerrar). (b) results.csv/
    trades.csv: el nº de filas NO puede haber bajado respecto de ayer --
    una caída real indicaría pérdida de datos (corrupción, sobrescritura
    accidental), nunca es normal en ficheros append-only."""
    salida = {}
    ahora = datetime.now(timezone.utc)

    trades_path = DIR_LIVE / "trades.csv"
    atascados = []
    n_trades = 0
    try:
        with open(trades_path, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                n_trades += 1
                if row.get("status") != "OPEN":
                    continue
                end_str = (row.get("end_date") or "").replace("Z", "+00:00")
                try:
                    end_dt = datetime.fromisoformat(end_str)
                    if end_dt.tzinfo is None:
                        end_dt = end_dt.replace(tzinfo=timezone.utc)
                except Exception:
                    continue
                edad_min = (ahora - end_dt).total_seconds() / 60
                if edad_min > UMBRAL_TRADE_ABIERTO_TRAS_CIERRE_MIN:
                    atascados.append({
                        "market_id": row.get("market_id"), "strategy": row.get("strategy"),
                        "subtype": row.get("subtype"), "minutos_desde_cierre": round(edad_min, 1),
                    })
    except FileNotFoundError:
        salida["trades_csv_error"] = "no existe"

    results_path = DIR_SHADOW / "results.csv"
    n_results = 0
    try:
        with open(results_path, encoding="utf-8") as f:
            n_results = sum(1 for _ in f) - 1
    except FileNotFoundError:
        salida["results_csv_error"] = "no existe"

    salida["trades_abiertos_atascados"] = atascados
    salida["n_trades_total"] = n_trades
    salida["n_results_total"] = n_results
    return salida


def medir_carga_sistema() -> dict:
    """Load average + nº de cores -- ratio>UMBRAL_LOAD_RATIO sostenido
    revienta operaciones CPU-intensivas (git pack-objects el 05-Ago) sin
    que ningún otro check lo capture (RAM y disco pueden estar sanos con
    el sistema totalmente atascado de CPU)."""
    try:
        with open("/proc/loadavg", encoding="utf-8") as f:
            l1, l5, l15 = (float(x) for x in f.read().split()[:3])
    except Exception as e:
        return {"error": str(e)}
    try:
        nproc = int(_sh(["nproc"]).strip())
    except Exception:
        nproc = 1
    n_procesos = len(_sh(["ps", "-eo", "pid", "--no-headers"]).splitlines())
    return {
        "load1": l1, "load5": l5, "load15": l15, "nproc": nproc,
        "ratio5": round(l5 / nproc, 2) if nproc else None,
        "n_procesos_total": n_procesos,
    }


def medir_git_push_lag() -> dict:
    """Commits en HEAD por delante de la referencia LOCAL origin/main (sin
    fetch -- cero red, cero coste). Si el push lleva fallando, esta ref no
    avanza y el número crece cada ciclo -- exactamente el síntoma del
    05-Ago (push fallando desde 02:35 UTC, 4+ horas sin que nadie lo viera
    hasta que se intentó pushear a mano)."""
    try:
        out = _sh(["git", "-C", str(REPO), "rev-list", "--count", "origin/main..HEAD"])
        lag = int(out.strip())
        return {"commits_sin_pushear": lag}
    except Exception as e:
        return {"error": str(e)}


def main() -> int:
    _log("=== auditoría diaria de salud del sistema ===")
    reporte = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "pipeline": medir_ciclos_pipeline(),
        "procesos_colgados": medir_procesos_colgados(),
        "deploy": medir_deploy_stale(),
        "disco": medir_disco(),
        "ram": medir_ram(),
        "integridad_datos": medir_integridad_datos(),
        "carga_sistema": medir_carga_sistema(),
        "git_push": medir_git_push_lag(),
    }

    # Comparación contra ayer (histórico persistido) -- ver docstring:
    # importa tanto el umbral absoluto como la tendencia frente a la línea
    # base propia del sistema.
    historico = []
    if HIST_PATH.exists():
        try:
            historico = json.loads(HIST_PATH.read_text(encoding="utf-8"))
        except Exception:
            historico = []
    ayer = historico[-1] if historico else None

    anomalias = []
    p = reporte["pipeline"]
    if p.get("resolve_postmortem_max_s") and p["resolve_postmortem_max_s"] > UMBRAL_CICLO_LENTO_S:
        anomalias.append(f"⏱️ ciclo resolve+postmortem tardó {p['resolve_postmortem_max_s']:.0f}s "
                          f"(umbral {UMBRAL_CICLO_LENTO_S}s)")
    if ayer and p.get("resolve_postmortem_p50_s") and ayer.get("pipeline", {}).get("resolve_postmortem_p50_s"):
        hoy_p50 = p["resolve_postmortem_p50_s"]
        ayer_p50 = ayer["pipeline"]["resolve_postmortem_p50_s"]
        if ayer_p50 > 0 and hoy_p50 > ayer_p50 * 3 and hoy_p50 > 10:
            anomalias.append(f"📈 ciclo resolve+postmortem p50 subió de {ayer_p50:.1f}s a {hoy_p50:.1f}s "
                              f"(>3x) -- posible regresión de rendimiento")

    if reporte["procesos_colgados"]:
        for pc in reporte["procesos_colgados"]:
            anomalias.append(f"🚨 proceso colgado: {pc['cmd']} ({pc['segundos_vivo']}s vivo)")

    if reporte["deploy"].get("stale"):
        anomalias.append(f"⚠️ screens STALE (código en disco != código cargado): "
                          f"{', '.join(reporte['deploy']['stale'])}")

    d = reporte["disco"]
    if d.get("pct_usado") and d["pct_usado"] > (100 - UMBRAL_DISCO_LIBRE_PCT):
        anomalias.append(f"💾 disco al {d['pct_usado']:.0f}% ({d.get('gb_libres')}GB libres)")

    r = reporte["ram"]
    if r.get("ram_pct_libre") is not None and r["ram_pct_libre"] < 10:
        anomalias.append(f"🧠 RAM disponible {r['ram_pct_libre']:.0f}% libre")

    integ = reporte["integridad_datos"]
    if integ.get("trades_abiertos_atascados"):
        for t in integ["trades_abiertos_atascados"]:
            anomalias.append(f"⛔ trade real OPEN sin cerrar {t['minutos_desde_cierre']:.0f}min "
                              f"tras su cierre: {t['strategy']}#{t['subtype']} ({t['market_id']})")
    cs = reporte["carga_sistema"]
    if cs.get("ratio5") is not None and cs["ratio5"] > UMBRAL_LOAD_RATIO:
        anomalias.append(f"🔥 CPU sobresuscrita: load5={cs['load5']} en {cs['nproc']} cores "
                          f"(ratio={cs['ratio5']}x, umbral {UMBRAL_LOAD_RATIO}x) -- "
                          f"{cs.get('n_procesos_total')} procesos vivos")

    gp = reporte["git_push"]
    if gp.get("commits_sin_pushear", 0) > UMBRAL_PUSH_LAG_COMMITS:
        anomalias.append(f"📡 git push atascado: {gp['commits_sin_pushear']} commits locales "
                          f"sin llegar a GitHub (umbral {UMBRAL_PUSH_LAG_COMMITS}) -- riesgo de "
                          f"pérdida si el VPS cae")

    if ayer:
        ayer_integ = ayer.get("integridad_datos", {})
        for campo, etiqueta in (("n_trades_total", "trades.csv"), ("n_results_total", "results.csv")):
            hoy_n = integ.get(campo)
            ayer_n = ayer_integ.get(campo)
            if hoy_n is not None and ayer_n is not None and hoy_n < ayer_n:
                anomalias.append(f"🔴 {etiqueta} tiene MENOS filas que ayer ({hoy_n} < {ayer_n}) "
                                  f"-- posible pérdida de datos")

    reporte["anomalias"] = anomalias
    reporte["estado"] = "ANOMALIA" if anomalias else "OK"

    HOY_PATH.write_text(json.dumps(reporte, indent=2, ensure_ascii=False), encoding="utf-8")
    historico.append(reporte)
    historico = historico[-90:]  # 90 días de histórico, mismo horizonte que la retención de datos
    HIST_PATH.write_text(json.dumps(historico, indent=2, ensure_ascii=False), encoding="utf-8")

    _log(f"pipeline: p50={p.get('resolve_postmortem_p50_s')}s p95={p.get('resolve_postmortem_p95_s')}s "
         f"max={p.get('resolve_postmortem_max_s')}s (n={p.get('n_ciclos_resolve_postmortem')})")
    _log(f"disco: {d.get('pct_usado')}% usado, {d.get('gb_libres')}GB libres, "
         f".git={d.get('git_gb')}GB, data={d.get('data_gb')}GB")
    _log(f"ram: {r.get('ram_pct_libre')}% libre ({r.get('ram_disponible_gb')}GB de {r.get('ram_total_gb')}GB)")
    _log(f"integridad: {integ.get('n_trades_total')} trades, {integ.get('n_results_total')} results, "
         f"{len(integ.get('trades_abiertos_atascados', []))} atascados")
    _log(f"carga: load5={cs.get('load5')} nproc={cs.get('nproc')} ratio5={cs.get('ratio5')} "
         f"procesos={cs.get('n_procesos_total')} | git_push_lag={gp.get('commits_sin_pushear')} commits")
    _log(f"estado: {reporte['estado']} ({len(anomalias)} anomalía(s))")

    if anomalias:
        try:
            from shadow_digest import enviar_telegram
            texto = "🔧 *Auditoría diaria de salud del sistema — ANOMALÍAS*\n\n" + "\n".join(anomalias)
            ok = enviar_telegram(texto)
            _log(f"aviso Telegram enviado (ok={ok})")
        except Exception as e:
            _log(f"no se pudo enviar Telegram: {e}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
