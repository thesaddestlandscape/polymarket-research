"""csv_rotado.py — rotación sin pérdida de CSV append-only que se leen enteros.

05-Oct (disco al 91 %): data/shadow/dispersed_bot_executor_dryrun.csv pesaba
1,2 GB (5,97 M filas desde el 25-Ago, ~30 MB/día) y sus lectores diarios
(analisis_bot_wallets_gate_bucket_25ago.py, vigia_dispersed_bot_progreso_diario.py)
necesitan TODO el histórico. Cada rotación mueve el fichero vivo a una parte
.csv.gz fuera de git y el escritor (que abre en modo "a" en cada escritura y
pone cabecera si el fichero no existe) crea uno nuevo solo. Los lectores usan
abrir(): partes en orden + fichero vivo con UNA sola cabecera, es decir, las
mismas líneas en el mismo orden que el fichero único de antes.

Uso: python3 csv_rotado.py rotar <ruta.csv>   (cron diario, comprimir_data_historica.sh)
"""
import gzip
import hashlib
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

DIR_PARTES = Path("/root/polymarket-research-datalogs/csv_rotados")
ESPERA_ESCRITOR_S = 10  # un escritor con el fd ya abierto termina su escritura en ms


def _dir_partes(path: Path) -> Path:
    return DIR_PARTES / Path(path).stem


def _fuentes(path: Path) -> list:
    """Partes .csv.gz (orden = orden de rotación) + rotación a medias + fichero vivo."""
    path = Path(path)
    d = _dir_partes(path)
    partes = sorted(d.glob(f"{path.stem}_*.csv.gz")) if d.exists() else []
    con_parte = {p.name[len(path.stem) + 1:-len(".csv.gz")] for p in partes}
    rotando = [r for r in (sorted(d.glob(f"{path.stem}_*.csv.rotando")) if d.exists() else [])
               if r.name[len(path.stem) + 1:-len(".csv.rotando")] not in con_parte]
    vivo = [path] if path.exists() else []
    return partes + rotando + vivo


class _Lector:
    def __init__(self, fuentes, errors="strict"):
        self._errors = errors
        self._fuentes = fuentes
        self._f = None
        self._gen = self._lineas()

    def _abrir(self, p: Path):
        if p.name.endswith(".gz"):
            return gzip.open(p, "rt", encoding="utf-8", errors=self._errors, newline="")
        return open(p, encoding="utf-8", errors=self._errors, newline="")

    def _lineas(self):
        cabecera = None
        for p in self._fuentes:
            self._f = self._abrir(p)
            try:
                primera = self._f.readline()
                if cabecera is None:
                    cabecera = primera
                    yield primera
                elif primera and primera != cabecera:
                    yield primera  # fichero creado sin cabecera (carrera con el escritor)
                yield from self._f
            finally:
                self._f.close()
                self._f = None

    def readline(self):
        return next(self._gen, "")

    def __iter__(self):
        return self._gen

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self._gen.close()
        return False


def abrir(path, errors="strict"):
    """Como open(path, encoding="utf-8") para leer: readline(), iterable, context manager."""
    return _Lector(_fuentes(Path(path)), errors)


def _sha_texto(p: Path, comprimido: bool) -> str:
    h = hashlib.sha256()
    with (gzip.open(p, "rb") if comprimido else open(p, "rb")) as f:
        for bloque in iter(lambda: f.read(1 << 20), b""):
            h.update(bloque)
    return h.hexdigest()


def _comprimir_rotando(rot: Path, stem: str) -> None:
    ts = rot.name[len(stem) + 1:-len(".csv.rotando")]
    final = rot.with_name(f"{stem}_{ts}.csv.gz")
    tmp = final.with_name(final.name + ".tmp")
    with open(rot, "rb") as fi, gzip.open(tmp, "wb", compresslevel=6) as fo:
        for bloque in iter(lambda: fi.read(1 << 20), b""):
            fo.write(bloque)
    if _sha_texto(tmp, True) != _sha_texto(rot, False):
        tmp.unlink(missing_ok=True)
        raise RuntimeError(f"verificación fallida, se conserva {rot}")
    os.replace(tmp, final)
    rot.unlink()
    print(f"OK: {rot.name} -> {final}")


def rotar(path) -> None:
    path = Path(path).resolve()
    d = _dir_partes(path)
    d.mkdir(parents=True, exist_ok=True)
    # una rotación anterior que murió a medias se termina primero
    for rot in sorted(d.glob(f"{path.stem}_*.csv.rotando")):
        _comprimir_rotando(rot, path.stem)
    if not path.exists() or path.stat().st_size == 0:
        print(f"SKIP (no existe o vacío): {path}")
        return
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    rot = d / f"{path.stem}_{ts}.csv.rotando"
    os.rename(path, rot)  # mismo filesystem: atómico; nunca pasa por data/ (auto-commit)
    time.sleep(ESPERA_ESCRITOR_S)
    _comprimir_rotando(rot, path.stem)


