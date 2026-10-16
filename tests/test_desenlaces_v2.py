"""Pruebas de desenlaces(): gamma primero, /v2/tokens (on-chain) como fallback fail-closed. Sin red, sin datos reales."""
import gzip
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import analisis_maker_cancelacion_binance as M  # noqa: E402


class Resp:
    def __init__(self, status=200, data=None, raw=None, headers=None):
        self.status_code, self._d, self._raw, self.headers = status, data, raw, headers or {}

    def json(self):
        if self._raw is not None:
            raise json.JSONDecodeError("x", "", 0)
        return self._d


class Sesion:
    """Sesión falsa: gamma y v2 se programan por separado; registra las llamadas."""

    def __init__(self, gamma, v2):
        self.gamma, self.v2, self.llamadas = gamma, v2, []

    def get(self, url, **kw):
        self.llamadas.append(url)
        cola = self.gamma if "gamma" in url else self.v2
        r = cola.pop(0) if len(cola) > 1 else cola[0]
        if isinstance(r, Exception):
            raise r
        return r


def fila(tok, opp, cond, idx, resuelto=True, fp=None, **kw):
    d = {"token_id": tok, "condition_id": cond, "opposite_token_id": opp, "outcome_index": idx, "resolved": resuelto,
         "final_price": fp}
    d.update(kw)
    return d


def par_v2(m, ganador, cond=None):
    """Filas v2 de un mercado m (tokens 'm_Y', 'm_N') con ganador 'YES'/'NO'."""
    cond = cond or f"0xc{m}"
    return [fila(f"{m}_Y", f"{m}_N", cond, 0, fp=1.0 if ganador == "YES" else 0.0),
            fila(f"{m}_N", f"{m}_Y", cond, 1, fp=1.0 if ganador == "NO" else 0.0)]


@pytest.fixture
def entorno(tmp_path, monkeypatch):
    monkeypatch.setattr(M, "CACHE", tmp_path / "des.json")
    monkeypatch.setattr(M, "TOKENS_CACHE", tmp_path / "tok.json")
    monkeypatch.setattr(M, "REGISTRO_K", tmp_path / "reg")
    (tmp_path / "reg").mkdir()
    monkeypatch.setattr(M.time, "sleep", lambda s: None)

    def instalar(gamma, v2):
        s = Sesion(gamma, v2)
        monkeypatch.setattr(M.requests, "Session", lambda: s)
        return s
    return tmp_path, instalar


def registro(tmp, nombre, mids):
    lin = []
    for m in mids:
        for lado, t in (("YES", f"{m}_Y"), ("NO", f"{m}_N")):
            lin.append(f"k,1,{t},BTC,5min,{m},2026-10-15 10:00:00+00:00,{lado}")
    lin.insert(1, "h,1,xx,0.5,0.6,10")                       # filas que no son k se ignoran
    with gzip.open(tmp / "reg" / nombre, "wt") as fh:
        fh.write("\n".join(lin) + "\n")


def gamma_ok(mids_res):
    return Resp(200, [{"id": m, "outcomePrices": json.dumps(["1", "0"] if g == "YES" else ["0", "1"])}
                      for m, g in mids_res.items()])


def test_gamma_ok_no_toca_v2_ni_escribe_tokens(entorno):
    tmp, inst = entorno
    s = inst([gamma_ok({"1": "YES", "2": "NO"})], [Resp(500)])
    assert M.desenlaces({"1", "2"}) == {"1": "YES", "2": "NO"}
    assert all("gamma" in u for u in s.llamadas)
    assert not M.TOKENS_CACHE.exists()
    assert json.loads(M.CACHE.read_text()) == {"1": "YES", "2": "NO"}
    assert not list(tmp.glob("*.tmp*"))                     # escritura atómica sin restos


def test_gamma_roto_fallback_v2_desde_registro(entorno):
    tmp, inst = entorno
    registro(tmp, "m15_registro_2026-10-15.csv.gz", ["10", "11", "12"])
    s = inst([Resp(200, raw=True)], [Resp(200, {"data": par_v2("10", "YES") + par_v2("11", "NO") + par_v2("12", "YES")})])
    assert M.desenlaces({"10", "11", "12"}) == {"10": "YES", "11": "NO", "12": "YES"}
    assert json.loads(M.CACHE.read_text()) == {"10": "YES", "11": "NO", "12": "YES"}
    assert json.loads(M.TOKENS_CACHE.read_text())["mids"]["11"] == {"YES": "11_Y", "NO": "11_N"}
    # reinicio idempotente: todo en caché -> ninguna llamada de red
    s2 = inst([Resp(500)], [Resp(500)])
    assert M.desenlaces({"10", "11", "12"}) == {"10": "YES", "11": "NO", "12": "YES"}
    assert s2.llamadas == []


def test_fichero_ya_escaneado_no_se_relee(entorno, monkeypatch):
    tmp, inst = entorno
    registro(tmp, "m15_registro_2026-10-15.csv.gz", ["10"])
    inst([Resp(200, raw=True)], [Resp(200, {"data": []})])
    assert M.desenlaces({"10"}) == {}                       # on-chain aún sin datos -> ausente
    abiertos = []
    orig = M.gzip.open
    monkeypatch.setattr(M.gzip, "open", lambda *a, **k: abiertos.append(a) or orig(*a, **k))
    inst([Resp(200, raw=True)], [Resp(200, {"data": []})])
    assert M.desenlaces({"10", "99"}) == {}                 # 99 no está en ningún k; el fichero no se relee
    assert abiertos == []


