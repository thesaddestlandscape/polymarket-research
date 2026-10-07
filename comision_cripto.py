#!/usr/bin/env python3
"""comision_cripto.py -- UNA sola fórmula de PnL por € para los mercados cripto de Polymarket (07-Oct, Javi: "unificar la
comisión de todos los gates en una sola función"). Verificado en gamma/clob-markets 07-Oct: feeSchedule rate 0.07,
exponent 1, takerOnly (el maker no paga; rebateRate 0.2 para el maker, no incluido aquí).
Tomador que compra a precio p con 1 € (comisión incluida): acciones = 1 / (p·(1 + FEE·(1−p))). Si el exchange cobra la
comisión en acciones (compras), la ganancia es (1 − FEE·(1−p))/p − 1: igual a primer orden (<0,5 %). Pendiente
confirmarlo contra los rellenos on-chain (campo fee de onchain_fills_*).
  pnl_por_euro(p, acierto) = acierto / (p·(1 + FEE·(1−p))) − 1
Equivalencias medidas: la fórmula histórica "(1−p)/p·(1−0,07) si acierta, −1 si no" difiere <0,5 % en todo el rango
(no cambia veredictos); la de gate_bucket_propio sin comisión ("1/p − 1 − 0,02") sobreestimaba las ganancias a precio
bajo (+0,57 por acierto a p=0,1). Sports usa 0,05 y otra base: NO usar este módulo fuera de cripto.
"""
FEE_CRIPTO = 0.07


def pnl_por_euro(precio: float, acierto, fee: float = FEE_CRIPTO) -> float:
    """PnL por € arriesgado de una compra tomadora a `precio` que resuelve a favor (acierto=1/True) o en contra."""
    if acierto not in (0, 1, True, False, "0", "1"):
        raise ValueError(f"acierto debe ser 0/1/True/False/'0'/'1', no {acierto!r}")
    gana = acierto in (1, True, "1")                    # '0' (str de un CSV) NO cuenta como acierto
    return (1.0 if gana else 0.0) / (precio * (1 + fee * (1 - precio))) - 1.0
