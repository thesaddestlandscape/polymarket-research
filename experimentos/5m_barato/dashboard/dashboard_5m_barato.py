#!/usr/bin/env python3
"""Dashboard 5m barato (SOLO LECTURA) -- puerto 8892, screen `dash5m`. Solo stdlib, sin CDN, sin claves en la pagina.

Mismo patron que dashboard_server.py (HTTP Basic con DASHBOARD_USER/DASHBOARD_PASS de data/live/.env, tema oscuro), pero servidor
NUEVO e independiente. Nada de weather ni sports. Ningun endpoint envia ordenes, resetea suelos ni toca screens/procesos.

Pestanas: 1 CONTABILIDAD (wallet dedicada, estado_dashboard.json), 2 B REAL (H47: ledger por TAIL inverso en bloques + supervisor),
3 VIGIAS/H23/H59 (solo estado y ultima salida de logs, sin analizar).

Refresco de la contabilidad: un hilo ejecuta `nice -n 19 ionice -c3 python3 contabilidad_wallet_dedicada/actualizar.py` como maximo
cada 5 min (flock, nunca dos a la vez, nunca en 06:00-09:15Z salvo boton manual, que respeta el flock y un minimo de 60 s).

Arranque (NO lanzado todavia; registrado en pipeline_watchdog.py y verify_deploy.py):
  cd /root/polymarket-research && screen -dmS dash5m bash -c 'nice -n 10 .venv/bin/python experimentos/5m_barato/dashboard/dashboard_5m_barato.py >> logs/dashboard_5m_barato.log 2>&1'
Uso manual: dashboard_5m_barato.py [puerto] [--host 127.0.0.1]   (sin credenciales configuradas solo escucha en loopback: fail-closed)
"""
import base64
import fcntl
import hmac
import json
import os
import re
import resource
import socket
import subprocess
import sys
import threading
import time
from collections import Counter
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from socketserver import ThreadingMixIn

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[2]
CONT = RAIZ / "experimentos" / "5m_barato" / "contabilidad_wallet_dedicada"
ESTADO_JSON = CONT / "estado_dashboard.json"
POSICIONES_CSV = CONT / "posiciones.csv"
ACTUALIZAR = CONT / "actualizar.py"
LOCK_ACT = AQUI / ".actualizar.lock"
DL = Path("/root/polymarket-research-datalogs")
LEDGER_B = DL / "experimento_h47_B_ledger.jsonl"
SUP_LOG = DL / "h47_tandas_supervisor.log"
SUP_ESTADO = DL / "h47_tandas_supervisor_estado.json"
SUP_STOP = DL / "h47_tandas_supervisor.STOP"
KILLS = [DL / "experimento_h47.KILL", DL / "experimento_pares_dedicada.KILL"]
LOGS = RAIZ / "logs"

REFRESCO_S = 300            # contabilidad: maximo cada 5 min
MANUAL_MIN_S = 60
VENTANA_PROHIBIDA = (6 * 60, 9 * 60 + 15)   # minutos UTC, 06:00-09:15Z: sin refresco automatico
TIMEOUT_ACT_S = 900
LEDGER_TOPE_BYTES = 8 * 1024 * 1024
LEDGER_BLOQUE = 262144
PORT_DEF = 8892

# ------------------------------------------------------------------ auth (patron de dashboard_server.py)
_CLAVES_OK = ("DASHBOARD_USER", "DASHBOARD_PASS")


def _cargar_credenciales():
    """Env primero; si faltan, SOLO las dos claves DASHBOARD_* de data/live/.env (el resto del fichero se descarta sin guardarlo)."""
    u, p = os.environ.get("DASHBOARD_USER", ""), os.environ.get("DASHBOARD_PASS", "")
    if u and p:
        return u, p
    try:
        vals = {}
        for ln in (RAIZ / "data" / "live" / ".env").read_text(errors="replace").splitlines():
            k, sep, v = ln.strip().partition("=")
            if sep and k.strip() in _CLAVES_OK:
                vals[k.strip()] = v.strip().strip("'\"")
        return vals.get("DASHBOARD_USER", ""), vals.get("DASHBOARD_PASS", "")
    except OSError:
        return "", ""


DASH_USER, DASH_PASS = _cargar_credenciales()

# ------------------------------------------------------------------ utilidades
def ahora_utc():
    return datetime.now(timezone.utc)


