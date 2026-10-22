#!/usr/bin/env python3
"""h47_tandas_supervisor.py -- 20-Oct (Javi, autorizacion expresa: "mas tandas de 5 $, recoge el saldo ganado y reinvierte, sin parar").
Supervisa la screen h47B (H47 escalon B REAL, wallet dedicada, tope 5 $ por tanda). NO envia ordenes y NO resetea el suelo por su cuenta.
- B cae SIN kill pendiente -> relanza con el mismo comando (el suelo se recalcula = max(saldo-5, suelo previo): reinversion).
- B vivo y saldo >= suelo + 6 (ganancia asegurable), sin pujas en 90 s y SIN ordenes vivas -> lo cierra con SIGTERM (H47 cancela todo y
  deja fin_ejecucion) y lo relanza: el suelo sube a saldo-5.
- Tanda agotada (B parado con `parada`, o vivo pero sin poder postear 10 min por el suelo, y saldo-suelo < ROTACION_MARGEN_AGOTADA) -> cierra
  B (SIGTERM, espera a que termine y suelte el lock), ejecuta el modo propio de H47 `--rotar-tanda` y relanza B. Si H47 se niega, NO relanza.
- KILL pendiente (H47 o pares) o saldo < SALDO_DURO -> NO toca nada; avisa por Telegram (antirrebote).
- B termina limpio por el tope `--n` (fin_ejecucion sin parada con pujas >= n_max) -> aviso y NO relanza.
Frenos derivados del ledger (rotaciones 24 h, lanzamientos/hora), singleton por flock. Nunca SIGKILL, nunca `screen -X quit`.
Parar: crear /root/polymarket-research-datalogs/h47_tandas_supervisor.STOP o SIGTERM a este proceso.
"""
import fcntl
import json
import os
import re
import signal
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

DEV = Path("/root/polymarket-research-dev")
DL = Path("/root/polymarket-research-datalogs")
LEDGER = DL / "experimento_h47_B_ledger.jsonl"
KILL = DL / "experimento_h47.KILL"
KILL_PARES = DL / "experimento_pares_dedicada.KILL"
LOCK_H47 = DL / "experimento_h47.lock"
LOCK_SUP = DL / "h47_tandas_supervisor.lock"
ESTADO = DL / "h47_tandas_supervisor_estado.json"
STOP = DL / "h47_tandas_supervisor.STOP"
LOG = DL / "h47_tandas_supervisor.log"
PROC = Path("/proc")
PY = "/root/polymarket-research/.venv/bin/python"
WALLET = "0x659a40FF9920fEBc5a66836213040924343d297F"
SALDO_DURO = 12.0              # preregistrado: por debajo no se relanza nada
GANANCIA_ASEGURAR = 6.0        # saldo >= suelo + 6 -> reiniciar para subir el suelo
ROTACION_MARGEN_AGOTADA = 1.5  # = experimento_maker_h47.ROTACION_MARGEN_AGOTADA
PRESUPUESTO = 5.0              # = H47 PRESUPUESTO_UTIL (suelo tras un reinicio = saldo_base - presupuesto)
ROTACION_AUTOMATICA = False   # 22-Oct (Javi): el reseteo de suelo con dinero real lo hace la sesion principal, no este proceso
GRACIA_ARRANQUE_S = 600        # tras (re)arrancar B no se juzga "agotada" hasta pasados estos s
TERM_ESPERA_S = 900            # espera tras SIGTERM (H47 cancela, verifica y escribe fin_ejecucion); NO se escala a SIGKILL
MAX_LANZ_HORA = 4              # tope de lanzamientos de B por hora (ledger: eventos `config`)
CICLO_S = 120
RACHA_S, PAUSA_S, MAX_ROT_SUP_DIA = 45 * 60, 3 * 3600, 6
ILEGIBLE_AVISO_N, EXC_AVISO_N = 3, 3
sys.path.insert(0, str(DEV))

CONT = {"ilegible": 0, "exc": 0}
AVISOS_T = {}                  # antirrebote en memoria (clave -> epoch del ultimo aviso)
LANZ_T = []                    # lanzamientos de este proceso (epoch)


