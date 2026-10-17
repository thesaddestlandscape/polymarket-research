import pandas as pd, numpy as np, pickle
P=pd.read_pickle("/tmp/claude-0/-root-polymarket-research/a0c96fc2-2902-4388-9cab-9cffc412228c/scratchpad/vend/an/S.pkl")
def ev(pn,c):
    c=float(np.sum(c)); return float(np.sum(pn)/c) if c>0 else float("nan")
