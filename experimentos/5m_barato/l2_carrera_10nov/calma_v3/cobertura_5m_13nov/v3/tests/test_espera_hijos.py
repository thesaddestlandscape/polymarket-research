"""Unidad de la lib P5 compartida (deploy/lib_espera_hijos.sh): espera_hijos sostenida, hijos_vivos anclado, log_nuevo con rotacion, traceback_fatal,
espera_bnreg, libro5_crece. `ps` falso (fichero). Ademas: los DOS scripts de despliegue hacen 'source' de la lib (no hay copia) y la lib esta en SHA256SUMS."""
import os, subprocess
from pathlib import Path
import pytest

V3 = Path(__file__).resolve().parent.parent
CAL = V3.parent.parent
LIB = V3 / "deploy" / "lib_espera_hijos.sh"
REPO = "/root/polymarket-research"


def sh(tmp_path, cuerpo, ps="", env=None, timeout=60, vivos=None):
    """Ejecuta `cuerpo` con la lib cargada y un `ps` falso (fichero PSF con lineas 'pid ppid args'). vivos=True: el falso `ps` oculta los pids que ya no existen
    en /proc (para probar la escalada TERM/KILL con procesos reales); por defecto muestra el fichero tal cual."""
    (tmp_path / "bin").mkdir(exist_ok=True)
    (tmp_path / "ps_out").write_text(ps)
    (tmp_path / "bin/ps").write_text('#!/bin/bash\nwhile read -r l; do p=${l%% *}; case " $STUB_REALES " in *" $p "*) [ -d /proc/$p ] || continue;; esac; echo "$l"; done < "$PSF"\n')
    (tmp_path / "bin/ps").chmod(0o755)
    e = {"PATH": f"{tmp_path}/bin:" + os.environ["PATH"], "PSF": str(tmp_path / "ps_out"), "REPO": REPO, "P5_PASO": "0.3", "P5_ESTABLE_S": "1", "P5_MUEREN_S": "2",
         "P5_TERM_S": "999", "LOGOBS": str(tmp_path / "obs.log"), "TMP": str(tmp_path), "LIBRO5": str(tmp_path / "libro5"), "STUB_REALES": " ".join(map(str, vivos or []))}
    e.update(env or {})
    cmd = f'log() {{ :; }}; . {LIB}\n' + cuerpo
    return subprocess.run(["bash", "-c", cmd], capture_output=True, text=True, env=e, timeout=timeout).stdout


def espera(tmp_path, ps_ini, viejos, despues=None, retardo=0.6, env=None):
    bg = f'(sleep {retardo}; printf "%s" "{despues}" > "$PSF") &\n' if despues is not None else ""
    return sh(tmp_path, f'viejos="{viejos}"\n{bg}espera_hijos; echo "rc=$? HIJO=$HIJO PPID=$HIJO_PPID"; echo "$ESPERA_MOTIVO"', ps_ini, env)


OBS = lambda p: f"{p} 1 .venv/bin/python observadores_fase0.py\n"
H = lambda pid, ppid=900: f"{pid} {ppid} python -u {REPO}/libro_estado_ws.py --hijo\n"


def test_viejos_salen_dentro_del_plazo_pasa(tmp_path):
    ps = OBS(900) + H(11, 1) + H(12, 1) + H(99)                       # viejos 11/12 huerfanos (padre muerto), nuevo 99 hijo de observadores 900
    out = espera(tmp_path, ps, "11 12", despues=OBS(900) + H(99))
    assert "rc=0 HIJO=99 PPID=900" in out, out


def test_ya_solo_el_nuevo_pasa_tras_la_ventana_estable(tmp_path):
    assert "rc=0 HIJO=99" in espera(tmp_path, OBS(900) + H(99), "11 12")


def test_viejo_que_no_sale_falla_tras_el_plazo(tmp_path):
    out = espera(tmp_path, OBS(900) + H(11, 1) + H(99), "11 12")
    assert "rc=1" in out and "viejos aun vivos '11'" in out, out


def test_viejo_con_padre_observadores_vivo_cuenta_como_viejo(tmp_path):
    out = espera(tmp_path, OBS(800) + OBS(900) + H(11, 800) + H(99), "11")
    assert "rc=1" in out and "viejos aun vivos '11'" in out, out


def test_dos_nuevos_sostenidos_fallan_como_respawn_o_hijo_extra(tmp_path):
    out = espera(tmp_path, OBS(900) + H(99) + H(98), "11 12")
    assert "rc=1" in out and "RESPAWN" in out and "'99 98'" in out, out


def test_segundo_nuevo_transitorio_tambien_es_duro(tmp_path):
    out = espera(tmp_path, OBS(900) + H(99) + H(98), "11", despues=OBS(900) + H(99), retardo=0.8, env={"P5_ESTABLE_S": "2", "P5_MUEREN_S": "3"})
    assert "rc=1" in out and "RESPAWN" in out, out


