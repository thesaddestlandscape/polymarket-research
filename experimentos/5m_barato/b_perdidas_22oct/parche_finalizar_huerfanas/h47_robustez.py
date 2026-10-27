"""Robustez del ejecutor B (H47) frente a muertes del proceso: SOLO REGISTROS. No envia, cancela ni modifica ordenes; no toca precios ni stake.

Tres piezas (todas fail-safe: ante cualquier error se avisa por stderr/ledger y se sigue, jamas se bloquea ni se aborta el ciclo de trading):
 (a) hilo de huerfanas (SOLO ejecutor real, baja prioridad, arranque diferido): reconstruye `puja_fin` de mercados con puja_post sin puja_fin
     cuyo cierre ya paso, con una COPIA vendorizada de reconstruir_puja_fin.py (hash comprobado). Lee el ledger por su cuenta (nunca
     X.leer_ledger: su cache global no es thread-safe) y DIFIERE los slugs con ordenes aun sin verificar (se reintenta). Salida SEPARADA e
     idempotente por slug, nunca el ledger. Un puja_fin `interrumpida` (parcial) cuenta como huerfano: se reconstruye aparte (reconstruible).
 (b) finalizar_al_salir: corre DESPUES de ex.cerrar_salida (cancelacion de ordenes reales) -> ver instalar(); sin red; recoge los rellenos
     tardios que dejo cerrar_salida (sincronizar_rellenos) y escribe puja_fin parcial (interrumpida, relleno_cota_inferior) + mercado_fin.
 (c) tick: en el hot path solo copia el delta de mids (lock de libro minimo) a una cola ACOTADA en memoria; un hilo escritor aparte hace el gz
     (h47_mids_<ledger>_AAAA-MM-DD_<pid>.jsonl.gz: fichero propio por proceso, un miembro gzip por volcado; retencion RETENCION_DIAS). La cobertura
     ("hasta") solo avanza con el WS vivo. Perdida ante SIGKILL <= INTERVALO_S + cola. Sin setpriority/nice (inversion de prioridad con el GIL).
"""
import glob
import gzip
import hashlib
import importlib.util
import json
import os
import collections
import fcntl
import queue
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

DIR = Path(os.environ.get("H47R_DIR", "/root/polymarket-research-datalogs"))
RECON_OUT = os.environ.get("H47R_OUT", str(DIR / "puja_fin_reconstruido.jsonl"))
RPF_VENDOR = Path(__file__).resolve().parent / "reconstruir_puja_fin_vendor.py"
RPF_SHA256 = "6ba9de79b076021b92c8ae7cf18fd76d4e3df4bbf77ea29639d6d47054457c09"   # copia literal de etiquetado_pasivo/scripts/reconstruir_puja_fin.py
MARK_S = (5, 30, 120)               # = experimento_maker_h47.MARK_S (se comprueba en los tests)
INTERVALO_S = 10.0
RETENCION_DIAS = 14
ARRANQUE_DIFERIDO_S = 45.0          # el hilo de huerfanas no hace nada hasta pasado el arranque (el hot path va primero)
REINTENTO_S = 120.0
MAX_PASOS = 6                       # 1 pasada completa + reintentos SOLO de los diferidos (~10 min)
AMBITO_REINTENTO_S = 86400.0        # los reintentos solo miran mercados de las ultimas 24 h
FIN_ESPERA_S = 35.0                 # = experimento_maker_h47.FIN_ESPERA_S (se comprueba en los tests): el proceso vivo aun finaliza hasta fin+35 s
HOLGURA_S = 60.0
COLA_MAX = 2000
UMBRAL_WS_S = 5.0                   # = X.WS_MAX_S: sin mensajes del WS mas de esto = no se reclama cobertura
ESPERA_ESCRITOR_S = 3.0             # tope de espera a vaciar la cola en la salida

AVISOS = []                         # avisos de hilos aparte (los drena tick() en el hilo principal hacia el ledger: el ledger NO es thread-safe)
_LEDGER_DEF = [None]


def _aviso(msg, ledger=False):
    try:
        os.write(2, (f"[h47_robustez] {msg}\n").encode())
    except Exception:
        pass
    if ledger:
        AVISOS.append(str(msg)[:300])


def sha_codigo():
    """Hashes de este modulo y del vendor para el evento config (trazabilidad del codigo que corrio)."""
    try:
        return {"h47_robustez": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()[:16],
                "vendor_rpf": hashlib.sha256(RPF_VENDOR.read_bytes()).hexdigest()[:16]}
    except Exception as e:
        return {"error": f"{type(e).__name__}"}


