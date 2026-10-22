# Barrido de palancas contra la seleccion adversa de B (H47-B maker) -- 22-Oct-2026
Estado global: **EXPLORATORY**. Ninguna palanca convierte a B en EV positivo; una (actividad del mercado) reduce la perdida y es concordante en dos instrumentos. Nada toca B real.

## 1. Instrumentos (dos, independientes entre si) y su fidelidad
1. **Poblacion** (`scripts/build_units.py`, datos `datos/units/`): rellenos on-chain de OTROS makers ETH/SOL/XRP 5m, 09-21 Oct (21 parcial), pc 0,10-0,30, T 60-300; unidad = primeras 5 acc por (maker, mercado, lado); 113.918 unidades, 110.069 EUR, desenlace oficial 100 %. EV de la poblacion: A(09-13) +0,040, B(14-17) +0,069, C(18-21) -0,055 (cambio de regimen justo cuando corre B). Rasgos solo con casados >= 4 s antes del primer relleno. Limitacion: no tiene el contrafactico de las NO rellenadas.
2. **Simulador de cinta** (`scripts/sim_tape.py`, `sa_sim.py`, `datos/sim/`): pujas tipo B (ETH k=2, SOL/XRP k=1 bajo la ultima operacion, repeg 5 s, T 295-65, 5 acc, relleno si hay operacion del lado a precio estrictamente menor), 10.706 mercados, con contrafactico. Reproduce de B real: acierto de lo relleno 20,0 % vs 21,9 %, markout 5 s mediana -0,167 vs -0,13, fill 88 % vs 72 %. NO reproduce: no rellenadas 74 % vs 37,1 % ni el precio medio (0,242 vs 0,215; usa ultima operacion, no el bid top). **Nivel absoluto del simulador (-0,17) no transferible; solo efectos relativos y solo si replican en la poblacion.**

## 2. Magnitud de la seleccion adversa y parte irreducible (simulador, n=9.334 rellenos de 10.665 pujas, 13 dias)
- EV si se rellenara SIEMPRE la 1a puja cotizada (sin seleccion): **+0,064/EUR**; EV de lo realmente rellenado: **-0,173** (IC90 por dias -0,199,-0,148; 0/13 dias +) -> seleccion adversa = **0,237 por EUR**. Rebate maker estimado 20 % de la comision: +0,011 (no cambia nada).
- Descomposicion por "overshoot" (cuanto cruza la operacion por debajo de nuestra puja): <=3,5c (40 % de rellenos): EV ~ -0,015; >3,5c (60 %): EV ~ -0,28 (>7c: -0,426, n=2.486). La perdida es barridos de tamano, impredecibles antes del relleno. Markout medio sobre el precio de relleno: +5 s -0,19; +30 s -0,17; +120 s -0,12; resolucion -0,17 -> salir no recupera nada.
- Mejor regla (R1) recupera 0,029 de 0,237 (**12 %**); **~88 % irreducible** con rasgos de cinta/Binance. Poblacion: tras R1 el EV de lo pujado en 18-21 Oct es -0,009 (IC90 por dias -0,041,+0,067): consistente con 0, no positivo.

