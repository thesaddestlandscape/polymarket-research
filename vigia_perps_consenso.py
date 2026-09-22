#!/usr/bin/env python3
"""vigia_perps_consenso.py -- envoltorio de perps_consenso_dryrun.py para el
planificador vigias_frecuentes_fase0.py (carril propio "perps", subproceso).

Corre generación de señales + resolución de las que ya cumplieron el
horizonte, en un único subproceso (nice 10) para aislar el escaneo de CSV
(crece con polymarket_perps_wallet_fills_*.csv / polymarket_perps_market_
*.csv, ambos sin límite de tamaño todavía) del resto de vigías.

MODO DRY-RUN puro -- ver docstring de perps_consenso_dryrun.py."""
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent


def main() -> int:
    script = str(REPO / "perps_consenso_dryrun.py")
    ok = True
    for extra in ([], ["--resolver"]):
        r = subprocess.run(["nice", "-n", "10", sys.executable, script, *extra],
                           capture_output=True, text=True, timeout=600, cwd=str(REPO))
        print(r.stdout[-1000:])
        if r.returncode != 0:
            print(f"ERROR ejecutando perps_consenso_dryrun.py {extra} "
                  f"(rc={r.returncode}): {r.stderr[-1000:]}")
            ok = False
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
