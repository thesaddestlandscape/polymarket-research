#!/usr/bin/env python3
"""pl_core.py -- NUCLEO PURO del paquete de medicion de `l` (12-Nov-2026). SIN red, SIN firma, SIN py-clob-client, SIN leer .env: solo configuracion congelada, plan determinista, ledger (JSONL con fsync),
checkpoint atomico, manifiesto, replay de estado, presupuesto duro, clasificacion de respuestas del CLOB y analisis de anclas. El envio vive en pl_sender.py (doble) y pl_sender_real.py (adaptador real, cargado
SOLO con --real + fichero de confirmacion). Reutiliza (copia citada) los clasificadores puros de sonda1.py (clasificar_post/clasificar_excepcion_post/es_terminal) y plan_paquete_l.analiza para las anclas.
Contrato (Javi 12-Nov): wallet dedicada 0x659a...297F, saldo on-chain verificado 12-Nov = 0,612681 pUSD, perdida dura 0,61 $ (abortar al tocar el suelo), GTD (v6: NUNCA GTC) post-only BUY a 0,01 de 5 acc (0,05 $ de colateral),
<=12 simultaneas (12 x 0,05 = 0,60 <= 0,61: la perdida maxima es ESTRUCTURAL aunque se rellenaran todas), objetivo >=100 anclas DIRECTAS (canal de usuario) en BTC+ETH+SOL+XRP."""
import os, sys, json, time, hashlib, re, collections, dataclasses, glob, gzip, types, zlib, fcntl

HERE = os.path.dirname(os.path.abspath(__file__)) + '/'


class Invariante(Exception):
    """Violacion de un invariante de dinero/seguridad. Se lanza con `exigir` (raise explicito: NO desaparece con `python -O`, a diferencia de `assert`)."""


def exigir(cond, msg):
    if not cond: raise Invariante(msg)


VERSION = 'paquete_l_v21'                                 # v16 (13-Nov): 14o /code-review (3 hallazgos + pasada corta); invalida cualquier confirmacion escrita para v2..v15
WALLET_DEDICADA = '0x659a40FF9920fEBc5a66836213040924343d297F'
COINS = ('BTC', 'ETH', 'SOL', 'XRP')
FALLBACK_DIR = '/tmp'                                       # v4 (hallazgo 10): si el informe final no se puede escribir en el out, se deja aqui (y en stderr)
LOCK_DIR = '/tmp'                                           # v7 (hallazgo 3): locks de instancia unica (por wallet y por --out) FUERA de --out
OUT_BASE = '/root/polymarket-research-datalogs/paquete_l/'            # fuera de git; 1 directorio por run (~200 KB); retencion manual 30 d (ver LEEME)


