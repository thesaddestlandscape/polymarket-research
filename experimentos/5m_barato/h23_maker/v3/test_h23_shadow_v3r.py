#!/usr/bin/env python3
"""Tests del transporte robusto y multimoneda del shadow H23 (h23_shadow_v3r.py + h23_ws_lector.py). Sin red de produccion (servidor WS local), sin disco de produccion.
Desde este directorio: python3 -m pytest -q test_h23_shadow_v3r.py
Cubre: EQUIVALENCIA de decisiones con el shadow v3 (mismo flujo de mensajes -> mismas filas), orden por reloj logico (comandos vs tramas), hueco por conexion (solo limpia SUS tokens),
cierre del hueco por snapshot, fila ws_pair, registro propio (q solo si cambia, snapshots, trades, g/c, foto de estado), hijo lector real contra un servidor local (reconexion tras 1013,
fin de grupo, desbordamiento de cola = hueco explicito), particion de tokens, restauracion de moneda, reinicio idempotente."""
import asyncio, gzip, json, os, pickle, struct, subprocess, sys, time
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import numpy as np
import pytest
import h23_regla_v3 as R
import h23_shadow_v3 as V3
import h23_shadow_v3r as S

C = 1_800_000_000
U5, D5, U15, D15 = "u5", "d5", "u15", "d15"
TOKS = [U5, D5, U15, D15]
M5, M15 = {"id": "m5", "up": U5, "down": D5}, {"id": "m15", "up": U15, "down": D15}


def ms(T):
    return int(round((C - T) * 1000))


def msg_book(tk, b, bs, a, as_, ts):
    return json.dumps({"event_type": "book", "asset_id": tk, "timestamp": str(ts), "bids": [{"price": str(b), "size": str(bs)}], "asks": [{"price": str(a), "size": str(as_)}]})


def msg_pc(entries, ts):
    return json.dumps({"event_type": "price_change", "timestamp": str(ts), "price_changes": entries})


def msg_trade(tk, price, side, size, ts):
    return json.dumps({"event_type": "last_trade_price", "asset_id": tk, "price": str(price), "side": side, "size": str(size), "timestamp": str(ts)})


def nuevo_tp(topologia=4, registro=None):
    rows = []
    nuc = S.NucleoR(rows.append)
    tp = S.Transporte(nuc, topologia=topologia, registro=registro)
    return tp, nuc, rows


def abrir(tp, ts=None, coin="BTC"):
    ts = ts if ts is not None else ms(370)
    box = {}

    def f(t):
        p, info, toks, gr = tp.abrir_par(t, coin, C, M5, M15)
        info.slot_de = {U5: "0", D5: "1", U15: "2", D15: "3"}
        if tp.reg is not None:
            info.reg_idx = C
        box.update(p=p, info=info)
    tp.cmd(f, ts)
    tp.frames.append(("h", ts, None, None, None))
    tp.pump()
    return box["p"], box["info"]


def h(tp, t):
    tp.frames.append(("h", t, None, None, None))
    tp.pump()


def fr(tp, kind, t, grp, payload, pair="m5"):
    tp.frames.append((kind, t, pair, grp, payload))
    tp.pump()


def lado(tp, p, ts=None):
    ts = ts if ts is not None else ms(298.4)
    tp.cmd(lambda t: tp.nuc.fijar_lado(p, 100.0, 99.9, t), ts)
    h(tp, ts + 10)


def tipos(rows, t, **kw):
    return [r for r in rows if r["tipo"] == t and all(r.get(k) == v for k, v in kw.items())]


# ---------------------------------------------------------------------------------------------------------------------
def test_particion():
    assert S.particion(4, TOKS) == [[U5], [D5], [U15], [D15]]
    assert S.particion(2, TOKS) == [[U5, D5], [U15, D15]]
    assert S.particion(1, TOKS) == [TOKS]


def test_regla_y_hash_intactos():
    assert R.hash_config() == "3eeff503cf0a75c9" and S.R is R and S.V3.Nucleo is not None
    assert issubclass(S.NucleoR, V3.Nucleo)
    assert S.RefsMon.__mro__[1] is V3.Refs