# ------------------------------------------------------------------ utilidades
def ahora():
    return time.time()


def dormir(s):
    time.sleep(s)


def log(msg):
    with open(LOG, "a") as f:
        f.write(f"{datetime.now(timezone.utc).isoformat(timespec='seconds')} {msg}\n")


def _enviar(texto):
    sys.path.insert(0, str(DEV.parent / "polymarket-research"))
    from shadow_digest import enviar_telegram
    return enviar_telegram(texto)


def avisar(msg, clave=None, cooldown_s=3600):
    """Aviso por Telegram, fail-open (si falla, queda en el log) y con antirrebote por `clave`."""
    t = ahora()
    k = clave or msg[:40]
    if t - AVISOS_T.get(k, -1e18) < cooldown_s:
        return False
    AVISOS_T[k] = t
    log("AVISO " + msg)
    try:
        _enviar("h47sup: " + msg)
    except Exception as e:                 # nunca romper el ciclo por Telegram
        log(f"telegram fallo {type(e).__name__}: {str(e)[:100]}")
    return True


def _ts(e):
    try:
        return datetime.fromisoformat(e["ts"]).timestamp()
    except (KeyError, ValueError, TypeError):
        return None


def cargar_estado():
    try:
        return json.loads(ESTADO.read_text())
    except (OSError, ValueError):
        return {}


def fijar_pausa(hasta):
    st = cargar_estado()
    st["pausa_hasta"] = hasta
    tmp = Path(str(ESTADO) + ".tmp")
    tmp.write_text(json.dumps(st))
    os.replace(tmp, ESTADO)


def pausado(t=None):
    try:
        return (t if t is not None else ahora()) < float(cargar_estado().get("pausa_hasta", 0))
    except (TypeError, ValueError):
        return False


# ------------------------------------------------------------------ procesos
def screen_viva():
    """True si hay una screen h47B NO muerta ('Dead' = sesion zombi que no cuenta)."""
    out = subprocess.run(["screen", "-ls"], capture_output=True, text=True).stdout
    return any(re.search(r"\.h47B\s", ln) and "Dead" not in ln for ln in out.splitlines())


def pid_b():
    """PID del proceso python de B real (argv exacto; excluye --rotar-tanda y este proceso). None si no hay."""
    for d in os.listdir(PROC):
        if not d.isdigit() or int(d) == os.getpid():
            continue
        try:
            argv = (PROC / d / "cmdline").read_bytes().decode("utf-8", "replace").split("\0")
        except OSError:
            continue
        if (argv and os.path.basename(argv[0]).startswith("python")
                and any(a.endswith("experimento_maker_h47.py") for a in argv)
                and "--confirmo-dinero-real" in argv and "--rotar-tanda" not in argv
                and "--escalon" in argv and argv[argv.index("--escalon") + 1:][:1] == ["B"]):
            return int(d)
    return None


def lock_h47_libre():
    try:
        fd = open(LOCK_H47, "a")
    except OSError:
        return False
    try:
        fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        return True
    except OSError:
        return False
    finally:
        fd.close()


def cerrar_b():
    """Cierre limpio de B: UN SIGTERM al proceso python (H47 lo trata como parada limpia: cancela, verifica, fin_ejecucion; atexit) y espera a
    que el proceso termine, la screen desaparezca y se suelte el lock. NUNCA `screen -X quit` (SIGHUP) ni SIGKILL ni 2a senal (la 2a corta).
    True solo si B quedo cerrado y libre."""
    pid = pid_b()
    if pid is not None:
        try:
            os.kill(pid, signal.SIGTERM)
        except ProcessLookupError:
            pass
        log(f"SIGTERM a B (pid {pid}); espero hasta {TERM_ESPERA_S} s")
    t0 = ahora()
    while True:
        if pid_b() is None and not screen_viva() and lock_h47_libre():
            return True
        if ahora() - t0 >= TERM_ESPERA_S:
            return False
        dormir(5)


