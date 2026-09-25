#!/usr/bin/env python3
"""analisis_perps_consenso_categoria_25sep.py -- CONSENSO de wallets expertas POR CATEGORIA en Perps
(idea Javi 25-Sep, project_perps_pendientes_25sep #5). Reutiliza el cargador/markout de
analisis_perps_markout_entradas_25sep.py (entradas independientes; seguidor a +60 s; neto de 2x0,04 %;
SIN funding). Categorias por simbolo: petroleo (OIL), oro, plata, memecoins, indices, equity, cripto mayor/alt.
Experta (wallet, categoria) = >=N_EXP entradas independientes en TRAIN con retorno neto medio>0 y t>=T_EXP
(H=SEL_H h). Señal de consenso en un instrumento = >=2 wallets expertas distintas entrando en la misma
direccion en <=VENT_MIN min sin entrada contraria de otra experta; el seguidor entra 60 s despues de la
2a. Variante 'con salidas': una reduccion/cierre de experta cuenta como voto en sentido contrario.
Walk-forward: expertas elegidas antes del corte (70 % de dias), señales despues. Reporta n, retorno neto
medio a 1/6/24 h, t por clúster (dia,categoria) y n de expertas. Con la serie DENSA (cron 10 min, desde
25-Sep) el markout mejorara; hoy usa la serie dispersa de los fills -> solo orientativo."""
import collections, sys
from datetime import datetime, timezone
import analisis_perps_markout_entradas_25sep as M

N_EXP, T_EXP, SEL_H, VENT_MIN = 15, 1.5, 6, 60
MEME = {"DOGE", "SHIB", "PEPE", "BONK", "WIF", "FLOKI", "PENGU", "TRUMP", "FARTCOIN", "PUMP", "MOG", "POPCAT", "BRETT", "TURBO", "MEME", "WLD"}
MAYOR = {"BTC", "ETH", "SOL", "XRP", "BNB", "HYPE", "ADA", "AVAX", "LINK", "LTC", "TON"}


def categorias():
    import json
    d = json.loads((M.REPO / "data/shadow/polymarket_perps_instruments.json").read_text())
    out = {}
    for x in d:
        b, c = x["base_asset"].upper(), x["category"]
        cat = ("petroleo" if "OIL" in b else "oro" if "GOLD" in b else "plata" if "SILVER" in b else
               "memecoin" if b in MEME else "cripto_mayor" if b in MAYOR else
               "indice" if c == "index" else "equity" if c == "equity" else "cripto_alt")
        out[str(x["instrument_id"])] = (cat, x["symbol"])
    return out


def main():
    cats = categorias()
    ordenes, serie = M.cargar()
    ev_ent = M.eventos(ordenes)
    ent_ids = {id(o) for o in ev_ent}
    # votos: entradas (dir = lado) y, en la variante con salidas, reducciones (dir contraria al lado que reduce)
    votos = []
    for o in ordenes:
        if o["liq"] or o["price"] <= 0:
            continue
        cat = cats.get(o["ins"], ("?", "?"))[0]
        if M.es_entrada(o):
            if id(o) in ent_ids:
                votos.append({**o, "cat": cat, "dir": 1 if o["side"] == "long" else -1, "tipo": "ent"})
        elif o["prev"] != 0:
            votos.append({**o, "cat": cat, "dir": 1 if o["side"] == "long" else -1, "tipo": "sal"})  # comprar para cerrar corto = alcista
    votos.sort(key=lambda v: v["ts"])
    dias = sorted({datetime.fromtimestamp(v["ts"] / 1000, timezone.utc).strftime("%Y-%m-%d") for v in votos})
    corte = dias[len(dias) * 7 // 10]
    print(f"votos {len(votos)} | dias {dias[0]}..{dias[-1]} corte {corte}")
    # expertas por (wallet,categoria) con train
    tr = collections.defaultdict(list)
    for o in ev_ent:
        dia = datetime.fromtimestamp(o["ts"] / 1000, timezone.utc).strftime("%Y-%m-%d")
        if dia >= corte:
            continue
        p0 = M.precio_desde(serie, o["ins"], o["ts"] + M.LAT_S * 1000, 5 * 60_000)
        ph = M.precio_desde(serie, o["ins"], o["ts"] + SEL_H * 3_600_000, M.TOL_MIN * 60_000)
        if p0 and ph:
            d = 1 if o["side"] == "long" else -1
            tr[(o["w"], cats.get(o["ins"], ("?",))[0])].append(d * (ph / p0 - 1) - 2 * M.FEE_TAKER)
    exp = {k for k, v in tr.items() if len(v) >= N_EXP and sum(v) > 0 and M._t(v) >= T_EXP}
    porcat = collections.Counter(c for _, c in exp)
    print("expertas (wallet,categoria) seleccionadas:", len(exp), dict(porcat), "| candidatas con n>=%d:" % N_EXP, sum(len(v) >= N_EXP for v in tr.values()))
    for variante in ("solo_entradas", "con_salidas"):
        sig = []
        por_ins = collections.defaultdict(list)
        for v in votos:
            if (v["w"], v["cat"]) in exp and (variante == "con_salidas" or v["tipo"] == "ent"):
                por_ins[v["ins"]].append(v)
        for ins, L in por_ins.items():
            L.sort(key=lambda v: v["ts"])
            ult = -1e18
            for i, v in enumerate(L):
                vent = [x for x in L if 0 <= v["ts"] - x["ts"] <= VENT_MIN * 60_000]
                ws = {x["w"] for x in vent if x["dir"] == v["dir"]}
                contra = {x["w"] for x in vent if x["dir"] != v["dir"]}
                if len(ws) >= 2 and not contra and v["ts"] - ult > VENT_MIN * 60_000 and v["ts"] >= int(datetime.fromisoformat(corte).replace(tzinfo=timezone.utc).timestamp() * 1000):
                    ult = v["ts"]; sig.append((ins, v["ts"], v["dir"], v["cat"]))
        print(f"\nVARIANTE {variante}: señales de consenso en TEST: {len(sig)}")
        por = collections.defaultdict(list)
        for ins, ts, d, cat in sig:
            p0 = M.precio_desde(serie, ins, ts + M.LAT_S * 1000, 5 * 60_000)
            if not p0:
                continue
            dia = datetime.fromtimestamp(ts / 1000, timezone.utc).strftime("%Y-%m-%d")
            for h in M.HORIZONTES_H:
                ph = M.precio_desde(serie, ins, ts + h * 3_600_000, M.TOL_MIN * 60_000)
                if ph:
                    por[(cat, h)].append((dia, d * (ph / p0 - 1) - 2 * M.FEE_TAKER))
        for (cat, h), L in sorted(por.items()):
            x = [r for _, r in L]
            cl = collections.defaultdict(list)
            for dia, r in L:
                cl[dia].append(r)
            print(f"  {cat:12s} H={h:2d}h n={len(x):3d} ret neto medio={sum(x)/len(x)*100:+.3f}% t_cluster(día)={M._t([sum(v)/len(v) for v in cl.values()]):+.2f}")


if __name__ == "__main__":
    sys.exit(main())
