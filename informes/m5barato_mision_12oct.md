# Misión «5m barato» — rescatar, rediseñar y escalar (Javi, 12-Oct, prompt definitivo)

Objetivo: una política que compre el 5m a precio ejecutable con **EV neto condicionado a fill > 0**, que sobreviva a la
selección adversa y tenga capacidad hacia 200.000 €/año. Nada a dinero sin gates + /code-review medium + OK Javi.

## Paso 1 — Auditoría (HECHO 12-Oct)
Regla vigente = `vigia_5m_barato_forward.py` v4 (congelada 06-Oct 12:00Z; hash de config en `manifiesto.json`). Valor
relativo entre mercados anidados del mismo cierre C: referencias de apertura TWAP60 oficial (15m en C-900, 5m en C-300),
|gap| ≥ 1 bps. Lado s: ref15 > ref5 ⇒ Up15 implica Up5 ⇒ s = Up (si no, Down). bid15(s) es cota inferior de mercado de
P(s en 5m). **Señal**: margen_neto = bid15(s) − ask5(s) − 0,07·p(1−p) ≥ 0,05, con t ≥ C−300+1,5 s y t < C−10 s; libro
cruzado en cualquier pata ⇒ sin señal. **Evento** = primer instante (recepción de la fila q) con señal; re-arma tras 2 s sin
señal. **Oficial** = primer evento por (cierre, moneda). **Ejecución virtual**: límite p_lim = mayor precio de rejilla con
bid15(t0) − p − fee ≥ 0,05; llega a t0 + 215 ms; se llena contra los niveles 1-3 del ask del 5m en ese instante (lo que no
cabe = no llenado); stake 2 € (≥5 acciones). **PnL** = acciones × (pago oficial − precio − fee). Desenlace oficial por id.
Latencia 215 ms = POST medido 05-Oct (mediana 226 ms, incluye 150 ms de taker delay) + ~25 ms WS/decisión; jitter p95 700.
Nada se envía: es dry-run puro. Datos: registro ms (`maker_ms_*`, 4 d) + archivo 60 d `registro_5m_barato` en el volumen.

## Paso 2 — Reproducción (HECHO): `analisis_5m_barato_autopsia.py`
28 señales OOS (06-11 Oct), desenlace oficial 28/28. Reproduce el informe oficial al céntimo: 10 ejecutables a +215 ms,
+9,69 €, EV +0,413 €/€, −6,17 € sin la mejor operación. Mejor operación: BTC Up 10-Oct 15:56Z, ask señal 0,11, llenado
18,2 acc a 0,12 (clase D, otro nivel barato), +15,87 €. Sin BTC: −1,0 €/€ (1 sola ejecución no-BTC… todas perdedoras).
Deriva: últimos 3 días EV +0,19 / fill 32 % (7 ejecutables) vs anteriores +0,82 / 50 % (3): n diminuto, compatible con azar.
Clases a +215 ms: A sigue barato 9 · B cancelado/repreciado 8 · C consumido por tomador 10 · D otro nivel barato 1.
(C = el ask desaparece con operaciones registradas; B = desaparece sin operación: lo determina el vigía con filas t/q.)

## Paso 3 — Autopsia de selección adversa (HECHO) — RESULTADO CENTRAL
| a +215 ms | n | acierto | EV €/€ al ask de la SEÑAL (t0) |
|---|---|---|---|
| desaparecen (B+C) | 18 | 83 % | **+1,67** (IC90 por cierre +0,99/+2,81) |
| quedan (A) | 9 | 33 % | **−0,37** |
| todas al ask t0 | 28 | 68 % | +1,15 (IC90 +0,67/+2,05; sin mejor op +63,7 €) |
**La señal tiene valor en el instante de detección; otros se lo llevan en <215 ms y lo que queda es perdedor.**
Selección adversa medida, no supuesta. El contrafactual t0 NO es alcanzable como tomador (taker delay 150 ms + POST).

## Paso 4 — 5M_CHEAP_V2_ALL_SIGNALS (CONGELADA 12-Oct 16:00Z, hash af25ccdef65ef8a3)
`vigia_5m_barato_v2_forward.py` (cron 05:05, Telegram): todos los eventos (re-armes incluidos), L215, tope 3 ejecuciones y
6 € por mercado, unidad = cierre. Descubrimiento (06-11, NO es evidencia): 51 señales, 24 ejecutables en solo 12 cierres,
IC90 por cierre (−0,0/+2,21); con tope: 13 mercados, EV +0,985, sin BTC −1,0. Estado: **FORWARD_PENDING**.

