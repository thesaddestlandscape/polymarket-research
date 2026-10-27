import sys
f = sys.argv[1]
s = open(f).read()
old_op = '''        self.put([("T", t_ev, tk, p, msg.get("side") if msg.get("side") in ("BUY", "SELL") else "", s)])

    def alta(self, k, toks):'''
new_op = '''        self.put([("T", t_ev, tk, p, msg.get("side") if msg.get("side") in ("BUY", "SELL") else "", s)])
        _txlog(t_ev, tk, msg.get("transaction_hash"))   # 24-Oct: tx del casado en fichero APARTE (no toca el formato libro5)

    def alta(self, k, toks):'''
assert s.count(old_op) == 1
s = s.replace(old_op, new_op)
old_cls = '\nclass _Libro5:'
helper = '''
TXLOG_DIR = Path(os.environ.get("TXLOG_DIR", "/mnt/HC_Volume_106538179/libro5_tx"))
_TX = {"dia": None, "f": None, "vistos": set(), "flush": 0.0, "n": 0, "malos": 0}
_TXLK = threading.Lock()


def _txlog(t_ev, tk, tx):
    """Registra (t_ev, token, tx) de cada casado en un fichero de texto propio (≈15 MB/día), SIN tocar libro5 ni su formato.
    Una fila por (token, tx); hex validado; cualquier excepción se traga: esto nunca puede apagar libro5 ni la sesión WS."""
    try:
        if not (isinstance(tx, str) and len(tx) == 66 and tx.startswith("0x")):
            return
        int(tx, 16)
        ahora = time.time()
        dia = time.strftime("%Y-%m-%d", time.gmtime(ahora))
        with _TXLK:
            if _TX["dia"] != dia:
                if _TX["f"] is not None:
                    _TX["f"].close()
                TXLOG_DIR.mkdir(parents=True, exist_ok=True)
                _TX["f"] = open(TXLOG_DIR / f"libro5_tx_{dia}_{os.getpid()}.csv", "a", encoding="utf-8")
                _TX["dia"], _TX["vistos"] = dia, set()
            clave = (tk, tx)
            if clave in _TX["vistos"]:
                return
            _TX["vistos"].add(clave)
            _TX["f"].write(f"{t_ev},{tk},{tx},{int(ahora * 1000)}\\n")
            _TX["n"] += 1
            if ahora - _TX["flush"] >= 5:
                _TX["f"].flush()
                _TX["flush"] = ahora
    except Exception:
        _TX["malos"] += 1

'''
assert s.count(old_cls) == 1
s = s.replace(old_cls, helper + old_cls, 1)
open(f, 'w').write(s)