@dataclasses.dataclass(frozen=True)
class Config:
    wallet: str = WALLET_DEDICADA
    saldo_autorizado: float = 0.612681          # lo verificado on-chain el 12-Nov; Javi autoriza gastar SOLO esto
    perdida_dura: float = 0.61                  # $: techo de perdida; el suelo = saldo_inicial - perdida_dura
    precio: float = 0.01
    size: float = 5.0                           # minimo del CLOB (shares)
    max_simultaneas: int = 12
    lote: int = 8                               # ordenes por lote (secuencial; colateral reutilizado entre lotes)
    hold_min_s: float = 1.5                     # get_order devuelve null hasta ~1,06-1,41 s tras el POST (calibracion Sonda): hold >= 1,5 s para que el DELETE vea la orden indexada
    index_gracia_s: float = 4.0                 # ventana desde el ack en la que un 'no existe' de get_order NO es fallo de cancelacion (indexacion): se reintenta sin gastar intentos
    hold_max_s: float = 2.5
    objetivo_anclas: int = 100                  # anclas DIRECTAS validas (alta + cancelacion en el canal de usuario + cancel_try)
    min_anclas_moneda: dict = dataclasses.field(default_factory=lambda: {'BTC': 30, 'ETH': 20, 'SOL': 20, 'XRP': 20})
    peso_moneda: dict = dataclasses.field(default_factory=lambda: {'BTC': 2, 'ETH': 1, 'SOL': 1, 'XRP': 1})
    max_ordenes: int = 220                      # tope duro de ordenes enviadas (plan 140 + reserva)
    plan_ordenes: int = 140
    max_minutos: float = 45.0
    min_vida_mercado_s: float = 90.0            # v3 (hallazgo 2): mercados con tiempo de sobra (el precio no puede colapsar a 0,01 por cierre inminente)
    prep_presupuesto_s: float = 40.0            # margen de vida extra por el tiempo de preparacion del lote (gate del canal de usuario, tick) que se hace ANTES de enviar nada
    top_ask_max: float = 0.05                   # fase B: solo tokens casi resueltos (ask <= 0,05): la posicion residual vale <= 5 x 0,05 = 0,25 $ de valor esperado y se contabiliza
    push_poll_s: float = 0.25                   # cadencia de lectura local del canal de usuario (fills push)
    saldo_reintentos: int = 3
    saldo_backoff_s: tuple = (0.3, 0.6, 1.2)
    bid_min_lejos: float = 0.20                 # modo 'lejos' (v3, hallazgo 2): mejor bid publico >= 0,20 = 19 ticks por encima de nuestra orden a 0,01 (antes 0,05): rellenarla exigiria un colapso de precio de >=19c en <= 2,5 s
    ask_min: float = 0.02                       # post-only a 0,01 no cruza si ask >= 0,02
    req_por_s: float = 6.0                      # tope global de peticiones (POST+DELETE+lecturas) por segundo
    espaciado_post_s: float = 0.35
    espera_mercado_s: float = 2.0               # sin mercado/libro valido: reintento cada 2 s sin consumir el slot
    max_espera_mercado_s: float = 120.0         # ...y BLOCKED si dura 2 min
    kill_429_seguidos: int = 3
    backoff_429_s: tuple = (2.0, 4.0, 8.0)
    kill_rechazos_seguidos: int = 2
    ack_max_ms: int = 1000                      # ack > 1 s => anomalia (kill), como plan_paquete_l
    fase_b_max_rellenos: int = 0                # 0 = fase B DESACTIVADA (solo modo 'lejos'). >0: ordenes 'top' que pueden rellenarse (parciales); exige campo en la confirmacion
    fase_b_tope_usd: float = 0.15
    fase_b_ordenes: int = 12
    hold_b_min_s: float = 10.0
    hold_b_max_s: float = 20.0
    fase_b_min_vida_s: float = 15.0             # v7 (hallazgo 6): fase B BUSCA tokens casi resueltos, que solo existen en la recta final de un 5m (en ~0,3 de la vida): NO hereda los 90 s de la fase A (con hold 10-20 s + 2 + prep 40 = 142-152 s al elegir, casi nunca coincidia con bid==0,01 y ask<=0,05).
                                                # Aqui: vida al POST >= 15 + hold(10-20) + 2 = 27-37 s (margen para DELETE/indexacion 1,4 s/relleno y cierre) y al elegir +prep 40 s = 67-77 s
    fase_b_espera_s: float = 300.0              # v7 (hallazgo 6): sin token barato valido se espera hasta 1 ciclo completo de mercado 5m (la ventana aparece en la recta final) y la fase B TERMINA de forma benigna (el run conserva el status de la fase A)
    tol_saldo_usd: float = 0.004                # v3 (hallazgo 4): tolerancia de la comparacion saldo vs ledger; DEBE ser < 1 share a 0,01 (0,01 $) para ver un relleno minimo (antes 0,02 = 2 shares)
    libro_max_s: float = 1.0                    # v3 (hallazgo 2): si la lectura del libro justo antes del POST tarda mas, el libro se considera rancio y no se envia
    gtd_expira_s: int = 200                     # v4 (R2): cota DURA de vida en el exchange (GTD post-only). DOCS OFICIALES (docs.polymarket.com/trading/place-orders, leido 12-Nov): la orden GTD expira 60 s ANTES de la expiracion declarada y la expiracion debe estar >= 3 min en el futuro (si no, RECHAZADA) => 200 s = 20 s de margen sobre 180; vida efectiva maxima ~140 s. 0 = GTC. Si el CLOB rechaza GTD(+post-only) (o cualquier orden) => BLOCKED sin gasto y SIN cambiar de modo (v5: no hay caida a GTC; ese modo solo existiria con permiso explicito en la confirmacion)
    asentamiento_extra_s: float = 3.0           # v4 (hallazgo 5): tras el POST se espera index_gracia_s + 3 s antes de dar 'inexistente_verificada' o de comparar el saldo (indexacion de get_order + bloque on-chain)
    reloj_max_dispersion_s: float = 0.5         # v5 (R3): Root dispersion maxima de chrony; ademas Leap status Normal, Stratum 1-9 y Reference ID externo (reloj_sincronizado)
    cancel_intentos_barrido: int = 6            # v5 (hallazgo 1): intentos de cancelacion (con backoff, reloj del barrido) por orden antes de declararla INDETERMINADA / viva
    reloj_max_offset_s: float = 1.0             # v4 (hallazgo 4): con GTD, el reloj local debe estar a <= 1 s de NTP (chrony) antes de CADA lote; sin lectura => BLOCKED sin gasto
    cancel_lecturas_estado: int = 8             # v21: lecturas del estado tras una cancelacion aceptada antes de declarar INDETERMINADA (antes 4 a 0,25 s)
    cancel_lectura_espera_s: float = 0.5
    lote_kill_max_s: float = 20.0               # v21: tope de un lote con kill activo antes de ceder al barrido final
    seed: int = 20261112

    def __post_init__(self):
        exigir(self.max_simultaneas * self.size * self.precio <= self.perdida_dura + 1e-9, 'perdida estructural maxima > perdida dura')
        exigir(self.perdida_dura <= self.saldo_autorizado + 1e-9, 'perdida dura > saldo autorizado')
        exigir(self.precio <= 0.02 + 1e-12 and self.size >= 5.0 and 0 < self.lote <= self.max_simultaneas, 'precio/size/lote fuera de rango')
        exigir(self.fase_b_max_rellenos * self.size * self.precio <= self.fase_b_tope_usd + 1e-9, 'fase B: rellenos x coste > tope fase B')
        exigir(self.fase_b_tope_usd <= self.perdida_dura, 'tope fase B > perdida dura')
        exigir(0 < self.tol_saldo_usd < self.precio, 'tolerancia de saldo >= 1 share: no veria un relleno minimo')
        exigir(self.fase_b_min_vida_s > 0 and self.fase_b_espera_s > 0, 'fase B: vida minima/espera > 0')
        exigir(self.gtd_expira_s >= 185, 'GTD obligatorio (sin modo GTC): el CLOB exige expiracion >= now+3 min (180 s; docs 12-Nov) y se deja >= 5 s de margen')

    @property
    def coste_orden(self): return round(self.size * self.precio, 6)

    def sha(self): return hashlib.sha256(json.dumps(dataclasses.asdict(self), sort_keys=True, default=str).encode()).hexdigest()


FICHEROS_CODIGO = ('pl_core.py', 'pl_sender.py', 'pl_sender_real.py', 'paquete_l.py')
FICHEROS_VENDOR = ('vendor/vendor_main.py', 'vendor/cancel_evidencia.py', 'vendor/envio_real.py', 'vendor/plan_paquete_l.py', 'vendor/VENDOR_HASHES.json')     # TODO lo ejecutable del paquete esta en estos ficheros (entra en codigo_sha)
NOMBRES_VENDOR = ('vendor_main', 'cancel_evidencia', 'envio_real', 'plan_paquete_l')
PERMITIDOS_EN_DIR = FICHEROS_CODIGO + ('test_paquete_l.py',)


def verificar_vendor(base=HERE):
    """Compara el sha256 de cada fichero de vendor/ con VENDOR_HASHES.json. Devuelve (ok, alteradas). Fail-closed: falta de fichero/hash = no ok."""
    try: h = json.load(open(base + 'vendor/VENDOR_HASHES.json'))['copias']
    except (OSError, ValueError, KeyError): return False, ['VENDOR_HASHES.json']
    mal = [f for f, v in h.items() if not os.path.exists(base + 'vendor/' + f) or hashlib.sha256(open(base + 'vendor/' + f, 'rb').read()).hexdigest() != v.get('sha256_copia')]
    mal += [n + '.py' for n in NOMBRES_VENDOR if n + '.py' not in h]; return not mal, mal