## 3. Ranking de palancas (familia probada: 193 reglas poblacion + 147 simulador + ~35 variantes de parametros del simulador + 1 modelo; max-estadistico por permutacion de filas dentro de dia, 300 perms, walk-forward A/B/C; "p_fw" = p familiar)
| # | Palanca | Resultado | Etiqueta |
|---|---|---|---|
| 1 | **Actividad del mercado**: descartar si <26 acc casadas en 30 s (vol30; sim: sh30, v30, edad de la ultima operacion) | Pob.: A +0,116 (t 4,03, p_fw 0,010), B +0,065 (t 2,02), C +0,055 (t 1,72) en EV(pujar)-EV(descartar); sim 09-15 p_fw 0,003-0,013 y 16-21 t 2,1-2,5. Descarta 14 % de las unidades. Unica concordante en ambos instrumentos | PROMISING (debil) |
| 2 | **Noche 00-04 UTC** | Pob.: A +0,083 (t 3,52, p_fw 0,027), B +0,051 (1,73), C +0,207 (t 7,39); 11/13 dias peor; solo ETH (-0,127, IC90 d (-0,221,-0,031)); sim no concordante en descubrimiento (t 0,00), holdout t 1,8 | EXPLORATORY |
| 3 | d_open pequeno (lado barato desde la apertura) | A y C si (t 4,3 y 7,9), B no (t 0,33) | EXPLORATORY, no congelada |
| 4 | Sin XRP (H62) | Sim: -0,294 vs -0,123 (13 dias). Pob.: A t 5,5, B 1,1, C -0,14 (la penalizacion desaparece 18-21) | INCONCLUSA: H62 sigue su preregistro |
| 5 | T tardio / parar pronto (T>=183) | Sim: parar a T<=180 mejora -0,174 a -0,128 pero empezar tarde empeora (-0,214 a T0 240; -0,27 a 180). Pob.: C revierte (t -2,78, n 28.704) | REJECTED (contradiccion entre instrumentos) |
| 6 | Binance en contra (b10, z, fv_gap) | Pob.: z<=-0,54 revierte en C (t -3,34); consistente con H26-MS | REJECTED |
| 7 | Profundidad/banda de la puja (delta -2..+6, pmin, pmax, puja estatica 0,10-0,30) | Sim: -0,161 a -0,192 con delta; estatica -0,18 a -0,27; n 7.241-9.434. No mueve | REJECTED |
| 8 | Modelo logit multi-rasgo (17 rasgos, ajustado 09-15, evaluado 16-21 una vez) | AUC 0,604/0,603 (casi todo precio); decil superior +0,239 -> hold -0,068 (IC90 d (-0,196,+0,125), n 5.676) | REJECTED |
| 9 | Tomadores informados (inf120, requiere feed de wallets) | p_fw 0,02 en 09-15; no aparece entre las 24 de A en el walk-forward | REJECTED |
| 10 | Lado contrario / favorito 0,70-0,90 | Cinta completa (n 270k rellenos, 3,3 M EUR): EV -0,003..+0,011, IC90 incluye 0 | REJECTED (sin AS pero sin edge) |
| 11 | Salida posterior (vender a +5 s) | Markout -0,19 peor que mantener -0,17 (n 9.334) | REJECTED (cierra H40/H41 con otra via) |
| 12 | Pares/cobertura | Cementerio (-0,050 OOS), no repetido | sin retest |
| 13 | Tamano, posicion en cola, join vs mejorar | No observable en cinta | DATA_BLOCKED |
| 14 | Cambio del bid 15m, spread/profundidad L2, saltos Chainlink | No medidos (el registro ms solo retiene 4 d, 18-22 Oct) | DATA_BLOCKED |
Reglas descartadas por no pasar replicacion en B y C (p. ej. blk30, vol30>=487, act!=XRP, T>=122): REJECTED con n por periodo en `datos/scan3_units_reglas.csv`, `scan_units_reglas.csv`, `scan_sim_reglas.csv`.

## 4. Regla congelada (`reglas_congeladas.json`, hash sha256 22296520783df1d1...)
R1 = R1a (no pujar con <26 acc casadas en el mercado en 30 s) AND R1b (no pujar 00:00-03:59 UTC). Poblacion EV pujar vs todas: A +0,070/+0,040, B +0,080/+0,069, C -0,009/-0,055; ABC +0,054 (IC90 d +0,019,+0,090; sin 2 mejores dias +0,027; 8/13 dias +) frente a +0,025 (descartado -0,058). Retiene 71-74 % de EUR. Simulador: -0,144 vs -0,173, PnL -1.156 vs -1.942 EUR (5 acc). **Descuento por seleccion**: C no era virgen para R1 (se vio t_C al elegir finalistas) y el ABC es in-sample; el valor real solo lo da el forward.
Falsador: forward >=10 dias, diferencia EV(pujar)-EV(descartar) con IC90 por dias > 0 y n descartado >= 5.000; muere si desaparece al medir vol30 con el WS del CLOB.

