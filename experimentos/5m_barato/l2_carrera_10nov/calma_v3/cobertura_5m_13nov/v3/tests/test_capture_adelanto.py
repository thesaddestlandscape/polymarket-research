"""capture_markets v3: identico a main con defectos (diferencial), adelanto incremental, 429 (FIX opt-in), commit/auditoria, solo-adelanto."""
import csv, datetime as dt, importlib.util, json, os, subprocess, sys, threading, time
from pathlib import Path
import pytest
import requests
import universo_5m_io as U

STAGE = Path(__file__).resolve().parent.parent / "stage" / "capture_markets.py"
MAIN = Path("/root/polymarket-research/capture_markets.py")


class Resp:
    def __init__(self, status=200, data=None):
        self.status_code, self._d = status, data

    def raise_for_status(self):
        if self.status_code >= 400:
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


def _cargar(nombre, ruta, monkeypatch, tmp, horizonte="1440", fix="0"):
    monkeypatch.setenv("CAPTURE_5M_HORIZONTE_MIN", horizonte)
    monkeypatch.setenv("CAPTURE_429_FIX", fix)
    spec = importlib.util.spec_from_file_location(nombre, ruta)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    m.DIR_MARKETS = tmp / f"markets_{nombre}"
    m.DIR_MARKETS.mkdir(parents=True, exist_ok=True)   # main exige que exista (lo crea al importar con ruta relativa)
    return m


@pytest.fixture
def cm(tmp_path, monkeypatch):
    monkeypatch.setattr(U, "UNIV_DIR", tmp_path / "u5")
    m = _cargar("cm_v3", STAGE, monkeypatch, tmp_path)
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


def _sin_red(m, monkeypatch):
    monkeypatch.setattr(m, "fetch_coingecko_prices", lambda: {})
    monkeypatch.setattr(m, "guardar_precios", lambda *a, **k: None)
    monkeypatch.setattr(m, "fetch_todos_eventos_crypto", lambda: [])
    monkeypatch.setattr(m, "fetch_todos_updown", lambda: [])


# ---------------------------------------------------------------- (3) identico a main con los defectos
def _red_falsa(modo):
    """requests.get falso comun a main y v3: tag lists con eventos, ventanas por slug; modo '429_tag2' = 429 en la 2a lista de tags."""
    estado = {"n": 0}
    now = int(time.time())

    def get(url, params=None, headers=None, timeout=None):
        estado["n"] += 1
        if "tag_slug" in (params or {}):
            if modo == "429_tag2" and params["tag_slug"] == "bitcoin":
                return Resp(429)
            sl = f"{params['tag_slug'][:3]}-updown-5m-{((now // 300) + 5) * 300}"
            return Resp(200, [_evento(sl)])
        s = params["slug"]
        n = int(s.rsplit("-", 1)[1])
        return Resp(200, [_evento(s)] if n % 2 == 0 else [])
    return get


@pytest.mark.parametrize("modo", ["ok", "429_tag2"])
def test_con_defectos_comportamiento_identico_a_main(tmp_path, monkeypatch, modo):
    monkeypatch.setattr(U, "UNIV_DIR", tmp_path / "u5")
    mm = _cargar("cm_main", MAIN, monkeypatch, tmp_path, horizonte="0", fix="0")
    mv = _cargar("cm_v3d", STAGE, monkeypatch, tmp_path, horizonte="0", fix="0")
    for m in (mm, mv):
        monkeypatch.setattr(m, "fetch_coingecko_prices", lambda: {})
        monkeypatch.setattr(m, "guardar_precios", lambda *a, **k: None)
    monkeypatch.setattr(requests, "get", _red_falsa(modo))
    monkeypatch.setattr(time, "sleep", lambda s: None)
    rm, rv = mm.una_captura(), mv.una_captura()
    assert rm == rv

    def filas(m):
        f = next(m.DIR_MARKETS.glob("*.csv"))
        return [r[1:] for r in csv.reader(f.open(newline=""))]          # sin la marca de tiempo del ciclo
    assert filas(mm) == filas(mv) and len(filas(mm)) > 1
    assert not (tmp_path / "u5").exists()                               # sin pausa, sin estado, sin adelanto
    # bytes de guardar_mercados identicos (misma fila, mismo orden)
    ev = _evento("btc-updown-5m-1794686700")["markets"][0]
    ev.update(_event_id="1", _event_title="t", _event_slug="s", _event_volume24hr="0", _event_tags="Crypto")
    mm.guardar_mercados([ev], "2026-11-14T00:00:00+00:00")
    mv.guardar_mercados([ev], "2026-11-14T00:00:00+00:00")
    assert (mm.DIR_MARKETS / "2026-11-14.csv").read_bytes() == (mv.DIR_MARKETS / "2026-11-14.csv").read_bytes()