def cargar_vendor(nombre, base=HERE):
    """Hallazgo 1: carga un modulo de vendor/ SIN tocar sys.path. Lee los BYTES del fichero, comprueba su sha256 contra VENDOR_HASHES.json y ejecuta EXACTAMENTE esos bytes (sin ventana entre verificar e importar);
    el modulo queda en sys.modules (los demas modulos del vendor lo resuelven por nombre). Si ya hay un modulo con ese nombre que NO viene de aqui (sombra) => ImportError. Fail-closed."""
    if nombre not in NOMBRES_VENDOR: raise ImportError(f'{nombre}: no es un modulo del vendor')
    previo = sys.modules.get(nombre)
    if previo is not None:
        if getattr(previo, '__vendor_sha__', None) is None: raise ImportError(f'{nombre}: ya existe en sys.modules un modulo que NO es el vendor (sombra)')
        return previo
    try: h = json.load(open(base + 'vendor/VENDOR_HASHES.json'))['copias'][nombre + '.py']['sha256_copia']
    except (OSError, ValueError, KeyError) as e: raise ImportError(f'{nombre}: sin hash en VENDOR_HASHES.json ({type(e).__name__})')
    ruta = base + 'vendor/' + nombre + '.py'; datos = open(ruta, 'rb').read()
    if hashlib.sha256(datos).hexdigest() != h: raise ImportError(f'{nombre}: sha256 distinto al de VENDOR_HASHES.json: NO cargo')
    m = types.ModuleType(nombre); m.__file__ = ruta; m.__vendor_sha__ = h; sys.modules[nombre] = m
    try: exec(compile(datos, ruta, 'exec'), m.__dict__)
    except BaseException: sys.modules.pop(nombre, None); raise
    return m


def exigir_aislamiento(base=HERE):
    """Hallazgo 1 (solo envio real): el proceso debe correr con `python -I` (sin PYTHONPATH/PYTHONHOME/user-site/cwd en sys.path) y el directorio del paquete no puede contener ningun .py ajeno que pudiera
    sombrear la libreria estandar o un modulo importado. Fail-closed (sys.exit)."""
    if not sys.flags.isolated: sys.exit('envio real exige `python3 -I` (modo aislado): NO envio')
    if sys.flags.optimize: sys.exit('envio real exige ejecutar SIN -O/-OO (los invariantes de dinero no pueden depender de assert): NO envio')
    if any(p in ('', '.') for p in sys.path): sys.exit('sys.path contiene el directorio actual: NO envio')
    extra = sorted(f for f in os.listdir(base) if f.endswith('.py') and f not in PERMITIDOS_EN_DIR)
    if extra: sys.exit(f'ficheros .py ajenos en el directorio del paquete (podrian sombrear modulos): {extra}: NO envio')


def tomar_locks(wallet, out, lock_dir=None, wallet_lock=True):
    """v7 (hallazgo 3): INSTANCIA UNICA. flock exclusivo NO bloqueante por WALLET y por --out (realpath), en ficheros FUERA de --out (LOCK_DIR), tomados antes de cualquier lectura de estado/envio y mantenidos abiertos mientras viva el proceso (o hasta `liberar_locks`).
    Devuelve la lista de descriptores, o None si alguno esta tomado o no se puede crear (fail-closed: sin poder garantizar la instancia unica no se opera). NO toca nada de `out`."""
    fds = []
    for tipo, clave in ((('wallet', str(wallet).lower()),) if wallet_lock else ()) + (('out', os.path.realpath(str(out))),):
        ruta = os.path.join(lock_dir or LOCK_DIR, f'paquete_l_{tipo}_{hashlib.sha256(clave.encode()).hexdigest()[:20]}.lock')
        try: fd = os.open(ruta, os.O_RDWR | os.O_CREAT, 0o600)
        except OSError: liberar_locks(fds); return None
        try: fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError:
            try: os.close(fd)
            except OSError: pass
            liberar_locks(fds); return None
        try: os.ftruncate(fd, 0); os.write(fd, f'{os.getpid()} {tipo} {clave}\n'.encode())
        except OSError: pass
        fds.append(fd)
    return fds


def locks_de_run(cfg, out, real, lock_dir=None):
    """v8 (hallazgos 2 y 8): UNICO punto que decide los locks de un run. --out SIEMPRE; WALLET solo con envio real (un dry-run/simulacion no puede bloquear el run real aprobado ni al reves). None = no se pudo (ya hay otra instancia)."""
    return tomar_locks(cfg.wallet, out, lock_dir=lock_dir, wallet_lock=bool(real))


def liberar_locks(fds):
    for fd in (fds or []):
        try: os.close(fd)
        except OSError: pass


def sha_codigo(base=HERE):
    h = hashlib.sha256()
    for n in FICHEROS_CODIGO + FICHEROS_VENDOR:
        p = base + n; h.update(n.encode() + b'\0' + (open(p, 'rb').read() if os.path.exists(p) else b'<falta>') + b'\0')
    return h.hexdigest()


# ------------------------------------------------------------------------------------------------ plan determinista
@dataclasses.dataclass(frozen=True)
class Slot:
    i: int
    coin: str
    lado: int            # 0/1: que token del mercado (alterna)
    hold_s: float
    modo: str            # 'lejos' | 'top' (fase B)


