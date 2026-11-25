#!/usr/bin/env python3
"""probe_clob_en_429.py -- sonda PASIVA independiente (stdlib). Cada 10 s pide a gamma-api (/markets/<id>) y a CLOB (/markets/<condition_id>)
los mismos 5 mercados Up/Down 5m/15m vigentes (elegidos del CSV data/markets de hoy, refrescados cada 60 s) y registra status y latencia de
ambos: valida si CLOB responde mientras gamma da 429 (la hipotesis del fix). Solo lectura, sin credenciales, ~1 req/s en total.
Salida: /root/polymarket-research-datalogs/probe_clob_429_YYYY-MM-DD.csv.gz  (ts_ms,fuente,mercado,status,ms,detalle; detalle = 'tokens_ok' |
'tokens_distintos_de_gamma' | error). Retencion 5 d.
Uso: probe_clob_en_429.py --hasta HH:MM [--desde HH:MM]     (UTC; sin --desde empieza ya; --dur N para prueba de N s)"""
import csv, glob, gzip, io, json, os, sys, time, urllib.request, urllib.error
from datetime import datetime, timezone, timedelta
OUT = '/root/polymarket-research-datalogs'; CSVM = '/root/polymarket-research/data/markets/%s.csv'
UA = {'User-Agent': 'probe/1.0'}

def hm_a_epoch(hm):
    h, m = map(int, hm.split(':')); n = datetime.now(timezone.utc); t = n.replace(hour=h, minute=m, second=0, microsecond=0)
    return t.timestamp() if t.timestamp() >= n.timestamp() - 3600 else (t + timedelta(days=1)).timestamp()

def get(url):
    t0 = time.time()
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=8) as r:
            return r.status, int(1000 * (time.time() - t0)), r.read()
    except urllib.error.HTTPError as e:
        return e.code, int(1000 * (time.time() - t0)), b''
    except Exception as e:
        return 0, int(1000 * (time.time() - t0)), type(e).__name__.encode()

def elegir(n=5):
    f = CSVM % datetime.now(timezone.utc).strftime('%Y-%m-%d')
    try:
        with open(f, 'rb') as fh:
            hdr = fh.readline().decode().strip().split(','); fh.seek(0, 2); fh.seek(max(0, fh.tell() - 3_000_000)); fh.readline()
            rows = csv.DictReader(io.StringIO(fh.read().decode('utf8', 'replace')), fieldnames=hdr)
            vistos = {}; ahora = time.time()
            for r in rows:
                sl = r.get('slug') or ''
                if 'updown-5m' in sl or 'updown-15m' in sl:
                    try: e = datetime.fromisoformat(r['end_date'].replace('Z', '+00:00')).timestamp()
                    except Exception: continue
                    if e > ahora + 90 and r.get('condition_id', '').startswith('0x'): vistos[r['market_id']] = (r['condition_id'], e)
        return [(m, c) for m, (c, e) in sorted(vistos.items(), key=lambda kv: kv[1][1])[:n]]
    except Exception:
        return []

def main():
    a = sys.argv; dur = int(a[a.index('--dur') + 1]) if '--dur' in a else None
    t_ini = hm_a_epoch(a[a.index('--desde') + 1]) if '--desde' in a else time.time()
    t_fin = (time.time() + dur) if dur else hm_a_epoch(a[a.index('--hasta') + 1])
    for f in glob.glob(OUT + '/probe_clob_429_*.csv.gz'):
        if time.time() - os.path.getmtime(f) > 5 * 86400: os.remove(f)
    while time.time() < t_ini: time.sleep(1)
    gz = gzip.open(f'{OUT}/probe_clob_429_{datetime.now(timezone.utc):%Y-%m-%d}.csv.gz', 'at'); w = csv.writer(gz)
    if gz.tell() == 0: w.writerow(['ts_ms', 'fuente', 'mercado', 'status', 'ms', 'detalle'])
    mk, t_sel = [], 0
    while time.time() < t_fin:
        t0 = time.time()
        if t0 - t_sel > 60 or not mk: mk, t_sel = elegir() or mk, t0
        for mid, cid in mk:
            sg, mg, bg = get(f'https://gamma-api.polymarket.com/markets/{mid}')
            sc, mc, bc = get(f'https://clob.polymarket.com/markets/{cid}')
            tg = None
            if sg == 200:
                try: j = json.loads(bg); tk = j['clobTokenIds']; tg = set(json.loads(tk) if isinstance(tk, str) else tk)
                except Exception: tg = None
            dg = 'tokens_ok' if tg else (bg.decode('utf8', 'replace')[:40] if sg != 200 else 'json_raro')
            dc = bc.decode('utf8', 'replace')[:40] if sc != 200 else 'json_raro'
            if sc == 200:
                try:
                    tc = {x['token_id'] for x in json.loads(bc)['tokens']}; dc = 'tokens_ok' if (tg is None or tc == tg) else 'tokens_distintos_de_gamma'
                except Exception: pass
            ts = int(time.time() * 1000); w.writerow([ts, 'gamma', mid, sg, mg, dg]); w.writerow([ts, 'clob', mid, sc, mc, dc])
        gz.flush(); time.sleep(max(0, 10 - (time.time() - t0)))
    gz.close()

if __name__ == '__main__': main()
