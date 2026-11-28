#!/usr/bin/env python3
"""piloto_m1_m4.py DIA --etapa 1|2|3|4  (27-Nov, engineer 5m barato; contrato B_KVETO_CAP_27nov v1 + CONTRATO_CAPACIDAD_B_26nov.md M1/M4/libro cruzado). PILOTO de UN DIA, NADA confirmatorio.
0 ordenes, 0 red, 0 escrituras fuera de OUT (datalogs/capacidad_b_27nov/). dev-bk y dev se IMPORTAN (solo lectura, sys.dont_write_bytecode): no se copia ninguna funcion de decision.
Politica REAL de B-K (K6 = K1 + Calma; DEEP_PEG/H35 con repegado) = siml.run_day (b_policy_sim firmado + hooks RF5 + parches SIM-L), clase causal v3.4 por ventana (clases_causales_v34_DIA.pkl), latencia SOLO de
paquete_l ensayo_real_B2/B3/B5 (13-Nov: L1=34 principal / 47 robusto, L3a=57, L3b=59 = fallback documentado si no hay P1b COMPLETE; no desagregan por clase). Etapas (cada una = un proceso, idempotente):
  1: simula (exclusion P1b/SIM-L, RAM) -> ordenes_K6_<brazo>_DIA.pkl + etapa1_DIA.json (sello, shas, cobertura, contadores). Brazos: base (L1=34) y l1_47.
  2: UNA pasada en streaming sobre libro5_ms (zcat|grep, nada a disco): cobertura del join libro5_ms<->onchain (por (token,tx)), libro cruzado/bloqueado, y los eventos B/d/T de los tokens de las ordenes -> etapa2_DIA.pkl.
  3: M1 (cola delante y profundidad al nivel de B reconstruidas de libro5_ms; flujo en el nivel) + M4 (ancla: 0 rellenos reales de B el DIA; contraste de la cola con las 'puja_post' del seco).
  4: tablas finales + sello -> capacidad_b_27nov_piloto_DIA.json (+ run_manifest.json).
Unidad: 1.er relleno por (mercado, lado); EV ponderado por EUR (sum pnl / sum coste) y por unidad; no relleno = 0 en el EV incondicional. s>5 = CONTRAFACTUAL etiquetado (misma trayectoria de la puja; q_s del motor BASE).
Reloj: decision/llegada en RX (K del motor); la cola de libro5_ms se ordena por RECEPCION (orden de fichero con seq) y se lee en t_arr y t_arr+40 ms (sensibilidad al suelo rx-ex)."""
import sys, os, json, time, hashlib, pickle, subprocess, gzip, math, glob, collections
sys.dont_write_bytecode = True
import numpy as np
import pandas as pd

BK = '/root/polymarket-research-dev-bk'
BKE = BK + '/experimentos/5m_barato/b_k_ejecutor'
OUT = '/root/polymarket-research-datalogs/capacidad_b_27nov/'
L5MS = '/mnt/HC_Volume_106538179/libro5_ms/'
L5TX = '/mnt/HC_Volume_106538179/libro5_tx/'
ONCH = '/root/polymarket-research-datalogs/onchain_fills_%s.csv.gz'
SECO = '/root/polymarket-research-datalogs/experimento_h47_seco_BK_ledger.jsonl'
TAMANOS = (5, 10, 20, 50)
POL = 'K6'
BRAZOS = {'base': dict(), 'l1_47': dict(l1=47)}
TOLP = 0.0006
HORAS_PROHIBIDAS = ((600, 915), (2200, 2400), (0, 230))                     # 06:00-09:15Z racimo; 22:00-02:30Z seco/nulo
PUERTAS_P1B = ((1100, 1130), (1500, 1530))                                  # P1b real 11:05 / 15:15Z: no se compite (y SIM-L bloquearia su envio)
RAM_MIN_STOP, RAM_MIN_RUN = 2500, 5500


def ahora_hhmm():
    return int(time.strftime('%H%M', time.gmtime()))


def memdisp():
    return int([l for l in open('/proc/meminfo') if l.startswith('MemAvailable')][0].split()[1]) // 1024


def puerta(ram_min, esperar=1800):
    h = ahora_hhmm()
    for a, b in HORAS_PROHIBIDAS + PUERTAS_P1B:
        if a <= h < b: raise SystemExit(f'BLOCKED: hora {h} dentro de ventana prohibida {a}-{b}')
    t = 0
    while memdisp() < ram_min:
        if t >= esperar: raise SystemExit(f'BLOCKED: MemAvailable {memdisp()} MB < {ram_min} tras {esperar}s')
        time.sleep(20); t += 20


def guarda_ram(donde=''):
    a = memdisp()
    if a < RAM_MIN_STOP: raise SystemExit(f'PARADA: MemAvailable {a} MB < {RAM_MIN_STOP} ({donde})')


def escribe_json(p, d):
    tmp = p + '.tmp'
    with open(tmp, 'w') as f: json.dump(d, f, indent=1, sort_keys=True, default=str)
    os.replace(tmp, p)


def sha16(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 22), b''): h.update(b)
    return h.hexdigest()[:16]


def git_dev_bk():
    try:
        h = subprocess.run(['git', '-C', BK, 'rev-parse', 'HEAD'], capture_output=True, text=True, timeout=20).stdout.strip()
        st = subprocess.run(['git', '-C', BK, 'status', '--porcelain', '--untracked-files=no'], capture_output=True, text=True, timeout=30).stdout.splitlines()
        return h or 'missing', len(st)
    except Exception:
        return 'missing', -1


# ----------------------------------------------------------------------------------------------- etapa 1