def test_fix_429_aborta_sin_guardar_parcial_y_pausa_compartida(tmp_path, monkeypatch):
    monkeypatch.setattr(U, "UNIV_DIR", tmp_path / "u5")
    mv = _cargar("cm_v3f", STAGE, monkeypatch, tmp_path, horizonte="0", fix="1")
    monkeypatch.setattr(mv, "fetch_coingecko_prices", lambda: {})
    monkeypatch.setattr(mv, "guardar_precios", lambda *a, **k: None)
    monkeypatch.setattr(requests, "get", _red_falsa("429_tag2"))
    n, _ = mv.una_captura()
    assert n == 0 and not list(mv.DIR_MARKETS.glob("*.csv"))            # parcial descartado: NO se guarda como completo
    assert U.pausa_activa() > time.time()
    monkeypatch.setattr(requests, "get", _red_falsa("ok"))
    mv.una_captura()                                                     # en pausa: ningun GET, tampoco guarda
    assert not list(mv.DIR_MARKETS.glob("*.csv"))


def test_fix_429_apagado_no_crea_pausa_ni_aborta(tmp_path, monkeypatch):
    monkeypatch.setattr(U, "UNIV_DIR", tmp_path / "u5")
    mv = _cargar("cm_v3x", STAGE, monkeypatch, tmp_path, horizonte="0", fix="0")
    monkeypatch.setattr(mv, "fetch_coingecko_prices", lambda: {})
    monkeypatch.setattr(mv, "guardar_precios", lambda *a, **k: None)
    monkeypatch.setattr(requests, "get", _red_falsa("429_tag2"))
    mv.una_captura()
    assert U.pausa_activa() == 0 and list(mv.DIR_MARKETS.glob("*.csv"))   # guarda la lista parcial exactamente como main


def test_cabecera_identica_a_main(cm):
    cab = MAIN.read_text().split("CABECERA_MARKETS = [")[1].split("]")[0]
    assert [c.strip().strip('",') for c in cab.replace("\n", "").split(",") if c.strip()] == cm.CABECERA_MARKETS
    real = Path("/root/polymarket-research/data/markets/2026-11-13.csv")
    if real.exists():
        assert real.open().readline().strip() == ",".join(cm.CABECERA_MARKETS)


def test_horizonte_cero_no_hace_nada(cm):
    mk, ft, c = cm.fetch_updown_5m_adelanto(horizonte_min=0)
    assert (mk, ft) == ([], []) and cm.llamadas == []


# ---------------------------------------------------------------- adelanto
def test_data_markets_no_cambia_y_adelanto_va_a_universo_5m(cm, monkeypatch):
    _sin_red(cm, monkeypatch)
    cm.MAX_LOTES_CICLO = 3
    cm.una_captura()
    principal = list(cm.DIR_MARKETS.glob("*.csv"))
    assert len(principal) == 1 and sum(1 for _ in principal[0].open()) == 1          # solo cabecera
    ad = list(U.UNIV_DIR.glob("adelanto_*.csv"))
    filas = list(csv.reader(ad[0].open(newline="")))
    assert filas[0] == cm.CABECERA_MARKETS and len(filas) - 1 == 3 * cm.LOTE_SLUGS
    mk, _ = U.leer(directorio=U.UNIV_DIR)
    assert len(mk) == 3 * cm.LOTE_SLUGS and all(r["fuente"] == "capture" for r in mk.values())


