"""Tests sinteticos del parche de robustez de B (h47_robustez). Todo en seco/tmp: no toca el ledger, el lock ni el cliente reales."""
import gzip, hashlib, json, os, signal, subprocess, sys, time
from pathlib import Path
import pytest
sys.path.insert(0, str(Path(__file__).resolve().parent))
import test_experimento_maker_h47 as T
import experimento_maker_h47 as H
import experimento_pares_cola_15m as X
import h47_robustez as R

AQUI = Path(__file__).resolve().parent
PY = sys.executable


@pytest.fixture(autouse=True)
def _limpia_avisos():
    R.AVISOS.clear()
    R._STOP.clear()
    yield
    R.AVISOS.clear()
    R._STOP.clear()


@pytest.fixture(autouse=True)
def _dirs(tmp_path, monkeypatch):
    monkeypatch.setattr(R, "DIR", tmp_path)
    monkeypatch.setattr(R, "RECON_OUT", str(tmp_path / "puja_fin_reconstruido.jsonl"))
    return tmp_path


def iso(t):
    return time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime(t)) + ".000+00:00"


def ledger_a_mitad(tmp, ini, con_cierre=True, relleno=5.0):
    """Ledger de un proceso muerto a mitad de puja (sin puja_fin)."""
    slug = f"eth-updown-5m-{ini}"
    f = [dict(tipo="puja_post", oid="0xaa", slug=slug, coin="eth", lado="YES", k=2, precio=0.18, size=5, ts=iso(ini + 10), real=True),
         dict(tipo="lectura", oid="0xaa", f=relleno, precio=0.18, ts=iso(ini + 100), real=True)]
    if con_cierre:
        f.append(dict(tipo="cierre_mercado", slug=slug, motivo="t_stop", real=True))
    p = tmp / "ledger.jsonl"
    p.write_text("".join(json.dumps(d) + "\n" for d in f))
    return slug, f, p


def escribir_mids(tmp, ledger, slug, ini, hasta, puntos):
    p = R._ruta_mids(ledger, hasta)
    with gzip.open(p, "ab") as g:
        g.write((json.dumps({"slug": slug, "lado": "YES", "tok": "tU", "fin": ini + 300.0, "desde_idx": 0, "hasta": hasta, "m": puntos}) + "\n").encode())


def test_mark_s_igual_al_ejecutor():
    assert R.MARK_S == H.MARK_S


# ---- (a) reinicio a mitad de puja
def test_huerfana_reinicio_a_mitad_de_puja_idempotente_y_sin_tocar_ledger(tmp_path):
    ini = int(time.time()) - 1000
    slug, filas, led = ledger_a_mitad(tmp_path, ini)
    h0 = hashlib.sha256(led.read_bytes()).hexdigest()
    # mids persistidos por el proceso muerto, cobertura hasta ini+150: t0=ini+100 -> +5 s y +30 s cubiertos, +120 s NO (missing, nunca 0)
    escribir_mids(tmp_path, led, slug, ini, ini + 150, [[ini + 50, 0.20], [ini + 104, 0.22], [ini + 120, 0.24]])
    n, ya, regs = R.recuperar_huerfanas(filas, led, ahora=time.time(), posic={})
    assert (n, ya, len(regs)) == (1, 0, 1)
    r = regs[0]
    assert r["slug"] == slug and r["relleno_real"] is True and r["llenas_detectadas"] == 5.0 and r["fin_puja"] == "t_stop"
    rl = r["rellenos"][0]
    assert rl["mid_5s"] == 0.22 and abs(rl["markout_5s"] - (0.22 - 0.18) / 0.18) < 1e-9
    assert rl["mid_30s"] == 0.24
    assert rl["mid_120s"] is None and rl["markout_120s"] is None            # fuera de cobertura: missing
    out = [json.loads(l) for l in open(R.RECON_OUT)]
    assert len(out) == 1
    n2, ya2, _ = R.recuperar_huerfanas(filas, led, ahora=time.time(), posic={})   # 2o arranque: idempotente
    assert n2 == 0 and ya2 == 1 and len(open(R.RECON_OUT).read().splitlines()) == 1
    assert hashlib.sha256(led.read_bytes()).hexdigest() == h0               # el ledger no se toca


def test_huerfana_sin_mids_persistidos_markouts_missing_y_no_candidata_si_aun_no_cerro(tmp_path):
    ini = int(time.time()) - 1000
    slug, filas, led = ledger_a_mitad(tmp_path, ini)
    n, _, regs = R.recuperar_huerfanas(filas, led, posic={})
    assert regs[0]["markouts"] == "missing"                                  # script original: missing, no 0
    ini2 = int(time.time()) - 100                                            # su cierre (ini+300) no ha pasado
    _, filas2, led2 = ledger_a_mitad(tmp_path, ini2)
    assert R.recuperar_huerfanas(filas2, led2, posic={})[2] == []


def test_huerfana_con_puja_fin_ya_en_ledger_no_se_reconstruye(tmp_path):
    ini = int(time.time()) - 1000
    slug, filas, led = ledger_a_mitad(tmp_path, ini)
    filas.append(dict(tipo="puja_fin", slug=slug, real=True))
    assert R.recuperar_huerfanas(filas, led, posic={})[2] == []


def test_mids_gz_truncado_o_corrupto_no_rompe(tmp_path):
    ini = int(time.time()) - 1000
    slug, filas, led = ledger_a_mitad(tmp_path, ini)
    escribir_mids(tmp_path, led, slug, ini, ini + 150, [[ini + 104, 0.22]])
    p = R._ruta_mids(led, ini + 150)
    with open(p, "ab") as f:
        f.write(gzip.compress(b'{"slug": "x"}\n')[:-6])                    # miembro final truncado (SIGKILL a mitad de volcado)
    assert slug in R.leer_mids(led, ahora=ini + 150)
    n, _, regs = R.recuperar_huerfanas(filas, led, ahora=time.time(), posic={})
    assert n == 1 and regs[0]["rellenos"][0]["mid_5s"] == 0.22


# ---- (c) volcado incremental
def test_volcar_mids_incremental_sin_duplicar_y_solo_con_puja(tmp_path):
    ex = T.nuevo("volcado", real=False)
    c = T.ctx_de(ex, "eth")
    t0 = time.time()
    assert R.volcar_mids(ex, c, X.LEDGER, forzar=True) == 0                  # sin cara elegida: nada
    c.tok, c.hashes = "tU", ["seco-1"]
    c.lib.mids["tU"] = [(t0, 0.20), (t0 + 1, 0.21)]
    c.lib.ult_msg = t0 + 2
    assert R.volcar_mids(ex, c, X.LEDGER, ahora=t0 + 2) == 2
    assert R.volcar_mids(ex, c, X.LEDGER, ahora=t0 + 3) == 0                 # rate-limit
    c.lib.mids["tU"].append((t0 + 5, 0.23))
    c.lib.ult_msg = t0 + 20
    assert R.volcar_mids(ex, c, X.LEDGER, ahora=t0 + 20) == 1
    assert R.vaciar()
    e = R.leer_mids(X.LEDGER, ahora=t0 + 20)[c.mk["slug"]]
    assert [m for _, m in e["m"]] == [0.20, 0.21, 0.23] and e["hasta"] == t0 + 20


