# ADDENDUM2 a PREREG_DB1 (§6, RMR): definición operativa de «ráfaga». PROPUESTO, NO congelado
Autor: polymarket-quantum-alpha-miner. Fecha: 2026-11-10, de 08:20 a 08:45Z. Solo lectura y 0 órdenes. No se ha tocado ningún proceso, cron, ejecutor ni código congelado.
- Días usados: solo quemados, 20-Oct..08-Nov. El 09-Nov no está extraído en el VOL y no se ha extraído. No se ha mirado nada ≥10-Nov.
- **El criterio de selección se congeló ANTES de calcular**: `addendum2/CRITERIO_PREVIO.txt`, sha256 `18310f5f61f380a0…`, a las 08:26:05Z.
- Etiqueta: es una definición contable, no un hallazgo de alfa.
- Para congelar este addendum hace falta revisión del statistical-validator y OK del chief.

## 1. Regla propuesta
**Se MANTIENE R0, la regla que passdb aplica hoy, como definición oficial de ráfaga en RMR. Estatus: DESCRIPTIVA.** No hace falta tocar el código de DB1.

Definición de R0:
- Ráfaga = ≥2 tomadores distintos en el mismo (bloque, mercado).
  - Tomador = wallet on-chain; se excluyen las direcciones de `CHAIN_CONTRACTS`.
  - Solo cuentan las filas maker de bid (side 0) con precio ≤ 0,2049.
- Relleno de ráfaga = el nuestro, emparejado por print→tx (`_TPX`), cuando cae dentro de una ráfaga.

**Por qué se mantiene**, aplicando el criterio §6 en orden:
1. Ninguna alternativa cumple las condiciones (a)-(e).
2. R0 tampoco cumple (b) en la población S_pop:
   - DISC: Δ_adj +0,106, IC90 por día −0,017..+0,217.
   - HOLD: Δ_adj −0,002, IC90 por día −0,089..+0,089; 4 de 10 días con Δ > 0.
3. Por la regla 3 del criterio: «ninguna definición discrimina de forma estable en la población general». RMR se reporta con R0 como etiqueta DESCRIPTIVA, y su poder discriminante general queda en INSUFFICIENT_EVIDENCE.

**Apoyo, que no cambia el veredicto: en la exposición de B, R0 sí separa.**
- Muestra S_sim: rellenos G0 simulados por thru1, con las guardas del motor. 12 días (26-Oct..04-Nov, 07 y 08-Nov), n=3.591.
- EV: ráfaga −0,307 €/€ frente a suelto −0,062.
- Δ_adj +0,263 (IC90 por día +0,102..+0,429). Placebo de composición: p=0,000. Δ > 0 en 9 de 12 días.
- Quitando los 2 mejores días (04-Nov y 27-Oct), Δ baja de +0,245 a +0,170.
- Por periodo: DISC +0,378 (4 de 4 días); HOLD +0,178 (IC +0,012..+0,406; 5 de 8 días).
- Ninguna alternativa mejora a R0 en S_pop ni en S_sim. Las diferencias pareadas de V_adj están dentro del ruido o son peores (§3).

**Cláusula de coherencia.** Es post hoc y se declara como tal; no es una selección estadística y no cambia nada en DB1.
- Qué exige: la banda en la que se cuentan tomadores tiene que incluir el precio de nuestro propio relleno: `BAND_MAX = max(0,20, nivel máximo del brazo) + 0,0049`.
- Por qué: si no, «el nuestro dentro de una ráfaga» (§6) es imposible por construcción.
- Efecto en DB1: ninguno. Los niveles son 0,10/0,13/0,16/0,19.
- Propuesta: añadir en passdb un `assert max(niveles) <= BAND_MAX`. Lo implementaría el execution-engineer, con revisión.
- Si RMR se calcula alguna vez sobre rellenos REALES de B, o sobre brazos con niveles >0,20, hay que contar bids ≤0,40 (R2):
  - B real operó entre 0,11 y 0,29 el 20-23 Oct.
  - En sus 125 rellenos a 0,21-0,29, R0 marca el 5 % y R2 el 40 %. Con R2: ráfaga −0,52 frente a suelto −0,09.
  - En sus 96 rellenos ≤0,20, R0 y R2 casi coinciden (40 % frente a 42 %).

