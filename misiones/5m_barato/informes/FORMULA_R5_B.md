# FORMULA_R5_B — sim3-BTC, estados complementarios, monedas y capacidad (Ronda 5, 28-Oct-2026)

**Estado**: investigación; NO validada; no se autocertifica (falta validador/red-team independiente). Sin órdenes, sin producción, sin commits, sin agentes lanzados. Presupuesto: 20/20 llamadas (la 20 es la entrega).
**Expediente**: `/root/polymarket-research/experimentos/5m_barato/formula_r5_28oct/`: prerregistro `PREREG_FORMULA_R5.md` (13:09Z, ANTES de contrastar IS/OOS), `HASHES_R5.txt`, código `r5.py` (sim3 + familia), `r5f.py` (suite de rellenos), `r5_posthoc.py` (tablas post-hoc), salidas `salida_fam_{final,pooled,reverse}.txt`, `salida_suite_final.txt` (22 días), `salida_suite_interim09_27.txt`, `salida_posthoc.txt`.
**Convenciones**: EV/E = Σ take·(y−b) / Σ take·b, ponderado por € y BRUTO de comisión y de rebate; dEV/E = EV/E dentro de S menos fuera de S (diario; media por días); IC90 = t de Student por DÍAS (bootstrap por MERCADO solo donde se dice, 1.000 remuestras); reloj de RECEPCIÓN; precios 0,09–0,31; desenlace oficial por token (0 tokens sin desenlace en los 23 días simulados). Suite: días 06–27 (22); el 05-Oct se excluye por la regla mecánica de R4 (59.683 rellenos = 36 % de la mediana 164.447). Total 3,79 M de rellenos en 22 días.

## 0. Veredicto
1. **sim3-BTC prerregistrada: REJECTED.** Elegida con IS 05–15 únicamente (v057: barrido ≥400 acc, ventana +1…+120 s, T_rem 60–290 s, TD=1, puja en bb, banda ≥0,20): IS +0,010; **OOS 16–25 −0,065** (N=20; IC90 por días [−0,132; −0,008]; 2/10 días+; 543 ejec./día = 1,50 % del flujo S800-BTC; −25,4 k€/año); walk-forward −0,102 [−0,209; −0,010]; DEV 26–27 −0,067. p ajustado max-estadístico (270 candidatas) = 0,946. Fallan C1, C2, C4, C5.
2. **Por qué (medido, §2.4)**: cotizar siempre, sin S, cuesta −0,049 / −0,100 / −0,081 (IS/OOS/DEV; 24 variantes; 0 % con EV>0). S aporta +5,4 / +1,5 / +15,1 pp (S−SIEMPRE emparejado en 05–15 / 16–25 / 26–27): insuficiente en 2 de 3 tramos. Cola, cancelación, salto adverso y tamaño son de segundo orden; el signo de T_rem cambia entre tramos.
3. **La señal S sigue en los rellenos de TODOS los makers**: 06–25 (sin los 2 días de descubrimiento) +0,110 [+0,028; +0,192], 12/20 días+ (60 %); 22 días +0,149 [+0,062; +0,236], 14/22 (64 %). **Gate del 80 % de días positivos NO cumplido (no relajado).** Solo BTC (ETH +0,081 [−0,192; +0,354]; SOL −0,300 [−0,575; −0,025]).
4. Cobertura: 16 estados complementarios prerregistrados; ninguno pasa Holm al 5 % (mínimo 0,100); el efecto está en las colas del flujo propio y al subir la cobertura se diluye a 0 (flujo≥200 acc: cobertura 76,8 %, dEV −0,012).
5. No hay fórmula con EV OOS positivo. Candidata post-hoc v258 congelada para forward ≥28-Oct (§2.6): agregado 05–25 +0,034 (IC90 por días [−0,066; +0,099], 10/21 días+); detectar +0,05 con IC90>0 exige ≈52 días.
6. Portafolio: validado 0 €/año; contribución incremental validada 0. Capacidad: ver §7 (la cuota lograda es 0,4–1,5 % del flujo S frente al 9–17 % que haría falta).