def test_tick_nunca_lanza_aunque_falle_la_escritura(tmp_path, monkeypatch, capfd):
    ex = T.nuevo("tickfalla", real=False)
    c = T.ctx_de(ex, "eth")
    c.tok, c.hashes = "tU", ["seco-1"]
    c.lib.mids["tU"] = [(time.time(), 0.2)]
    R.AVISOS.clear()
    monkeypatch.setattr(R, "DIR", Path("/proc/no_se_puede_escribir"))
    R.tick(ex, c)                                                            # no lanza (el fallo es del escritor aparte)
    assert R.vaciar()
    c._h47r_t = 0.0
    c.lib.mids["tU"].append((time.time(), 0.21))
    R.tick(ex, c)
    assert R.vaciar()
    assert capfd.readouterr().err.count("escritor de mids fallido") == 1     # aviso una sola vez
    R.tick(ex, c)                                                            # el aviso del hilo escritor llega al LEDGER por el hilo principal
    assert any(e["tipo"] == "aviso_robustez" and "escritor" in e["msg"] for e in T.eventos())


# ---- (b) entre cierre_mercado y finalizar / salida
def _ctx_asentando(ex):
    c = T.ctx_de(ex, "eth", fin_en=100.0)
    c.tok, c.hashes, c.fase, c.posteado, c.motivo_cierre = "tU", ["seco-1"], "asentando", True, "t_stop"
    t0 = time.time()
    c.lib.mids["tU"] = [(t0 - 1, 0.20), (t0 + 0.0, 0.22)]
    c.estado["tU"]["rellenos"] = [{"oid": "seco-1", "acc": 5.0, "precio": 0.18, "t_deteccion": t0 - 0.5, "mid0": 0.2}]
    c.estado["tU"]["llenas"] = 5.0
    return c


def test_salida_entre_cierre_y_finalizar_escribe_puja_fin_parcial_una_sola_vez():
    ex = T.nuevo("salida", real=False)
    c = _ctx_asentando(ex)
    ex._log47({"tipo": "cierre_mercado", "slug": c.mk["slug"], "motivo": "t_stop", "T": 60.0})
    R.finalizar_al_salir(ex)
    R.finalizar_al_salir(ex)                                                 # idempotente
    fin = T.eventos("puja_fin")
    assert len(fin) == 1
    f = fin[0]
    assert f["interrumpida"] is True and f["relleno_cota_inferior"] is True and f["relleno_real"] is None or f["relleno_real"] is not False
    assert f["llenas_detectadas"] == 5.0 and f["fin_puja"] == "t_stop"
    r = f["rellenos"][0]
    assert r["mid_5s"] is None and r["markout_5s"] is None                  # t0+5 s aun no ha ocurrido: missing, no 0
    mf = T.eventos("mercado_fin")                                           # hallazgo 9: el parcial tambien emite mercado_fin (interrumpida)
    assert len(mf) == 1 and mf[0]["interrumpida"] is True and mf[0]["slug"] == c.mk["slug"] and mf[0]["trades_propios"] == "missing"


def test_salida_no_duplica_si_finalizar_ya_corrio_ni_toca_mercados_sin_puja():
    ex = T.nuevo("salida2", real=False)
    c = _ctx_asentando(ex)
    c.fase = "espera_fin"
    ex.finalizar(c)                                                          # camino normal
    c2 = T.ctx_de(ex, "sol")                                                 # mercado sin puja (c.hashes vacio)
    R.finalizar_al_salir(ex)
    assert len(T.eventos("puja_fin")) == 1 and "interrumpida" not in T.eventos("puja_fin")[0]


def test_primera_senal_ya_finaliza_por_el_camino_normal_y_el_atexit_no_duplica():
    ex = T.nuevo("senal1", real=False)
    c = _ctx_asentando(ex)
    c.fase = "espera_fin"
    ex._senal()                                                              # 1a SIGTERM del supervisor: ex.senal = True
    assert ex.senal is True
    ex.paso_seguro(c)                                                        # paso(): espera_fin + senal -> finalizar()
    assert len(T.eventos("puja_fin")) == 1 and c.fase in ("fin",) or ex.ctxs[c.mk["slug"]] == "terminado"
    R.finalizar_al_salir(ex)
    assert len(T.eventos("puja_fin")) == 1


def test_finalizar_al_salir_fail_safe_ante_ctx_roto(capfd):
    ex = T.nuevo("roto", real=False)
    c = _ctx_asentando(ex)
    c.estado["tU"]["rellenos"] = [{"corrupto": 1}]                           # ctx corrupto
    R.finalizar_al_salir(ex)                                                 # no lanza
    assert "puja_fin parcial fallido" in capfd.readouterr().err


# ---- procesos reales (hijo): SIGTERM x2 -> SystemExit -> atexit ; SIGKILL con volcado incremental
def _lanza(modo, tmp):
    env = dict(os.environ, H47R_DIR=str(tmp), PYTHONPATH="/root/polymarket-research-dev")
    p = subprocess.Popen([PY, str(AQUI / "_hijo_h47r.py"), modo], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, env=env)
    info = {}
    for _ in range(200):
        ln = p.stdout.readline().strip()
        if ln == "READY":
            break
        if "=" in ln:
            k, v = ln.split("=", 1)
            info[k] = v
        if p.poll() is not None:
            raise AssertionError(p.stderr.read())
    return p, info


def test_proceso_dos_sigterm_escriben_puja_fin_parcial(tmp_path):
    p, info = _lanza("sleep", tmp_path)
    p.send_signal(signal.SIGTERM)
    time.sleep(0.4)
    assert p.poll() is None                                                  # 1a señal: pide parar, no corta (harness)
    p.send_signal(signal.SIGTERM)
    p.wait(timeout=15)
    filas = [json.loads(l) for l in open(info["LEDGER"])]
    fin = [d for d in filas if d.get("tipo") == "puja_fin"]
    assert p.returncode == 130 and len(fin) == 1 and fin[0]["interrumpida"] is True and fin[0]["slug"] == info["SLUG"]
    # hallazgo 1: cerrar_salida (cancelacion) se invoca ANTES de cualquier registro del parche; sin I/O previa (ni mids ni puja_fin)
    tipos = [d.get("tipo") for d in filas]
    assert "cs_marca" in tipos and tipos.index("cs_marca") < tipos.index("puja_fin")
    assert [d for d in filas if d.get("tipo") == "cs_marca"][0]["mids_antes"] == 0
    assert fin[0]["post_cerrar_salida"] is True
    # hallazgo 9: mercado_fin parcial emitido tras el puja_fin; hallazgo 5: en seco no hay hilo ni escritura en el reconstruido
    assert "mercado_fin" in tipos and tipos.index("mercado_fin") > tipos.index("puja_fin")
    assert not (tmp_path / "puja_fin_reconstruido.jsonl").exists()


def test_proceso_sigkill_deja_mids_y_la_huerfana_se_recupera_con_markouts(tmp_path):
    p, info = _lanza("tick", tmp_path)
    time.sleep(1.5)
    p.kill()
    p.wait(timeout=10)
    led = Path(info["LEDGER"])
    filas = [json.loads(l) for l in open(led)]
    assert not [d for d in filas if d.get("tipo") == "puja_fin"]            # SIGKILL: nadie escribio puja_fin
    mids = R.leer_mids(led, ahora=time.time())
    assert info["SLUG"] in mids and mids[info["SLUG"]]["hasta"] > 0
    slug = info["SLUG"]
    # el hijo usa un slug con ini = ahora: para que el cierre "ya haya pasado" se reconstruye con ahora desplazado
    ini = int(slug.rsplit("-", 1)[1])
    filas = [dict(d, real=True) for d in filas if d.get("tipo") == "puja_post"] + \
            [dict(tipo="lectura", oid="seco-1", f=5.0, precio=0.18, ts=iso(mids[slug]["hasta"] - 1), real=True)]
    n, _, regs = R.recuperar_huerfanas(filas, led, ahora=ini + 400, posic={})
    assert n == 1 and regs[0]["relleno_real"] is True
    assert regs[0]["rellenos"][0]["mid_5s"] is None or regs[0]["rellenos"][0]["mid_5s"] in (0.2, 0.22)


