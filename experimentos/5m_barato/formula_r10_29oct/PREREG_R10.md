# PREREG R10 — hazard bajo BTC con bid15 CORREGIDO (29-Oct ~07:10Z, escrito ANTES de reconstruir/medir)
Motivo: auditor + verificación independiente (29-Oct 07:05Z, muestra día 2026-10-20, 400 tokens BTC 5m): en `m15_registro` la fecha de la fila `k` (campo $7 → `kstart` de `k15/k_*.npz`) es el CIERRE del 15m (ej.: k 11:00 ↔ q de 10:21 a 11:00, bid 0,999 a las 11:00:03). La clave de r7a.py:45 / r8h_build.py:59 `(side,(cie-300)//900*900)` apunta al 15m ANTERIOR (ya resuelto): bid15 p50 0,025, corr(bid15,bb) −0,045 (n=396). Clave corregida `(cie-300)//900*900+900`: p50 0,485, corr +0,375 (n=400). `bid15`, `m15`, `dbid15` del modelo HGB congelado `frozen_E2_hgb_BTC.pkl` (sha 971a86f4…) eran por tanto ruido de otro mercado. El modelo viejo y su OOS no se tocan.
## Qué cambia (y nada más)
`r10_build.py` = copia de `formula_r8_28oct/r8h_build.py` con (a) clave bid15 +900, (b) salida a `formula_r10_29oct/hz_BTC.npz`. `r10_train.py` = E2/BTC de `r9c.py` (HGB max_iter 200, lr 0,07, depth 5, min_leaf 100, random_state 1; OOF GroupKFold 5 en IS; Platt sobre OOF; umbral q05 del score IS; Y10) con rutas R10 + comparadores. Mismo universo (22 días de `r5f.inclusion`, BTC 5m, bb∈[0,10;0,35], T_rem 15-285 s, filas 2 s), mismas particiones IS 06-15 / OOS 16-25 / DEV 26-27, mismo desenlace oficial, reloj de recepción, N=10, EV bruto maker sin comisión (rebate 0), IC90 por días (`r4.tci`).
## Regla congelada (idéntica a R9-E2, sin retocar)
INVERSIÓN: score ≤ q05 IS (hazard bajo), m=3 (puja bb−0,03), vida 10 s, llegada +73 ms, relleno ESTRICTO, una orden/10,3 s por token. Sin barrido de parámetros: UNA regla, UN modelo.
## Estado máximo del IS/OOS 16-25/DEV
Regla, m=3, q05 y familia HGB se eligieron en R8 viendo el OOS 16-25 con el dataset roto: ese OOS NO es limpio para la regla. Por tanto el resultado IS/OOS/DEV de R10 es EXPLORATORY como máximo (informativo, nunca CANDIDATE).
## OOS limpio
Tras `r10_train.py` se escribe `HASHES_R10.txt` (sha256 de `frozen_R10_hgb_BTC.pkl`, `r10_build.py`, `r10_train.py`, este PREREG) con fecha de congelado D. Único OOS limpio = días UTC > D (D excluido). Requiere constructor forward corregido (copia de r9fwd.py con la clave +900; pendiente, NO ejecutado: sin cron hasta orden de Javi/chief). El modelo viejo (OOS 28-Oct+) no cuenta.
## Gates (sin relajar; aplican a la evaluación forward limpia; en IS/OOS se reportan como lectura)
n rellenos ≥ 40; ≥ 10 días; EV ponderado por € (Σpnl/Σcoste) ≥ +0,05 con IC90 por días > 0; EV sin los 2 mejores días > 0 (sin2); ≥ 8/10 días positivos; supera en la misma partición a SIEMPRE, ALEATORIO (misma fracción por partición, semilla 7) y ALTO (score ≥ q95 IS); top-día ≤ 30 % del pnl; mercados (día,token) distintos con relleno reportados. REJECTED si EV ≤ 0 o un comparador ≥ medida. Techo EXPLORATORY: relleno estricto es cota sin cola real (solo-toque no cuenta).
## Reproducción
`bash formula_r10_29oct/run_r10.sh` (espera load5≤8, MemAvailable≥2,5 GB, fuera de 06-09Z; ulimit 4,5 GB; nice 19 ionice 3). Logs: `log_run.txt`, `log_build.txt`, `log_train.txt`; salida `salida_r10_train.txt`.
## Juez forward (añadido 29-Oct ~07:25Z, antes de congelar)
El juez forward SOLO cuenta días UTC posteriores a la fecha de congelado D (D excluido) evaluados con `r10fwd.py` y el modelo `frozen_R10_hgb_BTC.pkl` (sha en `HASHES_R10.txt`, que debe incluir la línea `FECHA_CONGELADO YYYY-MM-DD`). `formula_r9_28oct/r9fwd.py` queda DEPRECADO (usa la clave bid15 vieja y el modelo sha 971a86f4): sus días no cuentan para R10. El cron de r9fwd ya fue retirado; ningún cron de r10fwd hasta orden de Javi/chief.

## Subreglas congeladas para el forward (29-Oct, tabla fina; EXPLORATORY)
Modelo congelado sha 5e495915 (HASHES_R10.txt). El forward (dias > 2026-10-29) evalua POR SEPARADO, con el mismo gate (n>=40, >=10 dias, EV ponderado por EUR, IC90 por dias >0, sin los 2 mejores dias, > ALEATORIO y > logit):
- S1: T_rem 200-286 (regla del modelo congelado).
- S2: T_rem 220-286 (union elegida con IS; recomendada por el agente).
- S3 (solo informativa): T_rem 220-260.
- Contabilidad: 1 relleno por (dia,token). Descartados: T280-300, T260-280, T120-200, T200-220.
- Comparadores: ALEATORIO, logit en inversion, SIEMPRE (misma banda, puja y dimensionado).
- Tabla fina: 72 celdas, se esperan 3-4 falsos positivos; el OOS 16-27 no es limpio.
