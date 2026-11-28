#!/usr/bin/env python3
"""fetch_polymarket_fills_onchain_v3.py (27-Nov, engineer 5m barato; ANEXO_V2 §1). Indexa ExchangeV3 0xe3333700cA9d93003F00f0F71f8515005F6c00Aa (mercados Protocol V2 de SOL/XRP/BNB/DOGE/HYPE desde ~23-Nov 13:25Z).
REUTILIZA SIN COPIAR el decodificador de fetch_polymarket_fills_onchain.py (mismos topics/ABI): se importa el modulo y solo se cambian EXCHANGE, CHECKPOINT, el directorio de salida (onchain_fills_YYYY-MM-DD ->
onchain_fills_v3_YYYY-MM-DD.csv.gz, mismo esquema, un miembro gzip por ejecucion) y TRAMO. NO modifica el script actual ni sus ficheros. RPC solo por polygon_rpc (el modulo importado). 0 ordenes.
Uso:  fetch_polymarket_fills_onchain_v3.py                      (cron */5: desde el checkpoint a la cabeza, <=600 bloques/ejecucion)
      fetch_polymarket_fills_onchain_v3.py --backfill [--desde 97800000]   (bucle idempotente y reanudable hasta la cabeza; por scripts/cron_pesado.sh, nunca 22:00-02:45Z)
Checkpoint propio: datalogs/onchain_fills_v3_checkpoint.json (ultimo bloque escrito). Un fallo antes de escribir el checkpoint no deja duplicados salvo caida ENTRE el append del dia y el checkpoint: verificar con verifica_onchain_v3.py (unicidad (tipo,tx,log_index))."""
import sys, time, json, datetime
from pathlib import Path
REPO = Path(__file__).resolve().parent; sys.path.insert(0, str(REPO))
import fetch_polymarket_fills_onchain as F
EXCHANGE_V3 = "0xe3333700ca9d93003f00f0f71f8515005f6c00aa"
BASE = Path("/root/polymarket-research-datalogs"); CKPT = BASE / "onchain_fills_v3_checkpoint.json"
DESDE_BACKFILL = 97_800_000


class _DirV3:
    """Hace que F.main escriba onchain_fills_v3_<dia>.csv.gz en el mismo directorio (F.DATALOGS / 'onchain_fills_X' -> '.../onchain_fills_v3_X')."""
    def __truediv__(self, nombre): return BASE / nombre.replace("onchain_fills_", "onchain_fills_v3_", 1)


def preparar(tramo):
    F.EXCHANGE = EXCHANGE_V3; F.CHECKPOINT = CKPT; F.DATALOGS = _DirV3(); F.TRAMO = tramo   # 50: 1rpc limita getLogs a 50 bloques, drpc (plan gratis) a 100
    if "--sin-aviso" not in sys.argv: sys.argv.append("--sin-aviso")       # el aviso de F habla de onchain_fills (V2): el aviso V3 lo da vigia_loggers_silenciosos / checkpoint


def ultimo():
    try: return json.loads(CKPT.read_text())["ultimo_bloque"]
    except Exception: return None


def main():
    if "--backfill" in sys.argv:
        import fcntl
        lock = open("/tmp/fetch_polymarket_fills_onchain_v3.lock", "w")          # el MISMO fichero que usa `flock -n` del cron */5: backfill y cron en vivo nunca a la vez (un checkpoint)
        try: fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError: print("otro indexador V3 en curso (lock)", flush=True); return 0
        preparar(50)
        if ultimo() is None:
            d = int(sys.argv[sys.argv.index("--desde") + 1]) if "--desde" in sys.argv else DESDE_BACKFILL
            CKPT.write_text(json.dumps({"ultimo_bloque": d - 1, "actualizado_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(), "atraso": None, "nota": "semilla de backfill"}))
        while True:
            h = int(time.strftime("%H%M", time.gmtime()))
            if h >= 2200 or h < 245: print("PARADA: ventana 22:00-02:45Z; reanudable", flush=True); return 3
            u0 = ultimo(); F.main(3000)
            if ultimo() == u0: print("sin bloques nuevos: backfill al dia", flush=True); return 0
            time.sleep(0.3)
    preparar(50)
    try: return F.main(600)
    except Exception as e: print(f"FALLO v3: {type(e).__name__}: {e}", flush=True); raise


if __name__ == "__main__":
    sys.exit(main())
