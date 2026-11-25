"""
universo_5m_io.py -- formato y E/S compartidos del universo Up/Down con TOKENS (13-Nov, staging).
Lo usan: capture_markets (adelanto, escritor), new_market_universo (listener, escritor), libro_estado_ws (lector, siembra de
tokens sin gamma/CLOB) y vigia_universo_5m_frescura (lector). Solo stdlib. Ninguna funcion toca red, ordenes ni data/markets.

Fichero: UNIV_DIR/new_market_universo_<dia>.csv.gz (dia = dia UTC de recepcion), un miembro gzip por lote escrito con O_APPEND
(concatenables). UNIV_DIR es un SUBdirectorio de datalogs (universo_5m/) para que ningun glob de datalogs/<prefijo>_*.csv* lo vea.
Lectura tolerante: miembro/fichero truncado -> se usa lo legible; filas invalidas se descartan; el mismo market_id con tokens o
condition_id DISTINTOS en dos filas = incoherente -> el mercado se EXCLUYE (fail-closed) y se cuenta.
"""
import csv, gzip, io, json, os, re, time, zlib
from datetime import datetime, timedelta, timezone
from pathlib import Path

UNIV_DIR = Path(os.environ.get("UNIVERSO_5M_DIR", "/root/polymarket-research-datalogs/universo_5m"))
PREFIJO = "new_market_universo_"
RETENCION_DIAS = 7
ACTIVOS = {"btc", "eth", "sol", "xrp", "doge", "bnb"}
DUR_S = {"5m": 300, "15m": 900, "1h": 3600, "4h": 14400}
RE_SLUG = re.compile(r"^([a-z0-9]+)-updown-(5m|15m|1h|4h|24h)-(\d+)$")      # polyv2*, hype... no casan
COLS = ["t_recv_ms", "t_evento_ms", "fuente", "market_id", "condition_id", "slug", "activo", "marco", "inicio_ts", "cierre_ts",
        "token_up", "token_down", "outcomes", "question"]


def fichero(dia, directorio=None):
    return Path(directorio or UNIV_DIR) / f"{PREFIJO}{dia}.csv.gz"


def dia_utc(t_s=None):
    return datetime.fromtimestamp(time.time() if t_s is None else t_s, timezone.utc).strftime("%Y-%m-%d")


def parsear_nuevo(e, t_recv, fuente="ws"):
    """new_market (o dict equivalente) -> fila, o None si no es Up/Down de las 6 monedas o esta incompleto/incoherente."""
    slug = str(e.get("slug") or "")
    m = RE_SLUG.match(slug)
    if not m or m.group(1) not in ACTIVOS:
        return None
    toks, outs = e.get("assets_ids") or e.get("clob_token_ids") or [], e.get("outcomes") or []
    if not isinstance(toks, list) or not isinstance(outs, list) or len(toks) != 2 or len(outs) != 2 or str(toks[0]) == str(toks[1]):
        return None
    por = {str(o).strip().lower(): str(t) for o, t in zip(outs, toks)}
    if set(por) != {"up", "down"} or not all(t.isdigit() for t in por.values()):
        return None
    mid, cid = str(e.get("id") or ""), str(e.get("market") or e.get("condition_id") or "")
    if not mid or not cid.startswith("0x"):
        return None
    ini, marco = int(m.group(3)), m.group(2)
    try:
        t_ev = int(e.get("timestamp") or t_recv)
    except (TypeError, ValueError):
        t_ev = t_recv
    return {"t_recv_ms": t_recv, "t_evento_ms": t_ev, "fuente": fuente, "market_id": mid, "condition_id": cid, "slug": slug,
            "activo": m.group(1).upper(), "marco": marco, "inicio_ts": ini, "cierre_ts": ini + DUR_S.get(marco, 0),
            "token_up": por["up"], "token_down": por["down"], "outcomes": json.dumps(outs), "question": str(e.get("question", ""))[:140]}


def filas_de_evento_gamma(ev, t_recv, fuente="gamma"):
    """Evento de gamma (events?slug=) -> filas (una por mercado up/down), mismas reglas que parsear_nuevo."""
    out = []
    for mk in ev.get("markets") or []:
        try:
            toks = mk.get("clobTokenIds")
            toks = json.loads(toks) if isinstance(toks, str) else toks
            outs = mk.get("outcomes")
            outs = json.loads(outs) if isinstance(outs, str) else outs
        except (TypeError, ValueError):
            continue
        f = parsear_nuevo({"slug": ev.get("slug"), "assets_ids": toks, "outcomes": outs, "id": mk.get("id"),
                           "market": mk.get("conditionId"), "question": mk.get("question")}, t_recv, fuente)
        if f:
            f["t_evento_ms"] = ""
            out.append(f)
    return out


