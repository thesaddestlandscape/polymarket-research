#!/usr/bin/env python3
"""regenerar_vendor.py -- ACCION EXPLICITA y puntual: (re)genera vendor/ y VENDOR_HASHES.json a partir del codigo ya revisado de la Sonda1 (dev, SOLO LECTURA) y de main (live_trade.py, SOLO LECTURA como TEXTO: nunca se importa).
Despues de esto el paquete NO importa nada de dev ni de main: carga solo vendor/ con `pl_core.cargar_vendor` (que compara el sha256 de los BYTES que va a ejecutar con VENDOR_HASHES.json).
  cancel_evidencia.py <- sonda1/p3_cancel_registro/cancel_evidencia.py   (copia byte a byte: canal de USUARIO, alta/cancel_try, gate_envio, adjuntar_env)
  plan_paquete_l.py   <- l_real_11nov/plan_paquete_l.py                  (copia byte a byte: `analiza`)
  envio_real.py       <- EXTRACTO de sonda1/sonda1.py (ast: class EnvioReal + _con_timeout + _ahora + log + ErrCrudo + constantes; lineas sin editar; solo cambia la CABECERA: ya no toca sys.path, `vendor_main` lo
                         resuelve `cargar_vendor` desde sys.modules)
  vendor_main.py      <- GENERADO (hallazgo 1 del /code-review 12-Nov): MINIMO sin `live_trade`, sin `polygon_rpc`, sin REPO ni variables de entorno, sin leer data/live/.env:
                         * hash_orden                                  VERBATIM (ast) de sonda1/vendor_main.py
                         * _clob_redondeo_parcheado + _parchear_redondeo_clob  VERBATIM (ast, TEXTO) de live_trade.py (codigo de seguridad live; se copia el texto, no se importa el modulo)
                         * cliente_dedicado / saldo_onchain            ESCRITOS aqui (PLANTILLA_MANUAL, para revisar): solo credenciales de la wallet DEDICADA en ruta fija, comprobacion exacta de la wallet
Los hashes de origen y de CADA segmento copiado quedan en VENDOR_HASHES.json (deriva de un segmento de origen = aviso en --verificar; no falla: el paquete usa la copia, no el origen).
`--verificar` comprueba solo contra los hashes (y informa de deriva).
v7: este generador es OFFLINE (nunca lo carga `cargar_vendor` ni corre en el envio real/preflight); sus `assert` pasaron a `raise`. `plan_paquete_l.plan()` (copia byte a byte, conserva un `assert`) es solo el GENERADOR de planes (`--plan`): el paquete solo usa `analiza` y un test comprueba que ningun modulo del envio llama a `plan`."""
import os, sys, ast, json, hashlib, shutil, time
HERE = os.path.dirname(os.path.abspath(__file__)) + '/'
S = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/'
LIVE_TRADE = '/root/polymarket-research/live_trade.py'
sha = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
shat = lambda t: hashlib.sha256(t.encode('utf-8')).hexdigest()
COPIAS = {'cancel_evidencia.py': S + 'p3_cancel_registro/cancel_evidencia.py', 'plan_paquete_l.py': HERE + '../../l_real_11nov/plan_paquete_l.py'}

CAB_VENDOR_MAIN = '''"""vendor_main.py -- GENERADO por regenerar_vendor.py (NO editar a mano: cambia el sha y el paquete se niega a cargarlo). MINIMO que necesita vendor/envio_real.py.
  hash_orden                                       VERBATIM de sonda1/vendor_main.py        (segmento y sha en VENDOR_HASHES.json)
  _clob_redondeo_parcheado, _parchear_redondeo_clob  VERBATIM (texto) de live_trade.py        (codigo de seguridad live; el modulo live_trade NUNCA se importa)
  cliente_dedicado, saldo_onchain                  escritos para el paquete (abajo): sin live_trade, sin polygon_rpc, sin REPO ni variables de entorno; los .env de produccion se abren SOLO para comparar y negarse (hallazgo 8).
"""
import dataclasses, json, os, stat, sys, time

ENV_DEDICADA = "/root/.secrets/experimento_pares.env"        # ruta FIJA: no sale del entorno ni de argumentos de linea de comandos
WALLET_DEDICADA = "0x659a40FF9920fEBc5a66836213040924343d297F"
ENVS_PRODUCCION = ("/root/polymarket-research/data/live/.env", "/root/polymarket-research/.env")     # SOLO comparacion (hallazgo 8); el 1o obligatorio
CLOB = "https://clob.polymarket.com"
PUSD = "0xC011a7E12a19f7B1f670d46F03B03f3342E82DFB"          # colateral (de sonda1/vendor_main.py)
RPCS = ("https://polygon-bor-rpc.publicnode.com", "https://polygon.drpc.org", "https://1rpc.io/matic")     # grupo 'latest' de polygon_rpc (12-Nov); lista FIJA, no se lee ningun JSON
RPC_MIN_VALIDAS = 2                                          # v7 (hallazgo 9): respuestas validas MINIMAS para dar un saldo (se toma el minimo); con menos => None


'''

