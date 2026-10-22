#!/usr/bin/env python3
"""h61b_sim.py -- brazo C (H61b, regla CONGELADA en h61b_regla.py) EMPAREJADO con v3 (r150, h23_regla_v3 3eeff503cf0a75c9) en los MISMOS cierres. OFFLINE, solo lectura, dry-run.
Por (moneda, dia): reutiliza sin copiar las piezas de ../h23_sim_v3.py (segmentos, llenar, querible, kmap, lados) y de simlib (grupos, DES). Para cada cierre del par anidado y brazo A/B:
  v3     = r150 sin defensa (instantes = libro 5m/15m)                  -> validacion: debe coincidir con v3_<coin>_<D>.csv oficial (cola/latencia/real/primer)
  C_reg  = v3 + defensa Binance con el aggTrade del registro ms (x_D)  (la fuente del replay H61)         [solo BTC: el registro solo se extrajo para BTC]
  C_live = v3 + defensa Binance con el aggTrade COMPLETO de multivenue_ms binance_spot (fetch propio)      [cualquier moneda MON6]
La defensa solo ENMASCARA el precio objetivo (want -> None) en los instantes con ret < -0,5 bps; lo demas es identico a v3 (mismo tamano real, universo ejecutable, 1 relleno cierra).
Celdas: cola {opt,base,cons} x (alta,cancel) {(79,60),(254,150)} a mult=1 modo primer; y en la celda central mult {1,2,5,10,20} x modo {primer,acum} (capacidad: tamano multiplo del real).
Salida (atomica, idempotente): DL/h61b/rows_<COIN>_<D>.csv.gz + cobertura_<COIN>_<D>.json + feed_live_<COIN>_<D>.npz. Uso: nice -n 19 ionice -c3 python3 -I h61b_sim.py D [COIN] [--force] (ulimit -v 2500000)"""
import csv, gzip, hashlib, json, os, sys, tempfile, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.dirname(HERE))
import numpy as np
import h23_sim_v3 as V3
import h61b_regla as RG
import h61b_feeds as FD
from h23_sim_v3 import R, simlib, segmentos, llenar, querible, CFG

DL = "/root/polymarket-research-datalogs/h61b/"
ALTS_IN = "/mnt/HC_Volume_106538179/datalogs_analisis_caches/h23_v2/alts/"
BTC_IN = "/mnt/HC_Volume_106538179/datalogs_analisis_caches/v4_comprar_lo_bueno/"
MULTS = (1, 2, 5, 10, 20)
CELDAS = [(c, lp, lc) for c in ("opt", "base", "cons") for lp, lc in ((79, 60), (254, 150))]
CENTRAL = ("base", 79, 60)
COLS = ["dia", "coin", "cierre", "lado", "m5", "brazo", "var", "modo", "mult", "cola", "lp", "lc", "n_seg", "precio", "prof_join", "need", "lleno", "coste", "n_fill", "t_rel", "p_rel",
        "gana", "rebate", "frac_bloq"]
CLAVE = ("dia", "coin", "cierre", "brazo", "var", "modo", "mult", "cola", "lp", "lc")


def sha_fichero(f, n=None):
    try:
        h = hashlib.sha256()
        with open(f, "rb") as fh:
            h.update(fh.read(n) if n else fh.read())
        return h.hexdigest()[:16]
    except OSError:
        return None


def celdas_para(var_es_central_only=False):
    """Lista (cola, lp, lc, mult, modo) a simular."""
    out = [(c, lp, lc, 1, "primer") for c, lp, lc in CELDAS]
    out += [(CENTRAL[0], CENTRAL[1], CENTRAL[2], m, md) for m in MULTS for md in ("primer", "acum") if not (m == 1 and md == "primer")]
    return out


def simular_variante(inst, want, bsz, tpm, t_fin, FIL, FE, C_row_base, var, brazo, frac_bloq, escribir):
    segs = segmentos(inst, want, bsz, RG.REPUJA_MS, tpm)
    if not segs:
        return False
    need1 = R.acciones_real(segs[0][0])
    for cola, lp, lc, mult, modo in celdas_para():
        need = need1 * mult
        lleno, coste, t_rel, p_rel, nfill = llenar(segs, need, CFG["colas"][cola], lp, lc, FIL, FE, t_fin, modo == "primer")
        reb = round(CFG["rebate"] * R.fee(coste / lleno) * lleno, 6) if lleno > 0 else 0.0
        escribir(dict(C_row_base, brazo=brazo, var=var, modo=modo, mult=mult, cola=cola, lp=lp, lc=lc, n_seg=len(segs), precio=segs[0][0], prof_join=round(segs[0][1], 2),
                      need=round(need, 2), lleno=round(lleno, 4), coste=round(coste, 6), n_fill=nfill, t_rel=t_rel if t_rel is not None else "", p_rel=p_rel if p_rel is not None else "",
                      rebate=reb, frac_bloq=round(frac_bloq, 4)))
    return True


