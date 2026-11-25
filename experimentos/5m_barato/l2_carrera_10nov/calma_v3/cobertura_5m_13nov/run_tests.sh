#!/bin/bash
# Ejecuta TODOS los tests de CB: pytest (capture/io/listener/vigia) + harness de libro_estado_ws (v5 + horizonte + siembra NMU).
CB="$(cd "$(dirname "$0")" && pwd)"
PY=/root/polymarket-research/.venv/bin/python
cd /root/polymarket-research && $PY -m pytest -q -p no:cacheprovider "$CB/tests" || exit 1
W="$(mktemp -d)"
cp "$CB/delta_nmu/libro_estado_ws.v5_horizonte_nmu.py" "$W/libro_estado_ws.py"
cp "$CB/delta_nmu/test_tokens_universo_nmu.py" "$W/test_tokens_universo.py"
cp "$CB/stage/universo_5m_io.py" "$W/"
cd "$W" && $PY -I test_tokens_universo.py | grep -E "FALLA|ERROR|TOTAL"; rc=${PIPESTATUS[0]}
rm -rf "$W"; exit $rc