# ------------------------------------------------------------------ ledger (lectura hacia atras por bloques)
def ledger_reverso(bloque=262144):
    """Eventos del ledger del FINAL hacia el principio, leyendo por bloques (sin ventana fija)."""
    try:
        f = open(LEDGER, "rb")
    except OSError:
        return
    with f:
        pos = f.seek(0, 2)
        resto = b""
        while pos > 0:
            n = min(bloque, pos)
            pos -= n
            f.seek(pos)
            datos = f.read(n) + resto
            lineas = datos.split(b"\n")
            resto = lineas[0] if pos > 0 else b""
            for ln in reversed(lineas[1:] if pos > 0 else lineas):
                if not ln.strip():
                    continue
                try:
                    e = json.loads(ln)
                except ValueError:
                    continue
                if isinstance(e, dict):
                    yield e


def suelo_vigente():
    """Como H47: maximo de los suelos (suelo_calculado/suelo_fijado/suelo_subido) desde el ULTIMO suelo_reiniciado; si tras el reinicio aun no hay
    ninguno, el que calculara B = saldo_base - presupuesto. None si no hay nada legible."""
    mx = None
    for e in ledger_reverso():
        t = e.get("tipo")
        if t in ("suelo_calculado", "suelo_fijado", "suelo_subido") and e.get("suelo") is not None:
            try:
                v = float(e["suelo"])
            except (TypeError, ValueError):
                continue
            mx = v if mx is None else max(mx, v)
        elif t == "suelo_reiniciado":
            if mx is not None:
                return mx
            try:
                return float(e["saldo_base"]) - PRESUPUESTO
            except (KeyError, TypeError, ValueError):
                return None
    return mx


def kill_pendiente():
    if KILL.exists() or KILL_PARES.exists():
        return True
    for e in ledger_reverso():
        if e.get("tipo") == "kill_rearmado":
            return False
        if e.get("real") and e.get("tipo") == "kill":
            return True
    return False


def ultimo_arranque():
    """Epoch del ultimo arranque de B (evento config / suelo_calculado). None si no hay."""
    for e in ledger_reverso():
        if e.get("tipo") in ("config", "suelo_calculado"):
            return _ts(e)
    return None


def segundos_desde_ultima_puja(t=None):
    for e in ledger_reverso():
        if e.get("tipo") in ("puja_post", "intencion_post", "intencion_cancel"):
            tt = _ts(e)
            if tt is not None:
                return (t if t is not None else ahora()) - tt
    return None


def ordenes_vivas():
    """oids con intencion_post (desde el ultimo arranque) sin post_rechazada ni fuera_libro (cancelada/casada/terminal)."""
    intent, cerr = {}, set()
    for e in ledger_reverso():
        tp = e.get("tipo")
        if tp in ("config", "suelo_calculado"):
            break
        if tp in ("intencion_post", "post_ok", "puja_post") and e.get("oid"):
            intent[e["oid"]] = 1
        elif tp in ("post_rechazada", "fuera_libro", "cancel_ya_terminal", "cancel_ya_terminal_ack") and e.get("oid"):
            cerr.add(e["oid"])
    return sorted(o for o in intent if o not in cerr)


def parada_sin_reseteo():
    """True si lo ultimo del ledger es un fin_ejecucion de B con `parada` (sin suelo_reiniciado ni nuevo arranque posteriores)."""
    for e in ledger_reverso():
        tp = e.get("tipo")
        if tp in ("suelo_reiniciado", "config", "suelo_calculado"):
            return False
        if tp == "fin_ejecucion":
            return bool(e.get("parada"))
    return False


def fin_por_tope():
    """True si el ultimo fin_ejecucion (posterior al ultimo arranque) cerro limpio por el tope --n: pujas >= n_max del config de esa ejecucion."""
    fin = None
    for e in ledger_reverso():
        tp = e.get("tipo")
        if fin is None:
            if tp in ("config", "suelo_calculado"):
                return False                       # B arrancado despues del ultimo fin: no es un fin por tope
            if tp == "fin_ejecucion":
                fin = e
        elif tp == "config":
            try:
                n_max = int(e.get("n_max"))
                pujas = int(fin.get("pujas"))
            except (TypeError, ValueError):
                return False
            return pujas >= n_max and not fin.get("kill")
    return False


