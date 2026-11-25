# V2 gate (copia versionada, F5-V4 17-Nov) grupo ('BTC',) (sin filtro de clase) desde 2026-11-04
Dias validos: 11 ['2026-11-04', '2026-11-05', '2026-11-06', '2026-11-07', '2026-11-08', '2026-11-09', '2026-11-10', '2026-11-11', '2026-11-12', '2026-11-13', '2026-11-14']
Dias malos/excluidos: []

Clase causal por print (t=r-100 ms): prints 966812 | lo 957425 hi 0 mixta 0 indet 9387 | EUR excluidos (mixta+indet) 0.97 % del coste; prints excluidos 0.97 %

EV bajo/medio/alto (pond. EUR): +0.068 / +0.003 / -0.051   | EV por unidad mercado-lado: +0.112 / +0.124 / +0.156
coste EUR bajo/medio/alto 567061 / 537247 / 2592946; prints 148957 / 139528 / 673271
exceso alto +57836 (IC90 dias inf +1592, p 0.0133, sin 2 mejores +28744, dias+ 8/11), exceso bajo -47114
bajo-alto por dia +0.100 (IC90 inf +0.037; dias+ 8/11); IC90 cierre exceso alto inf +22859

RT (base F2xmonedaxhora) exceso -8236 (IC90 dias inf -3326, dias+ 4/11)

## Gate (incluye placebo RT)
- 1_exc_alto>0 IC90 dias inf>0: SI
- 2_p<0,05: SI
- 3_sin2mejores>0: SI
- 4_exc_bajo<0: SI
- 5_monotonia: SI
- 6_IC90 cierre inf>0: SI
- 7_dias exc_alto>0 >=2/3: SI
- RT_base F2xmonedaxhora SumEXCESO>0 (literal del prereg): no
**EN CURSO / no cumple**