# MISIÓN 5M v1 — plan (09-Oct, Javi: "iniciar la investigación de 5m de la misma forma que 15m; ya sabes cómo y dónde mirar")

Método heredado de 15m v4 (`project_mision_15m_v4_08oct`): lo que decidió la misión fue mirar QUIÉN gana on-chain y con
qué ESTRUCTURA, no buscar señales. Reglas que se mantienen: congelar ANTES de ver PnL, veredicto en días NO usados,
contar variantes, fidelidad del simulador contra los bots ANTES del OOS, desenlace oficial con cobertura ≈100 %,
unidad = mercado (no relleno), desagregar por moneda × fase × banda de precio.

Atajos (lo ya sabido, no se repite): calibración del mercado a T>60 s (15m: calibrado ±1-2c); tomador tras Binance
cerrado en 5m (CLAUDE.md, forward 05-Oct); Φ(z) sobreconfiado; certeza terminal como TOMADOR refutada en 15m;
la ventaja de los cosechadores de pares es la POSICIÓN EN COLA (no replicable al final de la cola).

| Paso | Qué | Estado |
|---|---|---|
| 0 | Archivo 60 d: `m5_registro` (q/t 5m + x + k) y `m5_onchain` en el volumen; L2 multinivel 5m ya en `registro_5m_barato` (filas l) | ✅ 05-Oct; 06-08 relleno `at` 09:30Z; crons 04:00/04:10 |
| 1 | Quién gana on-chain 06-08 (`analisis_5m_v1_quien_gana.py`): rol, wallet, persistencia, perfil, estructura de pares del top, fase × banda | ⏳ `at` 10:30Z con guardián de RAM → `informes/m5v1_quien_gana_09oct.txt` |
| 2 | Política de los bots de pares en 5m (adaptar `analisis_15m_v4_politica_bots_pares.py`): anclan o no la 2ª pata, simetría, inventario, mismo bloque | pendiente de 1 |
| 3 | Certeza terminal 5m (paso 3b, 12-Oct, `analisis_5m_v1_certeza_terminal.py`) | ✅ NO PERSISTE: 207 'persistentes' +0,014/acc (06-08) → −0,004 (09-11, mismas wallets); superficie z×precio ±1c/acc sin celdas estables salvo z 3-4 p 0,97-0,99 (+0,008 → +0,005/acc, ~0,5 %); fases cambian de signo. Nuestra banda PRECIERRE 5m (0,25-0,65) queda fuera de este tramo |
| 4 | Simulador de cosechador de pares 5m con modelo de cola; fidelidad contra el mejor bot de pares 5m ANTES de cualquier OOS | pendiente de 2 |
| 5 | Híbridos en 5m (0xb970fb5c y cía.: `datalogs/m15v4_hibridos_onchain`, ya tiene TODOS sus mercados 05-08) | pendiente |
| 6 | Experimento real de cola en 5m (el de 15m parametrizado), en la wallet dedicada | tras el experimento 15m |
| — | Vigía forward pata 5m barata (otra línea 5m, regla congelada v4) | sigue a diario |

Primer vistazo (05-Oct, SOLO medio día, n insuficiente, sin conclusiones): volumen maker ~2,9 M$ en ~8 h (≈3x el 15m),
BTC ≈88 %; tomadores −47,9k$ con 50,3k$ de comisión (pierden ≈ la comisión); makers −2,4k$ + reembolso estimado 10k$;
makers con vol ≥2k$ ganadores 142 wallets +32k$ vs resto −28k$; en el top 15 maker hay estructura de pares (0x21f4c1a1
100 % ambos lados, coste mediano del par 0,943; 0x764fd57b 77 %, |neto|/acc 0,20) y direccionales.
