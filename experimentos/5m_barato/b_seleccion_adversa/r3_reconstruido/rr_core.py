#!/usr/bin/env python3
"""rr_core.py -- RECONSTRUCCION INFORMATIVA (offline, solo lectura) del brazo R3 shadow desde libro5_ms (L2 5m: B/d/T/G) + m15_registro (q = top del 15m).
Importa SIN modificar el nucleo vivo (r3_regla.Nucleo/Mercado). Salida SOLO en /root/polymarket-research-datalogs/r3_reconstruido/ con fuente=reconstruido.
Decisiones con tiempo de RECEPCION, orden de flujo (seq) por recepcion; libro cruzado/ausente del 15m => fail-closed (lo hace r3_regla). Sin red, sin ordenes."""
import gzip
import os
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

sys.path.insert(0, "/root/polymarket-research/experimentos/5m_barato/b_seleccion_adversa/r3_shadow")
import r3_regla as R  # noqa: E402

L5 = Path("/mnt/HC_Volume_106538179/libro5_ms")
M15 = Path("/mnt/HC_Volume_106538179/m15_registro")
OUT = Path("/root/polymarket-research-datalogs/r3_reconstruido")
MONEDAS = ("eth", "sol", "xrp")
DELTA_CREA_S = 0.2        # calibrado con las filas mkt del brazo vivo (ver rr_puerta.py --calibrar): mediana r - (ini-25 s)
TICK_MS = 100


def dia_ini(d):
    return int(datetime.strptime(d, "%Y-%m-%d").replace(tzinfo=timezone.utc).timestamp())


def dias_vecinos(d):
    t = dia_ini(d)
    return [datetime.fromtimestamp(t + k * 86400, timezone.utc).strftime("%Y-%m-%d") for k in (-1, 0, 1)]


def mapa_tokens(d):
    """{(coin, marco, fin_epoch): {'YES': tok, 'NO': tok, 'mid': id}} desde las filas k de m15_registro de D-1, D, D+1. conflictos = claves con >1 token por lado."""
    m, conf = {}, 0
    for dd in dias_vecinos(d):
        f = M15 / f"m15_registro_{dd}.csv.gz"
        if not f.exists():
            continue
        try:
            with gzip.open(f, "rb") as fh:
                for ln in fh:
                    if ln[:2] != b"k,":
                        continue
                    p = ln.decode().rstrip("\n").split(",")
                    if len(p) < 8 or p[4] not in ("5min", "15min") or p[3].lower() not in MONEDAS:
                        continue
                    fin = int(datetime.fromisoformat(p[6]).timestamp())
                    e = m.setdefault((p[3].lower(), p[4], fin), {"mid": p[5]})
                    if p[7] in e and e[p[7]] != p[2]:
                        conf += 1
                    e[p[7]] = p[2]
        except (EOFError, OSError):
            pass
    return m, conf


def mercados_dia(d, mapa):
    """Lista de mercados 5m del dia (ini en D) con tokens 5m y 15m. -> (lista, faltan)."""
    t0, out, faltan = dia_ini(d), [], []
    for ini in range(t0, t0 + 86400, 300):
        for coin in MONEDAS:
            e5 = mapa.get((coin, "5min", ini + 300))
            fin15 = ini // 900 * 900 + 900
            e15 = mapa.get((coin, "15min", fin15))
            slug = f"{coin}-updown-5m-{ini}"
            if not e5 or not e15 or "YES" not in e5 or "NO" not in e5 or "YES" not in e15 or "NO" not in e15:
                faltan.append(slug)
                continue
            out.append({"coin": coin, "ini": ini, "slug": slug, "id5": e5["mid"], "id15": e15["mid"],
                        "mk5": {"slug": slug, "id": e5["mid"], "up": e5["YES"], "down": e5["NO"]},
                        "mk15": {"slug": f"{coin}-updown-15m-{fin15 - 900}", "id": e15["mid"], "up": e15["YES"], "down": e15["NO"]}})
    return out, faltan


