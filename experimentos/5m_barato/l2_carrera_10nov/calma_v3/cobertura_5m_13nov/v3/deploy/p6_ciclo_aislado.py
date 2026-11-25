#!/usr/bin/env python3
"""p6_ciclo_aislado.py -- P6 (L2): PROVOCA la verificacion del capture_markets que acaba de quedar en main: UNA captura real (gamma/CoinGecko, solo lecturas HTTP) del codigo
desplegado, en un directorio TEMPORAL aislado (cwd = tmp: data/markets, data/prices y data/shadow caen ahi; UNIVERSO_5M_DIR = tmp/univ; sin cfg del adelanto => comportamiento
main). No escribe nada en el repo ni en datalogs. Veredicto determinista:
  exit 0 = OK      : rc 0, filas escritas en tmp/data/markets, ningun error de CODIGO, y NINGUN adelanto_*/new_market_universo_* con el adelanto apagado.
  exit 1 = FALLO   : error de codigo (Traceback o 'ERROR polymarket/precios: <NameError|...>'), rc != 0, ficheros de adelanto escritos con el adelanto apagado, o sin filas y sin
                     excusa transitoria.
  exit 2 = INCONCLUSO: todos los intentos (--intentos, separados --pausa s) chocaron con una causa transitoria (429/red/timeout): no se puede decidir.
Uso: p6_ciclo_aislado.py --repo R --tmp T [--timeout 240] [--intentos 3] [--pausa 70]"""
import argparse, os, re, shutil, subprocess, sys, time
from pathlib import Path

# UNICA fuente de las listas = deploy/clases_error.conf (CLAVE='valor'); CLASES_CONF puede apuntar a una copia verificada (la exporta el despliegue). Este modulo es el UNICO clasificador de
# errores: lib_espera_hijos.sh lo llama con `p6_ciclo_aislado.py --clasifica duro|blando|transitorio < texto` (sin duplicar la logica en awk/bash).
def _carga_conf(path):
    d = {}
    for l in Path(path).read_text().splitlines():
        m = re.match(r"^([A-Z_]+)='(.*)'\s*$", l)
        if m:
            d[m.group(1)] = m.group(2)
    return d


_CONF = _carga_conf(os.environ.get("CLASES_CONF") or Path(__file__).resolve().parent / "clases_error.conf")
CODIGO_BLANDO = _CONF["CAP_ERR_BLANDO"]
BLANDO = re.compile("^" + CODIGO_BLANDO + "$")
CLASE_RED, CLASE_OS = re.compile("^" + _CONF["CAP_CLASE_RED"] + "$"), re.compile("^" + _CONF["CAP_CLASE_OS"] + "$")
CLASE_HTTP, HTTP_MSG = re.compile("^" + _CONF["CAP_CLASE_HTTP"] + "$"), re.compile(_CONF["CAP_HTTP_TRANSITORIO_MSG"])
CLASE_JSON, JSON_MSG = re.compile("^" + _CONF["CAP_CLASE_JSON"] + "$"), re.compile(_CONF["CAP_JSON_TRANSITORIO_MSG"])
TRANSITORIO_ERE, LINEA_ERR = _CONF["CAP_TRANSITORIO_ERE"], _CONF["CAP_LINEA_ERR"]
TRANSITORIO = re.compile(TRANSITORIO_ERE)         # SOLO para el MENSAJE de una clase de SO (OSError..): patrones de red anclados (429/5xx, timed out, Connection reset/refused, Name or service not known)
OS_ENTORNO = re.compile(_CONF["CAP_OS_ENTORNO_MSG"])   # clase B: disco lleno ([Errno 28] / No space left on device) = entorno, inconcluso; NO es una frase de red
LINEA_TRANS = re.compile(_CONF["CAP_LINEA_TRANSITORIA_ERE"])     # L2: excusa de texto libre, ANCLADA al inicio de linea; un '429' o 'timeout' suelto NO cuenta
IDENT = re.compile(r"^[A-Za-z_][A-Za-z0-9_.]*$")
SALIDA = "from capture_markets import una_captura; r = una_captura(); print('RESULTADO', r)"