# ---------------------------------------------------------------------------------------------------------------------
def _escenario(rng, n_ev=40):
    """Lista de mensajes crudos (ts, texto) de un par: 4 snapshots y luego price_change (todos los tokens en UN mensaje, como el servidor para un mercado) y operaciones SELL del 5m."""
    ts_all = sorted(set(int(ms(295) + x) for x in rng.integers(0, 270_000, n_ev)))
    out = []
    t0 = ms(299)
    for tk, (b, bs, a, as_) in {D5: (0.60, 10, 0.70, 10), D15: (0.50, 10, 0.54, 10), U15: (0.40, 80, 0.44, 80), U5: (0.30, 100, 0.33, 50)}.items():
        out.append((t0, msg_book(tk, b, bs, a, as_, t0)))
    cur = {(U5, "BUY"): (0.30, 100.0), (U5, "SELL"): (0.33, 50.0), (U15, "BUY"): (0.40, 80.0), (U15, "SELL"): (0.44, 80.0),
           (D5, "BUY"): (0.60, 10.0), (D5, "SELL"): (0.70, 10.0), (D15, "BUY"): (0.50, 10.0), (D15, "SELL"): (0.54, 10.0)}
    for t in ts_all:
        if rng.random() < 0.25:
            out.append((t, msg_trade(U5, round(float(rng.choice([0.28, 0.30, 0.31, 0.33])), 2), "SELL", float(rng.integers(1, 12)), t)))
            continue
        b5 = round(float(rng.choice([0.26, 0.28, 0.30, 0.31, 0.32])), 2)
        b15 = round(float(rng.choice([0.34, 0.36, 0.40, 0.45, 0.48])), 2)
        new = {(U5, "BUY"): (b5, float(rng.integers(1, 200))), (U5, "SELL"): (round(b5 + 0.03, 2), 50.0), (U15, "BUY"): (b15, 80.0), (U15, "SELL"): (round(b15 + 0.02, 2), 80.0)}
        ent = []
        for (tk, side), (px, sz) in new.items():
            ant = cur[(tk, side)]
            if ant[0] != px:
                ent.append({"asset_id": tk, "side": side, "price": str(ant[0]), "size": "0"})
            if ant != (px, sz) or ant[0] != px:
                ent.append({"asset_id": tk, "side": side, "price": str(px), "size": str(sz)})
            cur[(tk, side)] = (px, sz)
        if ent:
            out.append((t, msg_pc(ent, t)))
    return out


def _por_v3(msgs):
    """Referencia: el bucle de mensajes de h23_shadow_v3.vigilar aplicado a mano sobre el Nucleo de v3."""
    rows = []
    n = V3.Nucleo(rows.append)
    p = n.nuevo_par(C, M5, M15, ms(370))
    lado_hecho = False
    for t, raw in msgs:
        if not lado_hecho and t > ms(298.4):                       # el lado se fija a su hora, entre mensajes (a igual hora, primero el comando)
            n.fijar_lado(p, 100.0, 99.9, ms(298.4))
            lado_hecho = True
        for m in [json.loads(raw)]:
            et = m.get("event_type")
            if et == "price_change":
                n.on_price_change(t, m.get("price_changes") or [])
            elif et == "last_trade_price":
                n.on_trade(m["asset_id"], t, m)
            elif et == "book":
                n.on_book(m["asset_id"], t, m.get("bids"), m.get("asks"))
    n.cerrar_par("m5", ms(-0.5))
    return rows


def _por_v3r(msgs, ticks=False):
    old = S.HB_TICK_MS
    S.HB_TICK_MS = old if ticks else 10 ** 12                     # la referencia (bucle de v3 sin silencios) no hace ticks de tiempo
    try:
        return _por_v3r_(msgs)
    finally:
        S.HB_TICK_MS = old


