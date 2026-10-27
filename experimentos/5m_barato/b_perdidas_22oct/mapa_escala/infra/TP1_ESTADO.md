# TP1-INFRA estado (24-Oct 09:55Z) — solo conteos y huecos, sin conclusiones de edge
Auditoría: awk/pandas en streaming sobre los .csv.gz (nice 19, <1 GB RAM, 0 B nuevos en sda: sda 76 %, todo en sdb). Scripts de auditoría en el scratchpad de la sesión (aud.sh, banda.py); extracción con la infra existente `infra/extrae_onchain_ext.py` (idempotente).

## 1. On-chain 5m/15m (volumen /mnt/HC_Volume_106538179/m5_onchain, m15_onchain)
Fuente `datalogs/onchain_fills_D.csv.gz` (filas/día, 24 h UTC sin horas vacías): 19-Oct 3.503.196 | 20 3.919.354 | 21 4.025.519 | 22 3.822.230 | 23 4.615.945 | 24 1.574.157 (parcial, hasta ~09:40Z). 18-Oct ya rotado (no existe). Los 19..22 son symlinks al volumen.
| día | 5m filas (tokens con fill) | 15m filas | horas vacías | estado |
|---|---|---|---|---|
| 17 | 1.765.980 (3475) | — | 0 | ok |
| 18 | 1.910.273 (3467) | — | 0 | ok |
| 19 | 1.974.608 (3474) | — | 0 | ok |
| 20 | 2.188.765 (3469) | 535.448 (1159) | 0 | ok |
| 21 | 2.100.227 (3473) | 565.673 (1167) | 0 | ok |
| 22 | 1.954.490 (3493) | 436.123 (1162) | 0 | COMPLETE en la práctica; manifest PARTIAL (ver abajo) |
| 23 | 2.179.926 (3467) | 533.556 (1161) | 0 | ok |
- El hueco del 22-Oct (m5 de 2 MB) ya estaba arreglado el 23-Oct 11:49Z (116 MB). Re-extraído hoy con --forzar 5m/15m/60m del 22: +6 filas en 5m y +3 en 15m respecto al fichero previo => no faltaba nada.
- Mapa de tokens 22-Oct: 1.728 mercados 5m/día (6 monedas x 288) y 576 de 15m (6 x 96) = rejilla teórica completa (BTC/ETH/SOL/XRP/DOGE/BNB). 23-Oct igual (1.728 / 576).
- Flag PARTIAL residual e irreparable: `maker_ms_2026-10-22_986560.csv.gz` tiene gzip corrupto A MEDIA CORRIENTE (468 tokens recuperados antes del corte). El mapa se completa con la unión de los maker_ms de D-1/D/D+1 y el m15_registro (recuperado el 23-Oct 11:57Z), y la rejilla sale completa, así que el riesgo es bajo, pero el manifest seguirá en PARTIAL mientras ese crudo exista (rota ~27-Oct). No es un hueco de datos de fills.
- Observación (no conclusión): 15m del 22-Oct tiene 436 k filas frente a 534-566 k de los días vecinos (-20 %), con mismos tokens y sin horas vacías; la fuente del día solo cae -5 %. Probablemente volumen real; no verificado.
- Claves de reanudación sin duplicados: (tx, log_index) por fila; ficheros por día atómicos (.tmp -> rename); `extract_D.json` en agentes_datos/mapa_infra/runs; índice de k por crudo en mapa_infra/tokmap (clave nombre+tamaño+mtime).

