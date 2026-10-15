"""EXPLORACIÓN (no validación) de LOWLOW-PAIR en BTC 5m con el registro ms (q = top por recepción, t = operaciones).
Variantes, 1 € por lado y mercado, desenlace oficial, sueltas contadas íntegras:
  BASE      tomador: primer instante con ask(s) <= 0,10 en cada lado, compra al ask de ese instante (sin latencia: cota)
  PRIMERA   tomador: solo la PRIMERA pata (longshot puro)
  MAKER_b   bid a b en ambos lados desde la apertura; relleno solo si una operación del token imprime a precio < b
  FILTRO15  BASE restringida a entradas con bid15(s) − ask5(s) >= 0,05 (solo 5m que cierran con un 15m)
Uso: nice -n 19 python3 analisis_lowlow_pair_exploratorio_15oct.py DIA   (15-Oct: 10-14 Oct todas negativas, ver informe del encargo)
"""
import bisect
import collections
import gzip
import sys
from datetime import datetime

sys.path.insert(0, "/root/polymarket-research")
from archivo_volumen import VOL  # noqa: E402
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402

dia = sys.argv[1]
B_MAKER = (0.03, 0.05, 0.07)


def leer_m5():
    """STREAMING: por token 5m BTC, primer instante (recepción) con ask <= 0,10 dentro de su ventana, y primera operación
    a precio < b para cada b de MAKER. Nada más en memoria."""
    from array import array  # noqa: F401
    meta, toque, maker = {}, {}, {b: {} for b in B_MAKER}
    with gzip.open(VOL / "m5_registro" / f"m5_registro_{dia}.csv.gz", "rt", errors="replace") as fh:
        try:
            for ln in fh:
                tp = ln[:2]
                if tp == "k,":
                    c = ln.rstrip("\n").split(",")
                    if len(c) >= 8 and c[3] == "BTC" and c[4] == "5min":
                        meta[c[2]] = (c[5], int(datetime.fromisoformat(c[6]).timestamp()), c[7])
                    continue
                if tp not in ("q,", "t,"):
                    continue
                c = ln.rstrip("\n").split(",")
                m = meta.get(c[2])
                if not m:
                    continue
                try:
                    if tp == "q,":
                        tr = int(c[7])
                        if c[4] in ("", "None") or not ((m[1] - 300) * 1000 <= tr <= m[1] * 1000):
                            continue
                        a = float(c[4])
                        if 0 < a <= 0.10 and (c[2] not in toque or tr < toque[c[2]][0]):
                            toque[c[2]] = (tr, a)
                    else:
                        tr, pr = int(c[6]), float(c[3])
                        if not ((m[1] - 300) * 1000 <= tr <= m[1] * 1000):
                            continue
                        for b in B_MAKER:
                            if pr < b - 1e-9 and (c[2] not in maker[b] or tr < maker[b][c[2]]):
                                maker[b][c[2]] = tr
                except (ValueError, IndexError):
                    continue
        except EOFError:
            pass
    return meta, toque, maker


def leer_m15():
    """Serie compacta (hora, bid) por token 15m BTC: arrays, ordenadas por hora."""
    from array import array
    meta, ser = {}, {}
    with gzip.open(VOL / "m15_registro" / f"m15_registro_{dia}.csv.gz", "rt", errors="replace") as fh:
        try:
            for ln in fh:
                tp = ln[:2]
                if tp == "k,":
                    c = ln.rstrip("\n").split(",")
                    if len(c) >= 8 and c[3] == "BTC" and c[4] == "15min":
                        meta[c[2]] = (c[5], int(datetime.fromisoformat(c[6]).timestamp()), c[7])
                    continue
                if tp != "q,":
                    continue
                c = ln.rstrip("\n").split(",")
                if c[2] not in meta or c[3] in ("", "None"):
                    continue
                try:
                    tr, b = int(c[7]), float(c[3])
                except (ValueError, IndexError):
                    continue
                t_, b_ = ser.setdefault(c[2], (array("q"), array("d")))
                t_.append(tr)
                b_.append(b)
        except EOFError:
            pass
    for tk, (t_, b_) in ser.items():
        o = sorted(range(len(t_)), key=t_.__getitem__)
        ser[tk] = (array("q", (t_[i] for i in o)), array("d", (b_[i] for i in o)))
    return meta, ser