## 1. Pase de lo evidente (antes de nada)
- **Qué mide cada número**: la suite mide EV/E de los rellenos on-chain de otros makers dentro/fuera de S; sim3 mide EV/E de NUESTRA puja simulada. Son objetos distintos: el maker medio (22 d) gana ≈ +0,047 (EV(S) +0,168 con 13,2 % del € + EV fuera de S +0,029), una puja estática simulada pierde −0,05…−0,10. Esa brecha de 10–15 pp es el verdadero hallazgo de §2.4(d).
- **Supuestos del simulador** (sim.py/sim2.py/r5.py): L1 con lectura a 130 ms; cola = tamaño visible del nivel al colocar (sin órdenes ocultas; las cancelaciones por delante no adelantan: cota conservadora de la fila, optimista en que el relleno es total al ser atravesado); sin parciales; sin impacto propio (N no altera la cola: optimista en tamaño); precio FIJO (sin repeg); cancelación TD (salto Binance BTC ≥2 bps en 300 ms: fuera de [j+100, j+1000) ms); comisión 0 y rebate 0 (el rebate del 20 % del fee del tomador, 0,014·(1−p) por € a p 0,10–0,30, sumaría ≈ +1,0…+1,3 pp: no cambia ningún veredicto de este informe).
- **Línea base trivial** "cotizar siempre" (misma banda/T_rem/TD/δ, sin S): −0,049 IS, −0,100 OOS, −0,081 DEV (media de 24 variantes; 0 % con EV>0 en los tres tramos; `salida_posthoc.txt` §2). Coherente con B real −0,072 (n=202 on-chain). Toda mejora de S se mide contra esa línea y contra 0.
- **Comprobaciones**: (i) la corrida `final` re-guardada reproduce la prerregistrada (v057, t=+0,39, p=0,9460; semilla 2813); (ii) la suite reproduce R4 en 09–25 (+0,109 [+0,035; +0,183], 11/17, cobertura 12,0/13,1 %); (iii) desenlace oficial para el 100 % de los tokens; (iv) el EV solo cuenta rellenos (sin rellenar no es relleno); (v) día 05 parcial excluido; (vi) una pasada intermedia de la suite (09–27, 13:16Z) se corrió tras congelar el prerregistro y antes del contraste de sim3; no tocó ninguna regla.

## 2. A) sim3-BTC: puja pasiva propia condicionada a S
### 2.1 Diseño (prerregistrado, hash antes de contrastar)
Hashes sha256 (primeros 16): PREREG `4362926ace9d418a`, r5.py `98023a68541971ca`, r5f.py `f28445c2ceb5dc52`, r4.py `e9fba2c8ec03289d`, identity3.py `a4d84add1c9476ef`, sim.py `e9909023be0aba02` (completos en `HASHES_R5.txt`, 13:09Z; hashes de las salidas al final del mismo fichero).
Familia: 432 variantes con S (θ {400, 800, 1600} acc × W1 {1, 5} s × W2 {30, 60, 120} s × T_rem {[60,290], [120,240]} × TD {0, 1} × δ {+0,01; 0; −0,01} × banda inferior {0,10; 0,20}) + 24 «SIEMPRE» = 456 variantes × N {5, 10, 20, 50}. Partición fijada antes de ver nada de sim3: IS 05–15 (11 d), OOS 16–25 (10 d), DEV 26–27, forward ≥28. Compuerta IS (opera ≥80 % de los días y ≥100 ejec./día a N=20: pasan 270 de 456; θ=1600 no pasa por falta de órdenes); criterio = mayor cota inferior IC90 (por días) del EV/E diario; p ajustado = volteo de signos por días, K=5000, max-estadístico sobre las candidatas. Éxito en OOS (N=20): C1 EV/E ≥ +0,05; C2 cota inferior IC90 por días > 0; C3 ≥250 ejec./día; C4 cuota ≥2 % del flujo S800-BTC de todos los makers; C5 ≥8/10 días+.
### 2.2 Resultado de la elegida (v057), N=20
| Tramo | EV/E agregado | día medio [IC90 por días] | días+ | ejec./día | cuota S800-BTC | pnl €/año |
|---|---|---|---|---|---|---|
| IS 05–15 (11 d) | +0,010 | +0,009 [−0,034; +0,052] | 6/11 | 508 | 1,39 % | +3.704 |
| **OOS 16–25 (10 d)** | **−0,065** | **−0,070 [−0,132; −0,008]** | **2/10** | 543 | 1,50 % | **−25.363** |
| DEV 26–27 (2 d) | −0,067 | −0,075 [−0,853; +0,703] | 1/2 | 624 | 1,72 % | −30.056 |
| Walk-forward OOS (eligió v057 ×6, v211 ×4) | −0,102 | −0,110 [−0,209; −0,010] | 2/10 | — | — | — |

