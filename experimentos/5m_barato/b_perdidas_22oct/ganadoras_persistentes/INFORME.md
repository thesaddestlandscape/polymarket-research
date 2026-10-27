# GANADORAS PERSISTENTES 5m banda 0,05-0,30 — roster walk-forward, roles on-chain y relaciones para B (25-Oct-2026, 12:00-12:55Z)
Estado: **EXPLORATORY (16 días, 06..21-Oct). Contribución validada para B: 0 €/año.** Solo lectura: m5_onchain (VOL) con maker/tomador explícitos, desenlace oficial `DL/mapa_escala/des.json` (cobertura **1,0000** de 5.100.265 fills de banda; 22-24 Oct excluidos: des 57/1.728). Sin tocar B, live, F2, crons. nice 19 / ionice 3 / ulimit 3 GB, fuera de 06-09Z.
Prereg `PREREG.md` sha 3d62fcdc… (antes de calcular nada) · `ADENDA1.md` 9d7cb6ae… (tras ver solo que el roster BH salía vacío) · `ADENDA2.md` (parte 1 sha f99696a3… tras a2; parte 2b añadida tras a3 y antes de a4; sha final 38059e0f…). Todo lo de las adendas es post-hoc.
Unidad = posición (wallet, mercado, lado comprado; ventas → compra del complementario); pnl a SU precio con fee real; EV€ = Σpnl/Σcoste; IC90 bootstrap por DÍA; rebate aparte.

## 1. Tabla roster × periodo (S1)
| Selección (ventana → medida) | elegibles/día | roster | EV€ medida | IC90 días | sin 2 mejores | días+ | n unid | placebo (p) | top-1 wallet |
|---|---|---|---|---|---|---|---|---|---|
| **BH-FDR q<0,10 (prereg)**, WF 7 d → d=13..21 | 1.894-1.958 | **0** todos los días | — | — | — | — | — | — | — |
| idem split 06-13 → 14-21 | 2.110 | **0** | — | — | — | — | — | — | — |
| z≥2 sin corregir (ADENDA1), WF | ídem | 9-39/día (89 únicas) | **+0,025** | (−0,063, +0,104) | −0,030 | 7/9 | 28.939 | media −0,018, p=0,23 | 10,8 % (0x41e2e1cc) |
| z≥2, split | 2.110 | 42 | +0,025 | (−0,059, +0,103) | −0,021 | 5/8 | 46.961 | p=0,33 | 28,6 % (0x41e2e1cc) |
| top 1 % por z, WF | ≈19 | — | +0,066 | (−0,027, +0,153) | +0,000 | 6/9 | 21.959 | — | — |
| **INVERSIÓN: perdedoras z≤−2**, WF | 108-222/día | — | **−0,196** | **(−0,259, −0,123)** | −0,224 | **0/9** | 24.927 | — | — |
| perdedoras, split | 131 | — | −0,176 | (−0,254, −0,109) | −0,239 | 1/8 | 13.196 | — | — |
**Test poblacional sin selección** (`a2_salida.txt`): elegibles con z≥2 = 9-42 por ventana frente a 43-48 esperadas por azar (2,28 %·N) → **no hay más ganadoras que las del azar**; con z≤−2 hay 108-222 (2,5-5× el azar). Conclusión S1: **a precio 0,05-0,30 las GANADORAS persistentes no son identificables por encima del azar con 7-8 días; las PERDEDORAS sí, y persisten fuera de muestra (0/9 días positivos)**. Perfil (ventana 14-20, `a3`): perdedoras n=222, **75 % del coste como TOMADOR**, precio medio 0,205, s medio desde apertura 126; roster z≥2 n=8: 86 % maker, entra más tarde (23 % del coste a ≥240 s). B (0x659a…297f) no es elegible (121 $ de banda en 20-21 Oct).

