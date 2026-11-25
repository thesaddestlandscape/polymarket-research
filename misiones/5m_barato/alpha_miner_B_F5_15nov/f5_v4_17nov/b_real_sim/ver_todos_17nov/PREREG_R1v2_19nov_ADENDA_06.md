# PREREG R1v2 — ADENDA 06 (19-Nov ~12:50Z, chief). Antes de leer ningún EV de la Puerta 0.
Base: PREREG_R1v2_19nov.md + ADENDA_01..05 (sha en sus .sha256). Decide las 4 ambigüedades que dejó el implementador de r1v2_eval (fase A):
1. Días de la Puerta 0: se simulan 03-09 Nov (PREREG §4); CONFIRMATORIOS = 05-09 Nov (ADENDA_03 §D excluye ≤04-Nov); 03-04 Nov se publican etiquetados POST HOC y no deciden.
2. Validez lo: PRIMARIA por celda (día, moneda) con n_clas ≥ 24 y frac_lo ≥ 0,5 según tabla_suelo_ventanas_19nov.csv firmada; el IC90 se calcula por DÍAS agregando las celdas válidas de cada día. Sensibilidad publicada: día válido solo si ETH, SOL y XRP son válidas a la vez.
3. Test de fuga NaN de F5_t: CONGELADO pasa si AUC ∈ [0,40; 0,60] en cada día con n_inválidos ≥ 20; días con n<20 se reportan sin decidir; si falla en algún día confirmatorio → Puerta 0 = BLOCKED_FUGA.
4. Cambio de tercil F5_t vs F5 (reloj exchange): solo DESCRIPTIVO (supuesto de tamaño declarado); no decide.
5. Recursos: ulimit -v 3000000 (como sec7) en run_puerta0.sh. Bloqueo: bloq0 (motor vigente) PRIMARIA; bloq1 (canal bloqueo = nivel entero) sensibilidad; el veredicto PASA exige mismo signo en ambas.
Nada más cambia.
