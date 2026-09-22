#!/usr/bin/env python3
"""vigia_perps_consenso.py -- envoltorio de perps_consenso_dryrun.py para el
planificador vigias_frecuentes_fase0.py (carril propio "perps", subproceso).

Corre generación de señales + resolución de las que ya cumplieron el
horizonte, en un único subproceso (nice 10) para aislar el escaneo de CSV
(crece con polymarket_perps_wallet_fills_*.csv / polymarket_perps_market_
*.csv, ambos sin límite de tamaño todavía) del resto de vigías.

MODO DRY-RUN puro -- ver docstring de perps_consenso_dryrun.py.

22-Sep (petición explícita Javi: "ponme un aviso en telegram cada vez que
haya una actualización de datos, así lo voy viendo"): tras cada corrida,
compara data/shadow/perps_consenso_stats.json contra el snapshot anterior
(latch) y avisa por Telegram (bot "cripto") si algo cambió -- fills nuevos,
wallets nuevas con posiciones, posiciones cerradas nuevas, wallets que
pasan a cualificar, o señales/resoluciones de consenso nuevas. Silencioso
si no hay ningún cambio real (no un ping cada 3h por rutina)."""
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
STATS = REPO / "data" / "shadow" / "perps_consenso_stats.json"
LATCH = REPO / "data" / "shadow" / "vigia_perps_consenso_latch.json"


def _texto_actualizacion(antes: dict, ahora: dict) -> str:
    lin = ["📡 Perps -- actualización de datos:"]
    campos = [
        ("n_fills", "fills"), ("n_wallets_con_posiciones", "wallets con posiciones"),
        ("n_posiciones_total", "posiciones totales"),
        ("n_posiciones_cerradas", "posiciones cerradas"),
        ("n_cualificadas", "wallets cualificadas para consenso"),
    ]
    for campo, etiqueta in campos:
        v0, v1 = antes.get(campo), ahora.get(campo)
        # /code-review 22-Sep: v1 puede faltar (esquema de STATS cambiado
        # entre versiones, escritura parcial) -- degradar sin crashear,
        # nunca perder la corrida entera por un campo nuevo/renombrado.
        if v0 is None or v1 is None:
            continue
        delta = v1 - v0
        if delta != 0:
            lin.append(f"  {etiqueta}: {v0} -> {v1} ({delta:+d})")
    n_sen = ahora.get("n_senales_nuevas", 0)
    if n_sen:
        lin.append(f"  🟢 {n_sen} señal(es) NUEVA(S) de consenso -- ver perps_consenso_dryrun.csv")
    if len(lin) == 1:
        return ""
    return "\n".join(lin)


def _avisar(ahora: dict) -> None:
    try:
        antes = json.loads(LATCH.read_text(encoding="utf-8")) if LATCH.exists() else None
    except Exception:
        antes = None
    if antes is not None:
        txt = _texto_actualizacion(antes, ahora)
        if txt:
            try:
                from shadow_digest import enviar_telegram
                enviar_telegram(txt, bot="cripto")
                print("telegram: actualización enviada")
            except Exception as e:
                print(f"aviso: no se pudo enviar Telegram: {type(e).__name__}: {e}")
    LATCH.write_text(json.dumps(ahora, ensure_ascii=False), encoding="utf-8")


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

    try:
        ahora = json.loads(STATS.read_text(encoding="utf-8")) if STATS.exists() else None
    except Exception:
        ahora = None
    if ahora is not None:
        _avisar(ahora)

    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
