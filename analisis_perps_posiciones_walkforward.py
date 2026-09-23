#!/usr/bin/env python3
"""analisis_perps_posiciones_walkforward.py -- (23-Sep, Perps) ¿Hay edge PERSISTENTE a nivel de
POSICIÓN en las wallets rastreadas? Unidad estadística = posición cerrada (cierre observado),
no fill ni orden. Datos: perps_fills_full/ (fetch_polymarket_perps_fills_full.py) segmentados con
perps_posiciones_v2.py. Solo lectura, sin dinero.

Método (mismo espíritu que el walk-forward del 21-Sep, ahora con datos válidos):
  1. Universo: wallets con backfill completo y NO alta_frecuencia; posiciones cerradas con
     notional_abre >= MIN_NOTIONAL.
  2. Corte temporal global por fecha de cierre (TRAIN_FRAC de las posiciones más antiguas).
  3. Selección en train: wallet con n_train >= MIN_N_TRAIN, media de ret_neto > 0 y IC90
     bootstrap (por posición) > 0.
  4. Medida en test (out-of-sample): media de ret_neto de las posiciones de las wallets elegidas,
     IC90 bootstrap AGRUPADO POR WALLET (las posiciones de una wallet no son independientes),
     tasa de acierto, nº de wallets/días independientes.
  5. Placebo: p-valor por permutación = con qué frecuencia una selección ALEATORIA del mismo
     tamaño entre las wallets elegibles iguala la media test de la selección real.
Métrica ret_neto = (pnl - fees)/notional_abre, SIN funding (no disponible: limitación).
"""
import json
import random
import statistics as st
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
import perps_posiciones_v2 as P  # noqa: E402

RUTA_STATE = REPO / "data/shadow/perps_fills_full_state.json"
OUT = REPO / "data/shadow/perps_walkforward_posiciones.json"
MIN_NOTIONAL = 100.0     # USD: descarta polvo
TRAIN_FRAC = 0.6
MIN_N_TRAIN = 8
N_BOOT = 2000
N_PERM = 2000
SEED = 42


def _ic90(vals, rng):
    if len(vals) < 3:
        return None
    n = len(vals)
    medias = sorted(sum(vals[rng.randrange(n)] for _ in range(n)) / n for _ in range(N_BOOT))
    return medias[int(0.05 * N_BOOT)], medias[int(0.95 * N_BOOT)]


def _ic90_cluster(por_wallet: dict, rng):
    """Bootstrap agrupado: remuestrea WALLETS (con reemplazo), la media es de todas las
    posiciones de las wallets sorteadas."""
    ws = list(por_wallet)
    if len(ws) < 3:
        return None
    medias = []
    for _ in range(N_BOOT):
        tot, n = 0.0, 0
        for _ in ws:
            v = por_wallet[ws[rng.randrange(len(ws))]]
            tot += sum(v); n += len(v)
        medias.append(tot / n if n else 0.0)
    medias.sort()
    return medias[int(0.05 * N_BOOT)], medias[int(0.95 * N_BOOT)]


