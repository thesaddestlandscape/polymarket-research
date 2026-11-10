#!/usr/bin/env python3
"""l2_gzcat.py FICHERO.gz [--stats RUTA.json] : zcat TOLERANTE para libro5_ms con gzip truncado/corrupto (restos de reinicios).
Escribe a stdout SOLO lineas completas (termina en \\n) hasta el punto de corrupcion; la linea final incompleta se descarta
(nunca se emite basura). Nunca aborta (exit 0 salvo fichero ilegible). Estadisticas a JSON y a stderr:
  truncado (stream sin cierre), corrupto (zlib.error), lineas_ok, bytes_comp/consumidos, linea_parcial_descartada (bytes),
  filas_perdidas_est = ESTIMACION de las filas tras el punto de fallo = comp_restante * filas/comp_consumido (None si no hay fallo).
Soporta ficheros con varios miembros gzip concatenados. "perdidas" es estimacion; las filas ya emitidas son exactas."""
import json, os, sys, zlib

CHUNK = 1 << 20


def leer_tolerante(path, salida, stats=None):
    """Vuelca lineas completas de `path` en `salida` (objeto con .write(bytes)). Devuelve dict de estadisticas."""
    st = {"fichero": os.path.basename(path), "bytes_comp": os.path.getsize(path), "bytes_comp_consumidos": 0,
          "lineas_ok": 0, "bytes_out": 0, "truncado": False, "corrupto": False, "error": None,
          "linea_parcial_descartada_bytes": 0, "filas_perdidas_est": None}
    resto = b""                      # texto descomprimido tras la ultima linea completa
    d = zlib.decompressobj(wbits=31)
    consumidos = 0
    fallo = False
    alimentado = [False]            # el miembro actual ha recibido datos

    def emitir(datos):
        nonlocal resto
        buf = resto + datos
        i = buf.rfind(b"\n")
        if i < 0:
            resto = buf
            return
        bloque, resto = buf[:i + 1], buf[i + 1:]
        salida.write(bloque)
        st["lineas_ok"] += bloque.count(b"\n")
        st["bytes_out"] += len(bloque)

    with open(path, "rb") as f:
        pendiente = b""
        while not fallo:
            chunk = f.read(CHUNK)
            if not chunk:
                break
            data = pendiente + chunk
            pendiente = b""
            while data and not fallo:
                alimentado[0] = True
                respaldo = d.copy()                # estado previo al trozo: permite recuperar lo anterior al fallo
                try:
                    out = d.decompress(data)
                except zlib.error as e:
                    st["corrupto"], st["error"] = True, str(e)[:120]
                    fallo = True
                    d = respaldo                   # reintento en rodajas pequenas hasta el byte que rompe
                    for i in range(0, len(data), 256):
                        try:
                            emitir(d.decompress(data[i:i + 256]))
                            consumidos += len(data[i:i + 256])
                        except zlib.error:
                            break
                    break
                emitir(out)
                if d.eof:                          # fin de miembro: siguiente miembro (si hay)
                    consumidos += len(data) - len(d.unused_data)
                    data = d.unused_data
                    d = zlib.decompressobj(wbits=31)
                    alimentado[0] = False
                    if data and data[:2] != b"\x1f\x8b":
                        st["corrupto"], st["error"] = True, "basura tras miembro gzip"
                        fallo = True
                else:
                    consumidos += len(data)
                    data = b""
        if not fallo and alimentado[0] and not d.eof:
            st["truncado"] = True          # miembro gzip abierto sin cierre
    if st["truncado"] and not st["corrupto"]:
        st["error"] = "fin de fichero sin cierre de miembro gzip"
    st["linea_parcial_descartada_bytes"] = len(resto)
    st["bytes_comp_consumidos"] = consumidos
    if (st["truncado"] or st["corrupto"]) and consumidos > 0 and st["lineas_ok"] > 0:
        rest = max(st["bytes_comp"] - consumidos, 0)
        st["filas_perdidas_est"] = int(rest * st["lineas_ok"] / consumidos) + (1 if resto else 0)
    elif (st["truncado"] or st["corrupto"]):
        st["filas_perdidas_est"] = 1 if resto else 0
    if stats:
        stats.update(st)
    return st


def main(argv):
    if not argv:
        print(__doc__, file=sys.stderr)
        return 2
    path, rutaj = argv[0], None
    if "--stats" in argv:
        rutaj = argv[argv.index("--stats") + 1]
    try:
        st = leer_tolerante(path, sys.stdout.buffer)
        sys.stdout.buffer.flush()
    except BrokenPipeError:
        return 0
    except OSError as e:
        print(json.dumps({"fichero": path, "error_fatal": str(e)}), file=sys.stderr)
        return 1
    if rutaj:
        tmp = rutaj + ".tmp"
        with open(tmp, "w") as fh:
            json.dump(st, fh)
        os.replace(tmp, rutaj)
    print(json.dumps(st), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
