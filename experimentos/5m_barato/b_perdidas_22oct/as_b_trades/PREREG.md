# PREREG as_b_trades (QA estadistico, 24-Oct-2026 ~10:12Z) - escrito ANTES de calcular cualquier EV por regla
Pregunta: existe alguna regla decidible antes del relleno (con latencia real) que separe fills de B ganadores de perdedores?
Ya visto ANTES de este prereg (no ciego): INFORME as_tomador s5 (SET_V bruto sobre B EXCESO +0,267, POST-HOC), totales anatomia 20-22 Oct,
INFORME b_regimen (R0). Por tanto TODO lo que salga sobre estos 215 fills es como mucho EXPLORATORY; confirmar exige dias nuevos.
Datos: fills = /mnt/HC_Volume_106538179/agentes_datos/as_tomador/verif/B_fills_mio.csv (215, taker on-chain, desenlace oficial);
ordenes = datalogs/etiquetado_pasivo/etiquetado_B_2026-10-2{0..3}.csv.gz (t0, precio, T_s, rpre, r900, h_w1, gana_lado tambien de NO rellenas);
rasgos de envio 20-22 Oct = experimentos/.../anatomia/pos_anotado2.csv (solo columnas *_post de ENVIO, dist_ref, vol60, bn_pre30, btc_pre30,
n_ordenes, tras_cancel, t_desde_open, fv_gap, hora, coin). EXCLUIDAS por mirar el futuro: mo*, mov_post*, bn_post*, btc_post*, cola_fill, p/acc reales del relleno no.
Unidad: mercado+lado (fills agregados); flag de una regla por unidad = flag de su orden; inferencia por CIERRE (fin): bootstrap 2000, semilla 7.
Metricas: EV=sum pnl/sum coste (por EUR); EXCESO=EV_retenido-EV_total; dPnL=-pnl de lo saltado; retencion EUR.
Split: TRAIN 20-21 Oct (elige), TEST 22-23 Oct (evalua, no se usa para elegir).
Familia P (reglas fijas, sin ajuste), K_P=3: P1 tomador en SET_V (09-18, previo a B); P2 tomador en SET_I (09-23: CONTAMINADO, incluye dias de B);
P3 R0 = h_w1==1. (N2/AR2h: DATA_BLOCKED si no hay pob_D causal; no se sustituye.)
Familia L (aprendida en TRAIN): por rasgo, candidatos = {tercil bajo, tercil alto} (continuos, cortes de TRAIN) o cada nivel (categoricos);
se elige el de menor EV_flag en TRAIN con >=15 % del EUR; + 1 arbol profundidad 2 (hoja >=15 unidades). K_L = n rasgos + 1.
K_total = K_P + K_L, alfa familiar 0,10 -> Bonferroni 0,10/K_total (una cola) y BH al 0,10.
Gate (sobrevive solo si TODO): EXCESO_TEST>0; p_placebo_TEST < alfa_Bonf (placebo = misma fraccion de EUR al azar dentro de dia, 5000);
IC (1-2*alfa_Bonf) por cierre del EXCESO en TEST con limite inferior >0; EXCESO>0 sin los 2 mejores dias (de dPnL); retencion >=40 %.
Potencia: MDE del EXCESO = (z_{1-alfa}+z_0,8)*SE_placebo; cierres necesarios para MDE en EV de +0,05 y +0,10.
Descriptivo AS: acierto de ordenes rellenas vs NO rellenas al mismo precio (EV virtual (gana-p)/p de las no rellenas).
