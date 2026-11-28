import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import diagnostico_latencia_p1b_28nov as D


def _run(tmp, n=6, lag=0.0, corrupta=False):
    d = tmp / "run"; (d / "cancel_evid").mkdir(parents=True)
    led, ev = [], []
    for k in range(n):
        oid = f"0x{k}"; ts = 1_000_000_000_000_000 + k * 1_000_000_000   # ns
        coin = "BTC" if k % 2 else "ETH"
        led.append(dict(k="intencion", oid_local=oid, coin=coin, tok=f"t{k}"))
        led.append(dict(k="post", oid_local=oid, clase="ok", t_send_ns=ts, t_ack_ns=ts + 60_000_000))
        led.append(dict(k="cancel", oid=oid, ok=True, intento=1, t_send_ns=ts + 2e9, t_ack_ns=ts + 2e9 + 58_000_000))
        ack_ms = ts / 1e6 + 60
        ev.append(dict(k="user_order", mine=True, tipo="PLACEMENT", oid=oid, ts_ex_ms=ack_ms - 25 + lag, t_recv_ms=ack_ms - 25 + lag + 17))
        cack = ts / 1e6 + 2000 + 58
        ev.append(dict(k="user_order", mine=True, tipo="CANCELLATION", oid=oid, ts_ex_ms=cack - 24 + lag, t_recv_ms=cack - 24 + lag + 18))
    txt = "\n".join(json.dumps(r) for r in led) + ("\n{rota\n" if corrupta else "\n")
    (d / "ledger.jsonl").write_text(txt)
    (d / "cancel_evid" / "e.jsonl").write_text("\n".join(json.dumps(r) for r in ev) + "\n")
    return str(d)


def test_normal_ws_sello_antes_del_ack(tmp_path):
    r = D.analiza(_run(tmp_path))
    m = r["por_moneda"]["TODAS"]
    assert m["post_http_ms"]["p50"] == 60 and m["delete_http_ms"]["p50"] == 58
    assert m["place_ex_menos_ack_ms"]["p50"] == -25 and m["place_recv_menos_ex_ms"]["p50"] == 17
    assert m["place_ex_menos_ack_frac_pos"]["frac_gt0"] == 0.0
    assert set(r["por_moneda"]) == {"TODAS", "BTC", "ETH"} and r["filas_corruptas"] == 0


def test_lag_de_publicacion_se_ve_en_ex_menos_ack_y_no_en_http_ni_recepcion(tmp_path):
    r = D.analiza(_run(tmp_path, lag=500.0))
    m = r["por_moneda"]["TODAS"]
    assert m["post_http_ms"]["p50"] == 60                      # el HTTP no cambia
    assert m["place_ex_menos_ack_ms"]["p50"] == 475 and m["place_ex_menos_ack_frac_pos"]["frac_gt100"] == 1.0
    assert m["place_recv_menos_ex_ms"]["p50"] == 17            # la recepcion tampoco


def test_filas_corruptas_se_cuentan_no_se_ignoran(tmp_path):
    assert D.analiza(_run(tmp_path, corrupta=True))["filas_corruptas"] == 1


def test_spearman_q_file(tmp_path):
    d = _run(tmp_path)
    q = tmp_path / "q.txt"
    # tasa de eventos distinta por token, sin relacion con el ack constante -> rho definido o None, nunca excepcion
    q.write_text("\n".join(f"{1_000_000_000_000 + k * 1000 - 100},t{k}" for k in range(6)) + "\n")
    r = D.analiza(d, str(q))
    assert r["spearman_ack_vs_tasa_q_1s"]["n"] == 6


def test_spearman_pocas_muestras_devuelve_none():
    assert D.spearman([1, 2], [1, 2]) is None


def test_testigo_mercado_ex_antes_del_ack_y_usuario_con_lag(tmp_path):
    d = _run(tmp_path, lag=500.0)
    f = tmp_path / "d.txt"; filas = []
    for k in range(6):
        ts = 1_000_000_000 + k * 1000; tok = f"t{k}"
        filas += [f"{ts - 500},{tok},0.01,100.00,0", f"{ts + 35},{tok},0.01,105.00,0",             # alta: +5 a ts+35 (antes del ack ts+60)
                  f"{ts + 2000 + 33},{tok},0.01,100.00,0"]                                         # baja: -5 a send_cancel+33
    f.write_text("\n".join(filas) + "\n")
    r = D.analiza(d, d_file=str(f)); m = r["por_moneda"]["TODAS"]
    assert m["alta_mercado_ex_menos_envio_ms"]["p50"] == 35 and m["alta_mercado_ex_menos_ack_ms"]["p50"] == -25
    assert m["cancel_mercado_ex_menos_envio_ms"]["p50"] == 33
    assert m["alta_mercado_ex_menos_usuario_ex_ms"]["p50"] < 0          # el canal de usuario (con lag de 500) llega DESPUES que el libro


def test_salto_ignora_cambios_que_no_son_exactamente_5():
    a = [(0, 100.0, 0), (10, 107.37, 0), (20, 112.37, 0)]
    assert D.salto(a, 0, 100, 5.0) == (20, 112.37, 0) and D.salto(a, 0, 15, 5.0) is None
