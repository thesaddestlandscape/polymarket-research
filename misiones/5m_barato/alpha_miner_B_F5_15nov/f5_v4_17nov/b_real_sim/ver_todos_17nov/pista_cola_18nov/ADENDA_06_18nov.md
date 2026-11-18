# ADENDA 06 al PREREG PISTA COLA (RE-B-COLA-CANCELA) — 18-Nov-2026. Etiqueta: MECANISMO (no EV, 0 órdenes). CONTRATO CONFIRMATORIO, vinculante para cheap5m-execution-engineer y statistical-validator.
Redactada por el agente de integridad de datos, ANTES de ejecutar p3 o run_p1 sobre ningún día del veredicto, sin ver tasas nuevas. Recoge el dictamen del validador estadístico (aprobado por Javi). Prereg, contrato y ADENDA_01-05 NO se editan: donde esta adenda es más estricta, prevalece ESTA. Solo especificación; la implementación es posterior y debe cumplir la lista H.
Nombres: tablas p1 `EV`, `PL`, `PW`, `CP`; campos `n_mk, C1, C2, q150, S, ty, suelo, sg, act2, WA_q, ttc, absr5, lvk, D, own`; desenlaces `f_V1..f_V7`, `f_*_e250`; estratos p7 `st` ∈ {z0, small, normal}; funciones p3 `pairs, ic_dias, ic_clus, tabla, maxstat`; p7 `eb, smd, design`. "Clase lo/hi" = `suelo`.

## A. Declaración de contaminación y días del veredicto
A1. Existe `out/obsoletos_preD1/p3_btc_act.json` (tasas evento−placebo pre-D-1 de 12 y 16-Nov: V1 +0,181, V4 +0,200, V5 +0,048, regla antigua, producidas ANTES de las ADENDA_01-05) y en 02-b se leyó FV1 de emparejados/sin pareja. Ambos hechos quedan declarados como información previa del equipo.
A2. 12 y 16-Nov = SOLO DISEÑO (fixtures, balance, calibración de reglas). No entran en ninguna tasa del veredicto ni en ningún gate.
A3. Días del veredicto: 13, 14, 15, 17, 18 y 19-Nov. Se exige ≥5 días VÁLIDOS (completos, que pasan E). 18 y 19-Nov solo cuando existan completos (cierre 24 h UTC + ficheros libro5_ms_prot, onchain_fills, m5_registro completos); si no, se esperan. Un día incompleto nunca entra parcial.
A4. Prohibido ejecutar p3 sobre tasas de 13-19-Nov antes de tener hashes congelados (K) y balance por día (E) calculado SIN columnas f_*.

## B. Test confirmatorio ÚNICO
B1. Una sola hipótesis confirmatoria: diferencia de tasa de disparo V1 (evento − control IPW+EB), población pooled (estratos z0+small+normal ponderados por la masa p7), clase de suelo `lo`, universo primario (n_mk=1, C1, sin propios), día = unidad.
B2. Multiplicidad: máximo-estadístico sobre las 7 variantes V1..V7 (permutación C3); p_maxstat <0,05 para V1.
B3. Estratos z0/small/normal: reportados con corrección Holm ×3 (sobre V1). Todo lo demás (V2-V7 por separado, hi, ETH/SOL/XRP, n_mk≥2, C2, otras ventanas, sens a/b/c, e250) = EXPLORATORIO, etiquetado así.
B4. Veredicto (reemplaza solo la parte estadística del prereg; M1/M2/LR/H-ACT se mantienen como en el prereg):
 SOPORTADA: B1 diferencia >0, p_maxstat(V1) <0,05, IC90 por días (C1) >0, semiancho pooled ≤0,03, gates C5 cumplidos, LR(V1) ≥1,5, y exceso n_mk=1 ≥ exceso n_mk≥2 (si no, H-ACT).
 NO SOPORTADA: semiancho pooled ≤0,02 Y límite superior del IC90 (el más ancho de C1/C2) < +0,02 (o diferencia ≤0), n ≥300 eventos primarios, ≥5 días válidos.
 INSUFFICIENT: todo lo demás (semiancho entre 0,02 y 0,03 con IC cruzando 0, small >0,06, <5 días, balance, hi sin datos). Nunca «cerrada».

