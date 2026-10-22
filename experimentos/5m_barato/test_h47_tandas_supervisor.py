"""Tests del vigilante de tandas H47 (h47_tandas_supervisor.py). Todo con fakes: ledger/locks/estado en tmp, screen, saldo, Telegram,
os.kill, subprocess y reloj falsos. No toca la wallet, el ledger real, las screens ni envia nada."""
import fcntl
import json
import signal
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
import h47_tandas_supervisor as S  # noqa: E402

T0 = 1_792_520_000.0


def iso(t):
    return datetime.fromtimestamp(t, timezone.utc).isoformat(timespec="milliseconds")


class Mundo:
    """Estado falso: reloj, screen, proceso B, saldo, telegram, llamadas a subprocess/os.kill."""

    def __init__(self, tmp):
        self.t = T0
        self.tmp = tmp
        self.viva = False
        self.pid = None
        self.saldo = 25.0
        self.tg = []
        self.kills = []
        self.lanzados = 0
        self.runs = []
        self.rot_resultado = None          # None = no responde (timeout) | (rc, stdout)
        self.rot_escribe = True            # si el CLI de rotacion llega a escribir el suelo_reiniciado
        self.muere_con_sigterm = True
        self.ev = []

    def escribe(self, tipo, dt=0.0, **kw):
        e = {"tipo": tipo, "real": True, "ts": iso(self.t + dt)}
        e.update(kw)
        self.ev.append(e)
        with open(S.LEDGER, "a") as f:
            f.write(json.dumps(e) + "\n")


@pytest.fixture
def W(tmp_path, monkeypatch):
    w = Mundo(tmp_path)
    monkeypatch.setattr(S, "LEDGER", tmp_path / "ledger.jsonl")
    monkeypatch.setattr(S, "KILL", tmp_path / "h47.KILL")
    monkeypatch.setattr(S, "KILL_PARES", tmp_path / "pares.KILL")
    monkeypatch.setattr(S, "LOCK_H47", tmp_path / "h47.lock")
    monkeypatch.setattr(S, "LOCK_SUP", tmp_path / "sup.lock")
    monkeypatch.setattr(S, "ESTADO", tmp_path / "estado.json")
    monkeypatch.setattr(S, "LOG", tmp_path / "sup.log")
    monkeypatch.setattr(S, "STOP", tmp_path / "STOP")
    monkeypatch.setattr(S, "PROC", tmp_path / "proc")
    monkeypatch.setattr(S, "ROTACION_AUTOMATICA", True)       # los tests de rotacion la ejercen; en produccion va a False (22-Oct)
    (tmp_path / "proc").mkdir()
    S.CONT.update(ilegible=0, exc=0)
    S.AVISOS_T.clear()
    S.LANZ_T.clear()
    monkeypatch.setattr(S, "ahora", lambda: w.t)
    monkeypatch.setattr(S, "dormir", lambda s: setattr(w, "t", w.t + s))
    monkeypatch.setattr(S, "_enviar", lambda txt: w.tg.append(txt) or True)
    monkeypatch.setattr(S, "saldo", lambda: w.saldo)
    monkeypatch.setattr(S, "screen_viva", lambda: w.viva)
    monkeypatch.setattr(S, "pid_b", lambda: w.pid)

    def fake_kill(pid, sig):
        w.kills.append((pid, sig))
        if w.muere_con_sigterm and sig == signal.SIGTERM:
            w.pid, w.viva = None, False
    monkeypatch.setattr(S.os, "kill", fake_kill)

    def fake_lanzar():
        w.lanzados += 1
        w.viva, w.pid = True, 4242
        S.LANZ_T.append(w.t)
    monkeypatch.setattr(S, "lanzar", fake_lanzar)

    def fake_run(cmd, **kw):
        w.runs.append(cmd)
        if "--rotar-tanda" in cmd:
            if w.rot_escribe:
                w.escribe("suelo_reiniciado", origen="rotar_tanda", saldo_base=w.saldo)
            if w.rot_resultado is None:
                raise subprocess.TimeoutExpired(cmd, 180)
            rc, out = w.rot_resultado
            return subprocess.CompletedProcess(cmd, rc, out, "")
        return subprocess.CompletedProcess(cmd, 0, "", "")
    monkeypatch.setattr(S.subprocess, "run", fake_run)
    return w