# ================================================================ 2a /code-review: tests por hallazgo
class _Ex:
    """Stub minimo de Exp47 para probar el orden de salida / el hilo sin mercados."""
    def __init__(self, real=True):
        self.real, self.ctxs, self.llamadas = real, {}, []
        self.vivas, self.canceladas, self.kill, self.senal, self._cerrado = {}, {}, None, False, False

    def cerrar_salida(self):
        self.llamadas.append("cerrar_salida")
        self._cerrado = True


# ---- 1: el finalizador va DESPUES de cerrar_salida
def test_h1_salida_llama_cerrar_salida_antes_que_los_registros(monkeypatch):
    ex = _Ex()
    R._envolver_cerrar_salida(ex)
    monkeypatch.setattr(R, "finalizar_al_salir", lambda e, post_cierre=None: e.llamadas.append(("registros", getattr(e, "_h47r_cs_ok", False))))
    R._salida(ex)
    assert ex.llamadas == ["cerrar_salida", ("registros", True)]                 # hallazgo 4: flag explicito de "cerrar_salida completo OK"


def test_h1_si_cerrar_salida_lanza_los_registros_salen_sin_garantia_de_sin_relleno(monkeypatch):
    ex = _Ex()
    def mal():
        ex.llamadas.append("cerrar_salida")
        raise RuntimeError("red")
    ex.cerrar_salida = mal
    R._envolver_cerrar_salida(ex)
    monkeypatch.setattr(R, "finalizar_al_salir", lambda e, post_cierre=None: e.llamadas.append(("registros", getattr(e, "_h47r_cs_ok", False))))
    with pytest.raises(RuntimeError):
        R._salida(ex)
    assert ex.llamadas == ["cerrar_salida", ("registros", False)]


def test_h1_instalar_registra_un_unico_hook_y_no_toca_el_de_cerrar_salida(monkeypatch):
    import atexit
    ex = T.nuevo("instala", real=False)
    reg, desreg = [], []
    monkeypatch.setattr(atexit, "register", lambda f, *a: reg.append((f, a)))
    monkeypatch.setattr(atexit, "unregister", lambda f: desreg.append(f))
    monkeypatch.setattr(R, "_hilo_huerfanas", lambda *a: None)
    R.instalar(ex)
    assert reg == [(R._salida, (ex,))] and desreg == []                      # nunca se desregistra el cerrar_salida original


# ---- 2: puja_fin parcial tras recoger rellenos; sin falso "sin relleno"; reconstruible
class _Ord:
    def __init__(self, lo=0.0, hi=5.0, abierta=False):
        self.lo, self.hi, self.abierta, self.alias, self.precio = lo, hi, abierta, False, 0.18


_N = [0]


def _ex_real_con_ctx(monkeypatch, ord_=None):
    _N[0] += 1
    ex = T.nuevo(f"real_parcial{_N[0]}", real=True)
    c = _ctx_asentando(ex)
    c.estado["tU"]["rellenos"], c.estado["tU"]["llenas"] = [], 0.0
    o = ord_ or _Ord()
    monkeypatch.setattr(ex, "ordenes", lambda: {"seco-1": o})
    return ex, c


def test_h2_sincroniza_rellenos_tardios_antes_de_resumir(monkeypatch):
    ex, c = _ex_real_con_ctx(monkeypatch)
    def sync(cc):                                                            # simula el relleno que cerrar_salida dejo en el ledger
        cc.estado["tU"]["rellenos"].append({"oid": "seco-1", "acc": 2.0, "precio": 0.18, "t_deteccion": time.time(), "tardio": True})
        cc.estado["tU"]["llenas"] = 2.0
        return 2.0
    monkeypatch.setattr(ex, "sincronizar_rellenos", sync)
    R.finalizar_al_salir(ex, post_cierre=True)
    f = T.eventos("puja_fin")[0]
    assert f["llenas_detectadas"] == 2.0 and f["relleno_real"] is True and f["rellenos_tardios"] == 1 and f["relleno_cota_inferior"] is True


def test_h2_nunca_congela_sin_relleno_falso(monkeypatch):
    ex, c = _ex_real_con_ctx(monkeypatch)
    for post, ord_, kill, esperado in [(True, _Ord(), None, False), (False, _Ord(), None, None),
                                       (True, _Ord(lo=0.0, hi=5.0, abierta=True), None, None), (True, _Ord(), "kill", None)]:
        monkeypatch.setattr(ex, "ordenes", lambda o=ord_: {"seco-1": o})
        ex.kill = kill
        monkeypatch.setattr(ex, "sincronizar_rellenos", lambda cc: 0.0)
        reg = R.resumen_parcial(ex, c, post_cierre=post)
        assert reg["relleno_real"] is esperado and reg["relleno_cota_inferior"] is True
    ex.kill = None
    monkeypatch.setattr(ex, "ordenes", lambda: {"seco-1": _Ord()})
    ex.vivas = {"seco-1": {}}                                                # orden aun viva al salir
    assert R.resumen_parcial(ex, c, post_cierre=True)["relleno_real"] is None
    assert R.resumen_parcial(ex, c, post_cierre=True)["ordenes_vivas_al_salir"] == ["seco-1"]
    ex.vivas = {}


def test_h2_parcial_es_reconstruible_y_el_reconstruido_lo_marca(tmp_path):
    ini = int(time.time()) - 1000
    slug, filas, led = ledger_a_mitad(tmp_path, ini)
    filas.append(dict(tipo="puja_fin", slug=slug, real=True, interrumpida=True, relleno_real=None, llenas_detectadas=0.0))
    n, _, regs = R.recuperar_huerfanas(filas, led, posic={})
    assert n == 1 and regs[0]["sustituye_puja_fin_parcial"] is True and regs[0]["llenas_detectadas"] == 5.0
    filas2 = [d for d in filas if d["tipo"] != "puja_fin"] + [dict(tipo="puja_fin", slug=slug, real=True)]
    assert R.recuperar_huerfanas(filas2, led, posic={})[2] == []             # un puja_fin completo SI cierra el mercado


# ---- 3: gz corrupto -> missing, no excepcion; purgar siempre
def test_h3_gz_con_miembro_corrupto_conserva_lo_anterior(tmp_path):
    ini = int(time.time()) - 1000
    slug, filas, led = ledger_a_mitad(tmp_path, ini)
    escribir_mids(tmp_path, led, slug, ini, ini + 150, [[ini + 104, 0.22]])
    p = R._ruta_mids(led, ini + 150)
    malo = bytearray(gzip.compress(b'{"slug": "x"}\n' * 50))
    for i in range(12, len(malo) - 8):
        malo[i] ^= 0xFF                                                      # zlib.error en mitad de miembro
    with open(p, "ab") as f:
        f.write(bytes(malo))
    mids = R.leer_mids(led, ahora=ini + 150)
    assert mids[slug]["m"] == [(ini + 104, 0.22)]