## C. Inferencia
C1. Unidad = DÍA. Diferencia diaria ponderada d_D = Σ_w f_ev − Σ_w f_ctrl (pesos p7 normalizados dentro del día, estratos p7 incluidos). IC90 = t de Student con df = (días válidos − 1) sobre {d_D}, media simple de días (si pesos por día se usan, declarar y reportar también la simple).
C2. Secundario: bootstrap por MERCADO (remuestreo de mercados completos, eventos+controles juntos, B=2000). Se reportan ambos; el que decide es el MÁS ANCHO.
C3. Permutación con signo por mercado sobre d_m = Σ f_ev(m) − Σ ω f_ctrl(m) (ω = pesos p7 de los controles del mercado m); 2.000 permutaciones, cambio de signo de d_m completo por mercado; p = máx-estadístico sobre las 7 variantes (estadístico = media ponderada de d_m estandarizada por variante).
C4. Gates de semiancho (del IC decisivo de C1/C2): pooled ≤0,02 para declarar NO SOPORTADA; ≤0,03 para poder leer SOPORTADA; estratos small ≤0,06, si no INSUFFICIENT para ese estrato.
C5. Concentración: ningún día >35 % del peso total (Σ masa p7 del día / Σ total); signo de la diferencia pooled estable dejando fuera cada día (leave-one-day-out, todos los signos iguales). Si falla → no puede ser SOPORTADA (INSUFFICIENT) y se reporta.
C6. Reportar siempre: n_eventos, n_eff (Kish), días, mercados, y EV/diferencia sin los 2 mejores días.