## 2. Datos, unidades y guardas (detalle en el criterio)
**Fuentes**: VOL `diseccion_bots_b_09nov/{mk,feat,tok}_D`, `maker_ms_desenlaces_cache.json` (desenlace oficial, cobertura 1,000), `wallet_cluster.json` (C2, ajustado en DISC), `b_fills_vida.csv`, `q11/toxicidad_thru1/out/RT_D.pkl` (var G0) y `precursores_barrido/out/tape_D.pkl`.

**Unidades**:
- **S_pop**: bids de otros makers rellenados a ≤0,2049 en 5m ETH/SOL/XRP. Con guardas, n=312.679.
- **S_sim**: rellenos G0 emparejados a su tx por la cinta (tape): 3.421 de 3.471, el 98,6 %.
- **S_real**: 215 rellenos ETH/SOL/XRP de B, del 20 al 23-Oct, todos en DISC.

**EV**: ponderado por € (Σpnl/Σcoste).

**Guardas**:
- Horas `bad_<d>.json` de passT, donde existe el fichero (26-Oct..08-Nov). El 20-25 Oct no tiene fichero y queda sin exclusión.
- Se ha corrido también sin guardas como sensibilidad.

**Periodos**: DISC 20-29 Oct; HOLD 30-Oct..08-Nov.

**Placebos**:
- P-comp: permutación dentro de día × moneda × tick × minuto del mercado; 200 permutaciones en S_pop y 1.000 en S_sim y S_real.
- P-temp: la misma regla evaluada en el bloque ±15 (unos 30 s).

## 3. Cifras (con guardas; IC90 bootstrap por día, 2.000 réplicas)
Leyenda: Δ = EV suelto − EV ráfaga; dV = V_adj(regla) − V_adj(R0), pareado por día. En las reglas de ventana de ms, la referencia es R0f.

| Muestra | Regla | cob € | EV ráf / suelto | Δ_adj (IC90 día) | dV vs ref (IC90) | días Δ>0 |
|---|---|---|---|---|---|---|
| S_pop DISC (10 d, n=200.885) | R0 | 0,508 | −0,060 / +0,119 | +0,106 (−0,017, +0,217) | — | 7/10 |
| S_pop HOLD (10 d, n=111.794) | R0 | 0,478 | +0,045 / +0,077 | −0,002 (−0,089, +0,089) | — | 4/10 |
| S_sim TODO (12 d, n=3.591) | R0 | 0,354 | −0,307 / −0,062 | +0,263 (+0,102, +0,429) | — | 9/12 |
| S_real DISC (4 d, n=215) | R0 | 0,140 | −0,355 / −0,026 | +0,526 (+0,002, +0,909) | — | 2/3 |
| S_real DISC | R2 | 0,371 | −0,434 / +0,141 | +0,473 (+0,127, +0,777) | +0,046 (−0,004, +0,126) | 2/3 |
| S_real (subconjunto con τ, n=210) | R0f | 0,398 | −0,399 / +0,189 | +0,436 (0,000, +0,819) | — | 2/3 |

Comprobación del arnés: R0f sobre B real reproduce exactamente la disección (87/210 en ráfaga; −0,40 frente a +0,189), y R6 marca el 85,6 % de los rellenos de B, en línea con el «85 % C2» de la disección.

## 4. Alternativas descartadas (en S_pop salvo que se indique; dV pareado frente a R0)
- **R1, econ20** (cuenta también las asks levantadas del complementario a ≥0,80):
  - dV DISC +0,0025 (−0,0032, +0,0079); HOLD −0,0030; S_sim −0,0088.
  - Sin mejora.
- **R2, bids ≤0,40**:
  - dV DISC −0,0060 (−0,0088, −0,0035), peor; HOLD −0,0004; S_sim +0,0018 (−0,0106, +0,0136).
  - Solo hace falta para rellenos >0,20 (cláusula del §1).
- **R3, econ40**: dV DISC −0,0044 (−0,0099, +0,0003); HOLD −0,0042; S_sim −0,0139.
- **R4, ≥3 tomadores**:
  - Cobertura 0,29. Δ_adj DISC +0,146 (−0,028, +0,286); HOLD −0,046 (−0,178, +0,078).
  - dV +0,0033 (−0,011, +0,016). En S_sim Δ_adj +0,40, pero V_adj igual que R0 (dV −0,0024).
  - Más pura pero más estrecha: el oráculo no gana nada.
