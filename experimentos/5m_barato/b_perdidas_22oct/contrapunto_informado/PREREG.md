# PREREG — CONTRAPUNTO INFORMADO (25-Oct-2026 ~12:10Z), escrito ANTES de calcular ningún EV por clase
Hipótesis a falsar (inferencia del chief, NO probada): los makers ganan +0,03..+0,08 €/€ como contrapunto de tomadores
NO informados; B pierde porque le rellenan los INFORMADOS. Palanca implícita: exponerse solo a no informados.
Antecedentes que ya vieron datos 09-21 Oct (no se repiten tal cual): F6 (clase por repetición tk_n, H1 no replica),
AS-TOMADOR (lista S_A/R_W por ROI previo, EXCESO +0,004/+0,016 IC cruza 0), wallets_ballenas_b. Novedad aquí:
periodo de MEDIDA 17-23 Oct (posterior), 6 monedas con BTC separado, clase por PERSISTENCIA diaria del PnL tomador
(no solo ROI acumulado), B por clase, y política con rasgos de quién tocó el libro en [t−33,t−5) s.

## Datos
- Órdenes tomadoras y rellenos maker-compra (p<0,45) de `agentes_datos/f6/{T,M}_D.parquet` (derivados de VOL/m5_onchain,
  5m, 6 monedas, 05-23 Oct; maker y tomador explícitos; ts = bloque ~2,4 s tras casado). 24-Oct no extraído → fuera.
- Desenlace oficial: maker_ms_desenlaces_cache ∪ mapa_escala/des.json ∪ b_vs_poblacion/datos/des_gamma.json. Se reporta
  cobertura en € por día; si <98 % en un día, se marca.
## Clase del tomador (EX ANTE, walk-forward por día natural UTC)
Para un relleno del día D, historia = órdenes tomadoras de ESA wallet en los días D−7..D−1 (días completos, nada del día D).
PnL tomador por orden a su precio de ejecución (= el ask/bid que cruzó), neto de su fee: compra acc·win−usd−fee, venta
usd−acc·win−fee; coste compra usd, venta acc−usd. Con historia: n_H órdenes, coste_H, días activos d_H, ROI_H=Σpnl/Σcoste,
f+ = fracción de días activos con ROI diario >0.
- ACT (activo) = n_H≥30, coste_H≥200 $, d_H≥3.
- INF (informado persistente) = ACT y ROI_H ≥ +0,02 y f+ ≥ 0,6.
- DES (desinformado persistente) = ACT y ROI_H ≤ −0,02 y f+ ≤ 0,4.
- MIX = ACT resto. NUEVO = no ACT.
## Medida (días 17-23 Oct = MEAS; 7 días ⇒ todo EXPLORATORY)
Rellenos maker-compra de OTROS makers con p∈[0,05,0,30] (población) y de B (0x659a40ff…297f). pnl maker = acc·win − usd
(sin fee; rebate 0,014·p(1−p)·acc aparte). EV = Σpnl/Σcoste (por €). IC90 bootstrap por DÍA y por CIERRE (cierre×moneda
agrupado en cierre). Universos: BTC y ALT (ETH,SOL,XRP,DOGE,BNB) por separado; descriptivo banda 0,10-0,30.
### H1 (primaria) — EV_maker(DES) − EV_maker(INF) > 0
Gate (por universo): dif>0, IC90 por día Y por cierre excluyen 0, mismo signo en mitades 17-19 y 20-23, sin 2 mejores
días >0, wallet maker top ≤30 % del € en cada clase y tomador top ≤30 % del € de cada clase, placebo (permutar la clase
entre WALLETS tomadoras dentro de moneda, 500 rep.) p<0,05. Inversión: la misma dif con la clase invertida (ROI_H con
signo cambiado) debe dar signo contrario.
### H2 (descriptiva, n pequeño) — B
Cuota de € de B rellenada por INF/DES/MIX/NUEVO vs la de la población en el mismo moneda×día×banda 0,05; EV de B por clase.
### H3 (política) — predecir la clase del tomador que llegará y no exponerse
Rasgos observables antes del relleno (todo con ts ≤ t−5 s por la incertidumbre del bloque): $ tomador en el mismo
mercado en [t−33,t−5) y [t−130,t−33) total y por clase (INF, DES, NUEVO) de quien lo hizo; T desde apertura; banda p;
moneda; hora UTC. Logit (estandarizado) Y=INF entrenado en 17-19, umbral = cuantil del 20 % de € con mayor P̂ en 17-19,
evaluado UNA vez en 20-23: saltar esos rellenos. ΔPnL = −Σpnl(saltados) (cota SUPERIOR: no modela sustitución por otros
rellenos ni que nuestra puja va detrás en la cola). Gate: ΔPnL>0 con IC90 por día y por cierre >0, sin 2 mejores días >0,
placebo (saltar al azar la misma fracción de € dentro de moneda×banda×día, 500 rep.) p<0,05. Oráculo (saltar INF reales)
como techo. Se reporta además la variante «saltar P̂(DES) baja» (solo exponerse cuando el modelo prevé DES), mismo método.
Multiplicidad: BH-FDR q=0,10 sobre {H1 BTC, H1 ALT, H3 BTC, H3 ALT}.
## Qué refuta la hipótesis del chief
(a) EV_maker(DES) ≤ EV_maker(INF) o IC cruza 0 en ambos universos; o (b) el EV de la población no depende de la clase (la
cuota INF de € es pequeña y su AS no explica −18..−33 pp); o (c) B no está sobreexpuesto a INF vs población.
Sin latencia vs Binance ni estado del libro (on-chain no los tiene; libro5/registro ms no cruzados por presupuesto): missing.