def _por_v3r_(msgs):
    tp, nuc, rows = nuevo_tp(topologia=1)
    p, info = abrir(tp)
    tp.cmd(lambda t: tp.nuc.fijar_lado(p, 100.0, 99.9, t), ms(298.4))
    for t, raw in msgs:
        fr(tp, "m", t, 0, raw)
    tp.cmd(lambda t: tp.cerrar_par_cmd(t, "m5", False), ms(-0.5))
    h(tp, ms(-0.6))
    return rows


def _norm(rows):
    out = []
    for r in rows:
        if r["tipo"] == "ws_pair":
            continue
        r = {k: v for k, v in r.items() if k not in ("coin", "tr")}
        out.append(r)
    return out


@pytest.mark.parametrize("seed", range(12))
def test_equivalencia_de_decisiones_con_v3(seed):
    """Topologia 1 (todos los tokens en una conexion) + reloj logico = EXACTAMENTE las mismas filas que el shadow v3 con el mismo flujo."""
    msgs = _escenario(np.random.default_rng(seed))
    a, b = _norm(_por_v3(msgs)), _norm(_por_v3r(msgs))
    assert a == b
    assert any(r["tipo"] == "relleno_resumen" for r in b)


def test_topologia_4_mismo_estado_final_que_topologia_1():
    """Con una conexion por token (mensajes partidos por token, misma hora) el libro final y los rellenos coinciden; solo pueden diferir estados transitorios intermedios."""
    rng = np.random.default_rng(3)
    msgs = _escenario(rng)
    tp, nuc, rows = nuevo_tp(topologia=4)
    p, info = abrir(tp)
    lado(tp, p)
    for t, raw in msgs:
        m = json.loads(raw)
        if m["event_type"] == "price_change":
            for g, tk in enumerate(TOKS):
                ents = [e for e in m["price_changes"] if e["asset_id"] == tk]
                if ents:
                    fr(tp, "m", t, g, msg_pc(ents, t))
        else:
            g = TOKS.index(m["asset_id"])
            fr(tp, "m", t, g, raw)
    tp1, nuc1, rows1 = nuevo_tp(topologia=1)
    p1, _ = abrir(tp1)
    lado(tp1, p1)
    for t, raw in msgs:
        fr(tp1, "m", t, 0, raw)
    for tk in TOKS:
        assert p.lib[tk].bids == p1.lib[tk].bids and p.lib[tk].asks == p1.lib[tk].asks
    assert len(tipos(rows, "puesto")) >= 1


def test_price_change_de_otro_token_se_filtra_por_conexion():
    """Si el servidor mandase entradas de otros tokens por una conexion, no se aplican dos veces ni se aplican fuera de su grupo."""
    tp, nuc, rows = nuevo_tp(topologia=4)
    p, info = abrir(tp)
    fr(tp, "m", ms(300), 0, msg_book(U5, 0.30, 100, 0.33, 50, ms(300)))
    fr(tp, "m", ms(299.9), 0, msg_pc([{"asset_id": D5, "side": "BUY", "price": "0.61", "size": "5"}], ms(299.9)))
    assert 0.61 not in p.lib[D5].bids


# ---------------------------------------------------------------------------------------------------------------------
def test_comando_espera_al_reloj_del_hijo_y_respeta_el_orden():
    tp, nuc, rows = nuevo_tp(topologia=1)
    orden = []
    tp.cmd(lambda t: orden.append(("cmd", t)), 1000)
    assert orden == []                                  # el reloj (wm=0) aun no ha pasado 1000
    tp.frames.append(("h", 900, None, None, None)); tp.pump()
    assert orden == []
    tp.frames.append(("h", 1100, None, None, None)); tp.pump()
    assert orden == [("cmd", 1000)]
    # una trama con hora anterior a un comando se procesa ANTES que el comando aunque llegue despues al pipe
    tp.cmd(lambda t: orden.append(("cmd2", t)), 2000)
    tp.frames.append(("p", 1500, "x", 0, None)); tp.frames.append(("p", 2500, "x", 0, None)); tp.pump()
    assert orden[-1] == ("cmd2", 2000)