PLANTILLA_MANUAL = '''

def cliente_dedicado(ruta=ENV_DEDICADA, wallet_esperada=WALLET_DEDICADA, _clob=None, _prod=ENVS_PRODUCCION):
    """Cliente CLOB V2 de la wallet DEDICADA (POLY_1271, funder = wallet de deposito). Fail-closed (sys.exit) si: la ruta (tras resolver symlinks) es una de produccion; el fichero no es regular o es legible por
    grupo/otros; faltan credenciales; la wallet de deposito NO es EXACTAMENTE la autorizada; o CUALQUIERA de POLY_PRIVATE_KEY / POLY_API_KEY / POLY_DEPOSIT_WALLET coincide con las de produccion.
    DECISION (2o /code-review, hallazgo 8; restaura la guarda de la Sonda1): los .env de produccion (`_prod`) se ABREN SOLO para COMPARAR y negarse a arrancar; sus valores jamas se usan ni se guardan ni se escriben. `data/live/.env` es
    OBLIGATORIO y legible (si no se puede comprobar => no arranco, como la Sonda1); el `.env` principal se compara ademas si existe. No importa live_trade: la unica clave que entra en el cliente es la de `ruta`.
    (`ruta`/`wallet_esperada`/`_clob`/`_prod` existen para los tests; el paquete llama sin argumentos.)"""
    from dotenv import dotenv_values
    ruta = str(ruta); norm = lambda x: str(x or "").strip().lower().removeprefix("0x")
    real = os.path.realpath(ruta); prod_reales = [os.path.realpath(p) for p in _prod]
    if real in prod_reales or os.path.basename(real) == ".env" or "data/live" in real:
        sys.exit(f"{ruta} (-> {real}) es/parece la credencial de produccion: no arranco")
    try:
        st = os.stat(real)
    except OSError as e:
        sys.exit(f"{ruta}: no se puede leer ({type(e).__name__}): no arranco")
    if not stat.S_ISREG(st.st_mode) or st.st_mode & 0o077:
        sys.exit(f"{ruta}: debe ser un fichero regular con permisos 600 (modo {oct(st.st_mode & 0o7777)}): no arranco")
    c = dotenv_values(real)
    faltan = [k for k in ("POLY_PRIVATE_KEY", "POLY_DEPOSIT_WALLET", "POLY_API_KEY", "POLY_API_SECRET", "POLY_API_PASSPHRASE") if not c.get(k)]
    if faltan:
        sys.exit(f"{ruta}: faltan {faltan}")
    if norm(c["POLY_DEPOSIT_WALLET"]) != norm(wallet_esperada):
        sys.exit("la wallet de deposito del fichero NO es la wallet dedicada autorizada: no arranco")
    for i, pp in enumerate(_prod):                                  # el primero es OBLIGATORIO; los demas solo si existen
        if i > 0 and not os.path.exists(pp):
            continue
        live = dotenv_values(pp) if os.path.exists(pp) else {}
        if not live.get("POLY_DEPOSIT_WALLET") or not live.get("POLY_API_KEY") or not live.get("POLY_PRIVATE_KEY"):
            sys.exit(f"no se puede comprobar que la wallet dedicada no sea la de produccion ({pp} ilegible o incompleto): no arranco")
        if any(norm(c[k]) == norm(live[k]) for k in ("POLY_DEPOSIT_WALLET", "POLY_API_KEY", "POLY_PRIVATE_KEY")):
            sys.exit(f"{ruta} comparte credenciales con {pp}: no arranco")
    _parchear_redondeo_clob()
    if _clob is None:
        from py_clob_client_v2 import ClobClient
        _clob = ClobClient
    from py_clob_client_v2 import ApiCreds
    from py_clob_client_v2.constants import POLYGON
    pk = c["POLY_PRIVATE_KEY"] if c["POLY_PRIVATE_KEY"].lower().startswith("0x") else "0x" + c["POLY_PRIVATE_KEY"]
    return _clob(CLOB, key=pk, chain_id=POLYGON,
                 creds=ApiCreds(api_key=c["POLY_API_KEY"], api_secret=c["POLY_API_SECRET"], api_passphrase=c["POLY_API_PASSPHRASE"]),
                 signature_type=3, funder=c["POLY_DEPOSIT_WALLET"])


def saldo_onchain(wallet, _post=None):
    """pUSD on-chain de la wallet de deposito (balanceOf, eth_call 'latest') por RPC publico. Las ordenes abiertas NO lo reducen (solo el casado). v7 (5o /code-review, hallazgo 9): exige SIEMPRE >= RPC_MIN_VALIDAS (2) respuestas validas de RPC distintos de la lista fija
    y devuelve el MINIMO (un nodo atrasado devolveria un saldo MAS ALTO y ocultaria un relleno: el minimo es el lado conservador). Con UNA sola respuesta valida (o ninguna) => None (ilegible: quien llama no envia / bloquea): una lectura sin contrastar no vale.
    Por que NO `polygon_rpc.llamar` (regla del repo: Polygon solo via polygon_rpc.py): se detiene en la PRIMERA respuesta valida (justo lo que se prohibe aqui), importa `requests` y relee un JSON fuera del paquete, incompatible con `python -I` + vendor con hash;
    RPCS replica su grupo 'latest' (un test lo compara con `polygon_rpc._POR_DEFECTO`)."""
    w = str(wallet or "").lower()
    if not (w.startswith("0x") and len(w) == 42):
        return None
    try:
        int(w[2:], 16)
    except ValueError:
        return None
    if _post is None:
        import requests
        _post = lambda url, js: requests.post(url, json=js, timeout=(2, 3)).json()
    js = {"jsonrpc": "2.0", "id": 1, "method": "eth_call", "params": [{"to": PUSD, "data": "0x70a08231" + w[2:].rjust(64, "0")}, "latest"]}
    vals, t_fin = [], time.monotonic() + 6.0
    for url in RPCS:
        if time.monotonic() > t_fin:
            break
        try:
            res = _post(url, js).get("result")
            if isinstance(res, str) and res.startswith("0x") and 3 <= len(res) <= 66:
                vals.append(int(res, 16) / 1e6)
        except Exception:
            continue
        if len(vals) >= RPC_MIN_VALIDAS:
            break
    return min(vals) if len(vals) >= RPC_MIN_VALIDAS else None
'''


