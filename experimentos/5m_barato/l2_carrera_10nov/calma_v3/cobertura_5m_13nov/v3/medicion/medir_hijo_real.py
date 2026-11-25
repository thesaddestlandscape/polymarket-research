#!/usr/bin/env python3
"""Mide el HIJO REAL de libro_estado_ws en un entorno AISLADO (sin tocar produccion): padre = el modulo indicado, universo FIJO (json),
registro/libro5/txlog en un directorio de pruebas, Binance en RESERVA (un flock ficticio ocupa el lock de bnreg: el hijo se comporta como
en produccion, donde bnreg es el dueno). Solo lectura sobre el WS publico del CLOB.
Uso: medir_hijo_real.py <dir_con_libro_estado_ws.py> <universo.json> <dir_aislado> <segundos> <etiqueta> [dir_extra_pythonpath]"""
import json, os, sys, time, threading, subprocess, resource
d_mod, uni, aislado, dur, etiq = sys.argv[1], sys.argv[2], sys.argv[3], float(sys.argv[4]), sys.argv[5]
extra = sys.argv[6] if len(sys.argv) > 6 else None
os.makedirs(aislado, exist_ok=True)
os.environ["LIBRO_WS_REGISTRO_DIR"] = os.path.join(aislado, "dl")
os.environ["LIBRO5_DIR"] = os.path.join(aislado, "libro5")
os.environ["TXLOG_DIR"] = os.path.join(aislado, "tx")
os.makedirs(os.environ["LIBRO_WS_REGISTRO_DIR"], exist_ok=True)
lock = os.path.join(os.environ["LIBRO_WS_REGISTRO_DIR"], ".binance_registro.lock")
dueno = subprocess.Popen(["flock", "-n", lock, "sleep", str(int(dur) + 120)])     # bnreg ficticio: el hijo queda en RESERVA
time.sleep(0.5)
sys.path.insert(0, d_mod)
if extra:
    sys.path.insert(0, extra)
import libro_estado_ws as L
U = json.load(open(uni))
toks = U["toks"]; claves = U["claves"]; meta = {k: tuple(v) for k, v in U["meta"].items()}


def universo_fijo(filtro_marcos=None):
    L._UNIVERSO.clear()
    L._UNIVERSO.update({"toks": toks, "claves": claves, "meta": meta})
    return toks


L._tokens_universo = universo_fijo
if hasattr(L, "TOK_CACHE_PATH"):
    L.TOK_CACHE_PATH = type(L.TOK_CACHE_PATH)(os.path.join(aislado, "cache.json"))
L.iniciar(("5min", "15min", "60min"))
t0 = time.time()
while L._HIJO.get("proc") is None and time.time() - t0 < 30:
    time.sleep(0.2)
hijo = L._HIJO["proc"].pid
tick = os.sysconf("SC_CLK_TCK")


def cpu_rss(pid):
    try:
        f = open(f"/proc/{pid}/stat").read().rsplit(")", 1)[1].split()
        rss = int(open(f"/proc/{pid}/statm").read().split()[1]) * os.sysconf("SC_PAGE_SIZE") / 1048576
        return (int(f[11]) + int(f[12])) / tick, rss
    except OSError:
        return None, None


lags, m = [], {"n_ev0": None}


def muestrea_lag():
    while True:
        u = L._ESTADO.get("ultimo_evento_ms", 0)
        if u:
            lags.append(time.time() * 1000 - u)
        time.sleep(0.05)


threading.Thread(target=muestrea_lag, daemon=True).start()
time.sleep(20)                                           # calentamiento (altas en trozos, libros iniciales)
lags.clear()
c0, _ = cpu_rss(hijo); p0 = sum(resource.getrusage(resource.RUSAGE_SELF)[:2]); e0 = L._ESTADO["n_eventos"]; t1 = time.time()
rss_max, serie = 0.0, []
while time.time() - t1 < dur:
    time.sleep(5)
    c, r = cpu_rss(hijo)
    rss_max = max(rss_max, r or 0)
    serie.append((round(time.time() - t1), round(r or 0, 1)))
c1, r1 = cpu_rss(hijo); p1 = sum(resource.getrusage(resource.RUSAGE_SELF)[:2]); e1 = L._ESTADO["n_eventos"]; seg = time.time() - t1
lg = sorted(lags)
pc = lambda q: round(lg[min(len(lg) - 1, int(q * len(lg)))], 1) if lg else None
print(json.dumps({"etiqueta": etiq, "segundos": round(seg), "tokens": len(toks), "hijo_pid": hijo, "reinicios_hijo": L._ESTADO["reinicios_hijo"],
                  "hijo_cpu_pct_1core": round(100 * (c1 - c0) / seg, 2), "hijo_rss_MB_final": round(r1, 1), "hijo_rss_MB_max": round(rss_max, 1),
                  "padre_cpu_pct_1core": round(100 * (p1 - p0) / seg, 2), "padre_rss_MB_max": round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024, 1),
                  "eventos_h": e1 - e0, "eventos_h_por_s": round((e1 - e0) / seg, 1),
                  "lag_ultimo_evento_ms_p50_p90_p99_max": [pc(.5), pc(.9), pc(.99), pc(1.0)] if lg else None, "n_lag": len(lg)}), flush=True)
os._exit(0)
