#!/usr/bin/env python3
"""analisis_5m_barato_competencia.py -- MISIÓN 5m barato (Javi 14-Oct), pasos 4 y 7: ¿QUIÉN se lleva las señales que
desaparecen, CUÁNDO respecto a nuestra detección, y QUÉ precursor público había antes?
Para cada evento B1_5m del vigía (todos, re-armes incluidos; fichero de eventos de v4 o del laboratorio), sobre el
registro ms archivado (m5_registro: q/t de 5m + x Binance; m15_registro: q de 15m) y el on-chain (m5_onchain):
  - t0 = hora de RECEPCIÓN de la fila q que creó la señal (nuestra detección);
  - consumo: primera operación COMPRADORA del token 5m del lado s a precio <= p_limite con hora del EXCHANGE >= t0 - 2 s:
    dt_consumo = t_exchange - t0 (negativo = ya se estaba consumiendo cuando la vimos);
  - desaparición: primera q (recepción) con ask5 > p_limite tras t0: dt_desaparece;
  - origen de la señal: qué pata cambió en la última q antes de t0 (bid15 subió = "15m", ask5 bajó = "5m"); edades;
  - Binance (aggTrade, recepción): retorno orientado al lado en [t0-1 s, t0] y [t0-5 s, t0]; instante del PRIMER cruce de
    +1 bp orientado en los 3 s previos (precursor) -> antelación sobre t0;
  - on-chain: wallet TOMADORA del relleno que consumió (fila del tomador: taker == exchange; token, precio <= p_limite,
    bloque en [t_exchange - 1 s, t_exchange + 6 s]; la más cercana) y su recurrencia.
Clasificación de anticipación (sección 9.3 del prompt) a la latencia de llegada L (355 ms P50 hoy, 223 optimizada):
  EARLY_ENOUGH_TO_EXECUTE: precursor + L < t_consumo; PRECURSOR_OBSERVED_BUT_TOO_LATE: precursor antes del consumo pero
  precursor + L >= consumo; AFTER_WALLET_ACTION: sin precursor antes del consumo; TIMING_UNCERTAIN: sin datos.
Uso: nice -n 19 python3 analisis_5m_barato_competencia.py [--eventos DIR] [--dias D1,D2]
Salida: datalogs/m5barato_mision/competencia_eventos.csv + competencia_informe.txt
"""
import argparse
import bisect
import csv
import gzip
import statistics as st
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402
from archivo_volumen import VOL  # noqa: E402

OUT = Path("/root/polymarket-research-datalogs/m5barato_mision")
EXCH = "0xe111180000d2663c0091e4f400237545b87b996b"
ANTES_MS, DESPUES_MS = 6000, 3000
LATS = {"L355_actual": 355, "L223_optimizada": 223}


def fee(p):
    return 0.07 * p * (1 - p)


def leer_registro(f, tokens, ventanas, monedas, marco=None):
    """q y t de los tokens pedidos dentro de su ventana; x de Binance de las monedas pedidas en cualquier ventana."""
    q, t, x = defaultdict(list), defaultdict(list), defaultdict(list)
    lo_bin = min((v[0] for v in ventanas.values()), default=0)
    with gzip.open(f, "rt", errors="replace") as fh:
        try:
            for ln in fh:
                tp = ln[:2]
                if tp == "x,":
                    if not monedas:
                        continue
                    c = ln.split(",")
                    mon = c[2][:-4]
                    if mon not in monedas:
                        continue
                    try:
                        tr = int(c[7])
                    except (ValueError, IndexError):
                        continue
                    if any(a <= tr <= b for a, b in monedas[mon]):
                        x[mon].append((tr, float(c[3])))
                    continue
                if tp not in ("q,", "t,"):
                    continue
                c = ln.rstrip("\n").split(",")
                tk = c[2]
                if tk not in tokens:
                    continue
                a, b = ventanas[tk]
                try:
                    if tp == "q,":
                        tr = int(c[7])
                        if a <= tr <= b:
                            q[tk].append((tr, float(c[3]) if c[3] not in ("", "None") else None,
                                          float(c[4]) if c[4] not in ("", "None") else None, int(c[1])))
                    else:
                        te = int(c[1])
                        if a <= te <= b:
                            t[tk].append((te, float(c[3]), c[4], float(c[5]), int(c[6])))
                except (ValueError, IndexError):
                    continue
        except (EOFError, OSError):
            pass
    for d in (q, t, x):
        for k in d:
            d[k].sort(key=lambda r: r[0])
    return q, t, x


