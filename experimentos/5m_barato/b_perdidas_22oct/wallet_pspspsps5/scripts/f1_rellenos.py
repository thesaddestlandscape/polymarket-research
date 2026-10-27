#!/usr/bin/env python3
"""f1: extrae rellenos on-chain 5m de pspspsps5 (0xb0f85baa...) por dia, reutilizando rellenos_dia de analisis_mo_money_pares_5m (solo lectura)."""
import sys
sys.path.insert(0, "/root/polymarket-research")
from pathlib import Path
import analisis_mo_money_pares_5m as mm
mm.W = "0xb0f85baa97990910a3e8ac2b4a58a322f01ecef5"
mm.OUT = Path("/root/polymarket-research-datalogs/wallet_pspspsps5")
for d in sys.argv[1:]:
    R = mm.rellenos_dia(d)
    print(d, None if R is None else (len(R), round(R.usdc.sum(), 1)), flush=True)
