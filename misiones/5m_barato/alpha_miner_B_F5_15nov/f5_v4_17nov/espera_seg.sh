#!/bin/bash
H=/root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov/f5_v4_17nov
until grep -q "FIN run_seg\|paro en" $H/run_seg.log; do sleep 60; done; echo listo
