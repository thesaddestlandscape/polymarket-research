# VALIDACIÓN INDEPENDIENTE de RE-CANCEL-B (E-RE-CB-01/02) — 26-Oct-2026. Veredicto: **VALIDADO CON RESERVAS**. Validado: 0 €.
Fuente: informe del validador independiente transmitido por la sesión principal (chief) el 26-Oct; copiado aquí fielmente por cheap5m-reverse-engineer (no es trabajo propio; el reverse-engineer NO aprueba su propio caso). Los scripts del validador no están en esta carpeta (scratchpad del validador).

## R1 (sin auto-print, E-RE-CB-02)
- ΔAUC M − placebo +90 s: +0,0675 (IC90 −0,002..+0,134 con semilla 11). Con semillas 1-5 el límite inferior cae en 0,000..+0,002 → según la ADENDA_R1 el resultado es PARCIAL en vez de REFUTA (IC en el filo según semilla).
- Reimplementación propia del validador: ΔAUC +0,055 (IC90 −0,019..+0,127), P_M 0,447, sesgo −0,051.
- Sensibilidad extrema (quitando también los prints de varios makers): ΔAUC +0,030, sesgo −0,094.
- Redacción correcta: «transferencia NO SOSTENIDA / NO DEMOSTRADA» (cota pesimista), no «refutada por poco».

## Puntuación ingenua (post-hoc, EXPLORATORY)
- Definición: volumen de prints que consumen el PRIMER objetivo de la puja hasta T−60 s (sin replay de cancelaciones).
- AUC 0,712 con prints propios / 0,706 sin prints propios.
- M − ingenua: ΔAUC +0,082 (IC90 +0,016..+0,152) con auto-print; −0,007 (IC90 −0,078..+0,068) sin auto-print.
- Lectura: la ventaja de ORDENACIÓN de M sobre la ingenua sale del auto-print; sin él, M solo aporta calibración de NIVEL (P_puja), no discriminación.

## Correcciones al expediente
- §6: «56/98 casados» se debe a VARIOS makers (41 rellenos multi-maker: 29 con print a precio de B pero con otro tamaño), no a tamaño parcial.
- §4 y H-CB-1 sobrevaloran la utilidad (la regla mecánica explica la vida, pero la discriminación del relleno sin auto-print no supera a la ingenua).
- §8: validación independiente = HECHA (VALIDADO CON RESERVAS, 0 €).

## Reservas
1. IC del ΔAUC sin auto-print en el filo según semilla (límite inferior −0,002..+0,002).
2. El mtime del PREREG no prueba el orden (no se puede probar la ausencia de pruebas interactivas previas).
3. TEST no virgen; 2 días (22-23 Oct); IC por cierre, no por días.

## Intervalo a reportar para F8/A1/R3 (siempre EXPLORATORY; pujas tipo B, bid 0,11-0,30, ETH/SOL/XRP)
- P_puja ∈ [0,44 sin auto-print; 0,52 con auto-print] frente a 0,497 real (TEST, n=187 pujas, 64 cierres).
- AUC ∈ [0,70; 0,79].
- Usar el extremo SIN auto-print, con sesgo ≈ −5 pp.
- Comparar SIEMPRE contra la puntuación ingenua (sin auto-print, M no la supera en ordenación).
