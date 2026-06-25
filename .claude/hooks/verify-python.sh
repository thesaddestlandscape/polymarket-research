#!/usr/bin/env bash
# Tras editar un .py, verifica que importa sin errores de sintaxis.

TOOL_INPUT=$(cat)
FILE=$(echo "$TOOL_INPUT" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('path') or d.get('file_path') or '')" 2>/dev/null)

[[ "$FILE" != *.py ]] && exit 0
[[ ! -f "$FILE" ]] && exit 0

cd /root/polymarket-research || exit 0
ERR=$(python3 -c "import ast; ast.parse(open('$FILE').read())" 2>&1)
if [ -n "$ERR" ]; then
    echo "⚠️ Syntax error en $FILE: $ERR" >&2
fi
exit 0
