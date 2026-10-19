#!/usr/bin/env python3
"""Tests de DetectorR5K (sin red ni disco). Ejecutar: python3 -I -m unittest test_detector_r5k  (desde este directorio)."""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from detector_r5k import DetectorR5K, normalizar  # noqa: E402
from r5k_eval import unid_cosechable  # noqa: E402

CIERRE = 1_800_000_000.0                     # epoch s del cierre del mercado de prueba
TOK = {"y": ("m1", "YES", CIERRE), "n": ("m1", "NO", CIERRE)}


def recv_ms(T):                               # recepción tal que quedan T segundos
    return int((CIERRE - T) * 1000)


class TestNormalizar(unittest.TestCase):
    def test_tomador_compra_y_maker_adquiere_opuesto(self):
        self.assertEqual(normalizar("YES", "BUY", 0.80, 10.0)[:2], ("NO", 0.20))
        self.assertEqual(normalizar("NO", "BUY", 0.75, 10.0)[:2], ("YES", 0.25))

    def test_tomador_vende_y_maker_compra_el_mismo_lado(self):
        self.assertEqual(normalizar("YES", "SELL", 0.15, 10.0)[:2], ("YES", 0.15))

    def test_coste_es_acc_por_pc(self):
        _, pc, acc, coste = normalizar("YES", "BUY", 0.80, 10.0)
        self.assertAlmostEqual(coste, acc * pc)

    def test_invalidos(self):
        self.assertIsNone(normalizar("YES", "BUY", 0.5, 0))
        self.assertIsNone(normalizar("YES", "BUY", 1.0, 5))
        self.assertIsNone(normalizar("YES", "XX", 0.5, 5))
        self.assertIsNone(normalizar("YES", "BUY", None, 5))


class TestBandaYTiempo(unittest.TestCase):
    def setUp(self):
        self.d = DetectorR5K(TOK)

    def test_limites_de_banda(self):
        self.d.on_trade("y", recv_ms(200), 0.90, "BUY", 1)     # pc 0.10 -> fuera (abierto por abajo)
        self.assertEqual(len(self.d.filas), 0)
        self.d.on_trade("y", recv_ms(200), 0.70, "BUY", 1)     # pc 0.30 -> dentro (cerrado por arriba)
        self.assertEqual(len(self.d.filas), 1)
        self.d.on_trade("y", recv_ms(200), 0.69, "BUY", 1)     # pc 0.31 -> fuera
        self.assertEqual(len(self.d.filas), 1)

    def test_limites_de_tiempo(self):
        self.d.on_trade("y", recv_ms(60), 0.80, "BUY", 1)      # T=60 -> fuera (abierto)
        self.d.on_trade("y", recv_ms(60.5), 0.80, "BUY", 1)    # T=60.5 -> dentro
        self.d.on_trade("y", recv_ms(300), 0.80, "BUY", 1)     # T=300 -> dentro
        self.d.on_trade("y", recv_ms(300.5), 0.80, "BUY", 1)   # T=300.5 -> fuera
        self.assertEqual(len(self.d.filas), 2)

    def test_token_desconocido_y_mensaje_ilegible(self):
        self.assertEqual(self.d.on_trade("zz", recv_ms(100), 0.8, "BUY", 5), [])
        self.assertEqual(self.d.al_trade("y", recv_ms(100), {"price": "x"}), [])
        self.assertEqual(self.d.stats["trade_ilegible"], 1)

    def test_lados_acumulan_por_separado(self):
        self.d.on_trade("y", recv_ms(200), 0.80, "BUY", 100)   # maker adquiere NO
        self.d.on_trade("n", recv_ms(200), 0.80, "BUY", 100)   # maker adquiere YES
        self.assertEqual(self.d.cum[("m1", "NO")], 100)
        self.assertEqual(self.d.cum[("m1", "YES")], 100)