def plan_slots(cfg, n=None):
    """Plan determinista (semilla fija; NO depende de datos). Monedas en ciclo ponderado (BTC x2), hold ~ U(hold_min, hold_max), lado alterno. Las ultimas `fase_b_ordenes` son 'top' solo si fase B activa."""
    import random
    r = random.Random(cfg.seed); n = n or cfg.plan_ordenes; ciclo = [c for c in COINS for _ in range(cfg.peso_moneda[c])]; out = []
    r.shuffle(ciclo); k = 0
    for i in range(n):
        if k % len(ciclo) == 0 and k: r.shuffle(ciclo)
        c = ciclo[k % len(ciclo)]; k += 1
        out.append(Slot(i=i, coin=c, lado=i % 2, hold_s=round(r.uniform(cfg.hold_min_s, cfg.hold_max_s), 3), modo='lejos'))
    if cfg.fase_b_max_rellenos > 0:
        for j in range(cfg.fase_b_ordenes):
            idx = n - 1 - j; s = out[idx]; out[idx] = Slot(s.i, s.coin, s.lado, s.hold_s, 'top')
    return out


# ------------------------------------------------------------------------------------------------ clasificadores (copia de sonda1.py L209-228, L134-138)
def clasificar_post(resp):
    """'ok' | 'rechazo' (la orden NO esta en el libro) | 'ambiguo' (puede estar viva: reconciliar)."""
    if not isinstance(resp, dict): return 'ambiguo'
    if resp.get('success') is False or resp.get('errorMsg'): return 'rechazo'
    if resp.get('success') is True and str(resp.get('status') or '').strip().lower() in ('live', 'matched', 'delayed'): return 'ok'
    return 'ambiguo'


def clasificar_excepcion_post(e):
    if type(e).__name__ == 'EnvioBloqueado': return 'rechazo'            # cancel_evidencia.gate_envio bloqueo ANTES del POST (canal de usuario no listo): no salio nada
    sc = getattr(e, 'status_code', None)
    if isinstance(sc, int) and 400 <= sc < 500 and sc not in (408, 425): return 'rechazo'
    return 'ambiguo'


def es_429(e):
    """v3 (hallazgo 6): 429 SOLO con status_code entero explicito == 429 (el CLOB no proceso la peticion). Cualquier otra cosa (texto con '429', timeouts, status ausente) es AMBIGUA: la orden pudo salir => se reconcilia, no se da por rechazada."""
    sc = getattr(e, 'status_code', None)
    return isinstance(sc, int) and not isinstance(sc, bool) and sc == 429


def post_status(resp):
    """Estado del ack de un POST en minusculas ('' si no es legible). Una GTC/GTD POST-ONLY a 0,01 solo puede quedar 'live'; 'matched'/'delayed' = anomalia (relleno o casado en curso) => corte inmediato (hallazgo 4)."""
    return str(resp.get('status') or '').strip().lower() if isinstance(resp, dict) else ''


STATUS_POST_ANOMALO = ('matched', 'delayed')


def es_terminal(est):
    e = str(est or '').strip().upper(); return e in ('MATCHED', 'INVALID', 'EXPIRED') or e.startswith('CANCELED')


def reloj_sincronizado(ch, cfg):
    """v5 (hallazgo 3) y v6 (hallazgo 5): `ch` = dict de leer_chrony(). True SOLO si chrony esta sincronizado con una fuente EXTERNA: Leap status Normal, Stratum 1-9 (>= 10 = reloj local/degradado), Reference ID != 0 y != 7F7F0101 (el
    reloj LOCAL de chrony, `local stratum`), |System time| <= reloj_max_offset_s y Root dispersion <= reloj_max_dispersion_s. Cualquier campo ausente/ilegible => False (fail-closed)."""
    if not isinstance(ch, dict): return False
    num = lambda k: ch.get(k) if isinstance(ch.get(k), (int, float)) and not isinstance(ch.get(k), bool) and ch.get(k) == ch.get(k) and abs(ch.get(k)) != float('inf') else None
    off, disp, st = num('system_time_s'), num('root_dispersion_s'), num('stratum'); rid = str(ch.get('ref_id') or '').strip().upper()
    return bool(str(ch.get('leap')).strip().lower() == 'normal' and st is not None and 1 <= st <= 9 and rid.strip('0') and rid != '7F7F0101' and off is not None and abs(off) <= cfg.reloj_max_offset_s + 1e-12 and disp is not None and 0 <= disp <= cfg.reloj_max_dispersion_s)


def id_servidor(resp, oid_local):
    if isinstance(resp, dict):
        o = str(resp.get('orderID') or '').strip()
        if o and o.lower() != str(oid_local).lower(): return o
    return None


# ------------------------------------------------------------------------------------------------ ledger
def escribir_con_fallback(ruta, obj, nombre):
    """v4 (hallazgo 10): escribe `obj` atomico en `ruta`; si falla (OSError), lo vuelca a stderr y a FALLBACK_DIR/paquete_l_<nombre>. Devuelve True si se escribio en `ruta`. Nunca lanza."""
    try: escribir_atomico(ruta, obj); return True
    except BaseException as e:
        try: print(f'NO SE PUDO ESCRIBIR {ruta} ({type(e).__name__}); contenido: ' + json.dumps(obj, default=str, sort_keys=True), file=sys.stderr, flush=True)
        except Exception: pass
        try: escribir_atomico(os.path.join(FALLBACK_DIR, 'paquete_l_' + nombre), obj)
        except BaseException: pass
        return False


def escribir_atomico(ruta, obj):
    tmp = ruta + '.tmp'
    try:
        with open(tmp, 'w') as f: json.dump(obj, f, indent=1, sort_keys=True, default=str); f.flush(); os.fsync(f.fileno())
        os.replace(tmp, ruta)
    except BaseException:                                                    # v18 (B): fallo REAL (ENOSPC, EROFS, destino directorio...): no deja el .tmp huerfano ocupando el poco espacio que queda
        try: os.unlink(tmp)
        except OSError: pass
        raise
    try:
        fd = os.open(os.path.dirname(ruta) or '.', os.O_RDONLY); os.fsync(fd); os.close(fd)
    except OSError: pass


