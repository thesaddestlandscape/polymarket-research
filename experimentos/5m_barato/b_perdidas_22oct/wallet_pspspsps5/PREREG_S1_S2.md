# PREREG S1 / S2 — forward pasivo (shadow, coste 0, sin órdenes) — redactado 24-Oct-2026 antes de ver ningún día ≥ 25-Oct
Origen: auditoría de la wallet 0xb0f85baa… (INFORME.md). K = 2 hipótesis (S1, S2), alfa por hipótesis 0,05/2 = 0,025 (IC90 por días ⇒ criterio «límite inferior > 0» como cota informativa; la decisión usa los gates de abajo). Aprobado por Javi (24-Oct) en esta forma; cualquier cambio posterior = versión nueva + OOS nuevo.
Datos: `m5_onchain_D` (extractor 04:10 UTC; BTC 5m solo), desenlace oficial `analisis_maker_cancelacion_binance.desenlaces()`, rasgos Binance `binance_bookticker_D.csv` (marca de recepción). Día D = día UTC del CIERRE del mercado. Unidad = mercado+lado; un relleno por (mercado, lado, nivel). Fee 0, rebate excluido, sin cola (F1 optimista) y con exigencia de cruce (F2 conservador). Primer día usable: 25-Oct. Primera lectura formal: 04-Nov (10 días). Nada de la ventana 05-23 Oct cuenta (contaminada por el descubrimiento).

## S1 — ESCALERA-CAÍDA-5M (BTC)
- Mercados: BTC 5m, ambos lados. Niveles de puja simulados L ∈ {0,30; 0,20; 0,10; 0,05; 0,03}, 5 acc por nivel y lado.
- Armado: solo con T ≤ 180 s (s hasta el cierre) y solo si el token ya imprimió ≥ 0,40 antes (pmax_prev ≥ 0,40, bloques estrictamente anteriores).
- Relleno F1 (optimista): primera operación pasiva de compra a precio ≤ L en ese token tras el armado. F2 (conservador, PRIMARIO): precio ≤ L − 0,01.
- Métrica primaria: EV ponderado por € = Σ 5·(win − L) / Σ 5·L sobre los rellenos F2 de los niveles < 0,10 (L = 0,05 y 0,03), unidad mercado+lado, IC90 bootstrap por días.
- Controles: (a) puja única L = 0,05 sin armado; (b) mismos niveles en ETH y SOL (informativo, no decide); (c) EV sin los 2 mejores días; (d) nivel a nivel.
- Gate de éxito (todo a la vez): ≥ 10 días de cierre, ≥ 800 unidades primarias, EV ≥ +0,10, IC90 por días > 0, ≥ 7/10 días con EV > 0, EV sin los 2 mejores días > 0, brecha vs control (a) ≥ +0,10 con IC90 por días > 0.
- Se REFUTA si: EV ≤ 0 con ≥ 800 unidades, o IC90 de la brecha incluye 0 tras 10 días.
- Expectativa previa HONESTA (de este análisis): la escalera ingenua optimista (sin cola) dio EV −0,145 (05-12 Oct) y −0,254 (17-23 Oct) en todas las monedas, y condicionar a z de Binance o a movimiento de 10 s no la rescata (−0,09..−0,24). S1 se espera refutar; su valor es cerrar la pregunta a coste cero.

## S2 — CARRY-90 (medición de capital, BTC)
- Niveles L ∈ {0,92; 0,95; 0,97}, 10 acc, solo T ≤ 150 s, token con pmax_prev ≥ 0,90. Relleno F2: operación pasiva a precio ≤ L − 0,01 (F1 informativo).
- Métrica primaria: EV por € y EV por € y hora de capital inmovilizado (Σ pnl / Σ L·acc·T/3600).
- Referencia W (medida 05-23 Oct, fills ≥ 0,90): EV +0,012 (IC90 por días +0,004..+0,020), n=6.066 fills, 2.548 unidades.
- Gate: ≥ 10 días, ≥ 1.500 unidades, EV ≥ +0,010, IC90 por días > 0, ≥ 7/10 días > 0.
- Se REFUTA si EV ≤ 0 con ≥ 1.500 unidades. No es candidata de capital con la dedicada (5 €): solo medición de capacidad.

## Implementación y cron (PROPUESTA, no instalar)
Script nuevo `s1s2_forward_pspsps5.py --dia D` (reutiliza la lógica de `f7_poblacion.py`, `f13_features.py`, `f16_placebo_escalera.py`; parametrizar f7 con `--pmin/--pmax` para el carry) escribiendo `datalogs/pspsps5_forward/s1_D.csv.gz`, `s2_D.csv.gz` e informe.
Cron: `25 10 * * * cd /root/polymarket-research && nice -n 19 ionice -c3 python3 s1s2_forward_pspsps5.py --dia $(date -u -d yesterday +\%F) >> logs/s1s2_forward.log 2>&1 || python3 telegram_aviso.py "s1s2 forward fallo"` (UTC, tras el extractor 04:10, fuera de 06-09Z; `ulimit -v 3000000`).
Este PREREG se hashea al guardarse (`PREREG_S1_S2.sha256`); el script debe imprimir el hash y abortar si no coincide.
