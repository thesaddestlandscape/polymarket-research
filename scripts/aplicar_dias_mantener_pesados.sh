#!/bin/bash
# Tarea unica programada con `at` (14-Nov, OK Javi): tras el despliegue v3 de las 22:19Z, comprimir antes (2 dias en vez de 3)
# SOLO data/markets, data/wallets/positions_* y leaderboard_* (~1,5 GB menos en /, sda1 al 88 %).
# Auditado 14-Nov: los lectores vivos de esos tres leen hoy/ayer ([-2:]) o solo escriben; el resto de patrones (trades, chainlink,
# polybolt, activity_ws, sports_spread, predictions, datalogs) NO se tocan. Sin perdida: comprimir_dir hace gzip + cmp y solo entonces borra.
# Idempotente, con copia .bak y bash -n; si algo falla, restaura y no toca nada. Log: logs/aplicar_dias_mantener.log
set -u
S=/root/polymarket-research/scripts/comprimir_data_historica.sh
LOG=/root/polymarket-research/logs/aplicar_dias_mantener.log
exec >>"$LOG" 2>&1
echo "=== $(date -u +%FT%TZ) inicio"
# 1) esperar a que acabe el despliegue (hasta 40 min); el [d] evita que pgrep se vea a si mismo
for i in $(seq 1 80); do pgrep -f "[d]eploy_deltas_libro_ws_once" >/dev/null || break; sleep 30; done
pgrep -f "[d]eploy_deltas_libro_ws_once" >/dev/null && { echo "ABORTO: el despliegue sigue corriendo; reintentar a mano"; exit 3; }
grep -q 'CUTOFF_COMPRIMIR_PESADOS' "$S" && { echo "ya aplicado, nada que hacer"; exit 0; }
cp -p "$S" "$S.bak_14nov" || { echo "ABORTO: no se pudo hacer copia"; exit 1; }
python3 - "$S" <<'EOF' || { cp -p "$S.bak_14nov" "$S"; echo "FALLO parche, restaurado"; exit 1; }
import sys
p = sys.argv[1]; s = open(p).read()
a = 'CUTOFF_COMPRIMIR_DATALOGS=$(date -u -d "-${DIAS_MANTENER_DATALOGS} days" +%Y-%m-%d)\n'
assert s.count(a) == 1
s = s.replace(a, a + '# 14-Nov (OK Javi): ventana de 2 dias SOLO para markets/positions/leaderboard (disco / al 88 %); el resto sigue en DIAS_MANTENER=3.\nDIAS_MANTENER_PESADOS=2\nCUTOFF_COMPRIMIR_PESADOS=$(date -u -d "-${DIAS_MANTENER_PESADOS} days" +%Y-%m-%d)\n')
for old in ('comprimir_dir data/markets "*.csv"\n',
            'comprimir_dir data/wallets "leaderboard_*.csv"\n',
            'comprimir_dir data/wallets "positions_*.csv"\n'):
    assert s.count(old) == 1, old
    s = s.replace(old, old.rstrip('\n') + ' "$CUTOFF_COMPRIMIR_PESADOS"\n')
open(p, 'w').write(s)
EOF
bash -n "$S" || { cp -p "$S.bak_14nov" "$S"; echo "FALLO bash -n, restaurado"; exit 1; }
grep -n 'CUTOFF_COMPRIMIR_PESADOS' "$S"
echo "OK aplicado; lo ejecuta el cron de las 03:00 UTC (gzip+cmp antes de borrar). Revertir: cp -p $S.bak_14nov $S"
