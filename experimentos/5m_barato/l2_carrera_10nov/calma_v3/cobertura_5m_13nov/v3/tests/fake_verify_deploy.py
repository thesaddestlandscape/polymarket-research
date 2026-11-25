"""verify_deploy FALSO del sandbox del despliegue (se copia como sb/repo/verify_deploy.py). Simula el reinicio de `observadores`: escribe el `ps` falso
(sb/ps_out, lineas 'pid ppid args'), el log de observadores y un libro5_ms que crece (solo filas G/B, sin filas d). Hijos = procesos `sleep` reales (se matan al final).
Modo de la 1a llamada = FAKE_VD_MODE; de las siguientes (marcha atras) = FAKE_VD_MODE_RB (por defecto ok)."""
import json, os, pathlib, subprocess, sys, time

sb = pathlib.Path(os.environ["SB"])
# contrato con el real: `verify_deploy.py` (informe) y `verify_deploy.py "--restart" <screen>`
if len(sys.argv) == 1:       # informe (solo lectura) como el real: la linea de observadores es la que parsea el contrato de P0; el real acepta "--restart <screen>"
    print("\u2705 observadores FRESH  pid=900 arrancado 11-14 03:20 | disco: libro_estado_ws.py 11-13 21:16 (103 modulos vigilados)")
    sys.exit(1)
pantalla = sys.argv[-1]
calls = sb / "vd_calls.txt"
previas = [l for l in calls.read_text().splitlines() if l.split()[0] == pantalla] if calls.exists() else []
idx = len(previas)
modo = os.environ.get("FAKE_VD_MODE", "ok") if idx == 0 else os.environ.get("FAKE_VD_MODE_RB", "ok")
with open(calls, "a") as f:
    f.write(pantalla + " " + modo + "\n")
if pantalla != "observadores":
    sys.exit(0)
R = str(sb / "repo")
LOG = sb / "repo/logs/observadores_fase0.log"
PS = sb / "ps_out"
OBSP = 900 + idx


def hijo():
    p = subprocess.Popen(["sleep", "600"], start_new_session=True)
    with open(sb / "pids", "a") as f:
        f.write(str(p.pid) + "\n")
    return p.pid


def obs(p=OBSP):
    return "%d 1 %s\n" % (p, os.environ.get("FAKE_OBS_CMD", ".venv/bin/python observadores_fase0.py"))


def hj(pid, ppid=OBSP):
    return "%d %d python -u %s/libro_estado_ws.py --hijo\n" % (pid, ppid, R)


def log(txt):
    with open(LOG, "a") as f:
        f.write(txt)


def conectado(*pids):
    log("".join("[x] conectado [BTC#5min], %s tokens (lector en proceso separado, pid %d)\n" % (os.environ.get("FAKE_TOKENS", "4"), x) for x in pids))     # FAKE_TOKENS: universo del hijo nuevo (A)


def lanzado(*pids):
    log("".join("[x] lector hijo lanzado (pid %d)\n" % x for x in pids))


def bg(script):
    subprocess.Popen(["bash", "-c", script], start_new_session=True)


def en(delay, cmd):
    """cmd tras `delay` s SOLO si esta sigue siendo la ultima llamada a verify_deploy (una marcha atras posterior no debe ser pisada por un escritor viejo)."""
    bg("sleep %s; [ \"$(grep -c '^observadores' %s)\" -eq %d ] && { %s; }" % (delay, calls, idx + 1, cmd))


def escribe_libro5(a):    # solo filas G/B (mercado quieto, sin filas d)
    d = os.environ.get("FAKE_VD_FECHA") or time.strftime("%Y-%m-%d", time.gmtime())      # FAKE_VD_FECHA: el hijo escribe en el fichero de OTRO dia (cruce de 00:00Z)
    bg("f=%s/libro5/libro5_ms_%s_%d.csv.gz; for i in $(seq 1 600); do echo 'G,1,*,arranque,,,1,1' >> $f; echo 'B,1,tok,0.4:5,0.5:5,,1,2' >> $f; sleep 0.3; done" % (sb, d, a))


def fresco():
    return json.loads((sb / "dl/binance_registro_estado.json").read_text())


TB_AP = 'Traceback (most recent call last):\n  File "%s/libro_estado_ws.py", line 9, in main\nKeyboardInterrupt\n' % R
TB_REAL = 'Traceback (most recent call last):\n  File "%s/libro_estado_ws.py", line 1, in f\nValueError: boom\n' % R
TB_WS = 'Traceback (most recent call last):\n  File "/x/site-packages/websockets/legacy/protocol.py", line 3, in recv\nConnectionResetError: x\n'

