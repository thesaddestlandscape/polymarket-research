# Identificacion H1a/H1b y SOLO (17-Nov) - diseno, coste 0, sin ordenes
Reloj: sa_ms/ex (passT_v3); latencia solo paquete_l B2,B3,B5 13-Nov, por clase de suelo lo/hi. Desenlace oficial.
## H1a vs H1b
H1b = nuestra orden ATRAE el golpe. Un virtual NO atrae (no toca el libro) => sus golpes = contrafactual limpio.
Diseno: mismos criterios de colocacion de B (coin x L x T x tam) aplicados como VIRTUAL en dias SIN orden real (24-Oct..17-Nov, registro ms) vs B real 20-23 Oct (n=1.942 eventos brazo B, P500=0,108).
Fuentes: ordenes_b.csv (reales, 20-23 Oct: 405/1121/1746/524), maker_ms_* 19-Oct..17-Nov (libro+cinta ms), cxb60_dryrun dec_* (virtuales CXB60/GEO1 desde 12-Nov; no son el mismo momento que B).
Contraste: P(golpe<=500ms | virtual) vs P(...| B real), emparejado por dia-bloque, coin, L, T, suelo lo/hi; IC90 por mercado/cierre. Igual>=> H1a; B>virtual => H1b.
Cautela: tape 20-23 Oct contiene prints propios; excluir mercados con orden propia en el brazo noB (ya hecho en f3).
## SOLO 89 + SOLO_ARRIBA 25
Falta: intencion/limite del tomador y su alternativa contrafactual (habria pegado a un bid mas bajo o no habria operado). Con on-chain solo se ve lo ejecutado; no el limite. Solo parcialmente: tomador por tx/wallet (tomadores.pkl, 215 ordenes) y su comportamiento en otros mercados (keep_onchain_re_as_b: 44 ficheros desde 26-Oct).
Recopilable YA: perfil historico de esas wallets tomadoras (limite tipico vs mejor bid, cuantas veces barren varios niveles) -> NO ejecutado aqui.
Logger nuevo (solo diseno): no hace falta si se usa virtual GEO1/CXB60 como contrafactual del evento; si se quiere el limite del tomador: gz, retencion 30 d, fuera de git, via libro_estado_ws trades(ex,rx).