## 2. Roles on-chain del roster z≥2 (S2; regla prereg sobre toda su actividad 5m en la ventana; medida en d; descriptivo)
| Rol (wallets únicas WF; ejemplo más frecuente) | WF EV€ (IC90 d) | split EV€ (IC90 d) | ¿consistente? |
|---|---|---|---|
| acumulador de pares (29; 0x02824266) | +0,003 (−0,105, +0,152) | +0,049 (−0,044, +0,135) | no, ≈0 |
| maker ambos lados direccional (19; 0x2a54d7c9) | +0,052 (−0,005, +0,104) | +0,036 (−0,050, +0,123) | signo sí, IC cruza 0 |
| maker pasivo (10; 0xc3924b9a, 0xb0f85baa = pspspsps5) | +0,064 (−0,082, +0,329) | **+0,194 (+0,017, +0,367)** | solo split |
| holder de longshots (5; 0x91fd00a8) | **+0,374 (+0,186, +0,446)**, n=328 unid, 4/7 d | +0,107 (−0,188, +0,425) | solo WF, n mínimo |
| gestor de salidas (8; 0xf074dc84) | **+0,075 (+0,026, +0,131)** | +0,005 (−0,074, +0,088) | solo WF |
| tomador-sniper (22; 0xc0145123) | −0,003 (−0,134, +0,069) | +0,005 (−0,084, +0,085) | ≈0 |
Ningún rol pasa en los dos esquemas; todos con n de wallets 5-29 (<40 unidades-gate solo en holder). 0x41e2e1cc (top-1) ya era una de las «36 sistemáticas de pares» del 30-Sep.

## 3. Mecanismo y réplica con NUESTRA latencia (S3) — relaciones candidatas
| Relación (patrón → regla para B) | Test | Resultado (días 13-21, WF) | Veredicto |
|---|---|---|---|
| R1 copiar roster-tomador al primer print tomador ≥2 s después (mismo mercado-lado) | EV€ de la copia | roster −0,082; **copia −0,087** IC90 (−0,220, +0,045), 2.398 de 3.213 unidades con print | REJECTED (= cementerio; y el informe diario de tomadoras al ask real con 272 ms da −0,04, BTC 0,10-0,25 IC90<0, 23 d) |
| R2 pujar (maker) solo en las celdas moneda×minuto×5c donde se concentran los roster-makers | Δ población en celdas vs toda la banda maker | Δ **+0,035** IC90 (+0,004, +0,063), sin2 +0,009, 5/9 d; **IC98,75 (−0,012, +0,077)** | NO es relación de wallet: las celdas son BTC 0,15-0,30 en todos los minutos y las celdas por POPULARIDAD (Δ +0,021) o de las PERDEDORAS (Δ +0,030) dan lo mismo → efecto «BTC > alts» del periodo. No pasa α=0,0125 |
| R3 idem tomador | Δ | +0,018 (−0,021, +0,054) | REJECTED |
| Skill no replicable (roster vs población en sus mismas celdas) | EV€ | maker +0,037 vs +0,024 esperado (+0,013/€, 6/9 d); tomador −0,033 vs −0,095 | cola/cancelación/selección que no vemos on-chain |
| R4 roster-maker ya compró mi lado ≤tf−5 s → mantener | Δ | −0,016 (−0,099, +0,071) | REJECTED |
| R5 roster-maker compró el lado opuesto → cancelar | exceso | +0,008 (−0,104, +0,117), 3/9 d | REJECTED |
| R6 perdedoras ya compraron mi lado ≤tf−5 s → cancelar | exceso | +0,003 (−0,032, +0,041); el 55-78 % del coste maker cae en mercado-lados con perdedoras previas | REJECTED |
| R6o perdedoras en el lado opuesto | Δ | −0,033 (−0,169, +0,115) | REJECTED |
| **R7a lado contrario de las perdedoras-tomadoras** (maker que les VENDE el barato = compra el complementario a 1−pc) | EV por € de capital | **+0,034 IC90 (+0,018, +0,049), sin2 +0,023, 8/9 d**, capital 0,77 M$ (+0,036 con rebate); frente a resto +0,002 y todo +0,004 | **SOLO INFORMATIVA**: un maker no elige quién le casa |
| R7b vender el barato en las celdas donde operan las perdedoras | Δ | −0,004 (−0,015, +0,008), 3/9 d | REJECTED: el valor está en la IDENTIDAD, no en la celda |
Mecanismos (hechos/inferencias): las ganadoras z≥2 son makers que entran más tarde (23 % ≥240 s); su ventaja sobre la población en las mismas celdas (+0,013/€) no es observable on-chain (inferido: gestión de órdenes) → inidentificable. Las perdedoras son tomadoras de longshots a ~0,20 con s≈126: pierden −0,20/€ OOS y ese dinero lo cobra el maker del complementario (+0,034/€), no quien puja el barato como B. **Binance: no medido (missing)** en este encargo.