def rotaciones_24h(t=None):
    """Instantes (epoch) de rotaciones automaticas (suelo_reiniciado origen rotar_tanda) en las ultimas 24 h, leidos del ledger."""
    t = t if t is not None else ahora()
    out = []
    for e in ledger_reverso():
        tt = _ts(e)
        if tt is not None and tt < t - 86400:
            break
        if e.get("tipo") == "suelo_reiniciado" and e.get("origen") == "rotar_tanda" and tt is not None:
            out.append(tt)
    return sorted(out)


def lanzamientos_hora(t=None):
    t = t if t is not None else ahora()
    n = 0
    for e in ledger_reverso():
        tt = _ts(e)
        if tt is not None and tt < t - 3600:
            break
        if e.get("tipo") == "config":
            n += 1
    return n + sum(1 for x in LANZ_T if t - x < 3600)   # los lanzamientos de este proceso aun sin config (B caido al arrancar)


def tanda_agotada_inactiva(t=None, ventana_s=600):
    """B vivo bloqueado por el suelo, por ESTADO: solo cuentan eventos POSTERIORES al ultimo arranque; el ultimo bloqueo_suelo_saldo es posterior a
    la ultima puja, y han pasado >= ventana_s desde esa actividad y >= GRACIA_ARRANQUE_S desde el arranque."""
    t = t if t is not None else ahora()
    t_puja = t_bloq = t_arr = None
    for e in ledger_reverso():
        tp = e.get("tipo")
        if tp in ("config", "suelo_calculado"):
            t_arr = _ts(e)
            break
        tt = _ts(e)
        if tt is None:
            continue
        # 22-Oct: intencion_cancel NO es actividad de puja: es la limpieza de la puja previa y llega ~0,3 s DESPUES del ultimo
        # bloqueo_suelo_saldo; contarla hacia t_puja hacia t_bloq < t_puja y la tanda agotada nunca se detectaba.
        if tp in ("puja_post", "intencion_post") and t_puja is None:
            t_puja = tt
        elif tp == "bloqueo_suelo_saldo" and t_bloq is None:
            t_bloq = tt
    if t_arr is None or t_bloq is None:
        return False
    if t - t_arr < GRACIA_ARRANQUE_S:
        return False
    return (t_puja is None or t_bloq >= t_puja) and t - max(t_bloq, t_puja or 0) >= ventana_s


# ------------------------------------------------------------------ acciones
def saldo():
    import experimento_pares_cola_15m as X
    return X.saldo_onchain(WALLET)


def lanzar():
    salida = DL / f"h47_real_B_{datetime.now(timezone.utc):%Y%m%d_%H%M}_sup.out"
    cmd = f"cd {DEV} && nice -n 10 {PY} experimento_maker_h47.py --escalon B --n 500 --confirmo-dinero-real >> {salida} 2>&1"
    subprocess.run(["screen", "-dmS", "h47B", "bash", "-c", cmd])
    LANZ_T.append(ahora())
    log(f"lanzado h47B -> {salida.name}")


def lanzar_seguro():
    """Lanza B salvo kill pendiente, pausa, fin por tope o tope de lanzamientos por hora. True si lanzo."""
    if kill_pendiente():
        log("kill pendiente: no lanzo")
        return False
    if pausado():
        log("pausa activa: no lanzo")
        return False
    if fin_por_tope():
        return False
    if lanzamientos_hora() >= MAX_LANZ_HORA:
        avisar(f"{MAX_LANZ_HORA} lanzamientos de B en 1 h: NO relanzo mas (posible bucle); pausa 1 h", "lanz_tope", 1800)
        fijar_pausa(ahora() + 3600)
        return False
    lanzar()
    return True