## Registro de versiones
| versión | hash | estado | resultado |
|---|---|---|---|
| v4 primera señal | manifiesto vigía | TESTING (OOS desde 06-Oct) | +0,413 €/€ n=10, depende de 1 op; sin BTC −1,0 |
| V2 todas las señales | af25ccdef65ef8a3 | FORWARD_PENDING (desde 12-Oct 16:00Z) | descubrimiento +0,985 (no cuenta) |
| H6 maker anticipatorio valor relativo | `analisis_5m_barato_maker_sim.py` | NO ROBUSTA (viva, Javi: no se descarta) | 06-11 Oct: M0,05 −0,06/−0,08 €/€ (48-106 merc.); única celda + (M0,10 lag 0, +0,31, n=23) = la más optimista de 9, lag 100 −0,02, sin BTC −0,21; rellenos ~50 % acierto (selección adversa del maker); pasivo +0,005 |

## Siguientes experimentos (prioridad por valor económico esperado)
1. **H6 MAKER ANTICIPATORIO de valor relativo** (el más prometedor por la autopsia): tener YA puesto un bid en el 5m (lado s)
   a p ≤ bid15(s) − fee − margen, cancelando/recolocando cuando cambia bid15 (cancelación medida ~60 ms; el maker no paga
   taker delay). Si un vendedor pone el ask barato, cruza contra nuestro bid y nos llena a nosotros primero (prioridad
   precio-tiempo). Riesgo a medir: fills cuando bid15 está rancio (selección adversa del maker). Simulación sobre el registro
   ms (q de ambas patas + operaciones t por recepción) y el archivo 60 d; cola conservadora; reembolso de maker aparte.
2. **H1/H3 EV actualizado a la llegada**: recalcular el margen con bid15 y ask5 en t0+L; no comprar si bid15 cayó (las A
   perdedoras). Se mide en el mismo simulador.
3. **Valor de la latencia**: supervivencia L150 48 % vs L215 36 %; EV a L150 +0,58 (13 fills, informe). Un tomador no baja
   de ~250 ms reales (CLAUDE.md): valor bajo salvo vía maker o VPS junto al CLOB (decisión Javi).
4. **Capacidad hacia 200k**: hoy ~2 ejecutables/día × 2 € → irrelevante; la cifra solo es discutible si H6 da EV>0 con
   fills/día y tamaño muy superiores. Se calcula con los fills del simulador, nunca con señales.

## Resultado H6 (12-Oct 16:40Z)
El valor de la señal solo existe para el TOMADOR MÁS RÁPIDO: un bid quieto en el umbral se llena ~50 % (quien cruza contra él sabe algo). Siguiente: valor económico de la latencia (profundidad al precio barato en t0 —columnas cap* del vigía—, señales/día, EV a L=100-150 ms) → ¿justifica VPS junto al CLOB (decisión Javi)? y distancia a 200k.

## Valor de la latencia (12-Oct 17:30Z, `analisis_5m_barato_latencia.py`, OOS 06-11 Oct, desenlace oficial 100 %)
- Señales: 4,7/día (primera por cierre-moneda, 28 mercados en 6 días); 8,5/día contando re-armes (mismos 28 mercados).
- Profundidad al precio barato en t0 (solo nivel 1): P50 7,7 € · P75 28 € · P90 99 € · máx 290 €.
- Stake 2 €: L215 36 % ejecutable, EV +0,41, +1,6 €/día · L150 46 %, +0,58, +3,0 €/día (IC90 cruza 0) · L0 (contrafactual)
  100 %, +1,15 (IC90 +0,67/+2,05), +13,3 €/día. L100 no medida (acotada entre L0 y L150).
- Techo teórico (L0 y TODO el nivel 1, una compra por mercado): +218 €/día (~80 k€/año) — pero 61 % de UNA operación
  (BTC a 0,11, +796 €); sin las 3 mejores +14 €/día; sin BTC −8,7 €/día. "Todas las señales" daba +827 €/día por DOBLE
  CONTEO de la misma liquidez en re-armes (descartado).
- Capacidad a L215 (vigía): stake 100 € → +653 € en 6 días, EV +0,83, pero sin el mejor día −0,19: la misma operación.
**Lectura**: ser más rápido ayuda (L215→L150 duplica el PnL/día), pero a escala realista son unos euros al día; el techo
depende de pocas ventanas BTC muy baratas y profundas. Sola, esta estrategia no es ruta a 200k (548 €/día); como mucho, un
componente si la latencia baja mucho (<100 ms, VPS junto al CLOB: decisión Javi) y si el forward confirma que esas
ventanas BTC se repiten. Siguiente: forward V2 + vigilar frecuencia de ventanas BTC "muy baratas y profundas".