def arranque(w, suelo=20.0, dt=0.0, n_max=230):
    w.escribe("suelo_calculado", dt=dt, suelo=suelo, saldo=suelo + 5)
    w.escribe("config", dt=dt, n_max=n_max)


# ---------------------------------------------------------------- (7) suelo vigente y lectura hacia atras
def test_suelo_vigente_lee_nombres_reales_y_toma_el_maximo(W):
    W.escribe("suelo_calculado", suelo=15.2)
    W.escribe("suelo_fijado", suelo=15.2)
    W.escribe("suelo_subido", suelo=18.9)
    W.escribe("suelo_subido", suelo=29.27)
    assert S.suelo_vigente() == pytest.approx(29.27)


def test_suelo_vigente_tras_reinicio_sin_suelo_nuevo_es_base_menos_presupuesto(W):
    W.escribe("suelo_calculado", suelo=29.27)
    W.escribe("suelo_reiniciado", origen="rotar_tanda", saldo_base=29.5)
    assert S.suelo_vigente() == pytest.approx(24.5)


def test_suelo_vigente_ignora_suelos_anteriores_al_reinicio(W):
    W.escribe("suelo_calculado", suelo=29.27)
    W.escribe("suelo_reiniciado", saldo_base=24.9)
    W.escribe("suelo_calculado", suelo=19.9)
    assert S.suelo_vigente() == pytest.approx(19.9)


def test_suelo_vigente_lo_encuentra_a_mas_de_20000_eventos(W):
    W.escribe("suelo_fijado", suelo=17.5)
    with open(S.LEDGER, "a") as f:                                  # 30.000 eventos de relleno (> ventana vieja de 20000)
        for i in range(30000):
            f.write('{"tipo":"puja_post","real":true,"ts":"%s","pad":"%s"}\n' % (iso(T0), "x" * 40))
    assert S.suelo_vigente() == pytest.approx(17.5)


def test_suelo_vigente_sin_ledger_o_sin_suelo_es_none(W):
    assert S.suelo_vigente() is None
    W.escribe("puja_post")
    assert S.suelo_vigente() is None


def test_ledger_reverso_tolera_lineas_cortadas_y_bloques_pequenos(W):
    for i in range(50):
        W.escribe("puja_post", n=i)
    with open(S.LEDGER, "a") as f:
        f.write('{"tipo": "corta')                                  # crash a medio escribir
    ns = [e["n"] for e in S.ledger_reverso(bloque=64) if e.get("tipo") == "puja_post"]
    assert ns == list(range(49, -1, -1))


# ---------------------------------------------------------------- kill
def test_kill_pendiente_ledger_fichero_y_pares(W):
    assert not S.kill_pendiente()
    W.escribe("kill", motivo="x")
    assert S.kill_pendiente()
    W.escribe("kill_rearmado")
    assert not S.kill_pendiente()
    S.KILL_PARES.write_text("x")
    assert S.kill_pendiente()                                       # (6) tambien el KILL de pares
    S.KILL_PARES.unlink()
    S.KILL.write_text("x")
    assert S.kill_pendiente()


def test_ciclo_kill_avisa_una_vez_antirrebote(W):
    W.escribe("kill", motivo="x")
    for _ in range(5):
        assert S.ciclo() == "kill"
        W.t += 120
    assert len([m for m in W.tg if "KILL" in m]) == 1
    assert W.lanzados == 0 and not W.kills
    W.t += 4000
    S.ciclo()
    assert len([m for m in W.tg if "KILL" in m]) == 2


