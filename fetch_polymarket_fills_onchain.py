#!/usr/bin/env python3
"""fetch_polymarket_fills_onchain.py -- sigue la cadena (Polygon) y guarda cada relleno del exchange de Polymarket con
MAKER y TOMADOR explícitos (05-Oct, misión "quién captura la ventana Binance -> Polymarket": el firehose solo deja
inferir el rol con heurística). Contrato actual descubierto desde un recibo real: 0xe111180000d2663c0091e4f400237545b87b996b
(las direcciones antiguas 0x4bFb.../0xC5d5... ya no emiten); ABI verificado en Sourcify v2:
  OrderFilled(bytes32 indexed orderHash, address indexed maker, address indexed taker, uint8 side, uint256 tokenId,
              uint256 makerAmountFilled, uint256 takerAmountFilled, uint256 fee, bytes32 builder, bytes32 metadata)
  OrdersMatched(bytes32 indexed takerOrderHash, address indexed takerOrderMaker, uint8 side, uint256 tokenId,
                uint256 makerAmountFilled, uint256 takerAmountFilled)
Verificado con una operación BTC 15m: el maker paga 0 de comisión y el tomador 0,07·p·(1−p)·acciones.
Salida: datalogs `onchain_fills_YYYY-MM-DD.csv.gz` (un miembro gzip COMPLETO por ejecución, nunca truncado; retención en
comprimir_data_historica.sh). Columnas: tipo (F=OrderFilled, M=OrdersMatched), bloque, ts_est (s, interpolado entre la
cabecera inicial y final del tramo; error < 1 bloque ≈ 1,5 s), tx, log_index, order_hash, maker, taker (en M: vacío),
side, token_id, maker_amt, taker_amt (6 decimales), fee. ~45 rellenos/s en todo Polymarket.
Cron */5 con flock. Estado: data/shadow/onchain_fills_checkpoint.json (último bloque escrito).
"""
import gzip
import io
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests
from eth_utils import keccak

REPO = Path(__file__).resolve().parent
RPC = "https://polygon-bor-rpc.publicnode.com"      # mismo que taker_rebate_tracker.py (polygon-rpc.com pide auth)
# 12-Oct: publicnode responde "Archive requests require a personal token" en cuanto el cursor se queda unos miles de
# bloques atrás. El 09-Oct 08:10 (racimo del OOM diario) se quedó atrás y desde entonces CADA ejecución pedía el mismo
# bloque viejo y moría: estado absorbente, 3,5 días sin datos on-chain (vigía H5M, misión 15m/5m). Failover a RPCs
# públicos que SÍ sirven eth_getLogs de archivo (probados 12-Oct con el bloque atascado: drpc, 1rpc, tenderly).
RPCS = [RPC, "https://polygon.drpc.org", "https://1rpc.io/matic", "https://gateway.tenderly.co/public/polygon"]
ATRASO_AVISO = 2400   # bloques (~1 h): aviso por Telegram si el cursor va más atrás que esto tras la ejecución
EXCHANGE = "0xe111180000d2663c0091e4f400237545b87b996b"
T_FILL = "0x" + keccak(text="OrderFilled(bytes32,address,address,uint8,uint256,uint256,uint256,uint256,bytes32,bytes32)").hex()
T_MATCH = "0x" + keccak(text="OrdersMatched(bytes32,address,uint8,uint256,uint256,uint256)").hex()
CHECKPOINT = REPO / "data/shadow/onchain_fills_checkpoint.json"
DATALOGS = Path("/root/polymarket-research-datalogs")
MARGEN = 5            # bloques de margen: el balanceador del nodo público a veces no tiene aún el último
TRAMO = 40            # bloques por eth_getLogs (~60 s de cadena, ~2.700 eventos)
MAX_POR_RUN = 600     # bloques por ejecución (~15 min de cadena): ponerse al día sin pisar la siguiente
INICIO_SIN_ESTADO = 200


def rpc(metodo, params, intentos=3):
    """Prueba los RPCS en orden; en cada uno, `intentos` reintentos salvo que pida token de archivo (pasa al siguiente)."""
    ultimo_error = None
    for url in RPCS:
        for i in range(intentos):
            try:
                r = requests.post(url, json={"jsonrpc": "2.0", "id": 1, "method": metodo, "params": params}, timeout=60).json()
                if "error" in r:
                    raise RuntimeError(r["error"])
                return r["result"]
            except Exception as e:
                ultimo_error = e
                if "Archive requests" in str(e) or "personal token" in str(e):
                    break
                if i < intentos - 1:
                    print(f"  reintento {metodo} ({url}): {type(e).__name__}: {str(e)[:150]}", flush=True)
                    time.sleep(2 * (i + 1))
    raise ultimo_error


def ts_bloque(n):
    return int(rpc("eth_getBlockByNumber", [hex(n), False])["timestamp"], 16)