def _ledger_actual():
    if _LEDGER_DEF[0] is None:
        from experimento_pares_cola_15m import LEDGER
        _LEDGER_DEF[0] = LEDGER
    return _LEDGER_DEF[0]


# ---------------------------------------------------------------- (c) mids incrementales: cola + escritor aparte
_Q = queue.Queue(maxsize=COLA_MAX)
_W = {"t": None}
_WLK = threading.Lock()
_STOP = threading.Event()           # parada ordenada de los hilos auxiliares
_HILOS = []


def _ruta_mids(ledger_path, ts=None):
    d = datetime.fromtimestamp(ts or time.time(), timezone.utc).strftime("%Y-%m-%d")
    return DIR / f"h47_mids_{Path(ledger_path).stem}_{d}_{os.getpid()}.jsonl.gz"   # fichero propio por proceso: un gz truncado solo pierde su cola


def _escritor():
    avisado = False
    while True:
        it = _Q.get()
        try:
            if it is None:
                return
            p, linea = it
            try:
                p.parent.mkdir(parents=True, exist_ok=True)
                with gzip.open(p, "ab") as f:           # un miembro gzip por volcado
                    f.write((json.dumps(linea, separators=(",", ":")) + "\n").encode())
            except Exception as e:                       # un volcado perdido deja HUECO (desde_idx): leer_mids no extiende la cobertura sobre el
                if not avisado:
                    avisado = True
                    _aviso(f"escritor de mids fallido: {type(e).__name__}: {str(e)[:120]}", ledger=True)
        finally:
            _Q.task_done()


def _escritor_asegurar():
    t = _W["t"]
    if t is not None and t.is_alive():
        return
    with _WLK:
        t = _W["t"]
        if t is None or not t.is_alive():
            _W["t"] = threading.Thread(target=_escritor, daemon=True, name="h47_mids_writer")
            _W["t"].start()
            _HILOS.append(_W["t"])


def vaciar(timeout=ESPERA_ESCRITOR_S):
    """Espera (acotado) a que el escritor vacie la cola. True si vacia."""
    fin = time.time() + timeout
    while _Q.unfinished_tasks and time.time() < fin:
        time.sleep(0.01)
    return not _Q.unfinished_tasks


def _ws_vivo(lib, ahora):
    """WS sano: hilo vivo, sin error y con mensajes recientes. Si no se puede saber -> False (fail-closed: no se reclama cobertura)."""
    try:
        return bool(lib.hilo.is_alive() and lib.error is None and ahora - lib.ult_msg <= UMBRAL_WS_S)
    except Exception:
        return False


def volcar_mids(ex, c, ledger_path, ahora=None, forzar=False):
    """Encola el delta de mids de la cara elegida (sin I/O). Devuelve nº de puntos encolados (0 si nada / no toca / cola llena).
    'hasta' (cobertura) solo avanza si el WS esta vivo; con WS muerto se vuelca igual lo que haya pero con la ultima cobertura sana.
    Cola llena: no se descarta nada, el indice no avanza y el delta se reenvia en el siguiente volcado (sin hueco)."""
    ahora = time.time() if ahora is None else ahora
    if c.tok is None or not (c.hashes or getattr(c, "posteado", False)):
        return 0
    if not forzar and ahora - getattr(c, "_h47r_t", 0.0) < INTERVALO_S:
        return 0
    idx = getattr(c, "_h47r_idx", 0)
    with c.lib.lk:                                  # mínimo: solo la copia del trozo nuevo
        nuevos = c.lib.mids[c.tok][idx:]
    nuevos = [[float(t), float(m)] for t, m in nuevos]
    c._h47r_t = ahora
    if _ws_vivo(c.lib, ahora):
        c._h47r_hasta = ahora
    else:
        c._h47r_gap = True                          # sin mensajes: lo que haya NO cubre el intervalo; desde aqui la cobertura queda congelada
    hasta = getattr(c, "_h47r_hasta", 0.0)         # 0.0 = nunca hubo WS sano: no cubre nada
    linea = {"slug": c.mk["slug"], "lado": c.lados[c.tok], "tok": c.tok, "fin": c.mk["fin"], "desde_idx": idx, "hasta": hasta, "gap": bool(getattr(c, "_h47r_gap", False)), "m": nuevos}
    _escritor_asegurar()
    try:
        _Q.put_nowait((_ruta_mids(ledger_path, ahora), linea))
    except queue.Full:
        return 0
    c._h47r_idx = idx + len(nuevos)
    return len(nuevos)


