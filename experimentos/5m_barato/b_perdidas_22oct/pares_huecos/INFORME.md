# B: pares, rellenar el hueco (pata contraria) y cosecha — ingeniería inversa (22-Oct-2026, ~17:30Z). Estado: REJECTED para B / EXPLORATORY para H39b
Solo lectura. B (`experimento_maker_h47.py`, sha c82f5dc5f304b8a6 verificado en dev) y supervisor, procesos, crons y config sin tocar; sin órdenes.
Preregistro congelado ANTES de calcular: `PREREG.md` (sha256 fc6db829842fdb46…, `sha256sum -c PREREG.sha256`). `nice 19 ionice -c3 ulimit -v 3 GB`.
Cosechar al abrir en ETH/SOL/XRP NO se simula aquí (lo lleva `../cosechar_abrir/`); mis hallazgos de ganadores para ese agente: `GANADORES_PARES_PARA_COSECHAR.md`.

## 0. Respuesta corta a Javi
**No funcionan para B, y ahora sabemos por qué con dinero medido.** B es una apuesta de longshot (lado barato 0,10-0,30); su única fuente de EV es la prima del
longshot en los rellenos que no son barridos. La pata contraria es el favorito a 0,70-0,90 y, en el instante en que B se entera de su relleno, el par ya cuesta
**1,026 (B) / 1,009 (población) + 1c de comisión**: la selección adversa YA está cobrada. Comprar el contrario como tomador = vender la pata al bid (misma cuenta,
confirmado: en cosechar v2 «completar como tomador» y «salir» dan el mismo PnL al céntimo). Pujar el contrario como maker se rellena justo en las que iban a ganar
(cuando el barato sube) y recorta el pago 4-9×. Las 10 políticas pierden frente a mantener en B real y en población, en descubrimiento y en test. Lo único que hace
el par es bajar la varianza ~10× a cambio de convertir B en una pérdida casi segura (−0,09..−0,17 por €). Los que sí ganan con pares (0x21f4 BTC, 0xf074/0x0ab0 ETH)
no «tapan huecos»: cotizan ambos lados en continuo con clips de 5 acc y sobreviven porque su margen de par supera a su pata suelta, que también pierde.

