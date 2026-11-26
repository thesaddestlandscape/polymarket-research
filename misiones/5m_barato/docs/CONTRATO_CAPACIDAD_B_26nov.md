# CONTRATO DE MEDICION: CAPACIDAD de B y subvariante (H03) — 26-Nov-2026
measurement_id: CAP_B_26nov · version contrato: v1 · autor: polymarket-data-integrity-authority · estado global: **AMBER (contrato; nada ejecutado)**
Estado de partida: no se ha medido nada. Los veredictos por metrica son los del CONTRATO (GREEN = ejecutable tal cual; AMBER = ejecutable con la correccion indicada; RED = no medir).

## 1. Pregunta, decision, estimando
- Pregunta: ¿cuantos rellenos/dia y € colocados/dia puede absorber B (y subvariante) al nivel real de su politica, por tamano 5/10/20/50 acc, y con que EV/€ condicionado al tamano?
- Decision que cambia: dimensionar tamano y recarga (techo B real vs hueco) y si merece escalar al objetivo 200 k€/ano. Sustituye al techo «B ≲ 11 % del hueco».
- Estimando (INCONDICIONAL, regla de poblacion completa): por (moneda, clase lo, tamano s): `E[pnl]/dia` sobre TODAS las ventanas-mercado elegibles, con no relleno = 0. Descomposicion obligatoria P(relleno | s) × EV/€ | relleno, y comparacion explicita condicional vs incondicional. Reportar tambien €/dia colocado (coste inmovilizado) aunque no se rellene.
- Unidad: 1.er relleno por (mercado, lado) de la politica real; € ponderado (Σpnl/Σcoste), nunca media de cocientes. IC90 por DIAS (n efectivo = dias; cierres con ≥2 monedas = una apuesta). Sin los 2 mejores dias.

## 2. Instrumento y fuentes (por variable)
| Variable | Fuente | Reloj | Nota |
|---|---|---|---|
| Libro 5m al nivel de B (profundidad/cola delante) | libro5_ms / registro ms (`maker_ms_*`, filas q/h/t/x) del dia | RECEPCION (rx), ex solo para medir W | ordenar por rx; descartar libros cruzados/bloqueados (ver §5) |
| Casados del libro | libro5_tx (print ≈20 ms tras casado) y on-chain por hash (`onchain_fills_D`, maker/tomador explicitos) | bloque ≈2,4 s tras casado: NO para decidir | firma ≠ llegada; excluir txs propias |
| Binance | m5_registro filas `x`, columna recepcion (c[7]) | recepcion | no c[6] |
| Suelo/clase | suelo_p5 `manifest_suelo_DIA.json` COMPLETE + npz; clase por VENTANA (lo/hi/indet) con `--version-clase` del ejecutor | por ventana | no por fecha |
| Resolucion | TWAP60 oficial (passT_v4) | — | desenlace oficial, cobertura ≈100 % declarada |
| Latencia | paquete_l `ensayo_real_B2/B3/B5` (13-Nov): L1=34 (47 robusto), L3a=57, L3b=p50 P1b COMPLETE o 59; por clase de suelo lo/hi | local | ninguna otra fuente |
- Motor/sello: passT_v4 (`eng_v5`), SIM-L (`siml.py`) con politica REAL del ejecutor B-K: F5/F3, V5/V6, guarda intra (`guarda_intra`, commit 840e84f193e, solo tras firma de su prereg), Calma. Cada brazo con commit, sha de cadena (`manifest_codigo`) y arbol limpio.
- Dias: todos los COMPLETE disponibles; cobertura del join ≥0,90 por dia (A3) y por hora (≥100 filas q mapeadas/hora/moneda ETH,SOL,XRP). BTC=DATA_BLOCKED_BTC, HYPE sin datos: fuera, declarado.

## 3. Metricas, veredicto de contrato, ejecutor, RAM
| # | Metrica | Veredicto | Ejecuta | RAM est. | Condicion |
|---|---|---|---|---|---|
| M1 | Profundidad/cola alcanzable al nivel de B por s=5/10/20/50, por moneda y clase lo (cola delante, tamano en el nivel, reposicion) | GREEN | market-data-engineer | ≤3 GB por dia (ulimit -v 3 GB, cron_pesado, fuera de 06-09Z) | solo estado L2 rx-ordenado; sin ask de senal |
| M2 | Rellenos/dia y €/dia colocado por moneda × clase lo × s | AMBER | execution-engineer (SIM-L) | ~2,6 GB por dia (`traza_dia`) | solo con politica real completa; hasta firma de guarda intra y de SIML, brazo etiquetado «sin guarda intra» |
| M3 | EV/€ ponderado condicionado a s (AS crece con s) + P(relleno|s) + EV incondicional | AMBER | execution-engineer | idem M2 | el relleno de s grande consume niveles: modelar consumo de profundidad y cola, no el best ask; sin cola observada → `not_identifiable`, no rellenar |
| M4 | Rellenos propios reales (B real, 5 acc) como ancla de validacion de M2 | GREEN | market-data-engineer | <1 GB | cruzar con `bk_q_live_*` y on-chain por hash; solo ancla, no estimador |
| M5 | Techo agregado (suma por moneda, % del nicho) | RED hasta M1-M3 | — | — | no publicar un techo si M3 no tiene IC90 por dias >0 |
- Escalado de s>5: sin datos reales de relleno a s>5, M3 para 10/20/50 es CONTRAFACTUAL y se etiqueta `estimado_contrafactual` con su metodo; nunca como medido.
- Coste/parada: 1 dia piloto (M1) antes de nada; parar si cobertura <0,90, ≥2 dias sin COMPLETE, o RAM libre <3 GB. Un job a la vez, `cron_pesado.sh`, nice 19/ionice.

## 4. Cifras RETIRADAS (no citar como capacidad)
- «Techo B ≲ 11 % del hueco»; nicho 33,9 k€/dia; R3 136 €/dia a 5 acc y 130 rellenos/dia; B real 55 €/dia (0,16 %): sello viejo 24-Oct/10-Nov, no passT_v4/B-K. Se conservan solo como historia no citable.
- Todo EV R3/R2/skip025/V9/V3 (K04, sello viejo) y cualquier latencia de Sonda 30-Oct..05-Nov.

## 5. Calidad e integridad exigida
- Libro cruzado (bid>ask) o bloqueado (bid=ask): descartar el evento/estado y CONTARLO por dia y moneda. Un bid de pata cruzada no es real.
- Censura/supervivencia: denominador = ventanas elegibles, no ventanas con relleno; mercados sin trades = 0 rellenos, no missing.
- Prohibido: OHLC/mid/ultimo trade como ask; prints como unidad; «flujo tomador» del firehose; ask de senal por ask de decision.
- Reportar siempre: n mercados, n dias, n efectivo (cierres), cobertura por dia, EV ponderado y sin los 2 mejores dias, por clase lo/hi (hi solo sensibilidad).
- Gate: GREEN del contrato no sustituye validador estadistico ni red-team. Salida firmada: `Measurement Audit` con hash de datos/codigo.
