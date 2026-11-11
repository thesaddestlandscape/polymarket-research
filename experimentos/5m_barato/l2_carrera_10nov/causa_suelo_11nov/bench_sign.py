import time, statistics as st, sys
from eth_account import Account
k = Account.create().key.hex()          # clave ALEATORIA desechable; no se lee ninguna clave real
from py_clob_client_v2 import ClobClient, OrderArgsV2, PartialCreateOrderOptions
from py_clob_client_v2.clob_types import CreateOrderOptions
import inspect
c = ClobClient("https://clob.polymarket.com", chain_id=137, key=k)
tok = "7" * 60
args = OrderArgsV2(token_id=tok, price=0.12, size=5.0, side="BUY")
ts = []
for i in range(60):
    t0 = time.perf_counter()
    o = c.builder.build_order(args, CreateOrderOptions(tick_size="0.01", neg_risk=False), version=2, fee_rate_bps=None)
    ts.append((time.perf_counter() - t0) * 1000)
print("build_order+firma ms n=%d min=%.2f p50=%.2f p90=%.2f max=%.2f" % (len(ts), min(ts), st.median(ts), sorted(ts)[int(.9*len(ts))], max(ts)))
