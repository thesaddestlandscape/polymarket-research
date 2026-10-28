# PREREG escalera de patas B (28-Oct-2026). Escrito y hasheado ANTES de medir.
Universo: unidades P de alpha_miner_b_27oct/units (todas las monedas de 5m barato), relleno maker 5 acc a bb+0,01 (AS ya incluida), P_sh>=5. Entrada p0=P_cost/P_sh.
Rejilla (no se reajusta por moneda): escalones d en {0.05,0.10,0.15,0.20,0.30,0.45} sobre p0 (g=ceil a tick 0,01 de p0+d, g<=0,99);
escaleras de 2 patas = media de dos escalones i<j (10 acc = 2 ordenes de 5; mismo relleno de entrada supuesto, optimista);
terminales: H (mantener a cierre, venta viva hasta T-2s), D (cancelar y vender al bid como tomador en T-30s con fee), C (D solo si bid(T-30s)<p0, si no H).
Venta maker colocada en t1+150ms; rellena por 1er print de compra equivalente del token ESTRICTAMENTE por encima de g (BUY token p, o SELL complementario a 1-p). Sensibilidad >= g. Fee tomador 0,07p(1-p); rebate maker 20 % del fee del tomador (entrada y venta).
Buckets de compra p0: [<0.10),[0.10,0.15),[0.15,0.20),[0.20,0.25),[0.25,0.30). IS 05-22 Oct, OOS 23-26 Oct. Seleccion en IS por moneda x bucket, max-statistic por bootstrap de dias centrado (B=2000) sobre todas las celdas escalon/escalera x terminal.
Placebo: entrada tomadora a tiempo aleatorio (2 por pata, T U[60,290], ask en [0.10,0.30), fee tomador), mismas salidas. Inversion: pata complementaria comprada al ask en el instante del relleno (g<=0.99).
Metricas: EV ponderado Σpnl/Σcoste, IC90 por dias (bootstrap), sin 2 mejores dias, P(toque) vs p0/g.
Aceptacion CANDIDATE: OOS EVw>0 con IC90 por dias>0 y sin 2 mejores dias >0, p max-stat<0.05 en IS, n>=40 pares moneda x bucket seleccionada, >=3 dias OOS. EXPLORATORY: IS y OOS positivos sin IC>0. Si no, REJECTED.
Fuera de alcance declarado: compras <0,10 no cubiertas por P (BB_LO=0,10), niveles de cola, 15m.