def correr(D, coin="BTC", out_dir=DL, feeds=None, forzar=False, simular_in=None, brazos=None, prefijo="rows"):
    RG.verificar_congelada()
    BRAZ = brazos or CFG["brazos"]
    os.makedirs(out_dir, exist_ok=True)
    fo = os.path.join(out_dir, f"{prefijo}_{coin}_{D}.csv.gz")
    if os.path.exists(fo) and not forzar and validar_salida(fo):
        print(coin, D, "ya hecho y valido"); return json.load(open(os.path.join(out_dir, f"cobertura_{coin}_{D}.json" if prefijo == "rows" else f"cobertura_{prefijo}_{coin}_{D}.json")))
    IN = simular_in or (BTC_IN if coin == "BTC" else ALTS_IN)
    key = D if coin == "BTC" else f"{coin}_{D}"
    V3.IN = IN; simlib.O = IN
    km, LS = V3.kmap(key, coin), V3.lados(D, coin)
    FEEDS = {}
    if coin == "BTC" and (feeds is None or "reg" in feeds):
        FEEDS["C_reg"] = FD.cargar_reg(D)
    if feeds is None or "live" in feeds:
        FEEDS["C_live"] = FD.cargar_live(D, coin)
        if FEEDS["C_live"] is not None:
            np.savez_compressed(os.path.join(out_dir, f"feed_live_{coin}_{D}.npz.tmp.npz"), rx=FEEDS["C_live"][0], p=FEEDS["C_live"][1])
            os.replace(os.path.join(out_dir, f"feed_live_{coin}_{D}.npz.tmp.npz"), os.path.join(out_dir, f"feed_live_{coin}_{D}.npz"))
    FEEDS = {k: v for k, v in FEEDS.items() if v is not None}
    COB = dict(coin=coin, dia=D, feeds={k: len(v[0]) for k, v in FEEDS.items()}, cierres_grupo=0, con_lado=0, con_libro=0, sin_desenlace=0, errores=0, cotizados=0, v3_vs_superset_dif=0,
               fuente_rows=f"{IN}rows_{key}.csv.gz", sha_k=sha_fichero(IN + f"k_{key}.csv"), t0=time.time())
    ROWS = []; esc = ROWS.append
    for C, QS, TS in simlib.grupos(key):
        COB["cierres_grupo"] += 1
        try:
            if C not in LS: continue
            COB["con_lado"] += 1
            lado, m5id = LS[C]
            sl = "YES" if lado == "Up" else "NO"; ol = "NO" if sl == "YES" else "YES"
            k5, k15, k5o = km.get(("5min", C, sl)), km.get(("15min", C, sl)), km.get(("5min", C, ol))
            if not k5 or not k15 or k5[1] != m5id: continue
            q5, q15 = QS.get(k5[0]), QS.get(k15[0])
            if q5 is None or q15 is None or not len(q5.rx) or not len(q15.rx): continue
            COB["con_libro"] += 1
            out = simlib.DES.get(m5id); gana = None if out is None else (out == sl)
            if gana is None: COB["sin_desenlace"] += 1
            t_ini, t_fin = (C - 300) * 1000 + CFG["ref_conocible_ms"], (C - CFG["fin_margen_s"]) * 1000
            tpm = (C - CFG["t_min_ejec_s"]) * 1000
            ib = np.unique(np.concatenate([q5.rx, q15.rx])); ib = ib[(ib >= t_ini) & (ib < t_fin)]
            if not len(ib): continue
            FIL = []
            t5, t5o = TS.get(k5[0]), (TS.get(k5o[0]) if k5o else None)
            for tk, side_s in ((t5, True), (t5o, False)):
                if tk is None or not len(tk.rx): continue
                sel = (~tk.buy) if side_s else tk.buy
                pr = tk.p[sel] if side_s else np.round(1 - tk.p[sel], 4)
                for rx_, p_, sz_ in zip(tk.rx[sel], pr, tk.sz[sel]): FIL.append((int(rx_), float(p_), float(sz_)))
            FIL.sort(); FE = np.array([f[0] for f in FIL], dtype=np.int64)
            base = dict(dia=D, coin=coin, cierre=C, lado=lado, m5=m5id, gana="" if gana is None else int(gana))
            def preparar(inst):
                i5, i15 = q5.i(inst), q15.i(inst); ok = (i5 >= 0) & (i15 >= 0)
                inst, i5, i15 = inst[ok], i5[ok], i15[ok]
                return inst, q5.ask[i5], q5.bid[i5], q5.bsz[i5], q15.bid[i15], q15.ask[i15]
            for brazo, umbral in BRAZ.items():
                inst, ask5, bid5, bsz5, bid15, ask15 = preparar(ib)
                if not len(inst): continue
                want = [querible(R.querer(b5, a5, b15, a15, umbral), True) for b5, a5, b15, a15 in zip(bid5, ask5, bid15, ask15)]
                hubo = simular_variante(inst, want, bsz5, tpm, t_fin, FIL, FE, base, "v3", brazo, 0.0, esc)
                if hubo: COB["cotizados"] += 1
                for nom, fe in FEEDS.items():
                    rx, p = fe[0], fe[1]
                    bx = rx[(rx >= t_ini) & (rx < t_fin)]
                    inst2, ask5b, bid5b, bsz5b, bid15b, ask15b = preparar(np.unique(np.concatenate([ib, bx])))
                    if not len(inst2): continue
                    want2 = [querible(R.querer(b5, a5, b15, a15, umbral), True) for b5, a5, b15, a15 in zip(bid5b, ask5b, bid15b, ask15b)]
                    allow = RG.permitido(rx, p, inst2, lado)
                    quote = np.array([w is not None for w in want2]); fb = float((quote & ~allow).sum() / quote.sum()) if quote.any() else 0.0
                    wC = [w if a else None for w, a in zip(want2, allow)]
                    simular_variante(inst2, wC, bsz5b, tpm, t_fin, FIL, FE, base, nom, brazo, fb, esc)
                    if nom == next(iter(FEEDS)) and hubo:      # control: v3 recalculado sobre el superconjunto de instantes debe dar lo mismo que sobre los instantes de libro
                        tmp = []
                        simular_variante(inst2, want2, bsz5b, tpm, t_fin, FIL, FE, base, "v3sup", brazo, 0.0, tmp.append)
                        ref = [r for r in ROWS if r["cierre"] == C and r["brazo"] == brazo and r["var"] == "v3"]
                        a = {(r["modo"], r["mult"], r["cola"], r["lp"], r["lc"]): (r["lleno"], r["coste"]) for r in ref}
                        b = {(r["modo"], r["mult"], r["cola"], r["lp"], r["lc"]): (r["lleno"], r["coste"]) for r in tmp}
                        COB["v3_vs_superset_dif"] += int(a != b)
        except Exception as e:
            COB["errores"] += 1
            print(coin, D, C, type(e).__name__, str(e)[:100], flush=True)
    COB["t_s"] = round(time.time() - COB.pop("t0"), 1)
    COB["filas"] = len(ROWS)
    if not validar_filas(ROWS):
        raise RuntimeError("claves duplicadas en la salida: no se escribe")
    escribir_atomico(fo, ROWS)
    json.dump(COB, open(os.path.join(out_dir, f"cobertura_{coin}_{D}.json" if prefijo == "rows" else f"cobertura_{prefijo}_{coin}_{D}.json"), "w"))
    print(coin, D, COB, flush=True)
    return COB