def test_h3_fichero_no_gzip_o_excepcion_en_open_degradan_a_missing(tmp_path, monkeypatch):
    ini = int(time.time()) - 1000
    slug, filas, led = ledger_a_mitad(tmp_path, ini)
    R._ruta_mids(led, ini + 150).write_bytes(b"esto no es gzip")             # BadGzipFile
    assert R.leer_mids(led, ahora=ini + 150) == {}
    n, _, regs = R.recuperar_huerfanas(filas, led, ahora=time.time(), posic={})
    assert n == 1 and regs[0]["markouts"] == "missing" and regs[0]["rellenos"][0].get("mid_5s") is None
    import zlib
    def boom(*a, **k):
        raise zlib.error("x")
    monkeypatch.setattr(R.gzip, "open", boom)
    assert R.leer_mids(led, ahora=ini + 150) == {}                           # zlib.error al abrir: tampoco lanza


def test_h3_leer_mids_que_lanza_no_impide_escribir_la_huerfana(tmp_path, monkeypatch):
    ini = int(time.time()) - 1000
    slug, filas, led = ledger_a_mitad(tmp_path, ini)
    monkeypatch.setattr(R, "leer_mids", lambda *a, **k: (_ for _ in ()).throw(ValueError("x")))
    n, _, regs = R.recuperar_huerfanas(filas, led, posic={})
    assert n == 1 and regs[0]["markouts"] == "missing"


def test_h3_purgar_viejos_corre_en_instalar_real_y_seco(tmp_path, monkeypatch):
    import atexit
    monkeypatch.setattr(atexit, "register", lambda f, *a: None)
    monkeypatch.setattr(R, "_hilo_huerfanas", lambda *a: None)
    for real in (False, True):
        viejo = tmp_path / f"h47_mids_x_2020-01-01_{int(real)}.jsonl.gz"
        viejo.write_bytes(b"x")
        os.utime(viejo, (1000, 1000))
        R.instalar(T.nuevo(f"purga{int(real)}", real=real))
        assert not viejo.exists()


def test_h3_fallo_de_recuperacion_avisa_al_ledger(monkeypatch):
    monkeypatch.setattr(R, "ARRANQUE_DIFERIDO_S", 0.0)
    monkeypatch.setattr(R, "_cargar_rpf", lambda: (_ for _ in ()).throw(RuntimeError("sin vendor")))
    R._hilo_huerfanas(_Ex(), Path("x"))
    assert any("recuperacion de huerfanas fallida" in a for a in R.AVISOS)


def test_h3_hueco_en_volcados_no_extiende_la_cobertura(tmp_path):
    ini = int(time.time()) - 1000
    slug = f"eth-updown-5m-{ini}"
    def vol(desde, hasta, pts):
        with gzip.open(R._ruta_mids("l.jsonl", hasta), "ab") as g:
            g.write((json.dumps({"slug": slug, "lado": "YES", "tok": "t", "fin": ini + 300.0, "desde_idx": desde, "hasta": hasta, "m": pts}) + "\n").encode())
    vol(0, ini + 10, [[ini + 5, 0.2]])
    vol(5, ini + 100, [[ini + 90, 0.3]])                                     # el volcado idx 1..4 se perdio
    e = R.leer_mids("l.jsonl", ahora=ini + 100)[slug]
    assert e["hueco"] is True and e["hasta"] == ini + 10 and (ini + 90, 0.3) in e["m"]
    reg = {"slug": slug, "rellenos": [{"t_deteccion": ini + 80, "precio": 0.2}]}
    R.aplicar_markouts(reg, {slug: e})
    assert reg["rellenos"][0]["mid_5s"] is None                              # t0+5 = ini+85 > hasta: missing


# ---- 4: huerfanas con ordenes sin verificar se difieren
def _ledger_real_con_orden(tmp, ini, f=2.0, verificada=False, oid="0xbb"):
    import pares_contabilidad as C
    slug = f"eth-updown-5m-{ini}"
    base = dict(oid=oid, slug=slug, tok="tU", lado="YES", precio=0.18, size=5, real=True)
    filas = [dict(base, tipo="intencion_post", ts=iso(ini + 5)), dict(base, tipo="puja_post", coin="eth", k=2, ts=iso(ini + 10)),
             dict(tipo="lectura", oid=oid, f=f, precio=0.18, ts=iso(ini + 100), real=True),
             dict(tipo="cierre_mercado", slug=slug, motivo="t_stop", real=True)]
    if verificada:
        filas += [dict(tipo="fuera_libro", oid=oid, ts=iso(ini + 110), real=True),
                  dict(tipo="verificada", oid=oid, f=f, ts=iso(ini + 110 + C.T_VERIF_S + 5), real=True)]
    p = tmp / "l.jsonl"
    p.write_text("".join(json.dumps(d) + "\n" for d in filas))
    return slug, p


def test_h4_slug_con_orden_sin_verificar_se_difiere_y_luego_se_reconstruye(tmp_path):
    ini = int(time.time()) - 1000
    slug, led = _ledger_real_con_orden(tmp_path, ini, verificada=False)
    rpf = R._cargar_rpf()
    ex = _Ex(real=True)
    n, ya, regs, dif, _ = R.pasada_huerfanas(ex, led, rpf, ahora=time.time(), posic={})
    assert (n, regs, dif) == (0, [], [slug]) and not os.path.exists(R.RECON_OUT)
    slug, led = _ledger_real_con_orden(tmp_path, ini, verificada=True)       # verificar() ya corrio
    n, ya, regs, dif, _ = R.pasada_huerfanas(ex, led, rpf, ahora=time.time(), posic={})
    assert n == 1 and dif == [] and regs[0]["slug"] == slug and regs[0]["llenas_detectadas"] == 2.0


def test_h4_no_toca_slugs_de_este_proceso(tmp_path):
    ini = int(time.time()) - 1000
    slug, led = _ledger_real_con_orden(tmp_path, ini, verificada=True)
    ex = _Ex(real=True)
    ex.ctxs[slug] = type("C", (), {"mk": {"slug": slug}})()
    assert R.pasada_huerfanas(ex, led, R._cargar_rpf(), ahora=time.time(), posic={})[:2] == (0, 0)


def test_h4_el_hilo_reintenta_solo_los_diferidos_recientes_con_tope_bajo(monkeypatch):
    monkeypatch.setattr(R, "ARRANQUE_DIFERIDO_S", 0.0)
    monkeypatch.setattr(R, "REINTENTO_S", 0.01)
    monkeypatch.setattr(R, "_cargar_rpf", lambda: object())
    ini = int(time.time()) - 3600
    s1, viejo = f"eth-updown-5m-{ini}", f"eth-updown-5m-{ini - 3 * 86400}"
    res = iter([(0, 0, [], [s1, viejo], []), (1, 0, [{}], [], [])])
    llamadas = []
    monkeypatch.setattr(R, "pasada_huerfanas", lambda *a, **k: llamadas.append(k.get("solo")) or next(res))
    R._hilo_huerfanas(_Ex(), Path("x"))
    assert llamadas == [None, [s1]]                                           # 2a pasada: solo el diferido de las ultimas 24 h
    llamadas.clear()
    monkeypatch.setattr(R, "pasada_huerfanas", lambda *a, **k: llamadas.append(1) or (0, 0, [], [s1], []))
    R._hilo_huerfanas(_Ex(), Path("x"))
    assert len(llamadas) == R.MAX_PASOS == 6
    assert any("siguen esperando" in a for a in R.AVISOS)


