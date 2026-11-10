# PREREG_DB1 — ADDENDUM3: criterio de aceptación sustituto (A1-A3) y lectura de R4. CONGELADO 2026-11-10 ~12:55Z

Autoriza: Javi (10-Nov; R4: «la opción más beneficiosa y limpia»). Redacta: cheap5m-statistical-validator. 0 órdenes.
Hereda de PREREG_DB1 (sha256 1d12afa2f22a1bbb3ccece15b2aec01f437d86b7ef83f2a23479708e1197e998) y PREREG_DB1_ADDENDUM1 (sha256 b083b7a58c9dda13e673675ea2366c50f0cdb74e2ded972c469509298690bd1d).
Nada de este texto mira datos >= 2026-11-10.
DECLARACIÓN DE LO VISTO ANTES DE ELEGIR (no maquillar): el validator vio, ANTES de redactar §A y de elegir el suelo de 12 h de §B3, (1) las cifras por
día de G0 y de los brazos en los días QUEMADOS (`experimentos/5m_barato/db1/aceptacion.log`); (2) que la 1.ª ejecución de la aceptación con el criterio
literal (code_sha 74306488fc9c101e…) dio pass_=false (G0 n=2.499, −106,29 €, EV −0,057; dPnL CXJ150 +120,26) y sus descriptivos de brazos
(DB1_BASE +152,5 € sin rebate; DB2_BASE +87,7); (3) el placebo circular parcial (ADDENDUM2 §5.3). Ninguna regla de este texto usa PnL.

## A. Criterio de aceptación sustituto — POST HOC (declarado)
Motivo: el §1 del prereg fijó los objetivos (G0 n=2.938, −166,9 €, EV −0,076; CXJ150 dPnL +128) con la población de toxicidad_thru1 (solo horas bad
tx_ws). ADDENDUM1 (congelado después) añade la exclusión de HORAS por hueco Binance, que quita mercados enteros (engine.sane: hora de fin−300 o de
fin en _EXTRA_BAD). Con ADDENDUM1 aplicado el objetivo numérico literal es inalcanzable por construcción, no por un fallo del arnés.
Criterio (sustituye a los 6 checks antiguos de eval_db1.aceptacion; todos obligatorios, igualdad EXACTA, sin tolerancia salvo la indicada):
- A1. Para cada día quemado D (2026-10-26..2026-11-04) y var ∈ {G0, CXJ150}: RX_D[var] == RT_D[var] sin los mercados con hora((fin−300) s) o hora(fin)
  en excl_D.horas_excluidas; comparación fila a fila en (k, L, tf, q) redondeado a 1e-6, y Σpnl igual.
- A2. Identidad de unión: RX ∪ RT[mercados excluidos] reproduce el objetivo literal: G0 n=2.938, Σpnl −166,9 (±1), EV −0,076; dPnL CXJ150 +128 (±1).
- A3. Días sin filas en horas excluidas (10-30, 11-03): RX == RT sin filtro (control de que el filtro es lo único que cambia).
Por qué no depende del resultado: igualdad de conjuntos verificable por construcción; la exclusión la fija ADDENDUM1 con ticks de Binance (no con
desenlaces ni PnL); sin grados de libertad (no hay umbral que elegir).
RESULTADO (hecho, 10-Nov): PASS, A1-A3 todos verdaderos, `experimentos/5m_barato/db1/aceptacion.json`, code_sha
f33f2e4dd1483d6f7ae249ae6bdd7baddeda42f4b7d0edf854a6cbf142f2c3d4 (= sha256(sha256(passdb.py)+sha256(eval_db1.py)); recomputado por el validator).
Valores: unión G0 n=2.938, −166,89 €, EV −0,0763, dPnL CXJ150 +128,29; filtrado G0 n=2.499, −106,29 €, EV −0,0571, dPnL CXJ150 +120,26.
Fueron 2 ejecuciones en total: la literal (pass_=false, code_sha 74306488…) y esta (PASS). El campo `criterio` de aceptacion.json dice «(borrador)»: se
refiere a este texto, ahora congelado sin cambios en A1-A3.
Verificación independiente previa (validator, `addendum2/borradores_validator_10nov/verif_rt_filtrado.py`, sha256 b2bcdf025dee9367…): A1 10/10 días EQ.
RX reproducidos dentro de `experimentos/5m_barato/db1/out/` (10 días, checkpoint_db1.json con el mismo code_sha); hash agregado
59a2e8c176d498d7… = sha256 de la salida de `sha256sum out/RX_*.pkl` (recomputado por el validator).
Alcance: valida la FIDELIDAD del arnés para G0 y CXJ150. Los brazos DB1/DB2/DBU constan como validados EN CÓMPUTO (comunicado por el chief el 10-Nov; tests en
`tests/test_db1.py`); eso no es una aceptación contra objetivo externo. Un cambio de passdb.py o eval_db1.py cambia el code_sha
e invalida esta aceptación (eval_db1 lo comprueba).

