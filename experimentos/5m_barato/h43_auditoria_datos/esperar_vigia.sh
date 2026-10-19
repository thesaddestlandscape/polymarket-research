#!/bin/bash
# espera a que el vigia R5K escriba el informe del 18-Oct (json con 2026-10-18 en cobertura) o 10:30Z como maximo
F=/root/polymarket-research/data/shadow/vigia_5m_barato_r5k.json
until grep -q '"2026-10-18"' "$F" 2>/dev/null || [ "$(date -u +%H%M)" -ge 1030 ]; do sleep 60; done
echo LISTO $(date -u +%H:%M)
