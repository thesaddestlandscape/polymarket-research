#!/bin/bash
# Forward DIARIO en dry-run de 5m barato (OK Javi 14-Oct): V6_FOK_VUELO_BTC y V5_ORIGEN15M, SEPARADOS pero en SERIE (nunca a
# la vez: RAM). Procesa el día UTC anterior, cuando ya existen m5_registro/m15_registro (03:45/04:00) y el archivo
# registro_5m_barato (03:50). Cada paso con su ulimit y aviso de Telegram si falla; un fallo no impide el siguiente.
# Cron: 50 5 * * *  (antes del racimo 06-09Z). SOLO OBSERVACIÓN: nada firma ni envía órdenes.
cd /root/polymarket-research || exit 1
D=$(date -u -d "yesterday" +%Y-%m-%d)
PY=/usr/bin/python3
avisa() { $PY -c "import sys; sys.path.insert(0,'/root/polymarket-research'); from shadow_digest import enviar_telegram as e; e('🚨 Forward 5m barato: $1 FALLÓ ($D), ver logs/m5barato_forward_diario.log')"; }
echo "=== $(date -u +%FT%TZ) día $D"
# 1) V6: simulación de órdenes en vuelo del día (caché fok_vuelo_D_p250) + vigía
bash -c "ulimit -v 2500000; nice -n 15 ionice -c3 $PY analisis_5m_barato_fok_vuelo.py --desde $D --hasta $D" || avisa "V6 simulación"
bash -c "nice -n 15 $PY vigia_5m_barato_v6_forward.py --telegram" || avisa "V6 vigía"
$PY diag_v6_visible_anticipada.py || true      # diagnóstico visible/anticipada (fuera del fichero congelado)
# 2) V5: laboratorio (maquinaria v4 a 215/355/475 ms sobre el archivo) + vigía
bash -c "ulimit -v 4500000; nice -n 15 ionice -c3 $PY lab_5m_barato_replay.py --dia $D --tag lat" || avisa "V5 laboratorio"
bash -c "nice -n 15 $PY vigia_5m_barato_v5_forward.py --telegram" || avisa "V5 vigía"
# 3) Vigilancia por moneda (Javi 14-Oct: "mantenlo vigilado"): quién gana en los pares del día (caché on-chain) y pastel de
#    la caja por moneda acumulado -> si una altcoin muestra ventaja EVIDENTE, se explora con gate propio.
bash -c "ulimit -v 3500000; nice -n 15 ionice -c3 $PY analisis_5m_barato_quien_gana.py --desde $D --hasta $D" > /dev/null || avisa "quién gana (pares)"
bash -c "ulimit -v 2000000; nice -n 15 ionice -c3 $PY analisis_5m_barato_pastel_caja.py" | grep -E "PASTEL|por activo|por día" || avisa "pastel caja"
echo "=== fin $(date -u +%FT%TZ)"
