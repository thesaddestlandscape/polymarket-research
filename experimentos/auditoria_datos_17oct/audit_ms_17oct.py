import csv, gzip, sys, collections, zlib, datetime

GAP_MS = 30000

def iso(ms):
    try:
        return datetime.datetime.fromtimestamp(int(ms) / 1000, datetime.timezone.utc).strftime("%H:%M:%S")
    except Exception:
        return "?"

def pct_from_counter(cnt, p):
    tot = sum(cnt.values())
    if tot == 0:
        return None
    acc = 0
    target = p * tot
    for v in sorted(cnt):
        acc += cnt[v]
        if acc >= target:
            return v
    return None

def audit_libro(path):
    out = {}
    tipos = collections.Counter()
    tokens_all = set()
    tokens_por_tipo = collections.defaultdict(set)
    ncols = collections.Counter()
    bad_rows = []
    g_rows = []
    gc1 = collections.Counter()
    seq_prev = None
    seq_first = None
    seq_jumps = []
    seq_missing = 0
    seq_dup = 0
    seq_nonmono = 0
    seq_bad = 0
    rec_prev = None
    rec_nonmono = 0
    gaps = []
    gap_max = 0
    tdiff = collections.Counter()
    first_rec = None
    last_rec = None
    n = 0
    trunc = None
    f = gzip.open(path, "rt", newline="")
    reader = csv.reader(f)
    try:
        header = next(reader)
        out["header"] = ",".join(header)
        for row in reader:
            n += 1
            ncols[len(row)] += 1
            if len(row) != 8:
                if len(bad_rows) < 5:
                    bad_rows.append((n, len(row), ",".join(row)[:120]))
                continue
            tipo, t_ms, tok, c1, c2, c3, rec, seq = row
            tipos[tipo] += 1
            try:
                rec_i = int(rec)
            except ValueError:
                rec_i = None
            try:
                seq_i = int(seq)
            except ValueError:
                seq_i = None
                seq_bad += 1
            if tipo == "G":
                gc1[c1] += 1
                if len(g_rows) < 20:
                    g_rows.append((iso(rec), c1, c2, tok, seq))
            else:
                tokens_all.add(tok)
                tokens_por_tipo[tipo].add(tok)
                try:
                    if rec_i is not None and t_ms:
                        tdiff[rec_i - int(t_ms)] += 1
                except ValueError:
                    pass
            if seq_i is not None:
                if seq_first is None:
                    seq_first = seq_i
                if seq_prev is not None:
                    if seq_i == seq_prev:
                        seq_dup += 1
                    elif seq_i < seq_prev:
                        seq_nonmono += 1
                    elif seq_i > seq_prev + 1:
                        seq_missing += seq_i - seq_prev - 1
                        if len(seq_jumps) < 10:
                            seq_jumps.append((seq_prev, seq_i))
                seq_prev = seq_i
            if rec_i is not None:
                if first_rec is None:
                    first_rec = rec_i
                last_rec = rec_i
                if rec_prev is not None:
                    if rec_i < rec_prev:
                        rec_nonmono += 1
                    else:
                        d = rec_i - rec_prev
                        if d > GAP_MS:
                            gaps.append((iso(rec_prev), iso(rec_i), round(d / 1000, 1)))
                        if d > gap_max:
                            gap_max = d
                rec_prev = rec_i
    except (EOFError, zlib.error, gzip.BadGzipFile, OSError) as e:
        trunc = f"{type(e).__name__}: {e}"
    finally:
        f.close()
    out.update(dict(
        filas=n, tipos=dict(tipos), ncols=dict(ncols), bad_rows=bad_rows,
        tokens_distintos=len(tokens_all),
        tokens_por_tipo={k: len(v) for k, v in tokens_por_tipo.items()},
        g_motivos=dict(gc1), g_filas=g_rows,
        seq_primero=seq_first, seq_ultimo=seq_prev, seq_faltan=seq_missing,
        seq_saltos_muestra=seq_jumps, seq_dup=seq_dup, seq_no_mono=seq_nonmono, seq_no_int=seq_bad,
        rec_primero=iso(first_rec) if first_rec else None, rec_ultimo=iso(last_rec) if last_rec else None,
        rec_no_mono=rec_nonmono, huecos_gt30s=len(gaps), huecos_muestra=gaps[:10],
        hueco_max_s=round(gap_max / 1000, 1),
        rec_menos_t_p50_s=round((pct_from_counter(tdiff, 0.5) or 0) / 1000, 2),
        rec_menos_t_p90_s=round((pct_from_counter(tdiff, 0.9) or 0) / 1000, 2),
        rec_menos_t_p99_s=round((pct_from_counter(tdiff, 0.99) or 0) / 1000, 2),
        rec_menos_t_neg=sum(v for k, v in tdiff.items() if k < 0),
        truncado=trunc,
    ))
    return out

