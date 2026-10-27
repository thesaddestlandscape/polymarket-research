#!/usr/bin/env python3
"""ciclo_vida_W.py -- dado un fill de la wallet W (pspspsps5) reconstruye la VIDA DEL NIVEL (token, lado bid, precio) a
partir del feed crudo `libro5` (libro_estado_ws._Libro5: filas B/d/T/G con hora de exchange y de RECEPCION en ms).
Solo lectura; sin red ni ordenes. nice/ionice los pone quien lo llama.
Uso:  nice -n 19 ionice -c3 python3 -I ciclo_vida_W.py --dia 2026-10-22 [--tx 0x..|--order-hash 0x..|--n 5 --seed 1]
                                                      [--ventana-ant 120] [--ventana-post 20]
Alineacion: clave = (token, precio, tamano, bloque) -> fila T (last_trade_price) con mismo token/precio y
|recepcion - ts_est| <= TOL_S (por defecto 6 s: bloque ~2,4 s tras el casado + hora estimada +-2,4 s). Se prueba
tambien el token gemelo (precio 1-p, el CLOB publica cada casado en ambos tokens).
Limites (honestos): el feed es AGREGADO por nivel (tamano absoluto del nivel), no por orden: no hay id de orden en el
WS (el `hash` del price_change es de 40 hex, no el order_hash EIP-712 de 66). Una orden de W solo se ve como un salto
+acc del nivel (alta) y una bajada -acc (cancelacion si no hay T; relleno si hay T). Con otros makers en el mismo nivel
la atribucion es ambigua y se marca como tal (ALTA_EXACTA / ALTA_AMBIGUA / SIN_ALTA_VISIBLE).
"""
import argparse, bisect, csv, gzip, os, random, subprocess, sys, json
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, "/root/polymarket-research")
LIBRO5 = Path(os.environ.get("LIBRO5_DIR", "/mnt/HC_Volume_106538179/libro5_ms"))
WDIR = Path(os.environ.get("W_DIR", "/root/polymarket-research-datalogs/wallet_pspspsps5"))
TOL_S = 6.0   # el bloque llega ~2,4 s DESPUES del casado: T esperado en [-6 s, +0,5 s] respecto a ts_est (medido 22-Oct)
EPS_TAM = 0.011   # tolerancia en acciones al comparar tamanos (el feed redondea a 2 decimales)


def _hms(ms):
    return datetime.fromtimestamp(ms / 1000, timezone.utc).strftime("%H:%M:%S.%f")[:-3]


def indice_ficheros():
    """[(ruta, t_ini_ms, t_fin_ms)] con t_ini = recepcion de la 1a fila de datos y t_fin = mtime."""
    out = []
    for f in sorted(LIBRO5.glob("libro5_bajos_*.csv.gz")):     # extracto diario (extraer_libro5_bajos.sh): cubre el dia UTC entero
        d0 = datetime.strptime(f.name[13:23], "%Y-%m-%d").replace(tzinfo=timezone.utc).timestamp() * 1000
        out.append((f, int(d0) + 60000, int(d0) + 86400000 + 5000))
    for f in sorted(LIBRO5.glob("libro5_ms_*.csv.gz")):
        try:
            with gzip.open(f, "rt") as fh:
                next(fh)
                t0 = None
                for ln in fh:
                    p = ln.split(",")
                    if len(p) >= 8 and p[0] in "Bd T".replace(" ", ""):
                        t0 = int(p[6]); break
                    if len(p) >= 8 and p[0] == "G" and p[6].isdigit():
                        t0 = int(p[6]); break
        except Exception:
            continue
        if t0 is not None:
            out.append((f, t0, int(f.stat().st_mtime * 1000) + 5000))
    return out