def tokens_dia(dia, marco):
    m = {}
    pref = "m5" if marco == "5min" else "m15"
    f = VOL / f"{pref}_registro" / f"{pref}_registro_{dia}.csv.gz"
    if not f.exists():
        return m, f
    with gzip.open(f, "rt", errors="replace") as fh:
        try:
            for ln in fh:
                if ln.startswith("k,"):
                    c = ln.rstrip("\n").split(",")
                    if len(c) >= 8 and c[4] == marco:
                        m[(c[5], c[7])] = c[2]
        except (EOFError, OSError):
            pass
    return m, f


def tomadores_onchain(dia, peticiones):
    """peticiones: lista (idx, token, p_lim, t_ex_s). -> idx -> wallet tomadora."""
    f = VOL / "m5_onchain" / f"m5_onchain_{dia}.csv.gz"
    if not f.exists():
        return {}
    por_tok = defaultdict(list)
    for p in peticiones:
        por_tok[p[1]].append(p)
    mejor = {}
    with gzip.open(f, "rt", errors="replace") as fh:
        r = csv.reader(fh)
        cab = next(r)
        ix = {k: i for i, k in enumerate(cab)}
        for row in r:
            try:
                tok = row[ix["token_id"]]
                if tok not in por_tok or row[ix["tipo"]] != "F" or row[ix["taker"]] != EXCH or row[ix["side"]] != "0":
                    continue
                ts = float(row[ix["ts_est"]])
                usdc, acc = float(row[ix["maker_amt"]]), float(row[ix["taker_amt"]])
                if acc <= 0:
                    continue
                pr = usdc / acc
            except (ValueError, KeyError, IndexError):
                continue
            for idx, _, plim, tex in por_tok[tok]:
                if pr <= plim + 0.011 and tex - 1.0 <= ts <= tex + 6.0:
                    d = abs(ts - (tex + 1.5))
                    if idx not in mejor or d < mejor[idx][0]:
                        mejor[idx] = (d, row[ix["maker"]].lower(), round(pr, 4), acc)
    return {k: v[1:] for k, v in mejor.items()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--eventos", default="/root/polymarket-research-datalogs/vigia_5m_barato")
    ap.add_argument("--dias", default=None)
    a = ap.parse_args()
    E = []
    for fi in sorted(Path(a.eventos).glob("eventos_*.csv")):
        E += [e for e in csv.DictReader(open(fi)) if e["regla"] == "B1_5m"]
    for e in E:
        e["dia"] = datetime.fromtimestamp(int(e["t_deteccion"]) / 1000, timezone.utc).date().isoformat()
    dias = a.dias.split(",") if a.dias else sorted({e["dia"] for e in E})
    E = [e for e in E if e["dia"] in dias]
    des = desenlaces({e["market_compra"] for e in E})
    filas = []
    for dia in dias:
        Ed = [e for e in E if e["dia"] == dia]
        if not Ed:
            continue
        m5, f5 = tokens_dia(dia, "5min")
        m15, f15 = tokens_dia(dia, "15min")
        tok5, tok15, ven5, ven15, mon = {}, {}, {}, {}, defaultdict(list)
        for i, e in enumerate(Ed):
            lado = "YES" if e["lado"] == "Up" else "NO"
            t0 = int(e["t_deteccion"])
            tk5 = m5.get((e["market_compra"], lado))
            tk15 = m15.get((e["market_otro"], lado))
            tok5[i], tok15[i] = tk5, tk15
            for tk, ven in ((tk5, ven5), (tk15, ven15)):
                if tk:
                    a0, b0 = ven.get(tk, (t0 - ANTES_MS, t0 + DESPUES_MS))
                    ven[tk] = (min(a0, t0 - ANTES_MS), max(b0, t0 + DESPUES_MS))
            mon[e["moneda"]].append((t0 - ANTES_MS, t0 + DESPUES_MS))
        q5, t5, x = leer_registro(f5, set(ven5), ven5, mon) if f5.exists() else ({}, {}, {})
        q15, _, _ = leer_registro(f15, set(ven15), ven15, {}) if f15.exists() else ({}, {}, {})
        pet = []
        for i, e in enumerate(Ed):
            t0, plim = int(e["t_deteccion"]), float(e["p_limite"])
            sgn = 1 if e["lado"] == "Up" else -1
            fila = {"event_id": e["event_id"], "dia": dia, "moneda": e["moneda"], "lado": e["lado"], "es_primero": e["es_primero"],
                    "margen_neto": e["margen_neto"], "ask0": e["ask_compra_t0"], "bid15_0": e["bid_otro_t0"], "p_limite": plim,
                    "resto_s": e["resto_s"], "clase_L215": e["L215_clase"], "tok5": bool(tok5[i]), "tok15": bool(tok15[i])}
            r = des.get(e["market_compra"])
            fila["gana"] = None if r is None else ((r == "YES") == (e["lado"] == "Up"))
            a0 = float(e["ask_compra_t0"])
            fila["ev_hip_t0"] = None if r is None else round(((1.0 if fila["gana"] else 0.0) - a0 - fee(a0)) / (a0 + fee(a0)), 4)
            Q5 = q5.get(tok5[i], [])
            T5 = t5.get(tok5[i], [])
            Q15 = q15.get(tok15[i], [])
            # consumo y desaparición
            # referencia en reloj del EXCHANGE: hora de la última q del 5m recibida en t0 (la que mostraba el ask barato)
            q_t0 = [qq for qq in Q5 if qq[0] <= t0]
            t0_ex = q_t0[-1][3] if q_t0 else t0
            fila["feed_5m_ms"] = t0 - t0_ex
            cons = next((tr for tr in T5 if tr[0] > t0_ex and tr[2] == "BUY" and tr[1] <= plim + 1e-9), None)
            fila["compras_previas_2s"] = sum(1 for tr in T5 if t0_ex - 2000 <= tr[0] <= t0_ex and tr[2] == "BUY" and tr[1] <= plim + 1e-9)
            fila["dt_consumo_ms"] = cons[0] - t0 if cons else None
            fila["dt_consumo_rx_ms"] = cons[4] - t0 if cons else None
            des_ = next((qq for qq in Q5 if qq[0] > t0 and (qq[2] is None or qq[2] > plim + 1e-9)), None)
            fila["dt_desaparece_ms"] = des_[0] - t0 if des_ else None
            # origen y edades
            prev5 = [qq for qq in Q5 if qq[0] <= t0]
            prev15 = [qq for qq in Q15 if qq[0] <= t0]
            def edad(prev, k):
                if not prev:
                    return None
                v = prev[-1][k]
                for qq in reversed(prev):
                    if qq[k] != v:
                        return t0 - nxt
                    nxt = qq[0]
                return ANTES_MS                        # sin cambio en toda la ventana: al menos ANTES_MS
            fila["edad_ask5_ms"] = edad(prev5, 2) if prev5 else None
            fila["edad_bid15_ms"] = edad(prev15, 1) if prev15 else None
            ea, eb = fila["edad_ask5_ms"], fila["edad_bid15_ms"]
            fila["origen"] = (None if ea is None or eb is None else "15m" if eb < ea else "5m" if ea < eb else "ambos")
            # bid15 tras t0 (visible solo después: diagnóstico, NO decisión)
            for L in (215, 355):
                post = [qq for qq in Q15 if qq[0] <= t0 + L]
                fila[f"dbid15_{L}"] = round(post[-1][1] - float(e["bid_otro_t0"]), 3) if post and post[-1][1] is not None else None
            # Binance
            X = x.get(e["moneda"], [])
            XT = [v[0] for v in X]
            def px(t):
                j = bisect.bisect_right(XT, t) - 1
                return X[j][1] if j >= 0 else None
            p0 = px(t0)
            for w in (1000, 5000):
                pw = px(t0 - w)
                fila[f"bin_{w // 1000}s_bps"] = round(sgn * (p0 - pw) / pw * 1e4, 3) if p0 and pw else None
            prec = None
            base = px(t0 - 3000)
            if base:
                for tr, p in X:
                    if t0 - 3000 <= tr <= t0 and sgn * (p - base) / base * 1e4 >= 1.0:
                        prec = tr
                        break
            fila["precursor_bin_ms"] = prec - t0 if prec else None
            # anticipación
            for nom, L in LATS.items():
                if cons is None:
                    cl = "NO_CONSUMIDA"
                elif prec is None:
                    cl = "AFTER_WALLET_ACTION"
                elif prec + L < cons[0]:
                    cl = "EARLY_ENOUGH_TO_EXECUTE"
                elif prec < cons[0]:
                    cl = "PRECURSOR_OBSERVED_BUT_TOO_LATE"
                else:
                    cl = "AFTER_WALLET_ACTION"
                fila[f"anticipa_{nom}"] = cl
            if cons and tok5[i]:
                pet.append((len(filas), tok5[i], plim, cons[0] / 1000))
            filas.append(fila)
        for idx, (w, pr, acc) in tomadores_onchain(dia, pet).items():
            filas[idx].update({"tomador": w, "tomador_precio": pr, "tomador_acc": round(acc, 2)})
        print(f"{dia}: {len(Ed)} eventos, consumidos {sum(1 for f in filas if f['dia'] == dia and f.get('dt_consumo_ms') is not None)}, "
              f"con tomador on-chain {sum(1 for f in filas if f['dia'] == dia and f.get('tomador'))}", flush=True)
    campos = list(dict.fromkeys(k for f in filas for k in f))
    with open(OUT / "competencia_eventos.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=campos)
        w.writeheader()
        w.writerows(filas)
    # ---------- informe ----------
    L = [f"Competencia 5m barato: {len(filas)} eventos B1_5m ({dias[0]}..{dias[-1]}), tokens 5m/15m encontrados "
         f"{sum(1 for f in filas if f['tok5'])}/{sum(1 for f in filas if f['tok15'])}"]
    def q_(v, p):
        v = sorted(v)
        return v[min(len(v) - 1, int(p * len(v)))] if v else None
    dc = [f["dt_consumo_ms"] for f in filas if f.get("dt_consumo_ms") is not None]
    dd = [f["dt_desaparece_ms"] for f in filas if f.get("dt_desaparece_ms") is not None]
    L.append(f"feed 5m (recepción - exchange de la q de t0) P50 {q_(['x' and f['feed_5m_ms'] for f in filas if f.get('feed_5m_ms') is not None], .5)} ms")
    L.append(f"consumo (1ª compra <= p_lim con hora exchange > la de la q barata; dt vs NUESTRA recepción): n={len(dc)} P10/P50/P90 {q_(dc, .1)}/{q_(dc, .5)}/{q_(dc, .9)} ms; "
             f"<0 (ya en curso al detectar) {sum(1 for v in dc if v < 0)}; <215 {sum(1 for v in dc if v < 215)}; <355 {sum(1 for v in dc if v < 355)}")
    L.append(f"desaparición del precio (recepción): n={len(dd)} P10/P50/P90 {q_(dd, .1)}/{q_(dd, .5)}/{q_(dd, .9)} ms")
    for nom in ("origen",):
        L.append(f"\nPor ORIGEN de la señal (qué pata cambió justo antes de t0):")
        for o in ("15m", "5m", "ambos", None):
            g = [f for f in filas if f["origen"] == o and f["ev_hip_t0"] is not None]
            if not g:
                continue
            cons_ = [f for f in g if f.get("dt_consumo_ms") is not None and f["dt_consumo_ms"] < 355]
            L.append(f"  {str(o):6s} n={len(g):3d} acierto {sum(1 for f in g if f['gana'])}/{len(g)} EV hip t0 "
                     f"{st.mean(f['ev_hip_t0'] for f in g):+.3f} | consumidas <355 ms {len(cons_)} | "
                     f"ejecutable L215 {sum(1 for f in g if f['clase_L215'].startswith(('A', 'D')))} "
                     f"EV de esas {st.mean([f['ev_hip_t0'] for f in g if f['clase_L215'].startswith(('A', 'D'))] or [float('nan')]):+.3f}")
    L.append("\nBinance orientado al lado en el 1 s previo:")
    for nom, cond in (("a favor >= +1 bp", lambda v: v >= 1), ("plano (-1,+1)", lambda v: -1 < v < 1), ("en contra <= -1 bp", lambda v: v <= -1)):
        g = [f for f in filas if f.get("bin_1s_bps") is not None and cond(f["bin_1s_bps"]) and f["ev_hip_t0"] is not None]
        if g:
            L.append(f"  {nom:18s} n={len(g):3d} acierto {sum(1 for f in g if f['gana'])}/{len(g)} EV hip t0 {st.mean(f['ev_hip_t0'] for f in g):+.3f} "
                     f"| consumidas <355 {sum(1 for f in g if f.get('dt_consumo_ms') is not None and f['dt_consumo_ms'] < 355)} "
                     f"| quedan a L215 {sum(1 for f in g if f['clase_L215'].startswith(('A', 'D')))} EV quedan "
                     f"{st.mean([f['ev_hip_t0'] for f in g if f['clase_L215'].startswith(('A', 'D'))] or [float('nan')]):+.3f}")
    for nom in LATS:
        L.append(f"\nAnticipación con precursor Binance (+1 bp en 3 s) a {nom}: {dict(Counter(f[f'anticipa_{nom}'] for f in filas))}")
    tom = Counter(f.get("tomador") for f in filas if f.get("tomador"))
    L.append(f"\nTomadores on-chain de las consumidas: {sum(tom.values())} emparejadas, {len(tom)} wallets; top: "
             + ", ".join(f"{w[:10]}×{n}" for w, n in tom.most_common(8)))
    txt = "\n".join(L)
    print(txt)
    (OUT / "competencia_informe.txt").write_text(txt + "\n")


if __name__ == "__main__":
    main()