def tick(ex, c):
    """Llamada desde el bucle de run() antes de paso_seguro. Nunca lanza, sin I/O de disco (salvo drenar avisos raros al ledger)."""
    try:
        led = getattr(ex, "_h47r_ledger", None) or _ledger_actual()
        volcar_mids(ex, c, led)
        while AVISOS:
            ex._log47({"tipo": "aviso_robustez", "msg": AVISOS.pop(0)})
    except Exception as e:
        if not getattr(c, "_h47r_avisado", False):
            c._h47r_avisado = True
            _aviso(f"volcado de mids fallido ({c.mk.get('slug')}): {type(e).__name__}: {str(e)[:120]}")


def leer_mids(ledger_path, dias=3, ahora=None):
    """{slug: {"lado","fin","hasta","m":[(t,mid),..],"hueco":bool}} desde los gz recientes. Tolera ficheros/miembros corruptos o truncados
    (zlib.error, BadGzipFile, EOFError...: se conserva lo leido antes). Cobertura 'hasta' SOLO sobre volcados contiguos (desde_idx): tras un
    hueco deja de avanzar (los puntos posteriores se conservan, pero sin reclamar cobertura)."""
    ahora = time.time() if ahora is None else ahora
    out = {}
    for k in range(dias, -1, -1):                   # cronologico: el dia mas antiguo primero
        try:
            d = datetime.fromtimestamp(ahora - 86400 * k, timezone.utc).strftime("%Y-%m-%d")
            ps = sorted(glob.glob(str(DIR / f"h47_mids_{Path(ledger_path).stem}_{d}*.jsonl.gz")), key=lambda x: (os.path.getmtime(x), x))
        except Exception:
            continue
        for p in ps:                                 # un fichero por proceso (pid) + el formato antiguo sin pid
            yield_lineas = []
            try:
                with gzip.open(p, "rb") as f:
                    for ln in f:
                        yield_lineas.append(ln)
            except Exception:                        # miembro truncado/corrupto (SIGKILL, disco): este fichero solo pierde su cola
                pass
            _acumular(out, yield_lineas)
    for e in out.values():
        e["m"] = sorted(e["m"].items())
    return out


def _acumular(out, lineas):
    for ln in lineas:
        try:
            d = json.loads(ln)
            pts = [(float(t), float(m)) for t, m in d["m"]]
            hasta = float(d["hasta"])
            desde = int(d["desde_idx"])
            e = out.setdefault(d["slug"], {"lado": d["lado"], "fin": float(d["fin"]), "hasta": 0.0, "m": {}, "sig": 0, "hueco": False})
        except Exception:
            continue                                # linea corrupta/truncada: se ignora entera (no se usan datos a medias)
        if desde > e["sig"] or d.get("gap"):
            e["hueco"] = True                       # volcado perdido o WS caido en algun momento: la cobertura deja de avanzar
        if not e["hueco"]:
            e["hasta"] = max(e["hasta"], hasta)
        e["sig"] = max(e["sig"], desde + len(pts))
        for t, m in pts:
            e["m"][t] = m                           # idempotente ante volcados repetidos


def _mid_en(xs, t):
    lo, hi = 0, len(xs)
    while lo < hi:
        mid = (lo + hi) // 2
        if xs[mid][0] <= t:
            lo = mid + 1
        else:
            hi = mid
    return xs[lo - 1][1] if lo > 0 else None


def aplicar_markouts(reg, mids):
    """Rellena mid_Xs/markout_Xs de un puja_fin reconstruido con los mids persistidos. Valido solo si t0+s <= min(fin, cobertura 'hasta')
    y el relleno no es tardio; si no, None (missing). Devuelve el nº de markouts calculados."""
    e = mids.get(reg["slug"])
    if not e:
        return 0
    n = 0
    for r in reg.get("rellenos", []):
        r["markouts_disponibles"] = False
        for s in MARK_S:
            t = r["t_deteccion"] + s
            ok = (not r.get("tardio")) and t <= e["fin"] and t <= e["hasta"]
            m = _mid_en(e["m"], t) if ok else None
            r[f"mid_{s}s"] = m
            r[f"markout_{s}s"] = (m - r["precio"]) / r["precio"] if m is not None else None
            if m is not None:
                n += 1
                r["markouts_disponibles"] = True
    if n:
        reg["markouts"] = "parcial_mids_persistidos"
        reg["mids_cobertura_hasta"] = e["hasta"]
    return n


