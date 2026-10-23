# L1 - Etiquetado pasivo rpre/r900 en B (23-Oct-2026)
Estado: **INSTALADO, recogiendo; sin conclusión.** Solo lectura de B (no se toca `experimento_h47.py`, h47B, h47sup ni ejecutores; no se importa ningún módulo del repo; sin claves, sin órdenes). Prereg: `PREREG_L1.md` (sha en `PREREG_L1.sha256`; enmendado una vez ANTES de calcular ningún EV: retorno exactamente 0 = `neutra`, no `missing`). Hashes de código: `HASHES.txt`.

## Qué hace y dónde escribe
- `scripts/etiquetar_pasivo.py etiquetar|resolver|cobertura` (un único .py; lock fcntl; escritura atómica con validación de lectura; checkpoint corrupto se aparta como `.corruptN` y se reconstruye; ledger con última línea a medias tolerada).
- Entradas (solo lectura): `/root/polymarket-research-datalogs/experimento_h47_B_ledger.jsonl`, `experimentos/5m_barato/contabilidad_wallet_dedicada/posiciones.csv` (solo `tanda_B`), `binance_bookticker_D.csv` (mid, hora de RECEPCIÓN; la fuente en vivo que ya graba `fetch_binance_bookticker.py`; ticks sólo cuando cambia el mid, se usa el último con recepción <= instante; edad >300 s = missing).
- Salida: `/root/polymarket-research-datalogs/etiquetado_pasivo_B/etiquetado_B_YYYY-MM-DD.csv.gz` (fuera de git; retención 30 d dentro del propio script), `run_manifest_{etiquetar,resolver}.json`, `cron.log`. Clave única `(unidad,id)`; día = UTC de `t_dec` (orden) o del primer relleno (posición). Dos unidades: `orden` (cada `puja_post`, también las NO rellenadas; sirve de control) y `posicion` (mercado,outcome de B; unidad del gate).
- Columnas: unidad,id,dia,mercado,token,coin,lado,outcome,precio,acc,acc_llena,coste,t0,t0_fuente,fin_s,T_s,rpre_bps,r900_bps,abs_rpre,clase_rpre,clase_r900,h_w1,bn_edad_max_s,etiquetado_utc,resuelto,gana_lado,pnl,pnl_fuente,resuelto_utc. `h_w1`=1 si a_favor y |rpre|>=7,7 bps. Orientado al lado comprado (YES/Up +, NO/Down -).
- Resolvedor (cron): gamma `closed=true` por slug, mapeo outcomes ["Up","Down"]; en posiciones toma `pnl`/`coste` de `posiciones.csv` (si aún no liquidada: estimado `acc*gana-coste`, marcado `estimado_gamma`) y cuenta discrepancias de desenlace gamma vs posiciones.csv.
- Cron (añadido; copia previa del crontab en el scratchpad de la sesión): `*/15 0-5,9-23` etiquetar y `7,37 0-5,9-23` resolver, `flock`, `nice 19 ionice -c3`, `ulimit -v 3 GB`, Telegram si falla (`scripts/l1_cron.sh`). Nunca 06-09Z. No es screen: no hay nada que registrar en `verify_deploy`/watchdog; los ficheros están en un subdirectorio de datalogs, por lo que `vigia_loggers_silenciosos` (globs de primer nivel) NO lo vigila y no dará falsos avisos mientras B esté parado.
- Evaluador del gate: `scripts/evaluar_gate.py` (hashea el prereg; imprime siempre días forward y n por clase).

## Verificación (esta sesión)
- `py_compile` OK. Fixture en scratchpad: 1.ª corrida 3.016 filas, 2.ª corrida 0 nuevas (idempotente, 0 duplicados); `truncate` del gz de un día -> se aparta como `.corrupt…`, se reconstruyen las mismas 1.193 filas y el resolvedor las deja 1.193/1.193 resueltas.
- Corrida real y backfill (ledger B empieza el 20-Oct 11:39Z: **no existe B antes del 20-Oct**, así que el «17-Oct» no tiene filas B): 20-Oct 405 órdenes/37 posiciones, 21-Oct 1.121/72, 22-Oct 1.746/77 = 3.272 órdenes y 186 posiciones, todo resuelto (3.458/3.458), 0 discrepancias gamma vs posiciones.csv, 0 duplicados, rpre missing 0 (rpre neutras: 21 el 21-Oct, 0 los demás días), r900 neutra 71 de 3.458 (mid sin cambio en 15 min; 63 órdenes + 8 posiciones).
- Contraste con W1 (aggTrade del registro ms) en las mismas 175 posiciones: rpre corr 0,9996 (|dif| p50 0,001, p90 0,95, máx 3,0 bps; mismo signo 99,4 %), r900 corr 0,996 (n=166, máx 15 bps; mismo signo 98,2 %); `h_w1` coincide en 99,4 % (1 desacuerdo de 175). La fuente bookTicker sirve y no cambia la clase salvo casos de borde.

## Lectura DESCRIPTIVA del backfill (20-22 Oct, ya vista en W1, NO cuenta para el gate)
184 posiciones con grupo definido (3 días, 101 cierres): h_w1=1 n=60 coste 66,2 € EV ponderado -0,368; h_w1=0 n=124 coste 136,7 € EV +0,144; Delta -0,513, IC90 por cierre (-0,99,-0,02); PnL h1 -24,4 / h0 +19,7 / total -4,7; PnL retenido +19,7 vs placebo medio +6,2 (p=0,10); sin los 2 mejores días Delta -0,219. Misma dirección que W1, no decide: 3 días, periodo elegido por W1, placebo p>0,05.

## Estado del gate (`python3 -I scripts/evaluar_gate.py`)
Días forward (>= 23-Oct) con posiciones resueltas: **0/10**; n(h_w1=1) 0/40 -> **NO EVALUABLE**. **Dependencia dura: B está parado** (13,26 $); el reloj solo corre con días en que B opera. Si B no reanuda, el gate no se alcanza; la alternativa sería etiquetar también la población on-chain forward (R1/E1b ya la extraen a diario) con el mismo código: no hecho, requiere decisión.

## Límites
Binance = bookTicker (no TWAP Chainlink de resolución). Posiciones sin `t_det` usan `primer_fill_chain-5 s` (campo `t0_fuente`). `r900` de órdenes se mide en `t_dec`, de posiciones en `t_det-4 s`; `rpre` no depende de t0. IC con pocos cierres y días correlacionados por moneda (se agrupa por cierre). `pnl` sin rebate maker (como `posiciones.csv`). 11 posiciones de B de `posiciones.csv` no estaban en `unidades_b.csv` de W1 (186 vs 175).

## Reproducir / operar
`python3 -I scripts/etiquetar_pasivo.py etiquetar --desde 2026-10-17` ; `... resolver` ; `... cobertura` ; `python3 -I scripts/evaluar_gate.py`. Prueba con otra carpeta: `L1_OUT=/ruta`.
