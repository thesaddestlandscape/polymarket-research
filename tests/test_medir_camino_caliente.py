"""Pruebas del desenlace de --casa (medir_camino_caliente): una orden que CASÓ nunca puede quedar como muerta/rechazada.
Cliente falso: no toca red ni dinero. Uso: /root/polymarket-research/.venv/bin/python -m pytest -q tests/test_medir_camino_caliente.py
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import medir_camino_caliente as M  # noqa: E402

FOK_MUERTA = {"error": "PolyApiException: PolyApiException[status_code=400, error_message={'error': \"order couldn't be "
                       "fully filled. FOK orders are fully filled or killed.\"}]"}
ASK, T0, ACK, TK = 0.98, 1_000_000, 230.0, "tokA"


class Cliente:
    def __init__(self, orden=None, saldos=(20.0,), lanza=False):
        self.orden, self.saldos, self.lanza, self.n = orden, list(saldos), lanza, 0

    def get_order(self, h):
        if self.lanza:
            raise RuntimeError("red")
        return self.orden


def _desenlace(c, res, prints=(), saldo_antes=20.0, saldo_despues=20.0):
    M._saldo_dedicada = lambda _c: saldo_despues
    return M._desenlace(c, "0xh", res, list(prints), TK, ASK, T0, ACK, saldo_antes, espera_s=0)


def _print(dt, size, price=ASK, tk=TK):
    return (tk, T0 + dt, {"price": str(price), "size": str(size), "side": "BUY"})


def test_fok_muerta_explicita_sin_pruebas_es_muerta():
    est, *_ = _desenlace(Cliente(orden=None), FOK_MUERTA)
    assert est == "muerta"


def test_matched_en_respuesta_es_casada_aunque_saldo_no_se_mueva():
    est, *_ = _desenlace(Cliente(orden={"size_matched": "7"}), {"status": "matched", "takingAmount": "7",
                                                                 "orderID": "0xh"})
    assert est == "casada"


def test_muerta_pero_saldo_baja_sube_a_ambigua():
    est, *_ = _desenlace(Cliente(orden=None), FOK_MUERTA, saldo_antes=20.0, saldo_despues=13.1)
    assert est == "ambigua"


def test_muerta_pero_prints_unicos_de_7_sube_a_ambigua():
    est, _o, t_print, grupo, _s = _desenlace(Cliente(orden=None), FOK_MUERTA, prints=[_print(180, 3), _print(200, 4)])
    assert grupo["atribucion"] == "unica" and est == "ambigua"


def test_muerta_sin_saldo_legible_es_ambigua():
    est, *_ = _desenlace(Cliente(orden=None), FOK_MUERTA, saldo_antes=None)
    assert est == "ambigua"


def test_muerta_con_get_order_dict_sin_cancelar_es_ambigua():
    est, *_ = _desenlace(Cliente(orden={"status": "MATCHED", "size_matched": "0"}), FOK_MUERTA)
    assert est == "ambigua"


def test_delayed_y_get_order_none_es_ambigua_no_muerta():
    est, *_ = _desenlace(Cliente(orden=None), {"status": "delayed", "orderID": "0xh", "success": True})
    assert est == "ambigua"


def test_error_de_red_es_ambigua():
    est, *_ = _desenlace(Cliente(lanza=True), {"error": "ReadTimeout: timed out"})
    assert est == "ambigua"


def test_casada_con_tamano_distinto_de_7_es_ambigua():
    est, *_ = _desenlace(Cliente(orden={"size_matched": "14"}), {"status": "delayed", "orderID": "0xh"})
    assert est == "ambigua"


def test_casada_por_get_order_tras_delayed():
    est, _o, t_print, grupo, _s = _desenlace(Cliente(orden={"size_matched": "7", "status": "MATCHED"}),
                                             {"status": "delayed", "orderID": "0xh"}, prints=[_print(190, 7)])
    assert est == "casada" and t_print == T0 + 190


def test_prints_antes_del_minimo_fisico_no_se_atribuyen():
    _e, _o, t_print, grupo, _s = _desenlace(Cliente(orden={"size_matched": "7"}), {"status": "matched",
                                                                                    "takingAmount": "7"},
                                            prints=[_print(60, 7)])
    assert t_print is None


def test_dos_grupos_de_7_es_atribucion_ambigua():
    _e, _o, t_print, grupo, _s = _desenlace(Cliente(orden={"size_matched": "7"}), {"status": "matched",
                                                                                    "takingAmount": "7"},
                                            prints=[_print(150, 7), _print(400, 2), _print(410, 5)])
    assert t_print is None and grupo["atribucion"].startswith("ambigua")


def test_tope_cuenta_intenciones_sin_casa_y_lineas_por_fila(tmp_path, monkeypatch):
    led = tmp_path / "l.jsonl"
    ahora = M.er.ahora_ms()
    filas = [{"fase": "intencion_casa", "hash": "a", "t": ahora},
             {"fase": "casa", "hash": "a", "estado": "muerta", "t_envio_ms": ahora},
             {"fase": "intencion_casa", "hash": "b", "t": ahora},                 # murió tras el POST: cuenta
             {"fase": "intencion_casa", "hash": "c", "t": ahora},
             {"fase": "casa", "hash": "c", "estado": "casada", "t_envio_ms": ahora},
             {"fase": "intencion_casa", "hash": None, "t": ahora},                # hash None: cuenta igual
             {"fase": "intencion_casa", "hash": None, "t": ahora}]
    led.write_text("\n".join(json.dumps(f) for f in filas) + "\n{truncada")
    monkeypatch.setattr(M, "LEDGER", led)
    assert M._casadas_ledger_24h() == 4                                          # b, c(casada), None, None