class Ledger:
    """JSONL append-only con fsync por fila. Clave unica `eid` (duplicados se ignoran al escribir y al leer). Una linea final corrupta (SIGKILL a medias) se TRUNCA al abrir y se cuenta."""
    def __init__(self, ruta):
        self.ruta = ruta; self.eids = set(); self.filas = []; self.corruptas = 0; self.duplicadas = 0; self.fallos_escritura = 0; self.fallidos = set(); self._abrir()

    def _abrir(self):
        buenas = []; ok_bytes = 0
        if os.path.exists(self.ruta):
            with open(self.ruta, 'rb') as f: datos = f.read()
            pos = 0
            for linea in datos.split(b'\n'):
                fin = pos + len(linea) + 1
                if not linea.strip(): pos = fin; continue
                try: row = json.loads(linea)
                except ValueError:
                    self.corruptas += 1; pos = fin; continue                    # linea corrupta: se descarta (y solo la cola se trunca abajo)
                if not isinstance(row, dict) or 'eid' not in row: self.corruptas += 1; pos = fin; continue
                if row['eid'] in self.eids: self.duplicadas += 1
                else: self.eids.add(row['eid']); buenas.append(row)
                ok_bytes = min(fin, len(datos)); pos = fin
            if self.corruptas or self.duplicadas or (datos and not datos.endswith(b'\n')):        # reescritura limpia (atomica); v5 (hallazgo 7): una ultima fila SIN salto de linea (aunque sea JSON valido) se completa antes de seguir en append, o la siguiente fila se pegaria a ella
                tmp = self.ruta + '.rep'
                with open(tmp, 'w') as f:
                    for r in buenas: f.write(json.dumps(r, sort_keys=True, default=str) + '\n')
                    f.flush(); os.fsync(f.fileno())
                os.replace(tmp, self.ruta)
        self.filas = buenas; self.sucio = False; self.f = open(self.ruta, 'a')

    def add(self, k, clave, n=0, **kw):
        """v4 (hallazgo 10): un fallo de escritura (disco lleno, OSError) NO propaga: la fila queda en memoria (la logica del run sigue con la verdad en memoria, el barrido cancela igualmente), se cuenta en
        `fallos_escritura`, y se intenta volcar a un fichero aparte y a stderr. `_final` nunca da COMPLETE si hubo fallos."""
        eid = f'{k}|{clave}|{n}'
        if eid in self.eids: self.duplicadas += 1; return None
        row = dict(eid=eid, k=k, clave=clave, **kw); linea = json.dumps(row, sort_keys=True, default=str) + '\n'
        try:
            if self.sucio: self.f.write('\n'); self.f.flush(); self.sucio = False                       # v6 (hallazgo 6): tras un fallo de escritura la ultima linea pudo quedar a medias: se cierra con '\n' ANTES de la siguiente fila (si no, se concatenaria y se perderian las dos)
            self.sucio = True; self.f.write(linea); self.f.flush(); os.fsync(self.f.fileno()); self.sucio = False
        except (OSError, ValueError) as e:
            self.fallos_escritura += 1
            self.fallidos.add(eid)                                                                       # v13 (hallazgo 2): la fila queda en memoria pero NO consta en disco: nunca cuenta como evidencia
            try: print(f'LEDGER NO ESCRIBIBLE ({type(e).__name__}); fila: {linea.strip()}', file=sys.stderr, flush=True)
            except Exception: pass
            try:
                with open(self.ruta + '.fallback', 'a') as g: g.write(linea)
            except Exception: pass
        self.eids.add(eid); self.filas.append(row); return row

    def cerrar(self):
        try: self.f.close()
        except Exception: pass


def leer_ledger_solo_lectura(ruta):
    """v6 (hallazgo 7): filas validas (JSON con `eid`, sin duplicados, en orden) de un ledger SIN abrirlo en append ni reescribirlo (a diferencia de `Ledger`, que repara el fichero). Para informes sobre un run ya cerrado."""
    filas, vistos = [], set()
    if not os.path.exists(ruta): return filas
    with open(ruta, 'rb') as f:
        for linea in f.read().split(b'\n'):
            if not linea.strip(): continue
            try: r = json.loads(linea)
            except ValueError: continue
            if isinstance(r, dict) and 'eid' in r and r['eid'] not in vistos: vistos.add(r['eid']); filas.append(r)
    return filas


@dataclasses.dataclass
class Orden:
    clave: str
    slot: int = -1
    coin: str = ''
    tok: str = ''
    modo: str = 'lejos'
    precio: float = 0.0
    size: float = 0.0
    oid: str = None
    t_envio_ns: int = None
    t_ack_ns: int = None
    clase_post: str = None
    cancel_ok: bool = False
    matched: float = 0.0
    cerrada: bool = False
    motivo: str = None
    indeterminada: bool = False
    t_intencion_ns: int = None


def replay_estado(filas):
    """Reconstruye el estado de TODAS las ordenes a partir del ledger (fuente de verdad). Devuelve (ordenes{clave: Orden}, resumen)."""
    O = {}
    for r in filas:
        c = r.get('clave'); k = r.get('k')
        if k == 'intencion': O[c] = Orden(clave=c, slot=r['slot'], coin=r['coin'], tok=r['tok'], modo=r.get('modo', 'lejos'), precio=r['precio'], size=r['size'], oid=r.get('oid_local'), t_intencion_ns=r.get('t_decision_ns'))
        elif c in O:
            o = O[c]
            if k == 'post':
                o.t_envio_ns = r.get('t_send_ns'); o.t_ack_ns = r.get('t_ack_ns'); o.clase_post = r.get('clase')
                if r.get('oid'): o.oid = r['oid']
            elif k == 'cancel' and r.get('ok'): o.cancel_ok = True
            elif k == 'estado': o.matched = max(o.matched, float(r.get('matched') or 0.0))
            elif k == 'cerrada': o.cerrada = True; o.motivo = r.get('motivo'); o.matched = max(o.matched, float(r.get('size_matched') or 0.0)); o.indeterminada = bool(r.get('indeterminada'))
    gasto = round(sum(o.matched * o.precio for o in O.values()), 6)
    vivas = [o for o in O.values() if not o.cerrada]
    res = dict(n_intenciones=len(O), n_vivas=len(vivas), n_cerradas=sum(1 for o in O.values() if o.cerrada), gasto_fills_usd=gasto, n_fills=sum(1 for o in O.values() if o.matched > 1e-9), n_indeterminadas=sum(1 for o in O.values() if o.indeterminada))
    return O, res