# ---------------------------------------------------------------- (6) avisos: saldo duro, ilegible, excepciones
def test_saldo_bajo_duro_avisa_y_no_toca(W):
    arranque(W)
    W.saldo = 11.0
    assert S.ciclo() == "saldo_duro"
    assert any("suelo duro" in m for m in W.tg) and W.lanzados == 0 and not W.runs


def test_ilegible_persistente_avisa_a_la_tercera(W):
    W.saldo = None
    arranque(W)
    for i in range(2):
        assert S.ciclo() == "ilegible"
    assert not W.tg
    S.ciclo()
    assert len(W.tg) == 1 and "ilegibles" in W.tg[0]
    S.ciclo()
    assert len(W.tg) == 1                                           # antirrebote
    W.saldo = 25.0
    S.ciclo()
    assert S.CONT["ilegible"] == 0


def test_suelo_ilegible_no_actua(W):
    assert S.ciclo() == "ilegible" and W.lanzados == 0


def test_excepciones_repetidas_avisan(W, monkeypatch):
    monkeypatch.setattr(S, "STOP", type("P", (), {"exists": lambda self: len(W.tg) > 0 or W.t > T0 + 10 * 120})())

    def boom():
        raise RuntimeError("rpc roto")
    monkeypatch.setattr(S, "ciclo", boom)
    fd = None
    monkeypatch.setattr(S, "tomar_lock", lambda path=None: object())
    S.main()
    assert any("excepciones seguidas" in m for m in W.tg)


def test_telegram_fail_open(W, monkeypatch):
    def mal(txt):
        raise OSError("sin red")
    monkeypatch.setattr(S, "_enviar", mal)
    assert S.avisar("hola", "k") is True                            # no propaga
    assert "telegram fallo OSError" in S.LOG.read_text()


# ---------------------------------------------------------------- (8) screen_viva ignora Dead
def test_screen_viva_ignora_dead(monkeypatch):
    def run(cmd, **kw):
        return subprocess.CompletedProcess(cmd, 0, "There are screens on:\n\t123.h47B\t(10/20/2026 06:00:00 PM)\t(Dead ???)\n", "")
    monkeypatch.setattr(S.subprocess, "run", run)
    assert S.screen_viva() is False

    def run2(cmd, **kw):
        return subprocess.CompletedProcess(cmd, 0, "\t123.h47B\t(10/20/2026)\t(Detached)\n\t9.h47sup\t(Detached)\n", "")
    monkeypatch.setattr(S.subprocess, "run", run2)
    assert S.screen_viva() is True

    def run3(cmd, **kw):
        return subprocess.CompletedProcess(cmd, 0, "\t9.h47sup\t(Detached)\n", "")
    monkeypatch.setattr(S.subprocess, "run", run3)
    assert S.screen_viva() is False


# ---------------------------------------------------------------- pid_b por argv exacto
def test_pid_b_argv_exacto(tmp_path, monkeypatch):
    monkeypatch.setattr(S, "PROC", tmp_path)

    def proc(pid, *argv):
        d = tmp_path / str(pid)
        d.mkdir()
        (d / "cmdline").write_bytes("\0".join(argv).encode() + b"\0")
    proc(10, "bash", "-c", "x experimento_maker_h47.py --escalon B --confirmo-dinero-real")
    proc(11, "/venv/bin/python", "experimento_maker_h47.py", "--escalon", "B", "--rotar-tanda", "--confirmo-dinero-real")
    proc(12, "/venv/bin/python", "experimento_maker_h47.py", "--escalon", "A", "--confirmo-dinero-real")
    assert S.pid_b() is None
    proc(13, "/venv/bin/python", "experimento_maker_h47.py", "--escalon", "B", "--n", "230", "--confirmo-dinero-real")
    assert S.pid_b() == 13


def test_lock_h47_libre(tmp_path, monkeypatch):
    monkeypatch.setattr(S, "LOCK_H47", tmp_path / "l.lock")
    assert S.lock_h47_libre()
    fd = open(tmp_path / "l.lock", "w")
    fcntl.flock(fd, fcntl.LOCK_EX)
    assert not S.lock_h47_libre()
    fd.close()


