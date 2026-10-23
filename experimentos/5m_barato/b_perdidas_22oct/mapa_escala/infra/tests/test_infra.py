import os, sys, json, gzip, tempfile, shutil, time, unittest, datetime as dt
TMP = tempfile.mkdtemp(prefix='mapa_infra_test_'); os.environ['MAPA_INFRA_ROOT'] = TMP + '/dl'; os.environ['MAPA_INFRA_VOL'] = TMP + '/vol'
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); sys.path.insert(0, '/root/polymarket-research')
import numpy as np, pandas as pd
import infra_lib as L, tokmap as T, tp1 as P, extrae_onchain_ext as E, n4 as N4
EXCH = L.EXCH; HDR = 'tipo,bloque,ts_est,tx,log_index,order_hash,maker,taker,side,token_id,maker_amt,taker_amt,fee\n'
def wgz(path, text, utime_old=True):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with gzip.open(path, 'wt') as f: f.write(text)
    if utime_old: t = time.time() - 7200; os.utime(path, (t, t))
def k(tok, coin, marco, mid, fin, lado): return f'k,1,{tok},{coin},{marco},{mid},{dt.datetime.fromtimestamp(fin, dt.timezone.utc).isoformat(sep=" ")},{lado}\n'
def fila(ts, tx, li, side, tok, mamt, tamt, taker='0xtaker', maker='0xmaker1'): return f'F,1,{ts},{tx},{li},h,{maker},{taker},{side},{tok},{mamt},{tamt},0\n'
def prepara(d, ganador='YES', extra_rows='', pc_usdc=2.5, salidas=True):
    t0 = int(dt.datetime.fromisoformat(d).replace(tzinfo=dt.timezone.utc).timestamp()) + 3600; fin = t0 + 300
    ks = k('tY', 'BTC', '5min', 'M1', fin, 'YES') + k('tN', 'BTC', '5min', 'M1', fin, 'NO') + k('eY', 'ETH', '5min', 'M2', fin, 'YES') + k('eN', 'ETH', '5min', 'M2', fin, 'NO') \
        + k('sY', 'ETH', '15min', 'M3', t0 + 900, 'YES') + k('sN', 'ETH', '15min', 'M3', t0 + 900, 'NO')
    wgz(f'{L.ROOT}/maker_ms_{d}_111.csv.gz', 'tipo,t_ms,id,c1,c2,c3,c4,c5\n' + ks)
    rows = HDR
    rows += fila(fin - 200, 'tx1', 0, 0, 'tY', pc_usdc, 10.0)                       # compra YES de 10 acc a pc 0.25 (T=200) -> N1
    rows += fila(fin - 200, 'tx1', 0, 0, 'tY', pc_usdc, 10.0)                       # duplicado (tx,li)
    rows += fila(fin - 100, 'tx2', 0, 1, 'tY', 10.0, 7.5, maker='0xmaker2')         # venta de 10 YES a 0.75 = compra NO a 0.25 -> coste 2.5, lc=NO
    rows += fila(fin - 100, 'tx3', 0, 0, 'tY', 3.0, 10.0)                           # pc = 0.30 exacto -> banda 4, fuera de N1
    rows += fila(fin - 100, 'tx4', 0, 0, 'tY', 2.0, 10.0)                           # pc = 0.20 exacto -> banda 3, dentro
    rows += fila(fin - 30, 'tx5', 0, 0, 'tY', 2.5, 10.0)                            # T=30 -> tb 0, fuera
    rows += fila(fin - 100, 'tx6', 0, 0, 'tY', 2.5, 10.0, taker=EXCH)               # taker == EXCH: excluido
    rows += fila(fin - 100, 'tx7', 0, 0, 'eY', 2.5, 10.0)                           # ETH 5m banda 3: fuera de N1
    rows += fila(fin - 100, 'tx8', 0, 0, 'eY', 9.5, 10.0)                           # ETH 5m pc .95 -> N3
    rows += fila(fin - 100, 'tx9', 0, 0, 'sY', 8.0, 10.0)                           # ETH 15m pc .80 -> N2
    rows += fila(fin - 100, 'txa', 0, 0, 'xxx', 8.0, 10.0)                          # token desconocido
    rows += extra_rows
    wgz(f'{L.ROOT}/onchain_fills_{d}.csv.gz', rows)
    for m, toks in ((('5min', ('tY', 'tN', 'eY', 'eN')), ('15min', ('sY', 'sN'))) if salidas else ()):
        sel = HDR + ''.join(l for l in rows.splitlines(True)[1:] if l.split(',')[9] in toks)
        wgz(f'{L.VOL}/{L.PREF[m]}_onchain/{L.PREF[m]}_onchain_{d}.csv.gz', sel)
    return fin
