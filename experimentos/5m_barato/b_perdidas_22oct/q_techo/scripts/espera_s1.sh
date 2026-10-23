#!/bin/bash
until grep -q FIN /root/polymarket-research-datalogs/q_techo/s1.log; do sleep 20; done
cd /root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/q_techo
ulimit -v 5000000
nice -n 19 ionice -c3 python3 -I scripts/s2_feat.py > /root/polymarket-research-datalogs/q_techo/s2.log 2>&1
echo S2FIN >> /root/polymarket-research-datalogs/q_techo/s2.log
