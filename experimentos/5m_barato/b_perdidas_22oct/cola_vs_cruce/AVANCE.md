# AVANCE cola vs cruce (22-Oct ~16:00Z) — clasificación validada + primer EV. EXPLORATORY. B no tocado.
Preregistro P1 congelado antes de calcular población: `prereg/PREREG_P1_CLASIFICACION.md` (sha256 0552983b…; lo ya visto, declarado en él).

**Definición (on-chain, sin reloj WS):** cada relleno maker = largo en c a pc. C1 = la MISMA tx rellena a otro maker más hondo (la orden
tomadora atravesó nuestro nivel = barrido en sentido estricto). C2 = no C1, pero en una tx posterior del mismo bloque o del siguiente
(~2 s) se rellena a alguien más hondo (se sigue casando por debajo). C3 = COLA (ni C1 ni C2). CRUCE = C1 ∪ C2.

**Validación sobre B (183 de 186 posiciones clasificadas; 3 sin token del 22-Oct tarde = missing; 175 con desenlace):**
concordancia con la clase WS de r3 (print por debajo en 1 s) 122/144 = 85 % (39 sin print WS: on-chain sí las clasifica).
«Cola» NO es relleno lento ni tardío: edad de la orden al relleno, mediana C1 1,8 s / C2 1,9 s / C3 2,2 s; rellenos tardíos 7/100 C3 vs 9/83 cruce.

| | n | EV €/€ | IC90 por día | IC90 por cierre | sin 2 mejores días | hit / precio |
|---|---|---|---|---|---|---|
| B C3 COLA | 95 | +0,097 | (+0,001, +0,171) | (−0,288, +0,493) | −0,116 | 23,2 % / 0,216 |
| B C1 barrido misma tx | 33 | −0,033 | (−0,29, +0,34) | | −0,34 | 21,2 % / 0,219 |
| B C2 se sigue casando por debajo | 47 | −0,349 | (−0,89, +0,12) | | −1,00 | 17,0 % / 0,213 |
| Población C3 COLA (28.871 unid., 17-22 Oct) | 18.627 | +0,003 | (−0,072, +0,089) | (−0,057, +0,063) | −0,070 | 21,2 % / 0,207 |
| Población C1 | 3.763 | +0,011 | (−0,085, +0,116) | | −0,085 | 21,2 % / 0,210 |
| Población C2 | 6.481 | −0,110 | (−0,199, −0,014) | (−0,190, −0,027) | −0,185 | 18,1 % / 0,206 |

Diferencia COLA−CRUCE en población: +0,067, IC90 por días (−0,003, +0,117), 4/6 días; estratificada por moneda×tramo de precio×tramo T: +0,068.
**Lectura honesta (3 puntos):**
1. El barrido en sentido estricto (la orden que nos rellena atraviesa nuestro nivel, C1) NO es lo malo: ≈0 en población y en B.
2. Lo malo es C2: que se siga casando por debajo en los ~2 s siguientes. La separación crece con la ventana que se mira después
   (COLA−CRUCE ≈ +0,04 mismo bloque, +0,07 a 1 bloque, +0,09 a 2, +0,21 a 5 bloques): es un MARKOUT ex post, no un tipo de relleno.
3. Antes del relleno casi no se predice (población, AUC C2): distancia al top 0,56/0,53; tamaño del top 0,54/0,54; nivel bid15 0,51/0,49;
   solo actividad vol30 0,59/0,60 (es R1, ya en forward). Gate P1 para pasar a palancas: FALLA (IC por días >0 solo en XRP; dist no pasa 0,55 en 20-22).
Siguiente: medir palancas directamente sobre EV con controles de igual volumen (incluido C2 de E1b, seguir el bid con 250 ms), sin
pasar por la etiqueta cola/cruce. Detalle y scripts en `scripts/`, datos en `datos/` (fuera de git).

## Avance 2 (22-Oct ~16:40Z) — aviso sobre «C2» de E1b (seguir el bid a 250 ms)
- **B real YA sigue el top en ~0,2 s.** Ledger de B (repega/cancela_banda) contra libro5: retraso repega − último cambio del top bid,
  p10/p50/p90 = 0,08 / 0,21 / 0,46 s (n=818 emparejadas de 3.199; el 91,6 % < 0,5 s; el 1 % ≥ 1,5 s) (`scripts/p2_verif_repega.py`).
  En el código (`experimento_maker_h47.decidir`) el 1,5 s es el ASENTADO tras cancelar (no repone hasta 1,5 s), no una espera a que el
  top se quede quieto. E1 (y la BASE preregistrada de mi E1Q) modelan B con la orden RANCIA 1,5 s tras moverse el top: ese BASE no es B.
  Por tanto el +0,076 de C2 en E1b (y mi S250: +0,051 frente a BASE en ELEGIR 17-19, IC90 por días +0,033..+0,077, retención 0,90)
  mide sobre todo el error del simulador, no una palanca nueva para B. Se mide aparte con un BASE fiel a B (B_FIEL; exploratorio).
- Simulador con cola E1Q (libro L2 libro5) construido; ELEGIR (2.160 mercados): BASE −0,238 (X1 atraviesa −0,339, X2 −0,211, X3 cola −0,066).

## Avance 3 (22-Oct ~18:10Z) — P2 terminado (ELEGIR 17-19: 2.160 mercados; MEDIR 20-22: 1.752 mercados), P3 (señales L2) en marcha
- Gate preregistrado P2 (S250 vs BASE, MEDIR): +0,122, IC90 por día (+0,074, +0,189), por cierre (+0,053, +0,187), 3/3 días, p igual
  volumen 0,000, retención 0,92 → PASA formalmente, PERO el BASE preregistrado (E1) no es B: B real ya repega a ~0,2 s. Sin palanca nueva.
- Simulador fiel a B (B_FIEL, reacción medida 280 ms, reposición 1,5 s): tasa de relleno 0,58 vs B real 0,61 en las mismas 239 pujas,
  acuerdo puja a puja 0,74 (el BASE de E1: 0,79 vs 0,61, acuerdo 0,70). EV B_FIEL: ELEGIR −0,171 / MEDIR +0,115 (régimen).
- Sobre B_FIEL (exploratorio): cancelar más rápido (65 ms en vez de 280 ms tras cambiar el top) = +0,155 (ELEGIR) / +0,105 (MEDIR, IC90
  por día +0,055..+0,221) con p de igual volumen 0,03/0,10, pero retiene solo 42-48 % del €: reduce volumen. Reponer a 250 ms (BF_R250)
  sube el volumen ×1,4 a EV ≈ igual (+0,022 / ver INFORME). K0, K10, KMAS, COLA50: sin efecto robusto (signo cambia entre periodos).