Tamaños OOS: N=5 −0,067 (−6,6 k€/año), N=10 −0,065 (−12,9 k), N=50 −0,071 (−68,2 k). Bootstrap por mercado OOS (1.731 mercados, N=20): [−0,112; −0,016]. Spearman IS-vs-OOS entre las 270 candidatas +0,353, pero el nivel cae en bloque: EV>0 en IS para el 39,3 % de las candidatas, en OOS para el 2,2 % (6 candidatas); media IS −0,003, media OOS −0,085.
Criterios: C1 ✗ (−0,065), C2 ✗ (superior −0,008 < 0), C3 ✓ (543), C4 ✗ a N=20 (1,50 %; ✓ a N=50 con EV −0,071), C5 ✗ (2/10). **FALLA.**
### 2.3 Qué NO se hizo
Sin comisión/rebate; sin impacto propio ni cola propia; sin otras monedas en sim3; sin identidad de maker (§10).
### 2.4 Diagnóstico medible del fallo (N=20; EV agregado medio por tramo; fuente `salida_posthoc.txt` §2 y `salida_fam_*.txt`)
| Dimensión | IS 05–15 | OOS 16–25 | DEV 26–27 | Lectura |
|---|---|---|---|---|
| SIEMPRE (24 var.) | −0,049 | −0,100 | −0,081 | la puja estática pierde 5–10 pp |
| S (246 var. de la compuerta) | +0,001 | −0,084 | +0,061 | nivel común cae 8 pp de IS a OOS |
| S − SIEMPRE emparejado (media; n var.) | +0,054 (264) | +0,015 (246; mediana +0,004) | +0,151 (252) | S ayuda siempre, 1,5–15 pp según tramo |
| θ=800 / θ=400 | +0,014 / −0,008 | −0,047 / −0,110 | +0,154 / −0,006 | barridos mayores, mejor, en los 3 tramos |
| T_rem 120–240 / 60–290 | +0,018 / −0,013 | −0,094 / −0,075 | +0,165 / −0,021 | signo inestable |
| θ800 × T120–240 (36 var.) | +0,049 (94 % >0) | −0,033 (17 % >0) | +0,342 (100 % >0) | mejor subfamilia relativa, negativa en OOS |
| Puja bb+0,01 / bb / bb−0,01 | +0,015 / +0,001 / −0,014 | −0,068 / −0,084 / −0,100 | +0,080 / +0,058 / +0,041 | cola: 1,5–3 pp por escalón, mismo orden en los 3 tramos |
| TD=1 − TD=0 | +0,006 | +0,005 | +0,015 | cancelación: +0,5…+1,5 pp |
| banda ≥0,20 − ≥0,10 | +0,012 | +0,010 | +0,008 | marginal |

