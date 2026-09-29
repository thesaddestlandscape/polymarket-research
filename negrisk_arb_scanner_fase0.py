#!/usr/bin/env python3
"""negrisk_arb_scanner_fase0.py -- FASE 0 (solo lectura, NUNCA orden real), 29-Sep.

Detecta arbitraje via conversión NegRiskAdapter -- el hueco real que
arb_scanner.py::analizar_oportunidades() (TIPO 2, "Overround Sell") ya
detecta pero marca como NO explotable ("requeriría vender, no disponible
en Polymarket sin posición previa"). Eso es incorrecto una vez se entiende
NegRiskAdapter: cuando sum(YES_i) > 1 en un grupo de outcomes mutuamente
excluyentes, típicamente sum(NO_i) < N-1 -- comprar el NO de TODOS los N
outcomes y convertirlos SÍ es una posición comprable (no requiere vender).

Mecánica exacta (verificada contra el contrato real, NO un blog de
terceros -- ver idea_negrisk_arb_investigado_29sep en memoria):
  contrato NegRiskAdapter.sol (github.com/Polymarket/neg-risk-ctf-adapter),
  función convertPositions(marketId, indexSet, amount):
    - indexSet = bitmask de outcomes cuyo NO se quema (k bits activos).
    - Si k==N (se queman los N NO): el llamante recibe
      (N-1) * amount * (1 - feeBips/10000) en USDC, SIN tokens YES.
    - feeBips es un parámetro fijado POR MERCADO en prepareMarket().
      Verificado on-chain (eth_call directo a getFeeBips(bytes32), función
      real del contrato desplegado en 0xd91E80cF2E7be2e162c6513ceD06f1dD0dA35296,
      Polygon) en 4 mercados reales activos distintos (elección francesa,
      Champions League, EPL, conteo de tweets): feeBips=0 en los 4 -- se
      asume 0 por defecto, pero se relee on-chain por evento para no
      asumir a ciegas si algún mercado tuviera un valor distinto.

Condición de arbitraje (k=N, la única que da USDC puro sin quedarte con
posición YES): coste = amount * sum(ask_NO_i, i=1..N) < payout =
amount * (N-1) * (1 - fee). Se ignora el caso k<N (mezcla YES+USDC) --
más complejo y no da una señal de arb limpia comparable.

Alcance deliberado: solo grupos con 2<=N<=30 (elecciones con 100+
candidatos son imposibles de llenar en la práctica y carísimas de
consultar -- 128 peticiones de libro por evento). Solo observación:
escribe data/shadow/negrisk_arb_fase0.csv, nunca coloca ninguna orden.

Cron sugerido: cada 15min (no es latencia-critica, una cesta de N legs
no se puede rellenar instantaneamente de todas formas).
"""
import csv
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

GAMMA = "https://gamma-api.polymarket.com"
NEGRISK_ADAPTER = "0xd91E80cF2E7be2e162c6513ceD06f1dD0dA35296"
RPC_URLS = ["https://polygon-bor-rpc.publicnode.com", "https://1rpc.io/matic"]
SELECTOR_GET_FEE_BIPS = "0x2582cb5e"  # keccak256("getFeeBips(bytes32)")[:4], verificado 29-Sep

N_MIN = 2
N_MAX = 30
MARGEN_MIN = 0.02   # exigir al menos 2% de margen sobre coste (cubre gas + slippage no medido)

OUT = REPO / "data" / "shadow" / "negrisk_arb_fase0.csv"
CAMPOS = ["timestamp_utc", "event_slug", "negrisk_market_id", "n_outcomes",
          "coste_total", "payout_bruto", "fee_bips", "payout_neto",
          "margen_abs", "margen_pct", "leg_mas_delgado_ask", "leg_mas_delgado_size",
          "n_legs_con_ask", "accionable"]

_SESSION = requests.Session()


def _log(msg: str) -> None:
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _get_fee_bips(market_id_hex: str) -> int | None:
    data = SELECTOR_GET_FEE_BIPS + market_id_hex[2:]
    for rpc in RPC_URLS:
        try:
            r = _SESSION.post(rpc, json={
                "jsonrpc": "2.0", "method": "eth_call",
                "params": [{"to": NEGRISK_ADAPTER, "data": data}, "latest"], "id": 1,
            }, timeout=8)
            resp = r.json()
            result = resp.get("result")
            if result:
                return int(result, 16)
        except Exception:
            continue
    return None


def _eventos_negrisk() -> list:
    eventos = []
    offset = 0
    while True:
        try:
            r = _SESSION.get(f"{GAMMA}/events", params={
                "closed": "false", "limit": 100, "offset": offset,
                "order": "volume24hr", "ascending": "false",
            }, timeout=15)
            r.raise_for_status()
            lote = r.json()
        except Exception as e:
            _log(f"error listando eventos (offset={offset}): {e}")
            break
        if not lote:
            break
        for e in lote:
            if e.get("negRisk") and e.get("negRiskMarketID"):
                eventos.append(e)
        offset += 100
        if offset >= 1000:  # techo razonable, evita barrer todo gamma-api cada corrida
            break
    return eventos


