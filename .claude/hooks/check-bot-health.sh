#!/usr/bin/env bash
# Tras cualquier edición de python, verifica que el bot sigue corriendo.
# Si el último commit de shadow tiene más de 10min → avisa.

TOOL_INPUT=$(cat)
FILE=$(echo "$TOOL_INPUT" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('path') or d.get('file_path') or '')" 2>/dev/null)

# Solo actuar en scripts del pipeline
[[ "$FILE" != *shadow_predict* ]] && [[ "$FILE" != *shadow_resolve* ]] && [[ "$FILE" != *fetch_binance* ]] && exit 0

LAST_COMMIT_TS=$(git log -1 --format="%ct" -- data/shadow/estado_actual.md 2>/dev/null)
if [ -z "$LAST_COMMIT_TS" ]; then exit 0; fi

NOW=$(date +%s)
AGE=$(( NOW - LAST_COMMIT_TS ))

if [ "$AGE" -gt 600 ]; then
    MIN=$(( AGE / 60 ))
    echo "⚠️  AVISO: El bot lleva ${MIN}min sin actualizar estado_actual.md. ¿Está corriendo el loop fast?" >&2
fi
exit 0