# ---------------------------------------------------------------- (1) cierre limpio con SIGTERM
def test_cerrar_b_usa_sigterm_nunca_screen_quit(W):
    W.viva, W.pid = True, 4242
    assert S.cerrar_b() is True
    assert W.kills == [(4242, signal.SIGTERM)]
    assert not [c for c in W.runs if "quit" in c]                    # no hay `screen -X quit`


def test_cerrar_b_espera_a_que_suelte_el_lock_y_no_escala(W, monkeypatch):
    W.viva, W.pid = True, 4242
    W.muere_con_sigterm = False                                     # B tarda: no muere
    assert S.cerrar_b() is False
    assert W.kills == [(4242, signal.SIGTERM)]                       # UN solo SIGTERM, nada de SIGKILL ni 2a senal
    assert W.t - T0 >= S.TERM_ESPERA_S


def test_cerrar_b_no_devuelve_true_si_el_lock_sigue_tomado(W, monkeypatch):
    W.viva, W.pid = True, 4242
    monkeypatch.setattr(S, "lock_h47_libre", lambda: False)
    assert S.cerrar_b() is False


def test_agotada_cierra_con_sigterm_rota_y_relanza(W):
    arranque(W, suelo=20.0, dt=-2000)
    W.escribe("puja_post", dt=-1500, oid="a")
    W.escribe("fuera_libro", dt=-1400, oid="a")
    W.escribe("bloqueo_suelo_saldo", dt=-1200)
    W.viva, W.pid, W.saldo = True, 4242, 20.9                        # saldo-suelo 0,9 < 1,5
    W.rot_resultado = (0, "tanda rotada")
    assert S.ciclo() == "rotar"
    assert W.kills == [(4242, signal.SIGTERM)]
    assert any("--rotar-tanda" in c for c in W.runs)
    assert W.lanzados == 1


def test_agotada_no_cierra_si_saldo_menos_suelo_supera_el_margen(W):
    arranque(W, suelo=20.0, dt=-2000)
    W.escribe("bloqueo_suelo_saldo", dt=-1200)
    W.viva, W.pid, W.saldo = True, 4242, 22.0                        # 2,0 >= 1,5: H47 se negaria
    assert S.ciclo() == "no_agotada"
    assert not W.kills and not W.runs


def test_agotada_no_cierra_con_ordenes_vivas(W):
    arranque(W, suelo=20.0, dt=-2000)
    W.escribe("intencion_post", dt=-1300, oid="viva")
    W.escribe("bloqueo_suelo_saldo", dt=-1200)
    W.viva, W.pid, W.saldo = True, 4242, 20.5
    assert S.ciclo() == "vivas"
    assert not W.kills


def test_ganancia_asegurable_cierra_con_sigterm_y_relanza(W):
    arranque(W, suelo=20.0, dt=-3000)
    W.escribe("puja_post", dt=-500, oid="a")
    W.escribe("fuera_libro", dt=-400, oid="a")
    W.viva, W.pid, W.saldo = True, 4242, 27.0
    assert S.ciclo() == "reinicio_ganancia"
    assert W.kills == [(4242, signal.SIGTERM)] and W.lanzados == 1


def test_ganancia_asegurable_espera_si_hay_orden_viva(W):
    arranque(W, suelo=20.0, dt=-3000)
    W.escribe("puja_post", dt=-500, oid="a")
    W.viva, W.pid, W.saldo = True, 4242, 27.0
    assert S.ciclo() == "vivas" and not W.kills


def test_ganancia_asegurable_no_relanza_si_cierre_falla(W):
    arranque(W, suelo=20.0, dt=-3000)
    W.escribe("puja_post", dt=-500, oid="a")
    W.escribe("fuera_libro", dt=-400, oid="a")
    W.viva, W.pid, W.saldo = True, 4242, 27.0
    W.muere_con_sigterm = False
    assert S.ciclo() == "cierre_fallo"
    assert W.lanzados == 0 and pausado_ok(W)


def pausado_ok(W):
    return S.pausado(W.t)


