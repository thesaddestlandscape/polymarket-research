"""Aisla los tests del lock REAL de la wallet dedicada (lo tiene el proceso B real): nunca se toca."""
import sys, tempfile
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(1, "/root/polymarket-research-dev")
import experimento_maker_h47 as H
H.LOCK_PARES = Path(tempfile.mkdtemp(prefix="lock_pares_test_")) / "pares.lock"
import h47_robustez as R            # los tests que ejecutan run() no deben escribir en los datalogs reales
_T = Path(tempfile.mkdtemp(prefix="h47r_test_"))
R.DIR = _T
R.RECON_OUT = str(_T / "puja_fin_reconstruido.jsonl")
