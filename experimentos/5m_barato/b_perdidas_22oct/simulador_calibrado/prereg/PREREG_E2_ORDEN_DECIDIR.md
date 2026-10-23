# PREREG E2 — simulador de B a nivel de ORDEN con el decidir() REAL en modo mock. 23-Oct-2026 ~06:15Z (antes de ejecutar nada de E2)
Continuación de E1 (NO_REPRODUCE, sha prereg E1 001c130d…). Visto antes (declarado, no ciego): todo el INFORME E1; estadísticos descriptivos de
`ordenes_b.json` (3.272 órdenes: post_ms p50 91, t_ret−t_dec p50 0,137, cancel_ms p50 66, vida en libro p50 0,58 s / media 1,19 s, 9,9 órdenes por puja,
186 órdenes con relleno, hazard 0,0466 rellenos por segundo vivo, hueco entre salida y siguiente t_dec p50 1,65 s); y que el ledger muestra
718 eventos `bloqueo_suelo_saldo` (158 de 305 pujas con ≥1 dentro de su ventana; saldo−mínimo p50 1,36 $ en los bloqueos): el presupuesto de
5 $ de la wallet dedicada LIMITA las órdenes simultáneas entre monedas; E1 no lo modelaba (cada mercado independiente, presupuesto infinito).
## Motor (M2)
- Decisión = `Exp47.decidir()` REAL de /root/polymarket-research-dev/experimento_maker_h47.py (sha256 c82f5dc5f304b8a6…, el mismo `codigo_sha` que la última
  `config` de B en el ledger), sin editar. Subclase mock que SOLO sustituye E/S: post, cancelar, liquidar, puede_enviar, _log47, _bloqueo, _libro5,
  `X.leer_ledger`→[] y `time` por reloj virtual. NO crea cliente CLOB, no firma, no lee .env, no escribe en ningún ledger. `elegir_cara`, `objetivo_h35`,
  `en_rejilla`, `tamano_orden`, `MIN_ENTRE_ACCIONES_S`, enfriamientos, un-relleno-cierra-la-puja, parada a T=60 s: todo el código real.
- Libro visto por el bot = libro5 (bids; ask = 1 − mejor bid del lado opuesto, como E1; limitación) en el instante (reloj − δ_obs).
- Relleno de cada orden virtual = `e1q_sim.vida_orden` (sin modificar; D1 declarada en E1) sobre libro5, calculado en el POST con t_end = cierre de puja;
  el bot lo DETECTA en el primer poll (POLL_S 0,5 s, fase propia) o al liquidar la cancelada ≥1,5 s después (ASENTAR_S); una cancelación que llega después del
  relleno devuelve True (como el exchange 'already matched') y el relleno se lee al liquidar.
- Simulación CONJUNTA por cierre (ETH+SOL+XRP del mismo slot), un solo `vivas/canceladas` y presupuesto compartido (como B real).
- Presupuesto: `puede_enviar` = H(t) − comprometido − coste ≥ 0 (comprometido = vivas+canceladas sin asentar de las 3 monedas), con H(t) = última observación del
  ledger real con hora ≤ t (suelo_fijado/suelo_subido: saldo−suelo; bloqueo_suelo_saldo: saldo−mínimo), 5,0 $ antes de la primera. Modo 'inf' (sin presupuesto) solo diagnóstico.
- Constantes fijadas DESDE los datos de órdenes, NO ajustadas: LAT_POST 0,085 s (t_call0−t_dec p50 0,041 + ½ post_ms p50 0,046), LAT_CAN 0,055 s (½ cancel_ms p50 0,066 + preparación 0,02), POLL 0,5 s,
  ASENTAR 1,5 s, T_INI 298, t_stop 60, tamaño = el que calcula `tamano_orden` (5..10 acc).
