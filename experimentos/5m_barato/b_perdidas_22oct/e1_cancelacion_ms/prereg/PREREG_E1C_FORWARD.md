# PREREG E1C-FORWARD (24-Oct-2026 ~10:55Z) — seguimiento pasivo de BN_W300_X2 (EXPLORATORY en E1C, falló Bonferroni)
Regla congelada (sin cambiar ningún parámetro): cancelar la orden maker de B cuando Binance aggTrade de su moneda (recepción c[7]) se mueve ≥2 bps
EN CONTRA del lado en 300 ms (Up: caída; Down: subida), evaluado en rejilla de 10 ms durante la vida de la orden. Cancelación efectiva t+60 ms;
casado = t_print − 30 ms. Código: e1c_senales.py (config BN_W300_X2) + e1c_eval.py, mismos supuestos (sustractivo, sin recolocación).
Datos: SOLO días posteriores al 22-Oct con rellenos reales de B (o de cualquier maker propio en la banda 0,10-0,30 5m ETH/SOL/XRP) con print localizado en L2
por recepción, y la población de rellenos de bid del libro5 de esos mismos días (e1c_pob.py, mismo flag, look 1 s).
Gate (una sola hipótesis, alfa 0,05 una cola), TODO a la vez:
1. ≥4 días nuevos y ≥150 rellenos propios evaluables; ΔPnL > 0; placebo (misma fracción al azar dentro de día, 5000) p < 0,05;
   IC90 por cierre de ΔPnL con límite inferior > 0; ΔPnL > 0 sin los 2 mejores días; ganadores perdidos ≤ 25 % del € evitado.
2. Réplica poblacional en los mismos días: EV€(con bandera) − EV€(sin bandera) < 0 con IC90 por cierre por debajo de 0.
3. Sensibilidad: con cancelación de 120 ms ΔPnL sigue > 0.
Si 1 pasa y 2 no: efecto propio de B (no generalizable) → no escalar. Ningún resultado de este forward autoriza envío real: va a /code-review + OK Javi.