def _bloques_fatales(out):
    """Misma logica que lib::traceback_fatal(out, 'capture_markets|universo_5m_io'): bloques Traceback que tocan esos modulos y no son de apagado."""
    fatal, inb, blk, hit = [], False, [], False
    for l in out.split("\n"):
        if l.startswith("Traceback (most recent call last)"):
            if not inb:
                inb, hit, blk = True, False, []
            blk.append(l); continue
        if inb and re.match(r"[ \t]", l):
            blk.append(l); hit = hit or bool(re.search(r"capture_markets|universo_5m_io", l)); continue
        if inb and re.match(r"(During handling of the above exception|The above exception was the direct cause)", l):
            blk.append(l); continue
        if inb:
            blk.append(l); inb = False
            if hit and not re.match(r"(builtins\.)?(KeyboardInterrupt|SystemExit|SIGTERM|BrokenPipeError)", l):
                fatal.append(blk)
    if inb and hit:
        fatal.append(blk)
    return fatal


def _transitoria(clase, msg):
    """El filtro transitorio mira la CLASE (ultimo componente), nunca la linea entera: de red (CAP_CLASE_RED) => transitoria; HTTPError solo con 401/403/408/429/5xx; JSONDecodeError solo con el
    mensaje tipico de cuerpo vacio/HTML; de SO (OSError..) solo si su MENSAJE casa; cualquier otra clase NUNCA (un NameError que diga 'ConnectionError' es codigo)."""
    u = clase.split(".")[-1]
    return (bool(CLASE_RED.match(u)) or bool(CLASE_HTTP.match(u) and HTTP_MSG.search(msg)) or bool(CLASE_JSON.match(u) and JSON_MSG.search(msg))
            or bool(CLASE_OS.match(u) and (TRANSITORIO.search(msg) or OS_ENTORNO.search(msg))))


def _cand_tb(out):
    """La excepcion de cada Traceback propio es SOLO la ULTIMA linea del bloque (no cuentan marcas de encadenado): CUALQUIER clase, con o sin modulo, con o sin ': mensaje' (L1: una clase de una sola
    palabra sin sufijo ni mensaje, p.ej. 'Boom', TAMBIEN es la excepcion: es DURA salvo que su clase sea transitoria). Devuelve (clase, mensaje, linea, es_gamma=False)."""
    res = []
    for b in _bloques_fatales(out):
        l = b[-1] if b else ""
        if not l or l[0] in " \t" or l.startswith("Traceback (most recent") or re.match(r"(During handling|The above exception)", l):
            continue
        c = l.split(":")[0]
        if IDENT.match(c):
            res.append((c, re.sub(r"^: ", "", l[len(c):]), l, False))
    return res


def _cand_ln(out):
    """Lineas '<CAP_LINEA_ERR>: <Clase>[: msg]' que capture_markets imprime sin Traceback. es_gamma = el prefijo es 'Error gamma ..' (respuesta de gamma): solo ahi una clase de datos es BLANDA."""
    res = []
    for l in out.split("\n"):
        m = re.search(LINEA_ERR + ": ", l)
        if m:
            r = l[m.end():]; c = r.split(":")[0]
            if IDENT.match(c):
                res.append((c, re.sub(r"^: ", "", r[len(c):]), l, l[m.start():].startswith("Error gamma")))
    return res


def clasifica(out):
    """(duros, blandos). DURO: excepcion de CUALQUIER clase en un Traceback propio; linea 'ERROR polymarket|precios|adelanto 5m: <Clase>' de CUALQUIER clase (esa ruta ya esta envuelta en
    except Exception: print = codigo propio); linea 'Error gamma ..: <Clase>' de clase no de datos. BLANDO: SOLO 'Error gamma ..: <KeyError|IndexError|ValueError|TypeError>'. Transitoria => se descarta."""
    duros = [l for c, m, l, g in _cand_tb(out) if not _transitoria(c, m)]
    blandos = []
    for c, m, l, g in _cand_ln(out):
        if _transitoria(c, m):
            continue
        (blandos if g and BLANDO.match(c.split(".")[-1]) else duros).append(l)
    return duros, blandos


def excusa(out):
    """L2: lineas que EXCUSAN un ciclo sin crecimiento (inconcluso, no fallo). Solo (a) la excepcion de un Traceback propio / linea 'Error gamma|ERROR ..' cuya CLASE es transitoria (_transitoria) y
    (b) lineas de texto libre que casan CAP_LINEA_TRANSITORIA_ERE ancladas al inicio. Un 429/timeout suelto en medio de una linea, o en un NameError, no excusa nada."""
    r = [l for c, m, l, g in _cand_tb(out) + _cand_ln(out) if _transitoria(c, m)]
    return r + [l for l in out.split("\n") if LINEA_TRANS.match(l)]


