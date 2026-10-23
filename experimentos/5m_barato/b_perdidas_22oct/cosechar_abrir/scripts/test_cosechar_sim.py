import os, sys, tempfile, numpy as np, pytest
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cosechar_sim as S
FIN_S = 1_800_000_000; FIN = FIN_S * 1000; T0 = FIN - 300000
D0 = T0 - 3600000
def make(q_yes, q_no, t_yes=(), t_no=(), x=(), tmp=None):
    """q_*: [(t_abs_ms, bid, ask, bsz, asz)], t_*: [(t_abs_ms, price, isBuy, size)], x: [(t_abs_ms, price)] Binance."""
    d = tempfile.mkdtemp(); S.OUT = d
    tokens = np.array(['1', '2']); tmap = np.array([['BTC', '5min', '100', '2027-01-15 08:00:00+00:00', 'YES'], ['BTC', '5min', '100', '2027-01-15 08:00:00+00:00', 'NO']])
    # fin real de la fixture
    import pandas as pd
    fin_iso = pd.Timestamp(FIN_S, unit='s', tz='UTC').isoformat(sep=' ')
    tmap[:, 3] = fin_iso
    def arr(rows, k, n):
        return np.array([(r[0] - D0) for r in rows], dtype=np.int32), np.full(len(rows), k, np.int16), np.array([r[1:1 + n] for r in rows], dtype=np.float32).reshape(len(rows), n)
    qa = arr(sorted(q_yes), 0, 4); qb = arr(sorted(q_no), 1, 4)
    ta = arr(sorted(t_yes), 0, 3); tb = arr(sorted(t_no), 1, 3)
    cat = lambda a, b: tuple(np.concatenate([u, v]) for u, v in zip(a, b))
    qr, qk, qv = cat(qa, qb); tr, tk, tv = cat(ta, tb)
    xs = sorted(x)
    np.savez(f'{d}/ms5_BTC_2027-01-15.npz', tokens=tokens, tmap=tmap, D0=D0, qr=qr, qk=qk, qv=qv, tr=tr, tk=tk, tv=tv,
             xr=np.array([r[0] - D0 for r in xs], np.int32), xv=np.array([r[1] for r in xs], np.float64))
    return S.Dia5('BTC', '2027-01-15')
BOOK = [(T0 - 1000, 0.47, 0.53, 20.0, 20.0)]
def test_through_fill_at_limit_price():
    D = make(BOOK, BOOK, t_yes=[(T0 + 2000, 0.47, 0, 7.0)])      # SELL del YES a 0.47 < 0.48: atraviesa
    res, px = S.simular_mercado(D, 0, 1, FIN, '100', 0.96, 'A0', 'BASE')
    u = S.unidad(res, px, 'YES')
    assert u['qY'] == 5.0 and u['qN'] == 0.0 and abs(u['cost'] - 5 * 0.48) < 1e-9 and abs(u['pnl'] - (5 - 2.4)) < 1e-9
    u2 = S.unidad(res, px, 'NO'); assert abs(u2['pnl'] + 2.4) < 1e-9       # pago unico: la pata ganadora paga 1/acc una vez
def test_opposite_buy_equivalent():
    D = make(BOOK, BOOK, t_no=[(T0 + 2000, 0.53, 1, 3.0)])         # BUY NO a 0.53 == SELL YES a 0.47
    res, px = S.simular_mercado(D, 0, 1, FIN, '100', 0.96, 'A0', 'BASE')
    assert abs(S.unidad(res, px, 'YES')['qY'] - 3.0) < 1e-6
def test_at_level_queue_regimes():
    book = [(T0 - 1000, 0.48, 0.53, 10.0, 20.0)]
    ev = [(T0 + 2000, 0.48, 0, 12.0)]                              # SELL a 0.48 = nivel: cola 10 delante
    D = make(book, book, t_yes=ev)
    q = {r: S.unidad(*S.simular_mercado(D, 0, 1, FIN, '100', 0.96, 'A0', r), 'YES')['qY'] for r in ('OPT', 'BASE', 'CONS')}
    assert q['OPT'] == 5.0 and abs(q['BASE'] - 2.0) < 1e-6 and q['CONS'] == 0.0
def test_no_fill_after_cancel_plus_grace():
    D = make(BOOK, BOOK, t_yes=[(FIN - S.T_FIN_MS + S.LCANCEL_MS + S.GRACE_MS + 50, 0.40, 0, 9.0)])
    res, px = S.simular_mercado(D, 0, 1, FIN, '100', 0.96, 'A0', 'BASE'); assert S.unidad(res, px, 'YES')['qY'] == 0.0
    D = make(BOOK, BOOK, t_yes=[(FIN - S.T_FIN_MS + 100, 0.40, 0, 9.0)])
    res, px = S.simular_mercado(D, 0, 1, FIN, '100', 0.96, 'A0', 'BASE'); assert S.unidad(res, px, 'YES')['qY'] == 5.0
def test_no_quote_if_bid_crosses_ask():
    book = [(T0 - 1000, 0.40, 0.48, 10.0, 10.0)]                   # ask 0.48 <= b: no se cotiza
    D = make(book, book, t_yes=[(T0 + 2000, 0.40, 0, 9.0)])
    res, px = S.simular_mercado(D, 0, 1, FIN, '100', 0.96, 'A0', 'BASE'); assert res['YES'] is None
def test_defense_bn_cancels_and_rearms_only_without_fills():
    x = [(T0 + 500 + i * 100, 100.0) for i in range(5)] + [(T0 + 1000, 100.0), (T0 + 1500, 100.03)]   # +3 bps en 1 s hacia T0+1500
    ev = [(T0 + 1700, 0.47, 0, 7.0), (T0 + 4000, 0.47, 0, 7.0)]
    D = make(BOOK, BOOK, t_yes=ev, x=x)
    res, px = S.simular_mercado(D, 0, 1, FIN, '100', 0.96, 'A_BN', 'BASE')
    f = res['YES']; assert f and f[0][0] == T0 + 4000                 # el primer trade cae tras la cancelacion y antes de recolocar -> no cuenta; el de 3.5 s si
    res0, _ = S.simular_mercado(D, 0, 1, FIN, '100', 0.96, 'A0', 'BASE'); assert res0['YES'][0][0] == T0 + 1700
def test_idempotent():
    D = make(BOOK, BOOK, t_yes=[(T0 + 2000, 0.47, 0, 7.0)], t_no=[(T0 + 5000, 0.46, 0, 2.0)])
    a = S.simular_mercado(D, 0, 1, FIN, '100', 0.96, 'A0', 'BASE'); b = S.simular_mercado(D, 0, 1, FIN, '100', 0.96, 'A0', 'BASE')
    assert a == b

def test_defense_not_applied_if_fill_before_cancel_effect():
    x = [(T0 + 500, 100.0), (T0 + 1500, 100.03)]
    D = make(BOOK, BOOK, t_yes=[(T0 + 1530, 0.47, 0, 7.0)], x=x)
    res, px = S.simular_mercado(D, 0, 1, FIN, '100', 0.96, 'A_BN', 'BASE'); assert res['YES'][0][0] == T0 + 1530
def test_float32_level_equality():
    book = [(T0 - 1000, 0.48, 0.53, 10.0, 20.0)]
    D = make(book, book, t_yes=[(T0 + 2000, 0.48, 0, 12.0)])
    assert abs(S.unidad(*S.simular_mercado(D, 0, 1, FIN, '100', 0.96, 'A0', 'BASE'), 'YES')['qY'] - 2.0) < 1e-6