def test_hueco_de_una_conexion_limpia_solo_sus_tokens_y_se_cierra_con_el_snapshot():
    tp, nuc, rows = nuevo_tp(topologia=4)
    p, info = abrir(tp)
    lado(tp, p)
    for g, (tk, b, a) in enumerate(((U5, 0.30, 0.33), (D5, 0.60, 0.70), (U15, 0.45, 0.47), (D15, 0.50, 0.54))):
        fr(tp, "m", ms(290) + g, g, msg_book(tk, b, 100, a, 50, ms(290)))
    assert all(p.lib[t].vivo for t in TOKS) and len(tipos(rows, "puesto", arm="A", var="join")) == 1
    fr(tp, "g", ms(250), 2, "ConnectionClosedError: received 1013 (try again later) slow consumer")       # cae el 15m up
    assert p.lib[U15].vivo is False and p.lib[U5].vivo and p.lib[D5].vivo and p.lib[D15].vivo
    assert tipos(rows, "cancela", arm="A", var="join")[0]["causa"] == "gap"
    assert p.reconex == 1 and info.caidas == 1 and 2 in info.hueco_abierto
    fr(tp, "c", ms(249.9), 2, 1)
    fr(tp, "m", ms(249.8), 2, msg_book(U15, 0.45, 100, 0.47, 50, ms(249.8)))
    assert p.lib[U15].vivo and info.hueco_abierto == {} and len(info.huecos) == 1
    a, b, g = info.huecos[0]
    assert (a, b, g) == (ms(250), ms(249.8), 2)
    # con el hueco cerrado, la cotizacion se reanuda (puesto nuevo)
    assert len(tipos(rows, "puesto", arm="A", var="join")) == 2
    h(tp, ms(249.7))
    tp.cmd(lambda t: tp.cerrar_par_cmd(t, "m5", False), ms(-0.5))
    h(tp, ms(-0.6))
    ws = tipos(rows, "ws_pair")[0]
    assert ws["caidas"] == 1 and ws["hueco_ms"] == 200 and ws["hueco_en_ventana_ms"] == 200 and ws["hueco_max_ms"] == 200 and ws["huecos_abiertos_al_cierre"] == 0
    assert ws["topologia"] == 4 and ws["n_grupos"] == 4
    fin = tipos(rows, "mercado_fin")[0]
    assert fin["completo"] is False and fin["reconex"] == 1                                        # criterio estricto de v3 intacto: cualquier caida = no completo
    assert all(r.get("coin") == "BTC" and r["tr"] == "v3r" for r in rows if r.get("mkt"))


def test_hueco_abierto_al_cierre_se_cuenta_y_no_se_oculta():
    tp, nuc, rows = nuevo_tp(topologia=4)
    p, info = abrir(tp)
    lado(tp, p)
    fr(tp, "g", ms(100), 0, "hijo_muerto")
    tp.cmd(lambda t: tp.cerrar_par_cmd(t, "m5", False), ms(-0.5))
    h(tp, ms(-0.6))
    ws = tipos(rows, "ws_pair")[0]
    assert ws["huecos_abiertos_al_cierre"] == 1 and ws["hueco_ms"] == ms(-0.5) - ms(100)


def test_pong_mantiene_vivo_el_par():
    tp, nuc, rows = nuevo_tp(topologia=4)
    p, info = abrir(tp)
    p.ult_msg = ms(299)
    fr(tp, "p", ms(296), 0, None)
    assert p.ult_msg == ms(296)


def test_tick_tras_1s_sin_mensajes():
    tp, nuc, rows = nuevo_tp(topologia=1)
    p, info = abrir(tp)
    lado(tp, p)
    fr(tp, "m", ms(299), 0, msg_book(U5, 0.30, 100, 0.33, 50, ms(299)))
    llamadas = []
    orig = nuc.tick
    nuc.tick = lambda t: (llamadas.append(t), orig(t))
    h(tp, ms(299) + 500)
    assert llamadas == []
    h(tp, ms(299) + 2000)
    assert llamadas == [ms(299) + 2000]
    h(tp, ms(299) + 2300)
    assert len(llamadas) == 1                                                                    # no mas de uno por segundo


