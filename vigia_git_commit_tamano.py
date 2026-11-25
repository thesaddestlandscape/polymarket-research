#!/usr/bin/env python3
"""vigia_git_commit_tamano.py (25-Nov) -- avisa si los commits de la última hora meten ficheros grandes.

Motivo: hasta el 25-Nov ~58 CSV/JSON de datos >2 MB que crecen seguían trackeados y git_batch_sync los
commiteaba ~225 veces/día (150-300 MB de blobs por commit) => ~1 GB/h de packs en sdb sin que nada avisara.
Este vigía suma, por commit de la última hora, el tamaño de los blobs nuevos y avisa (Telegram, latch por
fichero, no por valor) de todo fichero >2 MB modificado. Arreglo: git rm --cached + .gitignore.
Solo lectura sobre git. Cron horario.
"""
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
LATCH = REPO / "data" / "live" / "vigia_git_commit_tamano_latch.json"
UMBRAL_FICHERO = 2_000_000
UMBRAL_COMMIT = 20_000_000


def git(*a):
    return subprocess.run(["git", *a], cwd=REPO, capture_output=True, text=True, timeout=120).stdout


def main() -> int:
    commits = git("log", "--since=1 hour ago", "--format=%h").split()
    grandes, max_commit = {}, (0, "")
    for c in commits:
        total = 0
        for linea in git("diff-tree", "-r", "--no-commit-id", c).splitlines():
            p = linea.split(maxsplit=5)
            if len(p) < 6 or p[4] == "D":
                continue
            sha, ruta = p[3], p[5]
            try:
                tam = int(git("cat-file", "-s", sha).strip() or 0)
            except ValueError:
                continue
            total += tam
            if tam > UMBRAL_FICHERO:
                grandes[ruta] = max(grandes.get(ruta, 0), tam)
        if total > max_commit[0]:
            max_commit = (total, c)
    print(f"[vigia_git_commit_tamano] {len(commits)} commits, máx {max_commit[0]/1e6:.1f} MB ({max_commit[1]}), "
          f"{len(grandes)} ficheros >2 MB")
    try:
        latch = set(json.loads(LATCH.read_text()))
    except Exception:
        latch = set()
    nuevos = sorted(set(grandes) - latch)
    if nuevos:
        lineas = [f"• {r} ({grandes[r]/1e6:.1f} MB)" for r in nuevos[:15]]
        texto = ("💽 vigia_git_commit_tamano: ficheros >2 MB commiteados en la última hora (crecen el .git en sdb). "
                 "Arreglo: git rm --cached + .gitignore.\n" + "\n".join(lineas))
        try:
            from shadow_digest import enviar_telegram
            enviar_telegram(texto)
        except Exception as e:
            print(f"ERROR Telegram: {e}", file=sys.stderr)
        LATCH.write_text(json.dumps(sorted(latch | set(nuevos))))
        print(texto)
    return 0


if __name__ == "__main__":
    sys.exit(main())
