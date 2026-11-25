"""new_market_universo: relleno gamma, integracion con servidor WS falso (reconexion, duplicados ws/gamma, reinicio, cierre limpio)."""
import asyncio, importlib.util, json, os, signal, time
from pathlib import Path
import pytest
import websockets
import universo_5m_io as U

SRC = Path(__file__).resolve().parent.parent / "stage" / "new_market_universo.py"


@pytest.fixture
def nm(tmp_path, monkeypatch):
    monkeypatch.setattr(U, "UNIV_DIR", tmp_path / "u5")
    spec = importlib.util.spec_from_file_location("nmu", SRC)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    m.GAMMA_INTERVALO_S = 0.0
    m.HORIZONTE_RELLENO_MIN = 60
    return m


class R:
    def __init__(self, st, d):
        self.status_code, self._d = st, d

    def raise_for_status(self):
        if self.status_code >= 400:
            raise RuntimeError(self.status_code)

    def json(self):
        return self._d


def _gev(slug):
    n = abs(hash(slug)) % 10**9
    return {"slug": slug, "markets": [{"id": str(n), "conditionId": "0x" + str(n), "question": "q",
                                       "clobTokenIds": json.dumps([str(n) + "1", str(n) + "2"]), "outcomes": '["Up","Down"]'}]}


def test_relleno_lotes_de_12_y_salta_conocidos(nm):
    llamadas = []

    def get(p):
        llamadas.append(p)
        return R(200, [_gev(v) for k, v in p if k == "slug"])
    now = int(time.time())
    conocido = f"btc-updown-5m-{((now // 300) + 1) * 300}"
    filas, c = nm.rellenar_huecos({conocido}, ahora=now, get=get)
    assert all(sum(1 for k, _ in p if k == "slug") <= 12 for p in llamadas)
    assert conocido not in {s for p in llamadas for k, s in p}
    assert c["filas"] == len(filas) == c["pendientes"] and all(f["fuente"] == "gamma" for f in filas)


def test_relleno_aborta_en_429(nm):
    n = {"n": 0}

    def get(p):
        n["n"] += 1
        return R(429, None)
    filas, c = nm.rellenar_huecos(set(), get=get)
    assert c["abortado_429"] and n["n"] == 1 and filas == []


def test_relleno_lote_fallido_continua_y_respuesta_rota(nm):
    seq = iter([RuntimeError("boom"), "rota"] + [None] * 100)

    def get(p):
        x = next(seq)
        if isinstance(x, Exception):
            raise x
        if x == "rota":
            return R(200, {"x": 1})
        return R(200, [_gev(v) for k, v in p if k == "slug"])
    filas, c = nm.rellenar_huecos(set(), get=get)
    assert c["errores"] == 2 and len(filas) > 0


def _evento_ws(slug, mid, up, dn):
    return json.dumps({"event_type": "new_market", "id": mid, "market": "0xc" + mid, "slug": slug, "question": "q",
                       "assets_ids": [up, dn], "outcomes": ["Up", "Down"], "timestamp": str(int(time.time() * 1000))})


def _correr(nm, planes, espera_s, gamma=None):
    """planes: lista de listas de mensajes por conexion; tras enviarlos la conexion se cierra salvo la ultima."""
    conexiones = {"n": 0}

    async def handler(ws, *_):
        i = conexiones["n"]
        conexiones["n"] += 1
        try:
            await ws.recv()                                      # suscripcion
            for m in planes[min(i, len(planes) - 1)]:
                await ws.send(m)
            if i < len(planes) - 1:
                await ws.close()
                return
            async for msg in ws:
                if msg == "PING":
                    await ws.send("PONG")
        except websockets.ConnectionClosed:
            pass

    async def go():
        async with websockets.serve(handler, "127.0.0.1", 0) as srv:
            port = srv.sockets[0].getsockname()[1]
            nm.WS_URL = f"ws://127.0.0.1:{port}"
            t = asyncio.create_task(nm.main())
            await asyncio.sleep(espera_s)
            t0 = time.time()
            os.kill(os.getpid(), signal.SIGTERM)
            await asyncio.wait_for(t, 10)
            return time.time() - t0
    return asyncio.run(go()), conexiones["n"]


def _filas(tmp):
    mk, st = U.leer(directorio=tmp)
    return mk, st


