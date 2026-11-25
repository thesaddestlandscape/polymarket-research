# V2 gate (copia versionada, F5-V4 17-Nov) grupo ('ETH', 'SOL', 'XRP') (sin filtro de clase) desde 2026-11-04
Dias validos: 11 ['2026-11-04', '2026-11-05', '2026-11-06', '2026-11-07', '2026-11-08', '2026-11-09', '2026-11-10', '2026-11-11', '2026-11-12', '2026-11-13', '2026-11-14']
Dias malos/excluidos: []

EV bajo/medio/alto (pond. EUR): +0.059 / +0.007 / -0.135   | EV por unidad mercado-lado: +0.081 / +0.018 / -0.034
coste EUR bajo/medio/alto 140424 / 123108 / 66690; prints 70356 / 62674 / 35350
exceso alto +8850 (IC90 dias inf +479, p 0.0006, sin 2 mejores +5664, dias+ 9/11), exceso bajo -7963
bajo-alto por dia +0.188 (IC90 inf +0.118; dias+ 11/11); IC90 cierre exceso alto inf +5972

RT (base F2xmonedaxhora) exceso +2330 (IC90 dias inf -23, dias+ 9/11)

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