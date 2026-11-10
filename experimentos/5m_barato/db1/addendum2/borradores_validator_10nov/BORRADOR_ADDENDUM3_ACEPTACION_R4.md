# ADDENDUM3 a PREREG_DB1 (sha 1d12afa2...) y ADDENDUM1 (sha b083b7a5...) — BORRADOR, NO congelado
Autor: cheap5m-statistical-validator, 2026-11-10 ~10:30Z. Solo lectura. Autorizado por Javi (R4: "la opcion mas beneficiosa y limpia").
Nada de este texto mira datos >= 2026-11-10. Se vieron las cifras por dia de G0 en los QUEMADOS (aceptacion.log); ninguna regla de abajo usa PnL.

## A. Criterio de aceptacion sustituto — POST HOC (declarado)
Motivo: el §1 del prereg fijo los objetivos (G0 n=2.938, −166,9 €, EV −0,076; CXJ150 dPnL +128) con la poblacion de toxicidad_thru1
(solo horas bad tx_ws). ADDENDUM1 (congelado despues) anade la exclusion de HORAS por hueco Binance, que quita mercados enteros
(engine.sane: hora de fin−300 o de fin en _EXTRA_BAD). Con ADDENDUM1 aplicado el objetivo numerico literal es inalcanzable por
construccion, no por un fallo del arnes.
Criterio sustituto (sustituye a los 6 checks de eval_db1.aceptacion; todos obligatorios, igualdad EXACTA, sin tolerancia):
 A1. Para cada dia quemado D (10-26..11-04) y var in {G0, CXJ150}: RX_D[var] == RT_D[var] sin los mercados con
     hora((fin−300) s) o hora(fin) en excl_D.horas_excluidas; comparacion fila a fila en (k, L, tf, q) redondeado a 1e-6, y Σpnl igual.
 A2. Identidad de union: RX ∪ RT[mercados excluidos] reproduce el objetivo literal: G0 n=2.938, Σpnl −166,9 (±1), EV −0,076; dPnL CXJ150 +128 (±1).
 A3. Dias sin filas en horas excluidas (10-30, 11-03): RX == RT sin filtro (control de que el filtro es lo unico que cambia).
Por que no depende del resultado: es una igualdad de conjuntos verificable por construccion; la exclusion la fija ADDENDUM1 con
ticks de Binance (no con desenlaces ni PnL); el criterio no tiene grados de libertad (no hay umbral que elegir).
Verificacion independiente (validator, 10-Nov, nice 19, verif_rt_filtrado.py sha16 b2bcdf025dee9367): A1 10/10 dias EQ en G0 y CXJ150;
totales filtrados G0 n=2.499, −106,29 €; CXJ150 n=2.131; dPnL CXJ150 +120,26 (= aceptacion.json); RT sin filtro 2.938 / −166,89 / +128.
Alcance: valida fidelidad del arnes para G0 y CXJ150. Los brazos DB1/DB2/DBU y placebos NO quedan validados por esta aceptacion
(siguen dependiendo de los tests). eval_db1.aceptacion() se reescribe con A1-A3 y la aceptacion se repite UNA vez con code_sha nuevo.

## B. Lectura de R4 (ADDENDUM1) — aclaracion, no cambio de umbrales
Hecho: el codigo implementa R4 como "quedan >= 20 horas tras quitar las horas bad tx_ws Y las de Binance". El encabezado de R4 es
"Dia valido EN BINANCE" y su justificacion se calibro con dias de 24 horas sanas. El §4 del prereg y el prereg thru1 tratan las horas
bad tx_ws como horas que SALEN, sin minimo de horas por dia. Medido en quemados: las horas perdidas son sobre todo tx_ws (66 de 240),
no Binance (26 de 240); 11-03 sale invalido con 0 horas Binance excluidas. Desde 11-03 el filtro tx_ws quita un patron PERIODICO
(horas 3,7,11,15,19,23: 5-6 h/dia del 11-05 al 11-07) => con la lectura literal casi ningun dia forward llega a 20 h: veto estructural
(dias 11-05..08 por lectura literal: ~1/4 validos; 10 dias validos ~mediados de dic.; checkpoint 20 imposible antes del 31-Dic).
Lectura adoptada:
 B1. Dia valido en Binance <=> horas excluidas por Binance (R2 hueco + R5 evento) <= 3 Y horas con hueco de union > 300 s <= 2.
     (El "<4" ya era la regla vinculante; "≥20 de 24" es la misma condicion para un dia con 24 horas sanas.)
 B2. Las horas bad tx_ws salen como en §4/thru1 (no cuentan contra Binance).
 B3. Ajuste (unico, POST HOC, elegido por estructura y no por PnL): un dia cuenta solo si quedan >= 12 horas tras tx_ws y Binance
     (medio dia; protege C5 y el bootstrap por dia de dias casi vacios). Coste: en quemados 11-02 (5 h) y 11-04 (9 h) no cuentan;
     forward 11-05..08 (18-21 h con bnreg sin huecos) contarian todos.
 Descriptivo quemados (no decide): literal 4/10 validos; B1-B2 8/10 (fallan 10-31 con 5 h Binance y 11-01 con 6); B1-B3 6/10.
 G (30 s), union (10 s), 300 s y R6 no se tocan. Informe diario: horas tx_ws perdidas, horas Binance perdidas y horas que quedan.
Nota: los huecos Binance de los quemados (max 43-73 s, horas 3/10/22 casi a diario) son de la fuente ANTERIOR a bnreg y coinciden con
restart_ram 03:20/10:20/22:20Z (inferencia, no comprobada hueco a hueco). bnreg midio 0 huecos > 30 s el 09/10-Nov.