def rotar_y_relanzar():
    """Rotacion con el modo propio de H47. Frenos derivados del ledger: max MAX_ROT_SUP_DIA al dia y, si la ultima rotacion fue hace < RACHA_S,
    pausa PAUSA_S (aviso). B ya debe estar cerrado."""
    t = ahora()
    if pausado(t):
        return
    rots = rotaciones_24h(t)
    if len(rots) >= MAX_ROT_SUP_DIA:
        avisar(f"tope propio de {MAX_ROT_SUP_DIA} rotaciones en 24 h: NO roto mas; revisar B", "rot_tope", 1800)
        fijar_pausa(t + PAUSA_S)
        return
    if rots and t - rots[-1] < RACHA_S:
        avisar(f"dos tandas agotadas seguidas en < {RACHA_S // 60} min: pausa de {PAUSA_S // 3600} h sin rotar (posible regimen adverso o fallo)",
               "rot_racha", 1800)
        fijar_pausa(t + PAUSA_S)
        return
    for _ in range(12):                         # B recien cerrado: esperar a que suelte la screen y los locks
        if not screen_viva():
            break
        dormir(5)
    else:
        log("h47B sigue viva: no roto")
        return
    cmd = [PY, str(DEV / "experimento_maker_h47.py"), "--escalon", "B", "--confirmo-dinero-real", "--rotar-tanda"]
    t_cmd = ahora()
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, cwd=str(DEV), timeout=180)
        ok = r.returncode == 0 and "tanda rotada" in r.stdout
        log(f"rotar-tanda {'OK' if ok else 'NO realizada'} (rc={r.returncode}): {(r.stdout + r.stderr)[-260:]!r}")
        cola = (r.stdout + r.stderr)[-160:]
    except subprocess.TimeoutExpired:
        ok = any(x >= t_cmd - 5 for x in rotaciones_24h(ahora()))      # el ledger manda: si H47 llego a escribir el suelo_reiniciado, cuenta
        cola = "timeout"
        log(f"rotar-tanda TIMEOUT: ledger {'MUESTRA' if ok else 'no muestra'} la rotacion")
    if ok:
        s = saldo()
        avisar(f"tanda rotada: saldo {s if s is None else round(s, 2)} pUSD; relanzo B (rotaciones 24h: {len(rotaciones_24h(ahora()))})",
               "rotada", 0)
        lanzar_seguro()
    else:
        avisar("rotar-tanda NO realizada (guarda de H47: saldo bajo el suelo duro, tope diario, cuadre o precondicion); NO relanzo, revisar a mano: "
               + cola, "rot_no", 900)
        fijar_pausa(ahora() + 1800)


