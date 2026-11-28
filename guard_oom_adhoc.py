#!/usr/bin/env python3
"""guard_oom_adhoc.py -- que un análisis AD-HOC desbocado muera él, no los inocentes (28-Nov).

Incidente 27-Nov 10:52-11:38Z: 9 OOM-kills del kernel. Los causantes eran scripts ad-hoc de subagentes
(s.py, s2.py, diag14.py... sobre libro5_tx de un día entero) lanzados desde la sesión ssh de Claude sin
ulimit ni cron_pesado: 5-9 GB con oom_score_adj 0. El kernel mató PRIMERO a 5 jobs de pesados.slice
(adj 500: shadow_pnl_fiel, firehose_cache...) porque badness = rss + adj*(RAM+swap)/1000 y con ~28 GB
de RAM+swap el adj 500 suma ~14 GB: un job de cola de 1,5 GB "pesa" más que un ad-hoc de 9 GB.
guard_ram_fase0.py (cron */5, reinicia observadores) es demasiado lento y apunta al proceso equivocado.

Regla (cada 3 s, cron */1 con bucle de ~55 s):
  candidato = proceso python en /user.slice/ (sesiones ssh/Claude), SIN ningún SCREEN ancestro
              (las screens de producción cuelgan de SCREEN), oom_score_adj >= 0 y RSS >= 1.500 MB.
  1) se le sube oom_score_adj a 1000 -> el kernel lo elige antes que a cualquier otro.
  2) si además MemAvailable < 700 MB, se le manda SIGKILL al mayor (como haría el kernel, pero antes de que
     el sistema entre en thrashing y sin daños colaterales).
Nunca toca procesos con adj < 0 (dinero real, observadores), ni cron.service, ni pesados.slice.
Telegram una vez por proceso (clave pid+starttime) en data/live/guard_oom_adhoc_estado.json.
"""
import json
import os
import signal
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
ESTADO = REPO / "data" / "live" / "guard_oom_adhoc_estado.json"
RSS_MIN_MB = 1500
DISPONIBLE_KILL_MB = 700
PERIODO_S = 3
DURACION_S = 55


def _leer(p, f):
    try:
        return open(f"/proc/{p}/{f}").read()
    except OSError:
        return ""


def _stat(p):
    s = _leer(p, "stat")
    if not s:
        return None
    campos = s.rsplit(")", 1)[1].split()
    return int(campos[1]), campos[19]  # ppid, starttime


def _tiene_screen(p):
    a, n = p, 0
    while a > 1 and n < 64:
        st = _stat(a)
        if not st:
            return False
        a, n = st[0], n + 1
        if _leer(a, "comm").strip().lower().startswith("screen"):
            return True
    return False


def _disponible_mb():
    for ln in open("/proc/meminfo"):
        if ln.startswith("MemAvailable:"):
            return int(ln.split()[1]) / 1024
    return 0.0


def candidatos():
    out = []
    for p in os.listdir("/proc"):
        if not p.isdigit():
            continue
        if not _leer(p, "comm").startswith("python"):
            continue
        if "/user.slice/" not in _leer(p, "cgroup"):
            continue
        try:
            adj = int(_leer(p, "oom_score_adj").strip())
        except ValueError:
            continue
        if adj < 0:
            continue
        rss = 0
        for ln in _leer(p, "status").splitlines():
            if ln.startswith("VmRSS:"):
                rss = int(ln.split()[1]) // 1024
        if rss < RSS_MIN_MB or _tiene_screen(int(p)):
            continue
        st = _stat(p)
        if not st:
            continue
        cmd = _leer(p, "cmdline").replace("\0", " ").strip()[:200]
        out.append({"pid": int(p), "start": st[1], "rss": rss, "adj": adj, "cmd": cmd})
    return out


def _telegram(msg):
    try:
        sys.path.insert(0, str(REPO))
        from shadow_digest import enviar_telegram
        enviar_telegram(msg)
    except Exception as e:  # el aviso nunca debe tumbar el guardia
        print(f"[guard_oom_adhoc] telegram falló: {e}")


def main():
    try:
        est = json.loads(ESTADO.read_text())
    except (OSError, ValueError):
        est = {}
    vistos = est.get("avisados", {})
    fin = time.time() + DURACION_S
    cambiado = False
    while time.time() < fin:
        cs = candidatos()
        ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
        for c in cs:
            clave = f"{c['pid']}:{c['start']}"
            if c["adj"] < 1000:
                try:
                    Path(f"/proc/{c['pid']}/oom_score_adj").write_text("1000")
                    print(f"[guard_oom_adhoc] {ts} adj {c['adj']}->1000 pid={c['pid']} rss={c['rss']}MB {c['cmd']}")
                except OSError as e:
                    print(f"[guard_oom_adhoc] {ts} no pude subir adj pid={c['pid']}: {e}")
            if clave not in vistos:
                vistos[clave] = {"ts": ts, "rss_mb": c["rss"], "cmd": c["cmd"]}
                cambiado = True
                _telegram(f"🧯 GUARDIA OOM ad-hoc: proceso fuera de screen/cron con {c['rss']} MB → víctima preferente del "
                          f"kernel (oom_score_adj 1000)\n  pid {c['pid']}: {c['cmd'][:150]}\n  Análisis pesados: "
                          "scripts/cron_pesado.sh o ulimit -v.")
        disp = _disponible_mb()
        if cs and disp < DISPONIBLE_KILL_MB:
            c = max(cs, key=lambda x: x["rss"])
            try:
                os.kill(c["pid"], signal.SIGKILL)
                print(f"[guard_oom_adhoc] {ts} SIGKILL pid={c['pid']} rss={c['rss']}MB disp={disp:.0f}MB {c['cmd']}")
                vistos[f"{c['pid']}:{c['start']}"]["matado"] = ts
                cambiado = True
                _telegram(f"🚨 GUARDIA OOM ad-hoc: MATADO pid {c['pid']} ({c['rss']} MB) con RAM disponible "
                          f"{disp:.0f} MB < {DISPONIBLE_KILL_MB}\n  {c['cmd'][:150]}")
            except OSError as e:
                print(f"[guard_oom_adhoc] {ts} no pude matar pid={c['pid']}: {e}")
        time.sleep(PERIODO_S)
    if cambiado:
        # poda: solo los últimos 7 días
        lim = datetime.now(timezone.utc).timestamp() - 7 * 86400
        vistos = {k: v for k, v in vistos.items()
                  if datetime.fromisoformat(v["ts"]).timestamp() >= lim}
        ESTADO.write_text(json.dumps({"avisados": vistos}, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
