# W1 — Tendencia/régimen para B y qué hacen las wallets ganadoras de ETH según tendencia (23-Oct-2026)
Estado: **EXPLORATORY / sin regla validada.** Solo lectura (B, supervisor, ejecutores, crons sin tocar; sin órdenes ni claves). `nice 19 ionice -c3 ulimit -v ≤4,5 GB`; salida 27 MB.
Prereg congelado ANTES de calcular: `PREREG.md` (sha256 303c2090…, `sha256sum -c PREREG.sha256`). Lo añadido después va marcado POST-HOC. Hashes de scripts/salidas: `HASHES.txt`.

## 0. Respuesta corta
1. **Ningún indicador simple de tendencia separa el EV de B ni de la población cumpliendo el criterio preregistrado** (mismo signo DESC→TEST + IC90 por cierre en TEST que excluya 0 + placebo + max-estadístico + ≥4/6 días). Tres cumplen todo MENOS el IC por cierre en TEST. El candidato más cercano es **«tendencia previa a la ventana a favor del lado barato → peor EV»** (`rpre`, `r900`): el longshot comprado A FAVOR de la tendencia de los 15 min anteriores rinde peor que el comprado EN CONTRA. Pero es **dominado por los 3 días malos 17-19** y desaparece en 20-22 en € (§2). No es una regla de B hoy; es una hipótesis para forward.
2. **Los indicadores contemporáneos (Binance 60 s / desde la apertura, flujo de prints 60 s, bid15) no aportan**: signo inestable entre periodos (r60, rop, f60 invierten en TEST; rop −0,36 en TEST vs 0,00 en DESC).
3. **B real no distingue del placebo** (n=175; rpre Δ −0,43 pero placebo estratificado p=0,36; IC por cierre incluye 0). No se infiere nada de B solo.
4. **Las wallets ganadoras de ETH (0xf074dc84, 0x0ab01745) NO se adaptan a la tendencia a nivel de fills**: su cuota de fills «a favor de tendencia» y su tamaño son los de los demás makers del mismo mercado y precio (diferencias de ±0,3–2,6 pp, con IC que a veces excluye 0 por n enorme pero sin tamaño económico). Son market makers neutrales (asks en ambos lados, 0,3-0,7), no direccionales. Su EV (+0,012/+0,015 por €, sin rebate) viene de otra cosa (precio/cola/inventario acotado: `pares_huecos/GANADORES_PARES…`), no de leer tendencia. **Qué regla simple replica «evitar el lado contrario a la tendencia»: ninguna, porque no lo hacen.** La cancelación/recotización NO es observable (solo fills): inidentificable.
5. **Qué sí sale como pista simple y barata**: B ya compra longshots (0,10-0,30); entre ellos, el tramo comprado en CONTRA de la tendencia previa (reversión del régimen de 15 min) es el menos malo, y el comprado A FAVOR el peor. Medir en forward con ≥10 días **sin tocar B**: etiqueta pasiva `rpre`/`r900` en cada orden y mirar si Δ(CON−CONTRA) < 0 persiste.

## 1. Datos, unidades, definiciones (observado vs inferido)
- Población: `cola_posicion/datos/pop_units_*.csv.gz`, ETH/SOL/XRP 5m, 17-22 Oct, 5 acc por maker-mercado-lado, pc 0,10-0,30, T 60-300 s, **28.871 unidades con desenlace** (215 sin desenlace excluidas), coste 28.716 €, EV −0,0215. DESC 17-19 (14.7k), TEST 20-22 (13.6k; EV +0,074: el 21-Oct fue +973 €, así que el régimen cambia de signo entre periodos).
- B real: `salida/datos/unidades_b.csv`, 175 posiciones (coste 193,6 $, PnL −2,32 $); t0 = `t_det − 4 s` (9 sin t_det: `primer_fill_chain − 5 s`, marcadas; 9 salen con NaN en Binance = missing).
- **t0 (inferido):** población/wallets = hora de BLOQUE on-chain − 5 s (el bloque llega ~2,4 s después del casado; −5 s deja los indicadores dentro de la vida de la orden y sin mirar el barrido). B = detección − 4 s. NO es el instante de envío de las órdenes (inidentificable en población).
- Binance (aggTrade con RECEPCIÓN, `ms_D.npz`), libro 15m y prints 5m del mismo registro; todo con recepción ≤ t0. Indicadores orientados al lado comprado (CON = a favor). Cobertura 94-99 % (`an1.txt`). Cero/NaN = missing, no CONTRA.
- Indicadores: r300 (primario), r60, r900, rop (desde apertura de la ventana), rpre (900 s ANTERIORES a la apertura = régimen previo), b15 (mid 15m del mismo lado − 0,5), d15 (Δ mid15 en 300 s), f60 (flujo tomador neto equivalente-Up 60 s).

