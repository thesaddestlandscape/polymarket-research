import gzip, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import qc_l2_b5m as Q

def _fx(tmp_path, truncar=False):
    L = ["tipo,t_ms,token,c1,c2,c3,recepcion,seq",
         "B,1000,tk,0.30:10;0.31:5,0.40:7,,1001,1",
         "d,1100,tk,B,0.45,5.0,1101,2",          # bid 0.45 >= ask 0.40 -> cruzado
         "d,1200,tk,B,0.45,0.0,1201,3",
         "T,1300,tk,0.31,SELL,2,1302,4",
         "G,1400,tk,caida,,,1400,5",
         "d,1500,tk,B,0.30,9,1501,6",             # sin estado tras G: ignorada
         "d,1600,tk,B,0.30,9,1601,6"]             # seq repetida -> no monotona
    p = tmp_path / "libro5_ms_2026-11-09_1.csv.gz"
    raw = ("\n".join(L) + "\n").encode()
    if truncar:
        import zlib
        co = zlib.compressobj(wbits=31); data = co.compress(raw) + co.flush(zlib.Z_SYNC_FLUSH)
        p.write_bytes(data)                       # sin cierre del miembro gzip = truncado
    else:
        with gzip.open(p, "wb") as f: f.write(raw)
    return str(p)

def test_qc_cuenta_tipos_cruzados_huecos_seq(tmp_path):
    r, ts = Q.qc_fichero(_fx(tmp_path))
    assert r["filas"] == {"B": 1, "d": 4, "T": 1, "G": 1}
    assert r["libros_cruzados_tras_d"] == 1 and r["huecos_G"] == {"caida": 1}
    assert r["seq_no_monotona"] == 1 and r["tokens_con_B"] == 1 and not r["truncado"]
    assert ts == [("tk", 1300)]

def test_qc_tolera_truncado(tmp_path):
    r, _ = Q.qc_fichero(_fx(tmp_path, truncar=True))
    assert r["truncado"] and r["filas"]["B"] == 1

def test_cobertura_tx(tmp_path):
    f = tmp_path / "libro5_tx_2026-11-09_1.csv"; f.write_text("1302,tk,0xabc,1330\n")
    assert Q.cobertura_tx([str(f)], [("tk", 1300)])["frac"] == 1.0
    assert Q.cobertura_tx([str(f)], [("otro", 1300)])["frac"] == 0.0
    assert Q.cobertura_tx([str(f)], []) is None