def test_relleno_incremental_nearest_first_e_idempotente(cm):
    now = int(time.time())
    primeros = []
    for _ in range(10):
        mk, ft, c = _ciclo(cm, now)
        if not ft:
            break
        primeros.append(min(int(r["inicio_ts"]) for r in ft))
    assert primeros == sorted(primeros) and len(primeros) >= 3
    siguiente = ((now // 300) + 1) * 300
    n_esp = len(range(siguiente + 900, now + 1440 * 60 + 1, 300))
    assert len(U.leer(now, U.UNIV_DIR)[0]) == 6 * n_esp and 280 <= n_esp <= 290
    ll = len(cm.llamadas)
    assert _ciclo(cm, now)[1] == [] and len(cm.llamadas) == ll
    assert all(sum(1 for k, _ in p if k == "slug") <= cm.LOTE_SLUGS for p in cm.llamadas)


def test_cubre_lo_que_ya_trajo_el_listener(cm):
    now = int(time.time())
    t0 = ((now // 300) + 1) * 300 + 900
    U.escribir([U.parsear_nuevo({"id": "99", "market": "0xc99", "slug": f"btc-updown-5m-{t0}", "assets_ids": ["5", "6"],
                                 "outcomes": ["Up", "Down"]}, int(time.time() * 1000))], U.UNIV_DIR)
    assert f"btc-updown-5m-{t0}" not in {r["slug"] for r in cm.fetch_updown_5m_adelanto(ahora_ts=now)[1]}


def test_lote_fallido_se_reintenta_y_no_se_da_por_hecho(cm):
    now = int(time.time())
    cm.modo = "500"
    mk, ft, c = cm.fetch_updown_5m_adelanto(ahora_ts=now)
    assert ft == [] and c["lotes_fallidos"] == 3 and c["lotes"] == 3 and not cm._RAFAGA["abortada"]
    cm.modo = "lista_rota"
    assert cm.fetch_updown_5m_adelanto(ahora_ts=now)[2]["lotes_fallidos"] == 3
    cm.modo = "ok"
    assert len(_ciclo(cm, now)[1]) > 0


def test_inexistentes_no_se_marcan_y_se_reintentan(cm):
    now = int(time.time())
    lejos = ((now // 300) + 1) * 300 + 900 + 300 * 280
    cm.no_existen = {f"{a}-updown-5m-{t}" for a in cm.UPDOWN_ASSETS for t in range(lejos, lejos + 3000, 300)}
    for _ in range(8):
        if not _ciclo(cm, now)[1]:
            break
    assert not any(int(r["inicio_ts"]) >= lejos for r in U.leer(now, U.UNIV_DIR)[0].values())
    cm.no_existen = ()
    assert any(int(r["inicio_ts"]) >= lejos for r in cm.fetch_updown_5m_adelanto(ahora_ts=now + 301)[1])


def test_evento_sin_tokens_validos_no_se_da_por_hecho(cm):
    orig = cm._GET["fn"]

    def sin_tokens(url, params):
        r = orig(url, params)
        for ev in r._d:
            ev["markets"][0]["clobTokenIds"] = "[]"
        return r
    cm._GET["fn"] = sin_tokens
    mk, ft, c = cm.fetch_updown_5m_adelanto(ahora_ts=int(time.time()))
    assert ft == [] and c["tokens_invalidos"] > 0


# ---------------------------------------------------------------- 429 del adelanto
def test_429_adelanto_aborta_y_pausa_compartida(cm):
    cm.modo = "429"
    now = int(time.time())
    mk, ft, c = cm.fetch_updown_5m_adelanto(ahora_ts=now)
    assert c["abortado_429"] and len(cm.llamadas) == 1 and ft == [] and U.pausa_activa(now) > now
    cm._RAFAGA["abortada"] = False
    n = len(cm.llamadas)
    assert cm.fetch_updown_5m_adelanto(ahora_ts=now)[2]["en_pausa"] and len(cm.llamadas) == n   # otro ciclo/proceso: en pausa


def test_pausa_usa_universo_5m_io_no_copia(cm):
    assert not hasattr(cm, "_pausa_tras_429")                           # (9) sin duplicado; solo _pausa_local de respaldo
    assert cm.U is U


# ---------------------------------------------------------------- (7) commit primero, auditoria despues, sin repetir llamadas
def test_commit_de_tokens_primero_y_fallo_se_reintenta_sin_gamma(cm, monkeypatch):
    _sin_red(cm, monkeypatch)
    cm.MAX_LOTES_CICLO = 2
    orden = []
    real_escribir, real_guardar = U.escribir, cm.guardar_mercados
    monkeypatch.setattr(U, "escribir", lambda f, d=None: (orden.append("tokens"), real_escribir(f, d))[1])
    monkeypatch.setattr(cm, "guardar_mercados", lambda m, ts, archivo=None: (orden.append("auditoria"), real_guardar(m, ts, archivo))[1])
    cm.una_captura()
    assert orden.index("tokens") < len(orden) - 1 and orden[-2:] == ["tokens", "auditoria"]
    # fallo del commit: sin auditoria, filas retenidas, el ciclo siguiente reintenta SIN llamar a gamma
    n_gets = len(cm.llamadas)
    monkeypatch.setattr(U, "escribir", lambda f, d=None: (_ for _ in ()).throw(OSError("disco lleno")))
    cm.una_captura()
    assert len(cm._COLA_COMMIT) == 1 and len(cm.llamadas) == n_gets + 2    # 2 lotes del ciclo fallido; commit retenido
    n2 = len(cm.llamadas)
    cm.una_captura()                                                         # sigue fallando: ninguna llamada nueva a gamma
    assert len(cm.llamadas) == n2 and len(cm._COLA_COMMIT) == 1
    monkeypatch.setattr(U, "escribir", real_escribir)
    cm.una_captura()                                                         # disco ok: confirma lo pendiente (sin duplicar) y sigue
    assert cm._COLA_COMMIT == []
    mk, st = U.leer(directorio=U.UNIV_DIR)
    assert st["conflictos"] == 0


def test_fallo_de_auditoria_no_repite_ni_pierde_tokens(cm, monkeypatch):
    _sin_red(cm, monkeypatch)
    cm.MAX_LOTES_CICLO = 2
    monkeypatch.setattr(cm, "guardar_mercados", lambda *a, **k: (_ for _ in ()).throw(OSError("sin espacio")))
    cm.una_captura()
    assert len(U.leer(directorio=U.UNIV_DIR)[0]) == 2 * cm.LOTE_SLUGS and cm._COLA_COMMIT == []


# ---------------------------------------------------------------- cron: --solo-adelanto
def test_solo_adelanto_hasta_completar_y_una_instancia(cm, monkeypatch):
    assert cm.solo_adelanto(rondas=8) == 0
    now = int(time.time())
    siguiente = ((now // 300) + 1) * 300
    assert len(U.leer(now, U.UNIV_DIR)[0]) == 6 * len(range(siguiente + 900, now + 1440 * 60 + 1, 300))
    import fcntl
    fd = os.open(U.UNIV_DIR / ".solo_adelanto.lock", os.O_RDWR)
    fcntl.flock(fd, fcntl.LOCK_EX)                                           # otra instancia en curso
    n = len(cm.llamadas)
    assert cm.solo_adelanto() == 0 and len(cm.llamadas) == n
    os.close(fd)


def test_solo_adelanto_apagado_con_horizonte_cero(tmp_path, monkeypatch):
    monkeypatch.setattr(U, "UNIV_DIR", tmp_path / "u5")
    m = _cargar("cm_off", STAGE, monkeypatch, tmp_path, horizonte="0")
    assert m.solo_adelanto() == 0 and not (tmp_path / "u5").exists()


def test_sin_modulo_io_adelanto_y_fix_apagados(tmp_path):
    d = tmp_path / "solo"
    d.mkdir()
    (d / "capture_markets.py").write_text(STAGE.read_text())
    (d / "data_quality.py").write_text("def validar_precio(*a): return True,''\ndef fetch_coinbase_spot(*a, **k): return {}\ndef validar_cross_source(*a, **k): return {}\n")
    r = subprocess.run([sys.executable, "-I", "-c", "import sys; sys.path.insert(0,%r); import capture_markets as c; print(c.U, c.HORIZONTE_5M_MIN, c.FIX_429)" % str(d)],
                       capture_output=True, text=True, env={"CAPTURE_5M_HORIZONTE_MIN": "1440", "CAPTURE_429_FIX": "1", "PATH": os.environ["PATH"]})
    assert r.returncode == 0 and r.stdout.strip().endswith("None 0 False"), r.stderr + r.stdout


def test_activacion_por_fichero_cfg_y_el_entorno_manda(tmp_path, monkeypatch):
    monkeypatch.setattr(U, "UNIV_DIR", tmp_path / "u5")
    monkeypatch.delenv("CAPTURE_5M_HORIZONTE_MIN", raising=False)
    monkeypatch.delenv("CAPTURE_429_FIX", raising=False)

    def cargar():
        spec = importlib.util.spec_from_file_location("cm_cfg", STAGE)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        return m
    m = cargar()
    assert (m.HORIZONTE_5M_MIN, m.FIX_429) == (0, False)                       # sin nada: identico a main
    (tmp_path / "u5").mkdir()
    (tmp_path / "u5" / "cfg_CAPTURE_5M_HORIZONTE_MIN").write_text("1440\n")
    (tmp_path / "u5" / "cfg_CAPTURE_429_FIX").write_text("1")
    m = cargar()
    assert (m.HORIZONTE_5M_MIN, m.FIX_429) == (1440, True)
    monkeypatch.setenv("CAPTURE_5M_HORIZONTE_MIN", "0")
    assert cargar().HORIZONTE_5M_MIN == 0                                      # el entorno gana
    monkeypatch.delenv("CAPTURE_5M_HORIZONTE_MIN")
    (tmp_path / "u5" / "cfg_CAPTURE_5M_HORIZONTE_MIN").write_text("basura")
    assert cargar().HORIZONTE_5M_MIN == 0                                      # ilegible -> apagado
    (tmp_path / "u5" / "cfg_CAPTURE_5M_HORIZONTE_MIN").write_text("-5")
    assert cargar().HORIZONTE_5M_MIN == 0                                      # negativo -> apagado