## 2. Población: ¿separa el signo de la tendencia previa al relleno el EV? (`datos/an1.txt`, `scripts/an1.py`)
Δ = EV(CON) − EV(CONTRA), EV ponderado por € (Σpnl/Σcoste). IC90 por cierre (bootstrap de `fin`, ~1.700 cierres/periodo), por día entre paréntesis (3 clusters, no decide). Placebo: permutar (pnl,coste) dentro de dia×moneda×lado×cubo de precio 0,05, 1.000 permutaciones.
| ind | Δ DESC 17-19 | IC90 cierre DESC | Δ TEST 20-22 | IC90 cierre TEST (día) | placebo TEST p (una cola, sentido DESC) | días mismo signo (de 6) | veredicto prereg |
|---|---|---|---|---|---|---|---|
| r300 (primario) | +0,061 | −0,11,+0,23 | +0,066 | −0,11,+0,25 (−0,01,+0,14) | 0,048 | 4 | FALLA IC |
| r60 | +0,198 | +0,06,+0,34 | **−0,087** | −0,22,+0,04 | 0,95 | 3 | REFUTADA (invierte) |
| r900 | **−0,287** | −0,43,−0,13 | −0,062 | −0,27,+0,14 (−0,16,+0,08) | 0,032 | 5 | FALLA IC |
| rop | +0,002 | −0,18,+0,20 | **−0,360** | −0,54,−0,14 | 1,00 | — | REFUTADA (invierte) |
| **rpre** | **−0,250** | −0,42,−0,07 | **−0,103** | −0,31,+0,11 (−0,23,+0,03) | **0,001** | 4 (17,18,19,21) | FALLA IC (único con placebo+max-stat OK) |
| b15 | −0,059 | −0,23,+0,12 | −0,046 | −0,24,+0,16 | 0,16 | 4 | FALLA |
| d15 | +0,009 | −0,17,+0,18 | +0,024 | −0,20,+0,24 | 0,30 | — | FALLA |
| f60 | +0,033 | −0,08,+0,13 | −0,056 | −0,17,+0,06 | 0,95 | — | REFUTADA (invierte) |
p max-estadístico entre los 8 indicadores (TEST, dirección fijada en DESC): **0,043** (lo impulsa rpre).
- Contexto: las clases tienen el mismo precio medio (pcCON ≈ pcCONTRA ≈ 0,20-0,22) y casi el mismo acierto (rpre DESC 15,9 % vs 21,4 %; TEST 21,0 % vs 23,7 %): no es un efecto de precio.
- **POST-HOC** (no preregistrado): rpre Δ es negativo en las 3 monedas y en ambos periodos (DESC ETH −0,23/SOL −0,36/XRP −0,16; TEST −0,12/−0,07/−0,14) y monótono con la magnitud de la tendencia (|rpre| bajo/medio/alto: CONTRA−CON = +0,11/+0,21/+0,23). Es la pista más coherente, pero:
- **Regla de uso (TEST, quitar la clase CON de rpre = 44 % del coste):** EV retenido +0,114 frente a +0,074, **pero el PnL total BAJA −140 €** (placebo −453 €, p=0,002 = mejor que quitar al azar, aun así negativo). Por día de la población, ΔPnL de quitar CON(rpre): 17 +376, 18 +523, 19 +827, 20 +38, 21 **−38**, 22 **−140** (base de esos días −237,−739,−636,−138,+973,+160). Con r900: +359,+518,+720,+112,−115,−222. **El efecto vive en los días en que la población perdió; cuando los longshots ganan (21-22) quitar el lado «a favor» cuesta.** Es la trampa conocida «EV sube y el PnL total baja» + «dirección del día». Si el capital es el límite (B: 13 $, tandas de 5 $) el EV por € sí importa; eso decide el simulador calibrado, no este informe.
- Todas las demás reglas «skip» salen peores que el azar en PnL o con p>0,05 (r60 p 0,96, f60 0,97, rop 1,00).

## 3. B real (n=175; `datos/an1.txt`, `an3.txt`) — descriptivo, NO decide
rpre: CON n=85 EV −0,225 (PnL −21,2 $) vs CONTRA n=89 EV +0,204 (+20,1 $), Δ −0,43, IC90 cierre (−0,97,+0,10); placebo estratificado p=0,36 (las strata son de 2,6 unidades; placebo media −0,34 = poca potencia). r900 Δ −0,30 (p 0,63). r300 Δ +0,43 (n 41 vs 118, p 0,12). Misma dirección que la población en rpre/r900, pero indistinguible del placebo. B no tiene potencia para esto (pagos 4-9×).