## D. Campos nuevos en p1 (eventos y controles, MISMA función de cálculo, datos con rx ≤ t−1000 ms, reloj de RECEPCIÓN)
D1. `dist_ticks` = (mejor bid − p)/tick (tick vigente del token) al instante t−1000; ΣQ de los niveles mejores (`SQ_mej`, p'>p, bid del mismo token); `act2_mej` = actividad (nº de cambios, igual definición que act2) de esos niveles en [t−1000−W, t−1000) con W igual al de act2; `spread` (ask−bid mejor); `dp_signed` = variación con signo del mejor bid del token en [t−2000, t−1000); `sg` (sg estructural ya existente, recalculado ≤t−1000); `edad_nivel` = t−1000 − nacimiento del nivel (último instante con Q=0 previo), censurado y marcado si nace antes del inicio del fichero.
D2. Equilibrio EB: (i) el EB incluye `dist_ticks` como covariable, O bien se exige igualdad exacta del rango en ticks desde el top entre evento y control (se declara cuál en la implementación y se aplica a todos los días); (ii) si el KS evento/control de `edad_nivel` > 0,10 en cualquier estrato con n≥100, `edad_nivel` (log1p) entra en z0 y en el diseño EB; (iii) EB y pesos SEPARADOS por clase de suelo (lo/hi); (iv) sensibilidad obligatoria «solo nivel propio» (controles únicamente del mismo (token,p)), con su n_eff; (v) pooled reportado CON y SIN z0 (el indicador WA_q==0).
D3. Ningún campo nuevo usa información > t−1000 ni columnas f_*, C*, F*. Un campo NaN por falta de datos ≤t−1000 se marca; NaN no puede correlacionar con evento/control (test: SMD del indicador NaN ≤0,10), regla ya fijada tras la fuga R8-R10.

## E. Balance por DÍA COMPLETO (sin mirar desenlaces)
E1. Simple (emparejado p7): |SMD| ≤0,10 objetivo y ≤0,15 TOPE en cada estrato con n≥100, por día.
E2. Primario (IPW+EB): eCDF/KS máximo ≤0,10 en act2, WA_q, ttc, |r5| y dist_ticks (ponderado); además n_eff Kish por día y estrato.
E3. Prueba sin desenlaces: control del nivel propio frente a control vecino dentro de z0 y small, |SMD| ≤0,10 en las 7 covariables de p7 + dist_ticks + edad_nivel.
E4. Regla fijada AHORA: si un día falla E1, E2 o E3 en el estrato/clase del test confirmatorio, ese día se EXCLUYE del veredicto (se reporta y se cuenta contra los 5 días mínimos). Prohibido decidir exclusiones tras ver f_*. Si quedan <5 días → INSUFFICIENT.

## F. Unión on-chain (49 %)
F1. Por día: SMD de covariables pre-ventana (act2, WA_q, ttc, |r5|, dist_ticks, edad_nivel, suelo, ty) entre eventos con n_mk=NaN y eventos unidos. Si cualquier |SMD| >0,15 en un día → el veredicto se reporta TAMBIÉN sin restringir por n_mk (universo C1 completo, controles IPW sobre ese universo), y ambos deben coincidir en signo; si discrepan → INSUFFICIENT.
F2. Falsos emparejamientos (ventana ±60 s) reportados por día.

## G. Control p5 (descriptivo hasta cumplir la condición)
G1. Estratos: moneda × bin de dt × bin de vida (bins por terciles de las pujas, fijados en el día de cálculo sin mirar fill).
G2. Ancla válida solo si vida − dt ≥500 ms. Excluir anclas a ≤300 ms de un repegado propio.
G3. Reportar fracción cubierta (pujas, rellenos, no-rellenos retenidos).
G4. M3/R1 sobre B legible SOLO si el balance de dt y vida dentro de estratos queda |SMD| ≤0,15; si no, etiqueta DESCRIPTIVO y no se cita como evidencia de discriminación.

## H. Criterios de aceptación (binarios, para que el validador compruebe la implementación)
1. HASHES_CODIGO.txt contiene sha256 de p1_dia, p3_agrega, p7_ipw_balance, p5_control_sin_relleno, run_p1.sh y de esta adenda, escritos tras implementar y ANTES del primer día; los hashes en disco coinciden.
2. p3 excluye 12 y 16-Nov (lista de días del veredicto = {13,14,15,17,18,19}; falla si aparece otro).
3. p3 no se ejecuta sobre tasas si falta el informe de balance por día (E) o si algún día incompleto está en la lista.
4. p1 genera dist_ticks, SQ_mej, act2_mej, spread, dp_signed, sg, edad_nivel para eventos Y controles con la misma función.
5. Test unitario/aserción: ningún campo D usa rx > t−1000 (comprobación por muestra de ≥1.000 filas por día).
6. Los campos D no contienen NaN asimétrico (SMD del indicador NaN ≤0,10) o p7 los trata y lo reporta.
7. EB incluye dist_ticks o se verifica igualdad exacta de rango en ticks; implementación declara cuál.
8. edad_nivel entra en z0/diseño si KS>0,10 (check automático escrito en el informe).
9. EB y pesos calculados por clase de suelo lo/hi por separado.
10. Informe incluye la sensibilidad «solo nivel propio» con n_eff.
11. Informe incluye pooled con y sin z0.
12. Balance simple por día: |SMD| ≤0,15 en cada estrato n≥100 (tope) y se marca ≤0,10 objetivo.
13. Balance primario por día: KS ≤0,10 en las 5 variables de E2 y n_eff por día.
14. Prueba control propio vs vecino (E3) calculada sin leer f_* (aserción de columnas) y |SMD| ≤0,10.
15. Días que fallan E1-E3 están excluidos automáticamente según E4 y listados.
16. Test confirmatorio = V1 pooled, IPW+EB, clase lo; max-stat sobre V1..V7 (2.000 permutaciones, signo por mercado, d_m según C3).
17. Holm ×3 aplicado a estratos; resto marcado EXPLORATORIO en el JSON.
18. IC90 por días usa t de Student con df=días−1; IC bootstrap por mercado presente; el decisivo es el más ancho.
19. Gates de semiancho 0,02 / 0,03 / small 0,06 implementados tal cual.
20. Regla ningún día >35 % del peso y leave-one-day-out del signo, reportadas.
21. F1: SMD n_mk=NaN vs unido por día; si >0,15 se emite veredicto sin restringir por n_mk y se comparan.
22. p5: estratos moneda×dt×vida, vida−dt ≥500 ms, exclusión de ±300 ms de repegado propio, fracción cubierta; M3 marcado DESCRIPTIVO salvo SMD ≤0,15.
23. El veredicto emitido pertenece a {SOPORTADA, NO SOPORTADA, INSUFFICIENT} y aplica B4 literalmente.
24. Se reportan: n_eventos, n_eff, días, mercados, resultado sin los 2 mejores días, y se repiten V1 y V1_e250.
25. Ningún fichero de código de la lista del punto 1 modificado tras la firma (verificable por hash y mtime).

## Regla de oro
Ningún cambio de código tras firmar esta adenda salvo mediante una ADENDA_07 justificada por escrito ANTES de ver tasas (si ya se han visto tasas de 13-19-Nov, la ADENDA_07 solo puede ser aclaratoria y obliga a declarar «tasas vistas» y a repetir el veredicto como EXPLORATORIO). Los hashes de código se congelan en HASHES_CODIGO.txt al terminar la implementación y ANTES del primer día de veredicto. Esta adenda se firma con su .sha256.
