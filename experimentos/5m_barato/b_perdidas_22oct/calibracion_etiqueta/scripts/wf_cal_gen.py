#!/usr/bin/env python3
"""Genera wf_cal_offN.py a partir de f8_estructura/scripts/wf_f8.py SIN cambiar el modelo ni el gate: solo entrada/salida, coste c=5*bl, sin bloque M1F. Verifica cada sustitucion."""
import sys
off = sys.argv[1]; src = open('/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/f8_estructura/scripts/wf_f8.py').read()
def rep(s, a, b):
    assert a in s, a
    return s.replace(a, b)
s = src
s = rep(s, "DL = '/root/polymarket-research-datalogs/f8_estructura/'; OUTD = os.path.dirname(os.path.abspath(__file__)) + '/../datos/'", "DL = '/root/polymarket-research-datalogs/calibracion_etiqueta/'; OUTD = os.path.dirname(os.path.abspath(__file__)) + '/../datos/'")
s = rep(s, "pd.read_parquet(DL + 'tabla.parquet')", "pd.read_parquet(DL + 'tabla_cal_off%s.parquet')" % off)
s = rep(s, "V['c'] = 5.0 * V.b;", "V['c'] = 5.0 * V.bl;")
s = rep(s, "S.to_parquet(DL + 'f8_scores.parquet')", "S.to_parquet(DL + 'wfcal_scores_off%s.parquet')" % off)
s = rep(s, "OUTD + 'f8_resultados.json'", "OUTD + 'wfcal_resultados_off%s.json'" % off)
i = s.index("# M1F degradado sobre vidas RELLENAS"); j = s.index("json.dump(RES")
s = s[:i] + s[j:]
s = rep(s, "KEEP = sorted(set(P2) | {", "KEEP = sorted(set(P2) | {'bl', ")
open(__file__.rsplit('/', 1)[0] + '/wf_cal_off%s.py' % off, 'w').write(s); print('ok', off)