def audit_mv(path):
    out = {}
    tipos = collections.Counter()
    bolsas = collections.Counter()
    horas = collections.Counter()
    ncols = collections.Counter()
    g_rows = []
    g_motivos = collections.Counter()
    last_rec_key = {}      # (bolsa,simbolo) -> recepcion previa (Q+T)
    last_rec_bolsa = {}    # bolsa -> recepcion previa (cualquier fila)
    gaps_key = collections.Counter()
    gaps_key_max = {}
    gaps_bolsa = collections.Counter()
    gaps_bolsa_max = {}
    gaps_sample = []
    sello_diff = collections.defaultdict(collections.Counter)
    sello_vacio = collections.Counter()
    sello_neg = collections.Counter()
    simbolos = collections.defaultdict(set)
    first_rec = {}
    last_rec = {}
    n = 0
    trunc = None
    f = gzip.open(path, "rt", newline="")
    reader = csv.reader(f)
    try:
        header = next(reader)
        out["header"] = ",".join(header)
        for row in reader:
            n += 1
            ncols[len(row)] += 1
            if len(row) != 8:
                continue
            bolsa, tipo, sim, sello, rec, c1, c2, c3 = row
            try:
                rec_i = int(rec)
            except ValueError:
                continue
            tipos[(bolsa, tipo)] += 1
            bolsas[bolsa] += 1
            first_rec.setdefault(bolsa, rec_i)
            last_rec[bolsa] = rec_i
            if tipo == "G":
                g_motivos[(bolsa, c2, c3)] += 1
                if len(g_rows) < 40:
                    g_rows.append((bolsa, iso(rec_i), c2, c1[:20]))
                continue
            horas[(bolsa, tipo, datetime.datetime.fromtimestamp(rec_i / 1000, datetime.timezone.utc).strftime("%H"))] += 1
            simbolos[bolsa].add(sim)
            k = (bolsa, sim)
            if k in last_rec_key:
                d = rec_i - last_rec_key[k]
                if d > GAP_MS:
                    gaps_key[k] += 1
                    gaps_key_max[k] = max(gaps_key_max.get(k, 0), d)
            last_rec_key[k] = rec_i
            if bolsa in last_rec_bolsa:
                d = rec_i - last_rec_bolsa[bolsa]
                if d > GAP_MS:
                    gaps_bolsa[bolsa] += 1
                    gaps_bolsa_max[bolsa] = max(gaps_bolsa_max.get(bolsa, 0), d)
                    if len(gaps_sample) < 15:
                        gaps_sample.append((bolsa, iso(last_rec_bolsa[bolsa]), iso(rec_i), round(d / 1000, 1)))
            last_rec_bolsa[bolsa] = rec_i
            if sello == "":
                sello_vacio[bolsa] += 1
            else:
                try:
                    dd = rec_i - int(sello)
                    if dd < 0:
                        sello_neg[bolsa] += 1
                    sello_diff[bolsa][dd] += 1
                except ValueError:
                    sello_vacio[bolsa] += 1
    except (EOFError, zlib.error, gzip.BadGzipFile, OSError) as e:
        trunc = f"{type(e).__name__}: {e}"
    finally:
        f.close()
    out.update(dict(
        filas=n, ncols=dict(ncols),
        tipos={f"{b}|{t}": v for (b, t), v in tipos.items()},
        horas={f"{b}|{t}|{h}": v for (b, t, h), v in sorted(horas.items())},
        simbolos={b: len(s) for b, s in simbolos.items()},
        simbolos_lista={b: sorted(s) for b, s in simbolos.items()},
        g_motivos={f"{b}|{c2}|{c3}": v for (b, c2, c3), v in g_motivos.items()},
        g_filas=g_rows,
        huecos_gt30s_por_bolsa={b: gaps_bolsa.get(b, 0) for b in last_rec_bolsa},
        hueco_max_bolsa_s={b: round(v / 1000, 1) for b, v in gaps_bolsa_max.items()},
        huecos_gt30s_por_bolsa_simbolo={f"{b}|{s}": v for (b, s), v in gaps_key.items()},
        huecos_gt30s_muestra=gaps_sample,
        sello_vacio=dict(sello_vacio),
        sello_negativo=dict(sello_neg),
        rec_menos_sello_mediana_ms={b: pct_from_counter(c, 0.5) for b, c in sello_diff.items()},
        rec_menos_sello_p90_ms={b: pct_from_counter(c, 0.9) for b, c in sello_diff.items()},
        rec_primero={b: iso(v) for b, v in first_rec.items()},
        rec_ultimo={b: iso(v) for b, v in last_rec.items()},
        truncado=trunc,
    ))
    return out

if __name__ == "__main__":
    kind, path = sys.argv[1], sys.argv[2]
    res = audit_libro(path) if kind == "libro" else audit_mv(path)
    import pprint
    pprint.pprint(res, width=160, compact=True)
