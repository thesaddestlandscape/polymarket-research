"""Tests (sin red) del parche de capture_markets (stage)."""
import csv, datetime as dt, importlib.util, json, os, subprocess, sys, time
from pathlib import Path
import pytest
import universo_5m_io as U

STAGE = Path(__file__).resolve().parent.parent / "stage" / "capture_markets.py"
MAIN = Path("/root/polymarket-research/capture_markets.py")


class Resp:
    def __init__(self, status=200, data=None):
        self.status_code, self._d = status, data

    def raise_for_status(self):
        if self.status_code >= 400:
            import requests
            raise requests.HTTPError(f"HTTP {self.status_code}")

    def json(self):
        return self._d


def _evento(slug):
    ts = int(slug.rsplit("-", 1)[1])
    fin = dt.datetime.fromtimestamp(ts + 300, dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    n = abs(hash(slug)) % 10**12
    return {"id": slug[:6], "title": slug, "slug": slug, "volume24hr": 0, "tags": [{"label": "Crypto"}],
            "markets": [{"id": str(n), "conditionId": "0xc" + str(n), "question": f"X Up or Down {ts}", "slug": slug,
                         "endDate": fin, "outcomePrices": '["0.5","0.5"]', "outcomes": '["Up","Down"]',
                         "clobTokenIds": json.dumps([str(n) + "1", str(n) + "2"])}]}


@pytest.fixture
def cm(tmp_path, monkeypatch):
    monkeypatch.setenv("CAPTURE_5M_HORIZONTE_MIN", "1440")
    monkeypatch.setenv("CAPTURE_ESTADO_PATH", str(tmp_path / "estado.json"))
    monkeypatch.setenv("UNIVERSO_5M_DIR", str(tmp_path / "u5"))
    monkeypatch.setattr(U, "UNIV_DIR", tmp_path / "u5")
    spec = importlib.util.spec_from_file_location("cm_stage", STAGE)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    m.DIR_MARKETS = tmp_path / "markets"
    m.GAMMA_INTERVALO_MIN_S = 0.0
    m.llamadas, m.modo, m.no_existen = [], "ok", ()

    def fake(url, params):
        m.llamadas.append(params)
        slugs = [v for k, v in params if k == "slug"] if isinstance(params, list) else [params.get("slug")]
        if m.modo == "429":
            return Resp(429)
        if m.modo == "500":
            return Resp(500)
        if m.modo == "lista_rota":
            return Resp(200, {"no": "lista"})
        return Resp(200, [_evento(s) for s in slugs if s not in m.no_existen])
    m._GET["fn"] = fake
    return m


def _ciclo(cm, now):
    mk, ft, c = cm.fetch_updown_5m_adelanto(ahora_ts=now)
    U.escribir(ft)
    return mk, ft, c


def test_cabecera_identica_a_main(cm):
    cab = MAIN.read_text().split("CABECERA_MARKETS = [")[1].split("]")[0]
    assert [c.strip().strip('",') for c in cab.replace("\n", "").split(",") if c.strip()] == cm.CABECERA_MARKETS
    real = Path("/root/polymarket-research/data/markets/2026-11-13.csv")
    if real.exists():
        assert real.open().readline().strip() == ",".join(cm.CABECERA_MARKETS)


def test_horizonte_cero_no_hace_nada(cm):
    assert cm.fetch_updown_5m_adelanto(horizonte_min=0) == ([], [], cm.fetch_updown_5m_adelanto(horizonte_min=0)[2]) and cm.llamadas == []


def test_data_markets_no_cambia_ni_se_crea_con_adelanto(cm, monkeypatch):
    """El adelanto escribe SOLO en universo_5m/: data/markets queda como el comportamiento actual (cabecera, sin filas de adelanto)."""
    monkeypatch.setattr(cm, "fetch_coingecko_prices", lambda: {})
    monkeypatch.setattr(cm, "guardar_precios", lambda *a, **k: None)
    monkeypatch.setattr(cm, "fetch_todos_eventos_crypto", lambda: [])
    monkeypatch.setattr(cm, "fetch_todos_updown", lambda: [])
    cm.MAX_LOTES_CICLO = 3
    cm.una_captura()
    principal = list(cm.DIR_MARKETS.glob("*.csv"))
    assert len(principal) == 1 and sum(1 for _ in principal[0].open()) == 1          # solo cabecera
    ad = list(U.UNIV_DIR.glob("adelanto_*.csv"))
    assert len(ad) == 1
    filas = list(csv.reader(ad[0].open(newline="")))
    assert filas[0] == cm.CABECERA_MARKETS and len(filas) - 1 == 3 * cm.LOTE_SLUGS
    mk, st = U.leer(directorio=U.UNIV_DIR)
    assert len(mk) == 3 * cm.LOTE_SLUGS and all(r["fuente"] == "capture" for r in mk.values())


def test_relleno_incremental_nearest_first_e_idempotente(cm):
    now = int(time.time())
    primeros = []
    for ciclo in range(10):
        mk, ft, c = _ciclo(cm, now)
        if not ft:
            break
        primeros.append(min(int(r["inicio_ts"]) for r in ft))
        assert c["lotes"] <= cm.MAX_LOTES_CICLO
    assert primeros == sorted(primeros) and len(primeros) >= 3
    siguiente = ((now // 300) + 1) * 300
    n_esp = len(range(siguiente + 900, now + 1440 * 60 + 1, 300))
    mk, _ = U.leer(now, U.UNIV_DIR)
    assert len(mk) == 6 * n_esp and 280 <= n_esp <= 290
    ll = len(cm.llamadas)
    assert _ciclo(cm, now)[1] == [] and len(cm.llamadas) == ll                       # idempotente: 0 llamadas nuevas
    assert all(sum(1 for k, _ in p if k == "slug") <= cm.LOTE_SLUGS for p in cm.llamadas)


def test_reinicio_a_mitad_de_ciclo_no_deja_huecos_ni_duplica(cm):
    """Si el proceso muere tras escribir adelanto_<dia>.csv pero ANTES del commit de tokens, el ciclo siguiente repite el lote."""
    now = int(time.time())
    cm.MAX_LOTES_CICLO = 2
    mk, ft, c = cm.fetch_updown_5m_adelanto(ahora_ts=now)       # "murio" antes de U.escribir(ft)
    assert ft and U.leer(now, U.UNIV_DIR)[0] == {}
    mk2, ft2, c2 = cm.fetch_updown_5m_adelanto(ahora_ts=now)    # proceso nuevo: mismo trabajo
    assert [r["slug"] for r in ft2] == [r["slug"] for r in ft]
    U.escribir(ft2)
    mk3, ft3, _ = cm.fetch_updown_5m_adelanto(ahora_ts=now)
    assert not (set(r["slug"] for r in ft3) & set(r["slug"] for r in ft2))


def test_cubre_lo_que_ya_trajo_el_listener(cm):
    now = int(time.time())
    siguiente = ((now // 300) + 1) * 300
    t0 = siguiente + 900
    U.escribir([U.parsear_nuevo({"id": "99", "market": "0xc99", "slug": f"btc-updown-5m-{t0}", "assets_ids": ["5", "6"],
                                 "outcomes": ["Up", "Down"]}, int(time.time() * 1000))], U.UNIV_DIR)
    mk, ft, c = cm.fetch_updown_5m_adelanto(ahora_ts=now)
    assert f"btc-updown-5m-{t0}" not in {r["slug"] for r in ft}


def test_lote_fallido_se_reintenta_y_no_se_da_por_hecho(cm):
    now = int(time.time())
    cm.modo = "500"
    mk, ft, c = cm.fetch_updown_5m_adelanto(ahora_ts=now)
    assert ft == [] and c["lotes_fallidos"] == 3 and c["lotes"] == 3 and not cm._RAFAGA["abortada"]
    cm.modo = "lista_rota"
    assert cm.fetch_updown_5m_adelanto(ahora_ts=now)[2]["lotes_fallidos"] == 3
    cm.modo = "ok"
    assert len(_ciclo(cm, now)[1]) > 0


def test_evento_sin_tokens_validos_no_se_da_por_hecho(cm):
    now = int(time.time())
    orig = cm._GET["fn"]

    def sin_tokens(url, params):
        r = orig(url, params)
        for ev in r._d:
            ev["markets"][0]["clobTokenIds"] = "[]"
        return r
    cm._GET["fn"] = sin_tokens
    mk, ft, c = cm.fetch_updown_5m_adelanto(ahora_ts=now)
    assert ft == [] and c["tokens_invalidos"] > 0 and U.leer(now, U.UNIV_DIR)[0] == {}


def test_429_aborta_rafaga_y_pausa_persistente(cm):
    cm.modo = "429"
    now = dt.datetime(2026, 11, 13, 23, 47, 10, tzinfo=dt.timezone.utc)
    mk, ft, c = cm.fetch_updown_5m_adelanto(ahora_ts=int(now.timestamp()))
    assert c["abortado_429"] and len(cm.llamadas) == 1 and ft == []
    assert cm._pausa_tras_429(now) == dt.datetime(2026, 11, 14, 0, 2, tzinfo=dt.timezone.utc).timestamp()
    assert cm._pausa_tras_429(dt.datetime(2026, 11, 13, 20, 20, tzinfo=dt.timezone.utc)) == dt.datetime(2026, 11, 13, 20, 22, tzinfo=dt.timezone.utc).timestamp()
    assert json.loads(cm.ESTADO_PATH.read_text())["pausa_hasta"] > time.time()
    cm._ESTADO["cargado"], cm._ESTADO["pausa_hasta"] = False, 0.0                   # otro proceso
    assert cm.gamma_en_pausa()
    n = len(cm.llamadas)
    with pytest.raises(cm._Gamma429):
        cm._gamma_get(cm._GAMMA_URL_EVENTS, {"slug": "x"})
    assert len(cm.llamadas) == n


def test_429_en_ruta_cercana_y_taglist_tambien_aborta(cm):
    cm.modo = "429"
    r = cm.fetch_updown_por_horizonte(cm.UPDOWN_HORIZONTES[0])
    assert r == [] and len(cm.llamadas) == 1
    cm._RAFAGA["abortada"] = False
    cm.llamadas.clear()
    assert cm.fetch_events_por_slug("crypto") == [] and len(cm.llamadas) == 1


def test_una_captura_en_pausa_no_llama_a_gamma(cm, monkeypatch):
    monkeypatch.setattr(cm, "fetch_coingecko_prices", lambda: {})
    monkeypatch.setattr(cm, "guardar_precios", lambda *a, **k: None)
    cm._cargar_estado()
    cm._ESTADO["pausa_hasta"] = time.time() + 600
    cm.una_captura()
    assert cm.llamadas == [] and not cm.DIR_MARKETS.exists()


def test_estado_corrupto_o_reloj_absurdo(cm):
    cm.ESTADO_PATH.write_text("{no es json")
    cm._ESTADO["cargado"] = False
    cm._cargar_estado()
    assert cm._ESTADO["pausa_hasta"] == 0.0
    cm.ESTADO_PATH.write_text(json.dumps({"pausa_hasta": time.time() + 10**7}))        # pausa absurda (reloj saltado)
    cm._ESTADO["cargado"] = False
    cm._cargar_estado()
    assert cm._ESTADO["pausa_hasta"] == 0.0
    cm._ESTADO["pausa_hasta"] = time.time() + 60
    cm._guardar_estado()
    assert [p.name for p in cm.ESTADO_PATH.parent.iterdir() if ".tmp" in p.name] == []


def test_tokens_corruptos_en_disco_no_impiden_el_adelanto(cm):
    U.UNIV_DIR.mkdir(parents=True, exist_ok=True)
    U.fichero(U.dia_utc(), U.UNIV_DIR).write_bytes(b"\x1f\x8bxx basura")
    mk, ft, c = cm.fetch_updown_5m_adelanto(ahora_ts=int(time.time()))
    assert ft


def test_cambio_de_dia_sin_reescritura_el_lector_une_dos_dias(cm):
    """A las 00:00Z no hace falta reescribir: hoy+ayer ya cubren el horizonte de 24 h; el adelanto no repite lo de ayer."""
    ahora = dt.datetime(2026, 11, 14, 0, 1, tzinfo=dt.timezone.utc).timestamp()
    sig = ((int(ahora) // 300) + 1) * 300 + 900
    U.escribir([U.parsear_nuevo({"id": "7", "market": "0xc7", "slug": f"btc-updown-5m-{sig}", "assets_ids": ["5", "6"],
                                 "outcomes": ["Up", "Down"]}, int((ahora - 1800) * 1000))], U.UNIV_DIR)   # escrito el dia 13
    mk, ft, c = cm.fetch_updown_5m_adelanto(ahora_ts=int(ahora))
    assert f"btc-updown-5m-{sig}" not in {r["slug"] for r in ft}


def test_orden_commit_si_falla_la_escritura_de_tokens_no_hay_estado_falso(cm, monkeypatch):
    monkeypatch.setattr(cm, "fetch_coingecko_prices", lambda: {})
    monkeypatch.setattr(cm, "guardar_precios", lambda *a, **k: None)
    monkeypatch.setattr(cm, "fetch_todos_eventos_crypto", lambda: [])
    monkeypatch.setattr(cm, "fetch_todos_updown", lambda: [])
    monkeypatch.setattr(U, "escribir", lambda *a, **k: (_ for _ in ()).throw(OSError("disco lleno")))
    cm.MAX_LOTES_CICLO = 2
    cm.una_captura()                                         # no lanza; el siguiente ciclo repite
    assert U.leer(directorio=U.UNIV_DIR)[0] == {}


def test_sin_modulo_io_el_adelanto_queda_apagado(tmp_path):
    """Si universo_5m_io no se despliega, capture_markets arranca igual con el adelanto apagado."""
    d = tmp_path / "solo"
    d.mkdir()
    (d / "capture_markets.py").write_text(STAGE.read_text())
    (d / "data_quality.py").write_text("def validar_precio(*a): return True,''\ndef fetch_coinbase_spot(*a, **k): return {}\ndef validar_cross_source(*a, **k): return {}\n")
    r = subprocess.run([sys.executable, "-I", "-c", "import sys; sys.path.insert(0,%r); import capture_markets as c; print(c.U, c.HORIZONTE_5M_MIN)" % str(d)],
                       capture_output=True, text=True, env={"CAPTURE_5M_HORIZONTE_MIN": "1440", "PATH": os.environ["PATH"]})
    assert r.returncode == 0 and r.stdout.strip().endswith("None 0"), r.stderr + r.stdout