class TestCruceYCosecha(unittest.TestCase):
    def test_cruce_una_vez_y_prorrata(self):
        d = DetectorR5K(TOK)
        ev = d.on_trade("y", recv_ms(250), 0.80, "BUY", 4990)   # NO cum 4990
        self.assertEqual(ev, [])
        ev = d.on_trade("y", recv_ms(240), 0.80, "BUY", 20)     # cruza: 10 acc por encima del offset
        self.assertEqual([e["evento"] for e in ev], ["cruce"])
        st = d.estado[("m1", "NO")]
        self.assertAlmostEqual(st["take"][0][1], 10.0)           # prorrata: solo la parte por encima de 5000
        ev = d.on_trade("y", recv_ms(230), 0.80, "BUY", 100)    # no vuelve a cruzar; completa los 50
        self.assertEqual([e["evento"] for e in ev], ["cosecha_completa"])
        u = d.unidades()[("m1", "NO")]
        self.assertTrue(u["completa"])
        self.assertAlmostEqual(sum(t for _p, t, _r in u["take"]), 50.0)
        self.assertEqual(len(d.cruces), 1)

    def test_cosecha_excluye_fills_posteriores_a_270(self):
        d = DetectorR5K(TOK)
        d.on_trade("y", recv_ms(290), 0.80, "BUY", 5000)       # cruza con T=290 > 270: cuenta para cum, no para cosecha
        d.on_trade("y", recv_ms(280), 0.80, "BUY", 100)        # T=280 > 270: tampoco
        self.assertEqual(d.unidades(), {})
        d.on_trade("y", recv_ms(260), 0.80, "BUY", 100)        # T=260: sí
        u = d.unidades()[("m1", "NO")]
        self.assertAlmostEqual(sum(t for _p, t, _r in u["take"]), 50.0)

    def test_sin_cruce_sin_unidad(self):
        d = DetectorR5K(TOK)
        d.on_trade("y", recv_ms(200), 0.80, "BUY", 4999)
        self.assertEqual(d.unidades(), {})

    def test_coincide_con_el_criterio_offline_unid_cosechable(self):
        import random
        r = random.Random(3)
        d = DetectorR5K(TOK)
        for i in range(400):
            T = 300 - i * 0.7
            lado = r.choice(("y", "n"))
            px = r.choice((0.72, 0.75, 0.80, 0.85))
            d.on_trade(lado, recv_ms(T), px, r.choice(("BUY", "BUY", "SELL")) if False else "BUY", r.uniform(5, 120))
        rows = [(f[0], i, f[1], f[2], f[3], f[4], f[5], f[6]) for i, f in enumerate(d.filas)]
        U, _ = unid_cosechable(rows, {"m1": "YES"})
        online = d.unidades()
        self.assertEqual(set(U), set(online))
        for k, u in online.items():
            self.assertAlmostEqual(sum(p * t for p, t, _ in u["take"]), U[k]["c"], places=6)


class TestHuecos(unittest.TestCase):
    def test_hueco_dentro_de_la_ventana_marca_incompleto(self):
        d = DetectorR5K(TOK)
        self.assertTrue(d.completo("m1", CIERRE))
        d.on_gap("y", recv_ms(200))
        self.assertFalse(d.completo("m1", CIERRE))               # abierto
        d.on_snapshot("y", recv_ms(190))
        self.assertFalse(d.completo("m1", CIERRE))               # cerrado, pero solapa la ventana
        self.assertTrue(d.en_hueco("m1", recv_ms(195)))
        self.assertFalse(d.en_hueco("m1", recv_ms(180)))

    def test_hueco_fuera_de_la_ventana_no_afecta(self):
        d = DetectorR5K(TOK)
        d.on_gap("y", recv_ms(500))
        d.on_snapshot("y", recv_ms(400))
        self.assertTrue(d.completo("m1", CIERRE))                # terminó antes de T=300
        d2 = DetectorR5K(TOK)
        d2.on_gap("y", recv_ms(30))                               # empieza después de T=60
        self.assertTrue(d2.completo("m1", CIERRE))

    def test_gap_global_afecta_a_todos_los_tokens(self):
        d = DetectorR5K(TOK)
        d.on_gap(None, recv_ms(250))
        self.assertFalse(d.completo("m1", CIERRE))

    def test_cruce_registra_si_el_feed_estaba_completo(self):
        d = DetectorR5K(TOK)
        d.on_gap("y", recv_ms(280))
        ev = d.on_trade("y", recv_ms(250), 0.80, "BUY", 6000)
        self.assertFalse(ev[0]["completo"])                      # cum es cota inferior


class TestMemoria(unittest.TestCase):
    def test_podar_quita_mercados_cerrados(self):
        d = DetectorR5K(TOK)
        d.on_trade("y", recv_ms(200), 0.80, "BUY", 100)
        self.assertEqual(d.podar(CIERRE + 10), 0)                # aún dentro de max_edad_s
        self.assertEqual(d.podar(CIERRE + 5000), 2)
        self.assertEqual(len(d.cum), 0)


if __name__ == "__main__":
    unittest.main()