# ---------------------------------------------------------------- (2) B recien lanzado no es "agotado"
def test_bloqueo_anterior_al_ultimo_arranque_se_ignora(W):
    arranque(W, suelo=20.0, dt=-5000)
    W.escribe("bloqueo_suelo_saldo", dt=-4000)
    W.escribe("suelo_reiniciado", origen="rotar_tanda", dt=-3000, saldo_base=25.0)
    arranque(W, suelo=20.0, dt=-1000)                                # B recien lanzado tras la rotacion
    assert S.tanda_agotada_inactiva(W.t) is False


def test_gracia_tras_arranque_aunque_el_bloqueo_sea_posterior(W):
    arranque(W, suelo=20.0, dt=-300)                                 # 5 min desde el arranque < gracia
    W.escribe("bloqueo_suelo_saldo", dt=-290)
    assert S.tanda_agotada_inactiva(W.t) is False
    W.t += 400                                                       # 11,5 min tras el arranque y > 600 s desde el bloqueo
    assert S.tanda_agotada_inactiva(W.t) is True


def test_bloqueo_seguido_de_puja_no_es_agotada(W):
    arranque(W, dt=-3000)
    W.escribe("bloqueo_suelo_saldo", dt=-2000)
    W.escribe("puja_post", dt=-1000, oid="a")
    assert S.tanda_agotada_inactiva(W.t) is False


def test_ciclo_tras_rotacion_no_vuelve_a_rotar_B_recien_lanzado(W):
    arranque(W, suelo=20.0, dt=-4000)
    W.escribe("bloqueo_suelo_saldo", dt=-3500)
    W.escribe("suelo_reiniciado", origen="rotar_tanda", dt=-100, saldo_base=20.9)
    arranque(W, suelo=15.9, dt=-60)
    W.viva, W.pid, W.saldo = True, 4242, 20.9
    assert S.ciclo() == "ok" and not W.kills


# ---------------------------------------------------------------- (3) fin por tope y tope de lanzamientos
def test_fin_por_tope_no_relanza_y_avisa(W):
    arranque(W, suelo=20.0, dt=-3000, n_max=230)
    W.escribe("fin_ejecucion", dt=-100, pujas=230, kill=None, parada=None)
    W.viva, W.saldo = False, 25.0
    assert S.fin_por_tope()
    assert S.ciclo() == "tope"
    assert W.lanzados == 0
    assert any("tope" in m for m in W.tg)


def test_fin_con_parada_no_es_tope(W):
    arranque(W, n_max=230)
    W.escribe("fin_ejecucion", dt=10, pujas=31, kill=None, parada="saldo bajo")
    assert not S.fin_por_tope()


def test_nuevo_arranque_despues_del_tope_lo_anula(W):
    arranque(W, n_max=230, dt=-500)
    W.escribe("fin_ejecucion", dt=-400, pujas=230, parada=None)
    arranque(W, n_max=400, dt=-100)                                  # Javi subio --n a mano
    assert not S.fin_por_tope()


def test_caida_sin_kill_relanza_pero_con_tope_por_hora(W):
    arranque(W, suelo=20.0, dt=-100)
    W.saldo = 26.0                                                   # sin parada, no es tope
    res = []
    for i in range(7):
        W.viva, W.pid = False, None
        res.append(S.ciclo())
        W.t += 120
    assert W.lanzados == S.MAX_LANZ_HORA - 1                         # 1 `config` del ledger + lanzamientos propios hasta el tope
    assert "relanzo_frenado" in res
    assert any("lanzamientos" in m for m in W.tg)
    assert S.pausado(W.t - 120)


def test_caida_con_kill_no_relanza(W):
    arranque(W)
    W.escribe("kill", motivo="x")
    assert S.ciclo() == "kill" and W.lanzados == 0


