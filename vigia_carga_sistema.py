#!/usr/bin/env python3
"""vigia_carga_sistema.py — Vigía frecuente (cron cada 15min) de carga de
CPU y atasco de git push.

Origen (05-Ago, decisión explícita Javi tras el incidente real: el push
del fast loop llevaba fallando desde las 02:35 UTC -- 4+ horas, ~1650
commits sin llegar a GitHub -- sin que nadie lo detectara hasta que se
intentó pushear a mano). `analisis_diario_salud_sistema.py` YA mide esto
(medir_carga_sistema/medir_git_push_lag, reutilizadas aquí sin duplicar),
pero corre una vez al día (07:08 UTC) -- un problema que tarda 4h en
notarse necesita un vigía de cadencia mucho más corta, no solo el barrido
diario. Cero llamadas de red -- todo se lee de /proc y de la ref local
origin/main (git no hace fetch).

Avisa por Telegram con latch simple: solo cuando pasa de sano a anómalo,
o cuando el push llevaba atascado y se recupera (para que se sepa que ya
volvió a la normalidad sin tener que ir a comprobarlo).

26-Ago (bug real cazado por Javi -- "soluciona también el mensaje de
telegram de las 13:49"): con `ratio5` oscilando justo alrededor de
UMBRAL_LOAD_RATIO (3.0x) durante una sesión con varios análisis pesados
en paralelo, el latch de un solo umbral hacía "flapping" -- cada cruce
del 3.0x en cualquier dirección (cron cada 15min) mandaba un Telegram
nuevo, varias veces en una hora. Arreglado con HISTÉRESIS: entra en
anomalía a ratio>UMBRAL_LOAD_RATIO_ALTO, pero solo se considera
recuperado por debajo de UMBRAL_LOAD_RATIO_BAJO (más bajo) -- la zona
intermedia no dispara ningún aviso nuevo en ninguna dirección.
"""
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from analisis_diario_salud_sistema import (
    medir_carga_sistema, medir_git_push_lag,
    UMBRAL_LOAD_RATIO, UMBRAL_PUSH_LAG_COMMITS,
)

LATCH = REPO / "data/live/vigia_carga_sistema_latch.json"

UMBRAL_LOAD_RATIO_ALTO = UMBRAL_LOAD_RATIO  # 3.0x -- entra en anomalía
UMBRAL_LOAD_RATIO_BAJO = 2.0  # sale de anomalía solo por debajo de esto


def main() -> int:
    from shadow_digest import enviar_telegram

    cs = medir_carga_sistema()
    gp = medir_git_push_lag()

    try:
        prev0 = json.loads(LATCH.read_text()) if LATCH.exists() else {}
    except Exception:
        prev0 = {}
    prev_anomalo0 = prev0.get("anomalo", False)

    ratio5 = cs.get("ratio5")
    if ratio5 is None:
        carga_mal = False
    elif prev_anomalo0:
        # ya estábamos en anomalía -- solo sale si cae por debajo del umbral bajo
        carga_mal = ratio5 > UMBRAL_LOAD_RATIO_BAJO
    else:
        # estábamos sanos -- solo entra si sube del umbral alto
        carga_mal = ratio5 > UMBRAL_LOAD_RATIO_ALTO
    push_mal = gp.get("commits_sin_pushear", 0) > UMBRAL_PUSH_LAG_COMMITS
    anomalo = carga_mal or push_mal
    prev_anomalo = prev_anomalo0

    print(f"[vigia_carga_sistema] load5={cs.get('load5')} nproc={cs.get('nproc')} "
          f"ratio5={cs.get('ratio5')} push_lag={gp.get('commits_sin_pushear')} "
          f"anomalo={anomalo} prev={prev_anomalo}")

    if anomalo != prev_anomalo:
        if anomalo:
            partes = []
            if carga_mal:
                partes.append(f"CPU sobresuscrita: load5={cs['load5']} en {cs['nproc']} "
                               f"cores (ratio={cs['ratio5']}x)")
            if push_mal:
                partes.append(f"git push atascado: {gp['commits_sin_pushear']} commits "
                               f"sin llegar a GitHub")
            msg = "🔥 VIGÍA carga sistema — ANOMALÍA:\n" + "\n".join(f"  {p}" for p in partes)
        else:
            msg = ("✅ VIGÍA carga sistema — recuperado "
                   f"(load5={cs.get('load5')} ratio5={cs.get('ratio5')} "
                   f"push_lag={gp.get('commits_sin_pushear')})")
        ok = enviar_telegram(msg)
        print(f"[vigia_carga_sistema] aviso enviado (telegram={ok})")

    LATCH.write_text(json.dumps({
        "anomalo": anomalo, "load5": cs.get("load5"), "ratio5": cs.get("ratio5"),
        "commits_sin_pushear": gp.get("commits_sin_pushear"),
    }, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"[vigia_carga_sistema] ERROR {type(e).__name__}: {e}")
        sys.exit(0)
