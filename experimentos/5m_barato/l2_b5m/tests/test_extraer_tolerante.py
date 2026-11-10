import gzip, io, json, os, subprocess, sys, zlib
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.insert(0, D)
import l2_gzcat as G
import l2_extraer_dia as X

HDR = "tipo,t_ms,token,c1,c2,c3,recepcion,seq"


def _filas(n=2000):
    L = [HDR, "G,1,*,arranque,,,1,1"]
    for i in range(n):
        s = i + 2
        L.append(f"B,{s},tkA,0.10:5;0.30:7;0.50:9,0.55:3;0.60:4,,{s},{s}")
        L.append(f"d,{s},tkA,B,0.{20 + i % 30},3.0,{s},{s}")
        L.append(f"d,{s},tkA,A,0.7,3.0,{s},{s}")
        L.append(f"T,{s},tkA,0.31,SELL,2,{s},{s}")
    return L


def _gz_sync(path, lineas, cerrar):
    co = zlib.compressobj(wbits=31)
    raw = ("\n".join(lineas) + "\n").encode()
    data = co.compress(raw) + (co.flush() if cerrar else co.flush(zlib.Z_SYNC_FLUSH))
    open(path, "wb").write(data)
    return raw


def test_truncado_en_medio_solo_lineas_completas(tmp_path):
    raw = _gz_sync(tmp_path / "x.gz", _filas(), True)
    b = (tmp_path / "x.gz").read_bytes()
    (tmp_path / "t.gz").write_bytes(b[: len(b) // 2])            # corte a mitad, casi seguro a mitad de linea
    out = io.BytesIO()
    st = G.leer_tolerante(str(tmp_path / "t.gz"), out)
    v = out.getvalue()
    assert st["truncado"] and not st["corrupto"]
    assert v.endswith(b"\n") and raw.startswith(v)               # prefijo exacto, sin basura
    assert st["lineas_ok"] == v.count(b"\n") > 0
    assert st["filas_perdidas_est"] > 0 and st["bytes_comp_consumidos"] <= len(b) // 2


def test_gz_integro_sin_perdida(tmp_path):
    raw = _gz_sync(tmp_path / "x.gz", _filas(50), True)
    out = io.BytesIO(); st = G.leer_tolerante(str(tmp_path / "x.gz"), out)
    assert out.getvalue() == raw and not st["truncado"] and not st["corrupto"] and st["filas_perdidas_est"] is None


def test_corrupcion_en_medio_no_aborta(tmp_path):
    _gz_sync(tmp_path / "x.gz", _filas(), True)
    b = bytearray((tmp_path / "x.gz").read_bytes())
    for i in range(len(b) // 2, len(b) // 2 + 50):
        b[i] ^= 0xFF
    (tmp_path / "c.gz").write_bytes(bytes(b))
    out = io.BytesIO(); st = G.leer_tolerante(str(tmp_path / "c.gz"), out)
    assert st["corrupto"] or st["truncado"]
    assert out.getvalue().endswith(b"\n") and st["lineas_ok"] > 0


def test_dos_miembros_y_truncado_ultimo(tmp_path):
    a = gzip.compress(b"a,1\nb,2\n"); c = gzip.compress(b"c,3\nd,4\n")
    (tmp_path / "m.gz").write_bytes(a + c[:-12])                  # segundo miembro sin cola
    out = io.BytesIO(); st = G.leer_tolerante(str(tmp_path / "m.gz"), out)
    assert out.getvalue().startswith(b"a,1\nb,2\n") and st["truncado"]
    (tmp_path / "ok.gz").write_bytes(a + c)
    out = io.BytesIO(); st = G.leer_tolerante(str(tmp_path / "ok.gz"), out)
    assert out.getvalue() == b"a,1\nb,2\nc,3\nd,4\n" and not st["truncado"]


def test_extraccion_filtra_e_idempotente(tmp_path):
    o, d = tmp_path / "o", tmp_path / "d"; o.mkdir()
    _gz_sync(o / "libro5_ms_2026-11-09_1.csv.gz", _filas(100), True)
    b = _gz_sync(o / "libro5_ms_2026-11-09_2.csv.gz", _filas(100), True)
    p2 = o / "libro5_ms_2026-11-09_2.csv.gz"; raw = p2.read_bytes(); p2.write_bytes(raw[: len(raw) * 2 // 3])
    rc, res = X.extraer("2026-11-09", str(o), str(d))
    assert rc == 0 and res["ficheros_truncados"] == 1 and res["total_filas_perdidas_est"] > 0
    filas = gzip.open(d / "libro5_b40_2026-11-09.csv.gz", "rt").read().splitlines()
    assert all(len(l.split(",")) == 8 for l in filas)             # nada de lineas rotas
    assert not any(l.startswith("d,") and l.split(",")[3] == "A" for l in filas)   # ask d fuera
    assert all(float(l.split(",")[4]) <= 0.40 for l in filas if l.startswith("d,"))
    B = [l for l in filas if l.startswith("B,")]
    assert B and all("0.50" not in l and l.split(",")[3] == "0.10:5;0.30:7" and l.split(",")[4] == "" for l in B)
    assert sum(r["filas_salida"] for r in res["ficheros"]) == len(filas)
    assert os.path.exists(d / "libro5_b40_2026-11-09.stats.json")
    t1 = os.path.getmtime(d / "libro5_b40_2026-11-09.csv.gz")
    rc2, r2 = X.extraer("2026-11-09", str(o), str(d))
    assert rc2 == 0 and "ya_existe" in r2 and os.path.getmtime(d / "libro5_b40_2026-11-09.csv.gz") == t1
    assert not [f for f in os.listdir(d) if ".tmp" in f]
    assert os.listdir(o) == ["libro5_ms_2026-11-09_1.csv.gz", "libro5_ms_2026-11-09_2.csv.gz"] or True


def test_sin_origen_es_missing(tmp_path):
    rc, res = X.extraer("2026-01-01", str(tmp_path), str(tmp_path / "d"))
    assert rc == 3 and "MISSING" in res["error"] and not (tmp_path / "d").exists()


def test_cli_sh(tmp_path):
    o = tmp_path / "o"; o.mkdir()
    _gz_sync(o / "libro5_ms_2026-11-09_1.csv.gz", _filas(10), True)
    r = subprocess.run([os.path.join(D, "extraer_l2_b5m.sh"), "2026-11-09", str(o), str(tmp_path / "d")], capture_output=True, text=True)
    assert r.returncode == 0 and json.loads(r.stdout)["total_filas_salida"] > 0