def rejilla_cruzado(E, G, SL, dia):
    """Libro cruzado/bloqueado y sin dato, en la rejilla de 500 ms de [fin-300 s, fin-61 s] de cada token 5m (ETH/SOL/XRP) elegible (mismo filtro que la simulacion: sane ok, desenlace, par YES/NO), con la vista RX del motor (K).
    'dentro de banda' = bid en BAND_Q (0,03-0,45) = la banda del vivo (siml.BAND_Q). Estados: ok | cruzado (bid>ask) | bloqueado (bid=ask) | sin_lado (falta bid o ask) | sin_dato (sin fila q previa)."""
    K, D = E.K, E.D; lo, hi = SL.BAND_Q; rows = []
    byid = {}
    for k in E.ks:
        if E.sane(k) != 'ok' or G.capt_outcome(E, k) is None: continue
        byid.setdefault(D.mid[k], {})[D.lado[k]] = k
    for mid, v in byid.items():
        if 'YES' not in v or 'NO' not in v: continue
        for lado, k in v.items():
            fin = int(D.fin[k]); g = np.arange((fin - 300) * 1000, (fin - 61) * 1000 + 1, 500, dtype=np.int64)
            a, b = K.qb[k], K.qb[k + 1]
            qt = K.qt[a:b]; j = np.searchsorted(qt, g, side='right') - 1; ok = j >= 0; jj = np.where(ok, j, 0)
            bid = np.where(ok, K.v0[a:b][jj], np.nan).astype(float); ask = np.where(ok, K.v1[a:b][jj], np.nan).astype(float)
            vb = np.isfinite(bid) & (bid > 0); va = np.isfinite(ask) & (ask > 0)
            sin_dato = ~ok; sin_lado = ok & ~(vb & va)
            both = vb & va; cruz = both & (bid > ask + 1e-9); bloq = both & (np.abs(bid - ask) <= 1e-9)
            enb = vb & (bid >= lo - 1e-9) & (bid <= hi + 1e-9)
            rows.append(dict(k=int(k), mid=str(mid), lado=str(lado), coin=str(D.act[k]).lower(), fin=fin, n_pts=int(len(g)), n_banda=int(enb.sum()), n_cruz_banda=int((cruz & enb).sum()), n_bloq_banda=int((bloq & enb).sum()),
                             n_sin_lado_banda=int((sin_lado & enb).sum()), n_sin_dato=int(sin_dato.sum()), n_cruz=int(cruz.sum()), n_bloq=int(bloq.sum()), n_sin_lado=int(sin_lado.sum())))
    return pd.DataFrame(rows)

def etapa1(dia):
    puerta(RAM_MIN_RUN)
    sys.path.insert(0, BK); sys.path.insert(0, BKE)
    import siml as SL, paridad_lib as PL, exclusion_siml_p1b as EX, l3b_p1b as L3B, latencia_ref as LR
    import siml_run as SR
    EX.exige_sin_p1b_real()                                          # marca SIM-L vivo (P1b real se niega mientras dura) y comprueba que no hay P1b real vivo
    falta = SR.cintas_faltantes([dia])
    if falta: raise SystemExit(SR.mensaje_cintas(falta))
    sys.path.insert(0, str(SL.D_RF5))
    import experimento_maker_bk as BKm
    D = str(BKm.D_RF5); sys.path.insert(0, D)
    import rf5_run as RR, rf5_core as K5, rf5_nulo_inc as RN
    import eng_v5 as EV, puerta0_core as P0
    prob = RR.verifica_registro(); sello = RN.sello()
    if prob: raise SystemExit(f'BLOCKED: verifica_registro {prob}')
    tabla_cls = pickle.load(open(OUT + f'clases_causales_v34_{dia}.pkl', 'rb'))
    clase_de = SL.clase_de_ventana(tabla_cls)
    l3b = L3B.carga_l3b(time.strftime('%Y-%m-%d', time.gmtime()))
    cortes = K5.lee_cortes(); tp = RR.t_proc()
    E, info = EV.build(dia)
    bsrc = RR.FB.carga_binance(dia)
    gh, sucio = git_dev_bk()
    meta = dict(dia=dia, politica=POL, sello_rf5_actual=sello, sello_paridad_lib_SELLO_FIRMADO=PL.SELLO_FIRMADO, sello_coincide=(sello == PL.SELLO_FIRMADO), verifica_registro=prob,
                git_dev_bk=gh, git_dev_bk_ficheros_rastreados_modificados=sucio, l3b=l3b, latencia_fuente=LR.latencia_fuente(), latencia_recalculada=LR.recalcula(),
                clases_pkl_sha16=sha16(OUT + f'clases_causales_v34_{dia}.pkl'), clases_ventanas={f'{a_}|{b_}': n for (a_, b_), n in collections.Counter((k[0], v) for k, v in tabla_cls.items()).items()},
                sims=dict(origen=SL.carga().sha_origen, rapido=SL.carga().sha_rapido, siml=SL.carga().sha_siml), motor_info=info, arbol_sucio_nota='el seco/pins de dev-bk no se tocan: solo import', brazos={})
    rej = rejilla_cruzado(E, EV.G, SL, dia); rej.to_pickle(OUT + f'rejilla_cruzado_{dia}.pkl'); meta['rejilla_cruzado_filas'] = int(len(rej))
    for br, kw in BRAZOS.items():
        cfg = SR.cfg_de('base', 'A', l3b['post_block_ms']) if not kw else SL.configuracion(**dict(dict(post_block=int(l3b['post_block_ms'])), **kw))
        t0 = time.time(); guarda_ram('etapa1 ' + br)
        W = RR.motor(E, False); W.fills.clear()
        HK = K5.construye_hook(POL, K5.POLITICAS_K6, W._serie, bsrc, cortes, tp, lambda: W.fills, None)
        R, cov, HL = SL.run_day(dia, cfg, W, HK, clase_de=clase_de)
        if len(R):
            R = R.copy(); R['dia'] = dia
            R['token'] = [E.D.toks[int(k)] for k in R.k]
            R['token_comp'] = [(E.D.toks[int(E.D.comp(int(k)))] if E.D.comp(int(k)) is not None else '') for k in R.k]
            R['coin'] = R.coin.astype(str).str.lower()
            R['clase'] = [tabla_cls.get((c, int(round(f - 300)) * 1000), 'sin_clase') for c, f in zip(R.coin, R.fin)]
            # q por tamano s con el MISMO motor BASE (v4, tm3) y la MISMA trayectoria de la puja (t_arr, t_end): contrafactual para s != size observada
            for s in TAMANOS:
                qs = []
                for r in R.itertuples():
                    q, tf, _ = E.run_segment(int(r.k), float(r.L), int(r.t_arr), int(r.t_end), float(s), 'BASE')
                    qs.append(float(q) if (r.tf1 is not None and not pd.isna(r.tf1) and q >= 1e-3) else 0.0)
                R[f'q_{s}'] = qs
            R['q_base_recalc'] = [float(E.run_segment(int(r.k), float(r.L), int(r.t_arr), int(r.t_end), float(r.size), 'BASE')[0]) for r in R.itertuples()]
            if 'tf' not in R.columns: R['tf'] = -1
            R = P0.unidad_primer_relleno(R)
        R.to_pickle(OUT + f'ordenes_{POL}_{br}_{dia}.pkl.tmp'); os.replace(OUT + f'ordenes_{POL}_{br}_{dia}.pkl.tmp', OUT + f'ordenes_{POL}_{br}_{dia}.pkl')
        meta['brazos'][br] = dict(cfg=cfg, ordenes=int(len(R)), rellenos=int((R.q > 0).sum()) if len(R) else 0, mercados_con_orden=int(R.mid.nunique()) if len(R) else 0,
                                  cobertura=dict(mercados=cov.get('mercados'), skip=cov.get('skip'), eventos=cov.get('eventos')), contadores_hook=HL.cuenta, segundos=round(time.time() - t0, 1),
                                  pkl_sha16=sha16(OUT + f'ordenes_{POL}_{br}_{dia}.pkl'), q_base_vs_recalc_max_abs=(float((R.q - R.q_base_recalc).abs().max()) if len(R) else None),
                                  extra_rellenos_anulados=R.attrs.get('extra_rellenos'))
        del W, HK, R
    escribe_json(OUT + f'etapa1_{dia}.json', meta)
    print('etapa1 OK', json.dumps({b: v['ordenes'] for b, v in meta['brazos'].items()}), flush=True)


