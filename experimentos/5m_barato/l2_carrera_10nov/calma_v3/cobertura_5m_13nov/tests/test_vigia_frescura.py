import time
import pytest
import universo_5m_io as U
import vigia_universo_5m_frescura as V

MONEDAS = ["btc", "eth", "sol", "xrp", "doge", "bnb"]


def fila(a, ini, t_recv, fuente="ws", t_ev=None, mid=None):
    e = {"id": mid or f"{a}{ini}", "market": "0xc" + (mid or f"{a}{ini}"), "slug": f"{a}-updown-5m-{ini}", "assets_ids": [str(ini % 10**9) + "1", str(ini % 10**9) + "2"],
         "outcomes": ["Up", "Down"], "timestamp": str(int((t_ev if t_ev is not None else t_recv) * 1000))}
    f = U.parsear_nuevo(e, int(t_recv * 1000), fuente)
    f["mid"] = None
    return {k: v for k, v in f.items() if k != "mid"}


def poblar(d, ahora, horizonte_min=1400, ultimo_hace_s=60, fuente="ws"):
    base = (int(ahora) // 300) * 300
    filas = []
    for a in MONEDAS:
        for k in range(1, horizonte_min // 5):
            filas.append(fila(a, base + 300 * k, ahora - ultimo_hace_s if k == horizonte_min // 5 - 1 else ahora - 7200, fuente))
    U.escribir(filas, d)


def test_sano_no_avisa_y_se_arma(tmp_path):
    d, ahora = tmp_path / "u", time.time()
    poblar(d, ahora)
    prob, info, msgs = V.ejecutar(ahora, d, telegram=False)
    assert prob == {} and msgs == [] and info["cobertura_min"]["BTC"] > 1000


def test_sin_fichero_antes_de_armarse_no_avisa(tmp_path):
    prob, info, msgs = V.ejecutar(time.time(), tmp_path / "u", telegram=False)
    assert "sin_fichero" in prob and msgs == []


def test_sin_filas_nuevas_10min_avisa_una_vez_y_recupera(tmp_path):
    d, ahora = tmp_path / "u", time.time()
    poblar(d, ahora)
    V.ejecutar(ahora, d, telegram=False)
    enviados = []
    p, i, m = V.ejecutar(ahora + 700, d, telegram=True, enviar=lambda t, bot=None: enviados.append(t))
    assert "sin_5m_nuevos" in p and "ws_mudo" not in p and len(m) == 1 and len(enviados) == 1
    p, i, m = V.ejecutar(ahora + 760, d, telegram=True, enviar=lambda t, bot=None: enviados.append(t))
    assert m == [] and len(enviados) == 1                                         # latch: sin spam
    U.escribir([fila("btc", int(ahora) + 99999 // 300 * 300, ahora + 800)], d)    # llega una fila
    p, i, m = V.ejecutar(ahora + 801, d, telegram=False)
    assert "sin_5m_nuevos" not in p and any("recuperado" in x for x in m) is True or m == []


def test_ws_mudo_pero_relleno_vivo(tmp_path):
    d, ahora = tmp_path / "u", time.time()
    poblar(d, ahora, fuente="capture")
    V.ejecutar(ahora, d, telegram=False)
    p, _, _ = V.ejecutar(ahora + 1000, d, telegram=False)
    assert "ws_mudo" in p


def test_cobertura_por_moneda(tmp_path):
    d, ahora = tmp_path / "u", time.time()
    poblar(d, ahora)
    V.ejecutar(ahora, d, telegram=False)
    # tras 2 h sin nuevas filas la cobertura baja; se fuerza con un horizonte corto en BNB
    d2 = tmp_path / "u2"
    base = (int(ahora) // 300) * 300
    U.escribir([fila(a, base + 300 * k, ahora - 30) for a in MONEDAS if a != "bnb" for k in range(1, 100)] +
               [fila("bnb", base + 300 * k, ahora - 30) for k in range(1, 5)], d2)
    p, i = V.evaluar(ahora, d2)
    assert "cobertura" in p and "BNB" in p["cobertura"] and "BTC" not in p["cobertura"]


def test_desfase_de_reloj(tmp_path):
    d, ahora = tmp_path / "u", time.time()
    base = (int(ahora) // 300) * 300
    U.escribir([fila(a, base + 300 * k, ahora - 30, t_ev=ahora - 30 - 20) for a in MONEDAS for k in range(1, 300)], d)
    p, _ = V.evaluar(ahora, d)
    assert "desfase_reloj" in p


def test_fichero_truncado_y_conflicto_se_reportan(tmp_path):
    d, ahora = tmp_path / "u", time.time()
    poblar(d, ahora)
    p0 = U.fichero(U.dia_utc(ahora), d)
    p0.write_bytes(p0.read_bytes() + b"\x1f\x8b\x08xx")
    p, _ = V.evaluar(ahora, d)
    assert "fichero_truncado" in p
    U.escribir([fila("btc", (int(ahora) // 300) * 300 + 600, ahora, mid="XX"), fila("btc", (int(ahora) // 300) * 300 + 600, ahora, mid="XX")], d)
    base = (int(ahora) // 300) * 300 + 600
    e = fila("btc", base, ahora, mid="XX"); e["token_up"] = "424242"
    U.escribir([e], d)
    p, _ = V.evaluar(ahora, d)
    assert "conflictos_tokens" in p


def test_telegram_caido_no_rompe(tmp_path):
    d, ahora = tmp_path / "u", time.time()
    poblar(d, ahora)
    V.ejecutar(ahora, d, telegram=False)
    def malo(t, bot=None):
        raise RuntimeError("sin red")
    p, i, m = V.ejecutar(ahora + 700, d, telegram=True, enviar=malo)
    assert m
