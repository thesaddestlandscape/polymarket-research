#!/usr/bin/env python3
"""e1b_sim_ext.py DIA -- variantes EXTRA del ADDENDUM_E1b (A4, A5), calculadas con los MISMOS datos y funciones del simulador congelado scripts/e1_sim.py
(importado, sin tocarlo; su salida original e1_D.csv.gz no se modifica). Salida E1B/e1x_D.csv.gz, una fila por (mercado, variante):
  S1_x2_w2000|X50          A4 conservadora: evitado solo si recepcion_senal + 50 ms < tev (hora de exchange) del print  (requiere td; sin td -> no hay filas X50, missing)
  S1_x2_w2000|INV250 y |SH{+-60..240}_250   controles a 250 ms
  C1|D250                  A5: retirar 2 s cuando el top bid propio baja >= 1 tick respecto a hace 2.000 ms
  C2|FILL                  A5: la puja sigue al top bid con asentado de 250 ms (misma latencia que S1) en vez de 1.500 ms; se compara con BASE
Uso: se invoca desde e1b_diario.py (_sim_ext) con msdata.DD ya apuntando a E1B."""
import sys, os
import numpy as np, pandas as pd
AQUI = os.path.dirname(os.path.abspath(__file__)); PLAN = os.path.abspath(os.path.join(AQUI, '..'))
SAL = os.path.abspath(os.path.join(PLAN, '..', 'salida', 'scripts'))


def cargar():
    sys.path.insert(0, SAL); sys.path.insert(0, os.path.join(PLAN, 'scripts'))
    import msdata, e1_sim
    return msdata, e1_sim


def first_fill_x(ce, trig, D_ms, COOL):
    """como e1_sim.first_fill pero con la hora de exchange del print: cubierto si hay senal con senal + D_ms < ce(=senal <= ce-D_ms-1 -> D_ms=51) y ce - senal <= COOL"""
    if len(trig) == 0: return 0 if len(ce) else -1
    trig = np.sort(trig)
    for i, r in enumerate(ce):
        j = np.searchsorted(trig, r - D_ms, 'right') - 1
        if j >= 0 and r - trig[j] <= COOL: continue
        return i
    return -1


def c1_triggers(D, k, t0, t1):
    a, b = D.qs[k], D.qs[k + 1]; r = D.qr[a:b]; bid = D.qv[a:b, 0].astype(float)
    if len(r) < 2: return np.zeros(0, np.int64)
    j = np.searchsorted(r, r - 2000, 'right') - 1; ok = j >= 0
    drop = np.where(ok, bid - bid[np.clip(j, 0, None)], 0.0) <= -0.01 + 1e-9
    m = drop & (r >= t0) & (r <= t1) & np.isfinite(bid) & (bid > 0)
    return r[m]


