# PREREG INCLUSIÓN (detector de rellenos BUENOS) — congelado 24-Oct-2026 11:29Z (modelos) / 11:50Z (este texto), ANTES de ver ningún día ≥25-Oct
Origen: INFORME.md sec. 3 (pista POST-HOC, 12-20 Oct) + prueba 22-23 Oct (OOS respecto al TRAIN pero anterior a la congelación: NO cuenta).
Modelos congelados (HistGradientBoosting prof. 3, 200 it., lr 0,05, hoja 300, l2 1; TRAIN = todos los rellenos de población 09-20 Oct de q_techo/tab.pkl, n=110.600):
- **M1F** (primario desplegable): pc, T, moneda, hora, lado, vol30, bb, ba, bs, spread, depth_ticks, b15, a15, lvl15, gap15, vol30ws, r60f, rpre_s, CON. sha256 pickle eafda286…; corte EV ≥ 0,19356.
- **M2** (FULL, + historia de prints de build_units): sha256 pickle 65c7d29e…; corte EV ≥ 0,19940. Hoy DATA_BLOCKED en forward (no se producen units_D.pkl/att_D); se evalúa sólo si se cablea SIN tocar el modelo.
- Ficheros: /mnt/HC_Volume_106538179/agentes_datos/detector_ex_ante/MODELO_CONGELADO.json (sha256 21b4e4a7d8f40ddb…), pickles en la misma carpeta. Regla: bandera = EV predicho ≥ corte (≈10 % del € en TRAIN).
## 1. Población y unidad
Rellenos de OTROS makers ETH/SOL/XRP 5m, pc (0,10-0,30], T 60-300 s, primeras 5 acc por maker-mercado-lado, sin la wallet dedicada (`/root/polymarket-research-datalogs/sa_r1/units2_D.csv.gz`, cadena R1 forward); desenlace oficial (cobertura ≥99 % que exige r1_fwd_extract). Rasgos en t_obs = ts − 4 s, Binance por RECEPCIÓN. Días evaluables: **D ≥ 2026-10-25**; un día con cobertura <90 % de r60f/rpre_s/bb/b15/vol30ws = DATA_BLOCKED (no cuenta, no es 0).
## 2. Métricas por día
EV_pob = Σpnl/Σcoste; EV_top; exceso = pnl_top − f·pnl_día (f = fracción de € banderado); placebo = misma fracción de € al azar (Bernoulli, 2.000); brecha = EV_top − EV_pob; por moneda.
## 3. Gate (K = 2 modelos; α unilateral 0,025 cada uno) — evaluado al llegar a 15 días evaluables
Todo a la vez: ≥15 días; ≥3.000 unidades banderadas; exceso total >0; IC90 por días (bootstrap de días) del exceso con límite inferior >0; exceso sin los 2 mejores días >0; brecha media ≥ +0,03 €/€ con IC90 por días >0; ≥60 % días con exceso >0; placebo: p medio <0,025; ninguna moneda con brecha < −0,05 (n_top ≥300).
## 4. Falsador (fijado de antemano)
A los 15 días evaluables, si falla cualquier criterio de la sec. 3 → **REFUTADO** para ese modelo, sin re-entrenar ni cambiar el corte. Única extensión permitida (una vez): si exceso >0 y brecha >0 pero algún IC90 cruza 0 → 15 días más con el mismo modelo y gate. Nunca se cambia la población, el corte ni los rasgos.
## 5. Lo que NO autoriza
Pasar el gate = candidata. Para B hace falta además: P(relleno) de las pujas de B (o virtuales, `vida_puja_virtual_5m`) dentro de la bandera no inferior a fuera de ella (sec. 5 del INFORME), /code-review y OK de Javi. Descriptivos (no deciden): cruce con R1 (vol baja Binance) y zs∈(−1,0].
