"""mercado_version.py -- SELECTOR UNICO de version de firma POR MERCADO + carga AISLADA del SDK py_clob_client_v2 1.2.2 + hash local del orderID (26-Nov, OK Javi; Polymarket Protocol V2 por mercado).

COPIA IDENTICA en dos sitios (un test compara su sha256): paquete_l/vendor/mercado_version.py (la carga `pl_core.cargar_vendor`, con hash) y <b-k>/mercado_version.py. NO es codigo de produccion: ningun ejecutor live lo importa.
Hechos medidos 26-Nov (solo lectura): SOL/XRP/BNB/DOGE/HYPE 5m y 15m son `version:"v2"` en gamma (`version`, `positionIds`) y `"v":"v2"` en CLOB `/clob-markets/{conditionId}`; BTC/ETH son `v1` (sin `positionIds`).
  v2 -> se firma contra ExchangeV3 0xe3333700cA9d93003F00f0F71f8515005F6c00Aa, dominio "Polymarket CTF Exchange" version "3", con `position_id` (OrderArgsV2(position_id=...)); el SDK 1.0.1 de produccion NO lo conoce
        (firma contra el exchange v2 y el servidor responde `400 invalid POLY_1271 signature`).
  v1 -> comportamiento anterior: ExchangeV2 0xE111...B (o neg-risk 0xe2222...) dominio version "2", con token_id.
FAIL-CLOSED: version ausente / ilegible / distinta entre gamma, evento y CLOB / positionIds != clobTokenIds / token no perteneciente al mercado / v2 con negRisk => ErrVersion (NO se firma). Cache con caducidad corta (la migracion sigue en curso).
AISLAMIENTO del SDK: `cargar_sdk(raiz, hashes)` instala un buscador de modulos que SOLO sirve `py_clob_client_v2*` desde `raiz` ejecutando EXACTAMENTE los bytes cuyo sha256 figura en `hashes` (sin .pyc, sin sys.path); si ya hay un `py_clob_client_v2`
cargado desde otro sitio (p. ej. el 1.0.1 de site-packages) => ErrVersion. Solo afecta al proceso que lo llama: nada se instala en ningun venv y nada llega a produccion."""
import hashlib, importlib.abc, importlib.machinery, importlib.util, os, sys, threading, time
from dataclasses import dataclass

GAMMA = 'https://gamma-api.polymarket.com'
CLOB = 'https://clob.polymarket.com'
EXCHANGE_V3 = '0xe3333700cA9d93003F00f0F71f8515005F6c00Aa'
EXCHANGE_V2 = '0xE111180000d2663C0091e4f400237545B87B996B'
NEG_RISK_EXCHANGE_V2 = '0xe2222d279d744050d28e00520010520000310F59'
DOMINIO_V1, DOMINIO_V2 = '2', '3'          # version del dominio EIP-712 de cada familia de mercado (v1 -> "2", v2 -> "3")
SDK = 'py_clob_client_v2'
SDK_VERSION = '1.2.2'
TTL_S = 60.0


class ErrVersion(Exception):
    """No se puede decidir (o no coincide) la version de firma del mercado: NO se firma."""


@dataclass(frozen=True)
class InfoMercado:
    version: str                 # 'v1' | 'v2'
    condition_id: str
    tokens: tuple                # (Up, Down) tal como los da gamma (clobTokenIds == positionIds en v2)
    neg_risk: bool
    exchange: str                # verifyingContract con el que se firma
    dominio_version: str         # '2' | '3'
    usa_position_id: bool

    def a_dict(self): return dict(version=self.version, condition_id=self.condition_id, exchange=self.exchange, dominio_version=self.dominio_version, usa_position_id=self.usa_position_id, neg_risk=self.neg_risk)


def _http_get(url, params, timeout=2.5):
    import requests
    r = requests.get(url, params=params, timeout=timeout); r.raise_for_status(); return r.json()


def _lista_str(v, que):
    import json
    if isinstance(v, str):
        try: v = json.loads(v)
        except ValueError: raise ErrVersion(f'{que}_ilegible')
    if not isinstance(v, (list, tuple)) or len(v) != 2 or not all(isinstance(x, str) and x.strip() for x in v): raise ErrVersion(f'{que}_no_son_2_ids')
    return tuple(x.strip() for x in v)