- **R5, ráfaga con ≥1 tomador C2**:
  - En DISC es in-sample (los clusters se ajustaron con DISC): +0,147 (IC>0).
  - En HOLD falla: Δ_adj −0,059 (−0,133, +0,023); dV −0,0131 (−0,0239, +0,0017).
- **R6, identidad C2 del tomador propio**:
  - HOLD Δ_adj +0,010 (−0,060, +0,086); Δ bruto −0,071; S_sim dV −0,032 (−0,086, +0,033).
  - Exige una lista de wallets congelada, y esa lista caduca: hay wallets que solo operan 5-6 días.
- **R7, ≥2 órdenes aunque sean de la misma wallet**:
  - dV DISC −0,0095 (−0,0186, −0,0008); S_sim −0,0194 (−0,0411, −0,0019).
  - Peor: que las wallets sean distintas sí importa.
- **R10, barrido** (una sola orden que rellena ≥3 makers):
  - Δ_adj DISC −0,018, placebo p=0,81; dV −0,033 (−0,053, −0,014). S_sim −0,031.
  - No discrimina.
- **R11, tamaño** (acciones del grupo ≥100):
  - Cobertura 0,17. Δ_adj DISC +0,052 (−0,245, +0,265); HOLD −0,106.
  - dV −0,018 / −0,023; S_sim −0,049 (−0,080, −0,017).
- **R8, ventana ±250 ms** (comparada con R0f sobre el mismo conjunto feat); es la más cercana a pasar:
  - Δ_adj DISC +0,167 (+0,052, +0,272); HOLD +0,019 (−0,061, +0,101).
  - Falla (c): dV DISC +0,0145 (−0,0020, +0,0335). Falla también (b) por P-temp: Δ 0,211 < 0,232.
  - S_sim dV +0,012 (−0,032, +0,056); S_real −0,012.
  - Además exige en passdb hora de print e identidad por print→tx.
- **R9, ventana ±1000 ms**: Δ_adj DISC +0,127 (+0,004, +0,243); dV DISC +0,0061 (−0,0071, +0,0199). No cumple (c).
- **Sensibilidad post hoc** (descriptiva, fuera del criterio): S_pop limitada a los niveles de B (0,10-0,20).
  - R0, Δ_adj: DISC +0,165 (+0,053, +0,258), 8 de 10 días; HOLD +0,055 (−0,037, +0,157), 6 de 10 días.
  - Ninguna alternativa mejora a R0 por dV.
  - La dilución en la población viene de los ticks 0,03-0,09, el 52 % de S_pop, donde ráfaga y suelto no se separan (+0,005 frente a −0,023).

## 5. Hallazgos adversariales
1. **El placebo temporal separa más que la regla en todas las muestras**:
   - S_pop DISC: Δ_P-temp +0,327 frente a +0,179.
   - S_sim: +0,861 frente a +0,245.
   - Su cobertura es solo del 2-6 %.
   - Lectura: la toxicidad llega en EPISODIOS (agrupada en el tiempo), no solo por coincidir en el mismo bloque.
   - Defecto de diseño de mi criterio: comparar Δ con coberturas 10 veces distintas penaliza a todas las reglas. No se corrige a posteriori.
2. **Desglose descriptivo de esos episodios**:
   - En la 2ª mitad del mercado, un relleno con ráfaga en los 30 s ANTERIORES rinde −0,154 frente a +0,024 (5,6 % de los rellenos; 14 de 20 días).
   - En la 1ª mitad, un relleno con ráfaga en los 30 s POSTERIORES rinde −0,430 frente a +0,158 (18 de 20 días). Esa información es del futuro y no es accionable.
   - → Hipótesis ex ante **H-DB3 «episodio»**: no re-pegar durante X s después de observar una ráfaga en el mercado. Hay que prerregistrarla aparte. NO se ha probado aquí.
3. **La separación es propia de la exposición de B, no de la población**:
   - En HOLD, ninguna regla de bloque separa en la población.
   - En S_sim, incluso los rellenos sueltos pierden (−0,062; en HOLD −0,141).
   - Por tanto, cancelar todas las ráfagas no llevaría a G0 simulado a EV>0. Eso es pertinente para el objetivo «B total EV>0» del §6.
