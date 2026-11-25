"""Unidades de la 3a pasada de revision (lib_espera_hijos.sh / p6_ciclo_aislado.py): regex transitoria anclada (1), firma del adelanto (2), cap_ok por cfg y no por falta de
modulo (5), cfg atomicos con manifiesto y reversion inversa (6/8), ventanas horarias (7). Los de despliegue completo (3, 7, 8, 9, 10) estan en test_deploy_sandbox.py."""
import importlib.util, os, shutil, subprocess, sys
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from test_espera_hijos import sh, V3, LIB, REPO                      # noqa: E402

PY = "/root/polymarket-research/.venv/bin/python"
_spec = importlib.util.spec_from_file_location("p6_ciclo_aislado", V3 / "deploy/p6_ciclo_aislado.py")
P6 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(P6)

# ---------------------------------------------------------------- (1) regex transitoria anclada
NO_TRANSITORIO = ["precio 94290.5 en 1429 mercados", "1429 gamma slug=x", "ts=1700000429 ok", "hora 2026-11-14T10:42:9Z", "429 mercados nuevos", "HTTP 4290", "slug-429-abc",
                  "Timeout" + "x", "  Eventos unicos: 429", "ERROR polymarket: ValueError: x",
                  # L2: texto libre NO anclado / formas que capture_markets no imprime: no excusan nada
                  "HTTP 429", "status_code=429", "status: 429", "requests.exceptions.HTTPError: 502", "Max retries exceeded with url", "se vio un Read timed out en medio",
                  "log: Connection reset by peer", "ConnectionError", "timed out", "      Read timed out indentado como codigo", "x [429] gamma: rafaga abortada", "NameError: name 'Timeout' is not defined"]
SI_TRANSITORIO = ["  [429] gamma: rafaga abortada hasta 10:02:00Z", "  429 gamma slug=x offset=0: rafaga abortada (la lista parcial NO se guardara)",
                  "429 Client Error: Too Many Requests for url: https://gamma", "  429: ciclo abortado, 3 mercados parciales DESCARTADOS", "gamma en pausa tras 429 hasta 10:02:00Z",
                  "ERROR polymarket: ConnectionError: x", "Error gamma slug=a: ReadTimeout: x", "HTTP Error 503: Service Unavailable", "Read timed out", "Name or service not known",
                  "Connection refused", "  ERROR precios: OSError: [Errno 110] Connection timed out"]


def _bash_excusa(tmp_path, txt):
    return sh(tmp_path, 'cap_excusa "$T"', env={"T": txt}).strip() != ""


@pytest.mark.parametrize("txt", NO_TRANSITORIO)
def test_1_un_429_suelto_o_texto_libre_no_anclado_no_es_excusa_transitoria(tmp_path, txt):
    assert not _bash_excusa(tmp_path, txt) and not P6.excusa(txt), txt


@pytest.mark.parametrize("txt", SI_TRANSITORIO)
def test_1_las_formas_reales_de_429_y_red_si_lo_son(tmp_path, txt):
    assert _bash_excusa(tmp_path, txt) and P6.excusa(txt), txt


def test_1_bash_y_runner_usan_el_mismo_clasificador_de_excusa(tmp_path):
    corpus = "\n".join(NO_TRANSITORIO + SI_TRANSITORIO)
    assert [l for l in sh(tmp_path, 'cap_excusa "$T"', env={"T": corpus}).splitlines() if l] == P6.excusa(corpus)


# ---------------------------------------------------------------- (2) firma del adelanto: solo adelanto_*.csv
def test_2_la_firma_del_adelanto_ignora_new_market_universo(tmp_path):
    d = tmp_path / "univ"; d.mkdir()
    (d / "adelanto_2026-11-14.csv").write_text("a\n")
    f = lambda: sh(tmp_path, "adelanto_firma", env={"CFGDIR": str(d)}).strip()
    f0 = f()
    (d / "new_market_universo_2026-11-14.csv.gz").write_text("x")              # el listener independiente escribe: NO cambia la firma
    f1 = f(); (d / "new_market_universo_2026-11-14.csv.gz").write_text("xx" * 100)
    assert f0 == f1 == f()
    (d / "adelanto_2026-11-14.csv").write_text("a\nb\n")                         # el adelanto SI
    assert f() != f0


# ---------------------------------------------------------------- (5) cap_ok: apagado POR CFG (modulo presente), rc 0
def _dir_capture(tmp, con_io):
    d = tmp / "dir"; d.mkdir(); shutil.copy(V3 / "stage/capture_markets.py", d)
    if con_io:
        shutil.copy(V3 / "stage/universo_5m_io.py", d)
    return d