# ------------------------------------------------------------------------------------------------ presupuesto duro
class Presupuesto:
    """Perdida dura. gasto = max(saldo_inicial - saldo_actual, coste de rellenos del ledger). Suelo = saldo_inicial - perdida_dura. Nunca permite un POST si, con TODAS las vivas rellenadas mas esta, se tocaria el suelo."""
    def __init__(self, cfg, saldo_inicial):
        exigir(saldo_inicial is not None and saldo_inicial > 0, 'saldo inicial ilegible: no se opera')
        exigir(saldo_inicial <= cfg.saldo_autorizado + 0.05, f'saldo {saldo_inicial} muy por encima de lo autorizado {cfg.saldo_autorizado}: wallet/monto no esperado')
        self.cfg = cfg; self.s0 = float(saldo_inicial); self.suelo = round(self.s0 - cfg.perdida_dura, 6); self.saldo = float(saldo_inicial); self.gasto_ledger = 0.0

    def actualizar(self, saldo=None, gasto_ledger=None):
        if saldo is not None: self.saldo = float(saldo)
        if gasto_ledger is not None: self.gasto_ledger = float(gasto_ledger)

    @property
    def gasto(self): return max(round(self.s0 - self.saldo, 6), self.gasto_ledger)

    def toca_suelo(self): return self.gasto >= self.cfg.perdida_dura - 1e-9 or self.saldo <= self.suelo + 1e-9

    def puede_enviar(self, n_vivas):
        """True si con n_vivas ya vivas + esta nueva, rellenar TODAS no llevaria a >= perdida_dura."""
        return n_vivas + 1 <= self.cfg.max_simultaneas and self.gasto + (n_vivas + 1) * self.cfg.coste_orden < self.cfg.perdida_dura + 1e-9


# ------------------------------------------------------------------------------------------------ anclas (cancel_evid del canal de usuario)
def leer_evid(patron):
    """v7 (hallazgo 10): UNICA lectura de los cancel_evid del canal de usuario. Tolera .gz truncado y ultima linea rota: devuelve (eventos_legibles, ilegibles) con ilegibles = [dict(fichero, error)] (NUNCA lanza). Las lineas JSON rotas se descartan (la cola de un fichero que se esta escribiendo es normal)."""
    ev = []; ileg = []
    for f in sorted(glob.glob(patron)):
        try:
            with (gzip.open(f, 'rt') if f.endswith('.gz') else open(f)) as fh:
                for l in fh:
                    try: r = json.loads(l)
                    except ValueError: continue
                    if isinstance(r, dict): ev.append(r)
        except (OSError, EOFError, zlib.error, UnicodeError) as e: ileg.append(dict(fichero=f, error=type(e).__name__))
    return ev, ileg


def anclas_de_eventos(ev, ledger_filas=None):
    """Anclas DIRECTAS validas: oid con `alta` + user_order PLACEMENT y CANCELLATION (mine) + cancel_try canceled. Misma definicion que plan_paquete_l.analiza. Devuelve (total, por_moneda) a partir de eventos YA leidos."""
    g = lambda e: e.get('oid')
    alta = {g(e) for e in ev if e.get('k') == 'alta'}; plc = {g(e) for e in ev if e.get('k') == 'user_order' and e.get('mine') and e.get('tipo') == 'PLACEMENT'}
    can = {g(e) for e in ev if e.get('k') == 'user_order' and e.get('mine') and e.get('tipo') == 'CANCELLATION'}; cct = {g(e) for e in ev if e.get('k') == 'cancel_try' and e.get('canceled')}
    validas = (alta & plc & can & cct) - {None}
    coin_de_clave = {r['clave']: r['coin'] for r in (ledger_filas or []) if r.get('k') == 'intencion'}; por = collections.Counter()
    for r in (ledger_filas or []):
        if r.get('k') == 'post' and r.get('oid') in validas: por[coin_de_clave.get(r['clave'], '?')] += 1
    return len(validas), dict(por)


def contar_anclas(patron_evid, ledger_filas=None):
    """(total, por_moneda) con UNA lectura de los ficheros (`leer_evid`). NO lanza `plan_paquete_l.analiza` (eso solo en el informe final)."""
    return anclas_de_eventos(leer_evid(patron_evid)[0], ledger_filas)


def faltan_anclas(cfg, total, por_moneda):
    """True si aun faltan anclas (objetivo total o minimo por moneda)."""
    if total < cfg.objetivo_anclas: return True
    return any(por_moneda.get(c, 0) < m for c, m in cfg.min_anclas_moneda.items())


def d_proc_stats(filas):
    """d_proc = t_send_ns - t_trig_rx_ns del PRIMER DELETE de cada orden (intento == 1) en ms y d_red = t_ack_ns - t_send_ns de las cancelaciones OK. v7 (hallazgo 4): los reintentos (bucle de pre-indice, backoffs) comparten el t_trig_rx del primer intento
    y NO son procesamiento: se reportan APARTE en `reintentos` (nunca mezclados en d_proc_ms). Percentiles."""
    import numpy as np
    can = [r for r in filas if r.get('k') == 'cancel' and r.get('t_trig_rx_ns') and r.get('t_send_ns')]
    dp = [(r['t_send_ns'] - r['t_trig_rx_ns']) / 1e6 for r in can if r.get('intento') == 1]
    rt = [(r['t_send_ns'] - r['t_trig_rx_ns']) / 1e6 for r in can if isinstance(r.get('intento'), int) and r['intento'] > 1]
    dr = [(r['t_ack_ns'] - r['t_send_ns']) / 1e6 for r in filas if r.get('k') == 'cancel' and r.get('ok') and r.get('t_ack_ns') and r.get('t_send_ns')]
    f = lambda v: dict(n=len(v)) if not v else dict(n=len(v), p50=float(np.percentile(v, 50)), p90=float(np.percentile(v, 90)), max=float(max(v)))
    return dict(d_proc_ms=f(dp), d_red_cancel_ms=f(dr), reintentos=dict(n=len(rt), t_send_menos_t_trig_ms=f(rt), nota='reintentos de DELETE (intento > 1): tiempo desde el disparo del PRIMER intento; NO es d_proc'))