# ------------------------------------------------------------------ ciclo
def ciclo():
    """Un ciclo de supervision. Devuelve una etiqueta de la accion (para tests/log)."""
    if kill_pendiente():
        avisar("KILL pendiente (H47 o pares): NO toco nada; investigar y --rearmar-kill", "kill", 3600)
        log("KILL pendiente: no se toca nada")
        return "kill"
    s = saldo()
    suelo = suelo_vigente()
    if s is None or suelo is None:
        CONT["ilegible"] += 1
        log(f"saldo/suelo no legibles (saldo={s} suelo={suelo}) x{CONT['ilegible']}: no se toca nada")
        if CONT["ilegible"] >= ILEGIBLE_AVISO_N:
            avisar(f"saldo/suelo ilegibles {CONT['ilegible']} ciclos seguidos (saldo={s} suelo={suelo}): no se toca nada", "ilegible", 3600)
        return "ilegible"
    CONT["ilegible"] = 0
    if s < SALDO_DURO:
        avisar(f"saldo {s:.2f} < suelo duro {SALDO_DURO}: parado, no relanzo ni roto", "saldo_duro", 3600)
        log(f"saldo {s:.2f} < suelo duro {SALDO_DURO}: parado")
        return "saldo_duro"
    viva = screen_viva()
    if not viva:
        if fin_por_tope():
            avisar("B termino limpio por el tope --n (500): NO relanzo; decidir con Javi (nuevo tope o cierre)", "tope", 6 * 3600)
            log("fin por tope --n: no relanzo")
            return "tope"
        if pausado():
            log("pausa activa: B caido, no actuo")
            return "pausa"
        if parada_sin_reseteo():
            if not ROTACION_AUTOMATICA:
                avisar(f"h47B parado por 'parada' (tanda agotada, saldo {s:.2f}, suelo {suelo:.2f}): NO roto; hace falta --reiniciar-suelo (chief)", "agotada_manual", 1800)
                log("tanda agotada: rotacion automatica desactivada, NO relanzo")
                return "agotada_sin_rotar"
            log(f"h47B parado por 'parada' (tanda agotada, saldo {s:.2f}, suelo {suelo:.2f}): rotar tanda")
            rotar_y_relanzar()
            return "rotar"
        log(f"h47B caido sin kill (saldo {s:.2f}, suelo {suelo:.2f}): relanzo")
        if lanzar_seguro():
            avisar(f"B caido sin kill ni parada; relanzado (saldo {s:.2f}, suelo {suelo:.2f})", "caida", 600)
            return "relanzo"
        return "relanzo_frenado"
    if tanda_agotada_inactiva():
        if pausado():
            log("pausa activa: tanda agotada pero no actuo")
            return "pausa"
        if s - suelo >= ROTACION_MARGEN_AGOTADA:
            log(f"bloqueo viejo pero saldo-suelo {s - suelo:.2f} >= margen {ROTACION_MARGEN_AGOTADA}: no cierro")
            return "no_agotada"
        if not ROTACION_AUTOMATICA:
            avisar(f"B vivo pero tanda agotada (saldo {s:.2f}, suelo {suelo:.2f}): NO cierro ni roto; hace falta --reiniciar-suelo (chief)", "agotada_manual", 1800)
            return "agotada_sin_rotar"
        vivas = ordenes_vivas()
        if vivas:
            avisar(f"tanda agotada pero B con {len(vivas)} orden(es) viva(s) en el ledger: no cierro", "vivas", 1800)
            return "vivas"
        log(f"h47B vivo pero sin poder postear (saldo {s:.2f}, suelo {suelo:.2f}): cierro (SIGTERM) y roto la tanda")
        if not cerrar_b():
            avisar("B no cerro tras SIGTERM en el plazo: NO roto ni relanzo, revisar a mano", "cierre_fallo", 1800)
            fijar_pausa(ahora() + 1800)
            return "cierre_fallo"
        rotar_y_relanzar()
        return "rotar"
    if s >= suelo + GANANCIA_ASEGURAR:
        quieto = segundos_desde_ultima_puja()
        if quieto is not None and quieto >= 90:
            if pausado():
                log("pausa activa: ganancia asegurable pero no actuo")
                return "pausa"
            if ordenes_vivas():
                log("ganancia asegurable pero hay ordenes vivas en el ledger: espero")
                return "vivas"
            log(f"ganancia asegurable: saldo {s:.2f} >= suelo {suelo:.2f}+{GANANCIA_ASEGURAR}: cierro (SIGTERM) y reinicio B para subir el suelo")
            if not cerrar_b():
                avisar("B no cerro tras SIGTERM en el plazo (ganancia asegurable): no relanzo", "cierre_fallo", 1800)
                fijar_pausa(ahora() + 1800)
                return "cierre_fallo"
            lanzar_seguro()
            return "reinicio_ganancia"
    return "ok"


def tomar_lock(path=None):
    """Singleton: flock exclusivo no bloqueante. Devuelve el fd (mantenerlo vivo) o None si ya hay otro vigilante."""
    fd = open(path or LOCK_SUP, "a")
    try:
        fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        fd.close()
        return None
    return fd


def main():
    fd = tomar_lock()
    if fd is None:
        log("otro vigilante ya tiene el lock: salgo")
        sys.exit("otro h47_tandas_supervisor esta activo (lock)")
    log("supervisor arrancado (sin envio de ordenes; frenos derivados del ledger)")
    while not STOP.exists():
        try:
            ciclo()
            CONT["exc"] = 0
        except Exception as e:                       # nunca morir en silencio
            CONT["exc"] += 1
            log(f"error {type(e).__name__}: {str(e)[:160]} x{CONT['exc']}")
            if CONT["exc"] >= EXC_AVISO_N:
                avisar(f"{CONT['exc']} excepciones seguidas: {type(e).__name__}: {str(e)[:100]}", "exc", 3600)
        dormir(CICLO_S)
    log("STOP: supervisor parado")


if __name__ == "__main__":
    main()
