#!/usr/bin/env python3
"""experimento_maker_h23.py -- H23-MAKER-V1 REAL (PAQUETE PREPARADO, NO ENVIADO). Va en la raiz de /root/polymarket-research-dev junto a
experimento_maker_h47.py (NO lo modifica: lo importa y lo extiende por subclase; el diff contra H47 es CERO lineas).

⚠️ Con --confirmo-dinero-real ENVIA ORDENES REALES con la wallet DEDICADA. Sin esa bandera es un ENSAYO EN SECO (lee solo datos publicos, simula
con el modelo CONS del harness). Puertas de Javi (19/20-Oct), TODAS exigidas por el codigo en real, fail-closed:
  1. H47-B real terminado y con veredicto de la calibracion (no lo comprueba el codigo: lo atestigua el fichero del punto 3).
  2. /code-review adversarial (medium como minimo) de ESTE fichero + test_experimento_maker_h23.py.
  3. OK FINAL de Javi: el chief crea /root/polymarket-research-datalogs/H23_OK_JAVI.txt (texto libre: fecha + motivo) y pasa --ok-final-javi "<mismo texto>".
Sin las dos cosas (fichero + bandera con el mismo texto) el real NO arranca.

POLITICA (h23_regla.py, congelada; informe v4_comprar_lo_bueno §4): par BTC 5m/15m que cierra en C (C % 900 == 0); lado s por TWAP60 oficial
(ref15 = twap60(C-900), ref5 = twap60(C-300), |gap| >= 1 bp); puja GTC POST-ONLY de compra en el 5m lado s UNIENDOSE al mejor bid mientras
querer(...) lo permita (cota bid15, p <= p_limite(bid15, umbral), margen >= -0,05, libro no cruzado, T > 10 s); se CANCELA en cuanto la condicion se
rompe. Tras cancelar hay que ASENTAR (>= 1,5 s, regla del arnes) antes de volver a pujar = variante `join_r` del shadow (su EV es el que aplica a
este ejecutor, NO el de `join`). UN relleno (aunque parcial) CIERRA la puja del mercado (como H47). Brazo A (umbral 0,05, el congelado) por defecto;
B (0,02) solo con --brazo B y ledger aparte.
LIMITES DE DINERO: los de H47 intactos (presupuesto util <= 5 USD, suelo dinamico verificado on-chain, N fijo, 5 vivas max, tope 3 USD/orden, kill
persistente, cuadre on-chain, lock de la wallet). N_MAX['H23'] = 40 mercados con intencion (~12 dias a ~3,3 cotizaciones/dia segun el replay).
Tamano: 5 acc (minimo del mercado) o ceil(1 USD/precio) como H47 (NO los 2 EUR de la simulacion: el EV por € no depende del tamano; la capacidad si).
Ledger propio `experimento_h47_H23_ledger.jsonl` (el glob `experimento_h47_*_ledger.jsonl` de H47 lo cuenta como hermano: suelo y tope total compartidos).
Uso:  .venv/bin/python experimento_maker_h23.py                       (ENSAYO EN SECO)
      .venv/bin/python experimento_maker_h23.py --confirmo-dinero-real --ok-final-javi "<texto>"   (REAL; ver puertas)
"""
import argparse
import json
import math
import os
import sys
import time
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
sys.path.insert(0, str(AQUI / "experimentos/5m_barato/h23_maker"))      # h23_regla (fuente unica de la regla)
import experimento_maker_h47 as H   # noqa: E402
import h23_regla as R               # noqa: E402

X = H.X
OK_FICHERO = H.DATALOGS / "H23_OK_JAVI.txt"
H.N_MAX.setdefault("H23", 40)
H.K_POR_MONEDA.setdefault("btc", 0)           # H23 no usa k (join); Exp47.crear_ctx lo busca
T_STOP_H23 = float(R.CONFIG["fin_margen_s"])  # 10 s
H.LOOP_S = 0.02                               # reaccion a eventos: el arnes dormia 100 ms por vuelta (la cancelacion es el edge)
GAMMA_EV = "https://gamma-api.polymarket.com/markets"