# ---------------------------------------------------------------- (4) frenos derivados del ledger + singleton
def test_rotaciones_se_derivan_del_ledger_tras_reinicio_del_proceso(W):
    for dt in (-90000, -7000, -3000):
        W.escribe("suelo_reiniciado", origen="rotar_tanda", dt=dt, saldo_base=20.0)
    W.escribe("suelo_reiniciado", dt=-1000, saldo_base=20.0)         # manual: no cuenta
    r = S.rotaciones_24h(W.t)
    assert len(r) == 2 and r[-1] == pytest.approx(T0 - 3000, abs=1)


def test_racha_de_rotaciones_pausa_y_avisa(W):
    arranque(W, suelo=20.0, dt=-5000)
    W.escribe("suelo_reiniciado", origen="rotar_tanda", dt=-600, saldo_base=21.0)   # hace 10 min < 45 min
    W.escribe("fin_ejecucion", dt=-500, pujas=50, parada="saldo bajo")
    W.viva, W.saldo = False, 21.0
    assert S.ciclo() == "rotar"
    assert not [c for c in W.runs if "--rotar-tanda" in c]
    assert S.pausado(W.t) and any("seguidas" in m for m in W.tg)


def test_tope_diario_propio_pausa(W):
    for i in range(S.MAX_ROT_SUP_DIA):
        W.escribe("suelo_reiniciado", origen="rotar_tanda", dt=-80000 + i * 5000, saldo_base=20.0)
    W.escribe("fin_ejecucion", dt=-100, pujas=10, parada="saldo bajo")
    W.viva, W.saldo = False, 20.0
    S.ciclo()
    assert not [c for c in W.runs if "--rotar-tanda" in c] and S.pausado(W.t)


def test_singleton_flock(tmp_path):
    a = S.tomar_lock(tmp_path / "x.lock")
    assert a is not None
    assert S.tomar_lock(tmp_path / "x.lock") is None                 # segundo vigilante: rechazado
    a.close()
    b = S.tomar_lock(tmp_path / "x.lock")
    assert b is not None
    b.close()


def test_main_sale_si_hay_otro_vigilante(W, monkeypatch):
    monkeypatch.setattr(S, "tomar_lock", lambda path=None: None)
    with pytest.raises(SystemExit):
        S.main()


# ---------------------------------------------------------------- (5) PAUSA_HASTA respetada en todas las ramas
def test_pausa_respetada_en_caida_sin_kill(W):
    arranque(W, dt=-100)
    S.fijar_pausa(W.t + 3600)
    W.viva = False
    assert S.ciclo() == "pausa" and W.lanzados == 0


def test_pausa_respetada_en_parada_y_rotacion(W):
    arranque(W, dt=-5000)
    W.escribe("fin_ejecucion", dt=-100, pujas=50, parada="saldo bajo")
    S.fijar_pausa(W.t + 3600)
    assert S.ciclo() == "pausa" and not W.runs and W.lanzados == 0


def test_pausa_respetada_en_agotada_y_en_ganancia(W):
    arranque(W, suelo=20.0, dt=-3000)
    W.escribe("bloqueo_suelo_saldo", dt=-1200)
    W.viva, W.pid, W.saldo = True, 4242, 20.5
    S.fijar_pausa(W.t + 3600)
    assert S.ciclo() == "pausa" and not W.kills
    W.ev.clear()
    S.LEDGER.write_text("")
    arranque(W, suelo=20.0, dt=-3000)
    W.escribe("puja_post", dt=-500, oid="a")
    W.escribe("fuera_libro", dt=-400, oid="a")
    W.saldo = 27.0
    assert S.ciclo() == "pausa" and not W.kills


def test_pausa_expira(W):
    S.fijar_pausa(W.t + 100)
    assert S.pausado(W.t)
    assert not S.pausado(W.t + 101)


# ---------------------------------------------------------------- (8) TimeoutExpired del CLI de rotacion
def test_timeout_con_rotacion_escrita_se_contabiliza_y_relanza(W):
    arranque(W, suelo=20.0, dt=-5000)
    W.escribe("fin_ejecucion", dt=-4000, pujas=50, parada="saldo bajo")
    W.viva, W.saldo = False, 20.9
    W.rot_resultado, W.rot_escribe = None, True                      # el CLI cuelga pero el ledger muestra el suelo_reiniciado
    assert S.ciclo() == "rotar"
    assert len(S.rotaciones_24h(W.t)) == 1
    assert W.lanzados == 1