def segmentos(path, nombres_f=(), nombres_a=()):
    """(lineno, end, texto) de las funciones y asignaciones simples pedidas, tomadas con ast del TEXTO del fichero (sin importarlo)."""
    src = open(path, encoding='utf-8').read(); lines = src.split('\n'); out = []
    for n in ast.parse(src).body:
        seg = '\n'.join(lines[n.lineno - 1:n.end_lineno])
        if isinstance(n, ast.FunctionDef) and n.name in nombres_f: out.append((n.lineno, n.end_lineno, seg))
        elif isinstance(n, ast.Assign) and len(n.targets) == 1 and ast.unparse(n.targets[0]).strip('()') in nombres_a: out.append((n.lineno, n.end_lineno, seg))
    return out


def extracto_envio():
    src = open(S + 'sonda1.py', encoding='utf-8').read(); lines = src.split('\n'); tree = ast.parse(src); partes = []
    quiero_f = ('log', '_con_timeout', '_ahora'); quiero_c = ('ErrCrudo', 'EnvioReal'); quiero_a = ('NO_EXISTE', 'PRECARGA_TIMEOUT_S, PRECARGA_MARGEN_MIN_S')
    for n in tree.body:
        seg = '\n'.join(lines[n.lineno - 1:n.end_lineno])
        if isinstance(n, ast.FunctionDef) and n.name in quiero_f: partes.append((n.lineno, n.end_lineno, seg))
        elif isinstance(n, ast.ClassDef) and n.name in quiero_c: partes.append((n.lineno, n.end_lineno, seg))
        elif isinstance(n, ast.Assign) and len(n.targets) == 1 and ast.unparse(n.targets[0]).strip('()') in quiero_a: partes.append((n.lineno, n.end_lineno, seg))
    if len(partes) != 7: raise RuntimeError(f'extracto de sonda1.py inesperado: {[p[:2] for p in partes]}')
    cab = ('"""envio_real.py -- EXTRACTO VERBATIM de sonda1/sonda1.py (sha256 origen en VENDOR_HASHES.json; lineas ' + ', '.join(f'{a}-{b}' for a, b, _ in partes) + '). NO editar: regenerar con regenerar_vendor.py.\n'
           'Dependencias: `vendor_main` (la inyecta pl_core.cargar_vendor en sys.modules con el hash verificado; este modulo NO toca sys.path), re, threading, time, datetime. Solo lo usa pl_sender_real.py con --real + confirmacion."""\n'
           'import re, sys, os, threading, time\nfrom datetime import datetime, timezone\nimport vendor_main as V\n\n\n')
    return cab + '\n\n\n'.join(p[2] for p in partes) + '\n', [(a, b) for a, b, _ in partes]


