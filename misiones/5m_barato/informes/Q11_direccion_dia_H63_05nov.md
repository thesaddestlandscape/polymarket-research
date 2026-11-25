# Q11 (05-Nov, alpha-miner) - dirección del día ex ante, H63, H37-42, prereg SOL+0,13+calma
Datos reales usados: rellenos simulados de la escalera (dec2_D.pkl, 26-Oct..03-Nov, 9 d, ETH/SOL/XRP; 28.393 filas-variante) + Chainlink data/prices/chainlink_*.csv(.gz) filtrado source=chainlink, reloj de recepción, rasgos con datos <= tf-3 s (NaN 69-135 de 28.393, no predicen desenlace por construcción: se excluyen). LIMITE: las 22 d de m5_registro (05-26 Oct) NO tienen derivación de la escalera (esc_dec2 necesita la cinta sa_ms/libro5 desde 26-Oct); ampliar = trabajo pesado (post 09:30Z, load<4).
## 1. Dirección del día ex ante (experimentos/5m_barato/q11/q11_dir_dia.py, _b.py; q11_dir_dia_resultado.csv)
Alineado = signo(lado)*ret Chainlink. EV ponderado por EUR, alineado>0 vs <=0:
- T1 r1h: +0,389 (n=668) vs -0,125 (n=1234); spread +0,513, placebo bloque-mercado p=0,018, IC90 cierre (+0,15,+0,88), 8/9 d spread>0, sin 2 mejores +0,173 vs -0,219.
- T1 r6h: SIGNO CONTRARIO: alineado -0,148 vs +0,250; spread -0,399, p=0,016, IC90 cierre (-0,72,-0,07). r24h y desde 00:00Z: spread -0,22/-0,29, 3/9 d, p bloque 0,29.
- V2 (0,10/0,13/0,16) y G0 repiten el patrón (r1h +0,61/+0,31; r6h -0,54/-0,34).
Lectura: momentum a 1 h y reversión a 6 h con 9 días = no hay signo estable de la dirección; el residual de T1 lo ponen 26-Oct (+0,42) y 01-Nov (+0,64) frente a 7 días ~-0,1. Con 12 contrastes (4 ventanas x 3 variantes) el mejor p bloque 0,012 queda en ~0,14 Bonferroni; ventana elegida post hoc.
VEREDICTO: INSUFFICIENT (EXPLORATORIO, no regla). Si se quiere reabrir: prerreg r1h-alineado>0 (una ventana) forward >=10 d, juez forward_v2-style; no hay regla de salida limpia derivable aquí.
## 2. H63 filtro AS propio (q11_h63_as.py)
Walk-forward por día (corte = mediana de días previos, >=3 d de train), rasgos ex ante edad de la orden, lag al último salto, actividad 10 s, T, nivel; placebo por bloque-mercado (200 perm).
- G0: edad +0,117 (EV_kept +0,064 vs -0,053, 6/6 d) p=0,12; resto <=+0,03.
- T1: ningún rasgo aporta (edad -0,225, nivel +0,082 p=0,24, act10 +0,023).
VEREDICTO H63: REJECTED con estos rasgos (nada con p<0,10 tras 10 contrastes; edad invierte signo entre G0 y T1). nmk (barrido) excluido: es ex post.
## 3. H37-H42 (salidas): sin cambio. REJECTED el 17-Oct (H37/H40/H41, DECISION_LOG) en 09-13 Oct; reevaluar en 22 d necesita markouts post-relleno del registro ms (extracción pesada). Estado: INSUFFICIENT para reabrir, sin indicio de que cambie.
## 4. Prereg SOL+0,13+calma
misiones/5m_barato/docs/reverse-engineering/casos/RE-Q11/PREREG_Q11_SOL013.md (+ .sha256 38ebc6f85429ade9c7c04797c44806c2991431c3802f6b0e776a739ae330f96b). Forward desde 06-Nov, gates n>=40, >=10 d, sin 2 mejores >0, IC90 cierre >0, > PLA_T1 y > G0.
Gastados SOL L=0,13 (9 d): T1 n=117 +0,468 (sin2 +0,145, 5/9 d+); PLA_T1 +0,345; G0 +0,109 -> el placebo ya es positivo: el efecto es 'SOL a 0,13', no la calma. Prior: regresión a la media.
## Siguiente
cheap5m-statistical-validator: contrastar 1 y 2 (en especial el cambio de signo 1 h/6 h y el cálculo de ret) antes de citar nada; execution-engineer solo si el forward de SOL013 se acerca a n>=40 (el juez ya sale del cron 11:45Z; falta un script ana de filtro SOL/0,13).
