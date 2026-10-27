# ENMIENDA 1 al PREREG (26-Oct ~09:10Z, ANTES de calcular ninguna tasa/EV virtual; PREREG.sha256 sigue valiendo para el texto original)
Motivo: aviso del agente RE-AS-B. En `etiquetado_pasivo_B` la unidad `orden` duplicaba `acc_llena` (relleno_tardio contado dos veces: ya estaba en puja_fin.rellenos con tardio=True). Corregido en `etiquetado_pasivo/scripts/etiquetar_pasivo.py` (`acc_orden`, auto-correccion idempotente: 18 ordenes) con `tests/test_acc_llena.py`.
Verdad corregida (c1_build_b.py): 195 ordenes rellenas (antes 194: una resuelta tras la primera lectura), acc 1.040,9, PnL por ordenes -13,05 EUR; posiciones 202, acc 1.072,3, PnL -16,02 EUR. La diferencia (31,4 acc, -2,97 EUR) son 7 posiciones/pujas con relleno real que el ledger de B no atribuyo a ninguna orden.
Cambios al protocolo (no afectan a la seleccion de variante, que usa P_orden y P_puja):
1. Verdad de PUJA = alguna orden rellena O posicion existente para (mercado, lado) (`fill_puja`); la verdad de ORDEN sigue siendo acc_llena>0 (las 7 pujas no atribuidas no se imputan a ninguna orden: son fn inevitables de recall solo a nivel puja).
2. Todo EV/pnl real usa el acc_llena corregido.
3. El efecto "rellenas vs no rellenas" no se usa en ningun momento: las metricas son margen del relleno frente a su PRECIO (EV/EUR = pnl/coste), como pide el aviso.