def main(max_por_run=MAX_POR_RUN):
    try:
        ultimo = json.loads(CHECKPOINT.read_text())["ultimo_bloque"]
    except Exception:
        ultimo = None
    cabeza = int(rpc("eth_blockNumber", []), 16) - MARGEN
    desde = (ultimo + 1) if ultimo else cabeza - INICIO_SIN_ESTADO
    hasta = min(cabeza, desde + max_por_run - 1)
    if hasta < desde:
        print("sin bloques nuevos")
        return 0
    filas_por_dia, n = {}, 0
    b = desde
    while b <= hasta:
        e = min(hasta, b + TRAMO - 1)
        logs = rpc("eth_getLogs", [{"fromBlock": hex(b), "toBlock": hex(e), "address": EXCHANGE,
                                    "topics": [[T_FILL, T_MATCH]]}])
        t_b, t_e = ts_bloque(b), ts_bloque(e)
        for lg in logs:
            bl = int(lg["blockNumber"], 16)
            ts = t_b + (t_e - t_b) * (bl - b) / max(1, e - b)
            d = lg["data"][2:]
            w = [d[i:i + 64] for i in range(0, len(d), 64)]
            top = lg["topics"]
            if top[0] == T_FILL:
                fila = ("F", bl, round(ts, 1), lg["transactionHash"], int(lg["logIndex"], 16), top[1],
                        "0x" + top[2][-40:], "0x" + top[3][-40:], int(w[0], 16), int(w[1], 16),
                        int(w[2], 16) / 1e6, int(w[3], 16) / 1e6, int(w[4], 16) / 1e6)
            else:
                fila = ("M", bl, round(ts, 1), lg["transactionHash"], int(lg["logIndex"], 16), top[1],
                        "0x" + top[2][-40:], "", int(w[0], 16), int(w[1], 16),
                        int(w[2], 16) / 1e6, int(w[3], 16) / 1e6, "")
            dia = datetime.fromtimestamp(ts, timezone.utc).strftime("%Y-%m-%d")
            filas_por_dia.setdefault(dia, []).append(",".join(str(x) for x in fila))
            n += 1
        b = e + 1
    for dia, filas in filas_por_dia.items():
        ruta = DATALOGS / f"onchain_fills_{dia}.csv.gz"
        buf = io.BytesIO()
        with gzip.GzipFile(fileobj=buf, mode="wb", compresslevel=6) as g:
            if not ruta.exists():
                g.write(b"tipo,bloque,ts_est,tx,log_index,order_hash,maker,taker,side,token_id,maker_amt,taker_amt,fee\n")
            g.write(("\n".join(filas) + "\n").encode())
        with open(ruta, "ab") as f:          # un miembro gzip completo por ejecución
            f.write(buf.getvalue())
    try:
        atraso_prev = json.loads(CHECKPOINT.read_text()).get("atraso")
    except Exception:
        atraso_prev = None
    CHECKPOINT.write_text(json.dumps({"ultimo_bloque": hasta, "actualizado_utc": datetime.now(timezone.utc).isoformat(),
                                      "atraso": cabeza - hasta}))
    print(f"{datetime.now(timezone.utc):%Y-%m-%dT%H:%M:%SZ} bloques {desde}-{hasta} ({hasta - desde + 1}), eventos {n}, "
          f"atraso respecto a la cabeza {cabeza - hasta} bloques", flush=True)
    # solo si el atraso NO baja (poniéndose al día baja en cada ejecución: no avisar cada 5 min)
    if (cabeza - hasta > ATRASO_AVISO and atraso_prev is not None and cabeza - hasta >= atraso_prev
            and "--sin-aviso" not in sys.argv):
        try:
            sys.path.insert(0, str(REPO))
            from shadow_digest import enviar_telegram
            enviar_telegram(f"⚠️ onchain_fills atrasado {cabeza - hasta} bloques (~{(cabeza - hasta) * 2.1 / 3600:.1f} h) respecto a "
                            f"la cabeza de Polygon: se está poniendo al día ({max_por_run} bloques/ejecución). Si no baja, "
                            f"revisar logs/fetch_polymarket_fills_onchain.log")
        except Exception as e:
            print(f"aviso Telegram falló: {e}", flush=True)
    return 0


def _avisar_fallo(e):
    """12-Oct: el fallo del 09-Oct era una EXCEPCIÓN en cada ejecución y nadie se enteró en 3,5 días. Aviso si el
    checkpoint lleva >30 min sin avanzar, como mucho uno cada 6 h (latch con hora)."""
    try:
        cp = json.loads(CHECKPOINT.read_text())
        edad = time.time() - datetime.fromisoformat(cp["actualizado_utc"]).timestamp()
        latch = REPO / "data/live/onchain_fills_aviso_latch.json"
        ult = json.loads(latch.read_text())["ts"] if latch.exists() else 0
        if edad > 1800 and time.time() - ult > 6 * 3600:
            sys.path.insert(0, str(REPO))
            from shadow_digest import enviar_telegram
            enviar_telegram(f"🚨 fetch_polymarket_fills_onchain FALLA y el checkpoint lleva {edad / 3600:.1f} h parado: "
                            f"{type(e).__name__}: {str(e)[:200]}")
            latch.write_text(json.dumps({"ts": time.time()}))
    except Exception as e2:
        print(f"aviso de fallo no enviado: {e2}", flush=True)


if __name__ == "__main__":
    max_run = MAX_POR_RUN
    if "--max-bloques" in sys.argv:
        max_run = int(sys.argv[sys.argv.index("--max-bloques") + 1])
    try:
        sys.exit(main(max_run))
    except Exception as e:
        _avisar_fallo(e)
        raise
