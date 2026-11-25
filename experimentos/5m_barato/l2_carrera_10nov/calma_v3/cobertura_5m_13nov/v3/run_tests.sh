#!/bin/bash
# Ejecuta TODOS los tests de CB/v3: pytest (capture/io/listener/vigia + sandbox del despliegue) + harness de libro_estado_ws (v5 + horizonte + nmu + pausa 429).
# Sin --rapido incluye el sandbox del despliegue (~3 min). Nunca toca el sistema real (DEPLOY_SANDBOX=1 aborta si una ruta es la real).
CB="$(cd "$(dirname "$0")" && pwd)"
PY=/root/polymarket-research/.venv/bin/python
EXTRA=""; [ "${1:-}" = "--rapido" ] && EXTRA="--ignore=$CB/tests/test_deploy_sandbox.py"
# L3: volumen de pruebas para los e2e (tmpfs de 12 GB: tope, no reserva RAM) montado aqui y desmontado SIEMPRE por el trap (EXIT/INT/TERM). Se salta con --rapido o si ya hay E2E_DIR.
# Lanzar:  setsid bash run_tests.sh > run.log 2>&1 &   (E2E_DIR=/otro/volumen_con_>=10GB para usar el tuyo; sin montajes manuales)
E2E_VOL=""
limpia_vol() { [ -n "$E2E_VOL" ] && bash "$CB/tests/e2e/vol_e2e.sh" limpia "$E2E_VOL"; E2E_VOL=""; }
trap limpia_vol EXIT; trap 'exit 143' INT TERM
if [ "${1:-}" != "--rapido" ] && [ -z "${E2E_DIR:-}" ]; then
  E2E_VOL=$(bash "$CB/tests/e2e/vol_e2e.sh" monta) && export E2E_DIR="$E2E_VOL" || { E2E_VOL=""; echo "AVISO: no se pudo montar el tmpfs de pruebas (mount requiere root); los e2e fallaran con el mensaje 'E2E necesita >=10 GB libres'"; }
fi
cd /root/polymarket-research && $PY -m pytest -q -p no:cacheprovider $EXTRA "$CB/tests" || exit 1
W="$(mktemp -d)"
cp "$CB/delta_v3/libro_estado_ws.py" "$W/libro_estado_ws.py"
cp "$CB/delta_v3/test_tokens_universo.py" "$W/test_tokens_universo.py"
cp "$CB/stage/universo_5m_io.py" "$W/"
cd "$W" && $PY -I test_tokens_universo.py | grep -E "FALLA|ERROR|TOTAL|CALLS"; rc=${PIPESTATUS[0]}
cd "$CB" && rm -rf "$W"; exit $rc