m5, toque5, maker5 = leer_m5()
m15, q15 = leer_m15()
q15_por = {(cie, lado): tk for tk, (mkt, cie, lado) in m15.items() if cie % 900 == 0}
mercados = collections.defaultdict(dict)                       # mkt -> lado -> (tk, cierre)
for tk, (mkt, cie, lado) in m5.items():
    mercados[mkt][lado] = (tk, cie)
des = desenlaces(set(mercados))
res = collections.defaultdict(lambda: {"merc": 0, "pnl": 0.0, "pares": 0, "sueltas": 0, "compras": 0})


def gana(mkt, lado, p):
    return (1.0 / p - 1.0) if des[mkt] == lado else -1.0


def bid15_en(cie, lado, tms):
    tk = q15_por.get((cie, lado))
    if not tk or tk not in q15:
        return None
    t_, b_ = q15[tk]
    i = bisect.bisect_right(t_, tms) - 1
    return b_[i] if i >= 0 else None


for mkt, lados in mercados.items():
    if mkt not in des or des[mkt] not in ("YES", "NO") or len(lados) != 2:
        continue
    cie = next(iter(lados.values()))[1]
    t_ini, t_fin = (cie - 300) * 1000, cie * 1000
    # BASE / PRIMERA / FILTRO15: primer toque por lado
    toques = {lado: toque5[tk] for lado, (tk, _c) in lados.items() if tk in toque5}
    if toques:
        for var in ("BASE", "PRIMERA"):
            r = res[var]
            r["merc"] += 1
            usados = sorted(toques.items(), key=lambda x: x[1][0])
            if var == "PRIMERA":
                usados = usados[:1]
            for lado, (tr, a) in usados:
                r["pnl"] += gana(mkt, lado, a)
                r["compras"] += 1
            r["pares"] += len(usados) == 2
            r["sueltas"] += len(usados) == 1
        if cie % 900 == 0:
            ok = {l: x for l, x in toques.items()
                  if (bid15_en(cie, l, x[0]) or 0) - x[1] >= 0.05}
            r = res["FILTRO15"]
            if ok:
                r["merc"] += 1
                for lado, (tr, a) in ok.items():
                    r["pnl"] += gana(mkt, lado, a)
                    r["compras"] += 1
                r["pares"] += len(ok) == 2
                r["sueltas"] += len(ok) == 1
            res["BASE_en_cierres15"]["merc"] += 1
            for lado, (tr, a) in toques.items():
                res["BASE_en_cierres15"]["pnl"] += gana(mkt, lado, a)
    # MAKER_b
    for bm in B_MAKER:
        llen = {lado: maker5[bm][tk] for lado, (tk, _c) in lados.items() if tk in maker5[bm]}
        if llen:
            r = res[f"MAKER_{bm}"]
            r["merc"] += 1
            for lado in llen:
                r["pnl"] += gana(mkt, lado, bm)
                r["compras"] += 1
            r["pares"] += len(llen) == 2
            r["sueltas"] += len(llen) == 1

print(f"== {dia} (BTC 5m, {sum(1 for m in mercados if m in des)} mercados con desenlace)")
for k in ("BASE", "PRIMERA", "MAKER_0.03", "MAKER_0.05", "MAKER_0.07", "BASE_en_cierres15", "FILTRO15"):
    r = res[k]
    m = r["merc"] or 1
    print(f"  {k:18s} merc {r['merc']:4d} compras {r['compras']:4d} pares {r['pares']:3d} sueltas {r['sueltas']:4d} "
          f"PnL {r['pnl']:+8.1f} € ({r['pnl'] / m:+.3f}/merc)")