# ---------------------------------------------------------------- (a) huerfanas
def _cargar_rpf():
    """Copia VENDORIZADA (junto a este fichero) con hash comprobado; nunca se ejecuta codigo de otra ruta. RuntimeError si falta o no coincide."""
    if not RPF_VENDOR.exists():
        raise RuntimeError(f"falta {RPF_VENDOR.name} junto a h47_robustez.py")
    if hashlib.sha256(RPF_VENDOR.read_bytes()).hexdigest() != RPF_SHA256:
        raise RuntimeError(f"hash de {RPF_VENDOR.name} distinto del esperado: no se ejecuta")
    spec = importlib.util.spec_from_file_location("reconstruir_puja_fin_vendor", RPF_VENDOR)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    m.OUT = RECON_OUT
    return m


def recuperar_huerfanas(filas, ledger_path, ahora=None, rpf=None, posic=None, slugs=None):
    """Reconstruye y escribe (idempotente por slug, solo-anade, bajo flock) los puja_fin de mercados huerfanos. Un puja_fin `interrumpida` NO
    cuenta como cierre (se reconstruye aparte, marcado). Devuelve (n_nuevos, n_ya, regs)."""
    ahora = time.time() if ahora is None else ahora
    rpf = rpf or _cargar_rpf()
    parciales = {d.get("slug") for d in filas if isinstance(d, dict) and d.get("tipo") == "puja_fin" and d.get("interrumpida")}
    filas = [d for d in filas if not (isinstance(d, dict) and d.get("tipo") == "puja_fin" and d.get("interrumpida"))]
    regs = rpf.reconstruir(filas, rpf.cargar_posic() if posic is None else posic, ahora, slugs)
    if not regs:
        return 0, 0, []
    try:
        mids = leer_mids(ledger_path, ahora=ahora)
    except Exception as e:
        mids = {}
        _aviso(f"leer_mids fallido, markouts missing: {type(e).__name__}: {str(e)[:100]}")
    for r in regs:
        try:
            aplicar_markouts(r, mids)
        except Exception as e:
            _aviso(f"markouts de {r.get('slug')} fallidos (missing): {type(e).__name__}")
        if r["slug"] in parciales:
            r["sustituye_puja_fin_parcial"] = True
    nuevos, ya = escribir_preferente(regs)
    return nuevos, ya, regs


def _tiene_markouts(r):
    return r.get("markouts") not in (None, "missing")


def escribir_preferente(regs, out=None):
    """Como rpf.escribir: SOLO ANADE, bajo el MISMO flock OUT.lock, fsync, idempotente por slug. Unica diferencia: si el slug ya tiene fila pero todas
    con markouts 'missing' y la nueva los trae, se ANADE tambien (reemplaza_missing=True); el lector (markouts_desde_registro.por_slug) elige la
    completa. Devuelve (anadidas, ya_estaban)."""
    out = out or RECON_OUT
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out + ".lock", "w") as lk:
        fcntl.flock(lk, fcntl.LOCK_EX)
        previas = collections.defaultdict(list)
        if os.path.exists(out):
            for ln in open(out):
                try:
                    d = json.loads(ln)
                    previas[d.get("slug")].append(d)
                except Exception:
                    pass
        nuevas = []
        for r in regs:
            ex = previas.get(r["slug"])
            if not ex:
                nuevas.append(r)
            elif _tiene_markouts(r) and not any(_tiene_markouts(d) for d in ex):
                nuevas.append(dict(r, reemplaza_missing=True))
            if nuevas and nuevas[-1]["slug"] == r["slug"]:
                previas[r["slug"]].append(nuevas[-1])
        if nuevas:
            with open(out, "a") as f:
                if f.tell() and open(out, "rb").read()[-1:] != b"\n":
                    f.write("\n")                                  # cola a medias
                for r in nuevas:
                    f.write(json.dumps(r, separators=(",", ":")) + "\n")
                f.flush()
                os.fsync(f.fileno())
    return len(nuevas), len(regs) - len(nuevas)


class bloqueo_proceso:
    """flock NO bloqueante sobre OUT.proc.lock: UN solo reconstructor (hilo del ejecutor o cron diario) trabaja a la vez. Si esta tomado, `ok`=False
    y el llamador se salta la pasada (el otro ya esta procesando esos slugs; lo que marque queda en OUT y el siguiente lo ve como 'ya')."""
    def __init__(self, out=None):
        self.path = (out or RECON_OUT) + ".proc.lock"
        self.f, self.ok = None, False

    def __enter__(self):
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        self.f = open(self.path, "w")
        try:
            fcntl.flock(self.f, fcntl.LOCK_EX | fcntl.LOCK_NB)
            self.ok = True
        except OSError:
            self.ok = False
        return self

    def __exit__(self, *a):
        if self.f is not None:
            self.f.close()                          # cierra y libera el flock