def validar_filas(rows):
    ks = [tuple(r[c] for c in CLAVE) for r in rows]
    return len(ks) == len(set(ks))


def validar_salida(fo):
    try:
        with gzip.open(fo, "rt") as fh:
            rd = csv.DictReader(fh)
            if rd.fieldnames != COLS: return False
            rows = [{c: r[c] for c in CLAVE} for r in rd]
        return validar_filas(rows)
    except (OSError, EOFError, KeyError, ValueError):
        return False


def escribir_atomico(fo, rows):
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(fo), suffix=".tmp")
    os.close(fd)
    with gzip.open(tmp, "wt", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=COLS); w.writeheader(); w.writerows(rows)
    os.replace(tmp, fo)


if __name__ == "__main__":
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    if "--ext" in sys.argv:      # brazos nuevos de H61c (preregistro aparte); salida rows_ext_*, no entra en el gate de H61b
        pj = os.path.join(HERE, "H61c_BRAZOS_PREREGISTRO.json")
        correr(a[0], a[1] if len(a) > 1 else "BTC", forzar="--force" in sys.argv, brazos=json.load(open(pj))["brazos_nuevos"], prefijo="rows_ext")
    else:
        correr(a[0], a[1] if len(a) > 1 else "BTC", forzar="--force" in sys.argv)