def test_respawn_del_hijo_es_duro(tmp_path):
    out = sh(tmp_path, 'viejos="11"\n(sleep 0.6; printf "" > "$PSF"; sleep 0.6; printf "%s" "' + OBS(900) + H(77) + '" > "$PSF") &\nespera_hijos; echo "rc=$?"; echo "$ESPERA_MOTIVO"',
             OBS(900) + H(99), {"P5_MUEREN_S": "4", "P5_ESTABLE_S": "2"})
    assert "rc=1" in out and "RESPAWN" in out and "'99 77'" in out, out


def test_cero_hijos_falla_tras_el_plazo(tmp_path):
    out = espera(tmp_path, "", "11 12")
    assert "rc=1" in out and "= 0 hijos" in out, out


def test_nuevo_que_muere_y_no_es_sustituido_falla(tmp_path):
    out = espera(tmp_path, OBS(900) + H(99), "11", despues=OBS(900), retardo=0.5)
    assert "rc=1" in out and "= 0 hijos" in out, out


def test_hijo_ajeno_con_ruta_de_main_pero_otro_padre_no_cuenta(tmp_path):
    """I1: un 'libro_estado_ws.py --hijo' con la ruta de main pero hijo de otro proceso (medicion, harness) no es ni viejo ni nuevo."""
    ps = OBS(900) + H(99) + "600 1 python medir_hijo_real.py /x\n" + H(97, 600) + H(96, 1)
    out = espera(tmp_path, ps, "11")
    assert "rc=0 HIJO=99 PPID=900" in out, out
    assert sh(tmp_path, 'echo "[$(hijos_vivos)]"', ps).strip() == "[99]"


def test_hijos_vivos_solo_ruta_de_este_repo_y_padre_observadores(tmp_path):
    ps = OBS(900) + H(5) + "6 900 python /root/polymarket-research-dev/libro_estado_ws.py --hijo\n7 900 python /tmp/h/libro_estado_ws.py --hijo\n8 900 vim libro_estado_ws.py\n" + H(3)
    assert sh(tmp_path, 'echo "[$(hijos_vivos)]"', ps).strip() == "[3 5]"


def _sleeper():
    return int(subprocess.run(["bash", "-c", "setsid sleep 600 >/dev/null 2>&1 & echo $!"], capture_output=True, text=True).stdout.strip())


def test_escalada_term_a_viejo_huerfano_que_no_sale(tmp_path):
    """(a) un viejo cuyo padre YA no es observadores y no muere: SIGTERM tras P5_TERM_S (el sleeper muere con TERM) y el despliegue sigue. El `ps` falso oculta los pids reales ya muertos."""
    v = _sleeper()
    try:
        ps = OBS(900) + H(v, 1) + H(99)
        out = sh(tmp_path, f'viejos="{v}"\nespera_hijos; echo "rc=$? HIJO=$HIJO"; echo "$ESPERA_MOTIVO"', ps, {"P5_TERM_S": "1", "P5_KILL_GRACIA": "5", "P5_MUEREN_S": "6"}, vivos=[v])
        assert "rc=0 HIJO=99" in out, out
        assert not os.path.exists(f"/proc/{v}"), "el viejo huerfano deberia haber muerto por SIGTERM"
    finally:
        subprocess.run(["kill", "-9", str(v)], capture_output=True)


def test_escalada_kill_si_ignora_term(tmp_path):
    v = int(subprocess.run(["bash", "-c", "setsid bash -c 'trap \"\" TERM; while true; do sleep 1; done' >/dev/null 2>&1 & echo $!"], capture_output=True, text=True).stdout.strip())
    try:
        out = sh(tmp_path, f'viejos="{v}"\nespera_hijos; echo "rc=$? HIJO=$HIJO"', OBS(900) + H(v, 1) + H(99),
                 {"P5_TERM_S": "1", "P5_KILL_GRACIA": "2", "P5_MUEREN_S": "9"}, vivos=[v])
        assert "rc=0 HIJO=99" in out, out
        assert not os.path.exists(f"/proc/{v}")
    finally:
        subprocess.run(["kill", "-9", str(v)], capture_output=True)


def test_nunca_se_mata_a_un_viejo_con_padre_observadores_vivo_ni_a_ajenos(tmp_path):
    v, ajeno = _sleeper(), _sleeper()
    try:
        ps = OBS(800) + OBS(900) + H(v, 800) + H(ajeno, 600) + H(99)
        out = sh(tmp_path, f'viejos="{v}"\nespera_hijos; echo "rc=$?"', ps, {"P5_TERM_S": "1", "P5_KILL_GRACIA": "1", "P5_MUEREN_S": "4"}, vivos=[v, ajeno])
        assert "rc=1" in out, out
        assert os.path.exists(f"/proc/{v}") and os.path.exists(f"/proc/{ajeno}")
    finally:
        for p in (v, ajeno): subprocess.run(["kill", "-9", str(p)], capture_output=True)