def _repo_sin_modulo(tmp):
    r = tmp / "repo_sin_io"; r.mkdir(); shutil.copy("/root/polymarket-research/data_quality.py", r)
    return r


def _cap_ok(tmp, d, extra=None, repo=None):
    (tmp / "dl").mkdir(exist_ok=True)
    return sh(tmp, f'cap_ok "{d}"; echo "rc=$? $CAP_OK_MOTIVO"', env={"REPO": str(repo or REPO), "DL": str(tmp / "dl"), "PY": PY, **(extra or {})}, timeout=120)


def test_5_cap_ok_pasa_solo_con_modulo_presente_y_adelanto_apagado(tmp_path):
    assert "rc=0" in _cap_ok(tmp_path, _dir_capture(tmp_path, True))


def test_5_sin_universo_5m_io_cap_ok_falla_aunque_solo_adelanto_imprima_apagado(tmp_path):
    out = _cap_ok(tmp_path, _dir_capture(tmp_path, False), repo=_repo_sin_modulo(tmp_path))
    assert "rc=1" in out and "falta de modulo" in out, out


def test_5_adelanto_activo_por_cfg_no_pasa_y_un_rc_distinto_de_0_tampoco(tmp_path):
    d = _dir_capture(tmp_path, True)
    (tmp_path / "dl/traspaso_deltas_ws/_vacio").mkdir(parents=True); (tmp_path / "dl/traspaso_deltas_ws/_vacio/cfg_CAPTURE_5M_HORIZONTE_MIN").write_text("1440")
    out = _cap_ok(tmp_path, d)
    assert "rc=1" in out and "ACTIVO" in out, out
    (tmp_path / "dl/traspaso_deltas_ws/_vacio/cfg_CAPTURE_5M_HORIZONTE_MIN").unlink()
    (d / "capture_markets.py").write_text("raise SystemExit(7)\n")
    out = _cap_ok(tmp_path, d)
    assert "rc=1" in out, out


# ---------------------------------------------------------------- (6)(8) cfg atomicos, registrados y revertidos en orden inverso
def _cfg(tmp_path, cuerpo, extra=None, pre=None):
    d = tmp_path / "univ"; d.mkdir(exist_ok=True)
    for k, v in (pre or {}).items():
        (d / k).write_text(v)
    env = {"CFGDIR": str(d), "CFG_MANIFEST": str(tmp_path / "pre/manifest.txt"), "CONFIRMO_ADELANTO_6_MONEDAS": "1", **(extra or {})}
    return sh(tmp_path, 'log() { echo "LOG $*"; }\n' + cuerpo, env=env)


def test_6_activar_escribe_el_fix_antes_que_el_horizonte_de_forma_atomica_y_registra(tmp_path):
    out = _cfg(tmp_path, 'activar_cfg; echo "rc=$?"')
    d = tmp_path / "univ"
    assert "rc=0" in out and (d / "cfg_CAPTURE_429_FIX").read_text().strip() == "1" and (d / "cfg_CAPTURE_5M_HORIZONTE_MIN").read_text().strip() == "1440"
    assert [Path(x).name for x in (tmp_path / "pre/manifest.txt").read_text().split()] == ["cfg_CAPTURE_429_FIX", "cfg_CAPTURE_5M_HORIZONTE_MIN"]      # orden de escritura
    assert not list(d.glob(".cfg.*")), "no quedan temporales (tmp + mv)"


def test_6_8_revertir_borra_solo_lo_que_escribio_el_despliegue_y_en_orden_inverso(tmp_path):
    out = _cfg(tmp_path, 'activar_cfg; revertir_cfg; echo "rc=$?"', pre={"cfg_CAPTURE_5M_HORIZONTE_MIN": "7"})        # el horizonte lo escribio alguien a mano
    d = tmp_path / "univ"
    assert (d / "cfg_CAPTURE_5M_HORIZONTE_MIN").read_text() == "7", "lo escrito a mano ni se pisa ni se borra"
    assert not (d / "cfg_CAPTURE_429_FIX").exists() and "ya existia" in out
    out = _cfg(tmp_path, 'rm -f "$CFGDIR"/cfg_*; : > "$CFG_MANIFEST"; activar_cfg; revertir_cfg')
    revertidos = [l.split("/")[-1] for l in out.splitlines() if "cfg revertido" in l]
    assert revertidos == ["cfg_CAPTURE_5M_HORIZONTE_MIN", "cfg_CAPTURE_429_FIX"], out                              # inverso al de escritura


