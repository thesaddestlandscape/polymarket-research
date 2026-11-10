# PREREG H-DB3 «episodio» (brazo ex ante de la familia DB). CONGELADO 2026-11-10 ~12:55Z. EXPLORATORIA. 0 órdenes.

Autoriza: Javi (10-Nov). Redacta: cheap5m-statistical-validator. Universo 5m ETH/SOL/XRP; BTC DATA_BLOCKED.
Hereda de PREREG_DB1 (sha256 1d12afa2f22a1bbb3ccece15b2aec01f437d86b7ef83f2a23479708e1197e998), PREREG_DB1_ADDENDUM1 (sha256 b083b7a5…),
PREREG_DB1_ADDENDUM2 y PREREG_DB1_ADDENDUM3 (shas en sus .sha256): motor, guardas, cotas BASE/CROSS, desenlace oficial, días válidos (incl. B1-B3 y el
umbral de lado del print), checkpoints 10/20, robustez. Solo lo distinto va aquí.
Base (DÉBIL, declarada): descriptivo de ADDENDUM2 §5.2 en S_pop, sin IC y sin artefacto reproducible. Datos 2026-10-20..2026-11-09 QUEMADOS.
Visto antes de congelar: cifras por día de G0 y de los brazos en quemados y el placebo circular parcial de DB1/DB2 (ADDENDUM2 §5.3).

## 0. ESTADO DE IMPLEMENTACIÓN — NO SE EVALÚA TODAVÍA
Ni la variante DB3 ni su placebo (§5, con tiempo de pausa igualado ±10 %) están implementados en passdb.py/eval_db1.py; hacerlo cambia el code_sha
(f33f2e4d… hoy) y exige repetir la aceptación A1 de ADDENDUM3. Su implementación y aceptación son un paso POSTERIOR, con su propio addendum de código
congelado con sha (PREREG_H_DB3_ADDENDUM_CODIGO). Hasta que ese addendum esté congelado y su aceptación dé PASS, H-DB3 NO se evalúa, ningún día cuenta
y no se emite ninguna cifra de DB3 salvo los tests de implementación.

1. Hipótesis: tras una ráfaga R0 observada en un mercado, no tener bids en ese mercado durante X s mejora el PnL de G0.
2. Reloj (crítico): la identidad «>= 2 tomadores distintos» solo existe on-chain. t_det = hora del BLOQUE + 3 s (sensibilidad +6 s). Prohibido usar la
   hora del print con la identidad del bloque. Solo eventos con t_det < t de la decisión.
3. Brazo primario DB3_30: en t_det se cancelan los bids de G0 en ambos tokens del mercado a t_det + l (l = 150 ms); no re-arma hasta X = 30 s sin nueva
   ráfaga detectada y solo si G0 armaría. Los rellenos de G0 previos a t_det + l se mantienen (no hay salida).
   Descriptivos (no deciden): X = 10 y 60 s; retraso +6 s; mitades del mercado; moneda; YES/NO; franja de L.
4. Métrica: dPnL = PnL(DB3_30) − PnL(G0), BASE, EV ponderado por € (Σpnl/Σcoste) además de por unidad. Indicador de mandato aparte (no gate):
   EV_brazo > 0 con IC90 por día inf > 0.
5. Placebo (C6): desplazamiento circular de la serie de t_det por moneda y día (offset uniforme, >= 60 s), mismos X y l; tiempo total de pausa igual
   ±10 % (si no, se descarta la permutación y se reporta cuántas). 300 permutaciones, p = (1 + #{|d_perm − m| >= |d_obs − m|}) / 301, d_obs > m.
   (Motivo de igualar la pausa: ADDENDUM2 §5.1 y §5.3, nulos con cobertura distinta no son comparables.)
6. Inversión (C7): pausa de X s tras rellenos SUELTOS (1 tomador) con la misma tasa; dPnL_inv <= media del placebo.
7. Gates: C1-C10 de PREREG_DB1 tal cual (C1 incluye >= 40 rellenos de G0 quitados), salvo C6 con alfa/3: p <= 0,033 (familia {CXJ150, DB1, DB2, DB3}).
   Si DB3 y DB2 son CANDIDATO y comparten > 50 % de los rellenos quitados: un solo hallazgo.
8. Días: D >= día siguiente (00:00Z) a la congelación del addendum de código de §0, y nunca antes de 2026-11-11; válidos según DB1 + ADDENDUM1-3;
   insumo extra obligatorio: on-chain del día con cobertura de tomadores >= 0,95 de las tx del tape (si no, día NO VÁLIDO para DB3).
   Checkpoint 20 no antes de 2026-12-02. Tope 2026-12-31 (sin checkpoint 20 ⇒ INSUFFICIENT).
9. REFUTA / INSUFFICIENT: igual que DB1. Día válido sin rellenos ni de DB3 ni de G0: no cuenta en ese contraste.
10. Implementación (en el addendum de código): var nueva en passdb (execution-engineer), con tests que prueben t_det >= bloque + 3 s, que G0 queda
    idéntico (aceptación A1 de ADDENDUM3 repetida con el code_sha nuevo) y que el placebo iguala la pausa ±10 % y cuenta las permutaciones descartadas.
    Sin esas pruebas, ningún día cuenta.
