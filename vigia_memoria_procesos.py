#!/usr/bin/env python3
"""vigia_memoria_procesos.py -- (23-Sep) vigía de memoria por PROCESO (cron cada minuto).

Motivo: 8 OOM-kills en 24h y el kernel solo deja el PID y "python" (los procesos matados eran
tareas de corta vida, ya inexistentes al investigar). Causas encontradas y arregladas el 23-Sep
(resolvers que hacían list(csv.DictReader) de CSV de 70-230 MB, caché de 1,4 GB en
wallet_mirror_tracker) -- este vigía deja RASTRO del siguiente culpable, con su línea de comando.

Cada ejecución toma 4 muestras (cada 15s) de /proc: procesos con RSS+swap >= UMBRAL_MB -> una
línea por proceso en logs/vigia_memoria_procesos.log (solo si supera el umbral o cambia mucho).
Si MemAvailable+SwapFree < UMBRAL_LIBRE_MB -> aviso por Telegram con el top 5 (latch 1h).
Solo lectura, coste despreciable.
"""
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
LOG = REPO / "logs" / "vigia_memoria_procesos.log"
LATCH = REPO / "data" / "live" / "vigia_memoria_procesos_latch.json"
UMBRAL_MB = 800
UMBRAL_LIBRE_MB = 1500
MUESTRAS, CADA_S = 4, 15


def _meminfo() -> dict:
    d = {}
    for l in open("/proc/meminfo"):
        k, v = l.split(":", 1)
        d[k] = int(v.split()[0]) // 1024
    return d


def _procesos() -> list:
    out = []
    for p in os.listdir("/proc"):
        if not p.isdigit():
            continue
        try:
            st = {}
            for l in open(f"/proc/{p}/status"):
                if l.startswith(("VmRSS", "VmSwap", "VmHWM")):
                    k, v = l.split(":", 1)
                    st[k] = int(v.split()[0]) // 1024
            total = st.get("VmRSS", 0) + st.get("VmSwap", 0)
            if total < UMBRAL_MB:
                continue
            cmd = open(f"/proc/{p}/cmdline", "rb").read().replace(b"\0", b" ").decode(errors="replace")
            out.append((total, st.get("VmRSS", 0), st.get("VmSwap", 0), st.get("VmHWM", 0), int(p), cmd[:160]))
        except (OSError, ValueError):
            continue
    return sorted(out, reverse=True)


def main() -> int:
    LOG.parent.mkdir(exist_ok=True)
    for i in range(MUESTRAS):
        ahora = datetime.now(timezone.utc).isoformat(timespec="seconds")
        mi = _meminfo()
        libre = mi.get("MemAvailable", 0) + mi.get("SwapFree", 0)
        procs = _procesos()
        with open(LOG, "a", encoding="utf-8") as f:
            for tot, rss, swap, hwm, pid, cmd in procs:
                f.write(f"[{ahora}] {tot:5d} MB (rss {rss} swap {swap} pico {hwm}) pid {pid} | {cmd}\n")
            if libre < UMBRAL_LIBRE_MB:
                f.write(f"[{ahora}] ⚠️ memoria libre (RAM disp + swap libre) = {libre} MB\n")
        if libre < UMBRAL_LIBRE_MB:
            try:
                latch = json.loads(LATCH.read_text()) if LATCH.exists() else {}
            except Exception:
                latch = {}
            if time.time() - latch.get("ts", 0) > 3600:
                from shadow_digest import enviar_telegram
                top = "\n".join(f"{t} MB pid {p} {c[:80]}" for t, _, _, _, p, c in procs[:5])
                enviar_telegram(f"⚠️ Memoria baja: {libre} MB libres (RAM+swap). Top procesos:\n{top}")
                LATCH.write_text(json.dumps({"ts": time.time(), "libre_mb": libre}))
        if i < MUESTRAS - 1:
            time.sleep(CADA_S)
    return 0


if __name__ == "__main__":
    sys.exit(main())
