# Mapa de artefactos — misión 5m barato (verificado 16-Oct-2026 08:05Z)

Todas las rutas existen (comprobado con `ls` el 16-Oct). Raíz del repo: `/root/polymarket-research` (main = PRODUCCIÓN).
Datalogs pesados: `/root/polymarket-research-datalogs/` (abreviado `DL/`). Archivo de 60 días en el volumen
`/mnt/HC_Volume_106538179` (`archivo_volumen.VOL`). `crontab -l` es la fuente de verdad de horarios (UTC).
**Antes de buscar nada, mirar aquí.** Si algo no cuadra con el disco, gana el disco: anotarlo en DECISION_LOG.

## 0. Qué es "5m barato" (definición única)
Par anidado de cada cierre C: mercado 15m que cierra en C y mercado 5m que cierra en C (último tramo del 15m).
Lado implicado s por referencias TWAP60 oficiales: ref15 = twap60(C−900), ref5 = twap60(C−300); si ref15 > ref5 ⇒ s = Up
(Up en 15m implica Up en 5m), si no s = Down; |gap| ≥ 1 bp. **bid15(s) es una cota inferior de P(s en 5m)**: la pata
5m está "barata" cuando ask5(s) < bid15(s) − comisión. "Barato" NO significa "precio < 0,10": las líneas de wallets que
compran a precio bajo son otra cosa (sección 5) y no se mezclan.
**Universo**: v4/V2/V3/V5 son MULTIMONEDA (BTC, ETH, SOL, XRP, DOGE, BNB) tal como se congelaron; V6/V7/FV v4 son solo BTC.
Regla de Javi 14-Oct: diseño, parámetros y decisiones en BTC; datos de todas las monedas se siguen recogiendo; una ventaja
EVIDENTE en otra moneda se explora con su propio gate, nunca eligiendo parámetros sobre el mismo dato.

## 1. Subestrategias en forward (congeladas, solo observación)
| Pieza | Código (NO editar: hashean el fichero) | Cron UTC | Salida |
|---|---|---|---|
| v4 (= v1 corregida) | `vigia_5m_barato_forward.py` (CONFIG v4, hash_config 77a75859ae5cf22e; gates G1-G10 en el informe) | 04:35 (`ulimit -v 4500000`) | `DL/vigia_5m_barato/` eventos_D.csv, controles_D.csv, calidad_D.csv, manifiesto.json, informe.json/txt |
| v4 desde archivo | `vigia_5m_barato_desde_archivo.py --dia D` + `extraer_registro_5m_barato.py` (03:50) | — | reprocesar días del archivo 60 d |
| V2 todas las señales | `vigia_5m_barato_v2_forward.py` | 05:05 | `DL/vigia_5m_barato/v2_informe.json` |
| V3 filtro Binance 5 s | `vigia_5m_barato_v3_forward.py` | 05:10 | `DL/vigia_5m_barato/v3_informe.json` |
| V5 ORIGEN15M | `vigia_5m_barato_v5_forward.py` | 05:50 (dentro de `run_m5barato_forward_diario.sh`) | log diario |
| V6 FOK_VUELO_BTC | `vigia_5m_barato_v6_forward.py` (regla `analisis_5m_barato_fok_vuelo.py`) | 05:50 | `DL/m5barato_mision/fok_vuelo_D_p250.csv.gz`, `fok_vuelo_informe_p250.txt` |
| V7 DISPARO15M_BTC | `vigia_5m_barato_v7_forward.py` (regla `analisis_5m_barato_disparo15m.py`, sha c42f2c1f14ea) | 05:50 | `DL/m5barato_mision/disparo15m_D.csv.gz` (existen 14 y 15-Oct), `v7_informe.json`, `disparo15m_informe.txt` |
| FV v4 | `analisis_5m_barato_fv_modelo_v4.py` (sha 0a6d0e4488b68102; DESC 05-11 / valida 12-13 / OOS desde 14-Oct) | 05:50 | `DL/m5barato_mision/fv4_dataset_D.csv.gz`, `fv4_informe.txt` |
| H5M-BARATO-MAKER-v1 | `vigia_5m_barato_maker_forward.py` | 05:20 | informe diario (CONFIRMADA 14-Oct on-chain; NO capturable con órdenes propias, ver cementerio) |
Orquestador diario: `run_m5barato_forward_diario.sh` (05:50) → log `logs/m5barato_forward_diario.log` (V5, V6, V7, FV v4,
quién gana del día, pastel de la caja por moneda). Telegram bot=cripto.

## 2. Trabajos interrumpidos (P0)
- **Cosechar al abrir A/B**: `analisis_5m_cosechar_apertura.py` (commit del fix 340755d55f: cotizar solo con la ventana abierta,
  defensa por mercado). Informe esperado `DL/m5_cosechar_apertura/informe.txt` (NO existe); cachés `mercados_D.csv.gz` (la
  carpeta está vacía de cachés: se borraron al corregir el 15-Oct). Cola original: scratchpad de la sesión e58a093d
  `cola_cosechar_invisible.sh` → `cola.log` (vacío), `cosechar.log` (solo "desenlace oficial 97/97 (05-Oct), 291/291 (06-Oct)").
  Comando documentado: `cd /root/polymarket-research && nice -n 19 ionice -c3 python3 analisis_5m_cosechar_apertura.py`
  (reaprovecha cachés si existen). Leer su cabecera/argparse antes de lanzar.