def test_h3_pasada_foto_de_propios_antes_de_leer_y_margen_con_fin_espera(tmp_path):
    ahora = time.time()
    ini = int(ahora) - 300 - 70; ini -= ini % 300                              # fin hace ~70-370 s
    slug, led = _ledger_real_con_orden(tmp_path, ini, verificada=True)
    rpf = R._cargar_rpf()
    ex = _Ex(real=True)
    fin = ini + 300
    assert R.pasada_huerfanas(ex, led, rpf, ahora=fin + R.FIN_ESPERA_S + R.HOLGURA_S - 1, posic={})[:2] == (0, 0)   # aun en margen
    assert R.pasada_huerfanas(ex, led, rpf, ahora=fin + R.FIN_ESPERA_S + R.HOLGURA_S + 1, posic={})[0] == 1
    # la foto de propios se toma ANTES de abrir el ledger
    orden = []
    class Cache:
        filas = []
        def refrescar(self):
            orden.append("ledger")
    class Ctxs(dict):
        def values(self):
            orden.append("ctxs")
            return super().values()
    ex2 = _Ex(real=True)
    ex2.ctxs = Ctxs()
    R.pasada_huerfanas(ex2, led, None, ahora=ahora, cache=Cache())
    assert orden == ["ctxs", "ledger"]


def test_h3_flag_y_constantes_coinciden_con_el_ejecutor():
    assert R.FIN_ESPERA_S == H.FIN_ESPERA_S and R.UMBRAL_WS_S == X.WS_MAX_S


# ---- 5: solo ejecutor real
def test_h5_en_seco_no_arranca_el_hilo_de_huerfanas_y_en_real_si(monkeypatch):
    import atexit
    monkeypatch.setattr(atexit, "register", lambda f, *a: None)
    lanzados = []
    monkeypatch.setattr(R, "_hilo_huerfanas", lambda ex, led: lanzados.append(ex.real))
    R.instalar(T.nuevo("seco_h5", real=False))
    R.instalar(T.nuevo("real_h5", real=True))
    for _ in range(100):
        if len(lanzados) == 1:
            break
        time.sleep(0.01)
    time.sleep(0.05)
    assert lanzados == [True]


# ---- 6: vendorizado con hash
def test_h6_vendor_junto_al_modulo_y_hash_coincide():
    assert R.RPF_VENDOR.parent == Path(R.__file__).resolve().parent
    assert hashlib.sha256(R.RPF_VENDOR.read_bytes()).hexdigest() == R.RPF_SHA256
    assert R._cargar_rpf().OUT == R.RECON_OUT
    orig = AQUI.parent / "etiquetado_pasivo" / "scripts" / "reconstruir_puja_fin.py"
    if orig.exists():
        assert hashlib.sha256(orig.read_bytes()).hexdigest() == R.RPF_SHA256   # sigue siendo copia literal del original revisado


def test_h6_falta_o_hash_distinto_no_ejecuta_nada_y_avisa_al_ledger(tmp_path, monkeypatch):
    marca = tmp_path / "ejecutado"
    falso = tmp_path / "vendor.py"
    falso.write_text(f"open({str(marca)!r}, 'w').write('x')\n")
    monkeypatch.setattr(R, "RPF_VENDOR", falso)
    with pytest.raises(RuntimeError, match="hash"):
        R._cargar_rpf()
    assert not marca.exists()                                                # el codigo con hash distinto NO se ejecuta
    monkeypatch.setattr(R, "RPF_VENDOR", tmp_path / "no_existe.py")
    with pytest.raises(RuntimeError, match="falta"):
        R._cargar_rpf()
    monkeypatch.setattr(R, "ARRANQUE_DIFERIDO_S", 0.0)
    R._hilo_huerfanas(_Ex(), Path("x"))
    ex = T.nuevo("aviso_vendor", real=False)
    c = T.ctx_de(ex, "eth")
    c.tok, c.hashes = "tU", ["seco-1"]
    R.tick(ex, c)                                                            # el hilo principal vuelca el aviso al ledger
    assert any(e["tipo"] == "aviso_robustez" and "huerfanas fallida" in e["msg"] for e in T.eventos())


def test_h6_el_modulo_no_carga_codigo_por_ruta_absoluta_de_main():
    src = Path(R.__file__).read_text()
    assert "/root/polymarket-research/experimentos" not in src and "H47R_RPF" not in src


# ---- 7: tick sin I/O sincrono ni imports en el hot path
def test_h7_tick_no_escribe_en_el_hilo_llamante_y_no_importa_ledger(monkeypatch):
    ex = T.nuevo("hot", real=False)
    c = T.ctx_de(ex, "eth")
    c.tok, c.hashes = "tU", ["seco-1"]
    c.lib.mids["tU"] = [(time.time(), 0.2), (time.time() + 1, 0.21)]
    ex._h47r_ledger = X.LEDGER
    monkeypatch.setattr(R, "_ledger_actual", lambda: (_ for _ in ()).throw(AssertionError("import de LEDGER en el hot path")))
    hilos = []
    real_open = gzip.open
    monkeypatch.setattr(R.gzip, "open", lambda *a, **k: hilos.append(__import__("threading").current_thread().name) or real_open(*a, **k))
    R.tick(ex, c)
    assert R.vaciar()
    assert hilos and set(hilos) == {"h47_mids_writer"}                         # toda la E/S en el hilo escritor
    assert c._h47r_idx == 2


def test_h7_el_lock_del_libro_se_toma_una_vez_y_solo_para_copiar(monkeypatch):
    ex = T.nuevo("lock", real=False)
    c = T.ctx_de(ex, "eth")
    c.tok, c.hashes = "tU", ["seco-1"]
    c.lib.mids["tU"] = [(time.time(), 0.2)]
    ev = []
    class Spy:
        def __enter__(self):
            ev.append("in")
        def __exit__(self, *a):
            ev.append("out")
    c.lib.lk = Spy()
    real_put = R._Q.put_nowait
    monkeypatch.setattr(R._Q, "put_nowait", lambda it: ev.append("put") or real_put(it))
    R.volcar_mids(ex, c, X.LEDGER, forzar=True)
    assert ev == ["in", "out", "put"]                                         # el put (y cualquier E/S) fuera del lock
    R.vaciar()


# ---- 2 (2a review): sin nice por hilo; 8: Event de parada, join corto, sin print en daemons
def test_sin_setpriority_ni_print_en_el_modulo():
    src = Path(R.__file__).read_text().split('"""', 2)[2]
    assert "setpriority" not in src and "print(" not in src


def test_h8_hilo_huerfanas_espera_el_arranque_con_event_y_se_para_con_stop(monkeypatch):
    import threading
    monkeypatch.setattr(R, "ARRANQUE_DIFERIDO_S", 30.0)
    monkeypatch.setattr(R, "pasada_huerfanas", lambda *a, **k: (_ for _ in ()).throw(AssertionError("no debe trabajar")))
    monkeypatch.setattr(R, "_cargar_rpf", lambda: object())
    th = threading.Thread(target=R._hilo_huerfanas, args=(_Ex(), Path("x")), daemon=True)
    th.start()
    time.sleep(0.1)
    assert th.is_alive()
    R._STOP.set()
    th.join(2)
    assert not th.is_alive()


def test_h8_detener_para_y_une_los_hilos_en_poco_tiempo(monkeypatch):
    import threading
    R._escritor_asegurar()
    ev = threading.Event()
    h = threading.Thread(target=lambda: R._STOP.wait(30), daemon=True)
    h.start()
    R._HILOS.append(h)
    t0 = time.time()
    R.detener(espera=1.0)
    assert time.time() - t0 < 1.5 and not h.is_alive() and not R._W["t"].is_alive()
    R._escritor_asegurar()                                                    # se puede relanzar (tests / reinicio)
    assert R._W["t"].is_alive()


def test_h8_salida_llama_detener(monkeypatch):
    ex = _Ex()
    llam = []
    monkeypatch.setattr(R, "detener", lambda *a, **k: llam.append(1))
    R._salida(ex)
    assert llam == [1]