def purgar_viejos(ahora=None):
    ahora = time.time() if ahora is None else ahora
    for p in glob.glob(str(DIR / "h47_mids_*.jsonl.gz")):
        try:
            if ahora - os.path.getmtime(p) > RETENCION_DIAS * 86400:
                os.remove(p)
        except OSError:
            pass


def fin_de(slug):
    return float(slug.rsplit("-", 1)[1]) + 300.0


def slugs_sin_verificar(filas):
    """Slugs con alguna orden real aun no cerrada segun el plegado del ledger (UNICA definicion; la usa tambien el cron diario):
    abierta (hi>lo), anomala o ilegible, sin alias. Cubre intenciones sin puja_post. Una orden sin slug propio toma el de otra fila con su oid;
    si no tiene ninguno no es atribuible a un mercado y se ignora."""
    import pares_contabilidad as C
    filas = [d for d in filas if isinstance(d, dict)]
    oid2slug = {d["oid"]: d["slug"] for d in filas if d.get("oid") and isinstance(d.get("slug"), str) and d["slug"]}
    out = set()
    for o in C.plegar(filas).values():
        sl = o.slug if isinstance(o.slug, str) and o.slug else oid2slug.get(o.oid)
        if sl and not o.alias and (o.abierta or o.anomala or o.ilegible):
            out.add(sl)
    return out


Prep = collections.namedtuple("Prep", "permitidos parciales esperan inmaduros vencidos")


def preparar(filas, ahora, propios=(), max_edad_s=AMBITO_REINTENTO_S):
    """UNICA logica de seleccion de huerfanas (hilo del ejecutor y cron diario). Devuelve Prep(permitidos, parciales, esperan, inmaduros, vencidos):
    permitidos = maduros (fin+FIN_ESPERA_S+HOLGURA_S pasado), sin puja_fin completo, sin ordenes sin verificar y no propios;
    parciales  = slugs con un puja_fin `interrumpida` (NO cierra el mercado: se reconstruye aparte, marcado);
    esperan    = maduros con ordenes sin verificar y de las ultimas `max_edad_s` (24 h): los que de verdad esperan una verificacion;
    inmaduros  = aun no maduros (se reintentan, pero NO cuentan como 'esperan');
    vencidos   = sin verificar desde hace mas de `max_edad_s`: ya no se esperan; hay que avisar (una vez) para resolverlos a mano.
    Los slugs con solo intenciones (sin puja_post) cuentan como candidatos."""
    filas = [d for d in filas if isinstance(d, dict)]
    completos = {d.get("slug") for d in filas if d.get("tipo") == "puja_fin" and not d.get("interrumpida")}
    parciales = {d.get("slug") for d in filas if d.get("tipo") == "puja_fin" and d.get("interrumpida")}
    cand = {d["slug"] for d in filas if d.get("tipo") in ("puja_post", "intencion_post") and isinstance(d.get("slug"), str) and d["slug"]}
    cand -= completos
    cand -= set(propios)
    dif = slugs_sin_verificar(filas)
    maduros = {x for x in cand if ahora >= fin_de(x) + FIN_ESPERA_S + HOLGURA_S}
    viejos = {x for x in cand if ahora - fin_de(x) > max_edad_s}
    return Prep(maduros - dif, parciales, sorted((maduros & dif) - viejos), sorted(cand - maduros), sorted(viejos & dif))


class LedgerCache:
    """Lectura INCREMENTAL del ledger para el hilo de huerfanas (solo lineas completas nuevas; sin tocar X.leer_ledger, que no es thread-safe).
    Indice por slug (filas de ese mercado, en orden) para que los reintentos no sean O(ledger)."""
    def __init__(self, path):
        self.path, self.off, self.filas, self.por_slug, self.oid2slug = Path(path), 0, [], {}, {}

    def refrescar(self):
        try:
            if self.path.stat().st_size < self.off:
                self.__init__(self.path)            # truncado/rotado: se empieza de cero
            with open(self.path, "rb") as f:
                f.seek(self.off)
                datos = f.read()
        except OSError:
            return self.filas
        corte = datos.rfind(b"\n") + 1                 # solo lineas completas
        for ln in datos[:corte].splitlines():
            try:
                d = json.loads(ln)
            except Exception:
                continue
            if not isinstance(d, dict):
                continue
            self.filas.append(d)
            if d.get("oid") and isinstance(d.get("slug"), str) and d["slug"]:
                self.oid2slug[d["oid"]] = d["slug"]
            sl = d.get("slug") if isinstance(d.get("slug"), str) and d.get("slug") else self.oid2slug.get(d.get("oid"))
            if sl:
                self.por_slug.setdefault(sl, []).append(d)
        self.off += corte
        return self.filas

    def de_slugs(self, slugs):
        return [d for sl in sorted(slugs) for d in self.por_slug.get(sl, [])]


