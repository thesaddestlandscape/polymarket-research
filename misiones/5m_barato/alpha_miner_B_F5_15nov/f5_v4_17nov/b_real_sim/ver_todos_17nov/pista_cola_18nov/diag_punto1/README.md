# diag_punto1 (18-Nov): diagnosticos del punto 1 (caidas escalonadas sin print), solo masa caida vs fills on-chain.
c1.py: fixture 12-Nov (fx30m.csv.gz + E_fxB.pkl, en scratchpad de sesion, no copiados) -> on-chain F side=0 por (token,px); c1.pkl = salida.
c2.py: resumen de fraccion explicada (ventana estrecha/ancha). Resultado: >=80 % de la masa son retiradas reales (ADENDA_02, punto 1).
Rutas absolutas al scratchpad 5055698c...; entradas: E_fxB.pkl (p1 fixture B) y fx30m.csv.gz. Sin tasas evento-placebo. Solo lectura.
Verificado con cmp contra el scratchpad (ver abajo).
18-Nov: entradas (E_fxB.pkl, fx/fx30m.csv.gz) copiadas con cmp OK a /root/polymarket-research-datalogs/pista_cola_18nov/diag_punto1/ y c1.py apunta ahí.