## B. Lectura de R4 (ADDENDUM1)
Hecho: el código previo implementaba R4 como «quedan >= 20 horas tras quitar las horas bad tx_ws Y las de Binance». El encabezado de R4 es «Día válido
EN BINANCE» y su justificación se calibró con días de 24 horas sanas. El §4 del prereg y el prereg thru1 tratan las horas bad tx_ws como horas que
SALEN, sin mínimo de horas por día. Medido en quemados: las horas perdidas son sobre todo tx_ws (66 de 240), no Binance (26 de 240); 11-03 sale inválido
con 0 horas Binance excluidas. Desde 11-03 el filtro tx_ws quita un patrón PERIÓDICO (horas 3, 7, 11, 15, 19, 23: 5-6 h/día del 11-05 al 11-07) ⇒ con
la lectura literal casi ningún día forward llega a 20 h: veto estructural (11-05..08: ~1/4 válidos; 10 días válidos ~mediados de dic.; checkpoint 20
imposible antes del 31-Dic).
- B1. Día válido en Binance ⇔ horas excluidas por Binance (R2 hueco + R5 evento) <= 3 Y horas con hueco de unión > 300 s <= 2.
  («<4» ya era la regla vinculante; «>=20 de 24» es la misma condición para un día con 24 horas sanas.)
- B2. Las horas bad tx_ws salen como en §4/thru1 (no cuentan contra Binance).
- B3. Suelo (único, POST HOC, elegido por ESTRUCTURA y no por PnL, pero con las cifras por día de G0 en quemados ya vistas, ver la declaración
  inicial): un día cuenta solo si quedan >= 12 horas tras tx_ws y Binance (medio día; protege C5 y el bootstrap por día de días casi vacíos).
  Coste: en quemados 11-02 (5 h) y 11-04 (9 h) no cuentan; forward 11-05..08 (18-21 h con bnreg sin huecos) contarían todos.
  Implementado en passdb.py (MIN_HORAS_DIA = 12, línea 60; test `test_r4_addendum3_cuentan_solo_horas_binance_y_las_txws_no_suman`) DENTRO del code_sha
  f33f2e4d… de §A; el código existía antes de congelar este texto.
- Descriptivo quemados (no decide): literal 4/10 válidos; B1-B2 8/10 (fallan 10-31 con 5 h Binance y 11-01 con 6); B1-B3 6/10.
- G (30 s), unión (10 s), 300 s y R6 no se tocan. Informe diario: horas tx_ws perdidas, horas Binance perdidas y horas que quedan.
Nota: los huecos Binance de los quemados (máx 43-73 s, horas 3/10/22 casi a diario) son de la fuente ANTERIOR a bnreg y coinciden con restart_ram
03:20/10:20/22:20Z (inferencia, no comprobada hueco a hueco). bnreg midió 0 huecos > 30 s el 09/10-Nov.

## C. Lado del print (validez de DB2) — sin cambio de umbral
Concordancia lado_print medida 0,952 (08-Nov) y 0,964 (09-Nov), días pre-forward, comunicada por el chief (no recomputada por el validator): casi en el
umbral. Se MANTIENE el umbral prerregistrado (PREREG_DB1 §2/§4; passdb.py: >= 0,95 y >= 1.000 casados); no se relaja ni se endurece. Un día por debajo
es NO VÁLIDO para DB2 (DB1 no se ve afectado). Se espera que una fracción de días forward caiga fuera: se reporta, no se corrige.