def _ver(v, que):
    s = str(v).strip().lower() if isinstance(v, str) else ''
    if s not in ('v1', 'v2'): raise ErrVersion(f'{que}_version_ausente_o_desconocida:{v!r}')
    return s


def info_de_gamma(m, ev=None):
    """Version declarada por GAMMA para un mercado (dict de `markets[]`) -> InfoMercado. `ev` (el evento) es opcional: si trae `version` debe coincidir."""
    if not isinstance(m, dict): raise ErrVersion('mercado_gamma_no_es_dict')
    v = _ver(m.get('version'), 'gamma')
    if isinstance(ev, dict) and ev.get('version') is not None and _ver(ev.get('version'), 'gamma_evento') != v: raise ErrVersion('gamma_evento_y_mercado_discrepan')
    cond = m.get('conditionId')
    if not isinstance(cond, str) or not cond.startswith('0x') or len(cond) < 10: raise ErrVersion('conditionId_ausente')
    toks = _lista_str(m.get('clobTokenIds'), 'clobTokenIds'); nr = m.get('negRisk')
    if not isinstance(nr, bool): raise ErrVersion('negRisk_ausente_o_no_booleano')
    pos = m.get('positionIds')
    if v == 'v2':
        if pos is None: raise ErrVersion('v2_sin_positionIds')
        if _lista_str(pos, 'positionIds') != toks: raise ErrVersion('positionIds_distintos_de_clobTokenIds')
        if nr: raise ErrVersion('v2_con_negRisk_no_soportado')
        return InfoMercado('v2', cond, toks, False, EXCHANGE_V3, DOMINIO_V2, True)
    if pos not in (None, [], '', '[]') and _lista_str(pos, 'positionIds') != toks: raise ErrVersion('v1_con_positionIds_distintos')
    return InfoMercado('v1', cond, toks, nr, NEG_RISK_EXCHANGE_V2 if nr else EXCHANGE_V2, DOMINIO_V1, False)


def verificar_clob(info, cm):
    """Contrasta con CLOB `/clob-markets/{cond}`: `v` == version de gamma y los tokens `t[].t` == los de gamma."""
    if not isinstance(cm, dict): raise ErrVersion('clob_markets_ilegible')
    if _ver(cm.get('v'), 'clob') != info.version: raise ErrVersion(f'clob_v={cm.get("v")!r}_difiere_de_gamma={info.version}')
    c = cm.get('c')
    if isinstance(c, str) and c.lower() != info.condition_id.lower(): raise ErrVersion('clob_conditionId_distinto')
    t = cm.get('t')
    if not isinstance(t, list) or not all(isinstance(x, dict) and isinstance(x.get('t'), str) for x in t) or {x['t'] for x in t} != set(info.tokens): raise ErrVersion('clob_tokens_distintos_de_gamma')
    return info


def comprobar_libro(info, libro):
    """`/book` de un token: v2 => el libro trae `version`=='v2'; v1 => `version` ausente o 'v1'. Devuelve (ok, motivo). Solo lectura (preflight)."""
    if not isinstance(libro, dict): return False, 'libro_ilegible'
    vb = libro.get('version'); vb = vb.strip().lower() if isinstance(vb, str) else vb
    if info.version == 'v2': return (vb == 'v2'), f'libro.version={vb!r}'
    return (vb in (None, 'v1')), f'libro.version={vb!r}'