# ---------------------------------------------------------------------------------------------------------------------
def _gz_lineas(f):
    import zlib
    data = open(f, "rb").read()
    res = []
    while data:
        d = zlib.decompressobj(31)
        try:
            txt = d.decompress(data)
        except zlib.error:
            break
        res += txt.decode().splitlines()
        data = d.unused_data
        if not d.eof:
            break
    return res


def test_registro_propio(tmp_path):
    reg = S.RegistroPares(tmp_path, 7)
    tp, nuc, rows = nuevo_tp(topologia=4, registro=reg)
    box = {}

    def f(t):
        p, info, toks, gr = tp.abrir_par(t, "BTC", C, M5, M15)
        info.slot_de = {U5: "0", D5: "1", U15: "2", D15: "3"}
        info.reg_idx = C
        reg.put("BTC", t, f"P,{C},m5,m15,{U5},{D5},{U15},{D15},BTC,{t - C * 1000}")
        box["p"], box["info"] = p, info
    tp.cmd(f, ms(370)); h(tp, ms(369))
    p, info = box["p"], box["info"]
    lado(tp, p)
    fr(tp, "c", ms(309), 0, 1)
    fr(tp, "m", ms(309), 0, msg_book(U5, 0.30, 100, 0.33, 50, ms(309.01)))
    fr(tp, "m", ms(308), 0, msg_pc([{"asset_id": U5, "side": "BUY", "price": "0.30", "size": "100"}], ms(308)))            # mismo top -> no se escribe
    fr(tp, "m", ms(307), 0, msg_pc([{"asset_id": U5, "side": "BUY", "price": "0.30", "size": "90"}], ms(307.005)))            # tamano cambia -> q
    fr(tp, "m", ms(306), 0, msg_trade(U5, 0.30, "SELL", 5, ms(306)))
    fr(tp, "g", ms(250), 0, "x,y")
    tp.cmd(tp.foto_estado, ms(310), "m5")                                                           # foto tardia: no debe romper
    h(tp, ms(249))
    reg.cerrar()
    lns = _gz_lineas(os.path.join(tmp_path, f"h23_pares_BTC_{V3._dia(ms(300))}.csv.gz"))
    assert lns[0].startswith(f"P,{C},m5,m15,{U5}")
    q = [l for l in lns if l.startswith("q,")]
    assert q[0] == f"q,{C},0,{ms(309) - C*1000},-10,0.3,0.33,100.0,50.0,b"                          # snapshot del servidor: q con src b y ev-recv=+10... ver abajo
    assert q[1].endswith(",90.0,50.0,p") and len([l for l in q if l.endswith(",p")]) == 1
    assert [l for l in lns if l.startswith("t,")] == [f"t,{C},0,{ms(306) - C*1000},0,0.3,SELL,5"]
    assert [l for l in lns if l.startswith("g,")] == [f"g,{C},0,{ms(250) - C*1000},x;y"]
    assert [l for l in lns if l.startswith("c,")] == [f"c,{C},0,{ms(309) - C*1000}"]


# ---------------------------------------------------------------------------------------------------------------------
def test_restaurar_monedas_e_idempotencia(tmp_path):
    out = V3.Salida(tmp_path)
    nuc = S.NucleoR(out.put)
    nuc.coin_de["m5"] = "ETH"
    nuc.emit({"k": "x|1", "tipo": "par", "mkt": "m5", "r": ms(100)})
    out.cerrar()
    assert S.restaurar_monedas(tmp_path, ms(100) / 1000) == {"m5": "ETH"}
    em, rec = V3.restaurar(tmp_path, ms(100) / 1000)
    assert "x|1" in em
    nuc2 = S.NucleoR(lambda r: None, em, rec)
    assert nuc2.emit({"k": "x|1", "tipo": "par", "mkt": "m5"}) is False and nuc2.stats["duplicado_evitado"] == 1


