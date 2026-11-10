# PREREG H-DB3 "episodio" (brazo ex ante de la familia DB) — BORRADOR validator 10-Nov, NO congelado. EXPLORATORIA. 0 ordenes.
Hereda de PREREG_DB1 (sha 1d12afa2...) + ADDENDUM1 + ADDENDUM3 (al congelarse): motor, guardas, cotas BASE/CROSS, desenlace oficial,
dias validos, checkpoints 10/20, robustez. Solo lo distinto va aqui. Universo 5m ETH/SOL/XRP; BTC DATA_BLOCKED.
Base (debil, declarada): descriptivo de ADDENDUM2 §5.2 en S_pop, sin IC, sin artefacto reproducible. Datos 20-Oct..09-Nov QUEMADOS.

1. Hipotesis: tras una rafaga R0 observada en un mercado, no tener bids en ese mercado durante X s mejora el PnL de G0.
2. Reloj (critico): la identidad ">= 2 tomadores distintos" solo existe on-chain. t_det = hora del BLOQUE + 3 s (sensibilidad +6 s).
   Prohibido usar la hora del print con la identidad del bloque. Solo eventos con t_det < t de la decision.
3. Brazo primario DB3_30: en t_det se cancelan los bids de G0 en ambos tokens del mercado a t_det + l (l = 150 ms); no re-arma hasta
   X = 30 s sin nueva rafaga detectada y solo si G0 armaria. Rellenos de G0 previos a t_det + l se mantienen (no hay salida).
   Descriptivos (no deciden): X = 10 y 60 s; retraso +6 s; mitades del mercado; moneda; YES/NO; franja de L.
4. Metrica: dPnL = PnL(DB3_30) − PnL(G0), BASE, EV ponderado por €. Indicador de mandato aparte (no gate): EV_brazo > 0 con IC90 dia inf > 0.
5. Placebo (C6): desplazamiento circular de la serie de t_det por moneda y dia (offset uniforme, >= 60 s), mismo X y l; tiempo total
   de pausa igual ±10 % (si no, se descarta la permutacion y se reporta cuantas). 300 permutaciones, p = (1 + #{|d_perm − m| >= |d_obs − m|}) / 301, d_obs > m.
6. Inversion (C7): pausa de X s tras rellenos SUELTOS (1 tomador) con la misma tasa; dPnL_inv <= media del placebo.
7. Gates: C1-C10 de PREREG_DB1 tal cual (C1 incluye >= 40 rellenos de G0 quitados), salvo C6 con alfa/3: p <= 0,033 (familia
   {CXJ150, DB1, DB2, DB3}). Si DB3 y DB2 son CANDIDATO y comparten > 50 % de los rellenos quitados: un solo hallazgo.
8. Dias: D >= dia siguiente a la congelacion (00:00Z), validos segun DB1+ADDENDUM3; insumo extra obligatorio: on-chain del dia con
   cobertura de tomadores >= 0,95 de las tx del tape (si no, dia NO VALIDO para DB3). Checkpoint 20 no antes de 2026-12-02. Tope 2026-12-31.
9. REFUTA / INSUFFICIENT: igual que DB1. Dia valido sin rellenos ni de DB3 ni de G0: no cuenta en ese contraste.
10. Implementacion: var nueva en passdb (execution-engineer), con test que pruebe t_det >= bloque + 3 s y que G0 queda identico
    (aceptacion A1 de ADDENDUM3 repetida). Sin esa prueba, ningun dia cuenta.
