"""infra_lib.py - utilidades comunes de la infra pasiva MAPA-ESCALA (OLA 6 / TP1-INFRA). Solo lectura de datos publicos; escribe SOLO en
datalogs/mapa_infra, datalogs/mapa_tp1 y las carpetas nuevas m60/m240/m24h_onchain del volumen. No toca B, ejecutores ni modulos compartidos."""
import os, json, hashlib, subprocess, sys, time, datetime as dt
from pathlib import Path
ROOT = Path(os.environ.get('MAPA_INFRA_ROOT', '/root/polymarket-research-datalogs'))   # tests lo redirigen
VOL = Path(os.environ.get('MAPA_INFRA_VOL', '/mnt/HC_Volume_106538179'))
INFRA = ROOT / 'mapa_infra'; TP1 = ROOT / 'mapa_tp1'
REPO = Path('/root/polymarket-research')
EXCH = '0xe111180000d2663c0091e4f400237545b87b996b'
FWD0, FWD1 = '2026-10-24', '2026-11-02'            # PREREG_TESTS.md: 10 dias forward
PREF = {'5min': 'm5', '15min': 'm15', '60min': 'm60', '240min': 'm240', '24h': 'm24h'}
def now(): return dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
def log(msg, f=None):
    s = f'{now()} {msg}'; print(s, flush=True)
def atomic_json(path, obj):
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + '.tmp'); tmp.write_text(json.dumps(obj, indent=1, sort_keys=True, default=str)); os.replace(tmp, path)
def read_json(path, default=None):
    try: return json.loads(Path(path).read_text())
    except Exception: return default
def sha_file(p, n=16):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 22), b''): h.update(b)
    return h.hexdigest()[:n]
def sha_code(files):
    return {Path(f).name: sha_file(f) for f in files}
def telegram(texto):
    try:
        sys.path.insert(0, str(REPO)); from shadow_digest import enviar_telegram
        return bool(enviar_telegram(texto))
    except Exception as e:
        log(f'telegram FALLO {type(e).__name__}: {e}'); return False
def load5(): return os.getloadavg()[1]
def esperar_carga(maxload=7.0, max_min=45):
    """Espera (sleep, sin consumir nada) a load5 <= maxload; devuelve False si se agota el tiempo."""
    t0 = time.time()
    while load5() > maxload:
        if time.time() - t0 > max_min * 60: return False
        time.sleep(60)
    return True
def en_ventana_prohibida():
    h = dt.datetime.now(dt.timezone.utc); m = h.hour * 60 + h.minute
    return 6 * 60 <= m < 9 * 60 + 15 or 22 * 60 + 15 <= m < 22 * 60 + 30
def dias(a, b):
    d0, d1 = dt.date.fromisoformat(a), dt.date.fromisoformat(b)
    return [(d0 + dt.timedelta(days=i)).isoformat() for i in range((d1 - d0).days + 1)]
def ayer(k=1): return (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=k)).strftime('%Y-%m-%d')