## 4. Wallets ganadoras de ETH según tendencia (`datos/an2.txt`, `scripts/an2.py`)
17.787 fills (1.322 mercados) de 0xf074dc84 y 16.488 (1.550) de 0x0ab01745, rol maker, ETH 5m 17-22 Oct, lado largo efectivo (sus asks = compra del contrario). Comparación: cuota de fills CON-tendencia de la wallet frente a la cuota de los otros 319-321 k fills de makers ETH en el MISMO mercado y cubo de precio 0,10 (IC90 por cierre):
- Diferencia de cuota CON (wallet − esperada): 0xf074: r300 −1,1 pp (−1,6,−0,6), r60 −2,0, rop −1,7, rpre −0,3 (cruza 0), b15 −1,1, **f60 +2,6 pp (+2,0,+3,2)**; 0x0ab0: todas entre −0,7 y +0,6 pp, la mayoría con IC que cruza 0. **No evitan el lado contrario a la tendencia** (cuota CON ≈ 0,47-0,53 igual que el resto). Con tendencias grandes (|r300|>p80 ≈12 bps) 0x0ab0 pasa de 0,507 a 0,543 CON, 0xf074 de 0,498 a 0,511: efecto marginal.
- Tamaño: acc medio CON vs CONTRA 6,4/6,2 (f074 r300) y 6,9/6,8 (0ab0); mayor tamaño del lado a favor de rop/f60 (+0,6-0,9 acc) pero ~10 %: clips de 5 acc estables.
- EV (sin rebate) por clase: f074 CON +0,026/CONTRA −0,010 (r300), 0ab0 +0,031/−0,009; los otros makers +0,016/−0,032. Es decir, el lado «a favor de tendencia» rinde algo más para todos y las wallets lo capturan igual; su ventaja global (+0,012/+0,015 vs −0,003) está en AMBAS clases.
- **Lectura (inferencia):** son neutrales a la tendencia al nivel observable; si la gestionan es cancelando/recotizando (no observable). No hay regla de lado que copiar. Su alpha sigue siendo cola+inventario acotado+reequilibrio (H39b; fuera de este alcance y aún sin simulador calibrado — E1).
- No hecho: 0x21f4c1a1 (BTC): los `btc_ms_D.npz` no contienen Binance; habría que reconstruirlo de `maker_ms`. Pendiente si el chief lo pide.

## 5. Propuesta (solo hipótesis, para el simulador calibrado de E1/A1)
H-W1: «B no pujar el lado que va A FAVOR del régimen de los 15 min previos a la ventana (|rpre|≥ mediana ≈7,7 bps)». Timestamp de decisión: apertura de la ventana 5m (la tendencia previa ya es pasado a esa hora), sin dependencia de latencia. Debilidades que ataca: continuación intra-ventana contra una apuesta de reversión. No-entrada: CON y |rpre|≥7,7 bps. Refutaría: EV(CON−CONTRA) ≥ 0 en ≥10 días forward (IC90 por cierre), o PnL total del skip < placebo en el simulador calibrado, o que desaparezca al medir con 10-16 Oct (días disponibles en `VOL/m5_registro`, no usados aquí). Sin esto, **no cambiar B**.

## 6. Límites y avisos
- 6 días (17-22 Oct, el 22 parcial hasta ~14:40Z); régimen de día domina (EV DESC −0,10 vs TEST +0,07). IC por día con 3 clusters no vale; por cierre sí pero cierres de la misma hora de distintas monedas están correlacionados (el bootstrap por `fin` ya los agrupa).
- 8 indicadores × 3 periodos: se corrigió con max-estadístico solo en TEST; el resto de p son sin multiplicidad. POST-HOC por moneda/magnitud no corrige.
- t0 = bloque − 5 s es aproximado; B usa detección − 4 s. No hay sensibilidad a t0 (r300/r60 son los más sensibles; rpre/r900 no: ventana de 15 min).
- Binance ≠ Chainlink TWAP de resolución. f60 usa prints del 5m (dos filas por casación en el firehose; aquí se usan los prints del registro ms del CLOB, no el firehose).
- Wallets: solo fills (sin órdenes ni cancelaciones); las wallets fueron elegidas por Javi viendo su EV (no circular para el descriptivo de conducta, sí para cualquier lectura de EV); rebates no sumados; BTC 0x21f4 no hecho.
## 7. Reproducir
`cd /tmp; ulimit -v 4500000; nice -n 19 ionice -c3 python3 …/tendencia_wallets/scripts/feats.py` (→ `datos/feats_{pop,b,wal}.csv.gz`) → `an1.py` → `an2.py` → `an3.py` (→ `datos/an{1,2,3}.txt`). Entradas solo lectura: `../cola_posicion/datos/pop_units_*`, `../salida/datos/{ms_D.npz,unidades_b.csv}`, `../pares_huecos/datos/fills_alts.csv.gz`.
