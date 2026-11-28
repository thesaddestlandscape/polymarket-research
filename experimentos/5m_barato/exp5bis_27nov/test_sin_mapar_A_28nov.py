import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sin_mapar_A_28nov as S

DIA = '2026-11-25'


def reg(slug, tokens=('a', 'b'), v='v1', desfase=0):
    e = int(slug.rsplit('-', 1)[1]); d = 300 if '-5m-' in slug else 900
    import datetime as dt
    return dict(slug=slug, clobTokenIds=json.dumps(list(tokens)), version=v, endDate=dt.datetime.fromtimestamp(e + d + desfase, dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'))


def test_rejilla_288_y_96():
    assert len(S.rejilla(DIA, 'eth', '5m')) == 288 and len(S.rejilla(DIA, 'eth', '15m')) == 96
    assert S.rejilla(DIA, 'eth', '5m')[0][0] == 'eth-updown-5m-1795564800'


def test_endDate_inexacto_no_cuenta_y_gamma_vacio_cuenta_como_sin_mapar():
    g = S.rejilla(DIA, 'eth', '5m')[:3]
    cache = {}
    def get(slugs):
        return [reg(slugs[0]), reg(slugs[1], desfase=300)]        # el 2.o devuelve OTRO mercado (endDate distinto); el 3.o no viene
    rs, f = S.resuelve([(s, e) for s, _, e in g], cache, get, espera=0)
    assert rs[g[0][0]] is not None and rs[g[1][0]] is None and rs[g[2][0]] is None and f == 0
    assert list(cache) == [g[0][0]]                                  # solo lo validado se cachea


def test_fallo_http_cuenta_sin_mapar_no_omite():
    def get(slugs): raise RuntimeError('gamma 429')
    A, tm = S.metrica_A(DIA, 'eth', {'a'}, {}, get, espera=0)
    assert A['combinado']['esperados'] == 384 and A['combinado']['sin_mapar'] == 384 and A['A_ok'] is False and A['5m']['fallos_http'] == 288


def test_mapeado_exige_token_en_el_mapa_del_pipeline():
    def get(slugs): return [reg(s, tokens=('a', 'b')) for s in slugs]
    A, tm = S.metrica_A(DIA, 'eth', {'zzz'}, {}, get, espera=0)      # gamma resuelve todo pero el mapa no tiene los tokens
    assert A['5m']['gamma_valido'] == 288 and A['combinado']['en_mapa'] == 0 and A['A_ok'] is False
    A, tm = S.metrica_A(DIA, 'eth', {'a'}, {}, get, espera=0)
    assert A['combinado']['frac_sin_mapar'] == 0.0 and A['A_ok'] and tm['a'][0] == 'eth'


def test_umbral_010_y_estado_final():
    n = {'i': 0}
    def get(slugs):
        out = []
        for s in slugs:
            n['i'] += 1
            if n['i'] % 10 != 0: out.append(reg(s))                   # 10 % sin mapa exacto
        return out
    A, _ = S.metrica_A(DIA, 'eth', {'a'}, {}, get, espera=0)
    assert abs(A['combinado']['frac_sin_mapar'] - 0.10) < 0.01
    assert S.estado_final(False, 'COMPLETE') == 'SIN_MAPA' and S.estado_final(True, 'COMPLETE') == 'COMPLETE' and S.estado_final(True, 'PARTIAL_POR_MONEDA') == 'PARTIAL_POR_MONEDA'