def escribir(filas, directorio=None):
    """Un miembro gzip por (lote, dia), O_APPEND + fsync. Lanza OSError si falla (el llamador NO debe dar el lote por hecho)."""
    if not filas:
        return 0
    por_dia = {}
    for f in filas:
        por_dia.setdefault(dia_utc(int(f["t_recv_ms"]) / 1000), []).append(f)
    d = Path(directorio or UNIV_DIR)
    d.mkdir(parents=True, exist_ok=True)
    for dia, fs in por_dia.items():
        p = fichero(dia, d)
        buf = io.StringIO(newline="")
        w = csv.DictWriter(buf, fieldnames=COLS)
        w.writeheader()                         # cada miembro lleva cabecera; el lector la ignora
        w.writerows(fs)
        fd = os.open(p, os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o644)
        try:
            os.write(fd, gzip.compress(buf.getvalue().encode("utf-8")))
            os.fsync(fd)
        finally:
            os.close(fd)
    return len(filas)


def _miembros(raw):
    """Descomprime los miembros gzip concatenados de `raw`. Un miembro corrupto o cortado (escritura interrumpida) se SALTA: se
    resincroniza en la siguiente cabecera gzip, de modo que lo escrito DESPUES de un miembro roto sigue siendo legible. (bytes, ok)"""
    pos, out, ok = 0, [], True
    while pos < len(raw):
        d = zlib.decompressobj(31)
        try:
            data = d.decompress(raw[pos:])
            if not d.eof:
                raise zlib.error("miembro incompleto")
            out.append(data)
            pos = len(raw) - len(d.unused_data)
        except zlib.error:
            ok = False
            nxt = raw.find(b"\x1f\x8b\x08", pos + 1)
            if nxt < 0:
                break
            pos = nxt
    return b"".join(out), ok


def _leer_fichero(p):
    """Filas legibles de un .csv.gz (miembros concatenados); truncado/corrupto -> lo legible. (filas, ok)"""
    try:
        raw = Path(p).read_bytes()
    except OSError:
        return [], False
    datos, ok = _miembros(raw)
    out = []
    try:
        for r in csv.DictReader(io.StringIO(datos.decode("utf-8", errors="replace"), newline=""), fieldnames=COLS):
            if r.get("market_id") and r["market_id"] != "market_id" and r.get("token_up") and r["token_up"] != "token_up":
                out.append(r)
    except csv.Error:
        ok = False
    return out, ok


_CACHE = {}


def leer(ahora=None, directorio=None, dias=2):
    """(mercados, stats). mercados: {market_id: fila} de hoy y los (dias-1) anteriores, SIN filtrar por vigencia (el llamador filtra);
    stats: {'ficheros','filas','invalidas','conflictos','truncados'}. Sin ficheros -> ({}, stats con ficheros=0). Cache por (ruta,
    tamano, mtime): releer es gratis si no cambio."""
    ahora = time.time() if ahora is None else ahora
    d = Path(directorio or UNIV_DIR)
    st = {"ficheros": 0, "filas": 0, "invalidas": 0, "conflictos": 0, "truncados": 0}
    mercados, malos = {}, set()
    for i in range(dias - 1, -1, -1):           # antiguo -> reciente (el reciente gana en metadatos; los tokens deben coincidir)
        p = fichero(dia_utc(ahora - 86400 * i), d)
        try:
            s = p.stat()
        except OSError:
            continue
        clave = (str(p), s.st_ino, s.st_size, s.st_mtime_ns)
        c = _CACHE.get(str(p))
        if c and c[0] == clave:
            filas, ok = c[1], c[2]
        else:
            filas, ok = _leer_fichero(p)
            _CACHE[str(p)] = (clave, filas, ok)
        st["ficheros"] += 1
        st["truncados"] += 0 if ok else 1
        for r in filas:
            st["filas"] += 1
            try:
                mid, up, dn, cid = r["market_id"], r["token_up"], r["token_down"], r["condition_id"]
                cierre = int(r["cierre_ts"])
                if not (up.isdigit() and dn.isdigit() and up != dn and cid.startswith("0x")) or r["activo"].lower() not in ACTIVOS:
                    raise ValueError
            except (KeyError, ValueError, AttributeError, TypeError):
                st["invalidas"] += 1
                continue
            prev = mercados.get(mid)
            if prev is not None and (prev["token_up"], prev["token_down"], prev["condition_id"]) != (up, dn, cid):
                malos.add(mid)
            r["_cierre"] = cierre
            mercados[mid] = r
    for mid in malos:
        mercados.pop(mid, None)
    st["conflictos"] = len(malos)
    return mercados, st


def pausa_tras_429(ahora_dt):
    """Epoch hasta el que no se llama a gamma tras un 429: xx+1:02 si el 429 llega en xx:40-xx:59; 120 s en otro caso."""
    if ahora_dt.minute >= 40:
        return (ahora_dt.replace(minute=2, second=0, microsecond=0) + timedelta(hours=1)).timestamp()
    return (ahora_dt + timedelta(seconds=120)).timestamp()


def retencion(directorio=None, dias=RETENCION_DIAS):
    lim = time.time() - dias * 86400
    for p in Path(directorio or UNIV_DIR).glob("*"):
        try:
            if p.is_file() and p.stat().st_mtime < lim:
                p.unlink()
        except OSError:
            pass
