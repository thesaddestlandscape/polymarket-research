#!/bin/bash
ulimit -v 1500000
nice -n 19 ionice -c3 python3 /root/polymarket-research/experimentos/5m_barato/v4_comprar_lo_bueno/extrae.py /tmp/claude-0/-root-polymarket-research/ce552a77-92f9-49c1-8c13-d01ef139d7f6/scratchpad/ext