# ----------------------------------------------------------------------------------------------- etapa 2
def parse_bk(s):
    out = {}
    if s:
        for x in s.split(';'):
            if x:
                p, v = x.split(':'); out[float(p)] = float(v)
    return out


class Libro:
    """Libro de un token reconstruido de B (snapshot) + d (tamano ABSOLUTO del nivel; 0 = borra). best bid/ask incrementales (O(1) por delta salvo cuando se vacia el top)."""
    __slots__ = ('b', 'a', 'bb', 'aa')

    def __init__(s): s.b = {}; s.a = {}; s.bb = None; s.aa = None

    def recalc(s):
        s.bb = max((p for p, v in s.b.items() if v > 0), default=None); s.aa = min((p for p, v in s.a.items() if v > 0), default=None)

    def aplica(s, side, p, sz):
        if side == 'B':
            if sz > 0:
                s.b[p] = sz
                if s.bb is None or p > s.bb: s.bb = p
            else:
                s.b.pop(p, None)
                if s.bb is not None and abs(p - s.bb) < 1e-9: s.recalc()
        else:
            if sz > 0:
                s.a[p] = sz
                if s.aa is None or p < s.aa: s.aa = p
            else:
                s.a.pop(p, None)
                if s.aa is not None and abs(p - s.aa) < 1e-9: s.recalc()

    def top(s): return s.bb, s.aa

    def nivel(s, L): return sum(v for p, v in s.b.items() if abs(p - L) <= TOLP and v > 0)


def seco_puja_post(dia):
    """Del ledger del seco de B-K (dry-run, real=false): por orden simulada, (t_ms de intencion_post, token, precio, size, cola observada por el WS propio, libro propio). Solo del DIA."""
    import datetime as dt
    out = {}
    for ln in open(SECO):
        if dia not in ln: continue
        try: d = json.loads(ln)
        except ValueError: continue
        if not str(d.get('ts', '')).startswith(dia): continue
        o = d.get('oid')
        if d.get('tipo') == 'intencion_post':
            out[o] = dict(oid=o, slug=d.get('slug'), tok=d.get('tok'), lado=d.get('lado'), precio=float(d['precio']), size=float(d['size']), real=d.get('real'),
                          t_ms=int(dt.datetime.fromisoformat(d['ts']).timestamp() * 1000))
        elif d.get('tipo') == 'post_ok' and o in out: out[o]['cola_seco'] = d.get('cola'); out[o]['metodo_cola'] = d.get('metodo_cola')
        elif d.get('tipo') == 'puja_post' and o in out: out[o]['libro_seco'] = d.get('libro'); out[o]['T'] = d.get('T')
    return sorted(out.values(), key=lambda r: r['t_ms'])


def reales_ledger(dia):
    """Cuenta de filas real=true del DIA en los ledgers de B (B, BK, seco). 0 => B no opero con dinero real ese dia: M4 sin ancla real."""
    n = {}
    for f in ('experimento_h47_B_ledger.jsonl', 'experimento_h47_BK_ledger.jsonl', 'experimento_h47_seco_BK_ledger.jsonl'):
        c = tot = 0
        for ln in open('/root/polymarket-research-datalogs/' + f):
            if dia not in ln: continue
            try: d = json.loads(ln)
            except ValueError: continue
            if str(d.get('ts', '')).startswith(dia):
                tot += 1; c += int(d.get('real') is True)
        n[f] = dict(filas_dia=tot, real_true=c)
    return n


def orden_ficheros(fs):
    """Orden CRONOLOGICO (t_ms de la 2.a fila) y no por nombre (el pid del nombre no ordena)."""
    def t0(f):
        try:
            r = subprocess.run(f"zcat '{f}' 2>/dev/null | head -3 | tail -1", shell=True, capture_output=True, text=True, timeout=120).stdout.split(',')
            return int(r[1])
        except (ValueError, IndexError): return 1 << 62
    return sorted(fs, key=t0)


def lineas_filtradas(f, tokens, tmp):
    """zcat | grep -a -E con T,/B,/G, + ',TOKEN,' de los tokens; en streaming (nada a disco). Devuelve el Popen."""
    pats = tmp + '.pats'
    with open(pats, 'w') as fp:
        fp.write('^T,\n^B,\n^G,\n')
        for t in sorted(tokens): fp.write(f',{t},\n')
    return subprocess.Popen(f"zcat '{f}' 2>/dev/null | grep -a -E -f '{pats}'", shell=True, stdout=subprocess.PIPE, text=True, bufsize=1 << 20)