def mercado_15m(ini):
    r = H.requests.get(GAMMA_EV, params={"slug": f"btc-updown-15m-{ini}"}, timeout=10).json()
    if not r:
        return None
    m = r[0]
    toks, outs = json.loads(m["clobTokenIds"]), json.loads(m["outcomes"])
    return {"slug": m["slug"], "id": str(m["id"]), "toks": dict(zip(outs, toks))}


def lado_por_refs(ref15, ref5):
    """'Up'|'Down'|None (gap < minimo o referencia ausente). Fuente unica: h23_regla."""
    return R.lado_de_refs(ref15, ref5)


def objetivo_h23(top_5, top_15, umbral):
    """Precio al que querer estar pujando AHORA o None (= no pujar / cancelar). top_*: ((bid,sz)|None, (ask,sz)|None) del libro."""
    (b5, a5), (b15, a15) = top_5, top_15
    return R.querer(b5[0] if b5 else None, a5[0] if a5 else None, b15[0] if b15 else None, a15[0] if a15 else None, umbral)


class Ctx23(H.Ctx):
    def __init__(self, coin, mk, lib, k, mk15):
        super().__init__(coin, mk, lib, k)
        t15 = mk15["toks"]
        self.up15, self.dn15 = t15.get("Up") or t15.get("Yes"), t15.get("Down") or t15.get("No")
        self.s = self.tc = self.to = None
        self.mk15 = mk15