def pasada_huerfanas(ex, ledger_path, rpf, ahora=None, posic=None, solo=None, cache=None):
    """Una pasada. Foto de los slugs propios ANTES de leer el ledger. `solo` = reintento restringido a esos slugs (usa el indice de `cache`: coste
    proporcional a esos mercados, no al ledger). Devuelve (nuevos, ya, regs, pendientes, vencidos)."""
    ahora = time.time() if ahora is None else ahora
    propios = {c.mk["slug"] for c in list(ex.ctxs.values()) if hasattr(c, "mk")}      # ANTES de leer el ledger
    cache = cache or LedgerCache(ledger_path)
    cache.refrescar()
    filas = cache.filas if solo is None else cache.de_slugs(solo)
    prep = preparar(filas, ahora, propios)
    pendientes = prep.esperan + prep.inmaduros        # a reintentar (esperan + aun no maduros)
    if not prep.permitidos:
        return 0, 0, [], pendientes, prep.vencidos
    with bloqueo_proceso() as b:
        if not b.ok:                                  # el cron diario esta reconstruyendo: se reintenta en la siguiente pasada
            return 0, 0, [], sorted(set(pendientes) | prep.permitidos), prep.vencidos
        nuevos, ya, regs = recuperar_huerfanas(filas, ledger_path, ahora=ahora, rpf=rpf, posic=posic, slugs=prep.permitidos)
    return nuevos, ya, regs, pendientes, prep.vencidos


def _hilo_huerfanas(ex, ledger_path):
    """Sin print ni prioridades: avisos por os.write/ledger. Espera por Event (parada ordenada). Una pasada completa y reintentos SOLO de los
    que esperan (sin verificar o aun no maduros) de las ultimas 24 h, con el ledger leido de forma incremental."""
    try:
        if _STOP.wait(ARRANQUE_DIFERIDO_S):
            return
        rpf = _cargar_rpf()
        cache = LedgerCache(ledger_path)
        solo, esperan, avisados = None, [], False
        for _ in range(MAX_PASOS):
            nuevos, ya, regs, esperan, vencidos = pasada_huerfanas(ex, ledger_path, rpf, solo=solo, cache=cache)
            if vencidos and not avisados:               # UNA vez por proceso: llevan >24 h sin verificar y ya no se esperan
                avisados = True
                _aviso(f"huerfanas: {len(vencidos)} slug(s) sin verificar desde hace >24 h (resolver a mano): {vencidos[:5]}", ledger=True)
            if regs or esperan:
                _aviso(f"huerfanas: candidatas={len(regs)} nuevas={nuevos} ya_estaban={ya} esperan={len(esperan)} -> {RECON_OUT}", ledger=True)
            esperan = [x for x in esperan if time.time() - fin_de(x) <= AMBITO_REINTENTO_S]
            if not esperan or _STOP.wait(REINTENTO_S):
                break
            solo = esperan
        if esperan and not _STOP.is_set():
            _aviso(f"huerfanas: {len(esperan)} slug(s) siguen esperando (sin verificar / no maduros) tras {MAX_PASOS} pasadas: {esperan[:5]}", ledger=True)
    except Exception as e:
        _aviso(f"recuperacion de huerfanas fallida: {type(e).__name__}: {str(e)[:200]}", ledger=True)


