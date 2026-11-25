# Red-team PG_O50 / GEO6 (05-Nov, cheap5m-red-team-auditor). Escrito ANTES de calcular nada nuevo.
Base: escalera G de barrido_corr (engine.py sin tocar, cinta re-sincronizada = passC5c/C5d), dias 26-Oct..04-Nov (PG_O50 solo 29-Oct..04-Nov, scores Po_* y umbral C2o_thr 0,5 tal cual).
## R1 relleno «rancio» / fechado (rt_sim.py)
Mismos segmentos de cada politica (G0, GEO6, PG_O50), 5 modelos de relleno con rem propio por (k,L):
- BASE = engine.fill_segment 'BASE' (debe reproducir RC5c/RC5d exacto).
- STRICT = solo prints < L-TOLP (cota baja; travesia R9).
- OPT = engine 'OPT' (cola 0; cota alta de rellenos en L).
- CROSS = BASE + relleno inmediato si durante la vida el ask propio baja a <= L (o el bid del complementario sube a >= 1-L): la orden real habria sido cruzada ANTES (cota alta del relleno temprano).
- THIN = BASE con la travesia limitada al tamano del print (H-TOX-4) y acumulando prints.
Diagnostico por relleno BASE: t_below (primer bid < L tras t_arr), t_cross (primer ask<=L), mid a tf-300 y a t*-300 (t* = relleno CROSS).
Criterio fijado: SURVIVES si dPnL(PG_O50-G0) y dPnL(GEO6-G0) > 0 con IC90 por cierre > 0 en los 5 modelos; FABRICATED si alguno cambia de signo o pierde >=50 % en CROSS/OPT/STRICT; si no, INCONCLUSIVE. Igual para dPnL(PG_O50-GEO6) (criterio del prereg «supera a GEO6»).
## R2 simulado vs real (rt_b.py)
Ordenes reales de B 20-23 Oct (ordenes_b.parquet, verdad on-chain por order_hash): mismo fill_segment STRICT/BASE/OPT/CROSS con cinta WS (capt.Day.prints) sobre [t_ini, t_fin], cola real Q del ledger como cola (variante BASEQ). Tasa real vs simulada por celda (off 1c/2c/otro, banda de precio, moneda); EV de los rellenos reales que el sim pierde frente a los que acierta.
## R3 reposicion, doble conteo, regimen, sobreajuste (rt_r3.py, solo pkl existentes)
Familia de todas las politicas probadas en los mismos 7 dias (RC5, RC5b, RC5c, RC5d): p max-estadistico por cierre de dPnL vs G0; dPnL por dia frente a la tasa de victoria del lado NO; dPnL PG_O50-GEO6 con IC y dias forward necesarios.
