# ADENDA_01 a PREREG_R1v2_19nov.md (48fe638e...) y CONTRATO_R1v2_19nov_v2.md (6bda3605...) — 19-Nov-2026
Base congelada, NO editada. Aprobado por Javi el 19-Nov a partir de la pasada 1 del buscador (project_pasada1_b_f5_19nov.md). Fijado SIN mirar datos ni tasas evento-placebo. Todo lo no mencionado aqui no cambia.

## A1. Variante nueva V5 = «cancelar ante movimiento ADVERSO de Binance hasta t» (familia 4 -> 5)
- Fuente: filas x de m5_registro, solo con rx (c[7], RECEPCION) <= t; nunca c[6] (E de Binance).
- Regla: orden viva de B (lado Up/Down) se cancela si en la ventana (t-W, t] el movimiento de Binance es adverso al lado, |mov| >= X bps. X = 3 bps, W = 3000 ms (fijos; justificacion: H-TOX-6 «<=3 s tras salto adverso»; 3 bps ~ un tick de 1c en el ask segun el hallazgo del CLAUDE.md «tras 1-3 bps el ask se mueve +2/+3,6c»). Adverso = Binance sube y la orden es Down, o baja y la orden es Up. Sin variantes de X/W: cualquier otra = version nueva y cuenta.
- Efectividad (contrato): cancelacion a tiempo solo si rx + t_proc + L_cancel <= casado - 20 ms. L_cancel solo de paquete_l 13-Nov: p50 33 / p90 74 (PRIMARIA p90 74) / estres 111 ms, declarado por clase de suelo lo/hi. Si p90 |t_sim - t_real| > L_cancel, INSUFFICIENT (contrato v2).
- Aclaracion: la restriccion «Binance rx <= t-1000» (sec. 9 del prereg, grupo C) venia del balance de covariables de la pista cola y NO aplica a una regla de cancelacion causal; V5 usa rx <= t sin margen de 1000 ms. Los rasgos de grupo C de las otras variantes no cambian.
- Frecuencia de disparo (trampa «cancelar para siempre si X salta»): se reporta SIEMPRE la fraccion de vidas de orden con >=1 disparo y P(fill) con/sin regla; si dispara en >50 % de las vidas, el EV≈0 se declara «solo no operar», no efecto. Se compara el EV de los apartados con el relleno medio.
- Familia confirmatoria = 5 (E1 primaria, c=0; c=0,05; regla mu_hat<-c; V5; la de sec. 2 del prereg); p_max<0,05 por max-statistic (permutacion) sobre las 5. Criterios 1-9 y placebo/inversion de la base sin cambio.

## A2. Experimento EXPLORATORIO sobre los 202 rellenos reales de octubre (94 % hi -> solo exploratorio, fuera de la familia)
- Por relleno: marcado = movimiento adverso de Binance >= X (3 bps) en [casado-1500, casado-(74+t_proc+20)] ms con rx <= fin de ventana. Placebo: t aleatorio dentro de la vida de la MISMA orden, misma anchura de ventana y misma exigencia de efectividad (semilla fija, >=1000 sorteos).
- Aceptacion (las 3 a la vez): (i) tasa marcados >= 2x placebo; (ii) marcados cubren >= 30 % del € perdido; (iii) EV marcados - no marcados con IC90 por DIAS < 0 (ponderado por €, ademas de por unidad).
- Cumplirlo NO promociona V5 ni confirma nada: sirve de motivo para la version confirmatoria; sin ancla de noviembre y con 94 % hi, es solo exploratorio. Declarar n, dias y EV sin los 2 mejores dias.

## A3. Rebate
Rebate = 0 es la version PRIMARIA del EV (el suelo de pago ~1 $/dia exige mas volumen maker del que B tenia). Rebate 0,2 pasa a SENSIBILIDAD (invierte la sec. 1 del prereg). Fee 0,07 takerOnly sin cambio.

## A4. Nada mas cambia
Particiones, ceguera, puerta 0, E-SO-3, cortafuegos CXB, condiciones previas al EV y la prohibicion de promocionar exploratorias tras ver el HOLD siguen vigentes.