## 1. Variantes de pares / huecos / cosecha ya probadas (B o 5m)
| # | Variante | Instrumento | n | Resultado | Veredicto | Fichero |
|---|---|---|---|---|---|---|
| 1 | Pares 15m anclar/crear/mixta (maker ambos lados, pata quieta) | sim cola + ensayo crear | 80+80 merc | sueltas −33,21 $ = 226 % del margen; crear −0,103 $/merc IC90 (−0,32,+0,11) | REJECTED | memoria `project_mision_pares15_12oct`, `informes/pares15_mision_12oct.md` |
| 2 | Pares 15m: completar como tomador / salir al bid / límite τ | mismo | 77 | tomador imposible (bid+ask+fee ≥1); salir −15,8 $; τ −16..−25 $ | REJECTED | idem |
| 3 | Pares 5m maker en banda ≤0,45 (subestr. 4) | sim cola | 9 días | OOS −0,050, CABEZA −0,032, 0/4 días; sueltas 3× el margen | REJECTED (cementerio) | `TRAMPAS_5M_BARATO.md` |
| 4 | LOWLOW-PAIR ≤0,10 ambos lados BTC 5m | cota optimista | 10-14 Oct | −0,197 €/merc 0/5 días; suelta gana 0/1.314 | REJECTED | `analisis_lowlow_pair_exploratorio_15oct.py` |
| 5 | Cosechar al abrir v1 BTC (A sin/con defensa Binance; B defensa 15m) | sim cola, DESC 05-09 / OOS 10-14 | 10 días | 24/24 celdas OOS <0; pares completos 80-86 % y aún −0,04/−0,08 €/€ | REJECTED | `DL/m5_cosechar_apertura/informe.txt` |
| 6 | Cosechar v2 reactiva: completar pata suelta tomador (U1,00-1,05), salir (X), ambas, skew | idem | 2.726 merc | DESC 0/5 días+; OOS 0/64 >0 (mejor −0,026); par_maker +0,042 vs suelta −0,908 €/€ | REJECTED | `DL/m5_cosechar_apertura_v2/informe.txt`, `desglose_modo_final.txt` |
| 7 | Cosechar 13a régimen vol / 13b recompensas | sim | 10 días | calma peor; sin programa de recompensas en up/down | REJECTED | DECISION_LOG 16-Oct 12:00Z |
| 8 | Cobertura maker del contrario a 1−p−m (m 1-5c) sobre puja tipo B | simv2 libro real 17-21 | 3.269 rellenos | −0,336..−0,341; P(cobertura) 49-59 %; recorta ganadoras | REJECTED | `b_seleccion_adversa/INFORME.md` §C |
| 9 | Maker en el favorito 0,70-0,90 (lado contrario como estrategia) | cinta completa | 270 k rellenos | −0,003..+0,011, IC90 incluye 0 | REJECTED (sin AS pero sin edge) | idem §3 #10 |
| 10 | Salida de la pata tras el relleno (≡ cobertura tomadora): 40 reglas τ 5-60 s | B real + población 17-22 | 166 / 5.677 | todas <0 en test (−0,0003..−0,18) | REJECTED | `salida/INFORME.md` |
| 11 | V9 (1 relleno por cierre, cancelar el mismo lado en otras monedas) | 4 instrumentos | 9.334 sim | ≈ placebo | REJECTED | `V9_V3_INFORME.md` |
| 12 | @mo-money «pares» | on-chain 10 d | — | pares −15,85 k$, dirección +26,3 k$; alts 17-22: 12-20 % ambos lados, coste par med 1,145 | no es cosechador | `analisis_mo_money_pares_5m.py`, `datos/an_wallets.txt` |
| 13 | @flippingsharks «maker de pares» | on-chain/activity | 9 d | solo 32 % con 2.ª pata; ≈0 trading + rebates | no es cosechador | `wallets_18oct/informe.md` |
| 14 | H39 MM-REPOSO (ambos lados en continuo, clips 5, tope inventario) | — | — | sin correr: simulador maker NO_REPRODUCE | PENDING/BLOCKED | `REGISTRO_HIPOTESIS.md` H39 |
| 15 | **ESTE INFORME**: pata contraria sobre rellenos de B (HT0, HTc×3, HTs×3, HM×3 + OPT) | B real + población DESC/TEST | 166 / 3.094+2.583 | §2 | **REJECTED** | `datos/an_hedge.txt` |

## 2. Cuánto aporta la pata contraria en B (Parte A del PREREG; `scripts/hedge.py`, `scripts/an_hedge.py` → `datos/an_hedge.txt`)
Unidades: B real = 166 posiciones con hora de detección (20-22 Oct hasta ~12Z; 9 sin t_det = missing); población = primer relleno tipo B por mercado-lado de OTROS,
ETH/SOL/XRP 5m 0,10-0,30, T 65-295 s, 5 acc, t_ref = print + 0,5 s (DESC 17-19: 3.094 u.; TEST 20-22: 2.583 u.; 6 sin desenlace del 22 excluidas). Libro por
RECEPCIÓN (`salida/datos/ms_D.npz`). Tomador: envío t_ref+50 ms, casa al ask del contrario a +215 ms, +1c si no hay tamaño, comisión 0,07·a(1−a). Maker:
relleno solo con volumen que ATRAVIESA (CONS) o al precio (OPT, cota). EV = Σpnl/Σcoste de la pata barata; Δ emparejado contra mantener (H0).