(a) **Cola / selección adversa propia**: cuanto más al fondo de la cola, peor (orden monótono y estable); la puja pierde incluso con S porque los rellenos marginales de una puja estática son los de la cola atravesada. (b) **Cancelación**: TD aporta +0,5…+1,5 pp; el salto adverso de Binance ≤5 s tras el relleno afecta a 125 de 5.049 rellenos de v057 en OOS (2,5 %, EV −0,409): sin ellos −0,056 frente a −0,065, es decir ≈0,9 pp de los 6,5 pp. (c) **Tamaño**: EV/E invariante en N (5/10/20: −0,067/−0,065/−0,065; 50: −0,071): en el simulador N solo escala; en la realidad empeoraría. (d) **Brecha de gestión**: maker medio on-chain ≈ +0,047 frente a puja estática −0,05…−0,10; S (+1,5…+15 pp) no la cierra en 05–25 salvo 26–27. Hipótesis (no probada): el maker medio re-pega y cancela con información que una puja fija no tiene. (e) **T_rem** de v057: OOS [60,120) +0,114 (n=1.622), [120,180) −0,040, [180,240) −0,163, [240,301) −0,137; IS [60,120) −0,026, [120,180) +0,090, [180,240) −0,002, [240,301) −0,002: sin patrón estable. (f) **Cuota**: 0,4–1,5 % del flujo S a N=20.
### 2.5 Mecanismos distintos dentro de la familia hasheada y particiones alternativas
Las variantes de otro mecanismo (δ, TD, banda, T_rem, θ) están en la familia y se leyeron arriba. Las particiones alternativas son sensibilidad SECUNDARIA (la decisiva fue la prerregistrada):
| Partición | Selección en IS | p ajustado | OOS N=20 | Nota |
|---|---|---|---|---|
| IS 05–15 → OOS 16–25 (decisiva) | v057 | 0,946 | −0,065 [−0,132; −0,008], 2/10 | REJECTED |
| IS 05–25 (21 d) → 26–27 | v258 (θ800, W5–60, T120–240, TD1, bb+0,01, banda ≥0,10) | 0,930 | +0,339 (+0,53 y +0,20; 2/2; mercados [+0,055; +0,623], n=132) | 2 días, y son los de descubrimiento de S |
| IS 16–25 → OOS 05–15 (inversa) | v271 (θ800, W5–120, T60–290, TD1, bb+0,01, banda ≥0,20) | 1,000 | +0,006 [−0,126; +0,111], 7/11; WF −0,039 | ≈0 |
Ninguna selección tiene evidencia en su IS (p ajustado 0,93–1,00).
### 2.6 Fórmula entregada
**(i) Calibrada solo en IS 05–15 (prerregistrada): v057.** S = barrido (impresiones de zona SELL del token barato a p∈[0,085; 0,315] o BUY a p∈[0,685; 0,915], mismo token y lado, huecos ≤300 ms de hora de exchange) con tamaño ≥400 acc; ventana de cotización de fin_barrido+1 s a +120 s y T_rem∈[60,290] s; puja en bb (cola visible) si spread ≥0,02 y bb∈[0,20; 0,29]; precio fijo; tamaño 5→20 acc; cancelación TD (salto BTC ≥2 bps/300 ms: fuera [100, 1000) ms). EV OOS −0,065; WF −0,102. **NO implementar.**
**(ii) Candidata post-hoc v2 = v258 (NUEVA VERSIÓN: elegida con 05–25; no tiene OOS limpio).** S igual con θ=800 acc; ventana fin_barrido+5 s…+60 s; T_rem∈[120,240] s; puja en bb+0,01 (cola 0) si spread ≥0,02 y bb∈[0,10; 0,29]; TD=1; tamaño 5→10→20 acc (50 acc ya baja a +0,018). Agregado 05–25 (21 d): N=20 +0,034, día medio +0,017 [−0,066; +0,099], 10/21 días+, 157 ejec./día, 0,41 % de cuota, +2,8 k€/año; N=5 +0,037 (+0,8 k€/año); N=10 +0,037 (+1,5 k€/año); N=50 +0,018 (+3,7 k€/año). Tramo no usado en esa selección (26–27): N=20 +0,339 (+0,53, +0,20), 193 ejec./día, +32,9 k€/año; pero esos 2 días son los de descubrimiento de S y las dos mejores jornadas de S en rellenos. Estado: congelada para forward desde el 28-Oct; no validada.