## 5. Huecos y avisos
- 21-Oct parcial; hora de poblacion = bloque -2,4 s (+-1,5 s); bookTicker no es tick a tick; XRP/ETH/SOL solo. Cobertura de desenlace 100 %.
- vol30 on-chain vs WS del CLOB sin medir equivalencia. El valor sobre B real es pequeno (~+0,03-0,05 por EUR sobre ~70 % del volumen) y su efecto sobre rellenos de B (n=73) no es medible; la regla no sustituye al forward de >=10 dias.
- Periodo C negativo (-0,055) para toda la poblacion: parte de la perdida de B es regimen, no seleccion adversa de B.
- Datos efimeros: retencion on-chain 4 d (extraer diario si se hace forward); scratch de origen `/tmp/.../46569fb1.../scratchpad` (pop_*.pkl, alt_*.csv) no persistente, `datos/units/` y `datos/sim/` si lo son.
## 6. Reproduccion
`build_units.py S OUT` -> `scan_units.py N`, `scan3.py N`, `model_units.py`, `eval_r1.py`; `sim_tape.py S OUT dias` -> `fill_table.py`, `scan_sim.py N`; `an_full_tape.py`. Todo con nice 19, ulimit -v 3 GB; max RSS 1,0 GB.

---
# ESTADO INTERMEDIO 22-Oct ~09:30Z (tras los 4 encargos nuevos; se actualiza al final)
HECHO y verificable:
- HASH: `reglas_congeladas.json` v1 en disco = sha256 4550b14b...ec0a7 (hash del FICHERO, que contiene el campo hash interno); mi 22296520... era el hash del contenido SIN ese campo (circular). Copia congelada `reglas_congeladas_v1.json` + `HASH_v1.txt` (`sha256sum -c HASH_v1.txt` = OK) y `HASH_v1.LEEME.txt`. Desde v2 el hash vive solo en `HASH.txt`.
- FORWARD R1 en marcha (solo medicion): `scripts/r1_fwd_extract.py` (on-chain -> unidades, `datalogs/sa_r1/units_DIA.csv.gz`, gz, retencion 90 d, fuera de git), `scripts/r1_fwd_vigia.py` (gate+falsador, Telegram solo con veredicto nuevo), `scripts/r1_fwd_cron.sh` con `|| aviso`; cron 10:40Z diario (`crontab` respaldado en `datos/crontab_backup_22oct.txt`). Validacion del extractor: 20-Oct 8.748 unidades EV -0,033 vs 8.888 / -0,034 de build_units. Dias forward = >= 22-Oct. Lectura 0 (pre-forward, 21-Oct tras las 10:08Z, no vista al fijar R1; n=4.538): EV todas +0,246; R1a pujar +0,271 vs descartar +0,123 (n 3.736/802); R1b no aplica (la franja nocturna ya estaba en la primera mitad). 20-Oct: R1 pujar +0,001 vs descartar -0,138 (n 6.578/2.170).
- Postmortem re-ejecutable de B real: `scripts/b_postmortem.py` (ledger `experimento_h47_B_ledger.jsonl` + gamma, celdas moneda/T/precio/hora/cola/spread/repegs/dia, EV pond., IC90 por mercado, sin 2 mejores, p familiar max-estadistico, mitades cronologicas). Primera lectura (hasta 22-Oct 08:57Z): 209 pujas, 128 rellenos (61 %), EV +0,157 (IC90 -0,157,+0,471), sin 2 mejores +0,032; acierto relleno 0,250 vs no relleno 0,383 (n=81); markout 5 s mediana -0,103; 3 dias; ninguna celda con p_fw<0,7 (todo EXPLORATORY). Hipotesis a vigilar con 300-500 pujas: spread del libro al pujar <=0,02 (n=89, EV +0,394, IC90 (-0,012,+0,847)) frente a >0,02 (n=39, -0,32/-0,44).
- Aritmetica de capacidad (ETH/SOL/XRP, banda 0,10-0,30, T>60, 09-21 Oct, `datos/tape_celdas.csv`): flujo maker TOTAL 32.823 $/dia, pnl de TODOS los makers +868 $/dia (EV +0,026 bruto) = 317 k$/ano antes de rebate (rebate estimado +122 k$/ano); ETH EV +0,032, SOL +0,041, XRP -0,056. Una wallet "media" (~195 makers/dia) mueve ~43 $/dia: B ya es del tamano medio (42 $/dia). 200 k$ exigirian ~63 % del bote de esa banda.
EN CURSO / PENDIENTE: extraccion del registro ms 17-21 Oct (fallo por memoria en el 1er intento, reescrita compacta), sim con libro real (`sim_v2.py`), rasgos de libro/15m/spread (`attach_ms.py`), tarta de todas las monedas (`an_pie.py`), disenos que cambian el modelo (`an_v2.py`), camino a 200 k, reglas v2 + HASH.txt.

