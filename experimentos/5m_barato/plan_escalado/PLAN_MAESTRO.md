# PLAN MAESTRO DE ESCALADO 5m barato — 20-Oct-2026 (directiva Javi: ≥200 k€/año por subestrategia)
Validado hoy: 0 €; todo EXPLORATORY salvo PRECIERRE (live 2 €). $ = €. Objetivo 548 €/día. €/año = N/día × stake × EV × 365; capital para ≤1 % de ruina = 2,3·σ1²·stake/EV (σ1 = desv. por € apostado, EV pesimista). Cálculos: `escalado_numeros.py` → `salida_numeros.txt` (misma carpeta).

## 1. Una fila por subestrategia
| Subestrategia | EV/€ pond. (IC90) · n · días | Capacidad hoy | Nocional/día necesario (548/EV) vs medido | Palanca nº1 → experimento, fecha |
|---|---|---|---|---|
| **H55 favorito** (BTC) | desc. +0,179 (cierre +0,005,+0,34) n=36/13 d; sin 2 mejores +0,040; Bonf.×4 −0,058. Rival R1 +0,131 (10/10 d). OOS 19-Oct sin datos | 2,8 entradas/día; rival 147 $/unidad sin barrer profundidad | 6,85 k$ (EV 0,08) vs 5,6 → ×1.200 (×17 a 147 $) | Más oportunidades: 6 monedas + pares 15m⊂60m, 60m⊂4h → offline m5_registro, 22-Oct. Gate n≥40 ≈ 2-Nov |
| **H35/H47 alts** (ETH k2, SOL/XRP k1) | OOS 14-16 +0,064 (879 rell., IC días −0,12,+0,27); desc. +0,084 (1.547, 4/6 d); rebate +0,011 sin verificar | 293 rell. y 293 $/día a 5 acc | 7,3 k$ vs 293 → ×25 (94 k a K=50, no medido) | **H45** K=25/50 offline antes del 22-Oct (rota maker_ms 17-Oct); H47-B calibra colas |
| **H23 maker, cancela 60 ms** | +0,80 (días +0,20,+1,38) n=17/9 d; sin 2 mejores +0,25; simulador sin calibrar | 1,3 rell./día, 2-3 $/evento | 2,2 k$ vs 2,6 → ×840 | No escala sola: ejecuta H55/H53 (H54, una vía/evento). Sombra `h23_shadow` desde 20-Oct |
| **R5K** (BTC) | forward −0,307 (cierre −0,509,−0,105) 213 u./3 d | 830 $/día | EV<0 | **H48 24-Oct**: REJECTED si límite sup. <+0,05 |
| **V4 / V4b-0,02** (tomador) | V4 +0,277 n=25, sin mejor op. −0,002; V4b desc. +0,507 (cierre +0,056,+1,008) n=24, sin 2 mejores +0,11 | 1-2 ejec./día, p50 13,6 $; rival llega 188 ms antes | 5 k$ vs 2 → ×2.500 | Tomador cerrado (77 % de ganadoras se pierden a ≥145 ms). V4b OOS: n=40 ≈ 28-Nov; ejecutar vía H23 |
| **PRECIERRE 5m** (LIVE) | real n=24 +0,130 (días −0,40,+0,80), sin 2 mejores −0,116; virtual V0 n=74/26 d +0,06 | 2,85/día; profundidad p50 16 €, p90 94 € → regla ≥5× limita a ≈3 € | 9,1 k$ vs 8,6 → ×1.070 | Profundidad por banda de ask 0,25-0,95 y marco (offline, 22-Oct) |
| **PRECIERRE 15m** (LIVE) | real n=11 +0,253 (días −0,41,+0,91), sin 2 mejores −0,137; virtual V6 n=39 +0,19; V5 n=387 +0,06 (15/día) | ~1,5/día; profundidad sin medir | 2,9 k$ vs 3 → ×960 | Mismo experimento; V6 cierra n=40 en días; rampa 5 € exige 40 órdenes post-arreglo (hoy 4) |
Pool maker: 305 k$/día de coste, +0,040 pond.; 200 k a EV 0,075 = 2,4 % de su volumen (`LIBRO_OBJETIVO_200K.md`).

## 2. Escalera común y €/año por peldaño
**Gate (todos):** ≥40 órdenes reales (maker: ≥300 rellenos y S2 de H47: |tasa real−sim| ≤8 pp, acuerdo ≥0,70, markout ≤0,03), ≥10 días, EV pond. ≥+0,05 con IC90 por días >0, sin 2 mejores días >0, `analisis_log_growth` g>0, code-review + OK de Javi. **Kill:** pérdida acumulada del peldaño ≥ 1,645·σ1·s·√n − 0,05·s·n (≤5 % falso con EV +0,05; ≈4·s a n=40 en H55); nunca media acumulada. Bajar si las últimas 20 órdenes dan EV<0. **Reinversión:** retener ganancias; subir solo con gate y saldo ≥ capital de ruina 1 % del siguiente peldaño. Pérdida P95 en 100 órdenes con EV 0: 9,5·s (H55), 16,5·s (PRECIERRE), 34·s (maker).