def un_intento(repo, tmp, timeout, n, cap_viejo=None):
    """cap_viejo = ruta del capture_markets.py.pre: repite LA MISMA captura con el codigo VIEJO (sin universo_5m_io, que no existia en la base)."""
    d = Path(tmp) / f"run{n}"
    (d / "univ").mkdir(parents=True)
    for f in (("capture_markets.py", "data_quality.py") if cap_viejo else ("capture_markets.py", "universo_5m_io.py", "data_quality.py")):
        if (Path(repo) / f).exists():
            shutil.copy(Path(repo) / f, d / f)
    if cap_viejo:
        shutil.copy(cap_viejo, d / "capture_markets.py")
    env = {k: v for k, v in os.environ.items() if not k.startswith(("CAPTURE_", "UNIVERSO_5M"))}
    env["UNIVERSO_5M_DIR"] = str(d / "univ")
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    try:
        p = subprocess.run([sys.executable, "-I", "-c", "import sys; sys.path.insert(0, '.'); " + SALIDA], cwd=d, env=env, capture_output=True, text=True, timeout=timeout)
        out, rc = p.stdout + p.stderr, p.returncode
    except subprocess.TimeoutExpired as e:
        dec = lambda x: x.decode(errors="replace") if isinstance(x, bytes) else (x or "")
        out, rc = dec(e.stdout) + dec(e.stderr), 124          # tambien el stderr parcial (tracebacks) de lo que alcanzo a imprimir
        out += "\n(la captura aislada no termino en %ss)" % timeout
    filas = 0
    for f in (d / "data" / "markets").glob("*.csv") if (d / "data" / "markets").exists() else []:
        filas += max(0, sum(1 for _ in open(f, "rb")) - 1)
    adelanto = [x.name for x in (d / "univ").iterdir() if x.name.startswith(("adelanto_", "new_market_universo_"))]
    codigo, blandos = clasifica(out)
    return rc, out, filas, adelanto, codigo, blandos