## 3. B) Cobertura: 16 estados complementarios prerregistrados (dEV/E de cada estado vs el resto; suite s3)
| Estado | cob. n / € | dEV/E [IC90 días] | días+ | p Holm(16) |
|---|---|---|---|---|
| flujo propio = 0 | 8,7 / 9,6 % | +0,075 [+0,028; +0,123] | 15/22 | 0,100 |
| flujo propio (0, 200) | 14,5 / 12,6 | −0,039 [−0,082; +0,004] | 8/22 | 1 |
| [200, 800) | 16,1 / 17,1 | −0,045 [−0,082; −0,008] | 9/22 | 1 |
| [800, 3.200) | 47,6 / 46,7 | −0,039 [−0,084; +0,006] | 8/22 | 1 |
| [3.200, 12.800) | 12,9 / 13,7 | +0,108 [+0,039; +0,178] | 14/22 | 0,102 |
| ≥12.800 | 0,2 / 0,2 | +0,156 [−0,629; +0,941] | 5/13 | 1 |
| nº barridos ≥200: 0 / 1 / 2–3 | 39,3 / 19,2 / 24,5 | −0,039 / −0,020 / +0,014 | 11 / 9 / 11 de 22 | 1 / 1 / 1 |
| nº barridos ≥200: ≥4 | 17,0 / 17,6 | +0,080 [+0,022; +0,138] | 14/22 | 0,191 |
| BTC-líder (monedas no BTC) V=0 | 15,7 / 17,7 | +0,107 [+0,013; +0,202] | 14/22 | 0,420 |
| BTC-líder (0,200) / [200,800) / [800,3.200) / [3.200,12.800) / ≥12.800 | 6,6 / 15,6 / 50,1 / 11,9 / 0,1 | +0,004 / −0,070 / −0,042 / +0,052 / −0,360 | 11 / 6 / 10 / 15 / 3 de 22 | 1 |
Cobertura acumulada (umbral anidado de flujo propio en (5,60] s): ≥200 acc 76,8 % → dEV −0,012 [−0,046; +0,021], 8/22; ≥800 acc 60,7 % → +0,019 [−0,014; +0,052], 11/22; ≥3.200 acc 13,1 % → **+0,128 [+0,059; +0,197], 16/22 (73 %)**, p sin ajustar 0,002; ≥12.800 0,2 %.
**Lectura**: forma de U: el efecto vive en los extremos del flujo propio (mercado quieto o muy cargado), el 63 % central de los rellenos es ≈ −0,04. Subir la cobertura hacia 100 % diluye el efecto a 0. Cota superior de la suma de coberturas de los 4 estados con IC90>0 (S800 12,1 + quieto 8,7 + ≥3.200 12,9 + ≥4 barridos 17,0) = 50,7 %, con solapes sin calcular; ninguno supera Holm.

## 4. C) ETH y otras monedas (m5_onchain 05–08 integrado: 100 % de desenlaces, casadas 48–53 %, comprobado sin duplicados)
Umbral relativo por moneda = percentil de 800 acc en los clusters de BTC de los días IS (99,48 %), fijado sin desenlaces.
| Moneda (θ) | n_S | todos los días dEV/E [IC90 días] | días+ | bootstrap por mercado | OOS 16–25 | n que falta |
|---|---|---|---|---|---|---|
| BTC (800) | 451.856 | +0,140 [+0,052; +0,229] | 14/22 | [+0,041; +0,246] (6.331 mercados) | +0,099 [−0,001; +0,198], 7/10 | 8 días para t>1,645 (ya hay 22) |
| ETH (207) | 23.319 | +0,081 [−0,192; +0,354] | 10/22 | [−0,236; +0,437] | −0,178 [−0,478; +0,122], 4/10 | ≈229 días con esa media/sd (≈mediados de jun-2027) y el OOS apunta al signo contrario |
| SOL (119) | 3.092 | −0,300 [−0,575; −0,025] | 8/22 | [−0,579; −0,023] | −0,576 | negativo significativo |
| XRP (87) | 832 | −0,203 [−0,509; +0,102] | 6/22 | [−0,403; +0,304] | −0,069 | media ≤0 |
| DOGE (101) | 343 | +0,047 [−0,853; +0,947] | 4/18 | [−0,919; +1,807] | +0,555 (n=128) | ≈5.900 días |
| BNB (64) | 138 | +0,468 [−0,884; +1,820] | 4/15 | [−0,748; +0,746] | n=44 | ≈109 días (n_S minúsculo) |
HYPE/AVAX/LINK/otras: sin clusters suficientes en IS (n<300). **Conclusión**: la señal S, tal como está definida, es de BTC; ETH no es accionable (positivo débil en 22 días, negativo en 16–25); ampliar monedas no es una ruta a corto plazo.