## Calibración (solo TUNE = pujas del 20-Oct; EVAL = 21 y 22-Oct, no se toca)
Rejilla ÚNICA, cerrada: cadencia del bucle del bot C ∈ {0,10, 0,25, 0,50} s (fase aleatoria por cierre, semilla 20261023) × δ_obs ∈ {0, 0,10} s = 6 celdas
(alloc 'prop' fijo; 'lo'/'hi' = cotas de cola conservadora/optimista se reportan SOLO sobre la celda elegida). Pérdida de TUNE sobre pujas completas
(fin_puja ∈ {t_stop, relleno}, es decir sin kill/tick/ws): L = |ln(órd/puja sim ÷ real)| + |ln(hazard por orden sim ÷ real)| + |ln(vida mediana sim ÷ real)|;
elige mín. L (empate: primera celda en el orden de la rejilla). Con n≈50 pujas en TUNE la elección es ruidosa: se declara.
## Universo
Pujas reales = las de E1 (`datos/cal_real_pujas.csv`: 298 con mercado en el mapa; se simulan las de MEDIR rango, 257) y órdenes reales = `ordenes_b.json` de esas pujas.
Relleno real = rf_a (ledger puja_fin.rellenos) para B1/B2 y fills on-chain (b_clase) para EV/clases, como E1. No hay más días de B: el ledger acaba el 22-Oct 15:48Z (B parada).
## Clases unificadas (X/C)
Clase del relleno SIMULADO a partir de los prints L2 (mismos datos que el replay), con la definición on-chain: C1 = existe un print a precio < p dentro de [r_fill, r_fill+τ1]
(la misma "tx" del tomador), C2 = no C1 y existe uno en (r_fill+τ1, r_fill+2000 ms], C3 = resto. τ1 = 25 ms primario (sensibilidad 5 y 100 ms). Se compara con la clase on-chain `cl_h1_0.005`
de b_clase y además con la misma función aplicada a los rellenos reales localizados en L2 (print al nivel pc más cercano a t_det en [−3,5 s; +0,3 s]) para validar el proxy.
## Criterios (todos sobre EVAL, celda elegida; intervalos: bootstrap por mercado, 2.000 réplicas, semilla 20261023)
O1 órdenes por puja (pujas completas): razón de medias sim/real ∈ [0,85, 1,15] Y Spearman por puja ≥ 0,60.
O2 vida de la orden cancelada (t_cancel_efectiva − t_live, sim; t_fuera − t_ret, real): |ln razón de medianas| ≤ ln 1,25 Y KS D ≤ 0,15.
O3 hazard de relleno por orden (rellenos/órdenes): razón sim/real ∈ [0,80, 1,25]; y por segundo vivo, mismo intervalo.
O4 primera orden de la puja: mismo precio en ≥ 0,85 de las pujas y |t_dec sim − t_dec real| ≤ 1,0 s en ≥ 0,70.
B0–B3 de E1 con los MISMOS umbrales (B0 lado ≥0,90; B1 |Δtasa| ≤0,05; B2 acc ≥0,80, κ ≥0,60, recall y precisión ≥0,75; B3 KS D ≤0,15, |Δmed| ≤0,5 s, ≥70 % de pares a ≤1 s).
B4 EV agregado |Δ| ≤ 0,10 (€/€ ponderado por €) Y cuotas de coste por clase UNIFICADA a ≤ 0,10 cada una frente a on-chain.
B5 EV POR MONEDA con el signo correcto: para ETH, SOL y XRP, si |EV real| > 0,05 entonces sign(EV sim) = sign(EV real); si no, |ΔEV| ≤ 0,10; y en todas |ΔEV| ≤ 0,30
   (n≈60-90 por moneda: IC anchos, se reportan; PASA/FALLA sobre el punto estimado y se anota si el IC90 de ΔEV contiene 0).
## Veredicto (EVAL)
REPRODUCE solo si pasan O1-O4, B0-B5. REPRODUCE_PARCIAL = pasan O1-O3 y B0-B1 pero no B2/B5 (útil para tasas, no para palancas). Cualquier otro caso: NO_REPRODUCE.
"Reglas probables ya" (±0,05-0,10 €/€) solo si el veredicto es REPRODUCE o si el efecto de la palanca es mayor que el error de B5 medido; si no, se dice que no hay.
## Límites previstos
EVAL ≈ 170-200 pujas; SE de EV ≈ 0,12; libro5 sin asks (ask = 1 − bid opuesto); H(t) del presupuesto reconstruido a trozos (solo se observa en los bloqueos); reloj del bot ≠ reloj de libro5 (δ_obs lo absorbe); sin cola de espera de escritura del ledger.