def firma(codigo):
    """R3: 'falla igual' = mismo conjunto de CLASES de excepcion (el mensaje lleva rutas/valores que cambian); fail-closed: sin clase reconocible => firma unica (nunca 'igual')."""
    def clase(l):      # M1: Traceback => 1er campo de la ultima linea; linea '<CAP_LINEA_ERR>: <Clase>[: msg]' => la CLASE tras el prefijo (mismo criterio que _cand_ln), nunca el prefijo 'ERROR polymarket'
        c = l.strip().split(":")[0]
        if IDENT.match(c):
            return c.split(".")[-1]
        m = re.search(LINEA_ERR + ": ", l)
        return l[m.end():].split(":")[0].strip().split(".")[-1] if m else object()
    return frozenset(clase(l) for l in codigo) or frozenset({object()})


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if argv and argv[0] == "--clasifica":       # UNICO clasificador para bash: texto por stdin, imprime las lineas duras/blandas (rc 0)
        txt = sys.stdin.read()
        d, b = clasifica(txt)
        sel = excusa(txt) if argv[1:] == ["transitorio"] else (d if argv[1:] == ["duro"] else b)
        if sel:
            print("\n".join(sel))
        return 0
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True); ap.add_argument("--tmp", required=True)
    ap.add_argument("--timeout", type=float, default=240); ap.add_argument("--intentos", type=int, default=3); ap.add_argument("--pausa", type=float, default=70)
    ap.add_argument("--pre", default=None, help="capture_markets.py.pre (codigo VIEJO): ante un error DURO se repite la misma captura con el, para distinguir regresion de entorno")
    a = ap.parse_args(argv)
    ult = ""; n_blando = 0; ej_blando = ""; n_duro = 0; ej_duro = ""; viejo_igual = False
    for n in range(1, a.intentos + 1):
        rc, out, filas, adelanto, codigo, blandos = un_intento(a.repo, a.tmp, a.timeout, n)
        ult = out.strip().splitlines()[-1][:200] if out.strip() else "(sin salida)"
        if codigo:
            # R3: un DURO unico no revierte. (1) misma captura con el codigo VIEJO: si falla IGUAL (misma clase) no es regresion => INCONCLUSO, sin marcha atras;
            # (2) FALLO solo si el DURO PERSISTE en el nuevo (2 intentos separados por --pausa) o si no queda reintento y el viejo no falla igual (fail-closed: en duda, DURO).
            n_duro += 1; ej_duro = ' | '.join(codigo[:3])
            if a.pre and Path(a.pre).exists() and not viejo_igual:
                _, outv, _, _, codv, _ = un_intento(a.repo, a.tmp, a.timeout, "viejo%d" % n, cap_viejo=a.pre)
                if codv and firma(codv) == firma(codigo):
                    viejo_igual = True
                    print(f"INCONCLUSO intento {n}: el error de codigo ({ej_duro}) lo da IGUAL el capture_markets VIEJO (.pre): no es regresion del codigo nuevo, sin marcha atras"); return 2
                print(f"intento {n}: DURO en el codigo nuevo ({ej_duro}) y el viejo {'falla distinto: ' + ' | '.join(codv[:2]) if codv else 'NO falla'}")
            if n_duro >= 2 or n == a.intentos:
                print(f"FALLO intento {n}: rc={rc} error de codigo{' (persiste tras reintento)' if n_duro >= 2 else ' (ultimo intento, el viejo no falla igual)'}: {ej_duro}"); return 1
            print(f"intento {n}: error de codigo ({ej_duro}): reintento en {a.pausa:.0f}s para ver si persiste"); time.sleep(a.pausa); continue
        if adelanto:
            print(f"FALLO intento {n}: con el adelanto APAGADO se escribieron {adelanto} en el dir aislado"); return 1
        if rc == 0 and filas > 0:
            if n_duro:
                print(f"AVISO INTERMITENTE: un error de codigo previo NO se repitio ({ej_duro}); bug no determinista posible, no queda verificado")
            print(f"OK intento {n}: una captura real del codigo desplegado escribio {filas} filas en data/markets (dir aislado), sin errores de codigo ni adelanto"); return 0
        if blandos:       # error dependiente de datos de la API sin crecimiento: no decide solo; FALLO si se repite en TODOS los intentos
            n_blando += 1; ej_blando = blandos[0].strip()[:160]
            print(f"intento {n}: error dependiente de los datos de la API ({ej_blando}) sin filas escritas: no decide" + (f"; reintento en {a.pausa:.0f}s" if n < a.intentos else "; sin mas intentos"))
            if n < a.intentos:
                time.sleep(a.pausa)
            continue
        if rc == 0 and not excusa(out):
            print(f"FALLO intento {n}: rc=0, 0 filas escritas y sin causa transitoria ni error de codigo: {ult}"); return 1
        # rc 124 (timeout), causa transitoria, o rc != 0 sin error de codigo ni causa conocida (red/DNS fuera de los try, proceso matado): sin evidencia de bug => no decide
        causa = "causa transitoria (429/red/timeout)" if (rc == 124 or excusa(out)) else f"rc={rc} sin error de codigo ni causa conocida (no es evidencia de bug)"
        print(f"intento {n}: {causa}, filas={filas}: {ult}" + (f"; reintento en {a.pausa:.0f}s" if n < a.intentos else "; sin mas intentos"))
        if n < a.intentos:
            time.sleep(a.pausa)
    if n_blando == a.intentos:     # R5: un error dependiente de los DATOS de la API (KeyError/ValueError de una respuesta malformada) en todos los intentos NO revierte: el codigo viejo rompia igual. Solo un Traceback propio es FALLO.
        print(f"INCONCLUSO: el mismo tipo de error de datos de la API en TODOS los intentos ({ej_blando}): no es evidencia contra el codigo (un Traceback propio sí lo seria)"); return 2
    if n_duro:
        print(f"INCONCLUSO: un error de codigo ({ej_duro}) en un intento que no se repitio ni se pudo reconfirmar ({a.intentos} intentos; ultimo: {ult})"); return 2
    print(f"INCONCLUSO: {a.intentos} intentos sin veredicto (causa transitoria o rc != 0 sin evidencia de bug; ultimo: {ult})"); return 2


if __name__ == "__main__":
    sys.exit(main())
