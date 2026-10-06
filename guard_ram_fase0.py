#!/usr/bin/env python3
"""guard_ram_fase0.py -- guardia de RAM (06-Oct, Javi: "no podemos asumir este riesgo").

Contexto: restart_ram_fase0.sh reinicia observadores/vigiasfreq a horas fijas (03:20, 10:20, 22:20 UTC) para que no
se reinicie en horario USA y no se corte el histórico ms. Un horario fijo no garantiza nada si la RAM se dispara entre
dos pasadas, y un OOM del kernel puede matar cualquier proceso (los de dinero real llevan choom -500, pero el resto
del pipeline no). Este guardia cierra ese hueco: si la memoria DISPONIBLE del sistema baja del umbral y observadores
(el mayor acumulador, ~0,9-1 GB a las 3 h) pesa lo suficiente para que reiniciarlo ayude, lo reinicia YA, a cualquier
hora, con el mismo mecanismo probado (verify_deploy.py --restart). Perder el histórico ms es mejor que un OOM.

- Umbral: MemAvailable < 900 MB y RSS de observadores > 700 MB.
- Enfriamiento de 45 min entre reinicios (estado en data/live/guard_ram_fase0_estado.json) para no entrar en bucle.
- Telegram en cada reinicio y si el reinicio falla. Solo lee /proc y ps; no toca ningún proceso de dinero real.
Cron */5 con el MISMO flock que restart_ram_fase0.sh (nunca dos reinicios a la vez).
"""
import json
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
ESTADO = REPO / "data" / "live" / "guard_ram_fase0_estado.json"
UMBRAL_DISPONIBLE_MB = 900
UMBRAL_RSS_OBS_MB = 700
ENFRIAMIENTO_S = 45 * 60


def meminfo_mb():
    d = {}
    for ln in open("/proc/meminfo"):
        k, v = ln.split(":", 1)
        d[k] = int(v.split()[0]) / 1024
    return d


def rss_observadores_mb():
    """RSS del python de observadores_fase0.py (no del SCREEN ni del bash que lo lanza)."""
    out = subprocess.run(["ps", "-eo", "pid,rss,args"], capture_output=True, text=True, timeout=20).stdout
    best = 0.0
    for ln in out.splitlines()[1:]:
        p = ln.split(None, 2)
        if len(p) == 3 and "python" in p[2].split()[0] and "observadores_fase0.py" in p[2]:
            best = max(best, int(p[1]) / 1024)
    return best


def main():
    ahora = time.time()
    mi = meminfo_mb()
    disp, swap_libre = mi.get("MemAvailable", 0), mi.get("SwapFree", 0)
    rss = rss_observadores_mb()
    try:
        est = json.loads(ESTADO.read_text())
    except (OSError, ValueError):
        est = {}
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[guard_ram] {ts} disponible={disp:.0f}MB swap_libre={swap_libre:.0f}MB observadores={rss:.0f}MB")
    if disp >= UMBRAL_DISPONIBLE_MB or rss <= UMBRAL_RSS_OBS_MB:
        return 0
    if ahora - est.get("ultimo_reinicio_epoch", 0) < ENFRIAMIENTO_S:
        print(f"[guard_ram] bajo umbral pero en enfriamiento (último reinicio {est.get('ultimo_reinicio')})")
        return 0
    sys.path.insert(0, str(REPO))
    from shadow_digest import enviar_telegram
    r = subprocess.run([str(REPO / ".venv" / "bin" / "python"), "verify_deploy.py", "--restart", "observadores"],
                       cwd=REPO, capture_output=True, text=True, timeout=240)
    ok = r.returncode == 0
    disp2 = meminfo_mb().get("MemAvailable", 0)
    print(r.stdout[-800:], r.stderr[-800:])
    est = {"ultimo_reinicio": ts, "ultimo_reinicio_epoch": ahora, "disponible_antes_mb": round(disp),
           "disponible_despues_mb": round(disp2), "rss_observadores_mb": round(rss), "ok": ok,
           "n_reinicios": est.get("n_reinicios", 0) + 1}
    ESTADO.write_text(json.dumps(est, indent=1))
    enviar_telegram(("🧯 GUARDIA RAM: observadores reiniciado fuera de horario" if ok else
                     "🚨 GUARDIA RAM: FALLÓ el reinicio de observadores") +
                    f"\n  RAM disponible {disp:.0f} MB → {disp2:.0f} MB (umbral {UMBRAL_DISPONIBLE_MB})"
                    f"\n  observadores {rss:.0f} MB, swap libre {swap_libre:.0f} MB"
                    "\n  Se pierde el histórico ms en memoria; mejor que un OOM.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
