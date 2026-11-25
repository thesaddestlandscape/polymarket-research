# Revisión estadística independiente de Q-C2 (cheap5m-statistical-validator, 16-Nov 21:48Z)
Resumen transcrito por la sesión principal (el agente no tenía Write). Código del validador: scratchpad `qa_qc2.py` (sha256 2dfbd4bd…8413), independiente, ~1,2 s CPU. No edita nada sellado.

1. Sellos y cifras: OK. Reproduce V0 26,2 % (6 FP/0 TP), C1 72,5 %, C2 40,9 %, V4 −31,6 %, MIX anulaba 10 TP, T1 p cond. 0,512, T5 +1 ms; ΔEV IC90 [+0,011; +0,084].
2. FALLO NUEVO (polvo): 2 de los 6 FP anulados (23-Oct eth x=40, sol x=35) tienen q_s ≈ 2e-7 acciones (coma flotante, umbral q>1e-9). FP reales 10 (no 12); anulados reales 4; escalón 4/5 (no 6/7). EV sin cambio; recuentos y placebos sí. Afecta también a QC y brecha_nivel_v3.
3. Placebos sin polvo (S_obs=4): global sellado p 0,0002 (estructural, x<=rtt); D3 condicionado 0,057; nulo forward 0,053; sin TP con rtt>=1 s 0,14-0,15; solo lado FP 0,56.
4. Causalidad inversa también <1 s (p50 rtt 67,5 vs 65; TP afectables 75; MW p=0,003). Los 7 de T1 tienen todos cancel_ya_terminal_ack: T1 no informativa.
5. Veredicto: MECANISMO_SOPORTADO_POR_ORDEN se cumple LITERALMENTE; en sustancia, identificación por orden NO VALIDADA. Queda el NIVEL de δ (compatible con fantasmas al final del segmento; Fisher p=0,0005).
6. HI: solo compatible, no respaldada. T5 no discrimina (θ se cancela; solo 2 ventanas lo). T2 V4 FAIL frágil (11/36; con 2 menos AMBER; solo sig 8/28). Única inferencia válida: A_HI(20-23 Oct) <= ~32 ms. No hay A_LO del mismo periodo.
7. Relojes/n: A arrastra θ no medido 20-23 Oct; f ∈ [0 (A=0); 0,326 (A<=33)]. Filo de 1 ms (V2 17,9 %). n efectivo = 4 FP con dinero, 4 días/cierres; sin uno, f 0,18-0,20. ΔEV>0 es mecánico (los FP son perdedores). δ usa t_fuera (depende del desenlace): admisible en replay, NO trasladable a simulador forward.
8. «No validado»/INSUFFICIENT: identificación por orden, T4, T1; el 26,2 % como cifra puntual; «la carrera no necesita corrección HI». Se mantienen: corrección a MIX (anulaba 10 TP), C1/C2 en EV, cautela c.

Reparación (versión nueva descriptiva, sin tocar sellados): (a) umbral q>=1e-3 y recontar FP/S/T4/placebos; (b) STATUS: «literal; en sustancia no validado» + D3/nulo forward; (c) cierre como f(A) con cota A<=32 ms, sin cota inferior; (d) T1 «no informativa»; (e) retirar «no necesita corrección HI» hasta A_HI y A_LO medidos el mismo día (ADDENDUM2 §8).
Ninguna etiqueta autoriza operar en real.
