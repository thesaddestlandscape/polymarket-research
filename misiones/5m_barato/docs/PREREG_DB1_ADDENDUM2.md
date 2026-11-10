# PREREG_DB1 — ADDENDUM2 (§6, RMR): definición operativa de «ráfaga». CONGELADO 2026-11-10 ~12:55Z

Autoriza: Javi (10-Nov). Redacta: cheap5m-statistical-validator. Hereda de PREREG_DB1 (sha256 1d12afa2f22a1bbb3ccece15b2aec01f437d86b7ef83f2a23479708e1197e998)
y PREREG_DB1_ADDENDUM1 (sha256 b083b7a58c9dda13e673675ea2366c50f0cdb74e2ded972c469509298690bd1d). 0 órdenes. No mira datos >= 2026-11-10.
Texto base: `experimentos/5m_barato/db1/ADDENDUM2_PROPUESTO.md` (alpha-miner, 10-Nov 08:45Z; sha256 b1453e745904350bb1f373d78ccb53d06cd46738eb7ec9e5045bbf202c9d0331),
con criterio previo `addendum2/CRITERIO_PREVIO.txt` (sha256 18310f5f61f380a04f33bc2ee4eebf99d6ddd44d1c47530d4bca9177cdd1ed48, 08:26:05Z).
Sus §2, §3, §4, §6, §7, §8 y §9 se adoptan TAL CUAL. Este texto sustituye su §1 y §5. Lo POST HOC va marcado.

## 1. Regla
R0 es la definición oficial de ráfaga en RMR. Estatus: DESCRIPTIVA (contable). Poder discriminante general: INSUFFICIENT_EVIDENCE.
- Definición normativa = el CÓDIGO, no las réplicas: `experimentos/5m_barato/db1/passdb.py` (sha256 5e30771c0ec208cdec5440c3fcaa41f67e9299f17d408fedcb7e0e7faec3923d,
  dentro de code_sha f33f2e4dd1483d6f7ae249ae6bdd7baddeda42f4b7d0edf854a6cbf142f2c3d4 = sha256(sha(passdb.py)+sha(eval_db1.py))): BAND_MAX = 0,20 (línea 21);
  bids side 0 con pr <= BAND_MAX + 0,0049; ráfaga = >= 2 tomadores distintos, excluidos CHAIN_CONTRACTS (línea 20), por (bloque, mercado) (línea 226).
  Las cifras de `addendum2/add2_*` son una RÉPLICA APROXIMADA (suelo de extracción 0,03: no cuenta bids 0,01-0,02 → marca como mucho menos ráfagas).
- Coherencia (POST HOC, efecto nulo en DB1 por construcción): `passdb.check_band` exige, con fallo ruidoso, max(LEVELS de TODAS las variantes,
  incl. @CROSS/@STRICT/@OPT/@THIN) <= BAND_MAX y lo comprueba sobre el L de RX; test propio `tests/test_db1.py::test_band_max_levels_todas_las_variantes`.
  Si RMR se calcula sobre rellenos REALES de B o brazos con niveles > 0,20 se usa R2 (bids <= 0,40) y se reporta aparte.
- La etiqueta usa el bloque ENTERO (~2 s; incluye tomadores posteriores a nuestro relleno): contable y NUNCA ex ante. Ninguna regla de decisión
  (brazo, cancelación, filtro) puede usarla; el uso ex ante exige reloj propio (PREREG_H_DB3).
- Apoyo en S_sim (−0,307 vs −0,062; n=3.591): IN-SAMPLE respecto de los quemados de DB1 (mismos días); descriptivo, no es evidencia de brazos.

## 5.1 Placebo temporal — CORREGIDO, POST HOC (sustituye «No se corrige a posteriori» del §5.1 propuesto)
Defecto: comparar Δ de la regla con Δ de P-temp con coberturas 10x distintas (2-6 % vs ~35-50 %) no es una comparación válida.
Criterio (b) corregido, para todo informe RMR futuro:
- P-temp con la MISMA cobertura en € que la regla (±10 %), ensanchando la ventana desplazada hasta igualarla; o comparar V_adj = cobertura × Δ.
- P-temp PASADO (−15 bloques) y FUTURO (+15) por separado; solo el pasado informa de algo accionable (hoy `add2_dia.py` los mezcla).
- IC90 por día (bootstrap 2.000, semilla 20261110).
Efecto en DB1: ninguno (R0 es el statu quo y es descriptiva). Si con este criterio una alternativa superase a R0, NO cambia la etiqueta de DB1:
abre un prerregistro nuevo.

## 5.2 Episodios → H-DB3 (aclaración)
«−0,154 vs +0,024 (14/20 días)» es descriptivo, en S_pop (no en exposición G0), sin IC, condicionado a la 2.ª mitad (post hoc) y sin artefacto
reproducible en `addendum2/out` (no se encontró): no es base cuantitativa. H-DB3 va en `PREREG_H_DB3.md`.

## 5.3 Evidencia descriptiva QUEMADA del placebo circular de los brazos (no decide nada; consta para no ocultarla)
Fuente: driver del placebo circular en curso (`experimentos/5m_barato/db1/placebo/sN/`), 44 de 99 semillas al congelar; cifras comunicadas por el
chief el 10-Nov y NO recomputadas por el validator (no hay fichero agregado). Días quemados 26-Oct..04-Nov, BASE, sin rebate, € de dPnL frente a G0:
- DB1: nulo media +78,3, sd 37,5; real +152,6 (= `aceptacion.log`, 1.ª ejecución: DB1_BASE dpnl_sin_rebate +152,55, n_arm 1.597 / n_g0 2.499).
- DB2: nulo media +79,5, sd 35,3; real +87,7 (≈ nulo). DB2 NO supera su placebo en quemados.
- Cobertura NO equivalente: el nulo de DB1 tiene un n del 132 % del n real; el placebo cancela ~15 % frente a ~36 % del real. Mismo defecto que
  §5.1: la comparación DB1-vs-nulo no es válida tal cual y no se interpreta como señal. Estas cifras se vieron ANTES de congelar este texto,
  ADDENDUM3 y H-DB3; no se usan para elegir ninguna regla ni umbral de esos documentos.
- El placebo (C6) de DB1/DB2 en forward sigue siendo el de PREREG_DB1 tal cual; este apartado no lo modifica.

## 6. BTC: DATA_BLOCKED; R0 satura (95,7 %). Definición propia solo en el contrato BTC-DB1-DESC.
