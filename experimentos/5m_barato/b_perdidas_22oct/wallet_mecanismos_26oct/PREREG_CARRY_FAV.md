# PREREG CARRY-FAV-5M — 26-Oct ~13:20Z, ANTES de ver ningún EV de población por profundidad/T/tamaño (p1 aún sin salida)
Datos: p1 (fav_D: TODOS los rellenos maker de compra p>=0,60 en 5m, on-chain, con profundidad proxy `ticks` = ticks bajo el máximo
precio maker del mismo token en la misma tx). SEL = cierres 06-14 Oct; OOS = cierres 15-25 Oct (no mirado). Desenlace oficial.
EV ponderado por $ (Σpnl/Σcoste, comisión maker 0, rebate EXCLUIDO del criterio y reportado aparte), IC90 bootstrap por DÍAS.
Diseño en BTC (regla Javi 14-Oct); las otras 5 monedas se reportan como réplica, sin elegir parámetros en ellas.
## Selección (solo SEL, BTC, población ex-W ex-MM)
Rejilla K=16: banda de precio {[0,70,0,80) [0,80,0,90) [0,90,0,95) [0,95,0,99)} × profundidad {0, 1, 2-4, >=5 ticks}.
Celda elegida = la de MAYOR cota inferior IC90 por días con n>=2.000 rellenos y >=7/9 días positivos. Secundario (solo si mejora la cota
inferior): ventana T (s hasta cierre) {0-60, 60-120, 120-180, 180-300}; tamaño del relleno {<=10, 10-50, 50-200, >200 acc} solo descriptivo.
## Test OOS (15-25 Oct, una sola regla congelada)
Éxito (cota OPTIMISTA condicionada a relleno): EV >= +0,01 con IC90 por días >0, EV sin los 2 mejores días >0, >=7/11 días >0, y EV de la
regla > EV del resto de la banda en el mismo periodo (IC90 de la diferencia >0). Réplica en ETH/SOL/XRP/DOGE/BNB con la misma regla.
Refutada: cualquiera de lo anterior falla. Aunque pase, NO es ejecutable hasta pasar la simulación de final de cola (vpv de f3_carry, que
para pujas al mejor bid dio −0,035/−0,071): ese es el siguiente paso, no este.
## Orden (W y MM, descriptivo, ambos periodos): acc por order_hash, rellenos por orden, ticks, T, moneda, exposición concurrente por cierre
(p50/p95 del coste vivo), €/día; cambio de favorito = compras >=0,70 de ambos lados del mismo mercado (secuencia temporal).