| Política | B real Δ €/€ (IC90 día; cierre) | Pob. DESC Δ (IC90 día) | Pob. TEST Δ (IC90 día; cierre) | días+ TEST | sd por unidad (H0 1,83-2,23) |
|---|---|---|---|---|---|
| HT0 cubrir ya como tomador | −0,188 (−0,36,−0,01; −0,51,+0,10) | −0,055 (−0,09,−0,02) | **−0,169** (−0,20,−0,13; −0,23,−0,11) | 0/3 | 0,15-0,24 |
| HTc m=2/5/10c (cerrar el hueco solo con beneficio ≥m) | −0,190/−0,174/−0,157 | −0,059/−0,055/**−0,044** (elegida) | −0,148/−0,131/**−0,113** (−0,126,−0,095; −0,164,−0,058) | 0/3 | 0,5-0,8; se dispara en 53-76 % |
| HTs d=3/6/10c (stop: cubrir si el par se encarece) | −0,106/−0,079/**+0,048** (−0,02,+0,10; −0,13,+0,21) | −0,077/−0,060/−0,069 | −0,166/−0,148/−0,108 | 0/3 | 0,6-1,8 |
| HM m=0/2/4c (pujar el contrario) | −0,356/−0,312/−0,313 | −0,219/−0,225/−0,220 | −0,314/−0,301/−0,289 | 0/3 | 0,4-0,6; rellena 63-78 % |
| HM OPT (cota optimista de cola) | −0,327/−0,306/−0,275 | ≈−0,19 | −0,29..−0,27 | 0/3 | |
Base H0: B real +0,016 (IC90 día −0,15,+0,18); población DESC −0,030, TEST +0,079 (IC90 día +0,04,+0,10).
**Gate preregistrado:** mejor en DESC = HTc10 (Δ −0,044, ya negativa) → TEST −0,113 con IC90 <0 por día y por cierre. **FALLA → REJECTED.** HTs10 en B real (+0,048)
es la misma pista que «Binance ≥3 bps en contra» de `salida`: no replica en población (−0,108 TEST, IC90 <0). No hay placebo que hacer: ninguna política es positiva.

**Por qué (mecanismo medido):**
- El «hueco» en el instante útil: coste del par p + ask_contrario = **1,026** de media en B (detección real ~1,2 s tras el print) y **1,009** en población (+0,5 s);
  solo 8,4 % / 16,2 % de los rellenos permiten cerrar con par+comisión < 1. En los rellenos adversos el hueco ya es +4c (B) / +2c (pob.), en el resto +1c / 0.
- Cubrir como tomador = vender la pata al bid (misma cuenta; confirmado empíricamente en cosechar v2: `completado_tomador` = `salida`, −107,93 $ ambos).
  `salida` ya mostró que el bid tras el relleno es precio justo (acierto ≈ bid): cubrir solo paga medio spread + comisión (~0,02 $/acc ≈ 9-17 % del coste a p≈0,21).
- **¿El par convierte rellenos adversos en pérdida acotada sin matar el EV?** No. Descriptivo ex post: en los adversos (bid +5 s ≤ p−3c) HT0 pasa de −0,216 a −0,150
  (pob., +0,066, 4/6 días) y en B de −0,258 a −0,272; pero en el resto destruye el EV (pob. +0,165 → −0,048; B +0,310 → −0,065). Como ningún rasgo previo separa
  adversos de buenos (`salida` §4, `seleccion_adversa_plan` E1), el neto es −0,17/−0,19 por €. La cobertura parcial (fracción h) es una mezcla lineal: EV entre H0 y HT0, nunca mejor.
- Varianza: HT0 baja la sd por unidad de 1,8-2,2 a 0,15-0,24 y P(perder >50 % del coste) de 0,77 a 0,01-0,06. Es una palanca de CAPITAL que cuesta ~0,17 €/€:
  a escala B (~42 $/día de coste) ≈ −7 $/día seguros. No sirve ni para el problema de ruina de `tandas` (cambia ruina aleatoria por desangrado seguro).
- Viabilidad: tomador 215 ms (F1), sin necesidad de liquidar on-chain (ventaja sobre vender); pero 17/166 posiciones de B tienen <5 acc (parciales) y obligarían a
  sobrecubrir. Irrelevante: el EV ya es negativo antes de eso.

## 3. Ingeniería inversa de quien SÍ gana con pares (Parte B; `wallets_pares.py`, `an_wallets.py`, `diseccion.py`, `btc_cosechadores.py`)
Detalle y tablas en `GANADORES_PARES_PARA_COSECHAR.md`. Resumen:
- **BTC 17-21 Oct**: 0x21f4c1a1 sigue ganando **+1,21 %/vol** (931 k$, 4/5 días, par +6,1 % / residuo −4,7 %, 87 % maker, no reequilibra, inventario mediano 399 acc);
  0xaa1a4f31 −0,20 % (par +8,1 / residuo −8,3); 0x41e2e1cc −0,48 % (39 % maker). Ninguno de los dos primeros opera alts.
- **Alts (ETH/SOL/XRP) 17-22**: 63 «pareadoras» elegidas por conducta en 17-19 → TEST **+0,03 %/vol** IC90 días (−0,49 %,+0,79 %) frente a −1,20 % del placebo direccional:
  el par gana +5,6 % y la pata suelta lo devuelve (−4,7 %). **La pata suelta pierde en todas**: gana 28,7 % frente a un precio pagado de 34,9 %.
  0x41e2 en alts es tomador puro: margen de par +3-5 % comido por −3 % de comisión (≈0).
- **Cómo evitan la pata suelta las que mejor lo hacen** (0xf074dc84, 0x0ab01745; ETH, 100 % maker, elegidas viendo el TEST → EXPLORATORY): no la evitan con una
  cobertura posterior, la **acotan antes**: clips de 5 acc, 10-15 rellenos/mercado durante toda la ventana a 0,3-0,5, inventario máximo mediano 14-18 acc,
  **reequilibrado activo** (P(siguiente relleno reduce el desequilibrio) 0,64/0,55 frente a 0,43-0,48 de las que no), coste de par 0,965-0,975 (margen pequeño),
  residuo final 8-13 % de las acciones; 0xf074 va DELANTE en la cola (primero en el 70 % de los niveles compartidos). PnL +0,85..+1,5 %/vol sin rebate.
- **¿Replicable por nosotros?** Lo que hacen es H39 (MM en ambos lados en continuo), no una variante de B: B entra en 0,10-0,30, donde el «par» es longshot+favorito y no
  hay oscilación que recoger. Para H39 las incógnitas son la COLA (0xf074 va delante; nosotros, te→rx p50 38 / p90 161 ms + 50 ms de alta: sin medir) y el ritmo de
  órdenes (~15 rellenos y decenas de recotizaciones por mercado × 288 mercados/día). Capital pequeño (inventario ≤~30 acc ≈ 15 $). Escala: 0xf074 mueve ~14 k$/día en
  ETH; a +1 % serían ~50 k€/año **solo si igualáramos su cola**, y el simulador de maker no reproduce colas (BLOCKED). Por eso queda EXPLORATORY, no PROMISING.

## 4. Variables no exploradas que se desprenden (sin cosechar-al-abrir, que lleva otro agente)
1. **H39b «MM-INVENTARIO-ETH»** (nueva variante de H39 con el mecanismo de 0xf074/0x0ab0): asks/pujas en ambos lados de ETH 5m en continuo, clips 5, banda 0,30-0,70,
   tope |I| ≤15 acc, sesgo: retirar la cotización del lado que ya sobra (P(reduce) objetivo ≥0,6), T 290→50 s. Diferencia con H39: el reequilibrado y el tope son
   la regla, no un parámetro. **Bloqueo:** la cola. Prueba más barata y decisiva: la del propio H47 (micro-órdenes reales) en modo dos lados y tope 15 acc
   — requiere variante nueva + `/code-review` + OK de Javi; con el capital de hoy (5,12 $ sobre el suelo) solo valida maquinaria y posición en cola, no EV.
2. **Medir nuestra posición en cola con lo que ya hay**: rango de B en los niveles compartidos on-chain (método de `diseccion.py` sobre los 186 rellenos de B). Coste 0;
   dice si estamos delante (como 0xf074) o detrás (como 0xae68). Es el dato que bloquea H39/H39b.
3. Lo que NO merece cómputo: cobertura parcial (lineal), cobertura cruzada con otra moneda del mismo cierre (V9 ya ≈ placebo), cubrir en el 15m (no bloquea pago), pujar
   el favorito (sin edge), «completar cuando el hueco se abre» (HTc, §2).

## 5. Veredicto
- **Pares / rellenar el hueco / completar la pata suelta / cobertura parcial para B: REJECTED** (10 políticas preregistradas, B real + población DESC/TEST, 0/3 días
  positivos en test, IC90 <0). La pata contraria no mitiga la selección adversa de B: la cristaliza. Solo reduce varianza a un coste de ~0,17 €/€.
- Lo que gana en B sigue siendo lo mismo: rellenos en cola al precio (C3) y la prima del longshot en el nicho R2/R3 (`r3_escalado`); cualquier par recorta justo eso.
- Pares como ESTRATEGIA distinta (MM en continuo con inventario acotado): existe en población (0x21f4 BTC +1,2 %/vol; 0xf074/0x0ab0 ETH +1 %), pero el grupo de
  pareadoras en alts da ≈0 y el factor diferencial es cola + reequilibrado. **Siguiente:** (a) medir la cola real de B on-chain (coste 0, §4.2); (b) si B va delante,
  preregistrar H39b y pedir a Javi decidir si se prueba con micro-órdenes; si va detrás, cerrar pares también como estrategia salvo evidencia nueva.

## 6. Reproducir, ficheros, avisos
`nice -n 19 ionice -c3`, `ulimit -v 3000000`, desde /tmp:
`scripts/hedge.py b 2026-10-20 2026-10-21 2026-10-22` · `scripts/hedge.py pop 2026-10-17 … 2026-10-22` · `scripts/an_hedge.py` → `datos/an_hedge.txt` ·
`scripts/wallets_pares.py` (→ `datos/fills_alts.csv.gz`, `wm_ledger.csv.gz`) · `scripts/an_wallets.py` → `datos/an_wallets.txt` ·
`scripts/diseccion.py WALLET…` → `datos/diseccion_alts.txt` · `scripts/btc_cosechadores.py` → `datos/btc_cosech.txt`. Hashes en `HASHES.txt` (sha256).
Entradas sin modificar: `../salida/datos/{ms_D.npz,unidades_b.csv (sha 1cd186982212edac),desenlaces_extra.json}`, `../cola_vs_cruce/datos/{oc_D.csv.gz,tok_D.csv}`,
`/root/polymarket-research-datalogs/sa_ms/btc_ms_D.npz`, `VOL/m5_onchain/m5_onchain_D.csv.gz`, `maker_ms_desenlaces_cache.json`. Datos pesados en `datos/*.gz` (gitignored).
Avisos: B real son 3 días (n=166) y el 22-Oct parcial; la población usa la PRIMERA operación por mercado-lado (no la cola propia de B); el modelo tomador no simula
recotización en los 215 ms más allá del top; el maker CONS no tiene cola (los que van detrás rellenarían menos aún); rebate no sumado (0 $ cobrados por B);
on-chain con hora de bloque (~2,4 s tras el casado); los casos 0xf074/0x0ab0/0x43e7/0x31393 se eligieron viendo el TEST; la persistencia del grupo no es significativa.
Durante el trabajo un bucle de espera mío usó `pgrep -f` con su propio patrón (trampa conocida) y se esperó a sí mismo; lo maté por PID (no afectó a ningún proceso del sistema).