class Selector:
    """Cache (TTL corto) de InfoMercado por conditionId y por token. `get(url, params)` inyectable (tests). Hilo-seguro."""
    def __init__(self, get=None, ttl_s=TTL_S, reloj=time.time):
        self.get = get or _http_get; self.ttl = ttl_s; self.reloj = reloj; self._c = {}; self._por_tok = {}; self._lk = threading.Lock()

    def _vigente(self, t0): return self.reloj() - t0 < self.ttl

    def _guardar(self, info):
        t = self.reloj()
        with self._lk:
            self._c[info.condition_id] = (t, info)
            for k in info.tokens: self._por_tok[k] = info.condition_id

    def resolver(self, m, ev=None):
        """Mercado de gamma ya leido -> InfoMercado verificado ademas contra CLOB. Cualquier fallo => ErrVersion (la excepcion de red tambien: fail-closed)."""
        info = info_de_gamma(m, ev)
        with self._lk: c = self._c.get(info.condition_id)
        if c and c[1] == info and self._vigente(c[0]): return info
        try: cm = self.get(f'{CLOB}/clob-markets/{info.condition_id}', None)
        except Exception as e: raise ErrVersion(f'clob_markets_fallo:{type(e).__name__}')
        verificar_clob(info, cm); self._guardar(info); return info

    def por_token(self, tok, refrescar=False):
        """InfoMercado del token (cache vigente; si no, o con `refrescar=True`, gamma `/markets?clob_token_ids=` + CLOB). Token desconocido, sin mercado o ambiguo => ErrVersion.
        `refrescar=True` lo usa quien prepara el envio FUERA del camino caliente (para que la firma encuentre la cache vigente y no haga red)."""
        tok = str(tok).strip()
        with self._lk: cond = self._por_tok.get(tok); c = self._c.get(cond) if cond else None
        if c and not refrescar and self._vigente(c[0]): return c[1]
        try: r = self.get(f'{GAMMA}/markets', {'clob_token_ids': tok})
        except Exception as e: raise ErrVersion(f'gamma_por_token_fallo:{type(e).__name__}')
        if not isinstance(r, list) or len(r) != 1: raise ErrVersion(f'gamma_por_token:{len(r) if isinstance(r, list) else type(r).__name__}_mercados')
        if refrescar: self.invalidar_cond(str(r[0].get('conditionId')))
        info = self.resolver(r[0])
        if tok not in info.tokens: raise ErrVersion('token_no_pertenece_al_mercado')
        return info

    def invalidar_cond(self, cond):
        with self._lk: self._c.pop(cond, None)

    def invalidar(self):
        with self._lk: self._c.clear(); self._por_tok.clear()


_GLOBAL = [None]


def selector_global(get=None, ttl_s=None):
    """Instancia unica del proceso (la comparten el escaneo de mercados y la firma). `get`/`ttl_s` solo se usan al crearla (tests la sustituyen con `_GLOBAL[0] = Selector(...)`)."""
    if _GLOBAL[0] is None: _GLOBAL[0] = Selector(get=get, ttl_s=(TTL_S if ttl_s is None else ttl_s))
    return _GLOBAL[0]


def args_orden(info, OrderArgsV2, tok, price, size, side, expiration=None):
    """Argumentos de orden segun la version del mercado: v2 -> position_id (ExchangeV3); v1 -> token_id."""
    tok = str(tok)
    if tok not in info.tokens: raise ErrVersion('token_no_pertenece_al_mercado')
    kw = dict(price=price, size=size, side=side)
    if expiration is not None: kw['expiration'] = expiration
    return OrderArgsV2(position_id=tok, **kw) if info.usa_position_id else OrderArgsV2(token_id=tok, **kw)


def hash_orden(signed, info):
    """orderID = hash EIP-712 local (sin la firma) de una orden ya firmada, con el contrato y la version de dominio de SU mercado (v2 -> ExchangeV3 / dominio "3"; v1 -> exchange v2 o neg-risk v2 / "2")."""
    import dataclasses
    from py_clob_client_v2.order_utils.exchange_order_builder_v2 import ExchangeOrderBuilderV2
    from py_clob_client_v2.order_utils.model.order_data_v2 import OrderV2
    kw = {} if info.dominio_version == DOMINIO_V1 else dict(domain_version=info.dominio_version)
    b = ExchangeOrderBuilderV2(info.exchange, 137, None, **kw)
    campos = {k: v for k, v in dataclasses.asdict(signed).items() if k != 'signature'}
    return b.build_order_hash(b.build_order_typed_data(OrderV2(**campos)))


def typed_data(signed, info):
    """Typed data EIP-712 de la orden (para tests/preflight): domain.verifyingContract y domain.version de SU mercado."""
    import dataclasses
    from py_clob_client_v2.order_utils.exchange_order_builder_v2 import ExchangeOrderBuilderV2
    from py_clob_client_v2.order_utils.model.order_data_v2 import OrderV2
    kw = {} if info.dominio_version == DOMINIO_V1 else dict(domain_version=info.dominio_version)
    b = ExchangeOrderBuilderV2(info.exchange, 137, None, **kw)
    return b.build_order_typed_data(OrderV2(**{k: v for k, v in dataclasses.asdict(signed).items() if k != 'signature'}))


