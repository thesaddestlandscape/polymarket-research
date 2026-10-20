# V4 «comprar lo bueno» — informe 20-Oct-2026 (P2, Javi 19-Oct)

**Veredicto: NO CAPTURABLE como tomador (causa estructural). Maker H23: n insuficiente y simulador sin calibrar.** Todo con desenlace oficial (cobertura 100 %), EV ponderado por €, ask real nivel 1, relojes por recepción. Etiqueta: EXPLORATORY.

## 1. Quién se lleva el ask y cuándo (58 señales V4, 06-18 Oct; 84 con re-armes)
- 48/58 consumos con wallet on-chain; 38 wallets. Dominan 0x9783f45c (BTC, 5.982 fills/9 días, EV pond +0,28) y 0xe38cc08b.
- 1ª compra rival: recepción−t0 P50 49-57 ms (P10 −1, P90 177; n=29). Su print nos lleva **P50 188 ms** (P10-P90 68-246) sobre nuestro casado. Con retraso tomador ≥145 ms, **26/29 se enviaron antes de que viéramos el trigger**; 17/29 ya compraban en los 3 s previos.
- Nivel desaparecido <145 ms tras el trigger: consumo 11/16, cancela/recotiza 12/13 (el maker reprecia con la misma info).
- Al envío acotado los rivales (9.600 fills, 3 wallets) tienen margen V4 ≥0,05 solo en el 4,4 %; ≥−0,05 en el 61 % (placebo 21,5 %): **compran con umbral más laxo, no esperan nuestro trigger**.
- Binance llega a nosotros con P50 136 ms. Fuentes: `cronologia_58_senales.csv`, `r2/competidor.txt`, `r3_res/analisis_final.txt`.

## 2. Pérdida por latencia nuestra vs estructural
- F2: evento→decisión P50 0,8 ms; t_det F2−vigía P50 +2 ms (n=18): lo nuestro ya es mínimo. Quedan 215 ms (145 de retraso tomador + ~70 de red).
- 33 señales no rellenadas a 215 ms: 26 ganan. A 150 ms (suelo físico, inalcanzable) se recuperan **6/26 (23 %, +14,8 €)**; **20/26 (77 %) se pierden con cualquier latencia ≥145 ms**.
- Réplica BTC (10 días, 30 señales): L150 +0,99 (n=20), L215 +1,06 (n=13, sin 2 mejores días +0,08), L250 +0,83 (sin 2 mejores −0,10). Vigía OOS hasta 19-Oct: L215 +0,16 (27 ejec.), L250 −0,04.

## 3. Ingeniería inversa y precursor
- Mejor precursor = el propio margen: AUC de «V4 en los próximos 500 ms» 0,79 (DESC) / 0,82 (TEST); Binance r250/r1000 0,50-0,53; Δbid15 1 s 0,56-0,62. Binance ≥1 bp previo: 29 % de eventos vs 8 % de placebo, pero ~13 aciertos entre 1.188 episodios (precisión ≈1 %).
- Tomador anticipado (1er instante por cierre, 13 días, IC90 por cierre): m≥−0,03 → **−0,42** (n=214); m≥−0,03 + Binance → +0,64 DESC → **−0,71** TEST (no persiste); +Δbid15≥1c → +0,27 (0,00;0,60), sin 2 mejores días −0,03.
- Único hallazgo: **umbral 0,02 en vez de 0,05** → 24 ejecutables (V4: 12), EV +0,51 IC90 cierre (0,03;1,03), DESC +0,52/TEST +0,47, sin 2 mejores días +0,11. Exploratorio (≈16 reglas probadas, sin corrección): no sustituye a V4.
- Falsador: toda regla anticipada debe batir a V4 emparejada en cierres posteriores al 18-Oct (IC90 por cierre >0) o queda REJECTED.

## 4. Maker H23 (bid join en 5m lado s, margen ≥−0,05, cancela a 60 ms, rebate 20 %)
- Preregistrada: 43 cotizaciones, 17 rellenos, 9 días: EV pond **+0,80**, IC90 días (0,20;1,38), **sin 2 mejores días +0,25**, P(≥|acierto=precio)=0,021. Sin cancelar (control): +0,06 (n=31), coherente con la población real (H5M +0,003/+0,04), así que el simulador no inventa edge incondicional.
- Los rellenos «buenos» son 9 sin desplome (8 aciertos) y los 8 con desplome del bid pierden (−0,38; corte post hoc). Dos rellenos de 20 acc (>2 €) aportan 26 € de 37: sin ellos ≈ +0,33.
- Rellena 6/14 de las ganadoras perdidas por el tomador. Capacidad ≈1,3 rellenos/día: techo ~1 €/día a 2 €.
- Simulador NO validado contra órdenes reales (H47 pendiente; cola en desplomes y latencia 68 ms no verificables).

## Siguiente prueba
1. Congelar hoy el umbral 0,02 como V4b en sombra (n≥40 ejec., ≥10 días).
2. Mantener el maker H23 en simulación diaria con estas reglas y decidir micro-orden real solo tras H47 (OK Javi, /code-review).
3. Huecos: 19-20 Oct sin extraer; fills≠unidades en D; GBM omitido; la hora de envío rival es una cota con retraso supuesto de 145 ms.

Código: `r3/`; intermedios: `/mnt/HC_Volume_106538179/datalogs_analisis_caches/v4_comprar_lo_bueno/r3_out|r3_res`.
