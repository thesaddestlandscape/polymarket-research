# Briefs de la cola (chief, 25-Nov) — uno a la vez, informe ≤60 líneas, sin órdenes reales, sin tocar lo firmado

Mandato Javi 25-Nov (memoria feedback_b_integrar_todas_ventajas_200k_25nov): integrar en B y la subvariante TODO el universo conocido (ventajas, latencias, F5, mitigaciones de selección adversa), para ENTRAR cuando hay que entrar, NO ENTRAR cuando no, SALIR/CANCELAR cuando hay que salir, con el setup perfecto; EV > 0; camino a 200 k€/año. Sin relajar gates.

## 1. polymarket-data-integrity-authority — contrato de la matriz
Antes de que nadie mida nada para la matriz: para cada métrica que la matriz va a citar (EV/€ por pieza, AS, latencias, rellenos), fijar fuente, campo, reloj (recepción vs exchange, clase de suelo lo/hi por ventana), motor/sello vigente (passT_v4; RF5 a5161ce9a7df8294), latencia vigente (paquete_l 13-Nov), unidad (1.er relleno mercado-lado; EV ponderado por €; censura incondicional). Marcar qué cifras históricas NO son reutilizables (sello viejo, reloj sin verificar). Salida: docs/CONTRATO_MATRIZ_25nov.md con GREEN/AMBER/RED.

## 2. cheap5m-objetivo-200k — MATRIZ de ventajas y selección adversa
Fuentes: docs/MATRIZ_FUENTES_25nov.md (no leer las ~700 memorias: solo las del índice que toquen) + contrato del punto 1.
Una fila por pieza, en 4 ejes: (1) ENTRAR (armar, nivel, tamaño, repegado DEEP_PEG), (2) NO ENTRAR (F5 terciles/F1/F3, Calma-T1, clase de suelo, régimen, wallets, Binance), (3) SALIR/CANCELAR (V5=CXJ150, V6=E1b S1, cancelación por Binance, A3-CANCEL BTC, descarga de la pata perdedora), (4) SETUP (latencia real por clase, ventaja maker ~145 ms, taker delay, rebate 20 %, WS vs REST, relojes).
Columnas: pieza · eje · ¿en K1-K6? ¿en subvariante? ¿en el ejecutor B-K? · evidencia con motor vigente (n, días, IC90 por días) o «no validada» · AS que mitiga · cómo integrarla sin romper lo firmado (sombra ya / versión siguiente con prereg) · aporte estimado al libro de 200 k (con supuestos explícitos) · siguiente prueba mínima.
Regla: nada sale de la matriz sin refutación completa (gates, n efectivo, placebo, reloj correcto). Cruzar con preregs/ledgers (no proponer como nuevo lo ya existente). Salida: docs/MATRIZ_B_SUBVARIANTE_25nov.md + top-5 integraciones de más valor/esfuerzo para que Javi decida.

## 3. cheap5m-execution-engineer — subvariante BTC (c4_btc 6/10)
(3) simulador de B base BTC con passT_v4, 03-17 Nov, leyendo solo f5t → base_btc_D.ok; (7) C1/C3 BTC 03-17 (c1c3_btc_D.json ok:true); borradores de (4) adenda cortes p20/p80 BTC (F2b/F3b, cuantil numpy lineal de F5_0 de lados BTC bloq0) y (5) contrato E1b §12.2 BTC, para validador y firma del chief con OK de Javi. Más las integraciones de la matriz que Javi apruebe. Jobs pesados por cron_pesado, ≥4,5 GB libres medidos, nunca 06:00-09:15Z; verificar JSON y sello, nunca el rc.