---
# PARADA ORDENADA 22-Oct ~09:50Z (apagado del servidor por rescale) -- punto exacto de reanudacion
Procesos: ninguno en marcha. Cron instalado y que se mantiene: `40 10 * * *` -> `scripts/r1_fwd_cron.sh` (forward R1, solo medicion). Respaldo del crontab previo: `datos/crontab_backup_22oct.txt`.
HECHO: informe v1 + reglas_congeladas.json v1 (hash del FICHERO 4550b14b...ec0a7; `sha256sum -c HASH_v1.txt`; el 22296520... era el hash del contenido sin el campo hash, circular); forward R1 (extractor `r1_fwd_extract.py` validado: 20-Oct 8.748 unidades EV -0,033 vs 8.888/-0,034; vigia `r1_fwd_vigia.py`; cron). Lectura 0 pre-forward (21-Oct tras 10:08Z, n=4.538): EV todas +0,246; R1a pujar +0,271 vs descartar +0,123. Postmortem re-ejecutable de B real `scripts/b_postmortem.py` (209 pujas, 128 rellenos, EV +0,157 IC90 (-0,157,+0,471), sin 2 mejores +0,032; hipotesis spread<=0,02: n=89 EV +0,394 vs n=39 -0,3/-0,4). Capacidad: el bote maker de la banda ETH/SOL/XRP 0,10-0,30 es 868 $/dia = 317 k$/ano para TODOS los makers antes de rebate; 200 k exigiria ~63 %.
Datos guardados: `datalogs/sa_ms/ms_2026-10-17.npz` (registro ms 17-Oct, compacto), `datalogs/sa_r1/units_2026-10-20/21.csv.gz`, `datos/units/`, `datos/sim/`, `datos/tape_celdas.csv`.
PENDIENTE, en orden:
1. `python3 scripts/ms_extract.py 2026-10-18 2026-10-19 2026-10-20 2026-10-21` (de uno en uno, nice 19). El 18-Oct fallo por memoria al concatenar 21 M filas q (con mas RAM va tal cual). PRIORIDAD: el registro ms rota a ~5 dias (`ls /root/polymarket-research-datalogs/maker_ms_2026-10-1*`).
2. `scripts/sim_v2.py S OUT dias` (S = scratch /tmp/.../46569fb1.../scratchpad con alt_*.csv y gmap*.json: PUEDE HABERSE PERDIDO con el apagado (tmpfs); regenerar con b_lecciones_wallets/scripts/gmap.py y gmap19.py y alt_19..21 desde datalogs/onchain_fills_*.csv.gz; los dias <=18 usan parquet persistente). Luego `attach_ms.py S`, `an_pie.py datos/pie_celdas.csv`, `an_v2.py 300`.
3. Escribir «camino a 200 k€» (cuenta + hueco con LIBRO_OBJETIVO_200K.md: optimista no validado ~34 k, techo teorico ~119 k), candidatas por €/ano, reglas_congeladas.json v2 + `sha256sum reglas_congeladas.json > HASH.txt`.
4. Con 300-500 pujas de B: `python3 scripts/b_postmortem.py`.
5. Tras reiniciar: `crontab -l | grep sa_r1`; primer dato forward real = units_2026-10-22 (cron 10:40Z del 23-Oct); estado con `python3 scripts/r1_fwd_vigia.py`; log `datalogs/sa_r1/cron.log`.
Conclusion hasta ahora: la seleccion adversa del maker simulado que persigue el precio es 0,237/EUR (sim de cinta; nivel no transferible); R1 recupera ~12 %; el ~88 % restante sigue como hipotesis abierta (orden de Javi); la capacidad del bote limita los 200 k tanto como la seleccion adversa.