# ------------------------------------------------------------------------------------------------ SDK 1.2.2 aislado
_SDK_INSTALADO = [None]


class _Cargador(importlib.machinery.SourceFileLoader):
    def __init__(self, fullname, path, hashes):
        super().__init__(fullname, path); self._h = hashes

    def get_code(self, fullname):                                              # EXACTAMENTE los bytes verificados; sin .pyc (no hay ventana entre verificar y ejecutar)
        p = self.get_filename(fullname)
        with open(p, 'rb') as f: datos = f.read()
        if hashlib.sha256(datos).hexdigest() != self._h.get(p): raise ImportError(f'{fullname}: sha256 distinto al fijado: NO cargo')
        return self.source_to_code(datos, p)


class _Buscador(importlib.abc.MetaPathFinder):
    def __init__(self, raiz, hashes): self.raiz = raiz; self.h = hashes

    def find_spec(self, fullname, path=None, target=None):
        if fullname != SDK and not fullname.startswith(SDK + '.'): return None
        rel = os.path.join(self.raiz, *fullname.split('.'))
        for cand, pkg in ((os.path.join(rel, '__init__.py'), True), (rel + '.py', False)):
            if os.path.isfile(cand):
                if cand not in self.h: raise ImportError(f'{fullname}: fichero sin hash en el SDK vendorizado: NO cargo')
                return importlib.util.spec_from_file_location(fullname, cand, loader=_Cargador(fullname, cand, self.h), submodule_search_locations=([os.path.dirname(cand)] if pkg else None))
        raise ModuleNotFoundError(f'{fullname}: no existe en el SDK vendorizado (no se cae al de site-packages)', name=fullname)


def cargar_sdk(raiz, hashes):
    """Instala el SDK vendorizado (`raiz`/py_clob_client_v2/**, sha256 en `hashes` = {ruta relativa a `raiz`: sha256}). Verifica TODOS los ficheros ANTES de importar y que no sobren .py sin hash. Idempotente.
    ErrVersion si: falta/sobra/difiere un fichero; ya hay un `py_clob_client_v2` cargado desde otro sitio; o el modulo cargado no es el 1.2.2 (sin ExchangeV3 / sin position_id)."""
    raiz = os.path.realpath(raiz); h = {os.path.join(raiz, k): v for k, v in hashes.items() if k.startswith(SDK + '/')}
    if _SDK_INSTALADO[0] == raiz and SDK in sys.modules: return sys.modules[SDK]
    if not h: raise ErrVersion('sin hashes del SDK')
    previo = sys.modules.get(SDK)
    if previo is not None and not str(getattr(previo, '__file__', '')).startswith(raiz + os.sep): raise ErrVersion(f'{SDK} ya esta cargado desde {getattr(previo, "__file__", "?")}: NO instalo el vendorizado (mezcla de SDK)')
    for p, esperado in h.items():
        try: ok = hashlib.sha256(open(p, 'rb').read()).hexdigest() == esperado
        except OSError: ok = False
        if not ok: raise ErrVersion(f'SDK vendorizado alterado o incompleto: {os.path.relpath(p, raiz)}')
    sobran = [os.path.relpath(os.path.join(d, f), raiz) for d, _, fs in os.walk(os.path.join(raiz, SDK)) for f in fs if f.endswith('.py') and os.path.join(d, f) not in h]
    if sobran: raise ErrVersion(f'SDK vendorizado con .py sin hash: {sobran[:3]}')
    if previo is None: sys.meta_path.insert(0, _Buscador(raiz, h))
    m = __import__(SDK + '.order_builder.helpers', fromlist=['x']); import py_clob_client_v2 as sdk
    from py_clob_client_v2.config import get_contract_config
    if get_contract_config(137).exchange_v3.lower() != EXCHANGE_V3.lower() or not hasattr(m, '_resolve_order_routing'): raise ErrVersion('el SDK cargado no es el 1.2.2 (sin ExchangeV3 / position_id)')
    from py_clob_client_v2.client import ClobClient
    ClobClient._resolve_transactions_hashes = lambda self, response: response               # 1.2.2 sondea hasta 30 s `tradeIDs` DENTRO de post_order cuando la orden casa: el 1.0.1 no lo hacia (la latencia del POST no puede depender de eso); las fills se leen por canal de usuario/get_order
    _SDK_INSTALADO[0] = raiz; return sdk
