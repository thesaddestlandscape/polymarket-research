# H43 R5K — auditoría de datos (19-Oct-2026 ~07:50Z, market-data-engineer haiku; archivado por el chief)

**Veredicto:** no hay corrupción de datos ni look-ahead que explique la divergencia in-sample (+0,20) vs forward (−0,19/−0,29). Las diferencias entre implementaciones son de DEFINICIÓN y mueven el agregado ±0,01 y un día hasta ±0,1. Etiqueta: **EXPLORATORY (EN CURSO)**. Pendiente revalidación con sonnet/opus.

## Cifras corregidas (UNA definición: K cosechable = 50 acc con T∈(60,270], solo unidades completas, día = cierre UTC)
Fuente: `a7_cierre_final.py` → `/root/polymarket-research-datalogs/h43_auditoria/a7_cierre_final.json`.
- In-sample 06-16 Oct: n=985, 963 cierres, coste 9.073 USDC, EV ponderado **+0,201**, IC90 cierre [+0,087;+0,315], IC90 días [+0,109;+0,294], 9/11 días+, sin 2 mejores días +0,135, sin top-20 +0,105. Por día: 06 +0,315 · 07 +0,071 · 08 +0,184 · 09 −0,113 · 10 +0,191 · 11 +0,172 · 12 +0,139 · 13 +0,245 · 14 +0,628 · 15 +0,425 · 16 −0,021.
- Forward 17-Oct: n=61, 555,8 USDC, EV **−0,190** por cierre (−0,275 por fichero = vigía), IC90 cierre [−0,555;+0,203]. 18-Oct pendiente del vigía (validador: 69 u., −0,306 por fichero).

## Causas demostradas
- C1 ventana K posicional (vigía) vs cosechable (registro/validador): 23 unidades incompletas 06-16 Oct.
- C2 día de fichero (vigía) vs día de cierre (descubrimiento): un mercado de frontera mueve el 17-Oct de −0,275 a −0,190.
- C3 unidades incompletas incluidas (vigía) vs excluidas (validador).
- C4 descubrimiento cosechaba hasta T=300 (registro dice 270): +0,004. El «n=1.010, +0,212» original NO se reproduce exacto (−5 u., −0,01).
- Los «+0,18/+0,15/+0,63» del 17-Oct SÍ se reproducen: cosechable, completas, por fichero, días 10/12/14-Oct.

## Descartadas con prueba
Orden (0 inversiones), desenlaces (cachés coinciden 40.467/40.467; cobertura 17-Oct 287/287), token→lado (580/580), cobertura on-chain (sin huecos salvo 19 bloques el 15-Oct; 17-Oct raw = m5_onchain), régimen de makers (sin colapso), look-ahead en la construcción.

## Arreglos propuestos (NO aplicados)
- A1 módulo único `h43_unidades.py` con la definición de arriba + test de regresión (89/78/71 u. de 10/12/14-Oct; vigía 17-Oct).
- A2 vigía congelado intacto; si se quiere la regla cosechable, sidecar nuevo de solo lectura (/code-review medium + OK Javi).
- A3 aclarar en REGISTRO: día = cierre UTC; incompletas no cuentan; el +0,212 no se reproduce exacto.
- A4 nunca gate ni veredicto por día.
- A5 repetir el cruce crudo del 18-Oct con el kall de ese día (rawcheck18.out INVÁLIDO).
- A6 antes de cualquier uso en vivo: validar que el «volumen adquirido por makers» (on-chain, a posteriori) se puede observar en vivo con el WS (trampa firehose).

## Límites
`ts_est` de m5_onchain es estimado por bloque (T con error de segundos; con 3-5 s de retraso n −9/−15 %, EV ~+0,17). Población = fills de makers ya en el libro: cota optimista, no captura demostrada. Scripts: `a3`-`a7` en esta carpeta; salidas en `/root/polymarket-research-datalogs/h43_auditoria/`.