def test_lotes_de_25_mercados_y_parcial_gamma(entorno):
    tmp, inst = entorno
    mids = [str(1000 + i) for i in range(60)]
    registro(tmp, "m15_registro_2026-10-15.csv.gz", mids)
    todas = [x for m in mids[1:] for x in par_v2(m, "NO")]
    s = inst([gamma_ok({mids[0]: "YES"})], [Resp(200, {"data": todas[:50]}), Resp(200, {"data": todas[50:100]}),
                                             Resp(200, {"data": todas[100:]})])
    r = M.desenlaces(set(mids))
    assert r[mids[0]] == "YES" and all(r[m] == "NO" for m in mids[1:]) and len(r) == 60
    assert sum("v2" in u for u in s.llamadas) == 3          # 59 mercados -> 25 + 25 + 9


def test_tokens_por_mid_explicito_sin_registro(entorno):
    tmp, inst = entorno
    inst([Resp(200, raw=True)], [Resp(200, {"data": par_v2("7", "NO")})])
    assert M.desenlaces({"7"}, tokens_por_mid={"7": {"YES": "7_Y", "NO": "7_N"}}) == {"7": "NO"}


def test_429_con_reintento_y_http_fallido_no_inventa(entorno):
    tmp, inst = entorno
    registro(tmp, "m15_registro_2026-10-15.csv.gz", ["10"])
    inst([Resp(429)], [Resp(429, headers={"retry-after": "1"}), Resp(200, {"data": par_v2("10", "YES")})])
    assert M.desenlaces({"10"}) == {"10": "YES"}
    M.CACHE.unlink()
    inst([Resp(429)], [Resp(503), Resp(503), Resp(503), Resp(503)])
    assert M.desenlaces({"10"}) == {}                       # sin respuesta válida: ausente, no 0
    inst([Resp(429)], [Resp(400)])
    assert M.desenlaces({"10"}) == {}


def test_excepciones_de_red_y_json_roto_en_v2(entorno):
    tmp, inst = entorno
    registro(tmp, "m15_registro_2026-10-15.csv.gz", ["10"])
    inst([ConnectionError("x")], [ConnectionError("x"), Resp(200, raw=True), Resp(200, {"data": par_v2("10", "NO")})])
    assert M.desenlaces({"10"}) == {"10": "NO"}


@pytest.mark.parametrize("mod", [
    lambda y, n: n.update(resolved=False),                                   # una pata sin resolver
    lambda y, n: (y.update(resolved=False, final_price=None), n.update(resolved=False, final_price=None)),
    lambda y, n: (y.update(final_price=0.5), n.update(final_price=0.5)),      # 50/50
    lambda y, n: (y.update(final_price=1.0), n.update(final_price=1.0)),      # ambas ganan: incoherente
    lambda y, n: (y.update(final_price=0.0), n.update(final_price=0.0)),
    lambda y, n: n.update(condition_id="0xotra"),
    lambda y, n: y.update(opposite_token_id="zzz"),
    lambda y, n: y.update(outcome_index=1, clob_index=1),                    # YES no es el primer resultado
    lambda y, n: y.update(final_price="basura"),
    lambda y, n: y.pop("resolved"),
])
def test_desenlace_v2_fail_closed(mod):
    y, n = par_v2("5", "YES")
    mod(y, n)
    assert M.desenlace_v2(y, n) is None


def test_desenlace_v2_filas_ausentes_y_ok():
    y, n = par_v2("5", "YES")
    assert M.desenlace_v2(None, n) is None and M.desenlace_v2(y, None) is None
    assert M.desenlace_v2(y, n) == "YES"
    y, n = par_v2("5", "NO")
    assert M.desenlace_v2(y, n) == "NO"
    y, n = par_v2("5", "NO")
    y["final_price"], n["final_price"] = 0.9995, 0.0004                       # tolerancia igual que gamma (0,999)
    assert M.desenlace_v2(y, n) == "YES"


def test_registro_truncado_y_mapa_corrupto_no_rompen(entorno):
    tmp, inst = entorno
    registro(tmp, "m15_registro_2026-10-15.csv.gz", ["10"])
    b = (tmp / "reg" / "m15_registro_2026-10-15.csv.gz").read_bytes()
    (tmp / "reg" / "m15_registro_2026-10-14.csv.gz").write_bytes(b[: len(b) // 2])   # truncado
    M.TOKENS_CACHE.write_text("{no es json")
    inst([Resp(200, raw=True)], [Resp(200, {"data": par_v2("10", "YES")})])
    assert M.desenlaces({"10"}) == {"10": "YES"}


def test_mercado_sin_tokens_conocidos_queda_ausente(entorno):
    tmp, inst = entorno
    s = inst([Resp(200, raw=True)], [Resp(500)])
    assert M.desenlaces({"404"}) == {}
    assert not any("v2" in u for u in s.llamadas)


def test_fallo_inesperado_del_fallback_no_rompe_a_quien_llama(entorno, monkeypatch):
    tmp, inst = entorno
    inst([gamma_ok({"1": "YES"}), Resp(200, raw=True)], [Resp(500)])
    monkeypatch.setattr(M, "_desenlaces_v2", lambda *a: (_ for _ in ()).throw(RuntimeError("boom")))
    assert M.desenlaces({"1", "2"}) == {"1": "YES"}