| Stake $ | H55 €/año (EV 0,04 / 0,08) | capital ruina 1 % | PRECIERRE 15m (0,10 / 0,19) | PRECIERRE 5m (0,03 / 0,06) | H35 (EV 0,075) |
|---|---|---|---|---|---|
| 2 | 82 / 164 | 38 | 110 / 208 | 62 / 125 | 5 acc ≈ 8 k |
| 5 | 204 / 409 | 95 | 274 / 520 | 156 / 312 (techo) | 10 acc ≈ 16 k |
| 10 | 409 / 818 | 190 | 548 / 1.040 | — | 25 acc ≈ 40 k* |
| 25 | 1,0 k / 2,0 k | 476 | 1,4 k / 2,6 k | — | 50 acc ≈ 80 k* |
| 50 | 2,0 k / 4,1 k | 952 | — | — | — |
| 100→147 | 4,1-6,0 k / 8,2-12,0 k | 1,9-2,8 k | — | — | — |
*Si H45 pasa; escala lineal supuesta; kill 354 $ a 25 acc, 710 $ a 50. Autofinanciación H55: 125-212 días por peldaño; llegar a 147 $ pide ≈2,8 k€ (decisión de Javi).

## 3. Cierre del hueco
Con N y EV medidos el techo por fila es 0,2-12 k€/año. Los 200 k solo salen de ×N oportunidades × tamaño, con base en dos sitios: **(a)** H55 con ≈50 entradas/día a 147 $ y EV 0,08 (6 monedas + marcos 15m/60m; ≈2,8 k€ por flujo); **(b)** maker alts a K=50 con ≈2,4 % del pool (H45 decide 9 k o 94 k). PRECIERRE y H23: pocas oportunidades y poca profundidad; validan y financian. Sin doble conteo: H55, V4/V4b, H23 y H54 comparten cierre BTC (una apuesta por cierre: unión); H35 y R5K comparten wallet dedicada y un tope; PRECIERRE (wallet principal) correlaciona por dirección.

## 4. Calendario
**Revisión semanal (27-Oct), por fila:** n, días, EV pond. con IC90 por días y por cierre, EV sin 2 mejores días, kill, FOK muertas, tasa de relleno real vs sim, saldos (`balance_real.json`), ratio de profundidad. **Cinco acciones:**
1. H45 K=5/10/25/50 sobre maker_ms 17-18 Oct, antes del 22-Oct (execution-engineer; nice 19, fuera de 06-09Z).
2. H55 en alts y 15m⊂60m/60m⊂4h + ejecutor sombra sobre F2 (event-causality-analyst / execution-engineer).
3. H47-B: revisar el seco, OK final de Javi, calibrar colas (chief + Javi).
4. Profundidad por banda para PRECIERRE y stake vs regla 5× (risk-economics).
5. H48/H44 el 24-Oct y decisión de capital por peldaño (statistical-validator / Javi).

## ADENDA 20-Oct (chief, Javi: "cada céntimo se reinvierte en sí misma; escalarlo sin más capital")
Regla: 100 % de las ganancias de cada subestrategia se reinvierte en esa misma subestrategia (stake de cada peldaño = fracción de Kelly de SU bankroll).
Modelo (Kelly completo, f* = EV/σ², σ² = 4,2 por € y relleno según h5m_rampa): crecimiento diario g = n·EV²/σ² (n = entradas independientes con EV>0 por día). Stake final para 200 k€/año: s = 200.000/(EV·365·n).
| n/día | EV/€ | g (Kelly) | stake final | días desde 2 € (Kelly / ½ Kelly) |
|---|---|---|---|---|
| 2,8 | 0,08 | 0,43 %/d | 2.446 € | 1.666 / 3.332 |
| 2,8 | 0,04 | 0,11 %/d | 4.892 € | 7.315 |
| 10 | 0,08 | 1,52 %/d | 685 € | 383 / 766 |
| 20 | 0,08 | 3,05 %/d | 342 € | 169 / 338 |
| 50 | 0,08 | 7,62 %/d | 137 € | 55 / 111 |
| 50 | 0,04 | 1,90 %/d | 274 € | 258 / 517 |
Conclusión de diseño: sin capital externo, la velocidad la fijan n (oportunidades independientes/día) y EV (crece al cuadrado). Para llegar a ≥200 k€/año en ≤12 meses cada subestrategia necesita ≈20-50 entradas/día con EV ≥0,08 REAL (no el de n pequeño) Y que el stake final (137-342 €/entrada) quepa en la profundidad. Trabajo del equipo = fabricar n y EV: (1) 6 monedas × marcos 5m/15m/60m/4h × todas las ventanas anidadas; (2) variantes de entrada con más EV por selección (modelo de selección de cierres, AUC 0,75); (3) varias subestrategias no correlacionadas por mercado (sin doble conteo); (4) reinversión diaria automática por peldaño con gates y kill; (5) medir profundidad por banda para el techo de stake. Cada peldaño sigue exigiendo gates + /code-review + OK Javi.
