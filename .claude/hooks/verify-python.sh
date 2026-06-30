#!/usr/bin/env bash
# Tras editar un .py, verifica sintaxis con py_compile y bloquea si falla.

TOOL_INPUT=$(cat)
FILE=$(echo "$TOOL_INPUT" | python3 -c "
import sys,json
d=json.load(sys.stdin)
ti=d.get('tool_input',{})
print(ti.get('path') or ti.get('file_path') or '')
" 2>/dev/null)

[[ "$FILE" != *.py ]] && exit 0
[[ ! -f "$FILE" ]] && exit 0

ERR=$(python3 -m py_compile "$FILE" 2>&1)
if [ -n "$ERR" ]; then
    python3 -c "
import json,sys
print(json.dumps({
    'decision': 'block',
    'reason': sys.argv[1]
}))" "$FILE: $ERR"
    exit 0
fi
exit 0