def day(d, OUT):
    msdata, E = cargar(); Dia, SYM = msdata.Dia, msdata.SYM
    D = Dia(d); z = np.load(os.path.join(msdata.DD, f'ms_{d}.npz'), allow_pickle=False)
    td = z['td'] if 'td' in z.files else None
    rows = []; nmiss = 0; mk = {}
    for i, (act, marco, mid, fin, lado) in enumerate(D.tmap):
        if str(marco) != '5min' or str(act) not in SYM: continue
        fe = int(pd.Timestamp(str(fin)).timestamp()); mk.setdefault((str(act), fe, str(mid)), {})[str(lado)] = i
    STEP, T_HI, T_LO, SETTLE, LAG_VIVA, COOL = E.STEP, E.T_HI, E.T_LO, E.SETTLE, E.LAG_VIVA, E.COOL
    SHIFTS = E.SHIFTS; des = E.des
    for (act, fe, mid), dd in sorted(mk.items(), key=lambda x: x[0][1]):
        if 'YES' not in dd or 'NO' not in dd: continue
        w = des.get(mid)
        g = (fe * 1000 - np.arange(T_HI * 1000, T_LO * 1000 - 1, -STEP)).astype(np.int64)
        by, ay, lcy = E.tops(D, dd['YES'], g); bn, an, lcn = E.tops(D, dd['NO'], g)
        def band(b): return np.isfinite(b) & (b > 0.11 + 1e-9) & (b <= 0.30 + 1e-9)
        cy, cn = band(by), band(bn)
        if not (cy | cn).any(): continue
        if w is None: nmiss += 1; continue
        f0 = int(np.argmax(cy | cn)); yes = bool(cy[f0]); sg = 1 if yes else -1
        bid, ask, lc = (by, ay, lcy) if yes else (bn, an, lcn)
        kk = 2 if act == 'ETH' else 1; raw = E.obj_raw(bid, ask, kk)
        def objetivo(settle):
            O = np.full(len(g), np.nan); cur = np.nan
            for i in range(f0, len(g)):
                if np.isfinite(lc[i]) and g[i] - lc[i] >= settle: cur = raw[i]
                O[i] = cur
            return O
        O = objetivo(SETTLE)
        if not np.isfinite(O).any(): continue
        kown = dd['YES'] if yes else dd['NO']; kopp = dd['NO'] if yes else dd['YES']
        t0, t1 = int(g[0]), int(g[-1] + STEP)
        def candidatos(O):
            cr = []; cp = []; ce = []
            for k, own in ((kown, True), (kopp, False)):
                a, b = D.ts[k], D.ts[k + 1]; r = D.tr[a:b]
                i0, i1 = np.searchsorted(r, t0, 'right'), np.searchsorted(r, t1 + LAG_VIVA, 'right')
                v = D.tv[a + i0:a + i1]; rs = r[i0:i1]; tds = td[a + i0:a + i1] if td is not None else None
                for ii, (rr, (pr, sd, sz)) in enumerate(zip(rs, v)):
                    gi = int((rr - LAG_VIVA - t0) // STEP)
                    if gi < 0 or gi >= len(g): continue
                    o = O[gi]
                    if not np.isfinite(o): continue
                    if (own and sd == 0 and pr < o - 1e-6) or ((not own) and sd == 1 and pr > 1 - o + 1e-6):
                        cr.append(int(rr)); cp.append(o); ce.append(int(rr) - int(tds[ii]) if tds is not None else -1)
            o_ = np.argsort(cr, kind='stable')
            return np.array(cr, np.int64)[o_], np.array(cp)[o_], np.array(ce, np.int64)[o_]
        cr, cp, ce = candidatos(O)
        gana = int((w == 'YES') == yes)
        base = {'dia': d, 'act': act, 'mid': mid, 'fin': fe, 'yes': int(yes), 'gana': gana, 'n_cand': len(cr)}
        def emit(var, i, cp_=cp, cr_=cr):
            if i < 0: rows.append({**base, 'var': var, 'fill': 0, 'obj': np.nan, 'r': -1})
            else: rows.append({**base, 'var': var, 'fill': 1, 'obj': float(cp_[i]), 'r': int(cr_[i])})
        c, f = E.bn_trig(D, SYM[act], sg, t0, t1, 2000, 2); c = np.asarray(c, np.int64); f = np.asarray(f, np.int64)
        R = 'S1_x2_w2000'
        if td is not None: emit(f'{R}|X50', first_fill_x(ce, c, 51, COOL))
        emit(f'{R}|INV250', E.first_fill(cr, f, 250))
        for s in SHIFTS: emit(f'{R}|SH{s//1000:+d}_250', E.first_fill(cr, c + s, 250))
        emit('C1|D250', E.first_fill(cr, c1_triggers(D, kown, t0, t1), 250))
        cr2, cp2, _ = candidatos(objetivo(250)); emit('C2|FILL', 0 if len(cr2) else -1, cp2, cr2)
    df = pd.DataFrame(rows, columns=['dia', 'act', 'mid', 'fin', 'yes', 'gana', 'n_cand', 'var', 'fill', 'obj', 'r'])
    of = os.path.join(OUT, f'e1x_{d}.csv.gz'); df.to_csv(of, index=False)
    print(d, 'extras filas', len(df), 'mercados', df.mid.nunique(), 'con td' if td is not None else 'SIN td (X50 missing)', 'sin desenlace (missing)', nmiss, '->', of, flush=True)


if __name__ == '__main__':
    sys.exit('usar e1b_diario.py')