def test_timeout_sin_rotacion_escrita_no_relanza(W):
    arranque(W, suelo=20.0, dt=-5000)
    W.escribe("fin_ejecucion", dt=-4000, pujas=50, parada="saldo bajo")
    W.viva, W.saldo = False, 20.9
    W.rot_resultado, W.rot_escribe = None, False
    assert S.ciclo() == "rotar"
    assert W.lanzados == 0 and S.pausado(W.t) and any("NO realizada" in m for m in W.tg)


def test_h47_se_niega_no_relanza(W):
    arranque(W, suelo=20.0, dt=-5000)
    W.escribe("fin_ejecucion", dt=-4000, pujas=50, parada="saldo bajo")
    W.viva, W.saldo = False, 20.9
    W.rot_resultado, W.rot_escribe = (1, "--rotar-tanda: no se rota"), False
    S.ciclo()
    assert W.lanzados == 0 and S.pausado(W.t)


# ---------------------------------------------------------------- (9) contador desde el ledger al arrancar (proceso nuevo)
def test_proceso_nuevo_conoce_rotaciones_previas(W):
    for dt in (-20000, -15000, -10000, -9000, -8000, -7000):
        W.escribe("suelo_reiniciado", origen="rotar_tanda", dt=dt, saldo_base=20.0)
    arranque(W, dt=-6000)
    W.escribe("fin_ejecucion", dt=-3000, pujas=40, parada="saldo bajo")
    W.viva, W.saldo = False, 20.0
    assert S.LANZ_T == [] and S.AVISOS_T == {}                       # estado en memoria vacio (proceso recien arrancado)
    S.ciclo()
    assert not [c for c in W.runs if "--rotar-tanda" in c]           # ya hay 6 en 24 h segun el ledger
    assert any("tope propio" in m for m in W.tg)


def test_parada_antigua_no_dispara_rotacion_tras_nuevo_arranque(W):
    arranque(W, dt=-5000)
    W.escribe("fin_ejecucion", dt=-4000, pujas=50, parada="saldo bajo")
    arranque(W, dt=-1000)                                            # B se relanzo despues y cayo sin fin_ejecucion
    assert S.parada_sin_reseteo() is False


def test_ordenes_vivas_cuenta_solo_desde_el_ultimo_arranque(W):
    arranque(W, dt=-5000)
    W.escribe("intencion_post", dt=-4900, oid="vieja")
    arranque(W, dt=-1000)
    W.escribe("intencion_post", dt=-900, oid="a")
    W.escribe("intencion_post", dt=-800, oid="b")
    W.escribe("fuera_libro", dt=-700, oid="a")
    W.escribe("post_rechazada", dt=-600, oid="c")
    assert S.ordenes_vivas() == ["b"]


def test_rotacion_desactivada_no_rota_ni_cierra_ni_relanza(W, monkeypatch):
    monkeypatch.setattr(S, "ROTACION_AUTOMATICA", False)
    # B parada por `parada`: avisa y no relanza
    arranque(W, suelo=20.0, dt=-2000)
    W.escribe("fin_ejecucion", dt=-100, pujas=100, kill=None, parada="tanda agotada")
    W.viva, W.saldo = False, 20.5
    assert S.ciclo() == "agotada_sin_rotar"
    assert W.lanzados == 0 and not W.runs
    # B viva pero agotada: no la cierra
    W.viva, W.pid, W.saldo = True, 4242, 20.5
    W.escribe("bloqueo_suelo_saldo", dt=-1200)
    assert S.ciclo() == "agotada_sin_rotar"
    assert not W.kills and not W.runs


def test_relanza_con_n_500():
    assert "--n 500" in open(S.__file__).read() and "--n 230" not in open(S.__file__).read()