def stream2(dia):
    """Pasada UNICA en streaming sobre libro5_ms (checkpoint stream_DIA.pkl: si existe no se repite). Reconstruye el libro de los tokens de las ordenes (y del seco) y acumula flujo; guarda todos los T (token,t_ev,recv)."""
    f_out = OUT + f'stream_{dia}.pkl'
    if os.path.exists(f_out): return pickle.load(open(f_out, 'rb'))
    puerta(RAM_MIN_STOP + 1500)
    ficheros = orden_ficheros(sorted(glob.glob(L5MS + f'libro5_ms_{dia}_*.csv.gz')))
    if not ficheros: raise SystemExit(f'BLOCKED: sin libro5_ms {dia}')
    cons = collections.defaultdict(list)                              # consultas por token: (brz, i, t_arr, t_end, L) de TODOS los brazos
    comp_v = collections.defaultdict(list)                            # ventanas por token COMPLEMENTARIO (espejo): precio 1-L, solo tomadores BUY
    for brz in BRAZOS:
        R = pd.read_pickle(OUT + f'ordenes_{POL}_{brz}_{dia}.pkl')
        for i, r in enumerate(R.itertuples()):
            cons[str(r.token)].append((brz, i, int(r.t_arr), int(r.t_end), float(r.L)))
            if str(r.token_comp): comp_v[str(r.token_comp)].append((int(r.t_arr), int(r.t_end), float(r.L), brz, i))
    seco = seco_puja_post(dia)                                        # 'puja_post' del ensayo en seco de B-K (0 ordenes reales): ancla M4 de la COLA
    for i, r in enumerate(seco): cons[r['tok']].append(('seco', i, r['t_ms'], r['t_ms'] + 1, r['precio']))
    toks = set(cons)
    libros = collections.defaultdict(Libro); snap = {}                # snap[(brz,i,off)] = dict(ahead, best_bid, best_ask, depth_above, ...)
    flujo = collections.defaultdict(lambda: [0.0] * 9)                # (brz,i) -> [mismaSELL_L, mismaSELL_bajo, mismaTODO_L, espejoBUY_L, espejoBUY_bajo, n_T, mismaTODO_bajo, espejoTODO_L, espejoTODO_bajo]
    pend = {tk: 0 for tk in toks}
    qlist = {tk: sorted(set((c[2] + o, c[0], c[1], o, c[4]) for c in v for o in (0, 40))) for tk, v in cons.items()}
    ventanas = collections.defaultdict(list)
    for tk, v in cons.items():
        for c in v: ventanas[tk].append((c[2], c[3], c[4], c[0], c[1]))
    lineas = 0; T_total = 0; bloqueado = collections.Counter(); cruzado = collections.Counter(); obs = collections.Counter(); Trows = []; gaps = []
    tmp = OUT + f'.tmp_etapa2_{dia}'
    for f in ficheros:
        pr = lineas_filtradas(f, toks, tmp)
        for ln in pr.stdout:
            lineas += 1
            if lineas % 2_000_000 == 0: guarda_ram('etapa2 stream')
            c = ln.rstrip('\n').split(',')
            tp_ = c[0]
            if tp_ == 'T':
                try: Trows.append((c[2], int(c[1]), int(c[6]))); T_total += 1
                except (ValueError, IndexError): continue
                tk = c[2]
                if tk in ventanas or tk in comp_v:
                    t = int(c[6]); p = float(c[3]); sz = float(c[5]); sd = c[4]
                    for (t0, t1, L, b, i) in ventanas.get(tk, ()):
                        if t0 <= t <= t1:
                            if abs(p - L) <= TOLP:
                                flujo[(b, i)][2] += sz; flujo[(b, i)][5] += 1
                                if sd == 'SELL': flujo[(b, i)][0] += sz
                            elif p < L - TOLP:
                                flujo[(b, i)][6] += sz
                                if sd == 'SELL': flujo[(b, i)][1] += sz
                    for (t0, t1, L, b, i) in comp_v.get(tk, ()):
                        if t0 <= t <= t1:
                            if abs(p - (1.0 - L)) <= TOLP:
                                flujo[(b, i)][7] += sz
                                if sd == 'BUY': flujo[(b, i)][3] += sz
                            elif p > (1.0 - L) + TOLP:
                                flujo[(b, i)][8] += sz
                                if sd == 'BUY': flujo[(b, i)][4] += sz
            if tp_ == 'G':
                if len(c) > 3: gaps.append((int(c[1]), c[3]))
                continue
            if tp_ == 'B':
                tk = c[2]
                if tk in toks:
                    lb = libros[tk]; lb.b = parse_bk(c[3]); lb.a = parse_bk(c[4]); lb.recalc()
                continue
            if tp_ == 'd':
                tk = c[2]
                lb = libros[tk]; rx = int(c[6])
                ql = qlist[tk]; j = pend[tk]
                while j < len(ql) and ql[j][0] < rx:                  # consultas con t < rx: estado ANTES de aplicar este delta (orden por recepcion)
                    t, b, i, o, L = ql[j]; bb, aa = lb.top()
                    snap[(b, i, o)] = dict(ahead=lb.nivel(L), best_bid=bb, best_ask=aa, depth_above=sum(v for p, v in lb.b.items() if p > L + TOLP and v > 0),
                                           niveles_above=sum(1 for p, v in lb.b.items() if p > L + TOLP and v > 0), hay_libro=bool(lb.b or lb.a), rx_estado=rx)
                    j += 1
                pend[tk] = j
                lb.aplica(c[3], float(c[4]), float(c[5]))
                bb, aa = lb.top()
                if bb is not None and aa is not None:
                    if bb > aa + 1e-9: cruzado[tk] += 1
                    elif abs(bb - aa) < 1e-9: bloqueado[tk] += 1
                    obs[tk] += 1
        pr.stdout.close(); pr.wait()
    for tk, ql in qlist.items():                                      # consultas sin delta posterior: estado final (marcadas final=True)
        lb = libros.get(tk)
        for j in range(pend[tk], len(ql)):
            t, b, i, o, L = ql[j]
            if (b, i, o) in snap: continue
            bb, aa = (lb.top() if lb else (None, None))
            snap[(b, i, o)] = dict(ahead=(lb.nivel(L) if lb else None), best_bid=bb, best_ask=aa, depth_above=None, niveles_above=None, hay_libro=bool(lb and (lb.b or lb.a)), rx_estado=None, final=True)
    st = dict(ficheros=[os.path.basename(f) for f in ficheros], lineas=lineas, T_total=T_total, Trows=Trows, gaps=gaps, seco=seco, snap=dict(snap), flujo={k: v for k, v in flujo.items()}, cruzado=dict(cruzado), bloqueado=dict(bloqueado), obs=dict(obs), toks=sorted(toks))
    pickle.dump(st, open(f_out + '.tmp', 'wb')); os.replace(f_out + '.tmp', f_out)
    for pth in glob.glob(tmp + '*'): os.remove(pth)
    return st