def ficheros_l5(d):
    """Ficheros libro5 del dia D (en orden de mtime = orden temporal de los flujos) + los de D-1 que terminan en los ultimos 30 min antes de D."""
    t0 = dia_ini(d)
    res = []
    for p in L5.glob("libro5_ms_*.csv.gz"):
        dd = p.name[len("libro5_ms_"):len("libro5_ms_") + 10]
        mt = p.stat().st_mtime
        if dd == d or (dd == dias_vecinos(d)[0] and mt >= t0 - 1800):
            res.append((mt, p))
    # D+1: un 5m que cierra tras medianoche no hace falta (solo ini en D); su actividad termina en fin-60
    return [p for _, p in sorted(res)]


def filas_l5(ficheros, toks, desde_ms=0, hasta_ms=1 << 62):
    """Genera (recv_ms, tipo, tok, a, b, c, t_ms) en ORDEN DE FLUJO. toks = set de bytes; G con token propio o '*'. Tolera cola truncada."""
    for p in ficheros:
        try:
            fh = gzip.open(p, "rb")
        except OSError:
            continue
        try:
            for ln in fh:
                x = ln.split(b",", 7)
                if len(x) < 8:
                    continue
                t = x[0]
                tk = x[2]
                if t == b"G":
                    if tk != b"*" and tk not in toks:
                        continue
                elif tk not in toks:
                    continue
                try:
                    rc = int(x[6])
                except ValueError:
                    continue
                if rc < desde_ms:
                    continue
                if rc > hasta_ms:
                    return
                yield (rc, t.decode(), tk.decode(), x[3], x[4], x[5], int(x[1]))
        except (EOFError, OSError):
            pass
        finally:
            fh.close()


def cargar_q(d, toks15):
    """Arrays ordenados por recepcion de las filas q de los tokens 15m: (recv, tokidx, bid, ask, bsz, asz). Ventana D-1 23:20 .. D+1 00:10."""
    t0 = dia_ini(d) * 1000
    lo, hi = t0 - 40 * 60000, t0 + 86400000 + 10 * 60000
    idx = {t.encode(): i for i, t in enumerate(sorted(toks15))}
    from array import array
    cols = [array('q'), array('i')] + [array('d') for _ in range(4)]
    nan = float("nan")

    def f(s):
        return nan if s in (b"None", b"") else float(s)
    for dd in dias_vecinos(d):
        fp = M15 / f"m15_registro_{dd}.csv.gz"
        if not fp.exists():
            continue
        try:
            with gzip.open(fp, "rb") as fh:
                for ln in fh:
                    if ln[:2] != b"q,":
                        continue
                    x = ln.split(b",", 8)
                    i = idx.get(x[2])
                    if i is None or len(x) < 8:
                        continue
                    rc = int(x[7])
                    if rc < lo or rc > hi:
                        continue
                    cols[0].append(rc); cols[1].append(i); cols[2].append(f(x[3])); cols[3].append(f(x[4])); cols[4].append(f(x[5])); cols[5].append(f(x[6]))
        except (EOFError, OSError):
            pass
    a = [np.frombuffer(c, dtype=dt) for c, dt in zip(cols, (np.int64, np.int32, np.float64, np.float64, np.float64, np.float64))]
    o = np.argsort(a[0], kind="stable")
    return [c[o] for c in a], sorted(toks15)