# ---- 1 (2a review): fichero gz propio por pid
def test_r1_un_fichero_por_pid_y_leer_mids_los_lee_todos_el_truncado_solo_pierde_su_cola(tmp_path):
    ini = int(time.time()) - 1000
    ahora = ini + 200
    d = time.strftime("%Y-%m-%d", time.gmtime(ahora))
    assert R._ruta_mids("l.jsonl", ahora).name == f"h47_mids_l_{d}_{os.getpid()}.jsonl.gz"
    def vol(pid, slug, desde, pts, hasta, trunc=False):
        p = tmp_path / f"h47_mids_l_{d}_{pid}.jsonl.gz"
        with gzip.open(p, "ab") as g:
            g.write((json.dumps({"slug": slug, "lado": "YES", "tok": "t", "fin": ini + 300.0, "desde_idx": desde, "hasta": hasta, "gap": False, "m": pts}) + "\n").encode())
        if trunc:
            with open(p, "ab") as f:
                f.write(gzip.compress(b"x" * 300)[:-9])
    sa, sb = f"eth-updown-5m-{ini}", f"sol-updown-5m-{ini}"
    vol(111, sa, 0, [[ini + 10, 0.2]], ini + 20, trunc=True)                  # proceso 1: cola truncada
    vol(222, sb, 0, [[ini + 10, 0.3]], ini + 20)                              # proceso 2: intacto
    m = R.leer_mids("l.jsonl", ahora=ahora)
    assert m[sa]["m"] == [(ini + 10, 0.2)] and m[sb]["m"] == [(ini + 10, 0.3)]


# ---- 9 (2a review): cobertura solo con WS vivo; cola acotada; hash de codigo en config
def test_r9_ws_muerto_no_reclama_cobertura(tmp_path):
    ex = T.nuevo("wsmuerto", real=False)
    c = T.ctx_de(ex, "eth")
    c.tok, c.hashes = "tU", ["seco-1"]
    t0 = time.time()
    c.lib.mids["tU"] = [(t0, 0.2)]
    c.lib.ult_msg = t0
    R.volcar_mids(ex, c, X.LEDGER, ahora=t0 + 1, forzar=True)                  # sano: hasta = t0+1
    c.lib.error = "ConnectionClosed"                                           # WS caido
    c.lib.mids["tU"].append((t0 + 3, 0.21))
    R.volcar_mids(ex, c, X.LEDGER, ahora=t0 + 60, forzar=True)
    c.lib.error = None
    c.lib.ult_msg = t0 + 70
    c.lib.mids["tU"].append((t0 + 80, 0.22))
    R.volcar_mids(ex, c, X.LEDGER, ahora=t0 + 80, forzar=True)                 # recupera, pero hubo un hueco de cobertura
    assert R.vaciar()
    e = R.leer_mids(X.LEDGER, ahora=t0 + 80)[c.mk["slug"]]
    assert e["hasta"] == t0 + 1 and e["hueco"] is True and len(e["m"]) == 3
    # sin mensajes (ult_msg viejo) tampoco; sin atributos -> fail-closed
    c2 = T.ctx_de(ex, "sol")
    c2.tok, c2.hashes = "tU", ["x"]
    c2.lib.mids["tU"] = [(t0, 0.2)]
    c2.lib.ult_msg = t0 - 100
    R.volcar_mids(ex, c2, X.LEDGER, ahora=t0, forzar=True)
    assert R._ws_vivo(object(), t0) is False and R._ws_vivo(c2.lib, t0) is False and c2._h47r_gap is True


def test_r9_cola_llena_no_pierde_puntos_ni_adelanta_el_indice(monkeypatch):
    ex = T.nuevo("colallena", real=False)
    c = T.ctx_de(ex, "eth")
    c.tok, c.hashes = "tU", ["seco-1"]
    t0 = time.time()
    c.lib.mids["tU"] = [(t0, 0.2), (t0 + 1, 0.21)]
    c.lib.ult_msg = t0
    monkeypatch.setattr(R._Q, "put_nowait", lambda it: (_ for _ in ()).throw(R.queue.Full()))
    assert R.volcar_mids(ex, c, X.LEDGER, ahora=t0, forzar=True) == 0 and getattr(c, "_h47r_idx", 0) == 0   # nada perdido: se reenvia luego
    monkeypatch.undo()
    assert R._Q.maxsize == R.COLA_MAX
    assert R.volcar_mids(ex, c, X.LEDGER, ahora=t0, forzar=True) == 2


def test_r9_config_lleva_hash_de_robustez_y_vendor(monkeypatch):
    sha = R.sha_codigo()
    assert set(sha) == {"h47_robustez", "vendor_rpf"} and all(len(v) == 16 for v in sha.values())
    assert '"robustez_sha": (R.sha_codigo() if R is not None else None)' in Path(H.__file__).read_text()   # R ausente -> None explicito
    monkeypatch.setattr(R, "RPF_VENDOR", Path("/no/existe"))
    assert R.sha_codigo() == {"error": "FileNotFoundError"}


# ---- 9: hechos tras exito de _log47; mercado_fin
def test_h9_si_log47_falla_no_queda_hecho_y_se_reintenta():
    ex = T.nuevo("hechos", real=False)
    c = _ctx_asentando(ex)
    ex._log47({"tipo": "config_previa"})
    orig, n = ex._log47, [0]
    def flaky(ev):
        if ev.get("tipo") == "puja_fin" and n[0] == 0:
            n[0] += 1
            raise OSError("disco")
        return orig(ev)
    ex._log47 = flaky
    R.finalizar_al_salir(ex)
    assert c.mk["slug"] not in getattr(ex, "_h47r_hechos", set()) and T.eventos("puja_fin") == []
    R.finalizar_al_salir(ex)                                                  # 2o intento: ahora si
    assert len(T.eventos("puja_fin")) == 1 and c.mk["slug"] in ex._h47r_hechos
    R.finalizar_al_salir(ex)
    assert len(T.eventos("puja_fin")) == 1 and len(T.eventos("mercado_fin")) == 1


def test_h9_no_duplica_mercado_fin_si_ya_estaba():
    ex = T.nuevo("mf", real=False)
    c = _ctx_asentando(ex)
    ex._log47({"tipo": "mercado_fin", "slug": c.mk["slug"]})
    R.finalizar_al_salir(ex)
    assert len(T.eventos("mercado_fin")) == 1 and len(T.eventos("puja_fin")) == 1


def test_aviso_robustez_no_altera_la_contabilidad():
    import pares_contabilidad as C
    ex = T.nuevo("contab", real=True)
    ex._log47({"tipo": "aviso_robustez", "msg": "x"})
    ex._log47({"tipo": "mercado_fin", "slug": "s", "interrumpida": True})
    assert C.plegar(X.leer_ledger()) == {}