4. **1º frente a siguientes dentro de la ráfaga (R0)**:
   - S_sim: −0,311 frente a −0,301; da igual llegar primero o después.
   - S_pop DISC: +0,013 frente a −0,103.
   - S_real: −0,486 frente a −0,242, con n=38.

## 6. Subvariante BTC
**DATA_BLOCKED para esta definición, y además R0 se SATURA en BTC.**
- En la población BTC (bids de 0,03 a 0,20; n=2,06 M; 20 días), R0 marca el 95,7 % (DISC 0,961, HOLD 0,949). Es un veto casi total: no discrimina.
- R4 todavía marca el 88 %.
- Las reglas de ventana de ms no se pueden calcular: feat no tiene BTC.
- R6 (identidad C2) en BTC: Δ_adj +0,122 (+0,070, +0,176) con los 20 días juntos, pero en HOLD solo +0,030 (−0,004, +0,068).
- Los 24 rellenos BTC reales (0,01-0,03; 0 de 24 ganan):
  - 18 están por debajo del suelo de extracción de mk (0,03).
  - Los 6 a 0,03 salen en ráfaga con R0, R4 y R11 (6 de 6).
  - Con 0 aciertos, una etiqueta no puede separar nada dentro de la subvariante.
- Una definición propia para BTC necesitaría extraer los rellenos <0,03 y la hora de print de BTC (contrato aparte, BTC-DB1-DESC).

## 7. Riesgo de sesgo
- **Datos ya usados**:
  - S_real y S_pop son los mismos días que usó la disección (descubrimiento).
  - S_sim se solapa con los días quemados de la aceptación de DB1.
  - Los clusters C2 están ajustados en DISC.
- **Diferencias frente a passdb**:
  - El suelo de mk (0,03) hace que mi réplica de R0 no cuente los bids de 0,01-0,02, que passdb sí cuenta. Mi réplica marca, como mucho, menos ráfagas.
  - El P&L de S_sim incluye el rebate del motor; el de S_pop no. Es una constante igual para todas las etiquetas.
- **Calidad de muestras y emparejamientos**:
  - Las reglas de ms usan feat, una muestra de ≤25k órdenes al día; el 24,6 % de S_pop no tiene τ.
  - El emparejamiento relleno simulado→tx usa una ventana de 0-400 ms.
- **Guardas**:
  - Solo las horas `bad`. El 20-25 Oct no tiene guarda.
  - No se aplica la salud de Binance (ADDENDUM1), porque la etiqueta es solo on-chain.
- **Multiplicidad**: 12 reglas × 3 muestras. La regla de decisión favorece al status quo a propósito, y quedarse con R0 no introduce sesgo de selección en DB1.
- **Cláusula del §1**: post hoc, pero su efecto en DB1 es nulo por construcción.

## 8. Siguiente paso
1. El validador revisa y congela este addendum: R0 descriptiva, más la cláusula de coherencia en forma de assert.
2. Prerregistro aparte de H-DB3 «episodio» como brazo ex ante de DB. Medida: Δ EV del brazo frente a G0 en forward ≥10 días. Placebo: pausas aleatorias con la misma tasa.

## 9. Reproducción (`experimentos/5m_barato/db1/addendum2/`)
Scripts (sha256, 16 primeros caracteres):
- `add2_dia.py` f0cef17b9758be0f
- `add2_eval.py` e7d8fca179f79806 (seed 20261110)
- `add2_extra.py` 55c70a1091b9ae83

Comandos (cada uno con `nice -n 19 ionice -c3`, `ulimit -v 3000000`):
- `python3 -I add2_dia.py 2026-10-20 … 2026-11-08` → `out/d_<D>.npz`. Tarda 22 s en total, con un RSS máximo de 528 MB.
- `python3 -I add2_eval.py [--sin-guardas] [--ticks 10 20]` → `out/eval_guardas.txt`, `out/eval_sin_guardas.txt`, `out/eval_posthoc_t10_20.txt` y `out/resumen_add2*.json`.
- `python3 -I add2_extra.py`: desglose por tick y resultados sin los 2 mejores días.

Estado: COMPLETE para los 20 días disponibles (09-Nov no extraído).
