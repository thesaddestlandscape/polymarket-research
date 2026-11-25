# V2 gate (copia versionada, F5-V4 17-Nov) grupo ('ETH', 'SOL', 'XRP') SOLO clase causal pura desde 2026-11-04
Dias validos: 11 ['2026-11-04', '2026-11-05', '2026-11-06', '2026-11-07', '2026-11-08', '2026-11-09', '2026-11-10', '2026-11-11', '2026-11-12', '2026-11-13', '2026-11-14']
Dias malos/excluidos: []

Clase causal por print (t=r-100 ms): prints 168674 | lo 167030 hi 0 mixta 0 indet 1644 | EUR excluidos (mixta+indet) 0.85 % del coste; prints excluidos 0.97 %

EV bajo/medio/alto (pond. EUR): +0.058 / +0.009 / -0.136   | EV por unidad mercado-lado: +0.079 / +0.017 / -0.036
coste EUR bajo/medio/alto 139329 / 122108 / 66063; prints 69705 / 62081 / 34957
exceso alto +8886 (IC90 dias inf +477, p 0.0006, sin 2 mejores +5587, dias+ 9/11), exceso bajo -7721
bajo-alto por dia +0.188 (IC90 inf +0.117; dias+ 11/11); IC90 cierre exceso alto inf +5835

RT (base F2xmonedaxhora) exceso +2476 (IC90 dias inf -10, dias+ 9/11)

## Gate (incluye placebo RT)
- 1_exc_alto>0 IC90 dias inf>0: SI
- 2_p<0,05: SI
- 3_sin2mejores>0: SI
- 4_exc_bajo<0: SI
- 5_monotonia: SI
- 6_IC90 cierre inf>0: SI
- 7_dias exc_alto>0 >=2/3: SI
- RT_base F2xmonedaxhora SumEXCESO>0 (literal del prereg): SI
**LISTO: gate cumplido (incl. RT) si n>=10**