def test_ws_reconexion_duplicados_con_gamma_y_cierre_limpio(nm, tmp_path, monkeypatch):
    now = int(time.time())
    s1 = f"btc-updown-5m-{((now // 300) + 1) * 300 + 3600}"
    s2 = f"eth-updown-5m-{((now // 300) + 1) * 300 + 3600}"
    # gamma devuelve tambien el mercado s1 (mismo market_id/tokens que el WS) y los demas pendientes
    def fake_get(url, params=None, **k):
        sl = [v for kk, v in params if kk == "slug"]
        evs = []
        for s in sl:
            e = _gev(s)
            if s == s1:
                e["markets"][0].update(id="111", conditionId="0xc111", clobTokenIds='["501","502"]')
            evs.append(e)
        return R(200, evs)
    monkeypatch.setattr(nm.requests, "get", fake_get)
    planes = [[_evento_ws(s1, "111", "501", "502"), "basura no json", json.dumps([{"event_type": "book"}])],   # conexion 1: cae
              [_evento_ws(s1, "111", "501", "502"), _evento_ws(s2, "222", "601", "602"),
               _evento_ws("polyv2-btc-updown-5m-1", "9", "7", "8")]]                                          # conexion 2: duplicado + nuevo + ignorado
    dur_cierre, n_conex = _correr(nm, planes, 6.0)
    assert n_conex >= 2 and dur_cierre < 8
    mk, st = _filas(U.UNIV_DIR)
    assert mk["111"]["token_up"] == "501" and mk["222"]["token_down"] == "602" and "9" not in mk
    assert st["conflictos"] == 0 and st["truncados"] == 0
    # sin duplicados de market_id en el fichero (ws y gamma no se repiten)
    import csv, gzip
    ids = [r["market_id"] for r in csv.DictReader(gzip.open(U.fichero(U.dia_utc(), U.UNIV_DIR), "rt", newline="")) if r["market_id"] != "market_id"]
    assert len(ids) == len(set(ids))


def test_reinicio_idempotente_y_fichero_truncado(nm, tmp_path, monkeypatch):
    monkeypatch.setattr(nm.requests, "get", lambda *a, **k: R(200, []))
    now = int(time.time())
    s1 = f"btc-updown-5m-{((now // 300) + 1) * 300 + 3600}"
    planes = [[_evento_ws(s1, "111", "501", "502")]]
    _correr(nm, planes, 3.0)
    n1 = len(_filas(U.UNIV_DIR)[0])
    _correr(nm, planes, 3.0)                                                   # reinicio: mismo evento, no se reescribe
    mk, st = _filas(U.UNIV_DIR)
    assert len(mk) == n1 == 1
    p = U.fichero(U.dia_utc(), U.UNIV_DIR)
    p.write_bytes(p.read_bytes() + b"\x1f\x8b\x08corrupto")                    # truncado/basura: arranca igual y conserva lo legible
    _correr(nm, [[_evento_ws(f"eth-updown-5m-{((now // 300) + 1) * 300 + 3600}", "222", "601", "602")]], 3.0)
    mk, st = _filas(U.UNIV_DIR)
    assert "111" in mk


def test_429_en_relleno_pausa_y_no_reintenta(nm, monkeypatch):
    llamadas = {"n": 0}

    def fake_get(url, params=None, **k):
        llamadas["n"] += 1
        return R(429, None)
    monkeypatch.setattr(nm.requests, "get", fake_get)
    nm.RELLENO_PERIODICO_S = 0                                                  # reintentaria cada vuelta si no hubiera pausa
    _correr(nm, [[]], 5.0)
    assert llamadas["n"] == 1


def test_el_relleno_del_listener_salta_lo_que_ya_escribio_capture(nm, monkeypatch):
    """Hueco cruzado: si capture_markets (A) ya dejo un slug con tokens, el listener (B) no lo vuelve a pedir a gamma."""
    now = int(time.time())
    s1 = f"btc-updown-5m-{((now // 300) + 1) * 300 + 900}"
    U.escribir([U.parsear_nuevo({"id": "5", "market": "0xc5", "slug": s1, "assets_ids": ["5", "6"], "outcomes": ["Up", "Down"]},
                                now * 1000, "capture")], U.UNIV_DIR)
    pedidos = []

    def fake_get(url, params=None, **k):
        pedidos.extend(v for kk, v in params if kk == "slug")
        return R(200, [])
    monkeypatch.setattr(nm.requests, "get", fake_get)
    nm._relleno_sync(nm.Estado())
    assert pedidos and s1 not in pedidos