if modo == "cuelga":
    time.sleep(4)
    modo = "ok"
if os.environ.get("FAKE_BORRA_IO") == "1" and idx == 0:       # universo_5m_io desaparece de main: el adelanto "apagaria" por falta de modulo
    (sb / "repo/universo_5m_io.py").unlink(missing_ok=True)
if os.environ.get("FAKE_VD_HORA") and os.environ.get("SANDBOX_HORA_FILE") and idx == 0:      # la hora (simulada) cambia al reiniciar: p. ej. entra una ventana prohibida
    pathlib.Path(os.environ["SANDBOX_HORA_FILE"]).write_text(os.environ["FAKE_VD_HORA"])
if os.environ.get("FAKE_VD_GAMMA") == "1" and idx == 0:
    d = sb / "dl/universo_5m"
    d.mkdir(parents=True, exist_ok=True)
    (d / "gamma_pausa.json").write_text("{}")
if modo == "nolog":
    PS.write_text(obs())
    sys.exit(0)
a = hijo()
if modo == "cero":
    conectado(a); lanzado(a); PS.write_text(obs())
    sys.exit(0)
conectado(a); lanzado(a)
ps = obs() + hj(a)
if modo == "ajeno":       # un hijo de OTRO padre (medicion/harness) con la ruta de main: no cuenta
    ps += "600 1 python medir_hijo_real.py x\n" + hj(997, 600)
elif modo in ("viejo_no_sale", "viejos_salen"):
    ps += hj(5555, 1)       # el viejo (capturado antes del reinicio) sigue vivo, huerfano
    if modo == "viejos_salen":
        en(1, "printf '%s' '" + (obs() + hj(a)) + "' > " + str(PS))
elif modo in ("dos", "transitorio"):
    b = hijo(); conectado(b); lanzado(b); ps += hj(b)
    if modo == "transitorio":
        en(1.2, "printf '%s' '" + (obs() + hj(a)) + "' > " + str(PS))
elif modo == "respawn":   # el hijo muere y otro lo sustituye (DURO: respawn)
    b = hijo()
    en(0.8, "printf '%s' '" + obs() + "' > " + str(PS))
    en(1.6, "echo '[x] conectado [BTC#5min], 4 tokens (lector en proceso separado, pid %d)' >> %s; echo '[x] lector hijo lanzado (pid %d)' >> %s; printf '%%s' '%s' > %s" % (b, LOG, b, LOG, obs() + hj(b), PS))
    escribe_libro5(b)
elif modo == "tb_apagado":
    log(TB_AP)
elif modo == "tb_apagado_y_real" or modo == "traceback":
    log(TB_AP + TB_REAL if modo == "tb_apagado_y_real" else TB_REAL)
elif modo in ("tb_websockets", "tb_websockets_mudo"):
    log(TB_WS)
elif modo in ("bn_pierde", "bn_vuelve"):
    est = sb / "dl/binance_registro_estado.json"; e = fresco(); fr = json.dumps(e); e["ts"] = 1000; est.write_text(json.dumps(e))
    if modo == "bn_vuelve":
        en(1, "printf '%s' '" + fr + "' > " + str(est))