## 4. Infraestructura de ballenas (S4)
- `ballenas_timing_history.csv` solo tiene filas de 5m desde **2026-10-22T12:08Z** (387.049 filas; 58.269 en banda): **DATA_BLOCKED** para un uso no circular sobre 06-21 Oct.
- `wallet_edge_score_por_marco.json` (generado hoy, circular): 33 de las 89 wallets del roster WF están en sus 3.120 entradas 5m; solo descriptivo. `smart_money_consensus.json`/`ballenas_timing_state` no usados (circulares).

## 5. €/año honesto y qué refutaría
- **Replicable por B: 0 €/año.** R2 (+0,035/€ sobre ~55-90 €/día de B ⇒ ≈ +700-1.150 €/año como techo) no es de wallets y no pasa α; queda como «B en BTC 0,15-0,30 frente a alts», ya cubierto por otros trabajos de celdas.
- Informativo: perdedoras persistentes ≈ 4.600 $/día de pérdida en banda (41.440 $ en 9 d, solo las marcadas z≤−2); el lado que gana es el maker del complementario (+0,034/€).
- Refutaría R7 como vía: que el flujo de las perdedoras NO se repita en el mismo mercado-lado tras su primer fill visible (ver §6).

## 6. Siguiente prueba (una, falsable; solapa con contrapunto_informado → coordinar con el chief)
**R8 «perdedora visible → vender el barato»**: tras el primer fill on-chain visible de una perdedora persistente (ventana d−7..d−1) como TOMADORA del lado barato s en (m,s) con bloque t, EV por € de capital de los fills maker del complementario (vender s) de la población en (m,s) con bloque en [t+5, t+60] s frente al resto de fills maker-complementario en banda del mismo día. Gate: n≥40 mercados, ≥10 días, Δ>0 IC90 días >0, sin 2 mejores >0, BTC y alts mismo signo; sin look-ahead (identidad solo ≥ bloque+~3 s). Coste: lectura de F_banda + T (≈1 min).

## 7. Reproducción, rutas y warnings
`cd experimentos/5m_barato/b_perdidas_22oct/ganadoras_persistentes && ulimit -v 3000000 && nice -n 19 ionice -c3 python3 scripts/e1_roles.py && python3 scripts/a1_roster.py && python3 scripts/a2_roles_relaciones.py && python3 scripts/a3_perdedoras.py && python3 scripts/a4_contraparte.py` (≈1-2 min cada uno; e1 ≈10 min). Lee M_/T_ de `VOL/agentes_datos/wallets_ballenas_b/` (fills maker banda y órdenes tomadoras) y escribe `VOL/agentes_datos/ganadoras_persistentes/` (R_D.pkl, F_banda.pkl, G_wdia.pkl, sets.pkl, roster_WF_wallets.csv). Hashes: `HASHES.txt`.
Warnings: (1) 16 días, todo EXPLORATORY; (2) rol del maker por fills on-chain, sin órdenes/cancelaciones (no observables); (3) «balance de pares» = media ponderada por coste (no mediana como decía el prereg); (4) WMAP de wallets se reconstruye por orden de carga (determinista); (5) rebate inferido 0,2·fee, no observado; (6) R7a usa la identidad ex post de la contraparte: no es una regla ejecutable.