def test_verif_final_ok_y_fallos(tmp_path):
    (tmp_path / "libro5").mkdir(exist_ok=True)
    f5 = tmp_path / "libro5" / "libro5_ms_$(date -u +%F)_99.csv.gz"
    base = 'viejos="11"; off0=0; f=$LIBRO5/libro5_ms_$(date -u +%F)_99.csv.gz; : > $f; (sleep 0.5; echo "B,1" >> $f) &\n'
    obs = "[x] conectado [BTC#5min], 4 tokens (lector en proceso separado, pid 99)\n[x] lector hijo lanzado (pid 99)\n"
    (tmp_path / "obs.log").write_text(obs)
    out = sh(tmp_path, base + 'verif_final 99; echo "rc=$? $ESPERA_MOTIVO"', OBS(900) + H(99), {"P5_ESTABLE_S": "0", "P5_CRECE_S": "4"})
    assert "rc=0" in out, out
    (tmp_path / "obs.log").write_text(obs + "[x] lector hijo lanzado (pid 77)\n")                 # respawn: otro 'lanzado'
    out = sh(tmp_path, base + 'verif_final 99; echo "rc=$? $ESPERA_MOTIVO"', OBS(900) + H(99), {"P5_ESTABLE_S": "0", "P5_CRECE_S": "4"})
    assert "rc=1" in out and "respawn" in out, out
    (tmp_path / "obs.log").write_text(obs + "[x] conectado [ETH#5min], 4 tokens (lector en proceso separado, pid 77)\n")     # 'conectado' de otro pid
    out = sh(tmp_path, base + 'verif_final 99; echo "rc=$? $ESPERA_MOTIVO"', OBS(900) + H(99), {"P5_ESTABLE_S": "0", "P5_CRECE_S": "4"})
    assert "rc=1" in out and "respawn o hijo extra" in out, out
    (tmp_path / "obs.log").write_text(obs)
    out = sh(tmp_path, 'viejos="11"; off0=0; f=$LIBRO5/libro5_ms_$(date -u +%F)_99.csv.gz; : > $f\nverif_final 99; echo "rc=$? $ESPERA_MOTIVO"', OBS(900) + H(99),
             {"P5_ESTABLE_S": "0", "P5_CRECE_S": "2"})                                              # libro5 mudo (hilo muerto): DURO
    assert "rc=1" in out and "NO crece" in out, out


def test_libro5_crece_con_solo_filas_G_o_B_sin_filas_d(tmp_path):
    """(b) mercado quieto: basta cualquier fila (G/B/T); no se exige ninguna fila d."""
    (tmp_path / "libro5").mkdir(exist_ok=True); f = tmp_path / "libro5" / "libro5_ms_2026-11-14_7.csv.gz"; f.write_text("tipo,t_ms\n")
    assert "rc=0" in sh(tmp_path, f'(sleep 0.4; echo "G,1,*,arranque,,,1,1" >> {f}) &\nlibro5_crece 7 3; echo rc=$?')
    assert "rc=0" in sh(tmp_path, f'(sleep 0.4; echo "B,1,tok,0.4:5,0.5:5,,1,2" >> {f}) &\nlibro5_crece 7 3; echo rc=$?')
    assert "rc=1" in sh(tmp_path, 'libro5_crece 7 1; echo rc=$?')


@pytest.mark.parametrize("rotado", [False, True])
def test_log_nuevo_offset_ausente_y_rotacion(tmp_path, rotado):
    log = tmp_path / "obs.log"; log.write_text("A" * 100 + "\nviejo\n")
    off = log.stat().st_size
    if rotado: log.write_text("nuevo tras rotacion pid 5\n")       # mas corto que off0 => se relee desde 0
    else: log.write_text(log.read_text() + "nuevo pid 5\n")
    assert "nuevo" in sh(tmp_path, f'off0={off}\nlog_nuevo').lower()
    if not rotado: assert "viejo" not in sh(tmp_path, f'off0={off}\nlog_nuevo')
    log.unlink()
    assert sh(tmp_path, f'off0={off}\nlog_nuevo; echo fin').strip() == "fin"                        # log ausente: no revienta


def test_nuevos_pids_excluye_viejos(tmp_path):
    (tmp_path / "obs.log").write_text("[x] conectado [BTC#5min] pid 11\n[x] conectado [BTC#5min] pid 99\n")
    assert sh(tmp_path, 'off0=0; viejos="11 12"; nuevos_pids | tr "\\n" " "').strip() == "99"