## 5. D) Por qué S_reg replica y S_chain no
- **No es el reloj, es el umbral y la agregación**. S_chain con umbral 800 acc (por tx y tomador, hora de bloque) también replica: **+0,252 [+0,086; +0,417], 16/22 días+, cobertura 5,7/6,4 %**. Lo que no replicaba era S_chain≥200: +0,018 [−0,022; +0,058] (13/22; cobertura 37,2 %): al bajar el umbral entran barridos rutinarios sin información.
- Celdas 2×2 (S_reg800 × S_chain≥200): ambos 10,7 % de los rellenos, EV/E +0,178; solo reg 1,4 %, +0,091; solo chain 26,5 %, +0,005; ninguno 61,4 %, +0,039.
- S_reg800 con solo ventas del token barato: −0,009 [−0,146; +0,128] (cobertura 2,5 %): la información está en las compras del favorito (espejo), no en las ventas directas del barato.
- **Dosis-respuesta** (rellenos en (5,60] s tras 4.098 barridos BTC ≥800): por tamaño del barrido 800–1.600: +0,156 (n=3.247); 1.600–3.200: +0,291 (658); ≥3.200: +0,397 (193). Por nº de impresiones: 1–2 +0,155; 3–10 +0,325; 11–50 +0,172; ≥51 +0,145 (sin tendencia). Por duración: <1 s +0,234; 1–5 s +0,127; ≥5 s +0,375 (n=114).
- **Lectura**: característica explotable en tiempo real (el registro del WS ve el barrido; no hace falta on-chain) y no un artefacto del reloj de recepción. Mecanismo plausible (hipótesis, no aislado causalmente): tras un barrido grande a favor del favorito, el libro se limpia y se re-cotiza, y durante 5–60 s los rellenos de las pujas baratas son menos tóxicos.

## 6. E) Días positivos y gate del 80 %
| Conjunto | días | dEV/E medio [IC90] | días+ | % |
|---|---|---|---|---|
| R4 09–25 | 17 | +0,109 [+0,035; +0,183] | 11 | 65 % |
| 06–25 (sin los 2 de descubrimiento) | 20 | +0,110 [+0,028; +0,192] | 12 | 60 % |
| 06–08 (nuevos, m5_onchain) | 3 | +0,117 [−0,606; +0,840] | 1 | 33 % |
| 06–27 (todos) | 22 | +0,149 [+0,062; +0,236] | 14 | 64 % |
**El gate del 80 % queda NO cumplido** (60–65 %), sin relajar. Añadir 06–08 no mejora la fracción. El IC90 de la media por días sí queda >0 en R4, 06–25 y 06–27. El día 05 se excluye por la regla de inclusión.

## 7. F) Capacidad
Flujo S800-BTC de todos los makers (OOS 16–25): 266.344 acc/día = 48.847 €/día = 17,8 M€/año de coste. Cuota necesaria para 200 k€/año según el EV/E que se logre:
| EV/E logrado | cuota necesaria |
|---|---|
| +0,126 (EV(S) de los rellenos de todos los makers, 06–25) | 8,9 % |
| +0,093 (dEV agregado 06–25) | 12,1 % |
| +0,065 | 17,3 % |
| +0,034 (v258 agregado 05–25) | 33 % |
| ≤0 (v057 OOS) | imposible |
Rampa de tamaño (€ ≈ pUSD, sin FX):
| N | v057 OOS 16–25 (prerregistrada) | v258 agregado 05–25 (post-hoc) | v258 en 26–27 (post-hoc) |
|---|---|---|---|
| 5 | −6,6 k€/año (0,38 %) | +0,8 k€/año (0,10 %) | +9,0 k€/año (0,10 %) |
| 10 | −12,9 k (0,76 %) | +1,5 k (0,21 %) | +17,8 k (0,20 %) |
| 20 | −25,4 k (1,50 %) | +2,8 k (0,41 %) | +32,9 k (0,39 %) |
| 50 | −68,2 k (3,65 %) | +3,7 k (1,00 %) | +73,5 k (0,97 %) |
La cuota lograda (0,1–1,5 %) está 6–90 veces por debajo de la necesaria, aun con la cola ya modelada. La puja solapa con B (mismos tokens baratos BTC 5m, misma cola y capital): no se suma. Camino realista a 200 k€: ninguno demostrado con esta familia.

