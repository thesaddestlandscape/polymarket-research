#!/usr/bin/env python3
"""vigia_tamano_ficheros_git.py — vigía diaria de tamaño de ficheros
TRACKEADOS en git (no todo data/, solo lo que de verdad se commitea).

Origen (05-Ago, incidente real): data/shadow/ballenas_timing_history.csv
creció de 102MB (30-Jul) a 238MB sin estar en .gitignore, mientras
data/markets/data/trades/data/wallets ya estaban excluidos por el MISMO
motivo ("Datos re-generables o demasiado grandes para GitHub >100MB").
GitHub rechaza (hard block) cualquier push con un blob >100MB -- eso dejó
el repo SIN backup remoto durante 6.2 días (último push exitoso: 30-Jul
03:14 UTC) sin que nadie lo notara hasta que el digest diario de Telegram
llevaba días reportando "0 predicciones/0 resoluciones" (síntoma
indirecto: GitHub Actions hace checkout de un main congelado). Resuelto
el mismo día con squash+force-push (ver project_push_roto_carga_cpu_
resuelto_05ago / memoria del incidente). Este vigía es la pieza que
faltaba: nadie vigilaba el tamaño de los ficheros trackeados hasta que
GitHub los rechazaba.

Umbrales (GitHub real): 50MB = warning (push sigue funcionando, pero es
la señal temprana), 100MB = hard block (push falla de verdad). Avisa por
Telegram con latch simple (una vez por fichero+umbral cruzado, para no
repetir el aviso cada día una vez ya se sabe).

Cero llamadas de red -- solo `git ls-files` + `os.path.getsize` sobre el
working tree. Solo lectura, no toca ningún fichero ni config.
"""
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

LATCH = REPO / "data/live/vigia_tamano_ficheros_git_latch.json"
UMBRAL_WARNING_MB = 50.0
UMBRAL_BLOQUEO_MB = 100.0


def _ficheros_trackeados() -> list[str]:
    out = subprocess.run(["git", "-C", str(REPO), "ls-files"],
                          capture_output=True, text=True, timeout=30).stdout
    return [l for l in out.splitlines() if l]


def main() -> int:
    from shadow_digest import enviar_telegram

    try:
        vistos = json.loads(LATCH.read_text()) if LATCH.exists() else {}
    except Exception:
        vistos = {}

    avisos = []
    tamanos = {}
    for rel in _ficheros_trackeados():
        p = REPO / rel
        if not p.exists() or not p.is_file():
            continue
        mb = p.stat().st_size / (1024 * 1024)
        if mb < UMBRAL_WARNING_MB:
            continue
        tamanos[rel] = round(mb, 1)
        nivel = "BLOQUEO" if mb >= UMBRAL_BLOQUEO_MB else "warning"
        clave = f"{rel}#{nivel}"
        if clave not in vistos:
            avisos.append((rel, mb, nivel))
        vistos[clave] = round(mb, 1)

    print(f"[vigia_tamano_ficheros_git] {len(tamanos)} ficheros trackeados >={UMBRAL_WARNING_MB}MB: {tamanos}")
    if avisos:
        detalle = "\n".join(
            f"  {'🚨' if nivel == 'BLOQUEO' else '⚠️'} {rel}: {mb:.1f}MB ({nivel})"
            for rel, mb, nivel in avisos
        )
        msg = (
            "📦 VIGÍA tamaño de ficheros git — nuevo umbral cruzado:\n"
            f"{detalle}\n"
            "BLOQUEO=100MB (GitHub rechaza el push, incidente real 05-Ago con "
            "ballenas_timing_history.csv, 6.2 días sin backup remoto). "
            "warning=50MB (aún funciona, es la señal temprana). "
            "Si es un fichero que solo acumula (dry_run/observacional), añadir "
            "a .gitignore + git rm --cached ANTES de que cruce 100MB."
        )
        ok = enviar_telegram(msg)
        print(f"[vigia_tamano_ficheros_git] aviso enviado (telegram={ok})")

    LATCH.write_text(json.dumps(vistos, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"[vigia_tamano_ficheros_git] ERROR {type(e).__name__}: {e}")
        sys.exit(0)
