#!/usr/bin/env bash
# Bloquea ediciones directas a ficheros críticos del pipeline.
# results.csv y strategy_params.json solo se modifican vía scripts, no a mano.

TOOL_INPUT=$(cat)
FILE=$(echo "$TOOL_INPUT" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('path') or d.get('file_path') or '')" 2>/dev/null)

PROTECTED=("data/shadow/results.csv" "data/shadow/strategy_params.json" "data/live/.env" "data/live/LIVE_MODE_ON")

for p in "${PROTECTED[@]}"; do
    if [[ "$FILE" == *"$p"* ]]; then
        echo "{\"decision\":\"deny\",\"reason\":\"$FILE es gestionado por scripts del pipeline. Edítalo con el script correspondiente, no directamente.\"}"
        exit 0
    fi
done

echo '{"decision":"allow"}'
exit 0