# ================================================================ 3a /code-review
# ---- 1 y 2: una sola definicion de "sin verificar"; solo cuentan los que esperan
def test_t1_sin_verificar_cubre_intencion_huerfana_ilegible_y_anomalia():
    ini = int(time.time()) - 5000
    slug, led = _ledger_real_con_orden(Path(tempfile_dir()), ini, verificada=True)
    filas = [json.loads(l) for l in led.read_text().splitlines()]
    assert R.slugs_sin_verificar(filas) == set()
    solo_int = [d for d in filas if d["tipo"] == "intencion_post"]
    assert R.slugs_sin_verificar(solo_int) == {slug}                         # intencion sin puja_post ni lectura
    ilegible = [dict(d, size=None) if d["tipo"] == "intencion_post" else d for d in filas]
    assert R.slugs_sin_verificar(ilegible) == {slug}
    anomala = filas + [dict(tipo="lectura", oid="0xbb", f=99.0, real=True)]
    assert R.slugs_sin_verificar(anomala) == {slug}
    sin_slug = [dict(d, slug=None) if d["tipo"] == "intencion_post" else d for d in filas]    # intencion ilegible (sin slug): fail-closed
    assert R.slugs_sin_verificar(sin_slug) == {slug}                         # ...y se atribuye al mercado por su oid (fila puja_post)
    assert R.slugs_sin_verificar([d for d in sin_slug if d["tipo"] == "intencion_post"]) == set()   # sin ninguna fila con slug: no atribuible


def tempfile_dir():
    import tempfile
    return tempfile.mkdtemp(prefix="h47r_t_")


def test_t1_mercado_con_solo_intenciones_es_candidato_en_el_hilo(tmp_path):
    ini = int(time.time()) - 5000
    slug, led = _ledger_real_con_orden(tmp_path, ini, verificada=False)
    filas = [json.loads(l) for l in led.read_text().splitlines() if '"puja_post"' not in l and '"lectura"' not in l]
    led.write_text("".join(json.dumps(d) + "\n" for d in filas))
    n, ya, regs, esperan, _ = R.pasada_huerfanas(_Ex(real=True), led, R._cargar_rpf(), ahora=time.time(), posic={})
    assert (n, regs, esperan) == (0, [], [slug])


def test_t2_esperan_solo_cuenta_los_que_faltan_por_reconstruir(tmp_path):
    ini = int(time.time()) - 5000
    slug, led = _ledger_real_con_orden(tmp_path, ini, verificada=False)       # sin verificar -> espera
    with open(led, "a") as f:
        f.write(json.dumps(dict(tipo="puja_fin", slug=slug, real=True)) + "\n")   # ...pero ya tiene puja_fin COMPLETO
    assert R.pasada_huerfanas(_Ex(real=True), led, R._cargar_rpf(), ahora=time.time(), posic={})[3] == []
    with open(led, "a") as f:
        f.write(json.dumps(dict(tipo="puja_fin", slug=slug + "x", interrumpida=True, real=True)) + "\n")
    assert R.preparar([json.loads(l) for l in led.read_text().splitlines()], time.time()).esperan == []


# ---- 3: orden de instalar
def test_t3_instalar_registra_atexit_y_hilo_primero_y_cada_accesorio_en_su_try(monkeypatch):
    import atexit
    ex = T.nuevo("orden_inst", real=True)
    ev = []
    monkeypatch.setattr(atexit, "register", lambda f, *a: ev.append("atexit"))
    monkeypatch.setattr(R, "_hilo_huerfanas", lambda *a: ev.append("hilo"))
    monkeypatch.setattr(R, "purgar_viejos", lambda: (ev.append("purga"), (_ for _ in ()).throw(OSError("x")))[0])
    monkeypatch.setattr(R, "_escritor_asegurar", lambda: ev.append("escritor"))
    R.instalar(ex)
    for _ in range(100):
        if "hilo" in ev:
            break
        time.sleep(0.01)
    assert ev[0] == "atexit" and ev.index("hilo") < ev.index("purga") < ev.index("escritor")   # la purga fallida no impide el escritor


def test_t3_si_falla_el_ledger_o_el_atexit_el_resto_sigue(monkeypatch):
    import atexit
    ev = []
    ex = T.nuevo("orden_inst2", real=True)
    monkeypatch.setattr(R, "_ledger_actual", lambda: (_ for _ in ()).throw(RuntimeError("sin ledger")))
    monkeypatch.setattr(atexit, "register", lambda f, *a: ev.append("atexit"))
    monkeypatch.setattr(R, "purgar_viejos", lambda: ev.append("purga"))
    monkeypatch.setattr(R, "_escritor_asegurar", lambda: ev.append("escritor"))
    R.instalar(ex)
    assert ev == ["atexit", "purga", "escritor"]


# ---- 4: reintentar tambien los no maduros
def test_t4_el_hilo_reintenta_los_no_maduros_hasta_que_maduran(tmp_path, monkeypatch):
    import types
    ahora = 1_900_000_000.0
    ini = int(ahora) - 300 + 10                                                # fin dentro de 10 s; tras el arranque (+60 s) aun no maduro (fin+95)
    slug, led = _ledger_real_con_orden(tmp_path, ini, verificada=True)
    reloj = [ahora]
    class Stop:
        def wait(self, t):
            reloj[0] += 60.0
            return False
        def is_set(self): return False
        def clear(self): pass
        def set(self): pass
    monkeypatch.setattr(R, "time", types.SimpleNamespace(time=lambda: reloj[0], sleep=lambda x: None))
    monkeypatch.setattr(R, "_STOP", Stop())
    monkeypatch.setattr(R, "ARRANQUE_DIFERIDO_S", 0.0)
    monkeypatch.setattr(R, "AMBITO_REINTENTO_S", 10 ** 12)
    llamadas = []
    orig = R.pasada_huerfanas
    monkeypatch.setattr(R, "pasada_huerfanas", lambda *a, **k: (llamadas.append(k.get("solo")), orig(*a, **dict(k, posic={}), ahora=reloj[0]))[1])
    R._hilo_huerfanas(_Ex(real=True), led)
    assert llamadas[0] is None and llamadas[1] == [slug] and len(llamadas) == 2
    assert [json.loads(l)["slug"] for l in open(R.RECON_OUT)] == [slug]       # maduro en el 2o intento y reconstruido


# ---- 5: ledger incremental, reintentos no O(ledger)
def test_t5_ledger_cache_incremental_solo_lineas_completas_y_reset_si_se_trunca(tmp_path):
    p = tmp_path / "l.jsonl"
    p.write_text(json.dumps({"tipo": "a", "slug": "s1"}) + "\n" + json.dumps({"tipo": "b", "oid": "o", "slug": "s2"}) + "\n" + '{"tipo": "c", "sl')
    c = R.LedgerCache(p)
    assert len(c.refrescar()) == 2 and c.off == p.read_text().rfind("\n") + 1                # la linea a medias NO se consume
    with open(p, "a") as f:
        f.write('ug": "s1"}\n' + json.dumps({"tipo": "d", "oid": "o"}) + "\n" + "basura\n")
    assert [d["tipo"] for d in c.refrescar()] == ["a", "b", "c", "d"]                         # completa la 3a, indexa 'd' por oid, ignora basura
    assert [d["tipo"] for d in c.de_slugs(["s2"])] == ["b", "d"] and [d["tipo"] for d in c.de_slugs(["s1"])] == ["a", "c"]
    n = len(c.filas)
    assert len(c.refrescar()) == n                                                            # sin cambios: nada se relee/duplica
    p.write_text(json.dumps({"tipo": "z", "slug": "s9"}) + "\n")
    assert [d["tipo"] for d in c.refrescar()] == ["z"]                                        # ledger rotado/truncado: de cero