def iso(ts):
    return datetime.fromtimestamp(ts, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def leer_json(ruta):
    try:
        return json.loads(Path(ruta).read_text())
    except (OSError, ValueError):
        return None


def cola_texto(ruta, nbytes=8192):
    """Ultimos bytes del fichero (TAIL), sin cargarlo entero. [] si no existe."""
    try:
        with open(ruta, "rb") as f:
            n = f.seek(0, 2)
            f.seek(max(0, n - nbytes))
            datos = f.read()
        lineas = datos.decode("utf-8", "replace").splitlines()
        return lineas[1:] if n > nbytes else lineas
    except OSError:
        return []


def en_ventana_prohibida(t=None):
    t = t or ahora_utc()
    m = t.hour * 60 + t.minute
    return VENTANA_PROHIBIDA[0] <= m < VENTANA_PROHIBIDA[1]


# ------------------------------------------------------------------ refresco de la contabilidad (hilo + flock)
_ST = {"ultimo_intento": 0.0, "ultimo_ok": None, "ultimo_error": None, "corriendo": False, "manual_t": 0.0, "origen": None}
_ST_LOCK = threading.Lock()


def _limites_hijo():
    resource.setrlimit(resource.RLIMIT_AS, (2_500_000_000, 2_500_000_000))


def edad_estado_s():
    try:
        return time.time() - ESTADO_JSON.stat().st_mtime
    except OSError:
        return None


def ejecutar_actualizar(origen):
    """Una sola ejecucion de actualizar.py bajo flock no bloqueante. Devuelve texto de resultado."""
    with _ST_LOCK:
        if _ST["corriendo"]:
            return "ya hay una actualizacion en curso"
        _ST["corriendo"] = True
    fd = None
    try:
        fd = os.open(LOCK_ACT, os.O_CREAT | os.O_RDWR, 0o644)
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError:
            return "otra instancia tiene el flock"
        with _ST_LOCK:
            _ST["ultimo_intento"] = time.time()
            _ST["origen"] = origen
        cmd = ["nice", "-n", "19", "ionice", "-c3", sys.executable, str(ACTUALIZAR)]
        try:
            r = subprocess.run(cmd, cwd=str(RAIZ), capture_output=True, text=True, timeout=TIMEOUT_ACT_S, preexec_fn=_limites_hijo)
            ok = r.returncode == 0
            with _ST_LOCK:
                if ok:
                    _ST["ultimo_ok"], _ST["ultimo_error"] = time.time(), None
                else:
                    _ST["ultimo_error"] = f"rc={r.returncode}: {(r.stderr or r.stdout)[-300:]}"
            return "ok" if ok else _ST["ultimo_error"]
        except subprocess.TimeoutExpired:
            with _ST_LOCK:
                _ST["ultimo_error"] = f"timeout {TIMEOUT_ACT_S}s"
            return _ST["ultimo_error"]
        except Exception as e:  # noqa: BLE001
            with _ST_LOCK:
                _ST["ultimo_error"] = f"{type(e).__name__}: {e}"
            return _ST["ultimo_error"]
    finally:
        with _ST_LOCK:
            _ST["corriendo"] = False
        if fd is not None:
            try:
                os.close(fd)   # suelta el flock
            except OSError:
                pass


def bucle_refresco():
    while True:
        try:
            t = ahora_utc()
            edad = edad_estado_s()
            desde_intento = time.time() - _ST["ultimo_intento"]
            if (not en_ventana_prohibida(t) and (edad is None or edad >= REFRESCO_S) and desde_intento >= REFRESCO_S):
                ejecutar_actualizar("auto")
        except Exception as e:  # noqa: BLE001
            print(f"[dash5m] bucle_refresco: {type(e).__name__}: {e}", flush=True)
        time.sleep(30)


# ------------------------------------------------------------------ pestana 1: contabilidad
def datos_contabilidad():
    d = leer_json(ESTADO_JSON)
    if not isinstance(d, dict):
        return {"error": f"no se puede leer {ESTADO_JSON}"}
    if d.get("schema_version") != 1:
        return {"error": f"schema_version={d.get('schema_version')} no soportado (se espera 1)"}
    out = dict(d)
    # concentracion global: PnL realizado sin las 2 mejores posiciones liquidadas (de posiciones.csv)
    try:
        import csv
        pnls = []
        with open(POSICIONES_CSV, newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                if str(r.get("estado", "")).startswith("liquidada") and r.get("pnl_realizado") not in (None, ""):
                    pnls.append(float(r["pnl_realizado"]))
        pnls.sort(reverse=True)
        out["concentracion_global"] = {"n_posiciones_liquidadas": len(pnls), "pnl_total": round(sum(pnls), 4),
                                       "pnl_sin_2_mejores": round(sum(pnls[2:]), 4) if len(pnls) > 2 else None}
    except (OSError, ValueError, KeyError):
        out["concentracion_global"] = None
    out["_edad_s"] = edad_estado_s()
    return out


# ------------------------------------------------------------------ pestana 2: B real
_RE_TIPO = re.compile(rb'"tipo": "([a-z_0-9]+)"')
_TIPOS_JSON = {b"config", b"suelo_calculado", b"suelo_fijado", b"suelo_subido", b"suelo_reiniciado", b"kill", b"kill_rearmado",
               b"gemelo_relleno", b"relleno_tardio", b"puja_fin", b"fin_ejecucion", b"bloqueo_suelo_saldo"}
_CACHE_B = {"clave": None, "val": None}


def _ledger_reverso():
    """Lineas del ledger del final hacia el principio por bloques, hasta LEDGER_TOPE_BYTES. Nunca carga el fichero entero."""
    try:
        f = open(LEDGER_B, "rb")
    except OSError:
        return
    with f:
        pos = f.seek(0, 2)
        fin_ventana = max(0, pos - LEDGER_TOPE_BYTES)
        resto = b""
        while pos > fin_ventana:
            n = min(LEDGER_BLOQUE, pos - fin_ventana)
            pos -= n
            f.seek(pos)
            lineas = (f.read(n) + resto).split(b"\n")
            resto = lineas[0] if pos > fin_ventana else b""
            for ln in reversed(lineas[1:] if pos > fin_ventana else lineas):
                if ln.strip():
                    yield ln
        if resto.strip() and pos <= 0:
            yield resto


def analizar_ledger_b():
    try:
        st = LEDGER_B.stat()
    except OSError:
        return {"error": f"no existe {LEDGER_B}"}
    clave = (st.st_mtime_ns, st.st_size)
    if _CACHE_B["clave"] == clave:
        return _CACHE_B["val"]
    cont = Counter()           # tipos desde el ultimo `config` (tanda/arranque actual)
    config = None
    suelo = None               # max de suelos desde el ultimo suelo_reiniciado (logica del supervisor)
    suelo_cerrado = False
    kill = None                # 'kill' | 'rearmado' (el mas reciente)
    rellenos, ult_evento_ts, ult_fin_puja = [], None, None
    ult_bloqueo = None
    vistas = 0
    for ln in _ledger_reverso():
        vistas += 1
        m = _RE_TIPO.search(ln)
        if not m:
            continue
        tipo = m.group(1)
        if config is None:
            cont[tipo.decode()] += 1
        if tipo not in _TIPOS_JSON:
            if ult_evento_ts is None:
                try:
                    ult_evento_ts = json.loads(ln).get("ts")
                except ValueError:
                    pass
            continue
        try:
            e = json.loads(ln)
        except ValueError:
            continue
        if ult_evento_ts is None:
            ult_evento_ts = e.get("ts")
        t = tipo.decode()
        if t == "config" and config is None:
            config = e
        elif t in ("suelo_calculado", "suelo_fijado", "suelo_subido") and not suelo_cerrado and e.get("suelo") is not None:
            try:
                v = float(e["suelo"])
                suelo = v if suelo is None else max(suelo, v)
            except (TypeError, ValueError):
                pass
        elif t == "suelo_reiniciado" and not suelo_cerrado:
            suelo_cerrado = True
            if suelo is None:
                try:
                    suelo = float(e["saldo_base"]) - 5.0
                except (KeyError, TypeError, ValueError):
                    pass
        elif t == "kill_rearmado" and kill is None:
            kill = {"estado": "rearmado", "ts": e.get("ts")}
        elif t == "kill" and kill is None and e.get("real"):
            kill = {"estado": "KILL", "ts": e.get("ts"), "motivo": str(e.get("motivo") or e.get("razon") or "")[:200]}
        elif t in ("gemelo_relleno", "relleno_tardio") and len(rellenos) < 15 and (config is None):
            rellenos.append({"ts": e.get("ts"), "tipo": t, "acc": e.get("acc_total", e.get("acc")), "precio": e.get("precio"),
                             "slug": e.get("slug")})
        elif t == "puja_fin" and ult_fin_puja is None:
            ult_fin_puja = {k: e.get(k) for k in ("ts", "slug", "coin", "lado", "n_ordenes", "llenas_detectadas", "coste_detectado", "fin_puja")}
        elif t == "bloqueo_suelo_saldo" and ult_bloqueo is None:
            ult_bloqueo = {k: e.get(k) for k in ("ts", "saldo", "comprometido", "coste", "minimo")}
    cfg = None
    if config:
        cfg = {k: config.get(k) for k in ("ts", "n_max", "t_stop", "size", "monedas", "k", "saldo_min", "presupuesto_util", "saldo_inicial",
                                          "saldo_verificado", "max_vivas", "codigo_sha", "n_usadas_previas")}
    val = {
        "ledger_bytes": st.st_size, "ledger_mtime": iso(st.st_mtime), "lineas_leidas": vistas, "tope_bytes": LEDGER_TOPE_BYTES,
        "config": cfg, "suelo": suelo, "kill_ledger": kill or {"estado": "sin_eventos_kill_en_ventana"},
        "eventos_desde_config": dict(cont), "rellenos_recientes_tanda_actual": rellenos, "ultima_puja_fin": ult_fin_puja,
        "ultimo_bloqueo_suelo": ult_bloqueo, "ultimo_evento_ts": ult_evento_ts,
    }
    _CACHE_B.update(clave=clave, val=val)
    return val


def _screens():
    try:
        out = subprocess.run(["screen", "-ls"], capture_output=True, text=True, timeout=5).stdout
    except (OSError, subprocess.TimeoutExpired):
        return None
    return out


def estado_screens(nombres):
    out = _screens()
    if out is None:
        return {n: None for n in nombres}
    res = {}
    for n in nombres:
        linea = next((ln for ln in out.splitlines() if re.search(rf"\.{re.escape(n)}\s", ln)), None)
        res[n] = None if linea is None else ("Dead" if "Dead" in linea else "viva")
        if linea is None:
            res[n] = "ausente"
    return res


def datos_b_real():
    c = leer_json(ESTADO_JSON) or {}
    b = analizar_ledger_b()
    tandas = c.get("tandas_B") or []
    sup_lineas = [ln[:240] for ln in cola_texto(SUP_LOG, 6144) if ln.strip()][-14:]
    try:
        sup_edad = time.time() - SUP_LOG.stat().st_mtime
    except OSError:
        sup_edad = None
    sup_estado = leer_json(SUP_ESTADO) or {}
    pausa = sup_estado.get("pausa_hasta")
    kill_files = [str(k.name) for k in KILLS if k.exists()]
    kill_ledger = (b.get("kill_ledger") or {}).get("estado") if isinstance(b, dict) else None
    return {
        "saldo": (c.get("saldo") or {}),
        "tanda_actual": tandas[-1] if tandas else None,
        "n_tandas": len(tandas),
        "ledger": b,
        "kill": {"ficheros_kill": kill_files, "ledger": kill_ledger,
                 "pendiente": bool(kill_files) or kill_ledger == "KILL"},
        "supervisor": {"log_lineas": sup_lineas, "log_edad_s": sup_edad, "stop_file": SUP_STOP.exists(),
                       "pausa_hasta": pausa, "pausado": bool(pausa) and float(pausa) > time.time() if isinstance(pausa, (int, float)) else False,
                       "screens": estado_screens(["h47sup", "h47B"])},
    }


# ------------------------------------------------------------------ pestana 3: vigias / H23 / H59 (solo estado, sin analizar)
_VIGIAS = [
    ("m5barato_forward_diario.log", "V5/V6/V7/FV v4 (run_m5barato_forward_diario.sh, 05:50)"),
    ("vigia_5m_barato_forward.log", "V4 congelado (04:35)"),
    ("vigia_5m_barato_v2_forward.log", "V2 (05:05)"),
    ("vigia_5m_barato_v3_forward.log", "V3 (05:10)"),
    ("vigia_5m_barato_maker_forward.log", "H5M maker (05:20)"),
    ("vigia_5m_barato_r5k.log", "R5K"),
    ("h23_shadow.log", "H23 shadow (screen h23shadow)"),
    ("a6_shadow.log", "A6/H43 shadow (screen a6shadow)"),
]
_H59_GLOBS = ["*h59*", "*H59*"]


def datos_vigias():
    filas = []
    for nombre, desc in _VIGIAS:
        p = LOGS / nombre
        try:
            st = p.stat()
        except OSError:
            filas.append({"log": nombre, "desc": desc, "existe": False})
            continue
        util = [ln for ln in cola_texto(p, 6144) if ln.strip() and not ln.startswith("Mensaje enviado")]
        filas.append({"log": nombre, "desc": desc, "existe": True, "mtime": iso(st.st_mtime), "edad_s": time.time() - st.st_mtime,
                      "bytes": st.st_size, "ultimas": [ln[:260] for ln in util[-3:]]})
    h59 = []
    for base in (LOGS, DL):
        for g in _H59_GLOBS:
            h59 += [str(x) for x in sorted(base.glob(g))[:5]]
    return {"vigias": filas, "h59_ficheros": h59,
            "screens": estado_screens(["h23shadow", "a6shadow", "h47B", "h47sup", "dash5m"]),
            "nota": "Solo estado y ultima salida de cada log; sin analisis ni veredicto propio."}


# ------------------------------------------------------------------ API
def estado_global():
    with _ST_LOCK:
        st = dict(_ST)
    return {
        "ahora_utc": ahora_utc().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "refresco": {"edad_estado_s": edad_estado_s(), "corriendo": st["corriendo"], "origen_ultimo": st["origen"],
                     "ultimo_ok": iso(st["ultimo_ok"]) if st["ultimo_ok"] else None, "ultimo_error": st["ultimo_error"],
                     "ventana_prohibida_auto": en_ventana_prohibida(), "cada_s": REFRESCO_S},
        "load1": os.getloadavg()[0],
    }


def api_datos():
    return {"global": estado_global(), "contabilidad": datos_contabilidad(), "b_real": datos_b_real(), "vigias": datos_vigias()}


# ------------------------------------------------------------------ HTML (sin CDN; todo texto via textContent)
HTML = r"""<!doctype html><html lang="es"><head><meta charset="utf-8"><title>5m barato</title>
<meta name="viewport" content="width=device-width,initial-scale=1"><style>
:root{--bg:#131722;--card:#1e222d;--border:#2a2e39;--text:#d1d4dc;--mut:#787b86;--green:#26a69a;--red:#ef5350;--amber:#ffb74d;--blue:#2962ff}
*{box-sizing:border-box;margin:0;padding:0}body{background:var(--bg);color:var(--text);font:13px -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif}
header{display:flex;justify-content:space-between;align-items:center;padding:10px 18px;background:var(--card);border-bottom:1px solid var(--border)}
h1{font-size:16px}h2{font-size:13px;margin:14px 0 6px;color:var(--mut);text-transform:uppercase;letter-spacing:.05em}
.tabs{display:flex;gap:4px;padding:8px 14px;background:var(--card);border-bottom:1px solid var(--border)}
.tab{padding:6px 14px;border:1px solid var(--border);border-radius:4px;cursor:pointer;color:var(--mut);background:none}
.tab.on{color:var(--blue);border-color:var(--blue);background:#2962ff22}
main{padding:14px 18px;max-width:1400px}.pane{display:none}.pane.on{display:block}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(190px,1fr));gap:8px}
.card{background:var(--card);border:1px solid var(--border);border-radius:4px;padding:10px 12px}.card .k{color:var(--mut);font-size:11px}.card .v{font-size:19px;margin-top:3px}
.aviso{background:#ffb74d18;border:1px solid var(--amber);color:var(--amber);padding:8px 12px;border-radius:4px;margin:8px 0}
.bad{background:#ef535022;border:1px solid var(--red);color:var(--red);padding:8px 12px;border-radius:4px;margin:8px 0}
.ok{color:var(--green)}.no{color:var(--red)}.am{color:var(--amber)}.mut{color:var(--mut)}
table{border-collapse:collapse;width:100%;background:var(--card)}th,td{padding:4px 8px;border-bottom:1px solid var(--border);text-align:right;white-space:nowrap}
th{color:var(--mut);font-weight:500;font-size:11px}td:first-child,th:first-child,td.l,th.l{text-align:left}.sc{overflow-x:auto}
pre{background:var(--card);border:1px solid var(--border);padding:8px;font-size:11px;white-space:pre-wrap;word-break:break-all;border-radius:4px}
button{background:var(--card);color:var(--text);border:1px solid var(--border);padding:5px 12px;border-radius:4px;cursor:pointer}
svg{background:var(--card);border:1px solid var(--border);border-radius:4px;width:100%;height:200px}
</style></head><body>
<header><h1>5m barato <span class="mut">(solo lectura)</span></h1><div><span id="hdr" class="mut"></span> <button id="btn">Actualizar contabilidad ahora</button></div></header>
<div class="tabs"><button class="tab on" data-p="p1">1 Contabilidad</button><button class="tab" data-p="p2">2 B real</button><button class="tab" data-p="p3">3 Vigias / H23 / H59</button></div>
<main><div id="p1" class="pane on"></div><div id="p2" class="pane"></div><div id="p3" class="pane"></div></main>
<script>
const $=id=>document.getElementById(id);
function el(t,c,x){const e=document.createElement(t);if(c)e.className=c;if(x!==undefined&&x!==null)e.textContent=x;return e}
function f(v,d){return (v===null||v===undefined)?'n/d':(typeof v==='number'?v.toFixed(d===undefined?2:d):String(v))}
function sg(v,d){if(v===null||v===undefined)return el('span','mut','n/d');const s=el('span',v>0?'ok':(v<0?'no':''),(v>0?'+':'')+v.toFixed(d===undefined?2:d));return s}
function card(k,v,cls){const c=el('div','card');c.appendChild(el('div','k',k));c.appendChild(el('div','v '+(cls||''),v));return c}
function cards(items){const d=el('div','cards');items.forEach(i=>d.appendChild(card(i[0],i[1],i[2])));return d}
function tabla(cols,rows){const w=el('div','sc'),t=el('table'),h=el('tr');cols.forEach(c=>h.appendChild(el('th',c.l?'l':'',c.t)));t.appendChild(h);
 rows.forEach(r=>{const tr=el('tr');cols.forEach(c=>{const td=el('td',c.l?'l':'');let v=c.g(r);if(v instanceof Node)td.appendChild(v);else td.textContent=v;tr.appendChild(td)});t.appendChild(tr)});w.appendChild(t);return w}
function edad(s){if(s===null||s===undefined)return 'n/d';if(s<90)return Math.round(s)+' s';if(s<5400)return Math.round(s/60)+' min';if(s<172800)return (s/3600).toFixed(1)+' h';return (s/86400).toFixed(1)+' d'}
function grafico(serie,campo,titulo){const W=900,H=200,P=34;const ns='http://www.w3.org/2000/svg';const s=document.createElementNS(ns,'svg');s.setAttribute('viewBox','0 0 '+W+' '+H);
 const v=serie.map(x=>x[campo]).filter(x=>x!==null&&x!==undefined);if(v.length<2){s.appendChild(Object.assign(document.createElementNS(ns,'text'),{textContent:'sin datos'}));return s}
 const mn=Math.min(0,...v),mx=Math.max(...v),rg=(mx-mn)||1;const X=i=>P+i*(W-2*P)/(serie.length-1),Y=y=>H-P-(y-mn)*(H-2*P)/rg;
 let d='';serie.forEach((x,i)=>{if(x[campo]!==null&&x[campo]!==undefined)d+=(d?'L':'M')+X(i).toFixed(1)+' '+Y(x[campo]).toFixed(1)});
 const mk=(n,a)=>{const e=document.createElementNS(ns,n);for(const k in a)e.setAttribute(k,a[k]);return e};
 s.appendChild(mk('line',{x1:P,x2:W-P,y1:Y(0),y2:Y(0),stroke:'#2a2e39'}));
 s.appendChild(mk('path',{d:d,fill:'none',stroke:'#26a69a','stroke-width':2}));
 const t=(x,y,txt,a)=>{const e=mk('text',{x:x,y:y,fill:'#787b86','font-size':11,'text-anchor':a||'start'});e.textContent=txt;s.appendChild(e)};
 t(P,14,titulo);t(4,Y(mx)+4,mx.toFixed(1));t(4,Y(mn)+4,mn.toFixed(1));t(P,H-8,serie[0].fecha);t(W-P,H-8,serie[serie.length-1].fecha,'end');return s}
function rend1(D){const p=$('p1');p.textContent='';const c=D.contabilidad;if(c.error){p.appendChild(el('div','bad','ERROR: '+c.error));return}
 const cu=c.cuadre||{};
 p.appendChild(el('div',cu.ok?'aviso':'bad',''));p.lastChild.textContent=cu.ok?('CUADRE OK: diferencia '+f(cu.diferencia_pusd,6)+' pUSD (tolerancia '+f(cu.tolerancia_pusd,6)+')'):('CUADRE NO CUADRA: diferencia '+f(cu.diferencia_pusd,6)+' pUSD. '+(cu.motivo||''));
 p.lastChild.className=cu.ok?'card':'bad';p.lastChild.style.margin='8px 0';if(cu.ok)p.lastChild.style.color='var(--green)';
 const cg=c.concentracion_global;
 const av=el('div','aviso','AVISO DE CONCENTRACION: el PnL realizado depende de pocas posiciones. Sin las 2 mejores posiciones liquidadas: '+(cg&&cg.pnl_sin_2_mejores!==null?f(cg.pnl_sin_2_mejores)+' pUSD (de '+f(cg.pnl_total)+' sobre '+cg.n_posiciones_liquidadas+' posiciones)':'n/d')+'. El rol maker/tomador de cada fill es INFERIDO (no observado). EV ponderado por EUR, no por unidad.');p.appendChild(av);
 const s=c.saldo||{},k=c.capital||{},n=c.pnl||{};
 p.appendChild(cards([['Saldo on-chain (pUSD)',f(s.pusd_onchain,4)],['Hora del saldo (bloque '+f(s.bloque,0)+')',s.ts_utc||'n/d'],['Capital neto depositado',f(k.depositado_neto)],
  ['PnL realizado total',(n.realizado_total>=0?'+':'')+f(n.realizado_total),n.realizado_total>=0?'ok':'no'],['No realizado (MTM)',f(n.no_realizado_mtm)],['Saldo - capital',f(n.saldo_menos_capital_neto)],
  ['EV ponderado /EUR',f(n.ev_ponderado_por_euro,3)],['Comisiones',f(n.comisiones_pagadas,4)],['Posiciones / filas',f(n.n_posiciones,0)+' / '+f(n.n_filas_fill,0)],['Ganadoras por redimir',f(n.ganadoras_por_redimir_pusd)]]));
 const cols=[{t:'',l:1,g:r=>r.experimento!==undefined?r.experimento:('Tanda B '+r.tanda)},{t:'filas',g:r=>f(r.n_filas,0)},{t:'pos',g:r=>f(r.n_posiciones,0)},{t:'liq',g:r=>f(r.n_posiciones_liquidadas,0)},
  {t:'gan/perd',g:r=>r.ganadoras_posiciones+'/'+r.perdedoras_posiciones},{t:'coste',g:r=>f(r.coste_total)},{t:'PnL realizado',g:r=>sg(r.pnl_realizado)},{t:'sin 2 mejores',g:r=>sg(r.pnl_realizado_sin_2_mejores_posiciones)},
  {t:'EV pond./EUR',g:r=>f(r.ev_ponderado_por_euro,3)},{t:'abierto (coste)',g:r=>f(r.coste_abierto_pendiente)},{t:'MTM',g:r=>sg(r.pnl_no_realizado_mtm)},{t:'inicio',l:1,g:r=>r.inicio_utc||''}];
 p.appendChild(el('h2',null,'PnL por experimento'));p.appendChild(tabla(cols,c.por_experimento||[]));
 p.appendChild(el('h2',null,'PnL por tanda de B'));p.appendChild(tabla(cols,c.tandas_B||[]));
 const pa=c.posiciones_abiertas||{};p.appendChild(el('h2',null,'Posiciones abiertas ('+f(pa.n_filas,0)+' filas, coste '+f(pa.coste)+', MTM '+f(pa.valor_mtm,4)+', valor data-api '+f(pa.valor_data_api_value,4)+')'));
 p.appendChild(tabla([{t:'mercado',l:1,g:r=>r.mercado},{t:'lado',g:r=>r.outcome},{t:'acciones',g:r=>f(r.acciones,2)},{t:'coste',g:r=>f(r.coste)},{t:'MTM',g:r=>f(r.valor_mtm,4)},{t:'estado',l:1,g:r=>r.estado},{t:'exp',l:1,g:r=>r.experimento},{t:'tanda',g:r=>f(r.tanda_B,0)}],pa.detalle||[]));
 p.appendChild(el('h2',null,'Comprobaciones de cuadre'));
 p.appendChild(tabla([{t:'comprobacion',l:1,g:r=>r.nombre},{t:'estado',g:r=>{const inf=r.nombre.indexOf('informativo')>=0;const e=el('span',r.ok?'ok':(inf?'am':'no'),r.ok?'OK':(inf?'INFORMATIVO':'FALLA'));return e}},{t:'diferencia',g:r=>f(r.diferencia_pusd,6)}],cu.comprobaciones||[]));
 const cb=c.cobertura||{},oc=cb.onchain||{},ad=cb.actividad_data_api||{},gm=cb.desenlaces_gamma||{},cl=cb.conciliacion_ledger_B||{};
 p.appendChild(el('h2',null,'Cobertura'));
 p.appendChild(cards([['On-chain',f(oc.metodo)+' bloques '+f(oc.desde_bloque,0)+'..'+f(oc.hasta_bloque,0)+' ('+f(oc.transferencias_pusd_wallet,0)+' mov.)'],['data-api /activity',f(ad.filas,0)+' filas'],['Desenlaces gamma',f(gm.resueltos,0)+' de '+f(gm.mercados,0)+' resueltos'],
  ['Ledger B vs on-chain',f(cl.acciones_ledger,2)+' vs '+f(cl.acciones_onchain,2)+' acc., '+f(cl.n_discrepancias,0)+' disc.'],['No atribuido',f((c.no_atribuido||{}).fills,0)+' fills']]));
 p.appendChild(el('div','mut','Rewards/rebates: '+f(cb.rewards_y_rebates)));
 p.appendChild(el('h2',null,'Serie diaria'));const sd=c.serie_diaria||[];p.appendChild(grafico(sd,'saldo_cierre_pusd','saldo de cierre (pUSD)'));p.appendChild(grafico(sd,'pnl_liquidado_acum','PnL liquidado acumulado (pUSD)'));
 p.appendChild(tabla([{t:'fecha',l:1,g:r=>r.fecha},{t:'saldo cierre',g:r=>f(r.saldo_cierre_pusd,4)},{t:'depositos acum.',g:r=>f(r.depositos_acum)},{t:'PnL liq. dia',g:r=>sg(r.pnl_liquidado_dia)},{t:'PnL liq. acum.',g:r=>sg(r.pnl_liquidado_acum)},{t:'mov.',g:r=>f(r.n_movimientos,0)}],sd.slice().reverse()));
 p.appendChild(el('h2',null,'Ultimos 50 movimientos'));
 p.appendChild(tabla([{t:'fecha UTC',l:1,g:r=>r.fecha_utc},{t:'tipo',l:1,g:r=>r.tipo},{t:'importe',g:r=>sg(r.importe_pusd,4)},{t:'saldo',g:r=>f(r.saldo_acumulado,4)},{t:'mercado',l:1,g:r=>r.mercado||''},{t:'exp',l:1,g:r=>r.experimento||''},{t:'tanda',g:r=>f(r.tanda_B,0)},{t:'tx',l:1,g:r=>(r.tx||'').slice(0,12)}],c.ultimos_movimientos||[]));
 p.appendChild(el('div','mut','Generado '+c.generado_utc+' | wallet '+c.wallet+' | schema '+c.schema_version))}
function rend2(D){const p=$('p2');p.textContent='';const b=D.b_real,L=b.ledger||{},cf=L.config||{},t=b.tanda_actual||{},s=b.saldo||{},sp=b.supervisor||{},ks=b.kill||{};
 if(ks.pendiente)p.appendChild(el('div','bad','KILL PENDIENTE: '+(ks.ficheros_kill.join(', ')||'kill en ledger')+'. El supervisor no relanza nada.'));
 const sc=sp.screens||{};
 p.appendChild(cards([['Tanda actual',t.tanda!==undefined?('#'+t.tanda+' de '+b.n_tandas):'n/d'],['Inicio tanda',t.inicio_utc||'n/d'],['PnL realizado tanda',t.pnl_realizado!==undefined?((t.pnl_realizado>=0?'+':'')+f(t.pnl_realizado)):'n/d',t.pnl_realizado>=0?'ok':'no'],
  ['Saldo on-chain',f(s.pusd_onchain,4)],['Suelo vigente',f(L.suelo,4)],['Margen saldo - suelo',(s.pusd_onchain!==undefined&&L.suelo!==null&&L.suelo!==undefined)?f(s.pusd_onchain-L.suelo,2):'n/d'],
  ['KILL',ks.pendiente?'PENDIENTE':'no',ks.pendiente?'no':'ok'],['Screen h47B (envio real)',f(sc.h47B),sc.h47B==='viva'?'ok':'no'],['Screen h47sup',f(sc.h47sup),sc.h47sup==='viva'?'ok':'no'],
  ['Supervisor: ult. linea hace',edad(sp.log_edad_s)],['Pausa / STOP',(sp.pausado?'PAUSADO':'sin pausa')+' / '+(sp.stop_file?'STOP':'sin STOP')],['Ultimo evento ledger',L.ultimo_evento_ts||'n/d']]));
 p.appendChild(el('h2',null,'Configuracion de la ejecucion actual (ultimo evento config)'));
 p.appendChild(el('pre',null,JSON.stringify(cf,null,1)));
 p.appendChild(el('h2',null,'Eventos desde el ultimo config'));p.appendChild(el('pre',null,JSON.stringify(L.eventos_desde_config||{})));
 p.appendChild(el('h2',null,'Rellenos recientes (gemelo_relleno / relleno_tardio)'));
 p.appendChild(tabla([{t:'ts',l:1,g:r=>r.ts},{t:'tipo',l:1,g:r=>r.tipo},{t:'acc.',g:r=>f(r.acc,2)},{t:'precio',g:r=>f(r.precio,3)},{t:'mercado',l:1,g:r=>r.slug||''}],L.rellenos_recientes_tanda_actual||[]));
 if(L.ultima_puja_fin)p.appendChild(el('pre',null,'ultima puja_fin: '+JSON.stringify(L.ultima_puja_fin)));
 if(L.ultimo_bloqueo_suelo)p.appendChild(el('pre',null,'ultimo bloqueo_suelo_saldo: '+JSON.stringify(L.ultimo_bloqueo_suelo)));
 p.appendChild(el('h2',null,'Supervisor (ultimas lineas de h47_tandas_supervisor.log)'));p.appendChild(el('pre',null,(sp.log_lineas||[]).join('\n')));
 p.appendChild(el('div','mut','Ledger: '+f(L.ledger_bytes,0)+' bytes, leido por TAIL inverso (tope '+f(L.tope_bytes,0)+' bytes, '+f(L.lineas_leidas,0)+' lineas), mtime '+L.ledger_mtime))}
function rend3(D){const p=$('p3');p.textContent='';const v=D.vigias;p.appendChild(el('div','mut',v.nota));
 p.appendChild(cards(Object.keys(v.screens).map(k=>['screen '+k,v.screens[k]===null?'n/d':v.screens[k],v.screens[k]==='viva'?'ok':'mut'])));
 p.appendChild(el('h2',null,'Vigias 5m barato y sombras'));
 p.appendChild(tabla([{t:'log',l:1,g:r=>r.log},{t:'que es',l:1,g:r=>r.desc},{t:'ultima salida',l:1,g:r=>r.existe?r.mtime:'NO EXISTE'},{t:'hace',g:r=>r.existe?edad(r.edad_s):'n/d'},{t:'bytes',g:r=>r.existe?f(r.bytes,0):''}],v.vigias));
 v.vigias.filter(r=>r.existe).forEach(r=>{p.appendChild(el('h2',null,r.log));p.appendChild(el('pre',null,r.ultimas.join('\n')))});
 p.appendChild(el('h2',null,'H59 (congelada, dry-run pendiente)'));p.appendChild(el('pre',null,v.h59_ficheros.length?v.h59_ficheros.join('\n'):'sin logs ni ficheros H59 en logs/ ni datalogs'))}
let ultimo=null;
async function cargar(){try{const r=await fetch('/api/datos');if(!r.ok)throw new Error(r.status);ultimo=await r.json();const g=ultimo.global,rf=g.refresco;
 $('hdr').textContent=g.ahora_utc+' | contabilidad hace '+edad(rf.edad_estado_s)+(rf.corriendo?' | actualizando...':'')+(rf.ventana_prohibida_auto?' | auto-refresco en pausa (06:00-09:15Z)':'')+(rf.ultimo_error?' | ultimo error: '+rf.ultimo_error.slice(0,80):'')+' | load '+g.load1.toFixed(1);
 rend1(ultimo);rend2(ultimo);rend3(ultimo)}catch(e){$('hdr').textContent='error cargando: '+e}}
document.querySelectorAll('.tab').forEach(t=>t.onclick=()=>{document.querySelectorAll('.tab').forEach(x=>x.classList.remove('on'));document.querySelectorAll('.pane').forEach(x=>x.classList.remove('on'));t.classList.add('on');$(t.dataset.p).classList.add('on')});
$('btn').onclick=async()=>{$('btn').disabled=true;try{const r=await fetch('/api/refrescar',{method:'POST'});$('hdr').textContent='refresco manual: '+(await r.text())}finally{setTimeout(()=>{$('btn').disabled=false;cargar()},1500)}};
cargar();setInterval(cargar,20000);
</script></body></html>"""


# ------------------------------------------------------------------ servidor
class Handler(BaseHTTPRequestHandler):
    def _autenticado(self):
        if not (DASH_USER and DASH_PASS):
            return True   # solo posible en loopback (main() fuerza 127.0.0.1 sin credenciales)
        header = self.headers.get("Authorization", "")
        if not header.startswith("Basic "):
            return False
        try:
            user, _, pw = base64.b64decode(header[6:]).decode("utf-8").partition(":")
        except Exception:  # noqa: BLE001
            return False
        return hmac.compare_digest(user.encode(), DASH_USER.encode()) and hmac.compare_digest(pw.encode(), DASH_PASS.encode())

    def _pedir_auth(self):
        self.send_response(401)
        self.send_header("WWW-Authenticate", 'Basic realm="5m barato"')
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Autenticacion requerida")

    def _enviar(self, codigo, tipo, cuerpo):
        self.send_response(codigo)
        self.send_header("Content-Type", tipo)
        self.send_header("Content-Length", str(len(cuerpo)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(cuerpo)

    def do_GET(self):
        if not self._autenticado():
            return self._pedir_auth()
        ruta = self.path.split("?")[0]
        if ruta in ("/", "/index.html"):
            self._enviar(200, "text/html; charset=utf-8", HTML.encode())
        elif ruta == "/api/datos":
            try:
                cuerpo = json.dumps(api_datos(), default=str).encode()
            except Exception as e:  # noqa: BLE001
                return self._enviar(500, "text/plain", f"error: {type(e).__name__}: {e}".encode())
            self._enviar(200, "application/json", cuerpo)
        else:
            self._enviar(404, "text/plain", b"no existe")

    def do_POST(self):
        if not self._autenticado():
            return self._pedir_auth()
        if self.path.split("?")[0] != "/api/refrescar":
            return self._enviar(404, "text/plain", b"no existe")
        with _ST_LOCK:
            desde = time.time() - _ST["manual_t"]
            if desde < MANUAL_MIN_S:
                return self._enviar(429, "text/plain", f"espera {int(MANUAL_MIN_S - desde)} s".encode())
            _ST["manual_t"] = time.time()
        # el boton ejecuta en un hilo aparte (la peticion no espera 30 s); respeta el flock y "nunca dos a la vez"
        threading.Thread(target=ejecutar_actualizar, args=("manual",), daemon=True).start()
        self._enviar(202, "text/plain", b"lanzado (si no hay otra en curso)")

    def log_message(self, fmt, *args):
        print(f"[{ahora_utc().strftime('%H:%M:%S')}] {fmt % args}", flush=True)


class ServidorHilos(ThreadingMixIn, HTTPServer):
    daemon_threads = True


def main():
    args = [a for a in sys.argv[1:]]
    host = "0.0.0.0"
    if "--host" in args:
        i = args.index("--host")
        host = args[i + 1]
        del args[i:i + 2]
    puerto = int(args[0]) if args else PORT_DEF
    if not (DASH_USER and DASH_PASS):
        if host not in ("127.0.0.1", "localhost", "::1"):
            print("[dash5m] sin DASHBOARD_USER/DASHBOARD_PASS: fuerzo escucha SOLO en 127.0.0.1 (fail-closed)", flush=True)
            host = "127.0.0.1"
        print("[dash5m] AVISO: sin credenciales, acceso sin autenticacion (solo loopback)", flush=True)
    threading.Thread(target=bucle_refresco, daemon=True).start()
    srv = ServidorHilos((host, puerto), Handler)
    print(f"dash5m arrancando en http://{host}:{puerto} (solo lectura)", flush=True)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