# ---------------------------------------------------------------- (b) salida: puja_fin parcial sin red (DESPUES de cerrar_salida)
def resumen_parcial(ex, c, ahora=None, post_cierre=False):
    """puja_fin de un mercado vivo sin red (memoria + ledger). Mismos campos que Exp47.finalizar + interrumpida/cota inferior.
    relleno_real nunca afirma False sin garantia: solo si cerrar_salida corrio, ex.ordenes() no fallo, TODAS las ordenes estan vistas y cerradas y no hay vivas/kill."""
    ahora = time.time() if ahora is None else ahora
    lib, fin = c.lib, c.mk["fin"]
    for tok, e in c.estado.items():
        for r in e["rellenos"]:
            t0 = r["t_deteccion"]
            for s in MARK_S:
                m = lib.mid_en(tok, t0 + s) if (t0 + s <= min(fin, ahora) and not r.get("tardio")) else None
                r[f"mid_{s}s"] = m
                r[f"markout_{s}s"] = (m - r["precio"]) / r["precio"] if m is not None else None
    e = c.estado[c.tok]
    ords, ords_ok = {}, False
    try:
        ords = ex.ordenes() if ex.real else {}
        ords_ok = bool(ex.real)
    except Exception:
        pass
    sin_ver = sorted(h for h in c.hashes if h in ords and ords[h].abierta and not ords[h].alias)
    vivas = sorted(h for h in c.hashes if h in getattr(ex, "vivas", {}) or h in getattr(ex, "canceladas", {}))
    f_gem = [ex.gem_lleno.get(h, 0.0) for h in c.hashes] if ex.real else [ex.sim_lleno.get(h, 0.0) for h in c.hashes]
    if not ex.real:
        relleno = None
    elif e["llenas"] > 1e-9:
        relleno = True
    else:
        todas_cerradas = ords_ok and bool(c.hashes) and all(h in ords and not ords[h].abierta for h in c.hashes)    # fail-closed: toda orden vista y cerrada
        relleno = False if (post_cierre and todas_cerradas and not vivas and not ex.kill) else None
    return {"tipo": "puja_fin", "slug": c.mk["slug"], "coin": c.coin, "lado": c.lados[c.tok], "k": c.k, "n_ordenes": len(c.hashes),
            "llenas_detectadas": e["llenas"], "llenas_en_vuelo": sum(r["acc"] for r in e["rellenos"] if not r.get("tardio")),
            "rellenos_tardios": sum(1 for r in e["rellenos"] if r.get("tardio")), "coste_detectado": e["coste"],
            "fin_puja": c.fin_puja or c.motivo_cierre or "salida_proceso", "relleno_real": relleno,
            "relleno_solo_trades": [], "ordenes_sin_verificar": sin_ver, "ordenes_vivas_al_salir": vivas,
            "relleno_cota_inferior": True, "interrumpida": True, "post_cerrar_salida": bool(post_cierre), "contraste_trades": "missing",
            "sim_relleno_cualquiera": bool(any(x > 1e-9 for x in f_gem)), "sim_acciones_max": max(f_gem) if f_gem else 0.0,
            "rellenos": e["rellenos"], "libro_dec": c.libro_dec, "variante": "H35b" if ex.t_stop >= 90 else "H35",
            "lo_hi_por_orden": {h: [round(ords[h].lo, 4), round(ords[h].hi, 4)] for h in c.hashes if h in ords}}


def mercado_fin_parcial(ex, c):
    lib = c.lib
    return {"tipo": "mercado_fin", "slug": c.mk["slug"], "coin": c.coin, "motivo": c.motivo_cierre or "salida_proceso", "medido": c.medido,
            "posteado": c.posteado, "trades_propios": "missing", "kill": ex.kill, "senal": ex.senal, "interrumpida": True,
            "ws_malos": getattr(lib, "malos", 0), "ws_ultimo_malo": getattr(lib, "ultimo_malo", None)}


