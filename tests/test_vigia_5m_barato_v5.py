"""Pruebas de la definición congelada de V5 (origen 15m) sobre eventos sintéticos."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import vigia_5m_barato_v5_forward as V5  # noqa: E402


def ev(i, cie, mon, prim, ob, ca, t):
    return {"event_id": f"B1_5m_{mon}_{cie}_{i}", "regla": "B1_5m", "es_primero": "1" if prim else "0", "cierre": cie,
            "moneda": mon, "o_edad_bid_ms": ob, "c_edad_ask_ms": ca, "t_deteccion": t}


def test_origen():
    assert V5.origen_15m({"o_edad_bid_ms": "10", "c_edad_ask_ms": "50"})
    assert not V5.origen_15m({"o_edad_bid_ms": "50", "c_edad_ask_ms": "10"})
    assert not V5.origen_15m({"o_edad_bid_ms": "10", "c_edad_ask_ms": "10"})        # empate -> no
    assert not V5.origen_15m({"o_edad_bid_ms": "", "c_edad_ask_ms": "10"})          # sin dato -> no
    assert not V5.origen_15m({"o_edad_bid_ms": None, "c_edad_ask_ms": "10"})


def test_seleccion():
    E = [ev(1, "100", "BTC", True, "90", "5", 1), ev(2, "100", "BTC", False, "1", "80", 2), ev(3, "100", "BTC", False, "1", "80", 3),
         ev(1, "200", "ETH", True, "1", "80", 4), {"regla": "B2_15m", "es_primero": "1", "cierre": "300", "moneda": "SOL",
                                                    "o_edad_bid_ms": "1", "c_edad_ask_ms": "9", "t_deteccion": 5}]
    a = V5.seleccionar(E, "V5a")
    assert [e["event_id"] for e in a] == ["B1_5m_ETH_200_1"]                         # primer evento y origen 15m
    b = V5.seleccionar(E, "V5b")
    assert [e["event_id"] for e in b] == ["B1_5m_BTC_100_2", "B1_5m_ETH_200_1"]      # primer evento CON origen 15m


if __name__ == "__main__":
    test_origen()
    test_seleccion()
    print("OK")