def filas_token(fichero, tokens, ventanas=None):
    """Filas de los tokens (grep -F -f, Aho-Corasick en C) + las G globales (token '*'), en orden de seq, FILTRADAS en
    streaming a lo que hace falta (memoria acotada: un token caliente tiene millones de filas d):
      ventanas = {token: (lo_ms, hi_ms, {precios})} -> d solo bids de esos precios, B recortado a esos niveles, T y G
      dentro de [lo, hi] por RECEPCION. Sin ventanas devuelve todo (solo para trozos pequenos)."""
    import tempfile
    with tempfile.NamedTemporaryFile("w", suffix=".pat", delete=False) as pf:
        pf.write("\n".join(list(tokens) + [",*,"]) + "\n")
    cmd = "zcat '{}' | grep -a -F -f '{}'".format(fichero, pf.name)
    proc = subprocess.Popen(["bash", "-c", cmd], stdout=subprocess.PIPE, text=True)
    rows = []
    for ln in proc.stdout:
        p = ln.rstrip("\n").split(",")
        if len(p) < 8:
            continue
        if ventanas is not None:
            tk = p[2]
            w = ventanas.get(tk)
            rec = int(p[6]) if p[6].isdigit() else 0
            if p[0] == "G":
                if w is None and tk != "*":
                    continue
                lo_, hi_ = (w[0], w[1]) if w else (min(v[0] for v in ventanas.values()), max(v[1] for v in ventanas.values()))
                if not (lo_ - 600000 <= rec <= hi_):
                    continue
            elif w is None or not (w[0] <= rec <= w[1]):
                continue
            elif p[0] == "d":
                if p[3] != "B" or round(float(p[4]), 4) not in w[2]:
                    continue
            elif p[0] == "B":
                p[3] = ";".join(kv for kv in p[3].split(";") if kv and round(float(kv.split(":")[0]), 4) in w[2])
                p[4] = ""
        rows.append(p)
    proc.wait()
    os.unlink(pf.name)
    return rows


def tokens_de(dia):
    from analisis_5m_barato_quien_gana import mapas
    inv = {}
    for tok, (act, mkt, cierre, lado) in mapas(dia)["5min"].items():
        inv[(int(mkt), lado)] = tok
    return inv


def reconstruir(rows, token, gemelo, precio, t_fill_ms, ant_s, post_s):
    """Estado del nivel (token,'B',precio) fila a fila (orden de seq). Devuelve (serie, trades, huecos).
    serie = [(recv_ms, exch_ms, tam_nuevo, origen)]; trades = [(recv_ms, exch_ms, precio, lado, tam, token)]."""
    serie, trades, huecos = [], [], []
    reconstruir.xs = []
    nivel = None  # tamano actual del nivel o None si sin continuidad
    lo, hi = t_fill_ms - ant_s * 1000, t_fill_ms + post_s * 1000
    for p in rows:
        tipo, t_ms, tok = p[0], int(p[1]) if p[1].lstrip("-").isdigit() else 0, p[2]
        rec = int(p[6]) if p[6].isdigit() else t_ms
        if tipo == "G":
            if lo - 600000 <= rec <= hi and tok in ("*", token, gemelo):
                huecos.append((rec, tok[:6], p[3]))
            if tok in ("*", token):
                nivel = None
            continue
        if tok == token and tipo == "B":
            d = {}
            for kv in p[3].split(";"):
                if ":" in kv:
                    a, b = kv.split(":"); d[a] = float(b)
            nivel = d.get(f"{precio:g}", 0.0)
            if lo <= rec <= hi:
                serie.append((rec, t_ms, nivel, "B"))
        elif tok == token and tipo == "d" and p[3] == "B" and abs(float(p[4]) - precio) < 1e-9:
            nivel = float(p[5])
            if lo <= rec <= hi:
                serie.append((rec, t_ms, nivel, "d"))
        elif tipo == "X" and tok in (token, gemelo):
            reconstruir.xs.append((t_ms, tok, p[3].lower()))
        elif tipo == "T" and tok in (token, gemelo) and lo <= rec <= hi:
            trades.append((rec, t_ms, float(p[3]), p[4], float(p[5]), tok))
    return serie, trades, huecos