def cobertura(d, mercs, verbose=print):
    """Pre-pase de libro5 (solo filas B y G): por mercado, ¿feed continuo en [t_sub, fin-60+2]? -> {slug: motivo|'ok'}, estadisticas del pase."""
    toks = {}
    for m in mercs:
        toks[m["mk5"]["up"].encode()] = m["slug"]
        toks[m["mk5"]["down"].encode()] = m["slug"]
    tset = set(toks)
    G, Gstar, B = defaultdict(list), [], defaultdict(list)    # claves str (token)
    n = 0
    for rc, t, tk, a, b, c, tms in filas_l5(ficheros_l5(d), tset):
        n += 1
        if t == "G":
            (Gstar if tk == "*" else G[tk]).append(rc)
        elif t == "B":
            B[tk].append(rc)
    import bisect
    Gstar.sort()
    res, st = {}, defaultdict(int)
    for m in mercs:
        t_sub = int((m["ini"] - R.PRE_S + DELTA_CREA_S) * 1000)
        t_end = int((m["ini"] + 300 - R.T_STOP + 2) * 1000)
        motivo = "ok"
        for tk in (m["mk5"]["up"], m["mk5"]["down"]):
            gl = sorted(G.get(tk, []) + Gstar)
            bl = sorted(B.get(tk, []))
            # ultima ruptura <= t_sub
            i = bisect.bisect_right(gl, t_sub)
            ult_g = gl[i - 1] if i else -1
            j = bisect.bisect_right(bl, t_sub)
            ult_b = bl[j - 1] if j else -1
            if ult_b < 0 or ult_b < ult_g:
                motivo = "sin_B_previo"
                break
            k = bisect.bisect_right(gl, t_sub)
            if k < len(gl) and gl[k] <= t_end:
                motivo = "hueco_libro5"
                break
        res[m["slug"]] = motivo
        st[motivo] += 1
    verbose(f"cobertura {d}: filas B/G leidas={n} mercados={len(mercs)} " + " ".join(f"{k}={v}" for k, v in sorted(st.items())))
    return res, dict(st)


# ------------------------------------------------------------------ replay
def _niveles(s):
    out = {}
    for x in s.decode().split(";"):
        if ":" in x:
            p, z = x.split(":", 1)
            try:
                out[float(p)] = float(z)
            except ValueError:
                pass
    return out


def _snap(tk, bids, asks):
    return {"asset_id": tk, "bids": [{"price": p, "size": z} for p, z in bids.items()], "asks": [{"price": p, "size": z} for p, z in asks.items()]}


def _msg15(tk, s):
    bid, ask, bs, as_ = s
    return {"asset_id": tk, "bids": [] if bid != bid else [{"price": bid, "size": bs if bs == bs else 0.0}],
            "asks": [] if ask != ask else [{"price": ask, "size": as_ if as_ == as_ else 0.0}]}


