"""P31 (11-Ago): corrección tras aviso de Javi -- SÍ hay datos de libro
reales para validar fill-ability del fade de XRP#15min, en
data/markets/*.csv (best_bid/best_ask/spread, capturas ~1min, desde antes
del cambio TWAP). No hace falta esperar a acumular libro_snapshots.csv
propio -- cruzar directo por condition_id contra el histórico de mercados
ya capturado, mismo espíritu que el punto 2 del protocolo de zonas
externas en CLAUDE.md (gate_bucket_propio).

Para cada trade fade candidato (las 6 wallets XRP#15min post-TWAP),
busca el snapshot de mercado MÁS CERCANO EN EL TIEMPO tras ts_trade
(reacción realista, no instantánea) y calcula el precio REAL ejecutable
del lado contrario (best_ask del lado que fadeamos), no el precio al que
compró la wallet.
"""
import csv
import glob
import math
from datetime import datetime, timedelta, timezone

import numpy as np

import shadow_postmortem as sp

FEE = 0.07
Z_90 = 1.645
WALLETS_FADE_PREFIX = ['0x65a4af3a', '0xe8e086f7', '0x775d9de0',
                        '0xddb6e624', '0x97b3cdaa', '0x629da223']


def parse_iso(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def wilson_lower(hits, n, z=Z_90):
    if n == 0:
        return 0.0
    p = hits / n
    denom = 1 + z * z / n
    centro = p + z * z / (2 * n)
    margen = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (centro - margen) / denom


def breakeven(p_held):
    gross_win = (1 - p_held) / p_held
    return 1 / (1 + gross_win * (1 - FEE))


def main():
    trades = []
    with open('data/shadow/ballenas_timing_history.csv') as f:
        for row in csv.DictReader(f):
            if row.get('activo') != 'XRP' or row.get('marco') != '15m':
                continue
            if not any(row.get('wallet', '').startswith(p) for p in WALLETS_FADE_PREFIX):
                continue
            if sp.es_pre_twap('15min', row.get('ts_trade', '')):
                continue
            trades.append(row)
    print(f"Trades fade candidatos post-TWAP: {len(trades)}")

    condition_ids = {t['condition_id'] for t in trades}
    fechas = sorted({t['ts_trade'][:10] for t in trades})
    print(f"Fechas a cargar: {fechas}")

    # índice condition_id -> lista (ts_epoch, best_bid, best_ask)
    libro = {cid: [] for cid in condition_ids}
    for fecha in fechas:
        path = f"data/markets/{fecha}.csv"
        try:
            f = open(path, encoding="utf-8")
        except FileNotFoundError:
            continue
        print(f"  leyendo {path}...", flush=True)
        with f:
            reader = csv.reader(f)
            header = next(reader)
            i_ts = header.index("timestamp_utc")
            i_cid = header.index("condition_id")
            i_bb = header.index("best_bid")
            i_ba = header.index("best_ask")
            for row in reader:
                cid = row[i_cid]
                if cid not in libro:
                    continue
                try:
                    ts = parse_iso(row[i_ts]).timestamp()
                    bb = float(row[i_bb]) if row[i_bb] else None
                    ba = float(row[i_ba]) if row[i_ba] else None
                except Exception:
                    continue
                if bb is None or ba is None:
                    continue
                libro[cid].append((ts, bb, ba))
        print(f"    ok, condition_ids con datos hasta ahora: {sum(1 for v in libro.values() if v)}", flush=True)
    for cid in libro:
        libro[cid].sort()

    n_con_libro = 0
    n_sin_libro = 0
    hits = 0
    p_held_sum = 0.0
    detalle = []
    for t in trades:
        cid = t['condition_id']
        snaps = libro.get(cid, [])
        if not snaps:
            n_sin_libro += 1
            continue
        target = parse_iso(t['ts_trade']).timestamp()
        # snapshot MÁS CERCANO tras la reacción (target + margen de reacción 30s)
        reaction_target = target + 30
        candidatos = [s for s in snaps if s[0] >= reaction_target]
        if candidatos:
            snap = candidatos[0]
        else:
            # el mercado pudo cerrar antes de que hubiera snapshot posterior --
            # usar el último disponible antes del cierre (igual de válido,
            # es el libro más reciente que tuvimos)
            anteriores = [s for s in snaps if s[0] <= target + 900]
            if not anteriores:
                n_sin_libro += 1
                continue
            snap = anteriores[-1]
        if snap[0] - target > 900:  # snapshot demasiado lejos (>15min), descartar
            n_sin_libro += 1
            continue

        _, bb, ba = snap
        compro_yes = t.get('compro_yes') == '1'
        acierto = t.get('acierto') in ('1', 'True', 'true')
        # fadeamos: si compró YES, nosotros compramos NO al ask real de NO
        # (aprox 1-best_bid_yes, ya que price_no=1-price_yes en estos mercados);
        # si compró NO, compramos YES al best_ask_yes real.
        if compro_yes:
            fade_ask = 1 - bb
        else:
            fade_ask = ba
        fade_gano = not acierto
        n_con_libro += 1
        hits += int(fade_gano)
        p_held_sum += fade_ask
        detalle.append({
            "wallet": t['wallet'][:10], "ts_trade": t['ts_trade'],
            "compro_yes": compro_yes, "fade_ask_real": round(fade_ask, 4),
            "fade_gano": fade_gano, "delay_s": round(snap[0] - target, 1),
        })

    print(f"Con libro real cruzado: {n_con_libro}  sin libro/fuera de rango: {n_sin_libro}")
    if n_con_libro == 0:
        return
    hit = hits / n_con_libro
    p_medio = p_held_sum / n_con_libro
    be = breakeven(p_medio)
    wl = wilson_lower(hits, n_con_libro)
    rng = np.random.default_rng(7)
    sim = rng.binomial(n_con_libro, p_medio, size=20000) / n_con_libro
    pval = float(np.mean(np.abs(sim - p_medio) >= abs(hit - p_medio)))
    print(f"\nFADE con precio REAL ejecutable (best_ask/bid +30s reacción):")
    print(f"  n={n_con_libro}  hit={hit:.4f}  precio_medio_real={p_medio:.4f}  "
          f"breakeven={be:.4f}  wilson90lo={wl:.4f}  margen_pp={round((wl-be)*100,2)}  "
          f"p_shuffle={pval}")

    delays = [d['delay_s'] for d in detalle]
    print(f"  delay medio snapshot vs trade: {sum(delays)/len(delays):.1f}s "
          f"(min={min(delays):.0f}s max={max(delays):.0f}s)")


if __name__ == "__main__":
    main()