TB = lambda mod, exc: f'Traceback (most recent call last):\n  File "{REPO}/{mod}.py", line 3, in f\n    x()\n{exc}\n'


@pytest.mark.parametrize("exc,fatal", [("KeyboardInterrupt", False), ("SystemExit: 0", False), ("BrokenPipeError: [Errno 32] Broken pipe", False), ("SIGTERM", False),
                                       ("ValueError: boom", True), ("KeyError: 'x'", True)])
def test_traceback_fatal_firmas_de_apagado(tmp_path, exc, fatal):
    (tmp_path / "t.txt").write_text("linea\n" + TB("libro_estado_ws", exc) + "otra linea\n")
    out = sh(tmp_path, 'traceback_fatal "$(cat $TMP/t.txt)" "libro_estado_ws|universo_5m_io" >/dev/null; echo rc=$?')
    assert ("rc=0" in out) == fatal, out


def test_traceback_de_otro_modulo_no_cuenta_y_mezcla_apagado_mas_real(tmp_path):
    (tmp_path / "t.txt").write_text(TB("otro_modulo", "ValueError: x"))
    assert "rc=1" in sh(tmp_path, 'traceback_fatal "$(cat $TMP/t.txt)" "libro_estado_ws" >/dev/null; echo rc=$?')
    (tmp_path / "t.txt").write_text(TB("libro_estado_ws", "KeyboardInterrupt") + TB("libro_estado_ws", "ValueError: real"))
    assert "rc=0" in sh(tmp_path, 'traceback_fatal "$(cat $TMP/t.txt)" "libro_estado_ws" >/dev/null; echo rc=$?')


def test_traceback_encadenado_se_juzga_por_la_ultima_excepcion(tmp_path):
    enc = TB("libro_estado_ws", "KeyboardInterrupt") + "\nDuring handling of the above exception, another exception occurred:\n\n" + TB("libro_estado_ws", "SystemExit: 1")
    (tmp_path / "t.txt").write_text(enc)
    assert "rc=1" in sh(tmp_path, 'traceback_fatal "$(cat $TMP/t.txt)" "libro_estado_ws" >/dev/null; echo rc=$?')


def test_espera_bnreg_un_latido_fresco_en_la_ventana_basta(tmp_path):
    cuerpo = ('echo 0 > $TMP/n; bn_estado_ok() { n=$(cat $TMP/n); echo $((n+1)) > $TMP/n; [ $n -ge 3 ]; }; bn_es_duenyo() { return 0; }\n'
              'espera_bnreg 5; echo "rc=$? n=$(cat $TMP/n)"')
    assert "rc=0 n=4" in sh(tmp_path, cuerpo)


def test_espera_bnreg_sin_latido_o_sin_lock_falla_al_final_de_la_ventana(tmp_path):
    assert "rc=1" in sh(tmp_path, 'bn_estado_ok() { return 1; }; bn_es_duenyo() { return 0; }; espera_bnreg 1; echo rc=$?')
    assert "rc=1" in sh(tmp_path, 'bn_estado_ok() { return 0; }; bn_es_duenyo() { return 1; }; espera_bnreg 1; echo rc=$?')


def test_script_hace_source_de_la_lib_sin_copia_y_la_lib_esta_en_sha256sums():
    t = (V3 / "deploy/deploy_deltas_libro_ws_once.sh").read_text()
    assert "lib_espera_hijos.sh" in t and "espera_hijos() {" not in t and "hijos_vivos() {" not in t
    assert " deploy/lib_espera_hijos.sh" in (V3 / "SHA256SUMS").read_text()


def test_espera_tick_watchdog_sincroniza_con_el_proximo_ciclo_sin_exigir_cambio_de_log(tmp_path):
    w = tmp_path / "wd.log"; w.write_text("x\n")
    t = subprocess.run(["bash", "-c", f'log() {{ :; }}; . {LIB}; s=$SECONDS; espera_tick_watchdog {w}; echo "rc=$? t=$((SECONDS-s))"'], capture_output=True, text=True,
                       env={**os.environ, "WD_PERIODO": "2", "WD_MARGEN": "0"}, timeout=30).stdout
    assert "rc=0" in t, t                       # el log NO cambia durante la espera y aun asi pasa (el log real solo escribe cada ~10 min)


def test_espera_tick_watchdog_falla_si_el_log_falta_o_lleva_mas_de_900_s(tmp_path):
    w = tmp_path / "wd.log"
    run = lambda: subprocess.run(["bash", "-c", f'log() {{ :; }}; . {LIB}; espera_tick_watchdog {w}; echo rc=$?'], capture_output=True, text=True,
                                 env={**os.environ, "WD_PERIODO": "1", "WD_MARGEN": "0"}, timeout=30).stdout
    assert "rc=1" in run()
    w.write_text("x"); os.utime(w, (1, 1))
    assert "rc=1" in run()