def replay(d, mercs, cob, salida, log=print, max_mercados=None):
    """Reproduce el brazo vivo sobre los mercados con cobertura 'ok'. Un solo Nucleo por dia (los topes de B son globales). -> stats."""
    valid = [m for m in mercs if cob.get(m["slug"]) == "ok"]
    if max_mercados:
        valid = valid[:max_mercados]
    nuc = R.Nucleo(salida)
    por5 = {}                                  # tok5 -> mercado(dict)
    for m in valid:
        por5[m["mk5"]["up"]] = m
        por5[m["mk5"]["down"]] = m
    toks15 = {m["mk15"][k] for m in valid for k in ("up", "down")}
    q, nombres = cargar_q(d, toks15)
    qrecv, qtok, qb, qa, qbs, qas = q
    qn = len(qrecv)
    log(f"q 15m: filas={qn} tokens={len(nombres)}")
    qstate = {}                                # tok15 -> (bid, ask, bs, as)
    tok15_mercs = defaultdict(list)            # tok15 -> [Mercado vivo]
    estado = {}                                # tok5 -> [bids, asks] (None hasta el primer B tras ruptura)
    creates = sorted(((int((m["ini"] - R.PRE_S + DELTA_CREA_S) * 1000), m["slug"], m) for m in valid), key=lambda x: (x[0], x[1]))
    gen = filas_l5(ficheros_l5(d), {t.encode() for t in por5})
    nxt = next(gen, None)
    ci, qi = 0, 0
    vivos = {}                                 # slug -> Mercado vivo (no cerrado)
    st = defaultdict(int)
    next_tick = None
    INF = 1 << 62
    t_log = 0.0
    while True:
        if not vivos and ci >= len(creates):
            break
        tl = nxt[0] if nxt is not None else INF
        tq = int(qrecv[qi]) if qi < qn else INF
        tc = creates[ci][0] if ci < len(creates) else INF
        tt = next_tick if (vivos and next_tick is not None) else INF
        t = min(tl, tq, tc, tt)
        if t >= INF:
            break
        if t == tc:                                                    # alta de mercado + snapshots (como el WS al suscribir)
            _, slug, m = creates[ci]
            ci += 1
            nm = nuc.nuevo(m["coin"], m["ini"], m["mk5"], m["mk15"], t)
            for tk in (m["mk5"]["up"], m["mk5"]["down"]):
                e = estado.get(tk)
                if e is None:
                    st["snapshot_5m_ausente"] += 1
                    continue
                nm.on_msg(_snap(tk, e[0], e[1]), t / 1000.0)
            for tk in (m["mk15"]["up"], m["mk15"]["down"]):
                tok15_mercs[tk].append(nm)
                s15 = qstate.get(tk)
                if s15 is None:
                    st["snapshot_15m_ausente"] += 1
                    continue
                nm.on_msg(_msg15(tk, s15), t / 1000.0)
            if not vivos or next_tick is None:
                next_tick = (t // TICK_MS + 1) * TICK_MS
            vivos[slug] = nm
        elif t == tl:
            rc, ty, tk, a, b, c, tms = nxt
            nxt = next(gen, None)
            if ty == "G":
                st["G"] += 1
                if tk == "*":
                    for k2 in estado:
                        estado[k2] = None
                else:
                    estado[tk] = None
                continue
            m = por5.get(tk)
            if m is None:
                continue
            nm = vivos.get(m["slug"])
            if ty == "B":
                estado[tk] = [_niveles(a), _niveles(b)]
                if nm is not None:
                    nm.on_msg(_snap(tk, estado[tk][0], estado[tk][1]), rc / 1000.0)
            elif ty == "d":
                e = estado.get(tk)
                if e is None:
                    st["d_sin_B"] += 1
                    continue
                p, z = float(b), float(c)
                lado = e[0] if a == b"B" else e[1]
                if z <= 0:
                    lado.pop(p, None)
                else:
                    lado[p] = z
                if nm is not None:
                    nm.on_msg({"price_changes": [{"asset_id": tk, "price": p, "size": z, "side": "BUY" if a == b"B" else "SELL"}]}, rc / 1000.0)
            elif ty == "T" and nm is not None:
                nm.on_msg({"event_type": "last_trade_price", "asset_id": tk, "price": a.decode(), "side": b.decode(), "size": c.decode(), "timestamp": tms}, rc / 1000.0)
            st["filas5"] += 1
        elif t == tq:
            tk = nombres[int(qtok[qi])]
            s15 = (float(qb[qi]), float(qa[qi]), float(qbs[qi]), float(qas[qi]))
            qstate[tk] = s15
            lst = tok15_mercs.get(tk)
            if lst:
                msg = _msg15(tk, s15)
                for nm in lst:
                    nm.on_msg(msg, tq / 1000.0)
            qi += 1
        else:                                                          # tick de 10 Hz
            now = t / 1000.0
            for nm in vivos.values():
                nm.vivo(now)                                           # la conexion del brazo vivo estaba viva (PING/PONG); los huecos ya se excluyeron en `cobertura`
            nuc.tick(now)
            nuc.podar(now)
            for s in [s for s, nm in vivos.items() if nm.cerrado]:
                nm = vivos.pop(s)
                for tk15 in (nm.u15, nm.d15):
                    tok15_mercs[tk15] = [x for x in tok15_mercs[tk15] if x is not nm]
                for tk in (nm.up, nm.dn):
                    estado.pop(tk, None)
                    por5.pop(tk, None)
                st["cerrados"] += 1
            next_tick = t + TICK_MS
            if now - t_log > 3600:
                t_log = now
                log(f"  reloj={datetime.fromtimestamp(now, timezone.utc):%H:%M:%S} cerrados={st['cerrados']} vivos={len(vivos)}")
    for nm in list(nuc.mercados.values()):
        if not nm.cerrado:
            nuc.cerrar(nm, (next_tick or 0) / 1000.0, "parada_proceso")
            st["cierre_forzado"] += 1
    st["nuc_stats"] = dict(nuc.stats)
    return dict(st)
