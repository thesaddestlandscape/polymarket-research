# F6 TIPO-TOMADOR (selección adversa según tipo de flujo) — 24-Oct-2026
Etiqueta: **REJECTED como palanca (H1 no replica; H3 no pasa el gate); H2 (contexto predice el tipo) EXPLORATORY con efecto modesto; el EV extra de los «buenos contextos» NO pasa por el tipo de tomador.** No autoriza nada. Solo lectura, nice 19, sin tocar B/live/crons. PREREG.md (sha256 en PREREG.sha256) escrito ANTES de calcular EV; solo había visto la distribución de n por clase.

## Datos y método (reproducible)
- Población: `agentes_datos/q_techo/tab.pkl` (unidades de OTROS makers ETH/SOL/XRP 5m, pc 0,10–0,30, T 60–300 s, primeras 5 acc por maker-mercado-lado; n=113.918; desenlace oficial; EV=Σpnl/Σc por €; maker sin fee ni rebate). DISC 09–14 Oct (n=59.388), HOLD 15–20 (n=51.212); 21-Oct truncado → solo descriptivo.
- Taxonomía ex ante (`scripts/e1_extrae.py`, `e2_rasgos.py` sobre `m5_onchain` 05–23 Oct, 9,9 M órdenes tomadoras, 35.262 wallets, cobertura de desenlace 99,99 %): para el tomador de cada relleno, nº de órdenes tomadoras previas en [t−96 h, t−10 s) (tk_n), días activos, ticket medio, ROI previo (solo mercados cerrados ≥120 s antes), flujo reciente del mercado por clase del tomador. Clases: C1 ≤19 (2,6 % unid.), C2 20–199 (14,6 %), C3 200–1999 (32,6 %), C4 ≥2000 (49,1 %; **113 wallets**, 52 % del €).
- Scripts: `scripts/lib.py, e3_ev_clases.py, e4_ejes.py, e5_contexto.py, e6_politica.py, e7_control.py`; salidas en `datos/e3..e7_salida.txt`, `e5_preds.pkl`, `units_clases.pkl`.

## Tarea 2 — EV del lado maker por clase (H1: NO-REP ≤199 mejor que REP ≥200)
| periodo | EV total | NO-REP (17 % €) | REP (83 % €) | dif NO-REP−REP, IC90 por cierre | placebo (estratos día×moneda×pc) |
|---|---|---|---|---|---|
| DISC | +0,055 | +0,030 (−0,035,+0,095) | +0,060 (+0,009,+0,113) | **−0,031** (−0,083,+0,023) | p=0,82 |
| HOLD | −0,011 | +0,034 (−0,038,+0,112) | −0,021 (−0,074,+0,037) | **+0,055** (−0,006,+0,117) | p=0,002 |
- **El signo se invierte entre periodos** y por días (dif diaria de −0,127 a +0,190); sin los 2 mejores días HOLD +0,018. C1 (≤19) vs resto: +0,015 (DISC) / +0,067 (HOLD), IC90 cruzan 0. Por moneda en HOLD solo SOL cumple (+0,144, IC90 +0,037,+0,254; ETH +0,035, XRP +0,020), en DISC ninguna. **H1 FALLA** (no hay replicación DISC→HOLD; K=2, alfa 0,025). El nivel de EV lo domina el régimen del periodo (total +0,055 → −0,011), no el tipo.
- Ejes post-hoc (K=10, descriptivos, `e4_salida.txt`): ninguno mantiene signo e IC90>0 en ambos periodos (ticket grande: +0,141 DISC → +0,011 HOLD; ≥20.000 órdenes: +0,010 → −0,099; «perdedor previo» +0,043 → +0,023 con IC que cruza 0; «informado previo» +0,007/+0,049 cruza 0). Único signo estable: bots ≥2000 peor que el resto (−0,033 y −0,033, ambos IC cruzan 0).
- Mapa moneda×tramo×clase (48 celdas, `e3_salida.txt`): sin patrón; DISC y HOLD se contradicen en la mayoría (p. ej. ETH [0,10–0,15) NO-REP +0,09 → −0,16). Con 48 celdas y Bonferroni no hay ninguna.
- Compatibilidad con el hallazgo de W: la brecha +0,73/+0,49 con tomadores «raros» no se reproduce en la población (0,10–0,30). Ojo, no son comparables: W vive en p<0,10 y la clase «raro» de f23 se definió por repetición HACIA W (no ex ante). W sigue siendo específica de W/banda, no una propiedad del tipo de flujo.