class T1(unittest.TestCase):
    def setUp(self):
        shutil.rmtree(TMP, ignore_errors=True); os.makedirs(TMP)
        P.MIN_TOK = {'5min': 1, '15min': 1}; E.ESPERADO = {}
    def test_tokmap_cache_e_idempotencia(self):
        prepara('2026-10-24'); tk, info = T.tokens_dia('2026-10-24', ['5min', '15min'])
        self.assertEqual(len(tk['5min']), 4); self.assertEqual(len(tk['15min']), 2); self.assertEqual(info['truncados'], [])
        idx1 = json.load(open(L.INFRA / 'tokmap/indice.json')); tk2, _ = T.tokens_dia('2026-10-24', ['5min', '15min'])
        self.assertEqual(tk, tk2); self.assertEqual(idx1, json.load(open(L.INFRA / 'tokmap/indice.json')))
    def test_gz_corrupto_se_marca_truncado(self):
        prepara('2026-10-24'); f = f'{L.ROOT}/maker_ms_2026-10-24_222.csv.gz'
        wgz(f, 'tipo,t_ms,id,c1,c2,c3,c4,c5\n' + k('zz', 'SOL', '5min', 'M9', 1792800000, 'YES') + ''.join(f'q,{i},tok,1,2,3,4,5\n' for i in range(20000)))
        raw = open(f, 'rb').read(); open(f, 'wb').write(raw[:len(raw) // 2]); t = time.time() - 7200; os.utime(f, (t, t))   # corte
        tk, info = T.tokens_dia('2026-10-24', ['5min']); self.assertIn('maker_ms_2026-10-24_222.csv.gz', info['truncados'])
    def test_fichero_en_escritura_se_salta(self):
        prepara('2026-10-24'); wgz(f'{L.ROOT}/maker_ms_2026-10-24_333.csv.gz', 'x\n' + k('qq', 'SOL', '5min', 'M8', 1792800000, 'YES'), utime_old=False)
        tk, info = T.tokens_dia('2026-10-24', ['5min']); self.assertIn('maker_ms_2026-10-24_333.csv.gz', info['en_escritura']); self.assertNotIn('qq', tk['5min'])
    def test_tp1_dia_aritmetica_y_nichos(self):
        prepara('2026-10-24'); m = P.dia('2026-10-24'); self.assertEqual(m['estado'], 'COMPLETE', m.get('motivos'))
        C = pd.read_csv(P.dirs() / 'celdas_2026-10-24.csv.gz', dtype={'mid': str, 'maker': str})
        n1 = C[C.nicho == 'N1']; self.assertEqual(set(n1.mid), {'M1'})
        # N1: tx1 (2.5/10 YES), tx2 (compra NO a .25, coste 2.5), tx4 (pc .20, coste 2.0) ; excluidos: dup, pc .30, T=30, EXCH, token desconocido
        self.assertAlmostEqual(n1.coste.sum(), 2.5 + 2.5 + 2.0); self.assertEqual(int(n1.nf.sum()), 3)
        self.assertEqual(set(n1.lc), {'YES', 'NO'}); self.assertEqual(C[C.nicho == 'N2'].coste.sum(), 8.0); self.assertEqual(C[C.nicho == 'N3'].coste.sum(), 9.5)
        self.assertEqual(m['fuentes']['5min']['duplicados'], 1)
    def test_idempotencia_reinicio(self):
        prepara('2026-10-24'); P.dia('2026-10-24'); f = P.dirs() / 'celdas_2026-10-24.csv.gz'; sha = L.sha_file(f); mf = L.read_json(P.dirs() / 'tp1_2026-10-24.json')
        m2 = P.dia('2026-10-24'); self.assertEqual(L.sha_file(f), sha); self.assertEqual(m2['celdas_sha16'], mf['celdas_sha16'])
        P.dia('2026-10-24', forzar=True); self.assertEqual(L.sha_file(f), sha)           # recomputo forzado = mismo resultado, sin filas duplicadas
        C = pd.read_csv(f, dtype={'mid': str, 'maker': str}); self.assertFalse(C.duplicated(['nicho', 'coin', 'mid', 'lc', 'maker']).any())
    def test_eval_pnl_total_y_gates(self):
        # 10 dias; N1 pnl del dia: gana YES -> tx1 +7.5, tx2 (NO) -2.5, tx4 +8 ; pierde -> -2.5,+7.5,-2.0
        for i, d in enumerate(L.dias(L.FWD0, L.FWD1)): prepara(d); P.dia(d)
        des = {'M1': 'YES', 'M2': 'YES', 'M3': 'YES'}
        ev = P.evalua(des, hoy='2026-11-05'); r = ev['N1']
        self.assertEqual(r['n_validos'], 10); pnl_dia = 7.5 - 2.5 + 8.0; self.assertAlmostEqual(r['ev'], pnl_dia / 7.0)
        self.assertEqual(r['dias_pos'], 10); self.assertEqual(r['veredicto'], 'PASA')
        ev2 = P.evalua({'M1': 'NO'}, hoy='2026-11-05'); self.assertAlmostEqual(ev2['N1']['ev'], (-2.5 + 7.5 - 2.0) / 7.0)    # cobertura de N2/N3 = 0 -> invalidos
        self.assertEqual(ev2['N1']['veredicto'], 'PASA'); self.assertEqual(ev2['N2']['n_validos'], 0)
        g0 = P.NICHOS['N1']['gate']; P.NICHOS['N1']['gate'] = 5.0
        try: self.assertEqual(P.evalua(des, hoy='2026-11-05')['N1']['veredicto'], 'NO_PASA')
        finally: P.NICHOS['N1']['gate'] = g0
        ev3 = P.evalua({}, hoy='2026-11-05'); self.assertEqual(ev3['N1']['n_validos'], 0)         # sin desenlace: missing != 0, dias invalidos
        self.assertTrue(all(f['estado'].startswith('INVALIDO') for f in ev3['N1']['dias']))
    def test_acumulando_y_futuro(self):
        prepara('2026-10-24'); P.dia('2026-10-24'); ev = P.evalua({'M1': 'YES'}, hoy='2026-10-25'); self.assertTrue(ev['N1']['veredicto'].startswith('ACUMULANDO 1/10'))
    def test_extraccion_idempotente_y_truncado(self):
        d = '2026-10-24'; prepara(d, salidas=False); m = E.extrae_dia(d, ['5min', '15min'])
        self.assertEqual(m['estado'], 'COMPLETE', m); n5 = m['marcos']['5min']['n_out']; self.assertEqual(n5, 9)     # 9 filas de tokens 5m en el fixture
        m2 = E.extrae_dia(d, ['5min', '15min']); self.assertTrue(m2['marcos']['5min']['estado'].startswith('COMPLETE(ya'))
        # truncado por tamano: 4 dias previos grandes, el dia actual pequeno
        for k_ in range(1, 5):
            dd = (dt.date.fromisoformat(d) - dt.timedelta(days=k_)).isoformat(); p = E.destino('5min', dd); os.makedirs(p.parent, exist_ok=True); p.write_bytes(b'x' * 10000)
        E.destino('5min', d).write_bytes(b'x' * 100); self.assertEqual(E.estado_previo('5min', d), 'truncado')
        m3 = E.extrae_dia(d, ['5min']); self.assertTrue(m3['marcos']['5min']['estado'] in ('COMPLETE', 'PARTIAL'))
        self.assertGreater(E.destino('5min', d).stat().st_size, 100)
    def test_extraccion_fail_closed(self):
        d = '2026-10-24'; m = E.extrae_dia(d, ['5min']); self.assertEqual(m['estado'], 'BLOCKED')                   # sin on-chain
        prepara(d, salidas=False); os.remove(L.ROOT / f'maker_ms_{d}_111.csv.gz'); m = E.extrae_dia(d, ['5min']); self.assertEqual(m['marcos']['5min']['estado'], 'BLOCKED')   # sin mapa de tokens
    def test_extraccion_partial_si_mapa_incompleto(self):
        d = '2026-10-24'; prepara(d, salidas=False); E.ESPERADO = {'5min': 6500}; m = E.extrae_dia(d, ['5min']); self.assertEqual(m['marcos']['5min']['estado'], 'PARTIAL')
    def test_gamma_caido_bloquea_4h(self):
        d = '2026-10-24'; prepara(d, salidas=False); orig = T.gamma_dia
        def boom(*a, **k): raise RuntimeError('red caida')
        T.gamma_dia = boom
        try: m = E.extrae_dia(d, ['240min'])
        finally: T.gamma_dia = orig
        self.assertEqual(m['marcos']['240min']['estado'], 'BLOCKED'); self.assertFalse(E.destino('240min', d).exists())
    def test_n4_celdas_bordes(self):
        X = pd.DataFrame(dict(coin=['ETH'] * 6, mid=list('abcdef'), fin=[1.0] * 6, lc=['YES'] * 6, maker=['m'] * 6, coste=[1.0] * 6, acc=[10.0] * 6, reb=[0.0] * 6,
                              pc=[0.0099, 0.01, 0.05, 0.0999, 0.10, 0.02], T=[100, 100, 100, 100, 100, 300.0]))
        C = N4.celdas(X); self.assertEqual(sorted(C.mid), ['b', 'c', 'd']); self.assertEqual(dict(zip(C.mid, C.b)), {'b': 0, 'c': 4, 'd': 8}); self.assertTrue((C.tt == 0).all())
    def test_n4_minera_y_gate(self):
        rng = np.random.default_rng(1); dias_ = L.dias(L.FWD0, L.FWD1); rows = []
        for i, d in enumerate(dias_):
            for j in range(30):
                gana = rng.random() < 0.33; rows.append(dict(dia=d, coin='ETH', b=4, tt=1, lc='YES', mid=f'{d}{j}', maker=f'w{j % 5}', fin=1e9 + i * 1000 + j, coste=1.0, acc=3.0, reb=0.0, pnl=2.0 if gana else -1.0))
        C = pd.DataFrame(rows); R = N4.minera(C, dias_, dias_[4]); r = R[(R.coin == 'ETH') & (R.bucket == '0.05-0.06') & (R['T'] == '120-180') & (R.lado == 'YES')].iloc[0]
        self.assertEqual(r.cierres, 300); self.assertAlmostEqual(r.ev, C.pnl.sum() / C.coste.sum()); self.assertEqual(r.dias_pos, int((C.groupby('dia').pnl.sum() > 0).sum()))
        # la celda agregada (ALL, H, TODO, AMBOS) tiene los mismos datos; el resto de celdas no
        a = R[(R.coin == 'ALL') & (R.bucket == 'H0.05-0.10') & (R['T'] == 'TODO') & (R.lado == 'AMBOS')].iloc[0]; self.assertAlmostEqual(a.ev, r.ev)
        self.assertFalse(((R.coin == 'BTC') & (R.cierres > 0)).any()); self.assertTrue(R.q_bh.dropna().between(0, 1).all())
        R = N4.refina(R, C); self.assertIn('top1_wallet', R)
    def test_ventana_prohibida(self):
        self.assertIsInstance(L.en_ventana_prohibida(), bool)
if __name__ == '__main__': unittest.main(verbosity=2)