# ------------------------------------------------------------------------------------------------ analisis de la mejora «bid sin nosotros» (fase B)
def bid_sin_nosotros_mejora(eventos):
    """Compara dos reglas sobre eventos de fase B donde NUESTRA orden estaba visible en el nivel L: cada evento = dict(L, bid, szb, r_restante (size - matched, del canal de usuario), nuestra_visible (True/False), bid_post_otros_bajo_L (verdad: el
    bid de OTROS tras nuestra salida cae bajo L)). Regla A (actual): dispara si bid <= L tras restar nuestra orden como si siempre estuviera visible entera (size). Regla B (mejora): resta SOLO la cantidad restante visible r_restante y solo si `nuestra_visible`.
    Devuelve precision/recall de cada una. Funcion pura (se alimenta con anclas del canal de usuario + libro ms)."""
    EPS = 0.011; res = {}
    for nombre, usa_r in (('A_size_entera', False), ('B_restante_visible', True)):
        tp = fp = fn = tn = 0
        for e in eventos:
            visible = e['nuestra_visible']; resta = (e['r_restante'] if visible else 0.0) if usa_r else e['size']
            otros = e['szb'] - resta
            fire = (e['bid'] < e['L'] - 1e-9) or (abs(e['bid'] - e['L']) < 1e-9 and otros <= EPS)
            real = bool(e['bid_post_otros_bajo_L'])
            if fire and real: tp += 1
            elif fire and not real: fp += 1
            elif not fire and real: fn += 1
            else: tn += 1
        res[nombre] = dict(tp=tp, fp=fp, fn=fn, tn=tn, precision=(tp / (tp + fp)) if tp + fp else None, recall=(tp / (tp + fn)) if tp + fn else None)
    return res


# ------------------------------------------------------------------------------------------------ verificacion de mercados contra gamma (en vez de suponer slug / orden Up-Down)
NOMBRE_MONEDA = {'BTC': 'bitcoin', 'ETH': 'ethereum', 'SOL': 'solana', 'XRP': 'xrp'}


def verificar_mercado_gamma(coin, ini, ev):
    """Valida UN evento de gamma contra lo que el paquete SUPONE y devuelve (ok, motivo, [tok_up, tok_down], neg_risk). Fail-closed: cualquier discrepancia => (False, motivo, None, None).
    Comprueba (v3: `active`, `acceptingOrders`, `closed` y `negRisk` presentes y booleanos, no se suponen): slug exacto `{coin}-updown-5m-{ini}`; 1 solo mercado; outcomes == {Up, Down} y se mapean A LOS TOKENS por etiqueta (no por posicion); endDate == ini+300 s (±1); el titulo nombra la moneda;
    activo, no cerrado y acepta ordenes; tick 0,01 y orderMinSize <= 5. El orden [Up, Down] que se devuelve es el verificado (outcomes[i] <-> clobTokenIds[i])."""
    slug = f'{coin.lower()}-updown-5m-{ini}'
    if not isinstance(ev, dict) or ev.get('slug') != slug: return False, 'slug_distinto', None, None
    ms = ev.get('markets') or []
    if len(ms) != 1: return False, f'n_mercados={len(ms)}', None, None
    m = ms[0]
    try:
        toks = json.loads(m['clobTokenIds']) if isinstance(m.get('clobTokenIds'), str) else list(m.get('clobTokenIds') or [])
        outs = json.loads(m['outcomes']) if isinstance(m.get('outcomes'), str) else list(m.get('outcomes') or [])
    except (ValueError, TypeError): return False, 'tokens_u_outcomes_ilegibles', None, None
    if len(toks) != 2 or len(outs) != 2 or sorted(str(o).strip().lower() for o in outs) != ['down', 'up']: return False, f'outcomes={outs}', None, None
    mp = {str(o).strip().lower(): str(t) for o, t in zip(outs, toks)}
    import datetime as dt
    try: fin = dt.datetime.fromisoformat(str(m.get('endDate') or ev.get('endDate')).replace('Z', '+00:00')).timestamp()
    except ValueError: return False, 'endDate_ilegible', None, None
    if abs(fin - (ini + 300)) > 1.0: return False, f'endDate={fin} != {ini + 300}', None, None
    if NOMBRE_MONEDA[coin] not in str(ev.get('title') or m.get('question') or '').lower(): return False, 'titulo_sin_moneda', None, None
    for campo in ('active', 'acceptingOrders', 'closed', 'negRisk'):                       # v3 (hallazgo 10): cada campo debe venir PRESENTE y booleano; ausente/None/'true' (str) => rechazo (antes: ausente = ok)
        if not isinstance(m.get(campo), bool): return False, f'campo_{campo}_ausente_o_no_booleano', None, None
    if m['closed'] or not m['active'] or not m['acceptingOrders']: return False, 'no_acepta_ordenes', None, None
    try:
        if abs(float(m.get('orderPriceMinTickSize')) - 0.01) > 1e-9 or float(m.get('orderMinSize')) > 5.0 + 1e-9: return False, 'tick_o_minsize', None, None
    except (TypeError, ValueError): return False, 'tick_o_minsize_ilegible', None, None
    return True, 'ok', [mp['up'], mp['down']], m['negRisk']