def elegir_T(trades, xs, fill_tx, p, tok, t_fill):
    """Devuelve (lista de T candidatos [(off_ms, rec, ex, tam, mismo_token)], modo). Con fila X (tx del casado, desde que
    el parche libro5-tx este desplegado) la alineacion es EXACTA: los T del token con el mismo t_ex que el X de ese tx.
    Sin X: ventana [-6 s, +0,5 s] sobre el mismo precio (ambigua si hay varios)."""
    objetivo = {(t_ms, tk) for t_ms, tk, tx in xs if tx == (fill_tx or "").lower()}
    m = []
    if objetivo:
        for rec, ex, pr, lado, tam, tk in trades:
            if (ex, tk) in objetivo:
                m.append((rec - t_fill, rec, ex, tam, tk == tok))
        if m:
            return m, "TX"
    for rec, ex, pr, lado, tam, tk in trades:
        pn = pr if tk == tok else round(1 - pr, 4)
        if abs(pn - p) < 1e-6 and -TOL_S * 1000 <= rec - t_fill <= 500:
            m.append((rec - t_fill, rec, ex, tam, tk == tok))
    return m, "VENTANA"


def vida(fill, inv, idx, ant_s, post_s, cache, verbose=True):
    d = fill["dia"]
    tok = inv.get((int(fill["mkt"]), fill["lado"]))
    if tok is None:
        return {"error": "token_no_encontrado"}
    otro = "NO" if fill["lado"] == "YES" else "YES"
    gem = inv.get((int(fill["mkt"]), otro))
    t_fill = int(float(fill["ts_est"]) * 1000)
    p, acc = round(float(fill["p"]), 4), float(fill["acc"])
    comp = int(fill["side"]) == 0
    cand = [f for f, a, b in idx if a - 60000 <= t_fill <= b]
    if not cand:
        return {"error": "sin_fichero_libro5_para_esa_hora"}
    rows = []
    for f in cand:
        rows = [r for r in cache.get(f, []) if r[0] == "G" or r[2] in (tok, gem)]
        if any(r[0] != "G" for r in rows):
            break
    # W compra (side 0) -> su orden era un BID en el token; si vende, un ASK (no tratado: aviso)
    if not comp:
        return {"error": "fill_de_venta_no_soportado"}
    serie, trades, huecos = reconstruir(rows, tok, gem, p, t_fill, ant_s, post_s)
    # alineacion con T: mismo token+precio (o gemelo a 1-p), tolerancia TOL_S
    m, modo_al = elegir_T(trades, reconstruir.xs, fill["tx"], p, tok, t_fill)
    # saltos del nivel
    ev = []
    prev = None
    for rec, ex, tam, orig in serie:
        if prev is not None and abs(tam - prev) > 1e-9:
            ev.append((rec, ex, tam - prev, tam))
        prev = tam
    altas = [e for e in ev if e[2] > 0]
    bajas = [e for e in ev if e[2] < 0]
    # alta cuyo tamano == acc (orden completa de W) antes del fill
    t_ref = (m[0][1] if m else t_fill)
    alta_exacta = [e for e in altas if abs(e[2] - acc) <= EPS_TAM and e[0] <= t_ref]
    ref_ex = min(ev, key=lambda e: abs(e[0] - t_ref)) if ev else None
    clase = "ALTA_EXACTA" if alta_exacta else ("ALTA_AMBIGUA" if altas else "SIN_ALTA_VISIBLE")
    # bajas sin T cercano (+-1 s) = cancelaciones agregadas
    def hay_T(r):
        return any(abs(r - tr[0]) <= 1000 for tr in trades if abs((tr[2] if tr[5] == tok else 1 - tr[2]) - p) < 1e-6)
    canc = [e for e in bajas if not hay_T(e[0])]
    def altas_exactas(ser, tam, hasta):
        pv, out_ = None, []
        for rec_, ex_, t_, o_ in ser:
            if pv is not None and abs((t_ - pv) - tam) <= EPS_TAM and (t_ - pv) > 0 and rec_ <= hasta:
                out_.append(rec_)
            pv = t_
        return out_
    # PLACEBOS de la prueba "alta de tamano == acc": (a) tamano x1,37 en el mismo nivel; (b) nivel p+0,01 con acc
    pl_tam = len(altas_exactas(serie, round(acc * 1.37, 2), t_ref)) > 0
    s2, _, _ = reconstruir(rows, tok, gem, round(p + 0.01, 4), t_fill, ant_s, post_s)
    pl_niv = len(altas_exactas(s2, acc, t_ref)) > 0
    # tamano de la bajada coincidente con el T (relleno visible): bajada del nivel >= 0.9*acc dentro de +-300 ms del T
    caida_T = None
    if m:
        for rec_, ex_, dl_, tam_ in ev:
            if dl_ < 0 and abs(rec_ - m[0][1]) <= 300 and abs(-dl_ - acc) <= max(EPS_TAM, 0.02 * acc):
                caida_T = round(-dl_, 3); break
    res = {"tx": fill["tx"], "token": tok[:10] + "..", "p": p, "acc": acc, "t_fill": _hms(t_fill), "mkt": fill["mkt"],
           "act": fill["act"], "T_s": float(fill["T"]), "n_eventos_nivel": len(serie), "T_matches": len(m),
           "clase_alta": clase, "n_altas": len(altas), "n_bajas": len(bajas), "n_bajas_sin_T": len(canc),
           "huecos": len(huecos), "placebo_tam": pl_tam, "placebo_nivel": pl_niv, "caida_T_igual_acc": caida_T,
           "T_unico": len(m) == 1, "alineacion": modo_al}
    if alta_exacta:
        a = alta_exacta[-1]
        res["reposo_s"] = round((t_ref - a[0]) / 1000, 3)
        res["alta_hora"] = _hms(a[0])
    if m:
        res["T_offset_ms"] = m[0][0]
        res["T_tam"] = m[0][3]
    if verbose:
        print(f"\n=== fill {fill['tx'][:12]} {fill['act']} mkt {fill['mkt']} {fill['lado']} p={p} acc={acc} "
              f"bloque~{_hms(t_fill)} T-al-cierre={float(fill['T']):.0f}s  [{clase}]")
        print(f"    huecos G en ventana: {huecos if huecos else 'ninguno'}")
        print("    hora_recv     exch_ms->recv   tam_nivel  delta     clasificacion")
        prev = None
        ruido = 0
        for rec, ex, tam, orig in serie:
            if prev is None or abs(tam - prev) > 1e-9:
                dl = (tam - prev) if prev is not None else float("nan")
                cerca = -2500 <= rec - t_fill <= 6000
                if prev is not None and not cerca and abs(dl) < 0.5 * acc:
                    ruido += 1; prev = tam; continue
                tag = ""
                if prev is not None:
                    if dl > 0 and abs(dl - acc) <= EPS_TAM: tag = "ALTA ==acc (posible W)"
                    elif dl > 0: tag = "alta"
                    elif hay_T(rec): tag = "baja con T (relleno)"
                    else: tag = "baja SIN T (cancelacion)"
                print(f"    {_hms(rec)}  {rec-ex:>5}ms  {tam:>10.2f}  {dl:>9.2f}  {tag}")
            prev = tam
        print(f"    (+{ruido} eventos menores de 0,5*acc fuera de +-2,5/6 s omitidos)")
        for off, rec, ex, tam, mis in m:
            print(f"    T  {_hms(rec)}  off_vs_bloque={off:+d}ms tam={tam} {'mismo token' if mis else 'token gemelo'}")
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dia", required=True)
    ap.add_argument("--tx"); ap.add_argument("--order-hash")
    ap.add_argument("--n", type=int, default=5); ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--ventana-ant", type=float, default=120); ap.add_argument("--ventana-post", type=float, default=20)
    ap.add_argument("--min-acc", type=float, default=5.0)
    ap.add_argument("--hora-desde", default="00:00"); ap.add_argument("--hora-hasta", default="23:59")
    ap.add_argument("--pmin", type=float, default=0.0); ap.add_argument("--pmax", type=float, default=1.0)
    ap.add_argument("--lote", action="store_true", help="solo estadisticas agregadas + placebos")
    a = ap.parse_args()
    with gzip.open(WDIR / f"ordenes_{a.dia}.csv.gz", "rt") as fh:
        fills = list(csv.DictReader(fh))
    for f in fills: f["dia"] = a.dia
    if a.tx: sel = [f for f in fills if f["tx"] == a.tx]
    elif a.order_hash: sel = [f for f in fills if f["order_hash"] == a.order_hash]
    else:
        h0, h1 = a.hora_desde, a.hora_hasta
        def hh(f): return datetime.fromtimestamp(float(f["ts_est"]), timezone.utc).strftime("%H:%M")
        pool = [f for f in fills if int(f["side"]) == 0 and float(f["acc"]) >= a.min_acc and h0 <= hh(f) <= h1
                and a.pmin <= float(f["p"]) <= a.pmax]
        random.Random(a.seed).shuffle(pool); sel = pool[:a.n]
    inv = tokens_de(a.dia); idx = indice_ficheros()
    toks_por_fich = {}
    for f in sel:
        tf = int(float(f["ts_est"]) * 1000)
        pr = round(float(f["p"]), 4)
        tk = inv.get((int(f["mkt"]), f["lado"]))
        gm = inv.get((int(f["mkt"]), "NO" if f["lado"] == "YES" else "YES"))
        for fi in [x for x, lo_, hi_ in idx if lo_ - 60000 <= tf <= hi_]:
            W = toks_por_fich.setdefault(fi, {})
            for t_, ps in ((tk, {pr, round(pr + 0.01, 4)}), (gm, set())):    # el gemelo solo aporta T
                if not t_: continue
                lo_, hi_, ps0 = W.get(t_, (10**15, 0, set()))
                W[t_] = (min(lo_, tf - int(a.ventana_ant * 1000) - 8000), max(hi_, tf + int(a.ventana_post * 1000)), ps0 | ps)
    cache = {fi: filas_token(fi, sorted(W), W) for fi, W in toks_por_fich.items()}
    out = [vida(f, inv, idx, a.ventana_ant, a.ventana_post, cache, verbose=not a.lote) for f in sel]
    if a.lote:
        ok = [r for r in out if "error" not in r]
        n = len(ok)
        def fr(k): return sum(1 for r in ok if r.get(k)) / max(n, 1)
        print(f"LOTE dia={a.dia} fills={len(sel)} validos={n} errores={len(out)-n}")
        print(f"  fills con >=1 T alineado [-6s,+0,5s] mismo precio : {sum(1 for r in ok if r['T_matches']>0)}/{n}")
        print(f"  ... con EXACTAMENTE 1 T (alineacion unica sin tx)   : {sum(1 for r in ok if r['T_unico'])}/{n}")
        print(f"  ... T con tam == acc (+-2%)                          : {sum(1 for r in ok if r.get('T_tam') and abs(r['T_tam']-r['acc'])<=max(0.011,0.02*r['acc']))}/{n}")
        print(f"  clase_alta ALTA_EXACTA (alta de tam==acc en <={a.ventana_ant:.0f} s previos): {fr('clase_alta') and sum(1 for r in ok if r['clase_alta']=='ALTA_EXACTA')}/{n}")
        print(f"  PLACEBO mismo nivel, tam x1,37: {sum(1 for r in ok if r['placebo_tam'])}/{n}   PLACEBO nivel p+0,01, tam acc: {sum(1 for r in ok if r['placebo_nivel'])}/{n}")
        print(f"  caida del nivel == acc en +-300 ms del T (relleno visible): {sum(1 for r in ok if r['caida_T_igual_acc'])}/{n}")
        rep = sorted(r['reposo_s'] for r in ok if 'reposo_s' in r)
        if rep: print(f"  reposo alta->T (solo ALTA_EXACTA, n={len(rep)}): p10 {rep[len(rep)//10]} p50 {rep[len(rep)//2]} p90 {rep[(9*len(rep))//10]} s")
        offs = sorted(r['T_offset_ms'] for r in ok if r.get('T_unico') and 'T_offset_ms' in r)
        if offs: print(f"  offset T-vs-ts_est (solo alineacion unica, n={len(offs)}): p10 {offs[len(offs)//10]} p50 {offs[len(offs)//2]} p90 {offs[(9*len(offs))//10]} ms")
        print(f"  huecos G en ventana: {sum(r['huecos'] for r in ok)}")
        for r in ok: print(json.dumps(r))
    else:
        print("\nRESUMEN"); [print(json.dumps(r)) for r in out]


if __name__ == "__main__":
    main()