def rotar_antiguas(path, lock=None, dias=3, dias_muertas=10) -> int:
    """Rotación POR ANTIGÜEDAD (02-Nov) para CSV cuyo resolvedor REESCRIBE filas (acierto vacío -> 0/1): rotar() entero
    dejaría filas pendientes huérfanas. Mueve a una parte .csv.gz el PREFIJO contiguo de filas con timestamp_utc (1ª
    columna, ISO con 'T') < ahora-`dias` y ya resueltas (o más viejas que `dias_muertas`, que se cuentan y avisan); el resto
    queda vivo. partes + vivo (abrir()) = las MISMAS líneas en el MISMO orden. TODO bajo el flock de los escritores `lock`
    (la rotación diaria mueve ~1 día: segundos), así el offset no puede quedar obsoleto. Temporales en el dir de partes
    (fuera de data/ y del auto-commit). Devuelve filas movidas."""
    import csv as _csv
    import fcntl
    from datetime import timedelta
    path = Path(path).resolve()
    if not path.exists():
        return 0
    d = _dir_partes(path); d.mkdir(parents=True, exist_ok=True)
    for huer in list(d.glob("*.tmp")) + list(d.glob("*.live")):   # temporales huérfanos de una ejecución muerta
        huer.unlink(missing_ok=True)
    ahora = datetime.now(timezone.utc)
    corte = (ahora - timedelta(days=dias)).strftime("%Y-%m-%dT%H:%M:%S").encode()
    corte_muerta = (ahora - timedelta(days=dias_muertas)).strftime("%Y-%m-%dT%H:%M:%S").encode()

    def _ts(l):
        t = l.split(b",", 1)[0].strip(b'"')
        return t if t[:2] == b"20" and len(t) >= 19 and t[4:5] == b"-" else None

    lk = open(lock, "a") if lock else None
    try:
        if lk:
            fcntl.flock(lk, fcntl.LOCK_EX)
        with open(path, "rb") as f:
            cab = f.readline()
            idx = next((i for i, c in enumerate(next(_csv.reader([cab.decode("utf-8", "replace")]))) if c == "acierto"), None)
            fin = f.tell(); n = muertas = 0
            while True:
                l = f.readline()
                if not l:
                    fin = f.tell(); break
                t = _ts(l)
                if t is None:            # fila corrupta/NUL: viaja con las viejas mientras el prefijo siga
                    n += 1; fin = f.tell(); continue
                if t >= corte:
                    break
                resuelta = True
                if idx is not None:
                    try:
                        resuelta = next(_csv.reader([l.decode("utf-8", "replace")]))[idx] in ("0", "1")
                    except Exception:
                        resuelta = False
                if not resuelta:
                    if t >= corte_muerta:
                        break
                    muertas += 1
                n += 1; fin = f.tell()
        if n == 0:
            print(f"SKIP {path.name}: nada que rotar"); return 0
        final = d / f"{path.stem}_{ahora.strftime('%Y%m%dT%H%M%SZ')}.csv.gz"
        tmp_p = final.with_name(final.name + ".tmp"); tmp_v = d / f"{path.stem}.{os.getpid()}.live"
        with open(path, "rb") as f, gzip.open(tmp_p, "wb", compresslevel=6) as gp, open(tmp_v, "wb") as gv:
            f.readline(); gp.write(cab); gv.write(cab)
            resto = fin - f.tell()
            while resto > 0:
                b = f.read(min(1 << 20, resto)); gp.write(b); resto -= len(b)
            while True:
                b = f.read(1 << 20)
                if not b: break
                gv.write(b)
            leidos = f.tell()
            gv.flush(); os.fsync(gv.fileno())
        with gzip.open(tmp_p, "rb") as gp:
            n_p = sum(1 for _ in gp)
        with open(path, "rb") as f:
            f.seek(fin - 1); ok_fin = f.read(1) == b"\n"
        # delta: cualquier escritor SIN lock que añadiera durante la copia
        with open(path, "rb") as f, open(tmp_v, "ab") as gv:
            for _ in range(20):
                f.seek(leidos); b = f.read()
                if b: gv.write(b); leidos += len(b)
                gv.flush(); os.fsync(gv.fileno())
                if path.stat().st_size <= leidos: break
        orig = path.stat().st_size
        if not ok_fin or n_p - 1 != n or orig != leidos or os.path.getsize(tmp_v) != len(cab) + (leidos - fin):
            tmp_p.unlink(missing_ok=True); tmp_v.unlink(missing_ok=True)
            raise RuntimeError(f"verificacion fallida rotar_antiguas {path.name}: {n_p=} {n=} {ok_fin=} {orig=} {leidos=}")
        os.replace(tmp_p, final)
        os.replace(tmp_v, path)
        print(f"OK: {n} filas -> {final} ({orig} -> {path.stat().st_size} bytes); pendientes MUERTAS (> {dias_muertas} d) movidas sin resolver: {muertas}")
        return n
    finally:
        if lk:
            fcntl.flock(lk, fcntl.LOCK_UN); lk.close()


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "rotar_antiguas":
        rotar_antiguas(sys.argv[2], lock=(sys.argv[3] if len(sys.argv) > 3 else None))
    elif len(sys.argv) == 3 and sys.argv[1] == "rotar":
        rotar(sys.argv[2])
    else:
        sys.exit("uso: csv_rotado.py rotar <ruta.csv> | rotar_antiguas <ruta.csv> [lockfile]")