def etapa2(dia):
    st = stream2(dia); guarda_ram('etapa2 join')
    Tset = set(st['Trows']); toks = set(st['toks']); univ = set(t[0] for t in Tset) | toks
    # libro5_tx: (t_ev, token, tx, recv); cobertura de cada evento por libro5_ms, y (tx, token) cubiertos
    n_tx = n_en = 0; tx_con_ms = set(); vistos = set()
    for f_ in sorted(glob.glob(L5TX + f'libro5_tx_{dia}_*.csv.gz')):
        with gzip.open(f_, 'rt') as fh:
            for ln in fh:
                c = ln.rstrip('\n').split(',')
                if len(c) < 4: continue
                try: k = (c[1], int(c[0]), int(c[3]))
                except ValueError: continue
                kk = (c[2], c[1], k[1], k[2])
                if kk in vistos: continue
                vistos.add(kk); n_tx += 1
                if k in Tset: n_en += 1; tx_con_ms.add((c[2], c[1]))
    vistos = None
    txs_ms = set(t for t, _ in tx_con_ms); tx_u = set(); tx_u_hit = set()
    n_oc = n_hit = 0; hora_n = collections.Counter(); hora_h = collections.Counter(); par_vistos = set(); propias = 0; n_F = 0
    for ch in pd.read_csv(ONCH % dia, usecols=['tipo', 'tx', 'token_id', 'ts_est', 'maker', 'taker'], dtype=object, chunksize=400_000):
        ch = ch[ch.tipo == 'F']; n_F += len(ch)
        propias += int((ch.maker.str.lower().str.startswith(('0x659a', '0xb6ed')) | ch.taker.str.lower().str.startswith(('0x659a', '0xb6ed'))).sum())
        for tx_, tk_, ts_ in zip(ch.tx.values, ch.token_id.values, ch.ts_est.values):
            if tk_ not in univ or (tx_, tk_) in par_vistos: continue
            tx_u.add(tx_)
            if tx_ in txs_ms: tx_u_hit.add(tx_)
            par_vistos.add((tx_, tk_)); h = int((float(ts_) // 3600) % 24); hora_n[h] += 1; n_oc += 1
            if (tx_, tk_) in tx_con_ms: n_hit += 1; hora_h[h] += 1
    cov_h = {h: dict(n=hora_n[h], cubiertos=hora_h[h]) for h in range(24)}
    res = dict(dia=dia, ficheros=st['ficheros'], lineas_leidas_filtradas=st['lineas'], T_filas=int(st['T_total']), T_unicos=int(len(Tset)),
               libro5_tx_filas=int(n_tx), libro5_tx_cubiertas_por_ms=(n_en / n_tx if n_tx else None),
               onchain_F_filas=int(n_F), onchain_tx_token_universo=int(n_oc), onchain_cubiertas_por_libro5_ms=(n_hit / n_oc if n_oc else None),
               onchain_cubiertas_n=int(n_hit), onchain_tx_universo=int(len(tx_u)), onchain_cubiertas_por_tx=(len(tx_u_hit) / len(tx_u) if tx_u else None), onchain_cubiertas_por_tx_n=int(len(tx_u_hit)), por_hora=cov_h, horas_min_cobertura=min((v['cubiertos'] / v['n'] for v in cov_h.values() if v['n'] >= 100), default=None),
               onchain_filas_de_wallets_propias_prefijo_0x659a_0xb6ed=int(propias), gaps_G=[(int(a), b) for a, b in st['gaps']][:50],
               cruzado_estados=int(sum(st['cruzado'].values())), bloqueado_estados=int(sum(st['bloqueado'].values())), estados_observados=int(sum(st['obs'].values())),
               nota_join='UNIDAD = casado (tx). libro5_ms.T == libro5_tx por (token, t_ev, recv); libro5_tx == onchain F por tx, universo = tokens vistos en libro5_ms. onchain_cubiertas_por_tx = por tx (cualquier ficha); onchain_cubiertas_por_libro5_ms = por (tx, ficha): el WS publica el casado bajo UNA ficha, el onchain trae filas de AMBAS fichas del par, por eso esta segunda es ~0,54 y no es una perdida de datos. NO prueba precio/tamano igual.')
    pickle.dump(dict(seco=st['seco'], snap=st['snap'], flujo=st['flujo'], res=res, cruzado=st['cruzado'], bloqueado=st['bloqueado'], obs=st['obs']), open(OUT + f'etapa2_{dia}.pkl.tmp', 'wb'))
    os.replace(OUT + f'etapa2_{dia}.pkl.tmp', OUT + f'etapa2_{dia}.pkl'); escribe_json(OUT + f'etapa2_{dia}_cobertura.json', res)
    print('etapa2 OK cobertura_join', res['onchain_cubiertas_por_libro5_ms'], 'tx_ms', res['libro5_tx_cubiertas_por_ms'], flush=True)


# ----------------------------------------------------------------------------------------------- etapa 3 (M1 + M4 + libro cruzado) y 4 (sello)
FEE = 0.07; REBATE = 0.2                           # feeSchedule cripto 0,07 y rebateRate 0,2 (CLAUDE.md, verificado 07-Oct); principal SIN rebate, sensibilidad CON
SEED = 20261127


def q_cons(r, sn, fl, s, espejo=True, todo_lado=False):
    """Cota CONSERVADORA FIFO con la cola REAL del libro5_ms: ahead = tamano en el nivel a t_arr (sin cancelaciones por delante), rellenos = flujo de tomadores al precio del nivel durante la vida (SELL en la misma ficha
    + BUY en la ficha complementaria a 1-L si espejo=True); barrido (a precio peor) = relleno completo. fl = [mismaSELL_L, mismaSELL_bajo, mismaTODO_L, espejoBUY_L, espejoBUY_bajo, n]."""
    if sn is None or sn.get('ahead') is None: return float('nan')                     # sin libro5 a t_arr: SIN DATO (no 0)
    fl = list(fl) + [0.0] * (9 - len(fl)) if fl is not None else [0.0] * 9               # sin trades en la ventana = flujo 0 (dato presente)
    if todo_lado: en, bajo = fl[2] + fl[7], fl[6] + fl[8]                                # COTA ALTA: sin filtrar el lado (semantica de `side` de T sin verificar)
    else: en, bajo = (fl[0] + fl[3], fl[1] + fl[4]) if espejo else (fl[0], fl[1])
    if bajo > 0: return float(s)
    return float(min(max(en - sn['ahead'], 0.0), s))


def unidades(df, qcol):
    """1.er relleno por (mid, lado) con qcol>0; las pujas sin relleno aportan una fila con q=0 (su primera orden). -> DataFrame por puja con q, coste, pnl."""
    d = df.sort_values(['mid', 'lado', 'n_ord'], kind='stable'); rows = []
    for (mid, lado), g in d.groupby(['mid', 'lado'], sort=False):
        f = g[g[qcol] > 0]
        r = (f.iloc[0] if len(f) else g.iloc[0]); q = float(r[qcol]) if len(f) else 0.0
        rows.append(dict(mid=mid, lado=lado, coin=r.coin, clase=r.clase, fin=int(r.fin), L=float(r.L), q=q, cost=q * float(r.L), pnl=q * (float(r.gana) - float(r.L)),
                         reb=REBATE * FEE * float(r.L) * (1 - float(r.L)) * q, n_ord=int(r.n_ord), size=float(r.size)))
    return pd.DataFrame(rows)


def ic_boot(u, B=2000):
    """IC90 por MERCADO (cluster = mid) del EV ponderado por EUR (sum pnl / sum coste) y del EV incondicional por puja (sum pnl / n pujas). Bootstrap fijo."""
    if not len(u): return None
    rng = np.random.default_rng(SEED); g = u.groupby('mid').agg(p=('pnl', 'sum'), c=('cost', 'sum'), n=('pnl', 'size')); P, C, N = g.p.values, g.c.values, g.n.values
    ev, inc = [], []
    for _ in range(B):
        i = rng.integers(0, len(g), len(g)); sc = C[i].sum()
        if sc > 0: ev.append(P[i].sum() / sc)
        inc.append(P[i].sum() / N[i].sum())
    q = lambda a: [float(np.percentile(a, 5)), float(np.percentile(a, 95))] if a else None
    return dict(ev_eur_ic90=q(ev), ev_eur_boot_n=len(ev), inc_por_puja_ic90=q(inc), mercados=int(len(g)))


def resumen_u(u, nml_elegibles=None):
    if not len(u): return dict(n_pujas=0)
    f = u[u.q > 0]; sc = float(u.cost.sum()); out = dict(n_pujas=int(len(u)), n_mercados=int(u.mid.nunique()), n_cierres=int(u.fin.nunique()), n_rellenos=int(len(f)), n_mercados_con_relleno=int(f.mid.nunique()), n_cierres_con_relleno=int(f.fin.nunique()),
                                                          p_relleno=float(len(f) / len(u)), acciones_rellenas=float(u.q.sum()), coste_eur=sc, pnl_eur=float(u.pnl.sum()),
                                                          ev_eur_ponderado=(float(u.pnl.sum() / sc) if sc > 0 else None), ev_por_unidad_media_pnl_sobre_coste=(float((f.pnl / f.cost).mean()) if len(f) else None),
                                                          pnl_con_rebate_eur=float((u.pnl + u.reb).sum()), ev_eur_con_rebate=(float((u.pnl + u.reb).sum() / sc) if sc > 0 else None),
                                                          ev_dado_relleno_eur_por_puja_rellena=(float(f.pnl.sum() / len(f)) if len(f) else None), ev_incondicional_pnl_por_puja=float(u.pnl.sum() / len(u)),
                                                          identidad_P_x_EVcond=(float(len(f) / len(u) * (f.pnl.sum() / len(f))) if len(f) else 0.0))
    if nml_elegibles: out.update(mercados_lado_elegibles=int(nml_elegibles), p_relleno_sobre_elegibles=float(len(f) / nml_elegibles), pnl_incondicional_por_mercado_lado_elegible=float(u.pnl.sum() / nml_elegibles))
    out['ic90'] = ic_boot(u)
    return out


def q4(a):
    a = pd.Series([x for x in a if x is not None and not (isinstance(x, float) and math.isnan(x))], dtype=float)
    return dict(n=int(len(a)), p25=float(a.quantile(.25)) if len(a) else None, p50=float(a.quantile(.5)) if len(a) else None, p75=float(a.quantile(.75)) if len(a) else None, p90=float(a.quantile(.9)) if len(a) else None) if len(a) else dict(n=0)


def etapa3(dia):
    e1 = json.load(open(OUT + f'etapa1_{dia}.json')); e2 = pickle.load(open(OUT + f'etapa2_{dia}.pkl', 'rb')); rej = pd.read_pickle(OUT + f'rejilla_cruzado_{dia}.pkl'); res2 = e2['res']
    cob = res2['onchain_cubiertas_por_tx']
    if cob is None or cob < 0.90:
        out = dict(dia=dia, status='BLOCKED', motivo=f'cobertura del join libro5_ms<->onchain por casado (tx) {cob} < 0,90 (contrato: parar); por (tx, ficha) {res2["onchain_cubiertas_por_libro5_ms"]}', cobertura_join=res2)
        escribe_json(OUT + f'capacidad_b_27nov_piloto_{dia}.json', out); print('BLOCKED cobertura', cob); return
    out = dict(contrato='B_KVETO_CAP_27nov v1 + CONTRATO_CAPACIDAD_B_26nov.md (M1, M4, libro cruzado)', dia=dia, politica=POL, status='PILOTO_1_DIA_NO_CONFIRMATORIO',
               avisos=['1 dia: IC por dias, EV sin los 2 mejores dias y n efectivo por dias NO calculables; IC90 por MERCADO (cluster mid) es exploratorio.', 'Todas las ventanas 25-Nov son clase lo (v3.4) para ETH/SOL/XRP: no hay hi en este dia (sensibilidad hi no calculable). BTC/DOGE/BNB/HYPE: sin clase, fuera, no confirmatorio.',
                       'Tamanos 10/20/50 = CONTRAFACTUAL (estimado_contrafactual): motor BASE v4 sobre la MISMA trayectoria de la puja de 5 acc; no hay relleno real a >5 acc; el tamano propio no mueve el libro.', 'Latencia: L1=34 (47 robusto), L3a=57, L3b=59 fallback; los ensayos B2/B3/B5 no desagregan por clase de suelo: igual para todas.',
                       'Sin guarda intra (prereg no firmado). Maker rebate 20 % solo como sensibilidad. Politica K6 de B-K (seco) sin guarda intra.'],
               etapa1=dict(sello_rf5_actual=e1['sello_rf5_actual'], sello_paridad_lib=e1['sello_paridad_lib_SELLO_FIRMADO'], sello_coincide=e1['sello_coincide'], git_dev_bk=e1['git_dev_bk'], arbol_rastreados_modificados=e1['git_dev_bk_ficheros_rastreados_modificados'],
                           latencia_recalculada=e1['latencia_recalculada'], l3b=e1['l3b'], brazos={b: {k: v for k, v in e1['brazos'][b].items() if k != 'cfg'} | dict(cfg=e1['brazos'][b]['cfg']) for b in e1['brazos']}, clases_ventanas=e1['clases_ventanas'], sims=e1['sims']),
               cobertura_join_libro5ms_onchain={k: v for k, v in res2.items() if k != 'por_hora'} | dict(por_hora_min_cobertura=res2['horas_min_cobertura']))
    # ---- libro cruzado / bloqueado / sin dato (vista RX del motor, rejilla 500 ms)
    cr = {}
    for coin, g in list(rej.groupby('coin')) + [('todas', rej)]:
        nb = int(g.n_banda.sum())
        cr[coin] = dict(mercado_lados_elegibles=int(len(g)), puntos_rejilla=int(g.n_pts.sum()), puntos_en_banda=nb, pct_banda_cruzado=(100 * float(g.n_cruz_banda.sum()) / nb if nb else None), pct_banda_bloqueado=(100 * float(g.n_bloq_banda.sum()) / nb if nb else None),
                        pct_banda_sin_lado=(100 * float(g.n_sin_lado_banda.sum()) / nb if nb else None), pct_total_sin_dato=100 * float(g.n_sin_dato.sum()) / max(int(g.n_pts.sum()), 1), pct_total_cruzado=100 * float(g.n_cruz.sum()) / max(int(g.n_pts.sum()), 1),
                        pct_total_bloqueado=100 * float(g.n_bloq.sum()) / max(int(g.n_pts.sum()), 1), mercado_lados_con_cruzado_banda=int((g.n_cruz_banda > 0).sum()), mercado_lados_con_bloqueado_banda=int((g.n_bloq_banda > 0).sum()),
                        mercado_lados_con_cruzado_o_bloqueado_banda=int(((g.n_cruz_banda + g.n_bloq_banda) > 0).sum()))
    out['libro_cruzado_bloqueado_rx'] = cr
    out['libro5_ms_estados_cruzado_bloqueado_en_tokens_de_ordenes'] = dict(cruzado=res2['cruzado_estados'], bloqueado=res2['bloqueado_estados'], observados=res2['estados_observados'])
    elegibles = rej.groupby('coin').size().to_dict(); aff = rej.assign(af=((rej.n_cruz_banda + rej.n_bloq_banda) > 0)).set_index(['mid', 'lado']).af.to_dict()
    # ---- M1 por brazo
    out['M1'] = {}; out['cruzado_vs_resto'] = {}
    for brz in BRAZOS:
        R = pd.read_pickle(OUT + f'ordenes_{POL}_{brz}_{dia}.pkl')
        if not len(R): out['M1'][brz] = 'sin ordenes'; continue
        R = R.reset_index(drop=True)
        for off in (0, 40):
            sn = [e2['snap'].get((brz, i, off)) for i in range(len(R))]
            R[f'ahead_{off}'] = [(x or {}).get('ahead') for x in sn]; R[f'bid_{off}'] = [(x or {}).get('best_bid') for x in sn]; R[f'depth_above_{off}'] = [(x or {}).get('depth_above') for x in sn]; R[f'niv_above_{off}'] = [(x or {}).get('niveles_above') for x in sn]
        FL = [(list(e2['flujo'].get((brz, i), [0.0] * 9)) + [0.0] * 9)[:9] for i in range(len(R))]
        R['flujo_L'] = [f[0] + f[3] for f in FL]; R['flujo_debajo'] = [f[1] + f[4] for f in FL]; R['flujo_L_misma_ficha_SELL'] = [f[0] for f in FL]; R['flujo_L_espejo_BUY'] = [f[3] for f in FL]; R['flujo_L_misma_ficha_todo_lado'] = [f[2] for f in FL]
        R['pos'] = np.where(R.bid_0.isna(), 'sin_libro5', np.where(np.abs(R.bid_0 - R.L) <= TOLP, 'top', np.where(R.bid_0 > R.L, 'detras_del_top', 'delante_del_top')))
        R['ticks_bajo_top'] = np.round((R.bid_0 - R.L) / 0.01).where(R.bid_0.notna())
        for s in TAMANOS:
            for off in (0, 40):
                R[f'qc{off}_{s}'] = [q_cons(r, e2['snap'].get((brz, i, off)), e2['flujo'].get((brz, i)), s) for i, r in enumerate(R.itertuples())]
            R[f'qm0_{s}'] = [q_cons(r, e2['snap'].get((brz, i, 0)), e2['flujo'].get((brz, i)), s, espejo=False) for i, r in enumerate(R.itertuples())]
            R[f'qa0_{s}'] = [q_cons(r, e2['snap'].get((brz, i, 0)), e2['flujo'].get((brz, i)), s, todo_lado=True) for i, r in enumerate(R.itertuples())]
        m1 = {}
        for coin, cl in [(c, k) for c in sorted(R.coin.unique()) for k in sorted(R[R.coin == c].clase.unique())] + [('todas', 'todas')]:
            g = R[(R.coin == coin) if coin != 'todas' else slice(None)]
            if coin != 'todas': g = g[g.clase == cl]
            nml = (int(rej[rej.coin == coin].shape[0]) if coin != 'todas' else int(rej.shape[0]))
            cel = dict(ordenes=int(len(g)), pujas=int(g.groupby(['mid', 'lado']).ngroups), mercado_lados_elegibles=nml, ordenes_por_posicion=g.pos.value_counts().to_dict(), size_observada=q4(g['size']), L=q4(g.L),
                       cola_delante_t_arr=q4(g.ahead_0), cola_delante_t_arr_mas40ms=q4(g.ahead_40), cola_delante_si_top=q4(g[g.pos == 'top'].ahead_0), profundidad_bid_por_encima_de_L=q4(g.depth_above_0), niveles_por_encima_de_L=q4(g.niv_above_0),
                       ticks_bajo_el_top=q4(g.ticks_bajo_top), flujo_tomadores_en_nivel_durante_vida=q4(g.flujo_L), flujo_misma_ficha_SELL=q4(g.flujo_L_misma_ficha_SELL), flujo_espejo_BUY=q4(g.flujo_L_espejo_BUY), flujo_tomadores_por_debajo_durante_vida=q4(g.flujo_debajo), ordenes_con_nivel_vacio_t_arr=int((g.ahead_0 == 0).sum()), ordenes_sin_libro5_a_t_arr=int(g.ahead_0.isna().sum()),
                       por_tamano={})
            for s in TAMANOS:
                d_ = dict(etiqueta=('observado_motor_BASE_v4' if s == 5 else 'estimado_contrafactual'))
                for nombre, col in (('BASE_motor_v4', f'q_{s}'), ('CONS_libro5_t_arr', f'qc0_{s}'), ('CONS_libro5_t_arr_mas40ms', f'qc40_{s}'), ('CONS_libro5_solo_misma_ficha', f'qm0_{s}'), ('CONS_libro5_cota_alta_sin_filtro_lado', f'qa0_{s}')):
                    gg = g.copy(); gg[col] = gg[col].fillna(0.0)
                    gg['_q'] = gg[col]
                    u = unidades(gg.assign(**{'q_tmp': gg['_q']}), 'q_tmp')
                    d_[nombre] = resumen_u(u, nml)
                    d_[nombre]['n_ordenes_cons_sin_dato_libro5'] = int(g[col].isna().sum()) if col.startswith('qc') else 0
                m_ = None
                d_['p_relleno_completo_BASE'] = float((unidades(g.assign(q_tmp=g[f'q_{s}']), 'q_tmp').q >= s - 1e-3).mean()) if len(g) else None
                cel['por_tamano'][str(s)] = d_
            m1[f'{coin}|{cl}'] = cel
        out['M1'][brz] = m1
        # libro cruzado: EV de las pujas en mercado-lados con cruzado/bloqueado en banda vs resto (tamano 5, motor BASE)
        u5 = unidades(R.assign(q_tmp=R['q_5']), 'q_tmp'); u5['afectado'] = [aff.get((m_, l_), None) for m_, l_ in zip(u5.mid, u5.lado)]
        cv = {}
        for lab, uu in (('afectados', u5[u5.afectado == True]), ('resto', u5[u5.afectado == False]), ('sin_rejilla', u5[u5.afectado.isna()])):
            n_ml = int(len(uu))
            cv[lab] = dict(pujas_mercado_lado=n_ml, rellenos=int((uu.q > 0).sum()), detalle=(resumen_u(uu) if n_ml >= 40 else 'n<40 mercados-lado: solo recuento'))
        cv['mercado_lados_afectados_total_rejilla'] = int(((rej.n_cruz_banda + rej.n_bloq_banda) > 0).sum())
        out['cruzado_vs_resto'][brz] = cv
        R.to_pickle(OUT + f'ordenes_{POL}_{brz}_{dia}_enriquecido.pkl')
    # ---- M4
    seco = e2['seco']; filas = []
    for i, r in enumerate(seco):
        sn = e2['snap'].get(('seco', i, 0)) or {}
        filas.append(dict(oid=r['oid'], slug=r['slug'], precio=r['precio'], cola_seco=r.get('cola_seco'), ahead_libro5=sn.get('ahead'), mejor_bid_libro5=sn.get('best_bid'),
                          bid_top_seco=(r.get('libro_seco') or {}).get('bids', [[None]])[0][0] if r.get('libro_seco') else None))
    dfm = pd.DataFrame(filas)
    if len(dfm):
        v = dfm.dropna(subset=['cola_seco', 'ahead_libro5']); dd = (v.ahead_libro5 - v.cola_seco)
        m4c = dict(n_seco=int(len(dfm)), n_comparables=int(len(v)), iguales_tol_0_01=int((dd.abs() <= 0.01).sum()), iguales_pct=(float((dd.abs() <= 0.01).mean()) if len(v) else None), abs_dif_p50=float(dd.abs().median()) if len(v) else None, abs_dif_p90=float(dd.abs().quantile(.9)) if len(v) else None,
                   libro5_mayor=int((dd > 0.01).sum()), libro5_menor=int((dd < -0.01).sum()), top_coincide=int((dfm.mejor_bid_libro5 == dfm.bid_top_seco).sum()))
    else: m4c = dict(n_seco=0)
    r1 = e1['brazos']['base']; Rb = pd.read_pickle(OUT + f'ordenes_{POL}_base_{dia}.pkl'); ini, fin = (min(r['t_ms'] for r in seco), max(r['t_ms'] for r in seco)) if seco else (None, None)
    sim_ventana = (Rb[(Rb.t_dec >= ini - 36 * 1000) & (Rb.t_dec <= fin + 60 * 1000)] if (len(Rb) and ini) else Rb.iloc[0:0])
    out['M4'] = dict(rellenos_reales_de_B_el_dia=dict(ledgers_real_true=reales_ledger(dia), onchain_filas_wallets_propias_prefijo=res2['onchain_filas_de_wallets_propias_prefijo_0x659a_0xb6ed'],
                                                     conclusion="0 rellenos reales de B el 25-Nov (B sin saldo a proposito; el ensayo K6 fue en SECO): M4 por hash NO ejecutable; no hay ancla de relleno real. Las filas real=true del BK ledger del dia son cancel_all y oid '0xh1' (mock de PRUEBAS escrito en el ledger de produccion 15:42/15:51Z: 0 posts, 0 fills, resp canceled=[]); 0 intencion_post real."),
                     ancla_alternativa_cola_seco=m4c, seco_ordenes=int(len(seco)), seco_pujas=int(len({r['slug'] + r['lado'] for r in seco})),
                     contraste_agregado_sim_misma_ventana=dict(ventana_ms=[ini, fin], sim_ordenes=int(len(sim_ventana)), sim_pujas=int(sim_ventana.groupby(['mid', 'lado']).ngroups) if len(sim_ventana) else 0,
                                                              nota='solo recuento (el seco corrio ~35 min en vivo con K6, el sim es SIM-L sobre el registro); no es contraste de fills (0 reales, 2 simulados).'))
    escribe_json(OUT + f'capacidad_b_27nov_piloto_{dia}.json', out)
    print('etapa3 OK', json.dumps(dict(status=out['status'], M4=out['M4']['ancla_alternativa_cola_seco'])), flush=True)


def etapa4(dia):
    p = OUT + f'capacidad_b_27nov_piloto_{dia}.json'; d = json.load(open(p))
    d['codigo_sha16'] = sha16(os.path.abspath(__file__)); d['generado'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    d['entradas_sha16'] = {f: sha16(OUT + f) for f in (f'clases_causales_v34_{dia}.pkl', f'ordenes_{POL}_base_{dia}.pkl', f'ordenes_{POL}_l1_47_{dia}.pkl', f'etapa2_{dia}.pkl', f'rejilla_cruzado_{dia}.pkl') if os.path.exists(OUT + f)}
    d.pop('sello_sha256_sin_este_campo', None)
    d['sello_sha256_sin_este_campo'] = hashlib.sha256(json.dumps(d, sort_keys=True, default=str).encode()).hexdigest()
    escribe_json(p, d)
    escribe_json(OUT + f'run_manifest_{dia}.json', dict(job='capacidad_b_27nov piloto M1/M4', dia=dia, status=d['status'], codigo_sha16=d['codigo_sha16'], entradas_sha16=d['entradas_sha16'], generado=d['generado'], reproduccion=f'bash {os.path.dirname(os.path.abspath(__file__))}/run_piloto.sh {dia}'))
    print('etapa4 OK', d['status'], d['sello_sha256_sin_este_campo'][:16])


if __name__ == '__main__':
    dia = sys.argv[1]; et = int(sys.argv[sys.argv.index('--etapa') + 1])
    os.makedirs(OUT, exist_ok=True)
    {1: etapa1, 2: etapa2, 3: etapa3, 4: etapa4}[et](dia)