## 8. Limitaciones convertidas en ventajas (adición de Javi)
**(a) Maldición del ganador**: selección anidada (walk-forward) de S entre 12 especificaciones (modo ALL/SELL × θ 100…3.200), ≥8 días de entrenamiento; se informa el EV del PROCEDIMIENTO. Naive (media): +0,163 [+0,054; +0,273], 10/14 días+ (elige A800 14 de 14); prudente (cota inferior IC90): +0,114 [+0,007; +0,221], 11/14 (A800 ×7, A400 ×4, A200 ×3; cobertura media elegida 29 %); S800 fijo = naive. Sin los 2 días de descubrimiento (14–25 Oct, 12 días): +0,101 [+0,006; +0,196], 8/12. El procedimiento converge a S800 y no rebaja el efecto de forma material (≈ +0,10), pero el límite inferior queda en +0,006.
**(b) Bootstrap por mercado cruzando 0**: restricción prerregistrada BTC y T_rem∈[120,240) s (motivada por el diagnóstico de R4 en 09–25): 09–25 días +0,195 [+0,055; +0,335], 12/17; **por mercado +0,168 [+0,026; +0,318] (4.748 mercados) → IC por mercado >0**. «Frescos» (06–08 y 26–27, 5 días; 26–27 son de descubrimiento de S): +0,357 [−0,243; +0,956], 3/5; por mercado +0,413 [+0,050; +0,800] (1.403). Todos: +0,232 [+0,084; +0,380], 15/22 (68 %); por mercado [+0,091; +0,376] (6.151). Por tramo de T_rem (BTC): <60 s −0,107 (9/22); 60–120 +0,055; 120–180 +0,155; **180–240 +0,285 [+0,111; +0,460], 15/22**; 240–301 +0,074. La restricción concentra el efecto, pero el único conjunto limpio son 3 días.
**(c) Pesos iguales cerca de 0**: el efecto crece con el tamaño del relleno (BTC): <5 acc +0,088 [+0,005; +0,172] 14/22; 5–20 +0,089 [+0,003; +0,176] 14/22; 20–100 +0,140 [+0,052; +0,227] 15/22; 100–500 +0,212 [+0,042; +0,382] 16/22; ≥500 +0,715 [+0,142; +1,288] 13/22 (n=154). Por precio plano (+0,11…+0,16 en los 4 tramos). El peso lo llevan los rellenos grandes; los pequeños (donde caerían nuestras 5–20 acc) valen ≈ +0,09 con IC justo >0. Ajustar el tamaño al alza no está soportado: los rellenos grandes son de makers con cola delantera y sin impacto propio.

## 9. Red team (qué podría invalidar lo anterior)
1. **Contaminación de descubrimiento**: θ=800/300 ms/(5,60] s se fijó en R3/R4 mirando 26–27; T_rem [120,240) sale del diagnóstico de R4 en 09–25. Limpio para S: solo 06–08 (3 d, 1/3+, IC [−0,606; +0,840]). Para v258: solo el forward.
2. **Dos mejores días**: sin 26–27 el efecto baja de +0,149 a +0,110 (R4 sin los 2 mejores días: +0,073).
3. **Rellenos de otros ≠ rellenos nuestros** (§1, §2.4d).
4. **Nivel de régimen**: el nivel de todas las variantes cae 8 pp entre 05–15 y 16–25; solo las diferencias emparejadas (S−SIEMPRE) son comparables entre tramos.
5. **Multiplicidad**: 456 variantes (max-T), 12 S, 16 estados (Holm), 6 monedas; el p sin ajustar del flujo ≥3.200 (0,002) no sobrevive a la familia.
6. **Criterio de selección**: la cota inferior favorece mucho volumen y poca media (eligió v057); una selección por media habría elegido v211 (IS +0,089, agregado 05–25 +0,026) y tampoco pasa.
7. **n efectivo**: la unidad son 22 días (sd diaria de v258 ≈ 0,22, derivada del IC90 con 21 días); 6.331 mercados por moneda; racimos de cierre no corregidos fuera de BTC.
8. **Simulador optimista en relleno total, sin impacto, sin parciales, precio fijo**; pesimista en cola, comisión y rebate a 0. Cuotas de 0,4–1,5 % son cotas.
9. **Un solo mes y un régimen** (octubre 2026); sin forward.
10. **Fuentes**: m5_onchain 05–08 con casadas 48–53 % (R4 17 d: 38–57 %); día 05 parcial.