## Tarea 3 — mapa de contexto (H2: ¿contexto ex ante predice que el próximo tomador sea NO-REP?)
Walk-forward diario, Y=NO-REP (base 18–19 %), placebo AUC p95 ≈0,51:
| modelo | AUC DISC (12–14) | AUC HOLD (15–20) | lift quintil sup. HOLD (IC90 cierre) |
|---|---|---|---|
| base (pc,T,hora,moneda,lado) | 0,542 | 0,538 | 1,14 (1,09–1,19) |
| + libro/Binance (logit) | 0,579 | 0,579 | 1,32 (1,28–1,36) |
| + libro + composición reciente del flujo (logit) | 0,583 | 0,587 | 1,35 (1,30–1,40) |
| + libro + flujo (HGB, el de mejor DISC) | 0,627 | **0,610** (0,603–0,619) | **1,49** (1,45–1,54) |
- Gate prereg (AUC HOLD ≥0,58 con IC>0,55; lift ≥1,5 con IC inferior ≥1,2): AUC cumple; lift 1,49 queda a 0,01 del umbral → **marginal/EXPLORATORY**. Predice mejor «BOT ≥2000» (AUC 0,607 logit). La señal más fuerte es el propio flujo reciente del mercado (repetidores activos hace <2 min → el siguiente tomador también lo es): autocorrelación de identidad dentro del mercado, ya implícita en el vol30 de R3.
## Tarea 4 — política «pujar solo donde P̂(NO-REP) es alta» (H3)
HGB, umbral por moneda fijado en DISC (retención 50/30/20 % del €), nivel elegido en DISC por prereg = 50 %. EV por € retenido y ΔPnL = −PnL de lo saltado (COTA SUPERIOR, sustitución no modelada; con haircut 50 % entre paréntesis):
- DISC (12–14): ΔPnL **−740 €** (50 %), −1.102 (30 %), −1.172 (20 %): saltar pierde porque el mercado era +EV; IC90 cruzan 0, 1/3 días >0.
- HOLD (15–20, una pasada), nivel elegido 50 %: retiene 49,7 % del €, EV_ret +0,003 vs total −0,011, **ΔPnL +606 € (+303), IC90 por cierre (−885,+2.098), sin los 2 mejores días −249, 4/6 días >0, placebo p=0,157 → FALLA el gate** (inversión −65). Descriptivos: 30 % ΔPnL +1.284 (IC −677,+3.244; sin 2 mejores días −4; placebo p<0,001; EV_ret +0,052), 20 % +1.268 (IC −931,+3.467; sin 2 días −25; EV_ret +0,080). Oráculo (clase real, retener NO-REP): ΔPnL +839 (IC −1.360,+3.004; sin 2 días −522; 4/6 días): ni con la clase conocida de antemano hay política que pase el gate.
- **Control decisivo (`e7_salida.txt`)**: el top-20 % de contexto tiene mayor EV que el resto en ambos periodos (HGB: +0,071 DISC, +0,100 HOLD IC90 +0,026,+0,177), pero (i) dentro de la MISMA clase la mejora persiste (REP: +0,139 vs +0,050 DISC; +0,036 vs −0,033 HOLD; NO-REP +0,160 vs −0,020 HOLD) y (ii) un modelo SIN información de tipo (solo pc,T,hora,moneda,lado; NO-REP 20 % vs 18 % en top/resto) da la misma o mayor mejora (+0,145 DISC, +0,066 HOLD). Es estructura precio/tiempo/régimen ya conocida (R3, bandas), **no selección adversa por tipo de tomador**.
- Escala: aun tomando como bueno el EV_ret +0,05…+0,08 del 30/20 % (no validado), a 136 €/día de puja de B (r3_escalado) y ~20–30 % retenido: ≈ 136×0,25×0,08×365 ≈ **1 k€/año de cota alta** (el 100 % de lo posible a 136 €/día es ≈ +4 k€/año con EV +0,08). Hueco a 200 k€: ≥ 99 %. Nunca extrapolar.

## Limitaciones
Unidad condicionada a relleno; maker sin rebate (≈+1…2 pp del coste a pc 0,10–0,20; no cambia el signo del contraste); ETH/SOL/XRP y pc≥0,10 (no cubre BTC ni p<0,10 donde vive W); tomador = wallet de la orden (bots con varias wallets quedan como «ocasionales»: sesgo a favor de NO-REP; las 113 wallets ≥2000 son el 49 % de las unidades); 21-Oct truncado; periodos DISC/HOLD cortos (6 d) y régimen distinto (EV total +0,055/−0,011); tab.pkl y otros informes ya vieron estos días (la selección de R2/R3 salió de 17–21).
## Prereg forward
Nada aguanta → no se registra forward de política. Opcional coste cero (L1): añadir al etiquetado pasivo la columna `tk_n` del tomador (clase C1–C4) y `share_rep` del flujo de 2 min en cada relleno propio de B/E1, ≥10 días, solo para re-medir H1 (NO-REP−REP, gate: dif>0 con IC90 por cierre>0 en 2 mitades temporales). Sin cambio de B.