# ---------------------------------------------------------------------------------------------------------------------
# Hijo lector REAL contra un servidor WS local
def _lanzar_hijo(url, extra_env=None):
    env = dict(os.environ, H23_WS_URL=url, **(extra_env or {}))
    return subprocess.Popen([sys.executable, "-I", os.path.join(HERE, "h23_ws_lector.py"), "--hijo"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, env=env)


def _frames(proc, hasta, timeout=15):
    """Lee tramas hasta que `hasta(frames)` o timeout."""
    out = []
    t0 = time.time()
    import select
    buf = b""
    while time.time() - t0 < timeout:
        r, _, _ = select.select([proc.stdout], [], [], 0.2)
        if not r:
            continue
        chunk = os.read(proc.stdout.fileno(), 1 << 20)
        if not chunk:
            break
        buf += chunk
        while len(buf) >= 4:
            n = struct.unpack("<I", buf[:4])[0]
            if len(buf) < 4 + n:
                break
            out.append(pickle.loads(buf[4:4 + n]))
            buf = buf[4 + n:]
        if hasta(out):
            break
    return out


def _servidor(handler):
    import websockets

    async def arranque():
        srv = await websockets.serve(handler, "127.0.0.1", 0)
        return srv, srv.sockets[0].getsockname()[1]
    return arranque


def _con_servidor(handler, cuerpo):
    """Ejecuta `cuerpo(url)` (bloqueante, en un hilo) mientras un servidor websockets local corre en el bucle de este hilo."""
    import threading
    res = {}

    async def main():
        srv, port = await _servidor(handler)()
        loop = asyncio.get_running_loop()
        res["v"] = await loop.run_in_executor(None, cuerpo, f"ws://127.0.0.1:{port}")
        srv.close()
        await srv.wait_closed()
    asyncio.run(main())
    return res["v"]


def test_hijo_entrega_mensajes_con_hora_de_recepcion_y_latidos():
    async def handler(ws):
        sub = json.loads(await ws.recv())
        assert sub["type"] == "market" and sub["assets_ids"] == ["a"]
        await ws.send(msg_book("a", 0.3, 10, 0.33, 10, 1))
        await ws.send("PONG")
        await ws.send(msg_trade("a", 0.3, "SELL", 2, 2))
        await asyncio.sleep(3)

    def cuerpo(url):
        p = _lanzar_hijo(url)
        t_envio = int(time.time() * 1000)
        p.stdin.write((json.dumps({"op": "sub", "pair": "P", "grp": 0, "tokens": ["a"], "fin_ms": t_envio + 2500}) + "\n").encode()); p.stdin.flush()
        fr_ = _frames(p, lambda fs: any(f[0] == "f" for f in fs), 10)
        p.stdin.write(b'{"op":"exit"}\n'); p.stdin.flush(); p.wait(5)
        return fr_, t_envio
    fr_, t_envio = _con_servidor(handler, cuerpo)
    kinds = [f[0] for f in fr_]
    assert kinds.count("c") == 1 and kinds.count("m") == 2 and kinds.count("p") == 1 and kinds.count("f") == 1 and kinds.count("h") >= 20
    ms_ = [f for f in fr_ if f[0] == "m"]
    assert all(t_envio - 50 <= f[1] <= t_envio + 6000 for f in ms_) and ms_[0][2] == "P" and "book" in ms_[0][4]
    ts = [f[1] for f in fr_]
    assert ts == sorted(ts)                                                                       # el reloj del hijo es monotono en la trama


def test_hijo_reconecta_tras_1013_y_marca_el_hueco():
    cuenta = {"n": 0}

    async def handler(ws):
        await ws.recv()
        cuenta["n"] += 1
        await ws.send(msg_book("a", 0.3, 10, 0.33, 10, cuenta["n"]))
        if cuenta["n"] == 1:
            await ws.close(code=1013, reason="slow consumer")
            return
        await asyncio.sleep(3)

    def cuerpo(url):
        p = _lanzar_hijo(url)
        t = int(time.time() * 1000)
        p.stdin.write((json.dumps({"op": "sub", "pair": "P", "grp": 1, "tokens": ["a"], "fin_ms": t + 2000}) + "\n").encode()); p.stdin.flush()
        fr_ = _frames(p, lambda fs: any(f[0] == "f" for f in fs), 10)
        p.stdin.write(b'{"op":"exit"}\n'); p.stdin.flush(); p.wait(5)
        return fr_
    fr_ = _con_servidor(handler, cuerpo)
    k = [f[0] for f in fr_ if f[0] in ("c", "m", "g", "f")]
    assert k[:5] == ["c", "m", "g", "c", "m"] and k[-1] == "f"
    g = [f for f in fr_ if f[0] == "g"][0]
    assert "1013" in g[4] and g[3] == 1
    c2 = [f for f in fr_ if f[0] == "c"][1]
    assert c2[1] - g[1] < 1500                                                                   # reconexion inmediata (< 1,5 s)


def test_hijo_desborda_cola_y_lo_dice():
    async def handler(ws):
        await ws.recv()
        for i in range(3000):
            await ws.send(msg_trade("a", 0.3, "SELL", 1, i))
        await asyncio.sleep(2)

    def cuerpo(url):
        p = _lanzar_hijo(url, {"H23_LECTOR_MAX_COLA": "50"})
        t = int(time.time() * 1000)
        p.stdin.write((json.dumps({"op": "sub", "pair": "P", "grp": 0, "tokens": ["a"], "fin_ms": t + 3000}) + "\n").encode()); p.stdin.flush()
        # el padre NO lee durante 1,5 s (padre lento): la cola crece en el hijo
        time.sleep(1.5)
        fr_ = _frames(p, lambda fs: any(f[0] == "f" for f in fs), 10)
        p.stdin.write(b'{"op":"exit"}\n'); p.stdin.flush(); p.wait(5)
        return fr_
    fr_ = _con_servidor(handler, cuerpo)
    n_m = sum(1 for f in fr_ if f[0] == "m")
    # con la cola de 50 y el pipe del SO lleno el hijo puede recibir todo (el pipe aguanta 64 KB) o desbordar: en AMBOS casos nada se pierde en silencio
    gaps = [f for f in fr_ if f[0] == "g"]
    assert n_m == 3000 or (gaps and any("cola_llena" in g[4] for g in gaps))


def test_transporte_integrado_con_hijo_falso(tmp_path):
    """Transporte REAL (subproceso, pickle, pipe) con un hijo falso que emite un guion: mismas filas que alimentar directamente."""
    msgs = _escenario(np.random.default_rng(5))
    guion = [("c", ms(369), "m5", 0, 1)] + [("m", t, "m5", 0, raw) for t, raw in msgs] + [("h", ms(-0.6), None, None, None)]
    fp = tmp_path / "guion.pkl"
    pickle.dump(guion, open(fp, "wb"))
    falso = tmp_path / "falso.py"
    falso.write_text("import pickle,struct,sys,time\nfor f in pickle.load(open(sys.argv[1],'rb')):\n    b=pickle.dumps(f,protocol=4); sys.stdout.buffer.write(struct.pack('<I',len(b))+b)\n"
                     "sys.stdout.buffer.flush()\nsys.stdin.read()\n")

    async def corre():
        rows = []
        nuc = S.NucleoR(rows.append)
        tp = S.Transporte(nuc, topologia=1, lector=[sys.executable, "-I", str(falso), str(fp)], nice_hijo=0)
        p, info = None, None
        box = {}

        def f(t):
            box["p"], box["info"], _, _ = tp.abrir_par(t, "BTC", C, M5, M15)
            box["info"].slot_de = {U5: "0", D5: "1", U15: "2", D15: "3"}
        tp.cmd(f, ms(370))                                       # espera a que el reloj del guion pase
        tp.cmd(lambda t: nuc.fijar_lado(box["p"], 100.0, 99.9, t), ms(298.4))
        tp.cmd(lambda t: tp.cerrar_par_cmd(t, "m5", False), ms(-0.5))
        await tp.lanzar()
        for _ in range(300):
            if tipos(rows, "mercado_fin"):
                break
            await asyncio.sleep(0.05)
        tp.parando = True
        await tp.parar()
        return rows
    rows = asyncio.run(corre())
    assert _norm(rows) == _norm(_por_v3(msgs))


# ---------------------------------------------------------------------------------------------------------------------
def test_hijo_muerto_se_relanza_marca_hueco_y_resuscribe(tmp_path):
    marca, logf = tmp_path / "murio", tmp_path / "stdin.log"
    falso = tmp_path / "falso2.py"
    falso.write_text("""import sys, os, pickle, struct, time, threading
marca, logf = sys.argv[1], sys.argv[2]
def emit(f):
    b = pickle.dumps(f, protocol=4); sys.stdout.buffer.write(struct.pack('<I', len(b)) + b); sys.stdout.buffer.flush()
primera = not os.path.exists(marca)
visto = threading.Event()
def lee():
    for ln in sys.stdin:
        open(logf, 'a').write(ln)
        visto.set()
threading.Thread(target=lee, daemon=True).start()
t_fin = time.time() + (30 if primera else 4)
while time.time() < t_fin:
    emit(('h', time.time_ns() // 1_000_000, None, None, None))
    if primera and visto.is_set():
        time.sleep(0.2); open(marca, 'w').write('x'); os._exit(1)
    time.sleep(0.05)
""")

    async def corre():
        rows = []
        nuc = S.NucleoR(rows.append)
        tp = S.Transporte(nuc, topologia=4, lector=[sys.executable, "-I", str(falso), str(marca), str(logf)], nice_hijo=0)
        await tp.lanzar()
        t0 = int(time.time() * 1000)
        box = {}

        def f(t):
            box["p"], box["info"], _, gr = tp.abrir_par(t, "BTC", C, M5, M15)
            box["info"].slot_de = {U5: "0", D5: "1", U15: "2", D15: "3"}
        tp.cmd(f, t0)
        for _ in range(100):
            if "p" in box:
                break
            await asyncio.sleep(0.05)
        assert "p" in box
        for i, g in enumerate(S.particion(4, TOKS)):
            tp.activos[("m5", i)] = (g, t0 + 60000)
            await tp._enviar({"op": "sub", "pair": "m5", "grp": i, "tokens": g, "fin_ms": t0 + 60000})
        for _ in range(200):
            if nuc.stats["hijo_relanzado"]:
                break
            await asyncio.sleep(0.05)
        await asyncio.sleep(1.0)
        tp.parando = True
        await tp.parar()
        return rows, nuc, box
    rows, nuc, box = asyncio.run(corre())
    assert nuc.stats["hijo_relanzado"] == 1
    gaps = tipos(rows, "gap")
    assert len(gaps) == 4 and {g["motivo"] for g in gaps} == {"hijo_muerto"} and {g["grp"] for g in gaps} == {0, 1, 2, 3}
    subs = [x for x in (json.loads(l) for l in open(logf)) if x['op'] == 'sub']
    assert len(subs) == 8 and sorted(s["grp"] for s in subs[4:]) == [0, 1, 2, 3]                  # las 4 suscripciones se repiten tras relanzar
    assert box["info"].caidas == 4


def test_reloj_forzado_si_el_hijo_calla():
    tp, nuc, rows = nuevo_tp(topologia=1)
    hecho = []
    tp.cmd(lambda t: hecho.append(t), V3.ahora_ms() + 100)
    assert hecho == []                                         # espera al reloj del hijo
    tp.t_frame_wall = V3.ahora_ms() - 2000                     # el hijo lleva 2 s sin tramas
    time.sleep(0.15)
    tp.vigilar_reloj()
    assert len(hecho) == 1 and nuc.stats["reloj_forzado"] == 1