## 10. Siguiente experimento decisivo (uno)
**Forward congelado de v258 desde el 28-Oct** con el mismo código (`r5.py ext D && r5.py sim D`, ≈80 s/día CPU a nice 19; el registro de cada día debe existir completo) y lectura con la rutina de `fam` (bloque forward). PASS (propuesta a micro-real solo con OK de Javi + validador + red-team): ≥10 días con EV/E ≥ +0,05 agregado, IC90 por días > 0 y ≥250 ejec./día (¡no se cumple con 157/día: C3 queda como informativo; el gate económico es C1+C2!). Con sd diaria 0,22, el IC90>0 a 10 días exige media ≥ +0,13; si el efecto real es +0,05, hacen falta ≈52 días (≈18-Dic-2026); si es +0,034, ≈113. KILL: tras 20 días media <+0,02 o IC90 superior <+0,05. Coste: CPU mínima, sin dinero. Cambia la decisión: abre o cierra la última rendija de sim3-BTC con datos que ni el IS ni el OOS ni el DEV tocaron.
Segundo en cola (no ejecutado): descomposición por DIRECCIÓN de maker de los rellenos en S (hay que conservar la dirección en `r4.build`): ¿el +0,10 de S lo cobran pocas direcciones que re-pegan/cancelan rápido? Cierra o abre la brecha de gestión de §2.4(d).
**Reabrir sim3-BTC** solo si: (a) v258 pasa forward, o (b) aparece un mecanismo de gestión que cierre la brecha de 10–15 pp. No se recomienda ampliar monedas ni estados.
Agentes necesarios (no lanzados): `cheap5m-statistical-validator` (reimplementar de cero el modelo de relleno y reproducir §2.2/§2.4); `cheap5m-red-team-auditor` (forward de v258 y contaminación de S); `cheap5m-execution-engineer` (job diario del forward; el cron lo instala la sesión principal con OK).

## 11. Reproducibilidad
- Orden: `bash run_ext.sh` (extrae 26→05 y construye 05–08 de m5_onchain en `/root/polymarket-research/experimentos/5m_barato/formula_r4_28oct/out/`, que gana d_2026-10-05..08.npz; el log original de R4 se conservó en `salida_build_R4_original.txt`); `python3 r5.py sim D` por día; `python3 r5.py fam --is D,.. --oos D,.. --dev D,.. --tag T`; `python3 r5f.py suite --tag T`; `python3 r5_posthoc.py`.
- Recursos usados: nice 19/ionice idle, `ulimit -v 4,5 GB`, fuera de 06:00–09:30Z, un trabajo pesado a la vez; sin tocar `data/live`, `.env`, vigías ni módulos compartidos; `ext/` y `simout/` en `.gitignore`.
- Semillas: max-T 2813, bootstrap 2814/7. Hashes: `HASHES_R5.txt`.

## 12. Incertidumbres sin resolver
- Si el +0,10 de S en rellenos de otros se puede cobrar con una puja propia (sim: no, salvo 26–27).
- Si 26–27 son un régimen (más barridos) o ruido; faltan días nuevos.
- Efecto real de comisión/rebate, impacto propio y cola real en la puja (el simulador no los modela).
- Unión real de la cobertura de los estados positivos (solapes no calculados).
- Mecanismo causal de S (hipótesis de limpieza del libro) sin aislar.
- Identidad de los makers que cobran el efecto.
- Espacio del expediente: 763M	ext 896K	simout 296K	. 
