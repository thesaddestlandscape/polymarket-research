# ADDENDUM A1-A8 a PREREG_E1b_CONFIRMACION_S1.md (v2) -- 22-Oct-2026 ~15:55Z
Historial: v1 (sha256 1b6d4175...559d, fijada 15:27Z, guardada como ADDENDUM_E1b.v1_sustituido.md) se sustituye por esta v2 ANTES de que exista ningun dia forward y antes de aplicarla
a ningun dato >= 23-Oct. Motivo: al validarla sobre 17-22 Oct el control A5 estaba mal disenado: C2 con SETTLE=0 es un re-cotizador de latencia cero (irreal) y C1/C2 conservan solo el 23 %/32 % del coste
(dPnL/EUR +0,13/+0,18 por puro volumen, con EV por EUR peor o igual que base), asi que "S1 > max(C1,C2)" no se podia cumplir nunca. Unicos cambios: A5 (C2 y criterio). Nada mas.
Fijado ANTES de existir ningun dia >= 2026-10-23 (hoy es 22-Oct; el cron solo extrae dias cerrados, el primero, el 23-Oct, a partir del 24-Oct 11:30Z).
El PREREG_E1b original (sha256 en PREREG_E1b_CONFIRMACION_S1.sha256) NO se modifica y su veredicto V0 sigue calculandose tal cual (S1_x2_w2000|D100, G1-G5).
Este addendum anade un segundo veredicto V1 ("ADD"), motivado por el red team (b_perdidas_22oct/red_team/rt1-rt3): en 17-22 Oct el efecto de S1 es
SUSTITUCION (re-puja mas barata, +0,0216/EUR IC90 cierre (+0,018,+0,025)) y no ELIMINACION de rellenos toxicos (+0,0146/EUR, IC cruza 0; eliminar al azar el mismo n
por dia ahorra igual o mas, p(azar>=obs)=0,81); la eliminacion depende del nivel de acierto de B real. V0 podria confirmarse "por volumen" sin mecanismo.
Todo lo que sigue se evalua con los mismos dias forward validos (>= 80 % de los 864 mercados 5m ETH/SOL/XRP con desenlace oficial) y sin reelegir nada.
## Definiciones
base = relleno BASE; ELIMINADO = relleno base sin relleno en la variante; SUSTITUCION = relleno base quitado/movido que se vuelve a rellenar (otro precio u otro print);
dPnL = pnl_variante - pnl_base por mercado; "/EUR" = sobre el coste base total. Bootstrap percentil 5-95 sobre DIAS (o CIERRES), 10.000 remuestras, semilla 20261022.
## A1 -- recuperar la puerta de EV de E1 (G4 original, omitida en E1b)
A1 se cumple si EV ponderado por EUR (suma pnl / suma coste) de la variante > el de base y el IC90 por DIA de la diferencia EV_var - EV_base tiene limite inferior > 0.
## A2 -- eliminacion y sustitucion se juzgan por separado
A2 se cumple si (a) sustitucion dPnL/EUR > 0 con IC90 por DIA inferior > 0, Y (b) [EV(eliminados) <= EV(todos los rellenos base) de la muestra] O [ahorro por eliminar > media del ahorro
de eliminar AL AZAR, entre los rellenos base del mismo dia, el mismo n de rellenos por dia, 5.000 sorteos, con p = P(azar >= observado) < 0,10]. Se informa tambien el IC90 por dia de la eliminacion sola.
## A3 -- EUR anual (informativo, no puerta)
Se reporta solo (i) la sustitucion/EUR, independiente del nivel de acierto, y (ii) la eliminacion RECALIBRADA al acierto de B real: acierto de los eliminados + (acierto real de B
en los dias forward - acierto simulado de los rellenos base), con B real = unidades_b.csv (posiciones B liquidadas); si B real tiene < 100 posiciones en los dias forward se usa
el delta de E1 (+3,3 pp = 21,7 % real frente a 18,4 %). EUR/anual = 365 x coste diario de B (media de unidades_b en dias forward; 42 EUR/dia si < 100 posiciones) x (i + ii). No se anuncia el EV bruto del sim.
## A4 -- D250 primario + variante conservadora con la hora del exchange
La variante PRIMARIA para V1 es S1_x2_w2000|D250 (retirada efectiva a +250 ms desde la recepcion de la senal). V0 sigue en D100.
Variante conservadora X50 (nueva): un candidato de relleno (print) solo se considera evitado si recepcion_senal + 50 ms < hora de exchange (tev) del print, y recepcion_senal mas
2.068 ms >= tev (misma ventana de enfriamiento). Requiere guardar tev: e1b/extraer_e1b.py guarda para cada fila q y t el desfase recepcion-tev (arrays qd, td) ademas de lo de extraer.py,
cuyas salidas son identicas (comprobado). Dias sin td (anteriores al despliegue) no tienen X50 (missing, no 0). Para V1 se exige dPnL(X50) > 0.
Controles de V1 en D250: INV250 (senal a favor, 250 ms) y 8 desplazamientos +-60..240 s a 250 ms; G3 de V1 compara dPnL/EUR de D250 con el INV250 y con el maximo de los 8 SH250.
## A5 -- controles sin Binance (descriptivos con puerta)
C1: retirar la puja 2 s (mismo enfriamiento, D250) cuando el top bid del propio token baja >= 1 tick (0,01) respecto al que habia 2.000 ms antes (ultima fila q <= t-2000 ms).
C2: sin retirar nada, la puja sigue al top bid sin el asentado de 1,5 s pero con la MISMA latencia de reaccion que S1 (asentado de 250 ms en lugar de 1.500 ms; rejilla de 100 ms): dPnL de C2 frente a BASE.
Un control DOMINA a S1 si su dPnL/EUR >= el de S1 (D250) Y su retencion de coste >= la de S1 (comparacion a volumen igualado: quitar volumen mejora cualquier EV negativo por si solo).
A5 se cumple si ningun control domina a S1. Se reportan dPnL/EUR, retencion y EV por EUR de C1, C2 y S1.
## A6 -- apilar sobre R3
Informativo: S1 es APILABLE_SOBRE_R3 solo si en el subconjunto R2-verdadero (bid15 mismo lado - obj <= 0,03 en r-100 ms) dPnL(D250) total >= 0. No condiciona V1 (V1 incluye G5 en R2-falso).
## A7 -- contraste con el ledger de B (descriptivo)
Por dia forward, de experimento_h47_B_ledger.jsonl: repegas hacia abajo/arriba (objetivo < de), cancelaciones (intencion_cancel), errores 429 y rechazos, y rellenos reales con y sin tras_cancel
(precio medio, acierto y EV de unidades_b). Objetivo: ver si una re-puja mas barata ya existe en B y si el ritmo de cancelaciones de S1 cabria sin 429. No es puerta.
## A8 -- familia de reglas ya mirada (multiplicidad)
Reglas "cancelar por senal" ya inspeccionadas en 17-22 Oct antes de este addendum: S1 {-2,-4 bps} x {0,5; 2 s}, S2 {0,5; 2 s}, S3 (2 s), variantes de retardo D0/D100/D250, 8 desplazamientos e inversion,
posthoc sobre S1_x2_w2000 (solape R2, B real), descomposicion y nulo del red team, y desde hoy X50, C1, C2. Solo S1_x2_w2000 es hipotesis de confirmacion; el resto es descriptivo o control y no se re-elige.
## Veredicto V1
CONFIRMADA_ADD: >= 5 dias validos y, sobre la variante D250: G1 (dPnL/EUR > 0, IC90 por DIA y por CIERRE con limite inferior > 0), G2 (>= 60 % de dias con dPnL > 0), G3 (mejor que INV250 y que max SH250),
G5 (R2-falso dPnL > 0) y A1, A2, A5, y dPnL(X50) > 0. REFUTADA_ADD: >= 5 dias y limite superior IC90 por dia (D250) <= 0, o >= 10 dias y estimacion puntual <= 0. Si no ACUMULANDO.
Etiqueta: si V0 = CONFIRMADA pero V1 != CONFIRMADA_ADD, se anuncia "CONFIRMADA SOLO POR VOLUMEN, mecanismo no demostrado" y no se propone B_S1.
Primera lectura: 28-Oct (dias 23-27). Ningun cambio a B antes de N=500 + /code-review + OK de Javi.
