#!/usr/bin/env bash
# Diagnóstico rápido del pipeline. Imprime PASS/FAIL por check.
# Salida: JSON con campos ok, issues[], summary.
set -euo pipefail
cd /root/polymarket-research

ISSUES=()

# 1. Sintaxis Python scripts críticos
SYNTAX=$(python3 -m py_compile \
  shadow_predict.py shadow_resolve.py shadow_postmortem.py \
  shadow_resumen.py fetch_binance_klines.py live_trade.py live_guard.py 2>&1) && \
  SYNTAX_OK=true || SYNTAX_OK=false
[[ $SYNTAX_OK == false ]] && ISSUES+=("SYNTAX:$SYNTAX")

# 2. Predictions CSV de hoy — ¿tiene filas o solo header?
HOY=$(date -u +%Y-%m-%d)
CSV="data/shadow/predictions_${HOY}.csv"
if [ -f "$CSV" ]; then
  BYTES=$(stat -c%s "$CSV" 2>/dev/null || stat -f%z "$CSV")
  LINES=$(wc -l < "$CSV")
  [[ $BYTES -le 300 ]] && ISSUES+=("PREDICTIONS_EMPTY:${CSV} ${BYTES}B ${LINES}L")
else
  ISSUES+=("PREDICTIONS_MISSING:$CSV")
fi

# 3. estado_actual.md — edad máxima 5 min
ESTADO="data/shadow/estado_actual.md"
if [ -f "$ESTADO" ]; then
  AGE=$(( $(date +%s) - $(stat -c%Y "$ESTADO" 2>/dev/null || stat -f%m "$ESTADO") ))
  [[ $AGE -gt 300 ]] && ISSUES+=("ESTADO_STALE:${AGE}s sin actualizar")
else
  ISSUES+=("ESTADO_MISSING")
fi

# 4. data_quality.json — ¿algún asset CRITICAL?
DQ="data/shadow/data_quality.json"
if [ -f "$DQ" ]; then
  CRITICAL=$(python3 -c "
import json
d=json.load(open('$DQ'))
crit=[s for s,v in d.get('assets',{}).items() if v.get('estado')=='CRITICAL']
print(','.join(crit))
" 2>/dev/null)
  [[ -n "$CRITICAL" ]] && ISSUES+=("DATA_CRITICAL:$CRITICAL")
fi

# 5. strategy_params.json — JSON válido con clave 'estrategias'
SP="data/shadow/strategy_params.json"
if [ -f "$SP" ]; then
  python3 -c "import json; d=json.load(open('$SP')); assert 'estrategias' in d" 2>/dev/null || \
    ISSUES+=("PARAMS_INVALID:strategy_params.json corrupto o sin clave 'estrategias'")
fi

# 6. Patrón UnboundLocalError conocido en shadow_predict.py
UBL=$(grep -n 'json.loads(features_json)' shadow_predict.py 2>/dev/null | head -3 || true)
[[ -n "$UBL" ]] && ISSUES+=("UNBOUND_RISK:json.loads antes de asignación:$UBL")

# 7. shadow_resolve.py — throttle y filtro SKIP
if [ -f "shadow_resolve.py" ]; then
  HAS_SLEEP=$(grep -c 'time\.sleep' shadow_resolve.py 2>/dev/null || echo 0)
  HAS_SKIP=$(grep -c 'SKIP' shadow_resolve.py 2>/dev/null || echo 0)
  WORKERS=$(grep -oP 'workers\s*[:=]\s*\K\d+' shadow_resolve.py 2>/dev/null | head -1 || echo 0)
  [[ $HAS_SLEEP -eq 0 ]] && ISSUES+=("RESOLVE_NO_THROTTLE:shadow_resolve.py sin time.sleep — riesgo 429")
  [[ $HAS_SKIP -eq 0 ]] && ISSUES+=("RESOLVE_NO_SKIP:shadow_resolve.py no filtra decision==SKIP")
  [[ -n "$WORKERS" && $WORKERS -gt 5 ]] && ISSUES+=("RESOLVE_WORKERS_HIGH:workers=$WORKERS>5 — riesgo 429")
fi

# 8. shadow_postmortem.py — checkpoint usa prediction_timestamp
if [ -f "shadow_postmortem.py" ]; then
  HAS_CKPT=$(grep -c 'cargar_ya_postmortem\|ya_procesadas' shadow_postmortem.py 2>/dev/null || echo 0)
  HAS_TS=$(grep -c 'prediction_timestamp' shadow_postmortem.py 2>/dev/null || echo 0)
  [[ $HAS_CKPT -eq 0 ]] && ISSUES+=("POSTMORTEM_NO_CHECKPOINT:sin función de deduplicación — riesgo duplicados")
  [[ $HAS_CKPT -gt 0 && $HAS_TS -eq 0 ]] && ISSUES+=("POSTMORTEM_CHECKPOINT_SIN_TS:checkpoint no usa prediction_timestamp — duplicados posibles")
fi

# Output estructurado
NISSUES=${#ISSUES[@]}
if [[ $NISSUES -eq 0 ]]; then
  python3 -c "import json; print(json.dumps({'ok':True,'issues':[],'summary':'Pipeline OK — sin bugs detectados'}))"
else
  python3 -c "
import json,sys
issues=sys.argv[1:]
print(json.dumps({'ok':False,'issues':issues,'summary':f'{len(issues)} problema(s) detectado(s)'}))
" "${ISSUES[@]}"
fi
