#!/bin/bash
# extraer_l2_b5m.sh DIA : extracto diario del plano de B (bids <= PMAX=0,40 de TODOS los tokens 5m, T y G integras) a
# libro5_b40/. REUTILIZA extraer_libro5_bajos.sh (idempotente, .tmp+mv); solo cambia PMAX y destino. NO instalado en cron.
# Espejo: el bid de L a p y el ask del complementario a 1-p son el mismo nivel; con bids<=0,40 de ambos tokens basta.
set -u
DIA="$1"
E=/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/captura_eventos_nivel/extraer_libro5_bajos.sh
PMAX=0.40 "$E" "$DIA" /mnt/HC_Volume_106538179/libro5_ms /mnt/HC_Volume_106538179/libro5_b40
