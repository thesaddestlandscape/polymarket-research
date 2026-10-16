# 5m barato — estado exacto 16-Oct-2026 07:40Z

Objetivo de la familia: 200 k€/año como SUMA de subestrategias. **Validado hoy: 0 €** (ninguna con gates; nada con dinero).
Estimado en descubrimiento, sin validar: ~60 k€/año cota (V7 ~28-37 k€ + V6 ~30 k€), ambas con ~0 ejecuciones forward.
Live cripto = solo RESOLUTION_SNIPER_PRECIERRE (24 tuplas). Pregunta de Javi 16-Oct "¿poner v1 a operar?": NO (gates abajo).

## 1. Subestrategias vivas (forward congelado, solo observación) — datos al 15-Oct
| Pieza | Qué hace | Forward | Gates | Lectura |
|---|---|---|---|---|
| v4 (= v1 corregida) | pata 5m si bid15(s) − ask5(s) − fee ≥ 0,05 | OOS desde 06-Oct: 43 señales, 17 ejecutables, +8,36 €, EV +0,21 €/€, 9 días | 4/10 (fallan n, días, IC90 diario (−0,47,+1,13), sin mejor día −0,18, sin top5 % −0,20, sin BTC −0,36) | 1 día = 180 % del PnL; DRIFT. n=40 ~27-28 Oct |
| V2 (todas, ≤3/mercado) | variante v4 | desde 12-Oct: 5 merc., −2,57 €, EV −0,18 | 0/7 | peor que v4 en el mismo periodo (−0,002) |
| V3 (v4 + filtro Binance 5 s) | — | desde 12-Oct: V3a 1 merc., −2,12 € | 0/7 | sin n |
| V5 ORIGEN15M | desajuste nacido del 15m | desde 14-Oct: 1 señal, 0 ejec. | 3/11 | sin n |
| V6 FOK_VUELO_BTC | FOK en vuelo si el ask baja | desde 14-Oct: 1 ejec., −2,12 € | 0/7 | sin n |
| V7 DISPARO15M_BTC ⭐ | dispara con operaciones del 15m | desde 14-Oct: 0 ejecuciones | — | mejor del descubrimiento (8/8 días +, EV +1,99); ⚠️ 0 eventos BTC desde 13-Oct: ¿se secó? |

Fuentes: datalogs/vigia_5m_barato/informe.txt, v2_informe.json, v3_informe.json, m5barato_mision/v7_informe.json, logs/m5barato_forward_diario.log.

## 2. Investigación en curso
- **FV v4** (FV de ms vs mid): OOS 14-15 Oct, R² Δmid 3 s 0,28/0,29, ΔBrier −0,003/−0,003, tomador M=0,05 n=457 +0,095 €/€ (+0,049 / +0,142). 2 días: no concluye. Cron 05:50.
- **Cosechar pares al abrir (A 5m normal / B 5m barato con defensa 15m)**: ⚠️ NO TERMINÓ (murió con la sesión del 15-Oct tras 05-06 Oct; sin informe). Relanzar fuera de 06-09Z: `nice -n 19 ionice -c3 python3 analisis_5m_cosechar_apertura.py`.
- **Fase 2 invisible (wallets baratas)**: ⚠️ NO ARRANCÓ. Detrás: `nice -n 19 ionice -c3 python3 analisis_5m_wallets_baratas_invisible.py`.
- Wallets que compran barato: makers baratos BTC +0,044 (≤0,10) / +0,082 (0,10-0,20); ganadoras 05-09 → +0,057 en 10-14 (IC90 días +0,022..+0,087) vs placebo −0,003.
- @mo-money: +10,4 k$/10 días = pares −15,9 k$ + dirección +26,3 k$ (maker direccional); 1ª pata barata +5,5 pp sobre el precio.

## 3. Infraestructura
- F1 (15-Oct, real): tomador ≈215 ms a casado; maker ≈50 ms en libro; cancelar en taker delay imposible.
- F2 (16-Oct, DRY-RUN en vivo de v4 y V7): `f2_5m_barato_dryrun.py` (2 procesos), firmador en proceso aparte (ArmeroProceso, 05a1082755, 3 pasadas /code-review). Conciliación 17-Oct: `python3 analisis_f2_5m_barato.py --dia 2026-10-16`. Criterios F2→F3 congelados en `informes/ejecutor_baja_latencia_diseno_15oct.md`.
- ref5 llega +1,31 s p50 / +1,78 p90 (>1,5 s en 25 %); 0/52 eventos v4 detectados antes → forward no inflado.

## 4. Cementerio
Pares 5m maker (OOS −0,050) · maker un lado · copiar makers ganadoras · copiar tomadoras persistentes · FV v1-v3 · LOWLOW-PAIR · BTC5M-FV-LONGSHOT · retraso deliberado · vender bid15 rancio · órdenes armadas/cancelar en delay · caja 2 patas a 250-400 ms (−35/−179 $).

## 5. Sin empezar
Caja en altcoins (pastel 10 d: XRP +703 $, DOGE +203, BNB +53; BTC −7.553, ETH −1.824, SOL −859) · anidados con 4h · caja maker 2 patas · maker con valor justo 4/4b (depende de FV v4).

## 6. Siguiente, en orden
1. Hoy fuera de 06-09Z: relanzar cosechar al abrir → fase 2 invisible.
2. Diagnosticar V7 sin señales (consulta barata al registro).
3. 17-Oct: 1ª conciliación F2; medir decisión→envío con firmador aparte.
4. Forward v4 y FV v4; si FV v4 aguanta ≥5 días → congelar maker con valor justo (subestrategia 4).
Pendiente con Javi: hallazgo #10 de las reviews (ejecutor_rapido/F2 en main, no en dev).
