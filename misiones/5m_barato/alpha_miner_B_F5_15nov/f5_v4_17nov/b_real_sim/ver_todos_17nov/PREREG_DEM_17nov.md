# PREREG DEM (cinta de demanda tomadora residual) — ver_todos_17nov — 17-Nov-2026 ~21:25Z (antes de la pasada 2)
Contrato: CONTRATO_MEDICION_F5_B_v2 (sin cambios de relojes/latencias). Motor engine_v4 sin tocar; copia v4_verif_dem.py (generada de verif_v5.py) + dem_hook.py.
Universo: 3.796 órdenes reales de B, 20-23 Oct, 202 rellenos reales. Base = r2_call00a35_intc33_v3d (debe reproducir 88 sim / 84 TP / 4 FP / 118 FN; si no, se para).
Ya visto antes del prereg (descriptivo, v1/v2): 98 FN clase 1: 72 SOLO, 24 SOLO_ARRIBA, 2 DEBAJO; orden tomadora nunca vista on-chain antes (0/98); 60/98 con remanente.
Mecanismo: print sintético (sello v3 del tx, precio L, tamaño S_T − acciones casadas con makers AJENOS) si eq_límite_tomador ≤ L.
Variantes: DEMr (solo tx con ≥1 maker ajeno = existirían sin nosotros) = PRIMARIA; DEMe (además sin filas nuestras); DEMall (incluye tx solo-nuestros: CIRCULAR, solo cota);
placebos DEMr_p30 / DEMr_m30 (eventos desplazados ±30 s).
Predicción: ganancia en SOLO_ARRIBA / MISMO_NIVEL / cola; 0 rescates SOLO en DEMr (por construcción).
ACEPTA el mecanismo si: ΔTP(DEMr) ≥ +5, precisión DEMr ≥ 0,85, ΔFP ≤ ΔTP/3 y max(ΔTP placebo) ≤ ΔTP(DEMr)/3.
REFUTA si: ΔTP(DEMr) ≤ max(ΔTP placebo) o precisión < 0,80. Entre medias: INCONCLUSO.
Se reporta además: recall por clase de FN, % nuevos TP a ±50 ms del relleno real, EV (Σpnl/Σcoste) de TP/FP/FN, y DEMall como techo circular.

## ADENDA 1 (17-Nov ~21:40Z, antes de la pasada 2; tras diagnóstico descriptivo v6 de clases 8 y 4)
Visto: clase 8 (11): en 10/11 a la llegada había puja > L (motor pone cola=INF y luego toma TODO el tamaño en L del libro real, que incluye nuestra orden real
y a quien llegó después); en 7/11 el operador nos casó ANTES que al otro maker en L. Clase 4 (8): relleno real 1-868 ms tras t_end; 6/8 ≤164 ms.
Variantes añadidas: COLA (cola inicial = `cola` de B en t_dec si puja>L; filas en L menos nuestro tamaño), C150 (prints hasta t_end+150 ms: retraso del tomador),
COLA_C150, DEMr_COLA_C150 (combinada). Criterio para cada una: ΔTP ≥ +3 y ΔFP ≤ ΔTP/2 → acepta; ΔFP > ΔTP → refuta; resto inconcluso.
COLA solo es válida para replay de órdenes REALES (resta de nuestro tamaño); en días contrafactuales la parte (2) no aplica.

## ADENDA 2 (17-Nov ~21:40Z): solo corrección de implementación (g.eq resolvía al método DataFrame.eq; ahora g['eq']). Sin cambio de criterios; la pasada 2 abortó antes de calcular ninguna métrica.

## ADENDA 3 (17-Nov ~21:50Z) — POST HOC, EXPLORATORIO (tras ver la pasada 2): DEMr+C150+COLA rescata 11 de clase 1 frente a 1 de cada pieza por separado.
Hipótesis de interacción: la demanda residual de DEMr llega a L pero el motor tiene cola=INF (puja > L a la llegada). Variantes DEMr_COLA y placebos DEMr_COLA_p30/_m30.
Mismo criterio que la primaria (ΔTP ≥ +5, prec ≥ 0,85, ΔFP ≤ ΔTP/3, placebo ≤ ΔTP/3), pero etiquetado EXPLORATORY por ser post hoc.
