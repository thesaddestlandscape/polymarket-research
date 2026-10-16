"""ArmeroProceso: firma en un proceso hijo, reposición tras tomar, caducidad y fail-closed (cliente falso, sin red).
Uso: .venv/bin/python -m pytest -q tests/test_ejecutor_rapido_armero.py"""
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import ejecutor_rapido as er  # noqa: E402


class _Falso:
    n = 0

    def create_order(self, args, opts):
        _Falso.n += 1
        if args.price == 0.66:
            raise ValueError("precio prohibido")
        return {"tok": args.token_id, "p": args.price, "tam": args.size, "salt": _Falso.n}


def cliente_falso():
    return _Falso()


def _esperar(f, s=10):
    t = time.time() + s
    while time.time() < t:
        if f():
            return True
        time.sleep(0.02)
    return False


def test_firma_repone_y_falla_cerrado():
    a = er.ArmeroProceso("test_ejecutor_rapido_armero:cliente_falso", "0.01", False, caducidad_s=3.0, reserva=2,
                         margen_s=1.0, nice=0, renovar_s=0.5)
    try:
        k1, k2, kx = ("T", 0.30, 6.67, "BUY"), ("T", 0.31, 6.46, "BUY"), ("T", 0.66, 5.0, "BUY")
        a.armar([k1, k2, kx])
        assert _esperar(lambda: a.listas(k1) == 2 and a.listas(k2) == 2)
        s1 = a.tomar(k1)
        assert s1["p"] == 0.30 and s1["tam"] == 6.67
        s2 = a.tomar(k1)
        assert s2["salt"] != s1["salt"]                         # cada firma se usa una vez
        assert _esperar(lambda: a.listas(k1) == 2)               # el hijo repone lo tomado
        assert a.tomar(kx) is None                               # la firma falla -> no hay orden (fail-closed)
        errs = []
        assert _esperar(lambda: errs.extend(a.sacar_errores()) or any(e[1] == kx for e in errs))
        assert a.tomar(("T", 0.50, 5.0, "BUY")) is None          # clave no armada
        a.armar([k2])                                            # retirar claves libera su reserva
        assert a.listas(k1) == 0 and a.tomar(k1) is None
        def salts():
            with a.lock:
                return [x[1]["salt"] for x in a.pool.get(k2, [])]
        viejas = salts()
        assert _esperar(lambda: bool(salts()) and all(x not in viejas for x in salts()), 8)   # renueva antes de caducar
    finally:
        a.parar()
        a.proc.join(5)
    assert not a.proc.is_alive()


def test_firmador_muerto_vacia_pool():
    a = er.ArmeroProceso("test_ejecutor_rapido_armero:cliente_falso", "0.01", False, caducidad_s=30.0, reserva=1,
                         nice=0)
    k = ("T", 0.40, 5.0, "BUY")
    a.armar([k])
    assert _esperar(lambda: a.listas(k) == 1)
    a.proc.kill()
    a.proc.join(5)
    assert _esperar(lambda: a.listas(k) == 0)                    # sin firmador: no se opera con restos
    assert a.tomar(k) is None and not a.vivo()


def cliente_que_muere():
    sys.exit("credenciales dudosas")


def test_error_avisado_una_vez_con_espera():
    a = er.ArmeroProceso("test_ejecutor_rapido_armero:cliente_falso", "0.01", False, nice=0)
    try:
        kx = ("T", 0.66, 5.0, "BUY")
        a.armar([kx])
        time.sleep(2.0)                                          # sin espera exponencial serían ~10-40 avisos
        assert sum(1 for e in a.sacar_errores() if e[1] == kx) == 1
    finally:
        a.parar()


def test_firmador_que_muere_al_arrancar_falla_rapido():
    t = time.time()
    try:
        er.ArmeroProceso("test_ejecutor_rapido_armero:cliente_que_muere", "0.01", False, nice=0, espera_listo_s=60)
        assert False, "debía lanzar"
    except RuntimeError:
        pass
    assert time.time() - t < 15                                  # EOF inmediato, no los 60 s de espera


def test_armar_con_firmador_caido_no_lanza():
    a = er.ArmeroProceso("test_ejecutor_rapido_armero:cliente_falso", "0.01", False, nice=0)
    a.proc.kill()
    a.proc.join(5)
    time.sleep(0.3)
    a.armar([("T", 0.30, 6.67, "BUY")])                          # no lanza
    assert not a.vivo() and a.tomar(("T", 0.30, 6.67, "BUY")) is None


def test_renovacion_nunca_deja_la_clave_sin_firma():
    a = er.ArmeroProceso("test_ejecutor_rapido_armero:cliente_falso", "0.01", False, caducidad_s=3.0, reserva=1,
                         margen_s=0.5, nice=0, renovar_s=1.0)
    try:
        k = ("T", 0.30, 6.67, "BUY")
        a.armar([k])
        assert _esperar(lambda: a.listas(k) >= 1)
        t = time.time()
        while time.time() - t < 7:                               # > 2 vidas: siempre hay una firma válida
            assert a.listas(k) >= 1
            time.sleep(0.05)
    finally:
        a.parar()


def test_firmas_de_epoca_anterior_se_descartan():
    a = er.ArmeroProceso("test_ejecutor_rapido_armero:cliente_falso", "0.01", False, reserva=2, nice=0)
    try:
        ks = [("T", round(x / 100, 2), 5.0, "BUY") for x in range(1, 60) if x != 66]
        for _ in range(5):                                       # cambios rápidos: muchas firmas en vuelo
            a.armar(ks)
            a.armar(ks[:1])
        a.armar(ks)
        assert _esperar(lambda: all(a.listas(k) >= 2 for k in ks), 15)   # tras los cambios, TODAS repuestas
        time.sleep(0.5)
        with a.lock:
            assert all(len(v) <= 4 for v in a.pool.values())     # tope 2×reserva
            assert set(a.pool) <= set(ks)
    finally:
        a.parar()


def test_parar_no_registra_muerte_falsa():
    a = er.ArmeroProceso("test_ejecutor_rapido_armero:cliente_falso", "0.01", False, nice=0)
    a.parar()
    time.sleep(0.3)
    assert not any("muerto" in str(e[2]) for e in a.sacar_errores()) and not a.vivo()


def test_cambio_de_claves_no_deja_huecos():
    """Reducir la rejilla al lado s (armar con un subconjunto) no deja sin firma las claves que siguen."""
    a = er.ArmeroProceso("test_ejecutor_rapido_armero:cliente_falso", "0.01", False, reserva=2, nice=0)
    try:
        up = [("UP", round(x / 100, 2), 5.0, "BUY") for x in range(1, 40)]
        dn = [("DN", round(x / 100, 2), 5.0, "BUY") for x in range(1, 40)]
        a.armar(up + dn)
        a.armar(dn)                                              # en vuelo aún hay firmas de dn y de up
        assert _esperar(lambda: all(a.listas(k) >= 2 for k in dn), 15)
        with a.lock:
            assert not any(k[0] == "UP" for k in a.pool)
    finally:
        a.parar()
