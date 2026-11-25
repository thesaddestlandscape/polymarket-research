#!/usr/bin/env python3
"""ejecutor_puro.py -- carga SIN importar el modulo (no se ejecuta el harness ni nada que toque credenciales) las funciones PURAS de decision de
/root/polymarket-research-dev/experimento_maker_h47.py y las constantes de politica, extrayendo su codigo por AST. Solo lectura del .py. Devuelve el sha256 del fuente usado.
Funciones: mils, en_banda, objetivo_h35, en_rejilla, tamano_orden. Constantes: K_POR_MONEDA, T_INI, T_STOP_DEF, LOOP_S, ASENTAR_H47_S, MIN_ENTRE_ACCIONES_S, REQUOTE_INVALIDO_S, MAX_VIVAS, SIZE_MIN, SIZE_MAX, POLL_S, MAX_ORDENES_PUJA."""
import ast, hashlib, math
SRC = '/root/polymarket-research-dev/experimento_maker_h47.py'
FUNCS = ('mils', 'en_banda', 'objetivo_h35', 'en_rejilla', 'tamano_orden')
CONSTS = ('K_POR_MONEDA', 'T_INI', 'T_STOP_DEF', 'LOOP_S', 'ASENTAR_H47_S', 'MIN_ENTRE_ACCIONES_S', 'REQUOTE_INVALIDO_S', 'MAX_VIVAS', 'POLL_S', 'MAX_ORDENES_PUJA')
def carga():
    txt = open(SRC, encoding='utf-8').read(); tree = ast.parse(txt); ns = {'math': math}; sha = hashlib.sha256(txt.encode()).hexdigest()
    for node in tree.body:
        if isinstance(node, ast.Assign):
            names = [t.id for t in node.targets if isinstance(t, ast.Name)]
            tup = [t for t in node.targets if isinstance(t, ast.Tuple)]
            if any(n in CONSTS for n in names) or any(n in ('SIZE_MIN', 'SIZE_MAX') for n in names) or (tup and {e.id for e in tup[0].elts if isinstance(e, ast.Name)} & {'SIZE_MIN', 'SIZE_MAX', 'MAX_ORDENES_PUJA'}):
                exec(compile(ast.Module([node], []), SRC, 'exec'), ns)
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in FUNCS: exec(compile(ast.Module([node], []), SRC, 'exec'), ns)
    miss = [n for n in FUNCS + CONSTS + ('SIZE_MIN', 'SIZE_MAX') if n not in ns]; assert not miss, miss
    return ns, sha