## 2. 60min / 4h / diario (volumen agentes_datos/mapa_infra/m60|m240|m24h_onchain, retención 60 d)
Cobertura 18..23-Oct: m60 18-23 todos; m240 y m24h 18-23 todos (23 completado hoy; el primer intento dio BLOCKED por HTTP 503 de gamma, reintento OK). Sin horas vacías en ninguno. Filas de mercado/fills (tras quitar taker=exchange y dedup tx+log_index), tokens con fill:
| día | 60m fills (tok) | 4h fills (tok; gamma 108) | diario fills (tok; gamma 48) |
|---|---|---|---|
| 18 | 37.368 (158) | 4.626 (74) | 4.733 (25) |
| 19 | 40.795 (158) | 5.867 (75) | 3.481 (22) |
| 20 | 45.570 (149) | 5.094 (76) | 3.755 (23) |
| 21 | 51.479 (164) | 6.013 (72) | 3.000 (23) |
| 22 | 41.563 (149) | 4.607 (74) | 2.684 (24) |
| 23 | 37.097 (154) | 3.852 (73) | 5.371 (22) |
Banda de precio 0,00-0,10 (precio del token operado, p=usdc/acc en compra, 1-usdc/acc en venta; fills, tokens con fill en banda, USDC):
- 60m: 5.105 / 5.839 / 5.977 / 5.536 / 4.930 / 5.424 fills (≈120-130 tokens/día; 3.600-5.800 USDC/día); <0,05: ≈3.000-3.300, 0,05-0,10: ≈1.800-3.000.
- 4h: 1.083 / 815 / 722 / 798 / 827 / 686 fills (44-50 tokens; 330-670 USDC/día).
- diario: 575 / 977 / 436 / 421 / 715 / 152 fills (9-15 tokens; 360-3.200 USDC/día; 23-Oct muy bajo).
- Referencia 5m: 138-151 k fills/día en banda (2.700 tokens, ≈85-89 k USDC); 15m: 35-36 k (≈920-960 tokens, 22-25 k USDC).
- pc fuera de [0,1] o NaN: 0 en todos los ficheros.
Límites de cobertura (declarar, no ignorar):
1. La universe 60m sale SOLO de los maker_ms/m15_registro: contiene BTC, ETH y SOL (72 mercados/día = 3 x 24). Si existen 60m de XRP/DOGE/BNB en Polymarket no están en el mapa; NO verificado contra gamma (pendiente: comprobar slugs 60m de esas monedas y, si existen, añadir mapa vía gamma como se hace para 4h/diario).
2. 4h/diario por gamma (slugs): 108 y 48 tokens/día cubren los 54 y 24 mercados teóricos; los tokens sin fill no son hueco.
3. Un token sin fills en la banda es "sin evento", no cero de mercado: no se ha medido libro, solo fills de maker (rellenos).
4. Rotación: onchain_fills guarda ~5 días (hoy 19..24). El 19 sale mañana; 5m/15m/60m/4h/diario de 19..23 ya extraídos, así que no se pierde nada si la cron corre cada día.

## 3. Cron TP1 diario propuesto (NO instalado)
Ya existe el orquestador `infra/mapa_infra_diario.sh` -> `diario.py` (D-3..D-1 extracción 5m/15m/60m/4h/diario + TP1 forward 24-Oct..02-Nov + resolvedor + eval; flock/espera load5<8 hasta 45 min/ulimit 3 GB/nice 19 ionice idle/Telegram si falla/ventana prohibida 06:00-09:15Z y 22:15-22:30Z). Línea propuesta:
`15 12 * * * flock -n /tmp/mapa_infra_diario.lock /root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/mapa_escala/infra/mapa_infra_diario.sh >> /root/polymarket-research/logs/mapa_infra_diario_cron.log 2>&1`
- 12:15Z: fuera de 06-09:15Z; no coincide con el 12:12 horario de `vigia_resolution_sniper_precierre` por más que unos minutos y espera a carga baja. El primer día TP1 evaluable es el 24-Oct (corre el 25-Oct 12:15). Reintenta D-3..D-1 cada día, así que un 503 de gamma se autocura antes de que rote el on-chain (~5 d).
- Falta decidir (Javi/chief): instalar la línea. Hasta entonces la extracción de 60m/4h/diario depende de lanzarla a mano: el 24-Oct 12:15 sería la primera pasada del cron real (extraería 21, 22, 23: todo ya existe salvo re-comprobación).

## 4. Qué falta
- Instalar el cron (arriba). Sin cron, el 24-Oct (primer día forward TP1) no se computa.
- Verificar con gamma si hay 60m de XRP/DOGE/BNB (hoy solo BTC/ETH/SOL).
- Rutas para el log de cron: crear el fichero de log no es necesario (>>).
- El crudo corrupto 22_986560 mantendrá PARTIAL en el manifest del 22-Oct hasta que rote (no recuperable).