elif modo.startswith("cap_"):
    # un capture_markets NUEVO aparece cuando P6 ya ha empezado (la linea "== P6" del log del despliegue), vive 3 s (sleeper real) y a +1 s hace lo del modo.
    # (crece?, texto que escribe en slow.log). FAKE_CAP_VIEJO=1: el proceso es un sleeper que YA vivia antes del despliegue (lo arranca el test: FAKE_CAP_PID) y se hace
    # visible en `ps` a mitad de su ciclo (no estaba en cap_pre); FAKE_SIN_INICIO=1: el ciclo no deja su cabecera '--- Ciclo slow N ---'.
    TB = 'Traceback (most recent call last):\n  File "%s/capture_markets.py", line 3, in una_captura\n%s\n'
    SL = "%s/repo/logs/slow.log" % sb
    imprime = lambda t: "printf '%%s\\n' '%s' >> %s" % (t, SL)
    modos = {"cap_ok": (True, ""), "cap_tb": (True, "printf '%s' '" + TB % (R, "ImportError: boom") + "' >> " + SL),
             "cap_trans": (True, "printf '%s' '" + TB % (R, "requests.exceptions.ConnectionError: x") + "' >> " + SL),
             "cap_sin_crecer": (False, ""), "cap_sin_crecer_1429": (False, imprime("precio 94290.5 en 1429 mercados, hora 10:42:9")),
             "cap_sin_crecer_429": (False, imprime("  [429] gamma: rafaga abortada")),
             # formato REAL de slow.log (14-Nov): el 429 de gamma sale como 'Error gamma slug=..: HTTPError: 429 Client Error', el error de codigo como 'ERROR polymarket: NameError'
             "cap_429_real": (False, imprime("  Error gamma slug=bitcoin offset=0: HTTPError: 429 Client Error: Too Many Requests for url: https://gamma-api.polymarket.com/events?tag_slug=bitcoin")),
             "cap_matado": (False, ""),          # SIGKILL/OOM: el proceso muere SIN '=== Fin ===' (ver `fin` abajo) y sin dejar nada en stderr
             "cap_nameerror_real": (True, imprime("  ERROR polymarket: NameError: name 'x' is not defined")),
             "cap_valueerror_real": (True, imprime("  ERROR polymarket: ValueError: boom")),
             "cap_runtimeerror_real": (True, imprime("  ERROR polymarket: RuntimeError: boom")),
             "cap_gamma_keyerror_sin_crecer": (False, imprime("  Error gamma slug=x offset=0: KeyError: 'id'")),
             "cap_gamma_keyerror_crece": (True, imprime("  Error gamma slug=x offset=0: KeyError: 'id'")),
             "cap_tb_palabra": (True, "printf '%s' '" + TB % (R, "Boom") + "' >> " + SL),                                                              # L1: clase de una sola palabra
             "cap_enospc": (True, "printf '%s' '" + TB % (R, "OSError: [Errno 28] No space left on device") + "' >> " + SL),          # B: disco lleno = entorno, no revierte un despliegue sano
             "cap_memoryerror": (True, "printf '%s' '" + TB % (R, "MemoryError") + "' >> " + SL),
             "cap_adelanto": (True, "mkdir -p %s/dl/universo_5m; echo x > %s/dl/universo_5m/adelanto_x.csv" % (sb, sb))}
    crece_, acc = modos[modo]
    crece = "mkdir -p %s/repo/data/markets; echo fila >> %s/repo/data/markets/$(date -u +%%F).csv" % (sb, sb) if crece_ else ""
    # FORMATO REAL: run_slow.sh:14 log() hace tee -a al mismo log que redirige el screen => cada cabecera y cada 'completado' salen DOS veces seguidas; tras el '=== Fin ===' de
    # capture_markets sigue capture_wallets con sus HTTPError de data-api y ValueError (que NO son del ciclo de capture_markets).
    inicio = "" if os.environ.get("FAKE_SIN_INICIO") == "1" else "echo '[t] --- Ciclo slow 7 ---' >> %s; echo '[t] --- Ciclo slow 7 ---' >> %s; " % (SL, SL)
    fin = ("printf '%%s\\n' '[t] === Fin ===' '[t] === Captura wallets ===' '  ERROR leaderboard VOL MONTH: HTTPError: 400 Client Error: Bad Request' "
           "'  Error en posiciones de 0xabc: ValueError' '[t] --- Ciclo slow 7 completado ---' '[t] --- Ciclo slow 7 completado ---' >> %s" % SL)
    if modo == "cap_matado":
        fin = "printf '%%s\\n' '[t] === Captura wallets ===' '  ERROR leaderboard VOL MONTH: HTTPError: 400 Client Error: Bad Request' '[t] --- Ciclo slow 7 completado ---' >> %s" % SL
    if os.environ.get("FAKE_CAP_VIEJO") == "1":
        pid = os.environ["FAKE_CAP_PID"]
        bg("for i in $(seq 1 600); do grep -qs '== P6' %s/dl/traspaso_deltas_ws/deploy_*.log && break; sleep 0.1; done; sleep 0.5; "
           "echo \"%s 1 /x/.venv/bin/python %s/capture_markets.py\" >> %s; %s sleep 1; %s %s"
           % (sb, pid, R, PS, inicio, "; ".join(x for x in (crece, acc) if x) + ";" if (crece or acc) else "", fin))
    else:
        bg("for i in $(seq 1 600); do grep -qs '== P6' %s/dl/traspaso_deltas_ws/deploy_*.log && break; sleep 0.1; done; sleep 0.5; setsid sleep 3 & p=$!; "
           "echo \"$p 1 /x/.venv/bin/python %s/capture_markets.py\" >> %s; %s sleep 1; %s %s"
           % (sb, R, PS, inicio, "; ".join(x for x in (crece, acc) if x) + ";" if (crece or acc) else "", fin))
ps += os.environ.get("FAKE_PS_EXTRA", "")       # lineas extra del ps falso (p. ej. un capture_markets en curso)
PS.write_text(ps)
if modo not in ("mudo", "tb_websockets_mudo", "respawn") and os.environ.get("HIJO_ESCRIBE", "1") == "1":
    escribe_libro5(a)
