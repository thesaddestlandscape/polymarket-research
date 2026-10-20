#!/usr/bin/env python3
"""h47_tandas_supervisor.py -- 20-Oct (Javi, autorizacion expresa: "mas tandas de 5 $, recoge el saldo ganado y reinvierte, sin parar").
Supervisa la screen h47B (H47 escalon B REAL, wallet dedicada, tope 5 $ por tanda). NO envia ordenes y NO resetea el suelo.
- B cae SIN kill pendiente -> relanza con el mismo comando (el suelo se recalcula = max(saldo-5, suelo previo): reinversion).
- B vivo y saldo >= suelo + 6 (ganancia asegurable) y sin pujas en 90 s -> lo reinicia: el suelo sube a saldo-5 (recoge ganancias).
- Tanda agotada (B parado con `parada`, o vivo pero sin poder postear 10 min por el suelo) -> cierra B si sigue vivo, ejecuta el modo propio de H47
  `--rotar-tanda` (Javi 20-Oct, opcion 2: auditado, solo con tanda agotada, saldo >= suelo duro 12 + presupuesto, max 12/dia, mismas
  precondiciones que el reseteo manual) y relanza B. Si H47 se niega, NO relanza y lo deja en el log.
- KILL pendiente o saldo < SALDO_DURO -> NO toca nada y lo deja escrito en el log.
Parar: crear /root/polymarket-research-datalogs/h47_tandas_supervisor.STOP o `screen -S h47sup -X quit`.
"""
import json
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

DEV = Path("/root/polymarket-research-dev")
DL = Path("/root/polymarket-research-datalogs")
LEDGER = DL / "experimento_h47_B_ledger.jsonl"
KILL = DL / "experimento_h47.KILL"
STOP = DL / "h47_tandas_supervisor.STOP"
LOG = DL / "h47_tandas_supervisor.log"
PY = "/root/polymarket-research/.venv/bin/python"
WALLET = "0x659a40FF9920fEBc5a66836213040924343d297F"
SALDO_DURO = 12.0          # preregistrado: por debajo no se relanza nada
GANANCIA_ASEGURAR = 6.0    # saldo >= suelo + 6 -> reiniciar para subir el suelo
CICLO_S = 120
sys.path.insert(0, str(DEV))


def log(msg):
    with open(LOG, "a") as f:
        f.write(f"{datetime.now(timezone.utc).isoformat(timespec='seconds')} {msg}\n")


def screen_viva():
    out = subprocess.run(["screen", "-ls"], capture_output=True, text=True).stdout
    return ".h47B\t" in out


def ledger_cola(n=400, sz_max=400_000):
    try:
        with open(LEDGER, "rb") as f:
            f.seek(0, 2)
            sz = f.tell()
            f.seek(max(0, sz - sz_max))
            lin = f.read().decode("utf-8", "replace").splitlines()[-n:]
    except OSError:
        return []
    ev = []
    for ln in lin:
        try:
            ev.append(json.loads(ln))
        except ValueError:
            pass
    return ev


def suelo_vigente(ev):
    s = None
    for e in ev:
        if e.get("tipo") in ("suelo_calculado", "suelo_fijado") and e.get("suelo") is not None:
            s = float(e["suelo"])
    return s


def kill_pendiente():
    if KILL.exists():
        return True
    pend = False
    for e in ledger_cola(5000, 4_000_000):
        if e.get("real") and e.get("tipo") == "kill":
            pend = True
        elif e.get("tipo") == "kill_rearmado":
            pend = False
    return pend


def segundos_desde_ultima_puja(ev):
    t = None
    for e in ev:
        if e.get("tipo") in ("puja_post", "intencion_post", "intencion_cancel"):
            try:
                t = datetime.fromisoformat(e["ts"]).timestamp()
            except (KeyError, ValueError):
                pass
    return None if t is None else time.time() - t


def parada_sin_reseteo(ev):
    """True si el ultimo fin_ejecucion de B trae `parada` (p. ej. saldo de arranque < suelo) y no hay un suelo_reiniciado posterior."""
    ult_fin = ult_reset = -1
    parada = None
    for i, e in enumerate(ev):
        if e.get("tipo") == "fin_ejecucion":
            ult_fin, parada = i, e.get("parada")
        elif e.get("tipo") == "suelo_reiniciado":
            ult_reset = i
    return bool(parada) and ult_fin > ult_reset


def tanda_agotada_inactiva(ev, ventana_s=600):
    """B vivo pero bloqueado por el suelo, decidido por ESTADO (el ledger emite UN bloqueo_suelo_saldo por transicion): el ultimo evento de
    puja/cancelacion es anterior al ultimo bloqueo_suelo_saldo y han pasado >= `ventana_s` s desde esa ultima actividad."""
    t_puja = t_bloq = None
    for e in ev:
        try:
            t = datetime.fromisoformat(e["ts"]).timestamp()
        except (KeyError, ValueError):
            continue
        if e.get("tipo") in ("puja_post", "intencion_post", "intencion_cancel"):
            t_puja = t
        elif e.get("tipo") == "bloqueo_suelo_saldo":
            t_bloq = t
    return t_bloq is not None and (t_puja is None or t_bloq >= t_puja) and time.time() - max(t_bloq, t_puja or 0) >= ventana_s


ROT_T = []            # instantes (epoch) de las rotaciones hechas por este proceso
PAUSA_HASTA = [0.0]
RACHA_S, PAUSA_S, MAX_ROT_SUP_DIA = 45 * 60, 3 * 3600, 6


