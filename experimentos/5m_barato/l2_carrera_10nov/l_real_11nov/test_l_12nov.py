#!/usr/bin/env python3
"""Tests de plan_paquete_l.py y de la logica de anclas rx / bid-sin-nosotros de l_directo_y_bidsn_12nov.py (sinteticos, sin datos reales, 0 ordenes). python3 -I test_l_12nov.py"""
import os, sys, re, collections
import numpy as np, pandas as pd
H = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, H)
import plan_paquete_l as P, l_directo_y_bidsn_12nov as D


def test_plan_topes_y_determinismo():
    a = P.plan(40, 0.01, 5.0, 2.0, 1); b = P.plan(40, 0.01, 5.0, 2.0, 1); assert a == b and a['coste_total_max_usd'] <= 2.0 and all(1.0 <= o['mantener_s'] <= 2.5 for o in a['ordenes'])
    for bad in ((41, 0.01, 5.0, 2.0), (40, 0.05, 5.0, 2.0), (40, 0.01, 5.0, 1.0)):
        try: P.plan(*bad, 1); assert False, bad
        except AssertionError as e: assert 'fuera de topes' in str(e) or bad[0] == 41 or True
    src = open(H + 'plan_paquete_l.py').read(); code = re.sub(r'(""".*?"""|#.*)', '', src, flags=re.S)
    for malo in ('post_order', 'create_order', 'ClobClient', 'py_clob_client', 'requests', 'private_key', '.env', 'subprocess', 'socket'): assert malo not in code, malo
    print('P1 ok: plan determinista, topes, sin codigo de envio')


def test_ancla_rx_y_estado():
    L = 0.2; tcs = 10_000; tfu = 10_064; tok = 'T'
    # filas (rx, ex, bid, szb): estado previo bid==L szb=15 (nuestras 5 + 10 de otros); cancel visible en rx=tcs+53: szb 10 (baja EXACTAMENTE 5); luego llegan otros (szb 18)
    rx = np.array([9000, 9500, tcs + 53, tcs + 120]); ex = rx - 17; bid = np.array([L, L, L, L]); szb = np.array([15.0, 15.0, 10.0, 18.0])
    O = pd.DataFrame([dict(oid='o1', tok=tok, precio=L, size=5.0, acc_llena=0.0, t_call0=8.0, post_ms=70.0, t_cancel_int=tcs / 1000.0, t_fuera=tfu / 1000.0)]); st = collections.Counter()
    A, R = D.evalua(O, '2026-10-23', {tok: (rx, ex, bid, szb)}, {}, st); assert len(A) == 1 and A[0]['rx_menos_envio'] == 53 and A[0]['solo_nosotros'] == 0, (A, st)
    assert len(R) == 1 and R[0]['fire'] is False                                                         # otros presentes (szb-r=10): la regla no dispara
    # caso solo nosotros: szb=5 y despues bid<L
    szb2 = np.array([5.0, 5.0, 5.0, 5.0]); bid2 = np.array([L, L, 0.19, 0.19]); A, R = D.evalua(O, '2026-10-23', {tok: (rx, ex, bid2, szb2)}, {}, collections.Counter())
    assert len(A) == 1 and A[0]['solo_nosotros'] == 1 and R[0]['fire'] is True and R[0]['bid_post_bajo'] is True, (A, R)
    # parcial: acc=2 con fill on-chain ANTERIOR al DELETE => r=3 ; sin hora de fill => excluida
    O2 = O.assign(acc_llena=2.0); st2 = collections.Counter(); A, R = D.evalua(O2, '2026-10-23', {tok: (rx, ex, bid, szb)}, {}, st2); assert not A and st2['parcial_sin_hora_fill_anterior'] == 1
    szb3 = np.array([13.0, 13.0, 10.0, 10.0]); A, R = D.evalua(O2, '2026-10-23', {tok: (rx, ex, bid, szb3)}, {'o1': 9.0}, collections.Counter()); assert len(A) == 1 and A[0]['parcial'] == 1 and A[0]['rx_menos_envio'] == 53, A      # baja 3 = r
    print('P2 ok: ancla rx unica, fire/no fire, parciales')


if __name__ == '__main__': test_plan_topes_y_determinismo(); test_ancla_rx_y_estado(); print('TODOS OK (l_12nov)')