# ------------------------------------------------------------------------------------------------ lectura incremental del canal de usuario (fills PUSH)
class EvidTail:
    """Lee SOLO las lineas nuevas de los cancel_evid_*.jsonl (el canal de usuario del CLOB ya los escribe) y devuelve {oid_en_minusculas: matched} de NUESTRAS ordenes: user_order con size_matched>0 o user_trade con size>0
    (status MATCHED/MINED/CONFIRMED) atribuido a un oid propio. Local (sin red), barato (offset por fichero); una linea parcial al final se espera al siguiente sondeo; .gz rotados se ignoran."""
    def __init__(self, patron): self.patron = patron; self.off = {}; self.buf = {}; self.fills = {}; self.filas_leidas = 0

    def sondear(self):
        for f in sorted(glob.glob(self.patron)):
            if f.endswith('.gz'): continue
            try: sz = os.path.getsize(f)
            except OSError: continue
            o = self.off.get(f, 0)
            if sz < o: o = 0; self.buf[f] = b''                                     # truncado/rotado
            if sz == o: continue
            try:
                with open(f, 'rb') as fh: fh.seek(o); datos = fh.read(sz - o)
            except OSError: continue
            self.off[f] = o + len(datos); txt = self.buf.get(f, b'') + datos; ult = txt.rfind(b'\n')
            if ult < 0: self.buf[f] = txt; continue
            self.buf[f] = txt[ult + 1:]
            for ln in txt[:ult].split(b'\n'):
                try: r = json.loads(ln)
                except ValueError: continue
                self.filas_leidas += 1; self._fila(r)
        return dict(self.fills)

    def _fila(self, r):
        if not isinstance(r, dict): return
        oid = str(r.get('oid') or '').lower()
        if not oid: return
        if r.get('k') == 'user_order' and r.get('mine') and (r.get('size_matched') or 0) > 1e-9: self.fills[oid] = max(self.fills.get(oid, 0.0), float(r['size_matched']))
        elif r.get('k') == 'user_trade' and (r.get('size') or 0) > 1e-9 and str(r.get('status') or '').upper() in ('MATCHED', 'MINED', 'CONFIRMED'): self.fills[oid] = max(self.fills.get(oid, 0.0), float(r['size']))


# ------------------------------------------------------------------------------------------------ relojes local vs exchange (medidos, no supuestos)
def reloj_stats(evid_filas):
    """Diferencias entre el reloj LOCAL (time.time_ns, alineado a monotonic) y el del EXCHANGE, a partir de las filas del canal de usuario, por oid propio:
      place_ex_menos_envio_ms = ts_ex(PLACEMENT) - t_envio_local(alta)      (>= 0 si los relojes coinciden; = offset + latencia de ida + procesado)
      place_recv_menos_ex_ms  = t_recepcion_local(PLACEMENT) - ts_ex        (offset + latencia de vuelta del WS)
      cancel_ex_menos_pre_ms  = ts_ex(CANCELLATION) - t_pre_local(cancel_try canceled)
      cancel_recv_menos_ex_ms = t_recepcion_local(CANCELLATION) - ts_ex
    No separa offset de latencia por si solas (solo el RTT simetrico lo haria): se publican las 4 y la suma ida+vuelta = place_recv - envio (= RTT local, sin offset)."""
    import numpy as np
    alta = {}; cpre = {}
    for e in evid_filas:
        if e.get('k') == 'alta' and e.get('oid'): alta[str(e['oid']).lower()] = e.get('t_envio_ms')
        elif e.get('k') == 'cancel_try' and e.get('canceled') and e.get('oid'): cpre.setdefault(str(e['oid']).lower(), e.get('t_pre_ms'))
    d = collections.defaultdict(list)
    for e in evid_filas:
        if e.get('k') != 'user_order' or not e.get('mine') or e.get('ts_ex_ms') is None: continue
        oid = str(e.get('oid') or '').lower(); tipo = e.get('tipo'); ex = e['ts_ex_ms']; rv = e.get('t_recv_ms')
        if tipo == 'PLACEMENT':
            if alta.get(oid) is not None: d['place_ex_menos_envio_ms'].append(ex - alta[oid])
            if rv is not None: d['place_recv_menos_ex_ms'].append(rv - ex)
            if alta.get(oid) is not None and rv is not None: d['rtt_local_envio_a_recepcion_placement_ms'].append(rv - alta[oid])
        elif tipo == 'CANCELLATION':
            if cpre.get(oid) is not None: d['cancel_ex_menos_pre_ms'].append(ex - cpre[oid])
            if rv is not None: d['cancel_recv_menos_ex_ms'].append(rv - ex)
    f = lambda v: dict(n=len(v)) if not v else dict(n=len(v), p50=float(np.percentile(v, 50)), p90=float(np.percentile(v, 90)), min=float(min(v)), max=float(max(v)))
    return {k: f(v) for k, v in d.items()}


# ------------------------------------------------------------------------------------------------ saldo con reintentos y validacion (fail-closed)
def leer_saldo_robusto(fn, reintentos, backoff, dormir, maximo=None):
    """Lee el saldo (RPC Polygon) hasta `reintentos` veces con backoff. Una lectura valida es un float finito >= 0 (y <= maximo si se da: un saldo imposiblemente alto = lectura de otra wallet/ruido). None si todas fallan."""
    import math
    for i in range(max(1, reintentos)):
        try: v = fn()
        except Exception: v = None
        if isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v) and v >= 0 and (maximo is None or v <= maximo): return float(v)
        if i < reintentos - 1: dormir(backoff[min(i, len(backoff) - 1)])
    return None


# ------------------------------------------------------------------------------------------------ posiciones residuales (fase B)
def residuales(filas):
    """Posiciones que quedan tras el run: por orden con size_matched > 0 (fase A o B): token, cantidad, coste a 0,01 y modo. Una posicion NO se puede eliminar sin vender; se contabiliza y se acota (cfg.fase_b_*)."""
    O, _ = replay_estado(filas); out = []
    for o in O.values():
        if o.matched > 1e-9: out.append(dict(clave=o.clave, coin=o.coin, tok=o.tok, cantidad=o.matched, precio=o.precio, coste_usd=round(o.matched * o.precio, 6), modo=o.modo))
    return out


def valor_residual(res, ganador_por_tok):
    """Valor final de las posiciones residuales con el desenlace OFICIAL (dict tok -> True/False/None). None = sin desenlace (missing != 0). Ganadora: cantidad x 1 $ reclamable por redencion MANUAL (este paquete no firma redenciones)."""
    out = []
    for r in res:
        g = ganador_por_tok.get(r['tok']); out.append(dict(r, ganador=g, valor_usd=(r['cantidad'] if g else 0.0) if g is not None else None, pnl_usd=((r['cantidad'] if g else 0.0) - r['coste_usd']) if g is not None else None))
    return out