def finalizar_al_salir(ex, post_cierre=None):
    """Salida. SOLO se ejecuta tras ex.cerrar_salida (ver instalar). Idempotente (un puja_fin y un mercado_fin por slug: ledger + memoria).
    Nunca lanza, sin red, acotado."""
    try:
        from experimento_pares_cola_15m import leer_ledger
        filas = leer_ledger()
        ya = {d.get("slug") for d in filas if d.get("tipo") == "puja_fin"}
        ya_mf = {d.get("slug") for d in filas if d.get("tipo") == "mercado_fin"}
        hechos = getattr(ex, "_h47r_hechos", None)
        if hechos is None:
            hechos = ex._h47r_hechos = set()
        led = getattr(ex, "_h47r_ledger", None) or _ledger_actual()
        post = bool(getattr(ex, "_h47r_cs_ok", False)) if post_cierre is None else bool(post_cierre)
        for c in list(ex.ctxs.values()):
            slug = None
            try:
                if not hasattr(c, "estado") or c.fase == "fin" or c.tok is None or not c.hashes:
                    continue
                slug = c.mk["slug"]
                if slug in ya or slug in hechos:
                    continue
                if ex.real:
                    try:
                        ex.sincronizar_rellenos(c)          # rellenos que cerrar_salida leyo tras cancelar (solo ledger, sin red)
                    except Exception as e:
                        _aviso(f"sincronizar_rellenos fallido ({slug}): {type(e).__name__}: {str(e)[:100]}")
                ex._log47(resumen_parcial(ex, c, post_cierre=post))
                hechos.add(slug)                            # solo tras el exito de _log47 (si falla, no queda "hecho")
                if slug not in ya_mf:
                    try:
                        ex._log47(mercado_fin_parcial(ex, c))
                    except Exception as e:
                        _aviso(f"mercado_fin parcial fallido ({slug}): {type(e).__name__}: {str(e)[:100]}")
                try:
                    volcar_mids(ex, c, led, forzar=True)
                except Exception:
                    pass
            except Exception as e:
                _aviso(f"puja_fin parcial fallido ({slug}): {type(e).__name__}: {str(e)[:120]}")
        vaciar()
        while AVISOS:
            try:
                ex._log47({"tipo": "aviso_robustez", "msg": AVISOS.pop(0)})
            except Exception:
                break
    except Exception as e:
        _aviso(f"finalizar_al_salir fallido: {type(e).__name__}: {str(e)[:160]}")


def detener(espera=1.0):
    """Parada ordenada: Event + centinela del escritor + join corto (acotado) de los hilos auxiliares. Nunca lanza."""
    try:
        _STOP.set()
        if _W["t"] is not None and _W["t"].is_alive():
            try:
                _Q.put_nowait(None)
            except queue.Full:
                pass
        fin = time.time() + espera
        for t in list(_HILOS):
            if t is not threading.current_thread():
                t.join(max(0.0, fin - time.time()))
        _HILOS[:] = [t for t in _HILOS if t.is_alive()]
    except Exception:
        pass


def _envolver_cerrar_salida(ex):
    """Todas las llamadas a ex.cerrar_salida pasan por aqui (run() la llama como self.cerrar_salida): `_h47r_cs_ok` = ALGUNA llamada la ejecuto hasta
    el final (tambien si fue por el camino normal de run()). Una llamada que encuentra `_cerrado` ya puesto (otra a medias / que lanzo) no lo marca."""
    orig = ex.cerrar_salida
    def cerrar_salida():
        antes = bool(getattr(ex, "_cerrado", False))
        orig()
        if not antes:
            ex._h47r_cs_ok = True
    ex.cerrar_salida = cerrar_salida


def _salida(ex):
    """atexit unico: PRIMERO ex.cerrar_salida (cancelar ordenes reales; idempotente), DESPUES los registros. Sin I/O antes de cancelar.
    Si cerrar_salida lanza o no completo, los registros salen SIN garantia de "sin relleno" (`_h47r_cs_ok` no se marca)."""
    try:
        ex.cerrar_salida()
    finally:
        try:
            finalizar_al_salir(ex)
        finally:
            detener()


def instalar(ex):
    """Llamar una vez al inicio de run(). atexit LIFO: este se registra despues que el de cerrar_salida (en Exp.__init__), asi que correria
    ANTES; por eso el hook llama el mismo a cerrar_salida primero y el registro original queda en no-op.
    Orden: PRIMERO atexit(_salida) y el hilo de huerfanas (solo ejecutor REAL: en seco no se escribe en el puja_fin_reconstruido de produccion);
    despues purga (real y seco) y escritor, cada uno en su propio try: un fallo accesorio nunca deja sin el hook de salida."""
    _STOP.clear()
    try:
        import atexit
        atexit.register(_salida, ex)
        _envolver_cerrar_salida(ex)
    except Exception as e:
        _aviso(f"instalar: atexit fallido: {type(e).__name__}: {str(e)[:120]}")
    try:
        ex._h47r_ledger = _ledger_actual()          # capturado aqui, fuera del hot path
        if ex.real:
            t = threading.Thread(target=_hilo_huerfanas, args=(ex, Path(ex._h47r_ledger)), daemon=True, name="h47_huerfanas")
            _HILOS.append(t)
            t.start()
    except Exception as e:
        _aviso(f"instalar: hilo de huerfanas fallido: {type(e).__name__}: {str(e)[:120]}")
    for f in (purgar_viejos, _escritor_asegurar):
        try:
            f()
        except Exception as e:
            _aviso(f"instalar: {f.__name__} fallido: {type(e).__name__}: {str(e)[:120]}")