def test_6_si_falla_la_2a_escritura_se_revierte_la_1a(tmp_path):
    (tmp_path / "stub").mkdir()
    (tmp_path / "stub/mv").write_text('#!/bin/bash\ncase "$*" in *HORIZONTE*) exit 1;; esac\nexec /bin/mv "$@"\n'); (tmp_path / "stub/mv").chmod(0o755)
    out = _cfg(tmp_path, 'activar_cfg; echo "rc=$?"', extra={"PATH": f"{tmp_path}/stub:" + os.environ["PATH"]})
    d = tmp_path / "univ"
    assert "rc=1" in out and not (d / "cfg_CAPTURE_429_FIX").exists() and not (d / "cfg_CAPTURE_5M_HORIZONTE_MIN").exists() and not list(d.glob(".cfg.*")), out
    assert (tmp_path / "pre/manifest.txt").read_text() == ""


# ---------------------------------------------------------------- (7) ventanas horarias
HM = lambda h, m: h * 60 + m


@pytest.mark.parametrize("minuto,prohibida", [
    (HM(5, 59), False), (HM(6, 0), True), (HM(9, 14), True), (HM(9, 15), False), (HM(13, 29), False), (HM(13, 30), True), (HM(20, 59), True), (HM(21, 0), False),
    (HM(3, 39), False), (HM(3, 40), True), (HM(4, 4), True), (HM(4, 5), False), (HM(11, 40), True), (HM(12, 5), False), (HM(19, 40), True),
    (HM(23, 39), False), (HM(23, 40), True), (HM(23, 59), True), (HM(0, 0), True), (HM(0, 4), True), (HM(0, 5), False), (1440 + 360, True), (-1, True)])
def test_7_ventana_de_en_los_limites(tmp_path, minuto, prohibida):
    out = sh(tmp_path, f'ventana_de {minuto} && echo "SI $VENTANA" || echo NO').strip()
    assert out.startswith("SI") == prohibida, (minuto, out)


@pytest.mark.parametrize("desde,esperado", [(HM(3, 15), 25), (HM(5, 50), 10), (HM(7, 0), 0), (HM(21, 0), 160), (HM(0, 5), 215), (HM(9, 15), 145)])
def test_7_min_hasta_ventana(tmp_path, desde, esperado):
    assert sh(tmp_path, f'min_hasta_ventana {desde}; echo "$MH"').strip() == str(esperado)


# ---------------------------------------------------------------- (3) el segmento analizado es el del ciclo NUEVO (desde su cabecera de run_slow.sh), no lo del viejo
def _verifica(tmp_path, nuevo_contenido):
    slow = tmp_path / "slow.log"; slow.write_text("previo\n")
    cuerpo = f'''
cap_pre=""; P6_MARCA_TS=$(( $(date +%s) - 10 )); P6_MARCA_OFF=$(stat -c %s {slow}); MARKETS_DIR={tmp_path}/mk; mkdir -p $MARKETS_DIR
printf 'Traceback (most recent call last):\\n  File "{REPO}/capture_markets.py", line 1, in f\\nImportError: del proceso VIEJO\\n[t] --- Ciclo slow 4 fin ---\\n' >> {slow}
printf '[t] --- Ciclo slow 5 ---\\n' >> {slow}
setsid sleep 2 & p=$!; echo "$p 1 python {REPO}/capture_markets.py" > "$PSF"
(sleep 1; printf '{nuevo_contenido}' >> {slow}; printf '[t] === Fin ===\\n' >> {slow}) &
P6_ESPERA_S=10 P6_PASO=0.3 verifica_capture {slow}; echo "rc=$? $CAP_MOTIVO"'''
    return sh(tmp_path, cuerpo, env={"P6_CICLO_S": "20"}, timeout=60)


def test_3_lo_escrito_antes_de_la_cabecera_del_ciclo_nuevo_no_cuenta(tmp_path):
    out = _verifica(tmp_path, "  429: ciclo abortado, 3 mercados parciales DESCARTADOS\\n")
    assert "rc=2" in out and "crecimiento no verificado" in out and "error de codigo" not in out, out      # el ImportError del proceso viejo (tras el offset, antes de la cabecera) se ignora (no es rc 1); el 429 del nuevo sin crecimiento es inconcluso (4), no OK


def test_3_un_traceback_del_ciclo_nuevo_si_cuenta(tmp_path):
    out = _verifica(tmp_path, 'Traceback (most recent call last):\\n  File "%s/capture_markets.py", line 3, in f\\nKeyError: x\\n' % REPO)
    assert "rc=1" in out and "error de codigo" in out, out