def generar_vendor_main():
    a = segmentos(S + 'vendor_main.py', nombres_f=('hash_orden',)); b = segmentos(LIVE_TRADE, nombres_f=('_parchear_redondeo_clob',), nombres_a=('_clob_redondeo_parcheado',))
    if not (len(a) == 1 and len(b) == 2): raise RuntimeError(f'segmentos inesperados: {a and [x[:2] for x in a]} {b and [x[:2] for x in b]}')
    txt = CAB_VENDOR_MAIN + a[0][2] + '\n\n\n' + '\n\n\n'.join(x[2] for x in b) + '\n' + PLANTILLA_MANUAL
    segs = [dict(origen=S + 'vendor_main.py', sha256_origen=sha(S + 'vendor_main.py'), lineas=[a[0][0], a[0][1]], nombre='hash_orden', sha256_segmento=shat(a[0][2]))]
    segs += [dict(origen=LIVE_TRADE, sha256_origen=sha(LIVE_TRADE), lineas=[x[0], x[1]], nombre=('_clob_redondeo_parcheado' if x[2].startswith('_clob') else '_parchear_redondeo_clob'), sha256_segmento=shat(x[2])) for x in b]
    return txt, segs


def main():
    if '--verificar' in sys.argv:
        h = json.load(open(HERE + 'VENDOR_HASHES.json'))['copias']; mal = [f for f, v in h.items() if not os.path.exists(HERE + f) or sha(HERE + f) != v['sha256_copia']]; deriva = []
        for f, v in h.items():
            if v.get('origen') and os.path.exists(v['origen']) and 'segmentos' not in v and sha(v['origen']) != v['sha256_origen']: deriva.append(f)
            for sg in v.get('segmentos', []):
                if os.path.exists(sg['origen']):
                    nf = ('hash_orden',) if sg['nombre'] == 'hash_orden' else ('_parchear_redondeo_clob',); na = ('_clob_redondeo_parcheado',) if sg['nombre'] == '_clob_redondeo_parcheado' else ()
                    cur = segmentos(sg['origen'], nombres_f=(nf if not na else ()), nombres_a=na)
                    if not cur or shat(cur[0][2]) != sg['sha256_segmento']: deriva.append(f + ':' + sg['nombre'])
        print(json.dumps(dict(ok=not mal, copias_alteradas=mal, deriva_respecto_a_origen=deriva), indent=1)); sys.exit(0 if not mal else 1)
    out = {}
    for f, o in COPIAS.items(): shutil.copyfile(o, HERE + f); out[f] = dict(origen=o, sha256_origen=sha(o), sha256_copia=sha(HERE + f))
    txt, rangos = extracto_envio(); open(HERE + 'envio_real.py', 'w', encoding='utf-8').write(txt); out['envio_real.py'] = dict(origen=S + 'sonda1.py', sha256_origen=sha(S + 'sonda1.py'), sha256_copia=sha(HERE + 'envio_real.py'), lineas_origen=rangos)
    txt, segs = generar_vendor_main(); open(HERE + 'vendor_main.py', 'w', encoding='utf-8').write(txt); out['vendor_main.py'] = dict(origen='GENERADO: segmentos verbatim + plantilla manual de regenerar_vendor.py', sha256_copia=sha(HERE + 'vendor_main.py'), segmentos=segs, sha256_regenerar=sha(HERE + 'regenerar_vendor.py'))
    json.dump(dict(creado_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), copias=out), open(HERE + 'VENDOR_HASHES.json', 'w'), indent=1); print(json.dumps(out, indent=1))


if __name__ == '__main__': main()