def avisar(msg):
    """Aviso por Telegram (fail-open: si falla, queda en el log)."""
    log("AVISO " + msg)
    try:
        sys.path.insert(0, str(DEV.parent / "polymarket-research"))
        from shadow_digest import enviar_telegram
        enviar_telegram("🧊 h47sup: " + msg)
    except Exception as e:
        log(f"telegram fallo {type(e).__name__}: {str(e)[:100]}")


def rotar_y_relanzar():
    """Rotacion con el modo propio de H47 (`--rotar-tanda`: tanda agotada, saldo >= suelo duro + presupuesto, tope diario movil, cuadre,
    auditado). Frenos propios: max MAX_ROT_SUP_DIA al dia y, si las dos ultimas tandas se agotaron en < RACHA_S, pausa PAUSA_S (aviso)."""
    ahora = time.time()
    if ahora < PAUSA_HASTA[0]:
        return
    ROT_T[:] = [t for t in ROT_T if ahora - t < 86400]
    if len(ROT_T) >= MAX_ROT_SUP_DIA:
        avisar(f"tope propio de {MAX_ROT_SUP_DIA} rotaciones en 24 h: NO roto mas; revisar B")
        PAUSA_HASTA[0] = ahora + PAUSA_S
        return
    if len(ROT_T) >= 1 and ahora - ROT_T[-1] < RACHA_S:
        avisar(f"dos tandas agotadas seguidas en < {RACHA_S // 60} min: pausa de {PAUSA_S // 3600} h sin rotar (posible regimen adverso o fallo)")
        PAUSA_HASTA[0] = ahora + PAUSA_S
        return
    for _ in range(12):                         # B recien cerrado: esperar a que suelte la screen y los locks
        if not screen_viva():
            break
        time.sleep(5)
    else:
        log("h47B sigue viva: no roto")
        return
    cmd = [PY, str(DEV / "experimento_maker_h47.py"), "--escalon", "B", "--confirmo-dinero-real", "--rotar-tanda"]
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=str(DEV), timeout=180)
    ok = r.returncode == 0 and "tanda rotada" in r.stdout
    log(f"rotar-tanda {'OK' if ok else 'NO realizada'} (rc={r.returncode}): {(r.stdout + r.stderr)[-260:]!r}")
    if ok:
        ROT_T.append(time.time())
        s = saldo()
        avisar(f"tanda rotada: saldo {s if s is None else round(s, 2)} pUSD; relanzo B" + (f" (rotaciones 24h: {len(ROT_T)})"))
        if not kill_pendiente() and not screen_viva():
            lanzar()
    else:
        avisar("rotar-tanda NO realizada (guarda de H47: saldo bajo el suelo duro, tope diario, cuadre o precondicion); NO relanzo, revisar a mano: "
               + (r.stdout + r.stderr)[-160:])
        PAUSA_HASTA[0] = time.time() + 1800


def saldo():
    import experimento_pares_cola_15m as X
    return X.saldo_onchain(WALLET)


def lanzar():
    salida = DL / f"h47_real_B_{datetime.now(timezone.utc):%Y%m%d_%H%M}_sup.out"
    cmd = f"cd {DEV} && nice -n 10 {PY} experimento_maker_h47.py --escalon B --n 230 --confirmo-dinero-real >> {salida} 2>&1"
    subprocess.run(["screen", "-dmS", "h47B", "bash", "-c", cmd])
    log(f"lanzado h47B -> {salida.name}")


def main():
    log("supervisor arrancado (sin envio de ordenes, sin reseteos de suelo)")
    while not STOP.exists():
        try:
            if kill_pendiente():
                log("KILL pendiente: no se toca nada (investigar + --rearmar-kill)")
            else:
                s = saldo()
                ev = ledger_cola()
                suelo = suelo_vigente(ledger_cola(20000, 6_000_000))      # el suelo puede estar a miles de eventos del final
                if s is None or suelo is None:
                    log(f"saldo/suelo no legibles (saldo={s} suelo={suelo}): no se toca nada")
                elif s < SALDO_DURO:
                    log(f"saldo {s:.2f} < suelo duro {SALDO_DURO}: parado")
                elif not screen_viva():
                    if parada_sin_reseteo(ledger_cola(20000, 6_000_000)):
                        if not getattr(main, "_avisado", False):
                            log(f"h47B parado por 'parada' (tanda agotada, saldo {s:.2f}, suelo {suelo:.2f}): NO relanzo; hace falta --reiniciar-suelo (chief)")
                            main._avisado = True
                    else:
                        main._avisado = False
                        log(f"h47B caido sin kill (saldo {s:.2f}, suelo {suelo:.2f}): relanzo")
                        lanzar()
                elif s >= suelo + GANANCIA_ASEGURAR:
                    quieto = segundos_desde_ultima_puja(ev)
                    if quieto is not None and quieto >= 90:
                        log(f"ganancia asegurable: saldo {s:.2f} >= suelo {suelo:.2f}+{GANANCIA_ASEGURAR}: reinicio B para subir el suelo")
                        subprocess.run(["screen", "-S", "h47B", "-X", "quit"])
                        time.sleep(15)
                        if not kill_pendiente():
                            lanzar()
                        else:
                            log("kill al cerrar: no relanzo")
        except Exception as e:                       # nunca morir en silencio
            log(f"error {type(e).__name__}: {str(e)[:160]}")
        time.sleep(CICLO_S)
    log("STOP: supervisor parado")


if __name__ == "__main__":
    main()