def main() -> int:
    rng = random.Random(SEED)
    estado = json.loads(RUTA_STATE.read_text()) if RUTA_STATE.exists() else {}
    validas = {a for a, r in estado.items() if r.get("back_done") and not r.get("alta_frecuencia")}
    excl_hf = sorted(a[:10] for a, r in estado.items() if r.get("alta_frecuencia"))
    pendientes = sorted(a[:10] for a, r in estado.items() if not r.get("back_done"))
    grupos = P.cargar_fills(validas)
    pos, rota_total, n_ord = [], 0, 0
    for (addr, iid), fs in grupos.items():
        ps, rota = P.segmentar(fs)
        rota_total += rota; n_ord += len(fs)
        for p in ps:
            if p["cerrada"] and p["notional_abre"] >= MIN_NOTIONAL:
                p["address"], p["iid"] = addr, iid
                pos.append(p)
    print(f"[perps_wf] wallets validas {len(validas)} | pendientes backfill {len(pendientes)} | "
          f"alta_frecuencia excluidas {len(excl_hf)}")
    print(f"[perps_wf] ordenes {n_ord} | cadena rota {rota_total} ({100*rota_total/max(1,n_ord):.2f}%) | "
          f"posiciones cerradas (>= {MIN_NOTIONAL:.0f} USD) {len(pos)}")
    if rota_total / max(1, n_ord) > 0.02:
        print("⚠️ cadena rota >2%: la segmentacion NO es fiable, no interpretar lo de abajo")
    if len(pos) < 60:
        print("n insuficiente para walk-forward (posiciones < 60) -- esperar mas backfill/datos")
        return 0

    pos.sort(key=lambda p: p["ts_cierre"])
    corte = pos[int(TRAIN_FRAC * len(pos))]["ts_cierre"]
    f = lambda t: datetime.fromtimestamp(t / 1000, timezone.utc).strftime("%Y-%m-%d")
    print(f"[perps_wf] rango {f(pos[0]['ts_cierre'])} -> {f(pos[-1]['ts_cierre'])} | corte train/test {f(corte)}")
    train, test = defaultdict(list), defaultdict(list)
    for p in pos:
        (train if p["ts_cierre"] <= corte else test)[p["address"]].append(p["ret_neto"])

    elegibles = [a for a, v in train.items() if len(v) >= MIN_N_TRAIN]
    elegidas = []
    for a in elegibles:
        v = train[a]
        if st.mean(v) > 0:
            ic = _ic90(v, rng)
            if ic and ic[0] > 0:
                elegidas.append(a)
    print(f"[perps_wf] wallets con n_train>={MIN_N_TRAIN}: {len(elegibles)} | elegidas (media>0 e IC90>0 en train): {len(elegidas)}")

    def _medida(ws):
        por_w = {a: test[a] for a in ws if test.get(a)}
        vals = [x for v in por_w.values() for x in v]
        return por_w, vals

    por_w, vals = _medida(elegidas)
    res = {"generado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
           "n_wallets_validas": len(validas), "n_posiciones": len(pos), "cadena_rota_pct": round(100 * rota_total / max(1, n_ord), 3),
           "corte": f(corte), "n_elegibles": len(elegibles), "n_elegidas": len(elegidas)}
    if vals:
        media = st.mean(vals)
        ic = _ic90_cluster(por_w, rng)
        hit = sum(1 for x in vals if x > 0) / len(vals)
        # placebo
        pool = [a for a in elegibles if test.get(a)]
        k = len([a for a in elegidas if test.get(a)])
        ge = 0
        for _ in range(N_PERM):
            m = rng.sample(pool, k) if 0 < k <= len(pool) else []
            v = [x for a in m for x in test[a]]
            if v and st.mean(v) >= media:
                ge += 1
        p_perm = (ge + 1) / (N_PERM + 1)
        dias = len({f(p["ts_cierre"]) for p in pos if p["ts_cierre"] > corte and p["address"] in por_w})
        res.update({"test_n_pos": len(vals), "test_n_wallets": len(por_w), "test_dias": dias,
                    "test_media_ret": round(media, 5), "test_hit": round(hit, 3),
                    "test_ic90_cluster": [round(x, 5) for x in ic] if ic else None,
                    "placebo_p": round(p_perm, 4),
                    "media_ret_no_elegidas_test": round(st.mean([x for a, v in test.items() if a not in elegidas for x in v]), 5)
                    if any(a not in elegidas for a in test) else None})
        print(f"[perps_wf] TEST elegidas: n_pos={len(vals)} wallets={len(por_w)} dias={dias} "
              f"ret medio={media:+.4%} hit={hit:.1%} IC90(wallet-cluster)={ic} placebo p={p_perm:.3f}")
        print(f"[perps_wf] TEST no elegidas: ret medio={res['media_ret_no_elegidas_test']}")
    else:
        print("[perps_wf] ninguna wallet elegida tiene posiciones en test")
    OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