- **Fase 2 invisible**: `analisis_5m_wallets_baratas_invisible.py` → informe `DL/m5barato_mision/invisible_informe.txt` (NO existe).
  Depende de `DL/m5barato_mision/baratas_wallets.csv` y `baratas_unidades_D.csv.gz` (05-14 Oct, existen).

## 3. Wallets y on-chain
- `analisis_5m_wallets_baratas.py` → `baratas_informe.txt`, `baratas_wallets.csv` (140/309 persistentes; placebo −0,003).
- `analisis_mo_money_pares_5m.py` (@mo-money 0x32ed2e54…; +10.406 $ / 10 d = pares −15.850 + dirección +26.256; 1ª pata maker
  ≤0,30 acierta 22,6 % vs precio 17,1 %, +5,5 pp en SEL y TEST).
- On-chain: `fetch_polymarket_fills_onchain.py` (cron */5, `DL/onchain_fills_D.csv.gz`, 4 d) vía `polygon_rpc.py`; archivo
  `VOL/m5_onchain/`; extractor `extraer_onchain_15m.py --marco 5m` (04:10). Maker y tomador explícitos.
- Makers H5M: `analisis_h5m_cola_simulada.py`, `analisis_h5m_quien_gana_banda.py`, `analisis_h5m_ganadoras_persistencia.py`
  (salidas `DL/h5m_cola_sim/`).

## 4. Datos de mercado (registro ms)
- `libro_estado_ws.py` (hijo de `observadores_fase0.py`; NO reiniciar observadores: pierde histórico) escribe
  `DL/maker_ms_YYYY-MM-DD_<pid>.csv.gz` (4 d): filas h (top 100 ms), q (top en cada cambio de precio, con hora del exchange
  y de RECEPCIÓN), t (operaciones), l/L (niveles ask; L = libro ask completo pares BTC desde 14-Oct 12:26Z), x (aggTrade
  Binance: c[7] = recepción), b (bookTicker), k (mapa token→moneda/marco/mercado/cierre/lado).
- Archivo 60 d: `VOL/m5_registro/m5_registro_D.csv.gz` y `VOL/m15_registro/` (extractores 03:45/04:00).
- Referencias TWAP60 oficiales: `data/prices/polybolt_D.csv[.gz]` canal `twap60` con `source=chainlink` (filtrar SIEMPRE `source`).
- Desenlace oficial: `analisis_maker_cancelacion_binance.desenlaces()` (gamma con `closed=true`).
- Comisión única: `comision_cripto.py` (`pnl_por_euro`).

## 5. Ejecutor y F2
- `ejecutor_rapido.py`: Libro (WS propio), Armero (en proceso), **ArmeroProceso** (firmador hijo, 05a1082755), Riesgo, Enviador
  (`inline=True` desde 712f497df1). **Lo usa también `medir_camino_caliente.py`, que envía órdenes REALES** → todo cambio con
  `/code-review` medium + tests (`tests/test_ejecutor_rapido_*.py`, `tests/test_medir_camino_caliente.py`).
- Diseño, presupuesto de latencia y **criterios F2→F3 CONGELADOS**: `informes/ejecutor_baja_latencia_diseno_15oct.md`.
- F2 en marcha (DRY-RUN fijo): `f2_5m_barato_dryrun.py` (2 procesos: BTC `--cpu 3 --envio-inline` con firma; altcoins
  `--sin-firma`), salida `DL/f2_5m_barato/f2_D.jsonl` + `f2_ledger_*.jsonl`. Conciliador: `python3 analisis_f2_5m_barato.py --dia D`
  (tras los crons 04:35 y 05:50 del día siguiente). **Gestión de estos procesos: SOLO la sesión principal** (cargan la wallet dedicada).

## 6. Informes y memoria
- Estado completo: `informes/m5barato_estado_16oct.md`. Tablero de subestrategias y cementerio: memoria
  `project_mision_5m_barato_validar_alpha_14oct`, `project_f2_ejecutor_5m_barato_16oct`.
- Capacidad V7: `analisis_5m_barato_v7_capacidad_n3.py` (profundidad P50 35 € niveles 1-3; total estimada P50 120 € / P75 295 €;
  stake 100 € techo ~81 k€/año, sin top3 ~28 k€; stake 250 € techo ~137 k€, sin top3 ~37,5 k€ — descubrimiento, n=18).
- Pastel de la caja: `analisis_5m_barato_pastel_caja.py` (persistentes de caja ~420 $/día ≈ 150 k$/año como techo poblacional).

## 7. Capital y límites reales (restricción dura para risk-economics)
- Bankroll on-chain cripto (wallet PRINCIPAL) 16-Oct: **34,59 $**; 17-Oct 39,66 $ libres + 4,51 $ posiciones; wallet DEDICADA 19,59 pUSD (tope 5 €) (`data/shadow/estado_actual.md`). `config_live.json::riesgo.max_stake_eur` = 2,0.
- Calendario `project_calendario_200k_11ago2027`: **sin recargas planificadas**. Wallet dedicada de experimentos: tope de pruebas
  5 € (Javi 15-Oct). Cualquier escenario con stake > 2 € o capital > bankroll es CONDICIONAL a una decisión de Javi y se etiqueta así.
- VPS: solo Helsinki (VPS cerca del CLOB DESCARTADO por Javi 15-Oct).
