#!/usr/bin/env python3
"""archivar_gz_volumen.py -- 13-Oct (Javi: opción (b) del disco, "dale a la b").
Mueve al VOLUMEN (/dev/sdb) los .gz diarios de más de DIAS días del disco raíz y deja en su sitio un symlink, para que
los lectores (glob + gzip.open) sigan funcionando igual. Cron diario 03:30 UTC, después de comprimir_data_historica.sh
(03:00), que comprime a 3 días y BORRA por retención.

Reglas (cada una cubre un riesgo visto al diseñarlo):
- Solo familias explícitas de FAMILIAS y solo ficheros con fecha en el NOMBRE anterior a hoy-DIAS (mismo criterio que
  comprimir_data_historica.sh).
- Nunca un fichero seguido por git ni uno no ignorado: el commit automático del loop subiría el symlink.
- maker_ms_*/onchain_fills_* NO entran: su retención es `find -mtime +4 -delete`, que mira el mtime del ENLACE.
- Copia con copy2 (conserva mtime) + comparación byte a byte antes de sustituir; sustitución atómica (os.replace de un
  symlink temporal) y el symlink hereda el mtime del original (predicciones_archivos.stat_logico y las cachés por
  fichero de resolve/postmortem siguen viendo la misma firma; stat() sigue el enlace de todos modos).
- Huérfanos: la retención de comprimir_data_historica.sh hace `rm` del symlink y el fichero real quedaría en el volumen
  para siempre; cada pasada borra del volumen lo que ya no tiene su symlink apuntándole.
- Guarda: no mueve nada si el volumen tiene menos de LIBRE_MIN_GB libres.
Uso: python3 archivar_gz_volumen.py [--dry-run] [--familia SUBCADENA]
"""
import argparse
import filecmp
import os
import re
import shutil
import subprocess
import sys
from datetime import date, timedelta
from pathlib import Path

VOL = Path("/mnt/HC_Volume_106538179")
DESTINO = VOL / "archivo_gz_raiz"
REPO = Path("/root/polymarket-research")
DATALOGS = Path("/root/polymarket-research-datalogs")
DIAS = 3
LIBRE_MIN_GB = 15.0
FAMILIAS = [                                   # (directorio, patrón)
    (REPO / "data/markets", "*.csv.gz"),
    (REPO / "data/wallets", "positions_*.csv.gz"),
    (REPO / "data/wallets", "leaderboard_*.csv.gz"),
    (REPO / "data/trades", "*.csv.gz"),
    (REPO / "data/shadow", "predictions_*.csv.gz"),
    (REPO / "data/shadow", "sports_spread_fase0_*.csv.gz"),
    (REPO / "data/sports", "activity_ws_*.csv.gz"),
    (REPO / "data/prices", "polybolt_*.csv.gz"),
    (DATALOGS, "polymarket_activity_*.csv.gz"),
    (DATALOGS, "libro_book_ws_*.csv.gz"),
    (DATALOGS, "libro_ambos_lados_*.csv.gz"),
]
_FECHA = re.compile(r"(\d{4}-\d{2}-\d{2})")


def _destino(f: Path) -> Path:
    return DESTINO / str(f).lstrip("/")


def _git_seguro(f: Path) -> bool:
    """True solo si el fichero está FUERA del repo, o dentro pero sin seguir por git e ignorado."""
    try:
        rel = f.relative_to(REPO)
    except ValueError:
        return True
    tracked = subprocess.run(["git", "-C", str(REPO), "ls-files", "--error-unmatch", str(rel)],
                             capture_output=True).returncode == 0
    ignorado = subprocess.run(["git", "-C", str(REPO), "check-ignore", "-q", str(rel)],
                              capture_output=True).returncode == 0
    return (not tracked) and ignorado


def candidatos(filtro=None):
    lim = (date.today() - timedelta(days=DIAS)).isoformat()
    for d, patron in FAMILIAS:
        if filtro and filtro not in str(d / patron):
            continue
        for f in sorted(d.glob(patron)):
            m = _FECHA.search(f.name)
            if f.is_symlink() or not f.is_file() or not m or m.group(1) >= lim:
                continue
            yield f


def archivar(f: Path, dry):
    if not _git_seguro(f):
        print(f"SKIP git: {f}")
        return 0
    dst = _destino(f)
    tam = f.stat().st_size
    if dry:
        print(f"[dry] {f} -> {dst} ({tam / 1e6:.0f} MB)")
        return tam
    dst.parent.mkdir(parents=True, exist_ok=True)
    tmp = dst.with_name(dst.name + ".tmp")
    shutil.copy2(f, tmp)
    if not filecmp.cmp(f, tmp, shallow=False):
        tmp.unlink()
        print(f"ERROR verificación, no se toca: {f}")
        return 0
    os.replace(tmp, dst)
    st = f.stat()
    link_tmp = f.with_name(f.name + ".lnk.tmp")
    if link_tmp.is_symlink() or link_tmp.exists():
        link_tmp.unlink()
    link_tmp.symlink_to(dst)
    os.utime(link_tmp, ns=(st.st_atime_ns, st.st_mtime_ns), follow_symlinks=False)
    os.replace(link_tmp, f)
    print(f"OK {f} -> {dst} ({tam / 1e6:.0f} MB)")
    return tam


def limpiar_huerfanos(dry):
    """Borra del volumen los ficheros cuyo symlink original ya no existe o ya no apunta a ellos (retención)."""
    n = 0
    if not DESTINO.exists():
        return 0
    for dst in DESTINO.rglob("*.gz"):
        orig = Path("/") / dst.relative_to(DESTINO)
        vivo = orig.is_symlink() and Path(os.readlink(orig)) == dst
        if not vivo:
            print(f"{'[dry] ' if dry else ''}huérfano borrado: {dst}")
            if not dry:
                dst.unlink()
            n += 1
    for tmp in DESTINO.rglob("*.tmp"):           # copias a medias de una pasada interrumpida
        if not dry:
            tmp.unlink()
    return n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--familia", help="subcadena de directorio/patrón para limitar la pasada")
    a = ap.parse_args()
    if not VOL.is_mount():
        print(f"ERROR: {VOL} no está montado; no se mueve nada")
        return 1
    huerf = limpiar_huerfanos(a.dry_run)
    movido = 0
    for f in candidatos(a.familia):
        if shutil.disk_usage(VOL).free / 1e9 - f.stat().st_size / 1e9 < LIBRE_MIN_GB:
            print(f"PARO: el volumen quedaría con menos de {LIBRE_MIN_GB} GB libres")
            break
        movido += archivar(f, a.dry_run)
    print(f"movido {movido / 1e9:.2f} GB, huérfanos {huerf}; raíz libre {shutil.disk_usage('/').free / 1e9:.1f} GB, "
          f"volumen libre {shutil.disk_usage(VOL).free / 1e9:.1f} GB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
