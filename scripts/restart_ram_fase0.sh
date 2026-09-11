#!/bin/bash
# restart_ram_fase0.sh -- reinicio diario de las screens fase0 consolidadas
# que más RAM acumulan con el tiempo (09-Sep, barrido de salud: RAM al
# límite, 235MB libres, swap 84%, 27 OOM-kills en 24h. vigiasfreq
# (vigias_frecuentes_fase0.py, scheduler de ~50 vigías en 1 proceso) y
# observadores (observadores_fase0.py, ~30 observadores en hilos dentro de
# 1 proceso) medidos con 1.7GB y 665MB de RSS respectivamente -- memoria
# acumulada de caches/objetos que CPython no siempre devuelve al SO, no un
# leak puntual identificado.
#
# Mitigación operativa, NO el fix de fondo: la causa raíz real (todo el
# pipeline de shadow_postmortem.py releyendo results.csv completo cada
# ciclo, más el número de procesos concurrentes en un VPS de 4 cores/7.6GB)
# requiere un rediseño mayor, aparcado para sesión dedicada -- ver memoria
# nativa project_pendiente_rediseno_pipeline_ram_09sep. Este script solo
# libera la memoria acumulada de 2 screens que son PURO monitoreo/logging
# (no ejecutan órdenes de dinero real -- eso vive en ejeclive/ejecdryrun/
# walletmirror, screens aparte, nunca tocadas aquí), usando el mecanismo ya
# existente y probado (verify_deploy.py --restart, incluye probe post-
# restart). Ambas screens ya corren con nice -n 10 desde el incidente de
# CPU del 05-Ago.
#
# Horario: 03:20 UTC, después de comprimir_data_historica.sh (03:00) y
# backup_results_csv.sh (03:05), antes de la ventana horaria live de Asia
# (04:00-05:00 UTC / 06:00-07:00 Madrid) -- franja sin trading activo
# conocido en ninguna estrategia con ventana horaria.
set -uo pipefail

cd /root/polymarket-research
for screen in vigiasfreq observadores; do
  echo "$(date -u) restart $screen"
  .venv/bin/python verify_deploy.py --restart "$screen"
done
echo "$(date -u) fin. RAM tras reinicio:"
free -h | head -2
