# MISIÓN «EL CLICK DE B» — selección adversa + 200.000 €/año (Javi 24-Oct: «miles de wallets lo han encontrado; nosotros también»)
Chief = sesión principal. Regla: ningún hallazgo cuenta sin (1) prereg antes de mirar, (2) discovery/holdout en días distintos, (3) IC90 por cierre/día, sin 2 mejores días, placebo+inversión, K declarado, (4) reverificación independiente desde datos CRUDOS por otro agente. Los agentes NO repiten callejones cerrados: leer la lista antes de proponer.

## CALLEJONES CERRADOS (24-Oct, con informe) — no repetir sin mecanismo nuevo
- Filtrar fills de B: tomadores informados (AS-TOMADOR REJECTED), R0/R2/R1 régimen (R1 = confusor moneda+hora+sábado, red-team), precio>0,243 (espejismo), edad/T/rpre/libro al enviar/hora/moneda/tamaño/parciales/re-armes + árbol prof. 2 (todo p≥0,05).
- Detectores: D-FUERTE AUC ~0,554 (perps, 15m cruzado, mid residual = nada); detector ex-ante de relleno malo a −4 s AUC 0,499-0,513.
- Cancelación en ms: BN_W300_X2 REJECTED (329.998 rellenos); libro propio/15m/profundidad/edad = solo no operar.
- Tomador V2-V7 (rival 150-300 ms por delante), pares/cosechar (−5 pp pata suelta), bandas 5m 0,01-0,10, 60m 0,10-0,30, JOIN, H43 R5K (forward en contra), X-SALIDA, rebate (suelo 1 €/día; +0,011 €/€ solo ≥90 €/día).
- Wallet pspspsps5 (0xb0f85baa…): ventaja REAL (placebo z=3,8, brecha +0,20/+0,44 holdout) pero mecanismo NO hallado con datos públicos (H-A..H-D refutadas); celda 20-200 acc, zs∈[−1,0], 70 % del PnL en tickets, sin explicar.
## HECHOS QUE SÍ TENEMOS (palancas)
- La AS es mecánica: rellenas aciertan −18 pp vs no rellenas (IC90 −0,26..−0,10); tomar esas unidades da ≈0.
- 44/48 grandes makers de BTC 5m son positivos (selección ex-post); 0x21f4/0xe290/0x86b1 +22..+34 k€/16 d con rebate 31-43 % del neto; B (alts) EV −0,072. BTC 0,05-0,30 = 56 % del neto con 10 % del volumen.
- Carry ≥0,90 maker = 63 % del capital de W (+3,3 k$); B no opera BTC.
- 15m ETH favoritos «robustos» (memoria); 4h/diario y banda 0-0,10 en recolección TP1.
## FLUJOS DE TRABAJO NUEVOS (ángulos todavía NO agotados)
- F1 HUELLA DE COHORTE: no un wallet sino los ~700 makers: qué rasgos de comportamiento (banda, momento en la ventana, tamaño, nº de ventanas simultáneas, fracción carry, moneda, reposición inferida de secuencias de fills) predicen EV persistente (discovery→holdout). Incluye por qué los grandes de BTC ganan y los de alts no (¿tamaño? ¿cola? ¿banda?).
- F2 MERCADOS CON MENOS SELECCIÓN ADVERSA: 15m ETH favoritos, 4h, diario, otras monedas/marcos: medir EV maker condicional a relleno (con AS incluida) por moneda×marco×bucket; dónde el relleno NO pierde 18 pp.
- F3 CARRY ≥0,90 MAKER como motor de capital (W lo usa 63 %): EV por € de comprar ≥0,90 en reposo, riesgo de cola, capacidad, solapes con rebate.
- F4 FIDELIDAD DEL SIMULADOR (cuello de botella): captura de eventos de nivel (en curso) + calibrar simulador contra ganadores para poder iterar sin dinero.
- F5 ENSAYO REAL MÍNIMO (requiere OK Javi + /code-review + recarga): micro-órdenes con cancelación para observar el ciclo de vida y la AS propia en BTC 0,05-0,30. DECISIÓN DE JAVI.
## CADENCIA
Olas de ≤3 agentes con tokens; al entregar uno, el chief lanza el siguiente de la cola o el red-team del que acaba de entregar. Cola: F1 → F2 → F3 → red-team de cada uno → síntesis «candidatas para forward» → OK Javi.