def _mejor_ask(token_id: str) -> tuple[float | None, float | None]:
    """(mejor_ask, size_en_ese_nivel) del token, o (None, None) si falla."""
    try:
        r = _SESSION.get("https://clob.polymarket.com/book", params={"token_id": token_id}, timeout=8)
        r.raise_for_status()
        book = r.json()
        asks = book.get("asks") or []
        if not asks:
            return None, None
        niveles = sorted(((float(a["price"]), float(a["size"])) for a in asks), key=lambda x: x[0])
        return niveles[0]
    except Exception:
        return None, None


def _token_no(mkt: dict) -> str | None:
    """Mismo criterio que resolution_sniper_observer.token_ids() pero solo el lado NO
    (no se importa esa función para no arrastrar sus dependencias de websocket)."""
    try:
        tokens = json.loads(mkt.get("clobTokenIds") or "[]")
        outcomes = json.loads(mkt.get("outcomes") or "[]")
    except Exception:
        return None
    if len(tokens) < 2 or len(outcomes) < 2:
        return None
    o0 = str(outcomes[0]).strip().lower()
    AFIRMATIVOS = {"yes", "up"}
    if o0 in AFIRMATIVOS:
        return tokens[1]
    return tokens[0]


def _guardar(fila: dict) -> None:
    nuevo = not OUT.exists()
    with open(OUT, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS)
        if nuevo:
            w.writeheader()
        w.writerow(fila)


def escanear_evento(evento: dict) -> None:
    slug = evento.get("slug", "")
    market_id = evento.get("negRiskMarketID", "")
    mercados = evento.get("markets", []) or []
    n = len(mercados)
    if not (N_MIN <= n <= N_MAX):
        return

    fee_bips = _get_fee_bips(market_id)
    if fee_bips is None:
        _log(f"[{slug}] no se pudo leer feeBips on-chain -- saltado (fail-closed)")
        return

    asks = []
    tamanos = []
    faltantes = 0
    for mkt in mercados:
        if mkt.get("closed") or mkt.get("acceptingOrders") is False:
            faltantes += 1
            asks.append(None)
            tamanos.append(None)
            continue
        tok_no = _token_no(mkt)
        if not tok_no:
            faltantes += 1
            asks.append(None)
            tamanos.append(None)
            continue
        ask, size = _mejor_ask(tok_no)
        asks.append(ask)
        tamanos.append(size)
        if ask is None:
            faltantes += 1

    n_con_ask = n - faltantes
    if faltantes > 0:
        # no se puede montar la cesta completa (k=N) sin TODOS los legs -- se
        # registra igualmente para ver cobertura, pero nunca accionable
        coste_total = None
        payout_bruto = payout_neto = margen_abs = margen_pct = None
        leg_min_ask = leg_min_size = None
        accionable = False
    else:
        coste_total = sum(asks)
        payout_bruto = (n - 1) * 1.0
        payout_neto = payout_bruto * (1 - fee_bips / 10_000)
        margen_abs = payout_neto - coste_total
        margen_pct = margen_abs / coste_total if coste_total > 0 else None
        idx_min = min(range(n), key=lambda i: asks[i])
        leg_min_ask, leg_min_size = asks[idx_min], tamanos[idx_min]
        accionable = margen_pct is not None and margen_pct >= MARGEN_MIN

    fila = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "event_slug": slug, "negrisk_market_id": market_id, "n_outcomes": n,
        "coste_total": round(coste_total, 4) if coste_total is not None else "",
        "payout_bruto": payout_bruto if payout_bruto is not None else "",
        "fee_bips": fee_bips,
        "payout_neto": round(payout_neto, 4) if payout_neto is not None else "",
        "margen_abs": round(margen_abs, 4) if margen_abs is not None else "",
        "margen_pct": round(margen_pct, 4) if margen_pct is not None else "",
        "leg_mas_delgado_ask": leg_min_ask if leg_min_ask is not None else "",
        "leg_mas_delgado_size": leg_min_size if leg_min_size is not None else "",
        "n_legs_con_ask": n_con_ask, "accionable": accionable,
    }
    _guardar(fila)
    if accionable:
        _log(f"🎯 [{slug}] N={n} coste={coste_total:.3f} payout_neto={payout_neto:.3f} "
             f"margen={margen_pct*100:.1f}% leg_delgado(ask={leg_min_ask},size={leg_min_size})")
    elif margen_pct is not None:
        _log(f"[{slug}] N={n} margen={margen_pct*100:.2f}% (no accionable)")
    else:
        _log(f"[{slug}] N={n} incompleto ({n_con_ask}/{n} legs con ask) -- no evaluable")


def main() -> None:
    _log(f"negrisk_arb_scanner_fase0 arrancado (N_MIN={N_MIN}, N_MAX={N_MAX}, solo lectura)")
    eventos = _eventos_negrisk()
    _log(f"{len(eventos)} eventos NegRisk activos (todos los tamaños)")
    en_rango = [e for e in eventos if N_MIN <= len(e.get("markets", [])) <= N_MAX]
    _log(f"{len(en_rango)} dentro del rango N∈[{N_MIN},{N_MAX}] evaluable con coste razonable")
    for e in en_rango:
        try:
            escanear_evento(e)
        except Exception as ex:
            _log(f"error escaneando {e.get('slug')}: {type(ex).__name__}: {ex}")
        time.sleep(0.3)  # no golpear gamma-api/CLOB de golpe


if __name__ == "__main__":
    main()