class Exp23(H.Exp47):
    def __init__(self, real, brazo="A", n_max=None, size=5, min_nocional=1.0, presupuesto=H.PRESUPUESTO_UTIL, max_vivas=H.MAX_VIVAS, refs=None):
        if brazo not in R.CONFIG["brazos"]:
            sys.exit(f"--brazo debe ser uno de {tuple(R.CONFIG['brazos'])}")
        self.brazo, self.umbral, self.refs = brazo, R.CONFIG["brazos"][brazo], refs
        super().__init__(real, "H23", n_max, T_STOP_H23, size, min_nocional, ("btc",), presupuesto, max_vivas)

    # ---- descubrimiento: solo el 5m que cierra con su 15m (C % 900 == 0)
    def lanzar_mercados(self, ahora):
        if self.parada or self.kill or self.senal or self.n_usadas() >= self.n_max:
            return
        c = (int(ahora // 900) + 1) * 900
        if not (c - 300 - 60 <= ahora < c - self.t_stop - 30):
            return
        slug = f"btc-updown-5m-{c - 300}"
        if slug in self.ctxs or ahora < self._gamma_err.get(slug, 0):
            return
        try:
            mk, mk15 = H.mercado_5m("btc", c - 300), mercado_15m(c - 900)
        except Exception as e:
            self._gamma_err[slug] = ahora + 10
            self._log47({"tipo": "gamma_error", "slug": slug, "e": str(e)[:160]})
            return
        if not mk or not mk15:
            self._gamma_err[slug] = ahora + 10
            return
        cx = self.crear_ctx("btc", mk, mk15)
        self.ctxs[slug] = cx if cx is not None else "saltado"

    def crear_ctx(self, coin, mk, mk15=None):
        if mk15 is None:
            return None
        base = super().crear_ctx(coin, mk)                  # valida tokens/slug usado/tick 0,01; abre un Libro 5m que se sustituye
        if base is None:
            return None
        base.lib.parar = True
        try:
            toks = [base.up, base.dn] + [t for t in (mk15["toks"].get("Up"), mk15["toks"].get("Down")) if t]
            lib = X.Libro(toks, registrar_trades=True)
        except Exception as ex:
            self._log47({"tipo": "ws_no_conecta_salto", "slug": mk["slug"], "e": str(ex)[:160]})
            return None
        return Ctx23(coin, mk, lib, 0, mk15)

    def _fijar_lado(self, c):
        if c.s is not None or self.refs is None:
            return
        r15, r5 = self.refs.get(c.mk["fin"] - 900), self.refs.get(c.mk["fin"] - 300)
        if not (r15 and r5):
            return
        s = lado_por_refs(r15[0], r5[0])
        self._log47({"tipo": "par_refs", "slug": c.mk["slug"], "ref15": r15[0], "ref5": r5[0], "lado": s, "leida_ms": r5[1]})
        if s is None:
            c.s = "descartado"
            return
        c.s = s
        c.tc, c.to = (c.up, c.up15) if s == "Up" else (c.dn, c.dn15)

    def elegir_cara(self, c):
        return c.tc

    def _objetivo(self, c):
        if c.s in (None, "descartado") or c.tc is None:
            return None
        if time.time() < c.mk["fin"] - 300 + R.CONFIG["ref_conocible_ms"] / 1000.0:
            return None
        return objetivo_h23(c.lib.top(c.tc), c.lib.top(c.to), self.umbral)

    def decidir(self, c, T, ahora):
        self._fijar_lado(c)
        self.sincronizar_rellenos(c)
        if c.tc is None:
            return
        tok = c.tc
        e = c.estado[tok]
        o = self.vivas.get(e["oid"]) if e["oid"] else None
        if e["cerrado"] or e["llenas"] > 1e-9:                       # un relleno (aunque parcial) cierra la puja
            e["cerrado"] = True
            c.fin_puja = c.fin_puja or "relleno"
            if o is not None and self.cancelar(e["oid"]):
                self.liquidar(e["oid"], o, True, c.estado, c.lib, T)
                e["oid"] = None
            return
        objetivo = self._objetivo(c) if c.lib.fresco() else None      # libro no fresco = sin vista = cancelar (fail-closed)
        if o is not None:
            if objetivo is not None and abs(objetivo - float(o["precio"])) < 1e-9:
                return
            h = e["oid"]                                              # condicion rota o el bid se movio: CANCELAR YA (sin limite de cadencia)
            if self.cancelar(h):
                c.t_accion = time.time()
                self.liquidar(h, o, True, c.estado, c.lib, T)
                self._log47({"tipo": "h23_cancela", "slug": c.mk["slug"], "de": o["precio"], "objetivo": objetivo, "T": round(T, 2),
                             "causa": "condicion" if objetivo is None else "bid_cambia"})
                e["oid"] = None
                if e["llenas"] > 1e-9:
                    e["cerrado"] = True
            return
        # ---- sin orden viva: ¿pujar? (mismos topes que H47)
        if objetivo is None or self.parada or self.kill or self.senal:
            return
        if any(x["tok"] == tok for x in self.canceladas.values()):
            return                                                    # cancelada sin asentar: no se repone todavia (>= 1,5 s)
        if time.time() < self.enfriar_tok.get(tok, 0) or ahora - c.t_accion < H.MIN_ENTRE_ACCIONES_S:
            return
        if c.mk["slug"] not in self.slugs_usados:
            if self.n_usadas() >= self.n_max or len(self.pujas_en_libro() - {c.mk["slug"]}) >= self.max_vivas:
                return
        if len(self.vivas) + len(self.canceladas) >= self.max_vivas:
            return
        if c.n_ord >= min(R.CONFIG["max_cotiz_por_mercado"], H.MAX_ORDENES_PUJA) or self.n_ordenes_total >= H.MAX_ORDENES_TOTAL:
            c.fin_puja = c.fin_puja or "tope_ordenes"
            e["cerrado"] = True
            return
        size = H.tamano_orden(objetivo, self.size, self.min_nocional)
        if size is None:
            self._bloqueo(("tam", objetivo), {"tipo": "bloqueo_tamano", "precio": objetivo})
            return
        mn = c.mk.get("min_size")
        if mn is not None and size < float(mn) - 1e-9:
            self._bloqueo(("minsize",), {"tipo": "bloqueo_min_size_mercado", "min": mn, "size": size})
            return
        if not self.puede_enviar(size * objetivo):
            return
        if c.mk["fin"] - time.time() <= self.t_stop + 2 or c.lib.tick_cambiado:
            return
        b, a = c.lib.top(tok)
        cola_dec = c.lib.tamano_nivel(tok, objetivo)
        n_ev = len(X.leer_ledger())
        h = self.post(c.mk["slug"], tok, c.lados[tok], objetivo, size, cola_dec, lib=c.lib, ajeno_dec=c.lib.mejor_bid_ajeno(tok),
                      ask_dec=a[0] if a else None, fin=c.mk["fin"])
        c.t_accion = time.time()
        if h is not None or any(ev.get("tipo") == "intencion_post" and ev.get("slug") == c.mk["slug"] for ev in X.leer_ledger()[n_ev:]):
            self.slugs_usados.add(c.mk["slug"])
            c.tok = c.tok or tok
        if h is None:
            return
        e["oid"] = h
        c.hashes.append(h)
        c.n_ord += 1
        c.posteado = True
        b15 = c.lib.top(c.to)[0]
        self._log47({"tipo": "puja_post", "oid": h, "slug": c.mk["slug"], "coin": "btc", "lado": c.lados[tok], "brazo": self.brazo, "precio": objetivo,
                     "size": size, "cola": cola_dec, "libro": self._libro5(c.lib, tok), "bid15": b15[0] if b15 else None,
                     "T": round(c.mk["fin"] - time.time(), 2), "n_orden": c.n_ord, "variante": f"H23-{self.brazo}", "t_dec": ahora,
                     "hash_regla": R.hash_config()})
        if c.libro_dec is None:
            c.libro_dec = self._libro5(c.lib, tok)


def exigir_puertas(real, ok_final):
    """Real SOLO con el fichero de OK de Javi y la bandera con su MISMO texto (fail-closed). Devuelve None si no es real."""
    if not real:
        return
    if not ok_final or not ok_final.strip():
        sys.exit("real exige --ok-final-javi con el texto del OK final de Javi")
    if not OK_FICHERO.exists():
        sys.exit(f"falta {OK_FICHERO} (lo crea el chief tras el OK FINAL de Javi, H47-B y el /code-review): no se envia nada")
    if OK_FICHERO.read_text().strip() != ok_final.strip():
        sys.exit("el texto de --ok-final-javi no coincide con el fichero de OK")


def configurar_rutas(real, brazo):
    esc = "H23" if brazo == "A" else "H23B"
    H.configurar_rutas(real, esc, T_STOP_H23)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--brazo", default="A", choices=tuple(R.CONFIG["brazos"]))
    ap.add_argument("--n", type=int, default=None, help="mercados con intencion (<= N_MAX['H23'] = 40)")
    ap.add_argument("--confirmo-dinero-real", action="store_true")
    ap.add_argument("--ok-final-javi", default=None)
    ap.add_argument("--size", type=int, default=5)
    ap.add_argument("--min-nocional", type=float, default=1.0)
    ap.add_argument("--presupuesto-util", type=float, default=H.PRESUPUESTO_UTIL)
    ap.add_argument("--max-vivas", type=int, default=2)
    ap.add_argument("--duracion-max-min", type=float, default=None)
    a = ap.parse_args(argv)
    real = a.confirmo_dinero_real
    exigir_puertas(real, a.ok_final_javi)
    if a.brazo == "B":
        H.N_MAX["H23B"] = H.N_MAX["H23"]
    configurar_rutas(real, a.brazo)
    if real:
        _ = H.tomar_lock_pares()
    sys.path.insert(0, str(AQUI / "experimentos/5m_barato/h23_maker"))
    import h23_shadow as S                       # Refs (solo lectura del CSV de PolyBolt)
    refs = S.Refs()
    ex = Exp23(real, a.brazo, a.n, a.size, a.min_nocional, a.presupuesto_util, a.max_vivas, refs=refs)
    print(f"{'REAL' if real else 'ENSAYO EN SECO'} H23 brazo {a.brazo}: N={ex.n_max} (ya usadas {ex.n_usadas()}); kill={ex.kill}; ledger {X.LEDGER}", flush=True)
    if real and ex.kill:
        sys.exit("kill pendiente: revisar y rearmar (con el rearme de H47)")
    ex.run(duracion_max_s=a.duracion_max_min * 60 if a.duracion_max_min else None)
    return 0


if __name__ == "__main__":
    sys.exit(main())