def test_t5_el_reintento_solo_pliega_las_filas_de_los_slugs_esperando(tmp_path, monkeypatch):
    ini = int(time.time()) - 5000
    slug, led = _ledger_real_con_orden(tmp_path, ini, verificada=False)
    for k in range(50):                                                       # ruido: otros mercados
        s2, extra = _ledger_real_con_orden(tmp_path / f"x{k}" if (tmp_path / f"x{k}").mkdir() is None else tmp_path, ini - 1000 - 300 * k, verificada=True)
        with open(led, "a") as f:
            f.write(Path(extra).read_text())
    cache, tam, vistos = R.LedgerCache(led), [], []
    orig = R.slugs_sin_verificar
    monkeypatch.setattr(R, "slugs_sin_verificar", lambda filas: (tam.append(len(filas)), orig(filas))[1])
    ex = _Ex(real=True)
    R.pasada_huerfanas(ex, led, R._cargar_rpf(), ahora=time.time(), posic={}, cache=cache)
    R.pasada_huerfanas(ex, led, R._cargar_rpf(), ahora=time.time(), posic={}, solo=[slug], cache=cache)
    assert tam[1] < tam[0] / 10 and tam[1] == len(cache.por_slug[slug])


# ---- 6: una sola fuente y paridad de campos con Exp47.finalizar
def test_t6_el_cron_no_redefine_constantes_ni_seleccion():
    src = (AQUI.parent / "etiquetado_pasivo" / "scripts" / "reconstructor_diario_puja_fin.py").read_text()
    assert "FIN_ESPERA_S" not in src and "HOLGURA_S" not in src and "def sin_verificar" not in src and "def preparar" not in src
    assert "H.preparar(" in src


def test_t6_resumen_parcial_no_pierde_campos_de_exp47_finalizar():
    ex = T.nuevo("paridad1", real=False)
    c = _ctx_asentando(ex)
    c.fase = "espera_fin"
    ex.finalizar(c)
    fin_ref, mf_ref = T.eventos("puja_fin")[0], T.eventos("mercado_fin")[0]
    ex2 = T.nuevo("paridad2", real=False)
    c2 = _ctx_asentando(ex2)
    parcial, mf = R.resumen_parcial(ex2, c2), R.mercado_fin_parcial(ex2, c2)
    falta = (set(fin_ref) - {"ts", "real", "escalon"}) - set(parcial)
    falta_mf = (set(mf_ref) - {"ts", "real", "escalon"}) - set(mf)
    assert not falta and not falta_mf, (falta, falta_mf)


# ================================================================ 4a /code-review
# ---- 3: limite de edad 24 h, 'esperan' sin inmaduros, aviso de vencidos una vez
def test_c3_preparar_separa_esperan_inmaduros_y_vencidos(tmp_path):
    ahora = time.time()
    for k in "abc":
        (tmp_path / k).mkdir()
    s_ok, l_ok = _ledger_real_con_orden(tmp_path / "a", int(ahora) - 5000, verificada=False, oid="0xa")           # sin verificar, reciente -> esperan
    s_inm, l_inm = _ledger_real_con_orden(tmp_path / "b", int(ahora) - 300 + 10, verificada=True, oid="0xb")      # aun no maduro
    s_old, l_old = _ledger_real_con_orden(tmp_path / "c", int(ahora) - 3 * 86400, verificada=False, oid="0xc")   # >24 h sin verificar -> vencido
    filas = [json.loads(l) for p in (l_ok, l_inm, l_old) for l in p.read_text().splitlines()]
    p = R.preparar(filas, ahora)
    assert p.esperan == [s_ok] and p.inmaduros == [s_inm] and p.vencidos == [s_old] and p.permitidos == set()


def test_c3_el_hilo_avisa_una_sola_vez_de_los_vencidos(monkeypatch):
    monkeypatch.setattr(R, "ARRANQUE_DIFERIDO_S", 0.0)
    monkeypatch.setattr(R, "REINTENTO_S", 0.01)
    monkeypatch.setattr(R, "_cargar_rpf", lambda: object())
    ini = int(time.time()) - 3600
    s1 = f"eth-updown-5m-{ini}"
    monkeypatch.setattr(R, "pasada_huerfanas", lambda *a, **k: (0, 0, [], [s1], ["eth-updown-5m-1"]))
    R._hilo_huerfanas(_Ex(), Path("x"))
    assert sum("sin verificar desde hace >24 h" in a for a in R.AVISOS) == 1


# ---- 4: una sola fuente de constantes
def test_c4_constantes_coinciden_entre_vendor_ejecutor_y_robustez():
    v = R._cargar_rpf()
    assert v.MARGEN_S == R.FIN_ESPERA_S == H.FIN_ESPERA_S and R.MARK_S == H.MARK_S


# ---- 5: carrera hilo vs cron
def test_c5_escribir_preferente_sustituye_missing_por_completa_y_audita(tmp_path):
    out = str(tmp_path / "o.jsonl")
    miss = dict(tipo="puja_fin", slug="a", markouts="missing", rellenos=[])
    comp = dict(tipo="puja_fin", slug="a", markouts="parcial_mids_persistidos", rellenos=[])
    assert R.escribir_preferente([miss, dict(miss, slug="b")], out) == (2, 0)
    assert R.escribir_preferente([dict(miss)], out) == (0, 1)                     # missing sobre missing: ya estaba
    assert R.escribir_preferente([comp], out) == (1, 0)                           # completa sobre missing: sustituye
    filas = {d["slug"]: d for d in map(json.loads, open(out))}
    assert filas["a"]["markouts"] == "parcial_mids_persistidos" and filas["a"]["reemplaza_missing"] is True and len(filas) == 2
    aud = [json.loads(l) for l in open(str(tmp_path / "o.reemplazos.jsonl"))]
    assert len(aud) == 1 and aud[0]["markouts"] == "missing"                      # la fila anterior queda auditable
    assert R.escribir_preferente([dict(miss, markouts="parcial_mids_persistidos", x=2)], out) == (0, 1)   # completa sobre completa: primero gana
    assert R.escribir_preferente([miss], out) == (0, 1) and not os.path.exists(out + ".tmp")


def test_c5_un_solo_reconstructor_a_la_vez_el_hilo_se_salta_la_pasada_si_el_cron_trabaja(tmp_path):
    ini = int(time.time()) - 5000
    slug, led = _ledger_real_con_orden(tmp_path, ini, verificada=True)
    with R.bloqueo_proceso() as a:
        assert a.ok
        with R.bloqueo_proceso() as b:
            assert not b.ok                                                       # segundo: no bloquea, se salta
            n, ya, regs, pend, _ = R.pasada_huerfanas(_Ex(real=True), led, R._cargar_rpf(), ahora=time.time(), posic={})
            assert (n, regs) == (0, []) and slug in pend and not os.path.exists(R.RECON_OUT)
    n, ya, regs, pend, _ = R.pasada_huerfanas(_Ex(real=True), led, R._cargar_rpf(), ahora=time.time(), posic={})
    assert n == 1                                                                 # liberado: ahora si


# ---- 6: cs_ok por cualquier camino que complete
def test_c6_cs_ok_se_marca_si_completo_por_el_camino_normal_de_run():
    ex = _Ex()
    R._envolver_cerrar_salida(ex)
    ex.cerrar_salida()                                                            # lo llama run() (camino normal)
    assert ex._h47r_cs_ok is True


def test_c6_cs_ok_no_se_marca_si_la_primera_llamada_fallo_y_luego_es_noop():
    ex = _Ex()
    def mal():
        if ex._cerrado:
            return                                                                # como el real: ya cerrado -> no-op
        ex._cerrado = True
        raise RuntimeError("red")
    ex.cerrar_salida = mal
    R._envolver_cerrar_salida(ex)
    with pytest.raises(RuntimeError):
        ex.cerrar_salida()
    ex2 = ex
    ex2.cerrar_salida()                                                           # 2a llamada (atexit): _cerrado ya puesto -> no-op, NO prueba nada
    assert getattr(ex, "_h47r_cs_ok", False) is False
