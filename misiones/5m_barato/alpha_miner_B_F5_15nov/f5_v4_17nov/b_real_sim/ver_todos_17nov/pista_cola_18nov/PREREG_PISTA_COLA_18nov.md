# PREREG PISTA COLA (RE-B-COLA-CANCELA) — 18-Nov-2026. Etiqueta: MECANISMO. Prohibido EV (salvo M3 sobre B 20-23 Oct como mecanismo). 0 órdenes.
Contrato vinculante: ../CONTRATO_PISTA_COLA_18nov.md (sha en ../CONTRATO_PISTA_COLA_18nov.sha256). Este prereg se congela ANTES de ejecutar p1/p2/p3.

## Hipótesis
H-CANC: en casados con un solo maker comprador (n_mk=1) en (tx, token X, p∈[0,10;0,30)) con cola>0 justo antes, la masa del nivel (y/o de niveles mejores) se evapora SIN imprimir en los ms previos al casado más de lo que se evapora en instantes emparejados sin casado.
H0 (nula): la evaporación previa es la misma que en el placebo emparejado (los casados ocurren en niveles más activos; n_mk=1 + Q>f es FIFO con el maker en cabeza y el resto detrás).
H-ACT: el exceso existe pero también en n_mk≥2 en igual medida (actividad general previa al tomador, no «cola delante que deja solo al último»).

## Datos
BTC 5m (primaria) días 11..17-Nov (libro5_ms_prot, onchain_fills, m5_registro x, sonda1 fotos para token↔slug). ETH/SOL/XRP aparte (secundario, si da tiempo). B 20-23 Oct (tomador_202.pkl + misma_orden_rows.pkl) para los 98 clase 1 y M3.
Reloj: RECEPCIÓN (c[6] de libro5_ms; c[7] de m5_registro x). Suelo por ventana de 5 min = p1(rx−ex) de filas d (≥200): lo ≤28, hi ≥33, indet. Resultados por clase de suelo antes del agregado.

## Unidad y definiciones (tal cual contrato §1-§2)
Evento = cluster de T (gap<300 ms) en nivel bid (X,p) (SELL X a p = dir; BUY comp a 1−p = mint); t_c = recepción del 1.er T. n_mk por unión con on-chain (regla mejorada, ver hueco a). Universo primario: n_mk=1 Y C1 (Q(t_c−150) − f > 0). C2 reportado aparte.
Masa cancelada en W = max(0, Q(inicio) − Q(fin) − impreso en W). Ventanas [−1000,−300), [−300,−150), [−150,−50). Repeg = caída compensada por subida ≥90 % de la misma masa en otro nivel bid del mismo token en ±5 ms (se resta).
Placebo EMPAREJADO: mismo (token,p) (fallback: mismo p, otro token del día), instante sin T en el nivel ±1 s, Q(t−150)>0, mismo estrato: tercil Q(t−150), bucket 60 s de tiempo al cierre, tercil |r5| Binance BTC (rx ≤ t−50), tercil actividad d del nivel en [t−1000, t−50) (desviación declarada: el contrato dice ±1 s; se usa solo la parte previa porque el propio relleno contamina el post).

## Regla primaria y variantes (7, máx-estadístico)
V1 = R1 primaria: dispara en t_e si masa cancelada sin imprimir en NUESTRO nivel en (t_e−300, t_e] ≥ 50 % de Q(t_e−300).
V2 τ=150 θ=50 %; V3 τ=1000 θ=50 %; V4 τ=300 θ=25 %; V5 = R2 (misma regla sobre la masa agregada de niveles MEJORES p'>p); V6 = R3 (salto Binance BTC rx ≥1 bp contra el token en (t_e−300, t_e]); V7 = V1 ∨ V5.
Evaluación: t_e ∈ [t_c−1000, t_c − 20 − L_total]. L_total p50 = 20 + 0 + 33 ms; p90 = p95(rx−ex) de la ventana de 5 min + 147 ms (paquete_l B2/B3/B5 13-Nov según contrato §8).
Estadístico por variante: diferencia de tasa de disparo evento − placebo emparejado (pares). Permutación: intercambio de etiquetas evento/placebo POR MERCADO (todos los pares de un mercado juntos), 2.000 permutaciones, p de cada variante contra el máximo de las 7.

## Métricas (contrato §8, tal cual)
M1 = fracción de eventos n_mk=1 con cola>0 (C1 y C2 por separado) en que R1 dispara a tiempo; éxito ≥50 % con L p90 y ≥70 % con p50.
M2 = LR = P(R1|evento) / P(R1|placebo emparejado); éxito LR ≥3.
M3 = sobre los rellenos de B 20-23 Oct (mecanismo): rellenos que R1 cancelaría, Σpnl de evitados, buenos perdidos vs malos evitados (€). Si no hay L2 de esos rellenos → NO EJECUTADO / DATA_BLOCKED.

## Criterio de veredicto (BTC, universo primario)
SOPORTADA: diferencia V1 evento−placebo >0 con p_maxstat <0,05 Y IC90 por días >0 en la clase lo (y en hi si n≥100 eventos hi) Y LR(V1) ≥1,5 Y el exceso en n_mk=1 ≥ exceso en n_mk≥2 (si no, se declara H-ACT en vez de H-CANC).
NO SOPORTADA: diferencia V1 ≤0 o IC90 por días con límite superior < +2 pp, con n ≥300 eventos primarios y ≥5 días.
INSUFFICIENT: cualquier otro caso (incl. n insuficiente, unión on-chain demasiado baja para clasificar n_mk, hi sin datos).
M1/M2 se reportan contra sus umbrales como «solución R1 útil / no útil», independiente del veredicto de mecanismo.

## 98 de B (directo, contrato §7.10)
Masa delante cancelada = cola al colocar (A0 = `cola` de tomador_202) − Σ taker_amt de fills on-chain side=0 en (tok, L) de otros makers ANTES del nuestro (bloque anterior o mismo bloque con log_index menor), desde la colocación. Sensibilidad de frontera de bloque: fills con ts_est > t_ini/1000 + 1,4 s (cota baja de cancelado) y + 3,8 s (cota alta). Reportar en clase 1 (n=98) frente a TP/otros (n_mk≥2) como control.

## Huecos (a)(b)(c)
(a) unión: T fila → agregado on-chain por (tx, X, p) sumando bids de X + asks del complementario a 1−p, ventana ts_est·1000 − rx ∈ [+800, +4500] ms; fallback por fila individual (s5). Falsos emparejamientos = misma regla con la ventana desplazada ±60 s.
(b) proxy: makers persistentes definidos en días impares (≥20 tx en banda), medidos en días pares, y al revés; evaporación V1 en eventos n_mk=1 cuyo maker es persistente vs no. Nunca se afirma que cancelan.
(c) llegada: cota t_llegada ≈ t_c − 20 − [145, 215] ms; fracción de eventos con salto Binance ≥1 bp contra el token ≥50 ms ANTES del inicio de la evaporación, vs placebo.

## Lo que NO se hace
Ningún EV, ningún forward CXB, nada del vigía congelado, ninguna orden. Lo no ejecutado se lista como NO EJECUTADO.
