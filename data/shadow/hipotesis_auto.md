# Hipótesis automáticas — 2026-09-18 01:51 UTC
_Generado por shadow_postmortem.py sobre 489745 resoluciones (PNL=+52897.74€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.505` → IC=-0.152 (n=202)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.248 (n=442)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.122 (n=413)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.248 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.122)

- **PATRÓN** `n_total_lado` > `76.0` → IC=+0.214 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 76.0 (IC base=+0.122)

- **PATRÓN** `banda_hit_calibrado` > `0.803` → IC=+0.259 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.803 (IC base=+0.122)

- **PATRÓN** `banda_z` > `10.241` → IC=+0.224 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 10.241 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.139 (n=336)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 11.0 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=513)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.122)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.122 (n=413)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.495 (IC base=+0.039)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.134 (n=162)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.255 (n=341)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=289)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=314)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.255 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.130)

- **PATRÓN** `n_total_lado` > `73.0` → IC=+0.218 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 73.0 (IC base=+0.130)

- **PATRÓN** `banda_hit_calibrado` > `0.624` → IC=+0.269 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.624 (IC base=+0.130)

- **PATRÓN** `banda_z` > `11.377` → IC=+0.250 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.377 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.152 (n=271)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 11.0 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=428)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `88.0` → IC=+0.144 (n=71)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 88.0 (IC base=+0.034)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.515` → IC=-0.204 (n=42)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.253 (n=87)

- **FILTRO** `py_entrada` > `0.845` → IC=-0.393 (n=26)

  - _Acción_: SKIP cuando `py_entrada` > 0.845
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=87)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.190 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=86)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=97)

- **PATRÓN** `py_entrada` > `0.515` → IC=+0.253 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.103)

- **PATRÓN** `banda_hit_calibrado` > `0.6284` → IC=+0.230 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6284 (IC base=+0.103)

- **PATRÓN** `banda_z` > `6.043` → IC=+0.172 (n=65)

  - _Acción_: Kelly boost +0.86€ cuando `banda_z` > 6.043 (IC base=+0.103)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.157 (n=103)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.02 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `1185.8848` → IC=+0.142 (n=65)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 1185.8848 (IC base=+0.103)

### BALLENAS_CONFIRMADAS_15M#XRP#15min
- **PATRÓN** `n_total_lado` > `38.0` → IC=+0.250 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 38.0 (IC base=+0.194)

- **PATRÓN** `banda_hit_calibrado` > `0.5987` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `banda_hit_calibrado` > 0.5987 (IC base=+0.194)

- **PATRÓN** `banda_z` > `3.283` → IC=+0.231 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 3.283 (IC base=+0.194)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.729` → IC=+0.188 (n=30)

  - _Acción_: Kelly boost +0.94€ cuando `ballenas_wallet_edge_medio` > 0.729 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.278 (n=25)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.01 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `2518.5859` → IC=+0.294 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2518.5859 (IC base=+0.194)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `144.22` → IC=-0.249 (n=6025)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 144.22
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=18076)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `141.1` → IC=-0.261 (n=831)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 141.1
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=2495)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` < `492.88` → IC=-0.157 (n=319)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 492.88
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=957)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `132.71` → IC=-0.295 (n=733)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 132.71
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=2202)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `159.03` → IC=-0.241 (n=1428)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 159.03
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=4285)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `117.99` → IC=-0.367 (n=1169)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 117.99
  - _Potencial_: sin este filtro IC_bueno=-0.108 (n=3508)

### CANDIDATA9_BOT_CONSENSO
- **FILTRO** `py_entrada` < `0.47` → IC=-0.244 (n=287)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=325)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.162 (n=140)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=446)

### CANDIDATA9_BOT_CONSENSO#BTC#5min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.252 (n=147)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=167)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.186 (n=68)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=220)

### CANDIDATA9_BOT_CONSENSO#ETH#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.253 (n=91)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=55)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.173 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=118)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.198 (n=12132)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.69 (IC base=+0.097)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=3030)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `5339.6996` → IC=+0.171 (n=1933)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 5339.6996 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.145 (n=9581)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 17.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.143 (n=11301)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 7.0 (IC base=+0.135)

- **PATRÓN** `py_entrada` < `0.345` → IC=+0.246 (n=8329)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.345 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.180 (n=5007)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `1657.3138` → IC=+0.163 (n=5647)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 1657.3138 (IC base=+0.135)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.210 (n=1445)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.203 (n=1416)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.351 (n=648)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.203 (n=1781)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `15335.1325` → IC=+0.227 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15335.1325 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.208 (n=1310)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.210 (n=1435)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` < `0.365` → IC=+0.273 (n=1256)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.365 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=1845)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `13438.2681` → IC=+0.221 (n=647)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13438.2681 (IC base=+0.203)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.62` → IC=+0.175 (n=284)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` > 0.62 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `4641.025` → IC=+0.148 (n=231)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 4641.025 (IC base=+0.101)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.174 (n=299)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 7.0 (IC base=+0.128)

- **PATRÓN** `py_entrada` < `0.435` → IC=+0.153 (n=682)

  - _Acción_: Kelly boost +0.77€ cuando `py_entrada` < 0.435 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.133 (n=549)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `3855.8996` → IC=+0.149 (n=425)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 3855.8996 (IC base=+0.128)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.146 (n=2432)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.139 (n=2065)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 15.0 (IC base=+0.138)

- **PATRÓN** `py_entrada` > `0.7` → IC=+0.328 (n=819)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.7 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.248 (n=1105)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.241)

- **PATRÓN** `py_entrada` < `0.305` → IC=+0.331 (n=818)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.305 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.248 (n=1282)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `3755.7636` → IC=+0.246 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3755.7636 (IC base=+0.241)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.133 (n=396)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 11.0 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.135 (n=565)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 17.0 (IC base=+0.130)

- **PATRÓN** `py_entrada` > `0.665` → IC=+0.228 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.665 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.137 (n=654)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.02 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `1910.5447` → IC=+0.159 (n=376)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 1910.5447 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.167 (n=148)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.077)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.225 (n=533)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.427 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.178 (n=987)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 7.0 (IC base=+0.172)

- **PATRÓN** `py_entrada` < `0.355` → IC=+0.269 (n=741)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.355 (IC base=+0.172)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.176 (n=1144)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.03 (IC base=+0.172)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.182 (n=309)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 6.0 (IC base=+0.170)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.172 (n=205)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 13.0 (IC base=+0.170)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.359 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.170)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.179 (n=182)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.02 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.135 (n=708)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 7.0 (IC base=+0.118)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.222 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.118)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.133 (n=336)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.02 (IC base=+0.118)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.8` → IC=-0.333 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=129)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=9603)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.199 (n=9166)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 17.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.223 (n=3361)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.339 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `8491.3442` → IC=+0.341 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8491.3442 (IC base=+0.197)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.176 (n=2271)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 17.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.178 (n=2375)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.74 (IC base=+0.168)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **FILTRO** `py_entrada` < `0.775` → IC=-0.284 (n=49)

  - _Acción_: SKIP cuando `py_entrada` < 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=63)

- **FILTRO** `libro_liquidez` < `9614.35` → IC=-0.328 (n=56)

  - _Acción_: SKIP cuando `libro_liquidez` < 9614.35
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=56)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.300 (n=233)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.267)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.271 (n=177)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.267)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.358 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.267)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.184 (n=2217)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 6.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.182 (n=2228)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 17.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.187 (n=1989)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.179)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.245 (n=2091)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.236)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.324 (n=702)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.321 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.236)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min
- **FILTRO** `hora_utc` < `18.0` → IC=-0.217 (n=58)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=20)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.250 (n=38)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=40)

- **FILTRO** `py_entrada` > `0.755` → IC=-0.267 (n=58)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=20)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.199 (n=2269)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.193 (n=1942)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.196 (n=1635)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.71 (IC base=+0.191)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.441 (n=385)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.434)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.435 (n=384)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.434)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.445 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.434)

- **PATRÓN** `libro_liquidez` > `2060.1801` → IC=+0.442 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2060.1801 (IC base=+0.434)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.436 (n=171)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.437)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.440 (n=115)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.437)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.457 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.437)

- **PATRÓN** `libro_liquidez` > `12599.6821` → IC=+0.446 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12599.6821 (IC base=+0.437)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.453 (n=148)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.465 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.441)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.439 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.441)

- **PATRÓN** `libro_liquidez` > `3244.9992` → IC=+0.437 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3244.9992 (IC base=+0.441)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.412 (n=89)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.408)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.402 (n=100)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.408)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.402 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.408)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.416 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.408)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=22)

- **FILTRO** `libro_liquidez` < `6836.9618` → IC=-0.333 (n=28)

  - _Acción_: SKIP cuando `libro_liquidez` < 6836.9618
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.198 (n=28522)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 8.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.238 (n=10767)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.196)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.171 (n=5816)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 5.0 (IC base=+0.171)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.176 (n=4892)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 15.0 (IC base=+0.171)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.187 (n=5276)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.171)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=5080)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.225 (n=5051)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.275 (n=1816)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.179 (n=2760)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 15.0 (IC base=+0.171)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.186 (n=5245)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.171)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` > `0.775` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.232 (n=2569)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.220 (n=1924)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.264 (n=1789)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.218)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.209 (n=4716)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.205)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.255 (n=2387)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.205)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.193 (n=4770)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 8.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.191 (n=4714)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.249 (n=1881)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.191)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.205 (n=4351)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.124)

- **PATRÓN** `restante_min` < `4.08` → IC=+0.134 (n=3978)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` < 4.08 (IC base=+0.124)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.151 (n=4028)

  - _Acción_: Kelly boost +0.76€ cuando `restante_min` > 4.95 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.137 (n=5869)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 8.0 (IC base=+0.124)

- **PATRÓN** `lag_apertura_s` < `3.27` → IC=+0.151 (n=3975)

  - _Acción_: Kelly boost +0.75€ cuando `lag_apertura_s` < 3.27 (IC base=+0.124)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.206 (n=2195)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.128)

- **PATRÓN** `restante_min` < `4.02` → IC=+0.136 (n=1980)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` < 4.02 (IC base=+0.128)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.148 (n=1973)

  - _Acción_: Kelly boost +0.74€ cuando `restante_min` > 4.94 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.143 (n=2900)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 8.0 (IC base=+0.128)

- **PATRÓN** `lag_apertura_s` < `3.88` → IC=+0.149 (n=1970)

  - _Acción_: Kelly boost +0.74€ cuando `lag_apertura_s` < 3.88 (IC base=+0.128)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.203 (n=2156)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.120)

- **PATRÓN** `restante_min` < `4.48` → IC=+0.126 (n=2648)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.48 (IC base=+0.120)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.149 (n=2070)

  - _Acción_: Kelly boost +0.74€ cuando `restante_min` > 4.96 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.125 (n=2000)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 18.0 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.130 (n=2969)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 8.0 (IC base=+0.120)

- **PATRÓN** `lag_apertura_s` < `2.45` → IC=+0.149 (n=2001)

  - _Acción_: Kelly boost +0.75€ cuando `lag_apertura_s` < 2.45 (IC base=+0.120)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.297 (n=1023)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.285)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.380 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `1604.6829` → IC=+0.293 (n=963)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1604.6829 (IC base=+0.285)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.288 (n=300)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.266)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.330 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.266)

- **PATRÓN** `libro_liquidez` > `4237.6328` → IC=+0.284 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4237.6328 (IC base=+0.266)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.328 (n=324)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.293)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.391 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `1492.929` → IC=+0.316 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1492.929 (IC base=+0.293)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.342 (n=80)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.335)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.361 (n=70)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.335)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.377 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.335)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.346 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.335)

- **PATRÓN** `libro_liquidez` > `761.0655` → IC=+0.371 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 761.0655 (IC base=+0.335)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.442 (n=447)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.432)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.439 (n=377)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.432)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.437 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.432)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.439 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.432)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.434 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.432)

- **PATRÓN** `libro_liquidez` > `1860.5823` → IC=+0.439 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1860.5823 (IC base=+0.432)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.441 (n=202)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.432)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.441 (n=201)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.432)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.440 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.432)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.432)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.439 (n=196)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.448 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.435)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.436 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.435)

- **PATRÓN** `libro_liquidez` > `2089.6231` → IC=+0.456 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2089.6231 (IC base=+0.435)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` > `12.0` → IC=+0.375 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.378)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.303 (n=201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.257)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.298 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.268 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `1376.3842` → IC=+0.285 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1376.3842 (IC base=+0.257)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.303 (n=201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.257)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.298 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.268 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `1376.3842` → IC=+0.285 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1376.3842 (IC base=+0.257)

### GBM_LATE_15M
- **PATRÓN** `ibs_20min` > `0.4985` → IC=+0.157 (n=5836)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` > 0.4985 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` < `0.1432` → IC=+0.247 (n=1302)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1432 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.835` → IC=+0.168 (n=2531)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 5.835 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` < `1.2208` → IC=+0.244 (n=1676)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2208 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` > `1.0665` → IC=+0.240 (n=760)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0665 (IC base=+0.098)

- **PATRÓN** `volumen_pendiente_norm` > `0.308` → IC=+0.207 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.308 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` > `1.9163` → IC=+0.200 (n=2892)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9163 (IC base=+0.098)

- **PATRÓN** `ibs_20min` < `0.5701` → IC=+0.132 (n=7977)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.5701 (IC base=+0.061)

- **PATRÓN** `dist_vwap_pct` > `0.5519` → IC=+0.184 (n=483)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.5519 (IC base=+0.061)

- **PATRÓN** `dist_vwap_pct` < `0.1359` → IC=+0.171 (n=2485)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.1359 (IC base=+0.061)

- **PATRÓN** `volumen_regimen` < `0.7009` → IC=+0.175 (n=1164)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.7009 (IC base=+0.061)

- **PATRÓN** `volumen_regimen` > `0.8714` → IC=+0.178 (n=1763)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 0.8714 (IC base=+0.061)

- **PATRÓN** `volumen_pendiente_norm` > `0.1674` → IC=+0.220 (n=1285)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1674 (IC base=+0.061)

- **PATRÓN** `volumen_spike_ratio` > `1.5869` → IC=+0.201 (n=3925)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5869 (IC base=+0.061)

- **PATRÓN** `ballena_activa_n` < `152.0` → IC=+0.211 (n=4164)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 152.0 (IC base=+0.061)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.183 (n=496)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0049 (IC base=+0.163)

- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.180 (n=492)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0079 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.3275` → IC=+0.163 (n=1477)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.3275 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.166 (n=729)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.163)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.186 (n=553)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 6.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.269 (n=569)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.977` → IC=+0.275 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.977 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.211 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` > `1.4306` → IC=+0.164 (n=1363)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.4306 (IC base=+0.163)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.184 (n=1398)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.04 (IC base=+0.163)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.249 (n=973)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.0883` → IC=+0.292 (n=364)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0883 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.249 (n=747)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` < `0.0583` → IC=+0.290 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0583 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.34` → IC=+0.247 (n=1135)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.34 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` < `0.092` → IC=+0.231 (n=915)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.092 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.2799` → IC=+0.262 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2799 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.6495` → IC=+0.255 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6495 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.235 (n=1135)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `1748.06` → IC=+0.251 (n=725)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1748.06 (IC base=+0.233)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.224 (n=980)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.1151` → IC=+0.246 (n=491)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1151 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.227 (n=1168)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `0.9149` → IC=+0.255 (n=505)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9149 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` > `0.1838` → IC=+0.214 (n=565)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1838 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` < `0.1267` → IC=+0.215 (n=861)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1267 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.762` → IC=+0.231 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.762 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` < `1.2558` → IC=+0.223 (n=1114)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2558 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` > `0.8751` → IC=+0.214 (n=742)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8751 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` < `0.1609` → IC=+0.213 (n=1132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1609 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.212 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` < `1.4011` → IC=+0.223 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4011 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `2.3728` → IC=+0.225 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3728 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `11012.3723` → IC=+0.222 (n=1113)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11012.3723 (IC base=+0.213)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.156 (n=1050)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0049 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.0753` → IC=+0.154 (n=400)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.0753 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.165 (n=404)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 18.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.6747` → IC=+0.175 (n=1192)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.6747 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` < `0.123` → IC=+0.151 (n=1092)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.123 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.426` → IC=+0.167 (n=202)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 11.426 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `1.2116` → IC=+0.147 (n=1192)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.2116 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `0.6183` → IC=+0.140 (n=1192)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 0.6183 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.1564` → IC=+0.180 (n=323)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.1564 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.4376` → IC=+0.152 (n=1083)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4376 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.4262` → IC=+0.143 (n=1083)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.4262 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `13573.7607` → IC=+0.151 (n=795)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 13573.7607 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `242.0` → IC=+0.161 (n=440)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 242.0 (IC base=+0.139)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.192 (n=1441)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0059 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.185 (n=718)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 15.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.190 (n=550)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 6.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.257 (n=562)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.502` → IC=+0.231 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.502 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` < `0.1059` → IC=+0.185 (n=1228)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` < 0.1059 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.3741` → IC=+0.184 (n=188)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.3741 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `2.9896` → IC=+0.200 (n=614)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9896 (IC base=+0.179)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.191 (n=1665)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.04 (IC base=+0.179)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.226 (n=1234)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.246 (n=412)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` < `0.3822` → IC=+0.234 (n=1086)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3822 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.695` → IC=+0.233 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.695 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.323` → IC=+0.218 (n=1354)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.323 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.3649` → IC=+0.266 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3649 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` < `1.846` → IC=+0.205 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.846 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` > `2.3042` → IC=+0.224 (n=738)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3042 (IC base=+0.216)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.229 (n=695)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `1899.5579` → IC=+0.237 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1899.5579 (IC base=+0.216)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.224 (n=711)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 27.0 (IC base=+0.216)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.152 (n=90)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=1827)

- **PATRÓN** `ibs_20min` > `0.9343` → IC=+0.178 (n=299)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.9343 (IC base=+0.008)

- **PATRÓN** `dist_vwap_pct` > `0.328` → IC=+0.337 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.328 (IC base=+0.008)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.401` → IC=+0.134 (n=566)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 4.401 (IC base=+0.008)

- **PATRÓN** `volumen_regimen` < `0.6587` → IC=+0.341 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6587 (IC base=+0.008)

- **PATRÓN** `volumen_regimen` > `1.1953` → IC=+0.354 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1953 (IC base=+0.008)

- **PATRÓN** `volumen_pendiente_norm` > `0.2908` → IC=+0.361 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2908 (IC base=+0.008)

- **PATRÓN** `volumen_spike_ratio` < `1.4943` → IC=+0.335 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4943 (IC base=+0.008)

- **PATRÓN** `volumen_spike_ratio` > `1.8189` → IC=+0.339 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8189 (IC base=+0.008)

- **PATRÓN** `ballena_activa_n` < `163.0` → IC=+0.342 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 163.0 (IC base=+0.008)

- **PATRÓN** `dist_vwap_pct` > `0.1648` → IC=+0.191 (n=221)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1648 (IC base=+0.008)

- **PATRÓN** `volumen_regimen` < `0.695` → IC=+0.164 (n=272)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.695 (IC base=+0.008)

- **PATRÓN** `volumen_pendiente_norm` > `0.2684` → IC=+0.232 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2684 (IC base=+0.008)

- **PATRÓN** `volumen_spike_ratio` > `1.5051` → IC=+0.189 (n=506)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 1.5051 (IC base=+0.008)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.154 (n=53)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=261)

- **FILTRO** `ibs_20min` < `0.375` → IC=-0.173 (n=102)

  - _Acción_: SKIP cuando `ibs_20min` < 0.375
  - _Potencial_: sin este filtro IC_bueno=+0.145 (n=212)

- **FILTRO** `ibs_20min` > `0.2717` → IC=-0.128 (n=1826)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2717
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=900)

- **FILTRO** `sigma_ewma_delta_pct` > `8.618` → IC=-0.210 (n=301)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.618
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=2425)

- **PATRÓN** `ibs_20min` > `0.7576` → IC=+0.206 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7576 (IC base=+0.041)

- **PATRÓN** `dist_vwap_pct` > `0.9797` → IC=+0.265 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9797 (IC base=+0.041)

- **PATRÓN** `dist_vwap_pct` < `0.6368` → IC=+0.292 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6368 (IC base=+0.041)

- **PATRÓN** `volumen_regimen` > `0.7957` → IC=+0.320 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7957 (IC base=+0.041)

- **PATRÓN** `volumen_pendiente_norm` < `0.0735` → IC=+0.320 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0735 (IC base=+0.041)

- **PATRÓN** `volumen_spike_ratio` < `1.8428` → IC=+0.303 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8428 (IC base=+0.041)

- **PATRÓN** `volumen_spike_ratio` > `1.449` → IC=+0.267 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.449 (IC base=+0.041)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.318 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 47.0 (IC base=+0.041)

- **PATRÓN** `dist_vwap_pct` > `0.7032` → IC=+0.321 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7032 (IC base=-0.046)

- **PATRÓN** `volumen_regimen` < `1.1047` → IC=+0.210 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1047 (IC base=-0.046)

- **PATRÓN** `volumen_regimen` > `0.9038` → IC=+0.194 (n=171)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` > 0.9038 (IC base=-0.046)

- **PATRÓN** `volumen_pendiente_norm` < `0.1972` → IC=+0.219 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1972 (IC base=-0.046)

- **PATRÓN** `volumen_pendiente_norm` > `0.0844` → IC=+0.230 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0844 (IC base=-0.046)

- **PATRÓN** `volumen_spike_ratio` < `2.4353` → IC=+0.254 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4353 (IC base=-0.046)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6598` → IC=-0.191 (n=458)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6598
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=1375)

- **FILTRO** `ibs_20min` < `0.6679` → IC=-0.161 (n=1209)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6679
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=624)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.196 (n=383)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=1450)

- **FILTRO** `ibs_20min` > `0.775` → IC=-0.200 (n=688)

  - _Acción_: SKIP cuando `ibs_20min` > 0.775
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=2072)

- **PATRÓN** `dist_vwap_pct` > `0.9637` → IC=+0.329 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9637 (IC base=-0.082)

- **PATRÓN** `dist_vwap_pct` < `0.2396` → IC=+0.313 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2396 (IC base=-0.082)

- **PATRÓN** `volumen_regimen` < `1.0034` → IC=+0.276 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0034 (IC base=-0.082)

- **PATRÓN** `volumen_regimen` > `0.616` → IC=+0.291 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.616 (IC base=-0.082)

- **PATRÓN** `volumen_pendiente_norm` > `0.0744` → IC=+0.300 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0744 (IC base=-0.082)

- **PATRÓN** `volumen_spike_ratio` > `1.8324` → IC=+0.290 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8324 (IC base=-0.082)

- **PATRÓN** `dist_vwap_pct` > `0.9919` → IC=+0.278 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9919 (IC base=-0.025)

- **PATRÓN** `dist_vwap_pct` < `0.2575` → IC=+0.250 (n=597)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2575 (IC base=-0.025)

- **PATRÓN** `volumen_regimen` < `0.7351` → IC=+0.251 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7351 (IC base=-0.025)

- **PATRÓN** `volumen_regimen` > `1.0826` → IC=+0.292 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0826 (IC base=-0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.1058` → IC=+0.272 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1058 (IC base=-0.025)

- **PATRÓN** `volumen_spike_ratio` < `2.224` → IC=+0.262 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.224 (IC base=-0.025)

- **PATRÓN** `volumen_spike_ratio` > `1.4747` → IC=+0.246 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4747 (IC base=-0.025)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.249 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=-0.025)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.182 (n=2721)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0093 (IC base=+0.089)

- **PATRÓN** `ibs_20min` > `0.4579` → IC=+0.179 (n=7281)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.4579 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` > `0.694` → IC=+0.279 (n=755)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.694 (IC base=+0.089)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.503` → IC=+0.147 (n=3859)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 3.503 (IC base=+0.089)

- **PATRÓN** `volumen_regimen` > `0.6784` → IC=+0.239 (n=2488)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6784 (IC base=+0.089)

- **PATRÓN** `volumen_pendiente_norm` > `0.2464` → IC=+0.261 (n=881)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2464 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` < `1.4778` → IC=+0.246 (n=1488)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4778 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` > `2.7529` → IC=+0.239 (n=1486)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7529 (IC base=+0.089)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.278 (n=3951)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.089)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.141 (n=2761)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` > 0.0086 (IC base=+0.070)

- **PATRÓN** `ibs_20min` < `0.554` → IC=+0.151 (n=7278)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.554 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.6674` → IC=+0.245 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6674 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` < `0.1626` → IC=+0.234 (n=2145)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1626 (IC base=+0.070)

- **PATRÓN** `volumen_regimen` < `0.715` → IC=+0.236 (n=1014)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.715 (IC base=+0.070)

- **PATRÓN** `volumen_regimen` > `1.1993` → IC=+0.253 (n=768)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1993 (IC base=+0.070)

- **PATRÓN** `volumen_pendiente_norm` > `0.2507` → IC=+0.316 (n=605)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2507 (IC base=+0.070)

- **PATRÓN** `volumen_spike_ratio` < `1.4931` → IC=+0.251 (n=999)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4931 (IC base=+0.070)

- **PATRÓN** `volumen_spike_ratio` > `2.37` → IC=+0.257 (n=1358)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.37 (IC base=+0.070)

- **PATRÓN** `ballena_activa_n` < `79.0` → IC=+0.259 (n=2859)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 79.0 (IC base=+0.070)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `sigma_ewma_delta_pct` > `4.264` → IC=-0.166 (n=420)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.264
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=1404)

- **PATRÓN** `ibs_20min` > `0.8745` → IC=+0.259 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8745 (IC base=+0.042)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.281` → IC=+0.153 (n=758)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 3.281 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.2248` → IC=+0.303 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2248 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` < `1.4419` → IC=+0.208 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4419 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` > `2.6094` → IC=+0.206 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6094 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` < `0.1845` → IC=+0.475 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1845 (IC base=-0.023)

- **PATRÓN** `volumen_spike_ratio` < `1.4415` → IC=+0.455 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4415 (IC base=-0.023)

- **PATRÓN** `volumen_spike_ratio` > `2.2378` → IC=+0.455 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2378 (IC base=-0.023)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` > `0.8203` → IC=-0.144 (n=607)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8203
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=1823)

- **PATRÓN** `dist_vwap_pct` > `0.1104` → IC=+0.140 (n=378)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.1104 (IC base=+0.013)

- **PATRÓN** `dist_vwap_pct` < `0.1571` → IC=+0.137 (n=618)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.1571 (IC base=+0.013)

- **PATRÓN** `volumen_regimen` > `0.85` → IC=+0.149 (n=479)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 0.85 (IC base=+0.013)

- **PATRÓN** `volumen_pendiente_norm` > `0.2725` → IC=+0.181 (n=92)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2725 (IC base=+0.013)

- **PATRÓN** `volumen_spike_ratio` < `1.4247` → IC=+0.185 (n=233)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 1.4247 (IC base=+0.013)

- **PATRÓN** `ballena_activa_n` < `229.0` → IC=+0.191 (n=231)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 229.0 (IC base=+0.013)

- **PATRÓN** `dist_vwap_pct` < `0.1458` → IC=+0.211 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1458 (IC base=+0.002)

- **PATRÓN** `volumen_regimen` > `0.5933` → IC=+0.206 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5933 (IC base=+0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.2799` → IC=+0.304 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2799 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` < `1.8118` → IC=+0.209 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8118 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` > `2.1868` → IC=+0.230 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1868 (IC base=+0.002)

- **PATRÓN** `ballena_activa_n` < `489.0` → IC=+0.214 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 489.0 (IC base=+0.002)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0074` → IC=+0.286 (n=866)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0074 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.0991` → IC=+0.245 (n=433)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0991 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.246 (n=656)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.240)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.254 (n=485)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.297 (n=668)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.827` → IC=+0.280 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.827 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` < `0.11` → IC=+0.256 (n=1092)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.11 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `1.8725` → IC=+0.244 (n=533)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8725 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `3.5945` → IC=+0.256 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.5945 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.257 (n=1483)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `1911.6981` → IC=+0.242 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1911.6981 (IC base=+0.240)

- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.299 (n=1032)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0055 (IC base=+0.281)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.317 (n=354)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.281)

- **PATRÓN** `ibs_20min` < `0.3333` → IC=+0.286 (n=1030)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3333 (IC base=+0.281)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.883` → IC=+0.298 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.883 (IC base=+0.281)

- **PATRÓN** `volumen_pendiente_norm` > `0.3459` → IC=+0.304 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3459 (IC base=+0.281)

- **PATRÓN** `volumen_spike_ratio` < `1.6355` → IC=+0.287 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6355 (IC base=+0.281)

- **PATRÓN** `volumen_spike_ratio` > `2.2184` → IC=+0.281 (n=623)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2184 (IC base=+0.281)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.290 (n=575)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.281)

- **PATRÓN** `libro_liquidez` > `1887.9956` → IC=+0.306 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1887.9956 (IC base=+0.281)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.279 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=+0.281)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` < `0.25` → IC=-0.213 (n=378)

  - _Acción_: SKIP cuando `ibs_20min` < 0.25
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=1138)

- **FILTRO** `ibs_20min` > `0.7987` → IC=-0.182 (n=489)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7987
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=1468)

- **PATRÓN** `ibs_20min` > `0.8036` → IC=+0.152 (n=516)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.8036 (IC base=-0.009)

- **PATRÓN** `dist_vwap_pct` > `0.4377` → IC=+0.209 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4377 (IC base=-0.009)

- **PATRÓN** `dist_vwap_pct` < `0.1802` → IC=+0.195 (n=283)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.1802 (IC base=-0.009)

- **PATRÓN** `volumen_regimen` < `0.956` → IC=+0.220 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.956 (IC base=-0.009)

- **PATRÓN** `volumen_regimen` > `0.6225` → IC=+0.197 (n=328)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` > 0.6225 (IC base=-0.009)

- **PATRÓN** `volumen_pendiente_norm` > `0.2647` → IC=+0.305 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2647 (IC base=-0.009)

- **PATRÓN** `volumen_spike_ratio` < `2.0696` → IC=+0.241 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0696 (IC base=-0.009)

- **PATRÓN** `volumen_spike_ratio` > `1.3739` → IC=+0.221 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.3739 (IC base=-0.009)

- **PATRÓN** `ballena_activa_n` < `109.0` → IC=+0.265 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 109.0 (IC base=-0.009)

- **PATRÓN** `dist_vwap_pct` > `0.122` → IC=+0.213 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.122 (IC base=-0.011)

- **PATRÓN** `volumen_regimen` < `0.6651` → IC=+0.188 (n=91)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.6651 (IC base=-0.011)

- **PATRÓN** `volumen_regimen` > `0.7255` → IC=+0.189 (n=242)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` > 0.7255 (IC base=-0.011)

- **PATRÓN** `volumen_pendiente_norm` > `0.1505` → IC=+0.309 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1505 (IC base=-0.011)

- **PATRÓN** `volumen_spike_ratio` < `1.7947` → IC=+0.248 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7947 (IC base=-0.011)

- **PATRÓN** `volumen_spike_ratio` > `2.4256` → IC=+0.269 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4256 (IC base=-0.011)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.253 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 143.0 (IC base=-0.011)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.68` → IC=-0.214 (n=880)

  - _Acción_: SKIP cuando `ibs_20min` < 0.68
  - _Potencial_: sin este filtro IC_bueno=+0.264 (n=880)

- **FILTRO** `ibs_20min` > `0.7083` → IC=-0.232 (n=460)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7083
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=1383)

- **FILTRO** `sigma_ewma_delta_pct` > `4.627` → IC=-0.174 (n=427)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.627
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=1416)

- **PATRÓN** `ibs_20min` > `0.68` → IC=+0.264 (n=880)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.68 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` > `0.185` → IC=+0.312 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.185 (IC base=+0.025)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.399` → IC=+0.147 (n=273)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 9.399 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` < `0.8657` → IC=+0.292 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8657 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` > `0.636` → IC=+0.280 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.636 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` < `0.1055` → IC=+0.279 (n=568)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1055 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.2757` → IC=+0.337 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2757 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `1.4456` → IC=+0.316 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4456 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.319 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.025)

- **PATRÓN** `ibs_20min` < `0.1071` → IC=+0.200 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1071 (IC base=+0.005)

- **PATRÓN** `dist_vwap_pct` > `0.7726` → IC=+0.194 (n=60)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.7726 (IC base=+0.005)

- **PATRÓN** `dist_vwap_pct` < `0.3939` → IC=+0.196 (n=406)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.3939 (IC base=+0.005)

- **PATRÓN** `volumen_regimen` < `0.7148` → IC=+0.242 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7148 (IC base=+0.005)

- **PATRÓN** `volumen_pendiente_norm` < `0.1017` → IC=+0.192 (n=358)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.1017 (IC base=+0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2666` → IC=+0.202 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2666 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` < `2.5876` → IC=+0.207 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5876 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` > `1.4993` → IC=+0.188 (n=366)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 1.4993 (IC base=+0.005)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.219 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=+0.005)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0157` → IC=+0.322 (n=724)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0157 (IC base=+0.273)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.279 (n=1135)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.273)

- **PATRÓN** `ibs_20min` > `0.9048` → IC=+0.347 (n=723)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9048 (IC base=+0.273)

- **PATRÓN** `dist_vwap_pct` > `0.2672` → IC=+0.317 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2672 (IC base=+0.273)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.398` → IC=+0.300 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.398 (IC base=+0.273)

- **PATRÓN** `volumen_regimen` > `0.6873` → IC=+0.289 (n=969)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6873 (IC base=+0.273)

- **PATRÓN** `volumen_pendiente_norm` > `0.2876` → IC=+0.304 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2876 (IC base=+0.273)

- **PATRÓN** `volumen_spike_ratio` < `1.5463` → IC=+0.281 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5463 (IC base=+0.273)

- **PATRÓN** `volumen_spike_ratio` > `2.206` → IC=+0.282 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.206 (IC base=+0.273)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.276 (n=1129)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.273)

- **PATRÓN** `libro_liquidez` > `2432.1384` → IC=+0.283 (n=969)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2432.1384 (IC base=+0.273)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.272 (n=401)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0073 (IC base=+0.270)

- **PATRÓN** `sigma_h` > `0.0146` → IC=+0.297 (n=800)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0146 (IC base=+0.270)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.285 (n=603)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.270)

- **PATRÓN** `ibs_20min` < `0.3953` → IC=+0.306 (n=1201)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3953 (IC base=+0.270)

- **PATRÓN** `dist_vwap_pct` > `0.5341` → IC=+0.288 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5341 (IC base=+0.270)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.453` → IC=+0.291 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.453 (IC base=+0.270)

- **PATRÓN** `volumen_regimen` > `1.2432` → IC=+0.306 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2432 (IC base=+0.270)

- **PATRÓN** `volumen_pendiente_norm` > `0.2431` → IC=+0.364 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2431 (IC base=+0.270)

- **PATRÓN** `volumen_spike_ratio` < `2.5474` → IC=+0.264 (n=1036)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5474 (IC base=+0.270)

- **PATRÓN** `volumen_spike_ratio` > `2.1719` → IC=+0.273 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1719 (IC base=+0.270)

- **PATRÓN** `libro_liquidez` > `2357.2754` → IC=+0.276 (n=1072)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2357.2754 (IC base=+0.270)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.175 (n=2148)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0048 (IC base=+0.166)

- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.199 (n=2144)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0106 (IC base=+0.166)

- **PATRÓN** `drift_60min` |x|≤ `0.3373` → IC=+0.174 (n=5656)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.3373 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.176 (n=6704)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` > `0.5808` → IC=+0.214 (n=6427)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5808 (IC base=+0.166)

- **PATRÓN** `dist_vwap_pct` > `0.9305` → IC=+0.216 (n=955)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9305 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.206` → IC=+0.249 (n=1327)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.206 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` < `1.2135` → IC=+0.161 (n=4261)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2135 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` > `0.6235` → IC=+0.157 (n=4260)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.6235 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` > `0.2979` → IC=+0.190 (n=945)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2979 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` < `1.5652` → IC=+0.173 (n=2692)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5652 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` > `2.6643` → IC=+0.170 (n=2038)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.6643 (IC base=+0.166)

- **PATRÓN** `libro_liquidez` > `3820.3005` → IC=+0.168 (n=2142)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 3820.3005 (IC base=+0.166)

- **PATRÓN** `ballena_activa_n` < `120.0` → IC=+0.181 (n=5333)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 120.0 (IC base=+0.166)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.186 (n=4159)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0064 (IC base=+0.170)

- **PATRÓN** `drift_60min` |x|≤ `0.079` → IC=+0.204 (n=2077)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.079 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.205 (n=2108)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.170)

- **PATRÓN** `ibs_20min` < `0.4712` → IC=+0.229 (n=6231)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4712 (IC base=+0.170)

- **PATRÓN** `dist_vwap_pct` < `0.2197` → IC=+0.161 (n=4641)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.2197 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.163` → IC=+0.196 (n=1072)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.163 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` < `1.1821` → IC=+0.154 (n=4558)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.1821 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` > `0.6248` → IC=+0.149 (n=4557)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.6248 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` > `0.2918` → IC=+0.230 (n=894)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2918 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` < `1.5756` → IC=+0.171 (n=2451)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.5756 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` > `2.6497` → IC=+0.176 (n=1857)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.6497 (IC base=+0.170)

- **PATRÓN** `ballena_activa_n` < `122.0` → IC=+0.172 (n=5192)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 122.0 (IC base=+0.170)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.221 (n=367)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.185)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.199 (n=367)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.185)

- **PATRÓN** `drift_60min` |x|≤ `0.3245` → IC=+0.203 (n=1099)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3245 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.207 (n=538)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.304 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.992` → IC=+0.307 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.992 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.2298` → IC=+0.239 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2298 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` < `2.5472` → IC=+0.173 (n=1002)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 2.5472 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` > `1.4261` → IC=+0.179 (n=1002)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.4261 (IC base=+0.185)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.204 (n=1047)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.185)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.243 (n=690)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.249 (n=699)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.1816` → IC=+0.288 (n=522)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1816 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.245 (n=709)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.239 (n=786)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.3402` → IC=+0.260 (n=782)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3402 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.016` → IC=+0.252 (n=847)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.016 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.0955` → IC=+0.234 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0955 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.23` → IC=+0.260 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.23 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.4302` → IC=+0.253 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4302 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.6424` → IC=+0.236 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6424 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=818)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1750.54` → IC=+0.255 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1750.54 (IC base=+0.237)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.253 (n=314)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.162)

- **PATRÓN** `drift_60min` |x|≤ `0.0751` → IC=+0.193 (n=314)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.0751 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=992)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.162)

- **PATRÓN** `ibs_20min` > `0.4211` → IC=+0.226 (n=940)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4211 (IC base=+0.162)

- **PATRÓN** `dist_vwap_pct` > `0.1948` → IC=+0.208 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1948 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.506` → IC=+0.219 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.506 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` < `1.2593` → IC=+0.172 (n=940)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 1.2593 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` < `0.0779` → IC=+0.161 (n=780)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` < 0.0779 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` > `0.232` → IC=+0.184 (n=207)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.232 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` < `1.4144` → IC=+0.197 (n=302)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.4144 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `10160.4873` → IC=+0.176 (n=940)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 10160.4873 (IC base=+0.162)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.165 (n=1069)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0057 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.059` → IC=+0.194 (n=358)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.059 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.161 (n=992)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 7.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.5429` → IC=+0.189 (n=1069)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.5429 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` < `0.1307` → IC=+0.164 (n=1092)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1307 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.901` → IC=+0.215 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.901 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.2129` → IC=+0.159 (n=1069)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2129 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.1578` → IC=+0.174 (n=329)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1578 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `2.4292` → IC=+0.155 (n=958)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4292 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `223.0` → IC=+0.161 (n=293)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 223.0 (IC base=+0.144)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.207 (n=716)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0076 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.1988` → IC=+0.206 (n=712)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1988 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.230 (n=368)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.289 (n=562)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.672` → IC=+0.273 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.672 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` < `0.2141` → IC=+0.187 (n=1028)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` < 0.2141 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.1338` → IC=+0.187 (n=413)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.1338 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` < `1.6619` → IC=+0.191 (n=334)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 1.6619 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `3.5963` → IC=+0.205 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.5963 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.203 (n=1219)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.190)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.229 (n=596)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.223)

- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.223 (n=892)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0057 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.0889` → IC=+0.243 (n=298)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0889 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.270 (n=319)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` < `0.3486` → IC=+0.254 (n=892)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3486 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.679` → IC=+0.273 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.679 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.3606` → IC=+0.271 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3606 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` < `1.6443` → IC=+0.215 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6443 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` > `3.5248` → IC=+0.244 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.5248 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `1899.5579` → IC=+0.240 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1899.5579 (IC base=+0.223)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.211 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 18.0 (IC base=+0.223)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.178 (n=892)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0066 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.4234` → IC=+0.162 (n=1014)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.4234 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.184 (n=362)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.3938` → IC=+0.201 (n=1014)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3938 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.1348` → IC=+0.185 (n=664)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.1348 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.979` → IC=+0.246 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.979 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `1.0503` → IC=+0.154 (n=892)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.0503 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` > `1.1899` → IC=+0.165 (n=338)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 1.1899 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.2888` → IC=+0.222 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2888 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `1.5341` → IC=+0.164 (n=436)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.5341 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `2.5113` → IC=+0.175 (n=330)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.5113 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `7038.1688` → IC=+0.187 (n=676)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 7038.1688 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `118.0` → IC=+0.158 (n=641)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 118.0 (IC base=+0.148)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.167 (n=1088)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0071 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.3804` → IC=+0.146 (n=1088)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3804 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.190 (n=366)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 18.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` < `0.6027` → IC=+0.182 (n=1087)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.6027 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` < `0.1485` → IC=+0.148 (n=1089)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1485 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.87` → IC=+0.195 (n=211)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 11.87 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` < `0.8541` → IC=+0.144 (n=725)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.8541 (IC base=+0.132)

- **PATRÓN** `volumen_pendiente_norm` > `0.2884` → IC=+0.209 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2884 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` < `1.799` → IC=+0.137 (n=648)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.799 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` > `2.4783` → IC=+0.147 (n=324)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 2.4783 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `10084.8377` → IC=+0.161 (n=493)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 10084.8377 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `174.0` → IC=+0.129 (n=902)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 174.0 (IC base=+0.132)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.156 (n=539)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0099 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.129 (n=1221)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 5.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` > `0.5098` → IC=+0.198 (n=1187)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.5098 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` > `1.0185` → IC=+0.217 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0185 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.47` → IC=+0.256 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.47 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `1.2233` → IC=+0.122 (n=1187)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.2233 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` < `1.8146` → IC=+0.129 (n=761)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.8146 (IC base=+0.111)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.121 (n=1227)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.02 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `2898.8632` → IC=+0.187 (n=538)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 2898.8632 (IC base=+0.111)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.130 (n=881)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 49.0 (IC base=+0.111)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.154 (n=403)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0053 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.169 (n=557)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 15.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` < `0.56` → IC=+0.204 (n=1201)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.56 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` > `0.6856` → IC=+0.134 (n=225)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 0.6856 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` < `0.1829` → IC=+0.134 (n=1092)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.1829 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.386` → IC=+0.152 (n=257)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 7.386 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `1.0407` → IC=+0.120 (n=1057)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_regimen` < 1.0407 (IC base=+0.111)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.176 (n=143)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` < `1.4638` → IC=+0.136 (n=352)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.4638 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` > `2.1782` → IC=+0.126 (n=479)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 2.1782 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `3085.144` → IC=+0.163 (n=401)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 3085.144 (IC base=+0.111)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0182` → IC=+0.213 (n=747)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0182 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.1686` → IC=+0.214 (n=494)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1686 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.220 (n=405)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` > `0.7255` → IC=+0.254 (n=1001)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7255 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` > `1.2191` → IC=+0.229 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2191 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.371` → IC=+0.242 (n=532)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.371 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` < `1.2068` → IC=+0.206 (n=1121)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2068 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` > `0.6141` → IC=+0.209 (n=1121)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6141 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` > `0.2413` → IC=+0.266 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2413 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` < `2.1881` → IC=+0.215 (n=948)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1881 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` > `1.4272` → IC=+0.206 (n=1077)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4272 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.202 (n=1153)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `2576.372` → IC=+0.201 (n=747)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2576.372 (IC base=+0.201)

- **PATRÓN** `sigma_h` < `0.008` → IC=+0.238 (n=403)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.204)

- **PATRÓN** `sigma_h` > `0.0168` → IC=+0.211 (n=801)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0168 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.089` → IC=+0.218 (n=402)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.089 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.222 (n=596)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.210 (n=549)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` < `0.0294` → IC=+0.310 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0294 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `1.1412` → IC=+0.229 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1412 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` < `0.2629` → IC=+0.205 (n=1264)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2629 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.713` → IC=+0.230 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.713 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` > `0.6258` → IC=+0.216 (n=1202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6258 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.282 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` < `2.2423` → IC=+0.197 (n=936)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.2423 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `1.4611` → IC=+0.196 (n=1064)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.4611 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `2553.3356` → IC=+0.214 (n=801)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2553.3356 (IC base=+0.204)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.156 (n=527)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0039 (IC base=+0.138)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.165 (n=524)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0089 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.3432` → IC=+0.142 (n=1382)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.3432 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.179 (n=799)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 15.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.3942` → IC=+0.170 (n=1570)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.3942 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.817` → IC=+0.164 (n=221)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.817 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.668` → IC=+0.166 (n=723)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 3.668 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.8678` → IC=+0.154 (n=902)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8678 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `1.2036` → IC=+0.140 (n=451)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 1.2036 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.1641` → IC=+0.168 (n=432)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.1641 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.4339` → IC=+0.153 (n=502)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.4339 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `2.5669` → IC=+0.168 (n=501)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.5669 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.142 (n=1754)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.02 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `8533.3968` → IC=+0.151 (n=712)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 8533.3968 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `158.0` → IC=+0.159 (n=1349)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 158.0 (IC base=+0.138)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.150 (n=558)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0038 (IC base=+0.115)

- **PATRÓN** `drift_60min` |x|≤ `0.3399` → IC=+0.130 (n=1463)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.3399 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.129 (n=1679)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 5.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` < `0.4882` → IC=+0.155 (n=1463)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.4882 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.009` → IC=+0.129 (n=481)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 6.009 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` < `1.2216` → IC=+0.123 (n=1474)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.2216 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` > `0.167` → IC=+0.142 (n=423)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.167 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` < `2.2373` → IC=+0.135 (n=1402)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.2373 (IC base=+0.115)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.124 (n=663)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 25.0 (IC base=+0.115)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3457` → IC=+0.123 (n=367)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.62€ cuando `drift_60min` |x|≤ 0.3457 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.145 (n=328)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 10.0 (IC base=+0.102)

- **PATRÓN** `ibs_20min` > `0.2805` → IC=+0.136 (n=366)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 0.2805 (IC base=+0.102)

- **PATRÓN** `dist_vwap_pct` > `0.501` → IC=+0.132 (n=74)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` > 0.501 (IC base=+0.102)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.31` → IC=+0.142 (n=171)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 3.31 (IC base=+0.102)

- **PATRÓN** `volumen_regimen` < `0.7037` → IC=+0.140 (n=162)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.7037 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `10437.138` → IC=+0.128 (n=366)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 10437.138 (IC base=+0.102)

- **PATRÓN** `ballena_activa_n` < `151.0` → IC=+0.161 (n=113)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 151.0 (IC base=+0.102)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.214 (n=173)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.3374` → IC=+0.152 (n=518)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.3374 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.152 (n=467)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 7.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.3447` → IC=+0.207 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3447 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.437` → IC=+0.144 (n=206)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 4.437 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.093` → IC=+0.136 (n=588)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 9.093 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `1.208` → IC=+0.139 (n=518)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.208 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` > `1.0619` → IC=+0.171 (n=235)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 1.0619 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.1595` → IC=+0.216 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1595 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `2.4413` → IC=+0.157 (n=508)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4413 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.42` → IC=+0.143 (n=508)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.42 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `153.0` → IC=+0.177 (n=165)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 153.0 (IC base=+0.134)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.257 (n=204)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.194)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.205 (n=154)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.194)

- **PATRÓN** `drift_60min` |x|≤ `0.0944` → IC=+0.220 (n=155)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0944 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.245 (n=229)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `0.3958` → IC=+0.240 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3958 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` > `0.138` → IC=+0.227 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.138 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.085` → IC=+0.235 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.085 (IC base=+0.194)

- **PATRÓN** `volumen_regimen` < `0.8363` → IC=+0.201 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8363 (IC base=+0.194)

- **PATRÓN** `volumen_regimen` > `1.1584` → IC=+0.218 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1584 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.2479` → IC=+0.321 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2479 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` < `1.3759` → IC=+0.221 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3759 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `2.391` → IC=+0.266 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.391 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `12317.9636` → IC=+0.211 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12317.9636 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.124 (n=416)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0067 (IC base=+0.101)

- **PATRÓN** `drift_60min` |x|≤ `0.0973` → IC=+0.152 (n=139)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.0973 (IC base=+0.101)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.128 (n=283)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 11.0 (IC base=+0.101)

- **PATRÓN** `ibs_20min` < `0.0561` → IC=+0.181 (n=139)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.0561 (IC base=+0.101)

- **PATRÓN** `dist_vwap_pct` > `0.1427` → IC=+0.123 (n=165)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` > 0.1427 (IC base=+0.101)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.432` → IC=+0.149 (n=112)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 6.432 (IC base=+0.101)

- **PATRÓN** `volumen_pendiente_norm` > `0.1654` → IC=+0.170 (n=98)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.1654 (IC base=+0.101)

- **PATRÓN** `volumen_spike_ratio` > `1.8125` → IC=+0.137 (n=265)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.8125 (IC base=+0.101)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `dist_vwap_pct` > `0.5565` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.5565
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=435)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.129 (n=324)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 8.0 (IC base=+0.091)

- **PATRÓN** `ibs_20min` > `0.8889` → IC=+0.202 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8889 (IC base=+0.091)

- **PATRÓN** `dist_vwap_pct` > `0.6084` → IC=+0.149 (n=75)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.6084 (IC base=+0.091)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.092` → IC=+0.171 (n=159)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 5.092 (IC base=+0.091)

- **PATRÓN** `volumen_pendiente_norm` > `0.2898` → IC=+0.180 (n=48)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2898 (IC base=+0.091)

- **PATRÓN** `volumen_spike_ratio` > `2.2136` → IC=+0.129 (n=149)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.2136 (IC base=+0.091)

- **PATRÓN** `libro_liquidez` > `3089.4567` → IC=+0.212 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3089.4567 (IC base=+0.091)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.155 (n=114)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 21.0 (IC base=+0.091)

- **PATRÓN** `ibs_20min` < `0.4872` → IC=+0.149 (n=340)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.4872 (IC base=+0.084)

- **PATRÓN** `volumen_regimen` < `0.7121` → IC=+0.132 (n=150)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 0.7121 (IC base=+0.084)

- **PATRÓN** `volumen_spike_ratio` < `1.604` → IC=+0.188 (n=139)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.604 (IC base=+0.084)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0232` → IC=+0.161 (n=178)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0232 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.2324` → IC=+0.178 (n=119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.2324 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.167 (n=64)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 16.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.216 (n=79)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.56` → IC=+0.191 (n=160)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.56 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.2468` → IC=+0.153 (n=93)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.2468 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `1.0795` → IC=+0.160 (n=201)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 1.0795 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.705` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 7.705 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.317` → IC=+0.175 (n=152)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` < 3.317 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` > `0.8803` → IC=+0.167 (n=118)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.8803 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` < `0.1233` → IC=+0.169 (n=140)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` < 0.1233 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `1.4421` → IC=+0.222 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4421 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.176 (n=180)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.02 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `2727.8122` → IC=+0.163 (n=81)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2727.8122 (IC base=+0.147)

- **PATRÓN** `sigma_h` > `0.022` → IC=+0.177 (n=91)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.022 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=71)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` < `0.08` → IC=+0.181 (n=67)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.08 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `1.1744` → IC=+0.295 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1744 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.53` → IC=+0.190 (n=27)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 9.53 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `1.0734` → IC=+0.126 (n=177)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.0734 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` > `0.6508` → IC=+0.140 (n=201)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 0.6508 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` < `0.1187` → IC=+0.133 (n=178)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` < 0.1187 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `1.6702` → IC=+0.131 (n=82)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.6702 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `2.0068` → IC=+0.127 (n=124)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 2.0068 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.146 (n=162)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 17.0 (IC base=+0.124)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.193 (n=3706)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.0088 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.174 (n=8532)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.213 (n=8171)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4706 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` > `0.884` → IC=+0.194 (n=1060)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.884 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.559` → IC=+0.223 (n=3993)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.559 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` < `0.8826` → IC=+0.164 (n=3654)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8826 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` > `0.2392` → IC=+0.192 (n=1538)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2392 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` > `2.6346` → IC=+0.183 (n=2597)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.6346 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `3790.4821` → IC=+0.169 (n=2722)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 3790.4821 (IC base=+0.165)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.192 (n=5997)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 92.0 (IC base=+0.165)

- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.196 (n=4989)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0068 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.4801` → IC=+0.184 (n=7475)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.4801 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.204 (n=2871)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.5625` → IC=+0.239 (n=7476)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5625 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` < `0.2302` → IC=+0.163 (n=4746)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.2302 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.842` → IC=+0.196 (n=1075)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 9.842 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.683` → IC=+0.183 (n=7228)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 3.683 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `0.7044` → IC=+0.160 (n=2278)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.7044 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` > `1.2035` → IC=+0.160 (n=1726)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 1.2035 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2889` → IC=+0.247 (n=977)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2889 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.2973` → IC=+0.190 (n=3055)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.2973 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.192 (n=2152)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 25.0 (IC base=+0.182)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.209 (n=462)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.191)

- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.210 (n=923)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.197 (n=680)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 15.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.203 (n=924)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.191)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.322 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.347` → IC=+0.291 (n=846)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.347 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` > `0.2243` → IC=+0.244 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2243 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` > `2.5813` → IC=+0.200 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5813 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.216 (n=1296)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.191)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.256 (n=1068)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.255)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.263 (n=1067)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0044 (IC base=+0.255)

- **PATRÓN** `drift_60min` |x|≤ `0.2039` → IC=+0.283 (n=711)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2039 (IC base=+0.255)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.267 (n=966)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.255)

- **PATRÓN** `ibs_20min` < `0.3505` → IC=+0.287 (n=938)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3505 (IC base=+0.255)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.403` → IC=+0.262 (n=1120)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.403 (IC base=+0.255)

- **PATRÓN** `volumen_pendiente_norm` > `0.2233` → IC=+0.301 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2233 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` > `1.8803` → IC=+0.277 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8803 (IC base=+0.255)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.255 (n=1115)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.255)

- **PATRÓN** `libro_liquidez` > `1749.5288` → IC=+0.273 (n=710)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1749.5288 (IC base=+0.255)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.197 (n=437)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0028 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.1837` → IC=+0.156 (n=865)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1837 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=1353)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.3149` → IC=+0.201 (n=1297)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3149 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.3225` → IC=+0.195 (n=490)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.3225 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.757` → IC=+0.156 (n=303)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 9.757 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.29` → IC=+0.154 (n=1153)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.29 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.6949` → IC=+0.181 (n=571)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.6949 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` < `0.0736` → IC=+0.154 (n=1129)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.0736 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.2649` → IC=+0.182 (n=187)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2649 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.1166` → IC=+0.157 (n=1094)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.1166 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.7574` → IC=+0.159 (n=829)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.7574 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `10964.1889` → IC=+0.167 (n=1159)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 10964.1889 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `486.0` → IC=+0.161 (n=1174)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 486.0 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.170 (n=1156)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0057 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.3265` → IC=+0.165 (n=1155)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.3265 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.175 (n=527)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 16.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` < `0.6377` → IC=+0.205 (n=1155)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6377 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.6855` → IC=+0.167 (n=172)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.6855 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` < `0.1262` → IC=+0.165 (n=1071)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1262 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.523` → IC=+0.173 (n=206)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 11.523 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `1.2029` → IC=+0.163 (n=1155)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2029 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.1504` → IC=+0.202 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1504 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `2.4232` → IC=+0.169 (n=1057)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 2.4232 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `1.7548` → IC=+0.159 (n=705)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.7548 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `12583.0078` → IC=+0.157 (n=770)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 12583.0078 (IC base=+0.154)

- **PATRÓN** `ballena_activa_n` < `366.0` → IC=+0.167 (n=641)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 366.0 (IC base=+0.154)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.229 (n=1306)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.218 (n=1369)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.214 (n=1318)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.6721` → IC=+0.251 (n=1165)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6721 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.556` → IC=+0.300 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.556 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` < `0.2161` → IC=+0.216 (n=1268)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2161 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `2.9826` → IC=+0.235 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9826 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.225 (n=1502)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.239 (n=1235)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.234)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.236 (n=563)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0092 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.256 (n=470)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.3636` → IC=+0.269 (n=1087)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3636 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.713` → IC=+0.274 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.713 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.3592` → IC=+0.295 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3592 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.7962` → IC=+0.225 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7962 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.2483` → IC=+0.233 (n=740)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2483 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.246 (n=703)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `1900.976` → IC=+0.244 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1900.976 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.258 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.234)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.175 (n=466)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0034 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.4335` → IC=+0.137 (n=1388)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.4335 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.144 (n=1452)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` > `0.6988` → IC=+0.229 (n=925)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6988 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` > `0.5535` → IC=+0.173 (n=371)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.5535 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.174` → IC=+0.159 (n=582)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 4.174 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.8772` → IC=+0.156 (n=926)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.8772 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.2772` → IC=+0.228 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2772 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `1.5119` → IC=+0.148 (n=589)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.5119 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `2.4575` → IC=+0.155 (n=445)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.4575 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `8688.9164` → IC=+0.229 (n=629)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8688.9164 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.165 (n=425)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 85.0 (IC base=+0.134)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.163 (n=1124)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0075 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.4442` → IC=+0.160 (n=1124)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.4442 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.175 (n=429)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.154 (n=504)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` < `0.6856` → IC=+0.196 (n=1125)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.6856 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` < `0.345` → IC=+0.145 (n=1153)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.345 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.009` → IC=+0.190 (n=169)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 11.009 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.186` → IC=+0.143 (n=1048)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 4.186 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `0.695` → IC=+0.150 (n=495)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.695 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` > `1.1764` → IC=+0.158 (n=375)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 1.1764 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.2782` → IC=+0.278 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2782 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `1.4426` → IC=+0.159 (n=1053)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.4426 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `11048.3545` → IC=+0.206 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11048.3545 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `164.0` → IC=+0.146 (n=922)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 164.0 (IC base=+0.143)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.162 (n=530)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.098)

- **PATRÓN** `ibs_20min` > `0.4694` → IC=+0.181 (n=1395)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.4694 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `1.0059` → IC=+0.184 (n=248)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 1.0059 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.364` → IC=+0.224 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.364 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `2920.0962` → IC=+0.237 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2920.0962 (IC base=+0.098)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.123 (n=1049)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 53.0 (IC base=+0.098)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.178 (n=451)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0056 (IC base=+0.113)

- **PATRÓN** `drift_60min` |x|≤ `0.1276` → IC=+0.156 (n=451)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1276 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.148 (n=640)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 15.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.6429` → IC=+0.207 (n=1351)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6429 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` < `0.4695` → IC=+0.128 (n=1319)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` < 0.4695 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.451` → IC=+0.126 (n=1299)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` < 3.451 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `0.7204` → IC=+0.150 (n=595)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.7204 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.2238` → IC=+0.173 (n=209)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2238 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` < `1.4671` → IC=+0.150 (n=398)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4671 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` > `2.5629` → IC=+0.125 (n=398)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` > 2.5629 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `2892.056` → IC=+0.162 (n=450)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2892.056 (IC base=+0.113)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0185` → IC=+0.214 (n=934)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0185 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.211 (n=1464)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `0.5116` → IC=+0.245 (n=1401)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5116 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `0.1843` → IC=+0.231 (n=786)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1843 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.372` → IC=+0.248 (n=678)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.372 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` < `1.2457` → IC=+0.209 (n=1402)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2457 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` > `0.6304` → IC=+0.209 (n=1401)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6304 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.0797` → IC=+0.232 (n=561)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0797 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `2.5676` → IC=+0.238 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5676 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.213 (n=1425)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `2587.0012` → IC=+0.209 (n=934)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2587.0012 (IC base=+0.205)

- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.235 (n=518)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0081 (IC base=+0.199)

- **PATRÓN** `sigma_h` > `0.0256` → IC=+0.218 (n=516)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0256 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.214 (n=756)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.200 (n=1635)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.5146` → IC=+0.254 (n=1548)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5146 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` > `0.4981` → IC=+0.199 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4981 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` < `0.2662` → IC=+0.204 (n=1450)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2662 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.731` → IC=+0.259 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.731 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` > `1.2292` → IC=+0.234 (n=516)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2292 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.2851` → IC=+0.255 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2851 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `2.2259` → IC=+0.194 (n=1203)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 2.2259 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `1.4468` → IC=+0.198 (n=1367)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.4468 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.207 (n=1008)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `2562.9213` → IC=+0.199 (n=1032)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2562.9213 (IC base=+0.199)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.135 (n=2600)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.155 (n=2235)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0094 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.526` → IC=+0.156 (n=2540)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.526 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.159 (n=850)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 18.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.160 (n=884)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 4.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `0.9389` → IC=+0.213 (n=847)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9389 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.1868` → IC=+0.153 (n=832)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.1868 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.737` → IC=+0.167 (n=820)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 5.737 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` > `0.9068` → IC=+0.152 (n=1033)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.9068 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.1737` → IC=+0.174 (n=695)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1737 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `1.4616` → IC=+0.162 (n=838)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.4616 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `1.9066` → IC=+0.157 (n=1675)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.9066 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `8216.4561` → IC=+0.153 (n=1152)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 8216.4561 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.188 (n=654)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0037 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.4873` → IC=+0.152 (n=1962)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.4873 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.164 (n=743)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.158 (n=659)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 4.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.1819` → IC=+0.161 (n=863)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.1819 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` > `0.7048` → IC=+0.139 (n=350)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.7048 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.274` → IC=+0.142 (n=1943)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 6.274 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `1.1133` → IC=+0.142 (n=1639)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.1133 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.0717` → IC=+0.149 (n=923)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.0717 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `2.5707` → IC=+0.138 (n=1942)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 2.5707 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.8237` → IC=+0.144 (n=1295)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.8237 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.135 (n=2600)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `7633.9254` → IC=+0.150 (n=1753)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 7633.9254 (IC base=+0.133)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.169 (n=279)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0058 (IC base=+0.156)

- **PATRÓN** `sigma_h` > `0.0035` → IC=+0.171 (n=284)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0035 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.0923` → IC=+0.185 (n=106)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.0923 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.165 (n=326)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` < `0.5413` → IC=+0.192 (n=212)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.5413 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `0.2289` → IC=+0.180 (n=145)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.2289 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.25` → IC=+0.164 (n=400)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` < 8.25 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` < `1.2448` → IC=+0.158 (n=317)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.2448 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` > `0.832` → IC=+0.190 (n=211)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` > 0.832 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` > `0.3073` → IC=+0.267 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3073 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `1.4419` → IC=+0.213 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4419 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` > `2.7581` → IC=+0.194 (n=106)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.7581 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `12617.0993` → IC=+0.205 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12617.0993 (IC base=+0.156)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.204 (n=387)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.3662` → IC=+0.143 (n=876)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3662 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.170 (n=337)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.165 (n=320)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 5.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` < `0.1568` → IC=+0.160 (n=386)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1568 (IC base=+0.131)

- **PATRÓN** `ibs_20min` > `0.6152` → IC=+0.139 (n=397)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` > 0.6152 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` > `0.7085` → IC=+0.154 (n=79)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.7085 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` < `0.2264` → IC=+0.132 (n=903)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.2264 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.318` → IC=+0.156 (n=855)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 6.318 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `0.8847` → IC=+0.176 (n=584)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.8847 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.0693` → IC=+0.161 (n=414)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.0693 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` < `2.5736` → IC=+0.140 (n=873)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.5736 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `1.8156` → IC=+0.142 (n=582)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.8156 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `11358.9394` → IC=+0.147 (n=876)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 11358.9394 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `712.0` → IC=+0.137 (n=830)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 712.0 (IC base=+0.131)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.186 (n=208)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.006 (IC base=+0.164)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.180 (n=282)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0099 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.4174` → IC=+0.173 (n=548)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.4174 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.222 (n=232)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `0.9934` → IC=+0.233 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9934 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.404` → IC=+0.217 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.404 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.2084` → IC=+0.204 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2084 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` < `3.3904` → IC=+0.166 (n=621)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 3.3904 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` > `2.2621` → IC=+0.171 (n=414)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.2621 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `2425.929` → IC=+0.197 (n=282)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2425.929 (IC base=+0.164)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.312 (n=30)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.254)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.262 (n=40)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.254)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.262 (n=40)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.254)

- **PATRÓN** `ibs_20min` > `0.4722` → IC=+0.312 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4722 (IC base=+0.254)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.213` → IC=+0.364 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.213 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` < `0.1317` → IC=+0.273 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1317 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` > `0.1037` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1037 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` < `2.5115` → IC=+0.281 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5115 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` > `3.6446` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.6446 (IC base=+0.254)

- **PATRÓN** `libro_liquidez` > `2463.7708` → IC=+0.283 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2463.7708 (IC base=+0.254)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0087` → IC=+0.152 (n=756)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0087 (IC base=+0.144)

- **PATRÓN** `sigma_h` > `0.0045` → IC=+0.151 (n=757)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0045 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.5033` → IC=+0.153 (n=756)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.5033 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.164 (n=296)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.152 (n=274)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 4.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.5481` → IC=+0.144 (n=504)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.5481 (IC base=+0.144)

- **PATRÓN** `ibs_20min` > `0.186` → IC=+0.156 (n=756)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` > 0.186 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.9619` → IC=+0.173 (n=166)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.9619 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` < `0.4234` → IC=+0.151 (n=720)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.4234 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.678` → IC=+0.153 (n=754)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 6.678 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.1119` → IC=+0.148 (n=665)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.1119 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` > `0.6454` → IC=+0.148 (n=756)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 0.6454 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.1755` → IC=+0.156 (n=225)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.1755 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `1.4406` → IC=+0.172 (n=248)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.4406 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=719)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `8127.2771` → IC=+0.149 (n=756)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 8127.2771 (IC base=+0.144)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.162 (n=545)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0071 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.5118` → IC=+0.181 (n=619)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.5118 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=235)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.154 (n=432)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 11.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.7429` → IC=+0.149 (n=619)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.7429 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.1001` → IC=+0.160 (n=619)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.1001 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.1548` → IC=+0.169 (n=279)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1548 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` < `0.3912` → IC=+0.148 (n=637)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.3912 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.985` → IC=+0.160 (n=139)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 8.985 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `0.647` → IC=+0.175 (n=207)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.647 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` > `0.7262` → IC=+0.154 (n=553)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 0.7262 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.0728` → IC=+0.178 (n=265)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.0728 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.1996` → IC=+0.167 (n=535)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.1996 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.4508` → IC=+0.161 (n=608)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.4508 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `8151.1111` → IC=+0.170 (n=619)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 8151.1111 (IC base=+0.148)

### GBM_LATE_5M#SOL#5min
- **FILTRO** `hora_utc` > `6.0` → IC=-0.150 (n=38)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=137)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=160)

- **PATRÓN** `ibs_20min` > `0.9848` → IC=+0.174 (n=44)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.9848 (IC base=+0.025)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.125` → IC=+0.184 (n=36)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 7.125 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.156` → IC=+0.136 (n=42)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.156 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` > `0.6259` → IC=+0.161 (n=54)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.6259 (IC base=+0.023)

### GBM_LATE_60M
- **FILTRO** `sigma_h` > `0.0076` → IC=-0.250 (n=98)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0076
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=298)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.235 (n=96)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=300)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.210 (n=308)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.128 (n=656)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 8.0 (IC base=+0.105)

- **PATRÓN** `ibs_20min` > `0.625` → IC=+0.208 (n=608)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.625 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `0.1301` → IC=+0.175 (n=318)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.1301 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.072` → IC=+0.226 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.072 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` < `1.0919` → IC=+0.128 (n=608)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.0919 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` > `0.975` → IC=+0.122 (n=276)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` > 0.975 (IC base=+0.105)

- **PATRÓN** `volumen_pendiente_norm` > `0.2862` → IC=+0.204 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2862 (IC base=+0.105)

- **PATRÓN** `volumen_spike_ratio` < `2.4945` → IC=+0.157 (n=500)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.4945 (IC base=+0.105)

- **PATRÓN** `volumen_spike_ratio` > `1.4023` → IC=+0.136 (n=500)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.4023 (IC base=+0.105)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.135 (n=491)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.02 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `2445.5482` → IC=+0.148 (n=265)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 2445.5482 (IC base=+0.105)

- **PATRÓN** `ibs_20min` < `0.0714` → IC=+0.280 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0714 (IC base=-0.028)

- **PATRÓN** `volumen_pendiente_norm` > `0.0631` → IC=+0.188 (n=75)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.0631 (IC base=-0.028)

- **PATRÓN** `volumen_spike_ratio` < `2.6357` → IC=+0.130 (n=163)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 2.6357 (IC base=-0.028)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.5802` → IC=-0.176 (n=69)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5802
  - _Potencial_: sin este filtro IC_bueno=+0.201 (n=209)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.174 (n=240)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.006 (IC base=+0.101)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.178 (n=88)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.101)

- **PATRÓN** `ibs_20min` > `0.5802` → IC=+0.201 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5802 (IC base=+0.101)

- **PATRÓN** `dist_vwap_pct` > `0.1249` → IC=+0.189 (n=101)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1249 (IC base=+0.101)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.734` → IC=+0.129 (n=130)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 3.734 (IC base=+0.101)

- **PATRÓN** `volumen_regimen` < `1.0527` → IC=+0.134 (n=184)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.0527 (IC base=+0.101)

- **PATRÓN** `volumen_pendiente_norm` < `0.0759` → IC=+0.151 (n=150)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.0759 (IC base=+0.101)

- **PATRÓN** `volumen_spike_ratio` < `2.0129` → IC=+0.184 (n=150)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 2.0129 (IC base=+0.101)

- **PATRÓN** `drift_60min` |x|≤ `0.0426` → IC=+0.200 (n=28)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0426 (IC base=+0.045)

- **PATRÓN** `ibs_20min` < `0.7371` → IC=+0.181 (n=92)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.7371 (IC base=+0.045)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.71` → IC=+0.179 (n=76)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` < 4.71 (IC base=+0.045)

- **PATRÓN** `volumen_regimen` < `0.9523` → IC=+0.139 (n=81)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.9523 (IC base=+0.045)

- **PATRÓN** `volumen_pendiente_norm` > `0.0643` → IC=+0.210 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0643 (IC base=+0.045)

- **PATRÓN** `volumen_spike_ratio` < `2.0748` → IC=+0.198 (n=61)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.0748 (IC base=+0.045)

- **PATRÓN** `libro_liquidez` > `3269.2861` → IC=+0.161 (n=54)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 3269.2861 (IC base=+0.045)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0064` → IC=-0.312 (n=30)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0064
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=91)

- **FILTRO** `hora_utc` > `6.0` → IC=-0.222 (n=52)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=69)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.175 (n=161)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.005 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.142 (n=216)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 8.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.6404` → IC=+0.241 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6404 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.1205` → IC=+0.188 (n=110)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1205 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.109` → IC=+0.322 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.109 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `1.0679` → IC=+0.153 (n=211)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.0679 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.5769` → IC=+0.146 (n=210)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 0.5769 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.3002` → IC=+0.259 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3002 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.7434` → IC=+0.179 (n=107)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.7434 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` > `1.3908` → IC=+0.161 (n=160)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.3908 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.156 (n=219)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.02 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `1096.6975` → IC=+0.194 (n=184)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 1096.6975 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.1005` → IC=+0.231 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1005 (IC base=-0.069)

- **PATRÓN** `volumen_pendiente_norm` > `0.0767` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.0767 (IC base=-0.069)

- **PATRÓN** `volumen_spike_ratio` > `2.7298` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7298 (IC base=-0.069)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.281 (n=39)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=82)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.167 (n=97)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.006 (IC base=+0.088)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.128 (n=221)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 7.0 (IC base=+0.088)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.191 (n=189)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.6667 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.8747` → IC=+0.203 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8747 (IC base=+0.088)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.345` → IC=+0.222 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.345 (IC base=+0.088)

- **PATRÓN** `volumen_regimen` < `0.7896` → IC=+0.120 (n=127)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_regimen` < 0.7896 (IC base=+0.088)

- **PATRÓN** `volumen_regimen` > `1.0632` → IC=+0.146 (n=63)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 1.0632 (IC base=+0.088)

- **PATRÓN** `volumen_pendiente_norm` > `0.0894` → IC=+0.187 (n=81)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.0894 (IC base=+0.088)

- **PATRÓN** `volumen_spike_ratio` < `2.1854` → IC=+0.171 (n=150)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 2.1854 (IC base=+0.088)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.143 (n=40)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.006 (IC base=-0.077)

- **PATRÓN** `ibs_20min` < `0.1154` → IC=+0.244 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1154 (IC base=-0.077)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.966` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.966 (IC base=-0.077)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `11.0` → IC=-0.429 (n=40)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.153 (n=125)

- **FILTRO** `dist_vwap_pct` > `0.2226` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2226
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=148)

- **FILTRO** `volumen_regimen` < `0.7296` → IC=-0.339 (n=54)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7296
  - _Potencial_: sin este filtro IC_bueno=-0.164 (n=111)

- **FILTRO** `volumen_pendiente_norm` > `0.1823` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1823
  - _Potencial_: sin este filtro IC_bueno=-0.139 (n=70)

- **FILTRO** `sigma_h` > `0.0051` → IC=-0.346 (n=50)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.262 (n=99)

- **FILTRO** `dist_vwap_pct` > `0.3412` → IC=-0.371 (n=29)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3412
  - _Potencial_: sin este filtro IC_bueno=-0.271 (n=120)

- **FILTRO** `sigma_ewma_delta_pct` > `8.432` → IC=-0.306 (n=29)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.432
  - _Potencial_: sin este filtro IC_bueno=-0.287 (n=120)

- **FILTRO** `volumen_pendiente_norm` > `0.074` → IC=-0.400 (n=18)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.074
  - _Potencial_: sin este filtro IC_bueno=-0.276 (n=47)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.134 (n=39)

- **FILTRO** `sigma_ewma_delta_pct` > `2.588` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.588
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=34)

- **FILTRO** `sigma_h` < `0.0019` → IC=-0.318 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0019
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=42)

- **FILTRO** `sigma_ewma_delta_pct` > `3.354` → IC=-0.269 (n=24)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 3.354
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=38)

- **FILTRO** `volumen_regimen` > `0.8276` → IC=-0.370 (n=21)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8276
  - _Potencial_: sin este filtro IC_bueno=-0.151 (n=41)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.8218` → IC=-0.450 (n=38)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8218
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=21)

- **FILTRO** `sigma_h` > `0.0033` → IC=-0.340 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.231 (n=24)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.389 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=34)

- **FILTRO** `dist_vwap_pct` > `0.0599` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.0599
  - _Potencial_: sin este filtro IC_bueno=-0.139 (n=34)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.450 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=22)

- **FILTRO** `dist_vwap_pct` < `0.1871` → IC=-0.370 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1871
  - _Potencial_: sin este filtro IC_bueno=-0.309 (n=19)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.2345` → IC=-0.136 (n=108)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2345
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=212)

- **FILTRO** `dist_vwap_pct` > `0.6344` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.6344
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=295)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.131 (n=101)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` > 0.0056 (IC base=+0.079)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.123 (n=104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 15.0 (IC base=+0.079)

- **PATRÓN** `ibs_20min` > `0.6522` → IC=+0.162 (n=223)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.6522 (IC base=+0.079)

- **PATRÓN** `dist_vwap_pct` > `0.47` → IC=+0.173 (n=50)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.47 (IC base=+0.079)

- **PATRÓN** `ibs_20min` < `0.2345` → IC=+0.121 (n=212)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` < 0.2345 (IC base=+0.034)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.104` → IC=+0.149 (n=75)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 9.104 (IC base=+0.034)

- **PATRÓN** `libro_liquidez` > `3837.0322` → IC=+0.149 (n=109)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 3837.0322 (IC base=+0.034)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=82)

- **FILTRO** `ibs_20min` < `0.5548` → IC=-0.385 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5548
  - _Potencial_: sin este filtro IC_bueno=+0.092 (n=74)

- **FILTRO** `volumen_regimen` < `0.7777` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7777
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=74)

- **PATRÓN** `ibs_20min` < `0.1435` → IC=+0.177 (n=97)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.1435 (IC base=+0.095)

- **PATRÓN** `volumen_pendiente_norm` < `0.1776` → IC=+0.130 (n=79)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.1776 (IC base=+0.095)

- **PATRÓN** `volumen_spike_ratio` < `2.9499` → IC=+0.130 (n=79)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 2.9499 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `3574.4675` → IC=+0.152 (n=110)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3574.4675 (IC base=+0.095)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `ibs_20min` < `0.8361` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8361
  - _Potencial_: sin este filtro IC_bueno=+0.209 (n=53)

- **FILTRO** `sigma_h` > `0.0053` → IC=-0.167 (n=25)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=77)

- **FILTRO** `ibs_20min` > `0.3236` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `ibs_20min` > 0.3236
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=77)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.167 (n=61)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0042 (IC base=+0.080)

- **PATRÓN** `drift_60min` |x|≤ `0.2791` → IC=+0.129 (n=60)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.2791 (IC base=+0.080)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.273 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.080)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.136 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 5.0 (IC base=+0.080)

- **PATRÓN** `ibs_20min` > `0.8361` → IC=+0.209 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8361 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` < `0.0869` → IC=+0.154 (n=50)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.0869 (IC base=+0.080)

- **PATRÓN** `volumen_regimen` > `1.1989` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.1989 (IC base=+0.080)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.161 (n=54)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.080)

- **PATRÓN** `libro_liquidez` > `1558.1749` → IC=+0.154 (n=53)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 1558.1749 (IC base=+0.080)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.429` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.429 (IC base=+0.000)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.2121` → IC=-0.203 (n=35)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2121
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=37)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.197 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0047 (IC base=+0.164)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.177 (n=60)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0058 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=43)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.164)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.167 (n=88)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 17.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` < `0.7619` → IC=+0.167 (n=40)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.7619 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `0.7619` → IC=+0.163 (n=81)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.7619 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `0.6434` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6434 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` < `0.2073` → IC=+0.171 (n=74)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.2073 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.688` → IC=+0.219 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.688 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` < `0.7968` → IC=+0.246 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7968 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.0976` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0976 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` < `1.4833` → IC=+0.342 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4833 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.173 (n=50)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.03 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `529.3167` → IC=+0.163 (n=90)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 529.3167 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.0808` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0808 (IC base=-0.041)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `hora_utc` > `16.0` → IC=+0.158 (n=194)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 16.0 (IC base=+0.114)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.130 (n=514)

  - _Acción_: Kelly boost +0.65€ cuando `py_entrada` > 0.5 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `2843.9766` → IC=+0.187 (n=177)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 2843.9766 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `2322.3754` → IC=+0.122 (n=586)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 2322.3754 (IC base=+0.098)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `hora_utc` > `16.0` → IC=+0.158 (n=194)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 16.0 (IC base=+0.114)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.130 (n=514)

  - _Acción_: Kelly boost +0.65€ cuando `py_entrada` > 0.5 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `2843.9766` → IC=+0.187 (n=177)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 2843.9766 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `2322.3754` → IC=+0.122 (n=586)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 2322.3754 (IC base=+0.098)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `10.0` → IC=-0.204 (n=69)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=72)

- **FILTRO** `py_entrada` < `0.435` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.435
  - _Potencial_: sin este filtro IC_bueno=-0.118 (n=108)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=125)

- **FILTRO** `libro_liquidez` < `2415.4574` → IC=-0.284 (n=35)

  - _Acción_: SKIP cuando `libro_liquidez` < 2415.4574
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=106)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=195)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=181)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=32)

- **FILTRO** `liq_n` < `4.0` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `liq_n` < 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=18)

- **FILTRO** `libro_liquidez` < `15479.8554` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `libro_liquidez` < 15479.8554
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=14)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

### LIQUIDACIONES_15M#XRP#15min
- **FILTRO** `liq_n` < `7.0` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `liq_n` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `libro_liquidez` < `2892.3985` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `libro_liquidez` < 2892.3985
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### LIQUIDACIONES_5M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=1376)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=92)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.128 (n=49)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.265 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=81)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=92)

- **FILTRO** `ballena_activa_n` > `558.0` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `ballena_activa_n` > 558.0
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=60)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `16.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=49)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_usd_total` < `33209.41` → IC=-0.152 (n=44)

  - _Acción_: SKIP cuando `liq_usd_total` < 33209.41
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=92)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=19)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.167 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=12)

- **FILTRO** `libro_liquidez` < `15405.8709` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `libro_liquidez` < 15405.8709
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `ballena_activa_n` > `569.0` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `ballena_activa_n` > 569.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

- **PATRÓN** `liq_usd_total` > `61042.02` → IC=+0.186 (n=68)

  - _Acción_: Kelly boost +0.93€ cuando `liq_usd_total` > 61042.02 (IC base=+0.029)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.162 (n=63)

  - _Acción_: Kelly boost +0.81€ cuando `py_entrada` < 0.495 (IC base=+0.029)

- **PATRÓN** `libro_liquidez` > `15568.3857` → IC=+0.133 (n=47)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 15568.3857 (IC base=+0.029)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `hora_utc` > `13.0` → IC=-0.154 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=74)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=614)

- **FILTRO** `liq_usd_total` < `9664.41` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `liq_usd_total` < 9664.41
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9593` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9593
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=16)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.318 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=420)

- **FILTRO** `liq_n` < `8.0` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `liq_n` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **FILTRO** `liq_usd_total` < `24810.11` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `liq_usd_total` < 24810.11
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

### LIQUIDACIONES_5M#XRP#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=77)

### LIQUIDACIONES_60M
- **FILTRO** `py_entrada` < `0.44` → IC=-0.143 (n=208)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=428)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=271)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=271)

- **FILTRO** `py_entrada` > `0.555` → IC=-0.200 (n=48)

  - _Acción_: SKIP cuando `py_entrada` > 0.555
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=238)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=162)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=162)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.125 (n=78)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=99)

- **FILTRO** `hora_utc` > `9.0` → IC=-0.151 (n=64)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=28)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.197 (n=31)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=61)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=165)

- **FILTRO** `py_entrada` > `0.555` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.555
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=66)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=214)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=214)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=98)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=1073)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=5550)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=6744)

### MOMENTUM_IBS_15M#BNB#15min
- **FILTRO** `libro_liquidez` < `2151.302` → IC=-0.153 (n=47)

  - _Acción_: SKIP cuando `libro_liquidez` < 2151.302
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=143)

### MOMENTUM_IBS_15M#BTC#15min
- **FILTRO** `py_entrada` > `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=1058)

- **FILTRO** `libro_liquidez` < `15906.9303` → IC=-0.152 (n=268)

  - _Acción_: SKIP cuando `libro_liquidez` < 15906.9303
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=805)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=1413)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.47` → IC=-0.180 (n=2809)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=8580)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.173 (n=2889)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=8962)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.215 (n=479)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=1459)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.172 (n=492)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=1620)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.121 (n=1158)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` > 0.5 (IC base=+0.020)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.205 (n=479)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=1500)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.222 (n=494)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=1601)

- **FILTRO** `ibs_20min` > `0.2846` → IC=-0.161 (n=523)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2846
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=1572)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.200 (n=464)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=1446)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.193 (n=510)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=1582)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `libro_spread` > `0.01` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=2478)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=2562)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=2568)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.147 (n=83)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=314)

- **FILTRO** `ibs_20min` > `0.1427` → IC=-0.132 (n=134)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1427
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=263)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.212 (n=64)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=196)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.185 (n=52)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.135 (n=176)

- **FILTRO** `py_entrada` > `0.625` → IC=-0.346 (n=50)

  - _Acción_: SKIP cuando `py_entrada` > 0.625
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=178)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=650)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.238 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=223)

### MOMENTUM_IBS_5M#BNB#5min
- **FILTRO** `hora_utc` > `17.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=40)

- **FILTRO** `drift_7min_pct` |x|> `0.0331` → IC=-0.158 (n=36)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.0331
  - _Potencial_: sin este filtro IC_bueno=+0.214 (n=19)

- **PATRÓN** `drift_7min_pct` |x|≤ `0.0331` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_7min_pct` |x|≤ 0.0331 (IC base=-0.026)

### MOMENTUM_IBS_5M#BTC#5min
- **FILTRO** `hora_utc` > `18.0` → IC=-0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 18.0
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=88)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.151 (n=41)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 17.0 (IC base=+0.038)

### MOMENTUM_IBS_5M#DOGE#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=38)

### MOMENTUM_IBS_5M#ETH#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=414)

### MOMENTUM_IBS_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=631)

### MOMENTUM_IBS_5M_BALLENA
- **FILTRO** `hora_utc` < `8.0` → IC=-0.129 (n=8098)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=18421)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.282 (n=6286)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=20233)

- **FILTRO** `ibs_7min` < `0.7` → IC=-0.243 (n=6586)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=19933)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.160 (n=9004)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=17515)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.229 (n=7824)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=25545)

- **FILTRO** `ibs_7min` > `0.2958` → IC=-0.176 (n=8342)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2958
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=25027)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.133 (n=1311)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=2981)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.310 (n=1017)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=3275)

- **FILTRO** `ibs_7min` < `0.708` → IC=-0.259 (n=1416)

  - _Acción_: SKIP cuando `ibs_7min` < 0.708
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=2876)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.199 (n=980)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=3312)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.150 (n=3894)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=1905)

- **FILTRO** `drift_7min_pct` |x|> `0.111` → IC=-0.123 (n=1971)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.111
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=3828)

- **FILTRO** `ibs_7min` > `0.8` → IC=-0.204 (n=1445)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=4354)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.138 (n=1067)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=3560)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.259 (n=1097)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=3530)

- **FILTRO** `ibs_7min` < `0.7545` → IC=-0.187 (n=1156)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7545
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=3471)

- **FILTRO** `ballena_activa_n` > `162.0` → IC=-0.178 (n=1150)

  - _Acción_: SKIP cuando `ballena_activa_n` > 162.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=3477)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.257 (n=1127)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=3581)

- **FILTRO** `ibs_7min` > `0.2549` → IC=-0.169 (n=1176)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2549
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=3532)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.183 (n=1172)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=3536)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.177 (n=979)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=3031)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.316 (n=966)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=3044)

- **FILTRO** `ibs_7min` < `0.2` → IC=-0.268 (n=994)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=3016)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.220 (n=925)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=3085)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.236 (n=1433)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=4679)

- **FILTRO** `ibs_7min` > `0.2608` → IC=-0.154 (n=2078)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2608
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=4034)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.128 (n=1385)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=2990)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.253 (n=1076)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=3299)

- **FILTRO** `ibs_7min` < `0.7422` → IC=-0.190 (n=1093)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7422
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=3282)

- **FILTRO** `ballena_activa_n` > `32.0` → IC=-0.186 (n=1079)

  - _Acción_: SKIP cuando `ballena_activa_n` > 32.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=3296)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.260 (n=1108)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=3375)

- **FILTRO** `ibs_7min` > `0.274` → IC=-0.174 (n=1120)

  - _Acción_: SKIP cuando `ibs_7min` > 0.274
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=3363)

- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.181 (n=1095)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=3388)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.37` → IC=-0.257 (n=1152)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=3588)

- **FILTRO** `ibs_7min` < `0.7143` → IC=-0.231 (n=1165)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7143
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=3575)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.171 (n=1547)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=4769)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.280 (n=1110)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=3365)

- **FILTRO** `ibs_7min` < `0.72` → IC=-0.235 (n=1118)

  - _Acción_: SKIP cuando `ibs_7min` < 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=3357)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.213 (n=1088)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=3387)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.206 (n=1410)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=4541)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=981)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=487)

- **FILTRO** `libro_liquidez` < `10509.8872` → IC=-0.152 (n=133)

  - _Acción_: SKIP cuando `libro_liquidez` < 10509.8872
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=400)

### MOMENTUM_IBS_5M_FADE#DOGE#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=596)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=568)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=313)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=534)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=436)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3982` → IC=+0.136 (n=658)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio` |x|> 0.3982 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.131 (n=592)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 6.0 (IC base=+0.121)

- **PATRÓN** `total_vol_5m` < `453.526` → IC=+0.162 (n=220)

  - _Acción_: Kelly boost +0.81€ cuando `total_vol_5m` < 453.526 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `3728.089` → IC=+0.127 (n=298)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 3728.089 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `60.0` → IC=+0.129 (n=548)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 60.0 (IC base=+0.121)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4377` → IC=+0.160 (n=51)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.80€ cuando `delta_ratio` |x|> 0.4377 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.175 (n=155)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.134)

- **PATRÓN** `total_vol_5m` < `417.524` → IC=+0.140 (n=134)

  - _Acción_: Kelly boost +0.70€ cuando `total_vol_5m` < 417.524 (IC base=+0.134)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4133` → IC=+0.188 (n=91)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio` |x|> 0.4133 (IC base=+0.104)

- **PATRÓN** `total_vol_5m` < `394.3776` → IC=+0.242 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 394.3776 (IC base=+0.104)

- **PATRÓN** `ballena_activa_n` < `70.0` → IC=+0.188 (n=46)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 70.0 (IC base=+0.104)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.399` → IC=+0.198 (n=117)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.99€ cuando `delta_ratio` |x|> 0.399 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.217 (n=44)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.150)

- **PATRÓN** `total_vol_5m` < `7671.127` → IC=+0.164 (n=117)

  - _Acción_: Kelly boost +0.82€ cuando `total_vol_5m` < 7671.127 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.186 (n=49)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 37.0 (IC base=+0.150)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.4` → IC=+0.164 (n=111)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.82€ cuando `delta_ratio` |x|> 0.4 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.146 (n=111)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 13.0 (IC base=+0.117)

- **PATRÓN** `total_vol_5m` < `356326.0` → IC=+0.140 (n=109)

  - _Acción_: Kelly boost +0.70€ cuando `total_vol_5m` < 356326.0 (IC base=+0.117)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.237 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.117)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` > `0.0056` → IC=-0.322 (n=150)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0056
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=151)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.179 (n=76)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0039 (IC base=-0.120)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `T_h` > `54.3209` → IC=-0.357 (n=47)

  - _Acción_: SKIP cuando `T_h` > 54.3209
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=48)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.265 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=-0.119)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0107` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0107
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=19)

- **FILTRO** `T_h` < `267.9719` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `T_h` < 267.9719
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=14)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0127` → IC=-0.182 (n=20)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0127
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=39)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0094` → IC=-0.234 (n=231)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0094
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=79)

- **FILTRO** `T_h` > `71.1632` → IC=-0.200 (n=231)

  - _Acción_: SKIP cuando `T_h` > 71.1632
  - _Potencial_: sin este filtro IC_bueno=-0.142 (n=79)

- **FILTRO** `pct_vs_K` |x|> `2.84` → IC=-0.421 (n=125)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.84
  - _Potencial_: sin este filtro IC_bueno=-0.102 (n=126)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.0078` → IC=-0.194 (n=83)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0078
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=30)

- **FILTRO** `T_h` > `63.9918` → IC=-0.209 (n=84)

  - _Acción_: SKIP cuando `T_h` > 63.9918
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=29)

- **FILTRO** `T_h` > `144.6172` → IC=-0.318 (n=20)

  - _Acción_: SKIP cuando `T_h` > 144.6172
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=68)

- **FILTRO** `pct_vs_K` |x|> `2.259` → IC=-0.433 (n=43)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.259
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=45)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `T_h` < `87.9808` → IC=-0.357 (n=26)

  - _Acción_: SKIP cuando `T_h` < 87.9808
  - _Potencial_: sin este filtro IC_bueno=-0.221 (n=59)

- **FILTRO** `sigma_h` > `0.0094` → IC=-0.283 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0094
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=65)

- **FILTRO** `sigma_h` < `0.004` → IC=-0.370 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.004
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=65)

- **FILTRO** `T_h` > `61.3303` → IC=-0.318 (n=64)

  - _Acción_: SKIP cuando `T_h` > 61.3303
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=22)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0126` → IC=-0.180 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0126
  - _Potencial_: sin este filtro IC_bueno=-0.112 (n=47)

- **FILTRO** `sigma_h` < `0.01` → IC=-0.230 (n=35)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=35)

- **FILTRO** `T_h` > `135.927` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `T_h` > 135.927
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=53)

- **FILTRO** `sigma_h` < `0.0129` → IC=-0.344 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0129
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=16)

- **FILTRO** `T_h` > `84.9421` → IC=-0.361 (n=34)

  - _Acción_: SKIP cuando `T_h` > 84.9421
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=12)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.15` → IC=+0.451 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.15 (IC base=+0.371)

- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.468 (n=29)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.371)

- **PATRÓN** `T_h` > `0.8774` → IC=+0.468 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8774 (IC base=+0.371)

- **PATRÓN** `dist_50` > `0.4377` → IC=+0.469 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4377 (IC base=+0.371)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.463 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.371)

- **PATRÓN** `edge` > `0.1023` → IC=+0.454 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1023 (IC base=+0.406)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.466 (n=57)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0092 (IC base=+0.406)

- **PATRÓN** `T_h` > `0.8072` → IC=+0.423 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8072 (IC base=+0.406)

- **PATRÓN** `dist_50` > `0.4084` → IC=+0.487 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4084 (IC base=+0.406)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.438 (n=79)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.406)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `dist_50` > `0.47` → IC=+0.457 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.477)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.460 (n=23)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.477)

- **PATRÓN** `edge` > `0.2335` → IC=+0.474 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2335 (IC base=+0.477)

- **PATRÓN** `sigma_h` < `0.0144` → IC=+0.483 (n=56)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0144 (IC base=+0.477)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.466 (n=56)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.477)

- **PATRÓN** `T_h` > `0.8977` → IC=+0.466 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8977 (IC base=+0.477)

- **PATRÓN** `dist_50` > `0.4421` → IC=+0.483 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4421 (IC base=+0.477)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.465 (n=55)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.477)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.470 (n=31)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.477)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=140)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=237)

- **PATRÓN** `streak_estiramiento` < `0.4763` → IC=+0.133 (n=47)

  - _Acción_: Kelly boost +0.66€ cuando `streak_estiramiento` < 0.4763 (IC base=+0.016)

- **PATRÓN** `streak_estiramiento` < `0.5545` → IC=+0.144 (n=99)

  - _Acción_: Kelly boost +0.72€ cuando `streak_estiramiento` < 0.5545 (IC base=+0.038)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=8)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `volumen_racha` > `991078.0` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `volumen_racha` > 991078.0
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=26)

- **PATRÓN** `volumen_racha` < `991078.0` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_racha` < 991078.0 (IC base=+0.000)

- **PATRÓN** `streak_estiramiento` < `0.4152` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `streak_estiramiento` < 0.4152 (IC base=+0.000)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.179 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=80)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=86)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=34)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=613)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=619)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=317)

### STREAK_FADE_60M
- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `libro_liquidez` < `2389.5844` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `libro_liquidez` < 2389.5844
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **PATRÓN** `streak_len` < `4.0` → IC=+0.132 (n=17)

  - _Acción_: Kelly boost +0.66€ cuando `streak_len` < 4.0 (IC base=+0.013)

### STREAK_FADE_60M#ETH#60min
- **FILTRO** `hora_utc` > `5.0` → IC=-0.147 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=489)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=988)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=582)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=606)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=2452)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=1260)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=1268)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.191 (n=393)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0041 (IC base=+0.180)

- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.222 (n=534)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0078 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.0523` → IC=+0.189 (n=393)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.0523 (IC base=+0.180)

- **PATRÓN** `delta_ratio_macro` |x|> `0.058` → IC=+0.181 (n=1177)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.91€ cuando `delta_ratio_macro` |x|> 0.058 (IC base=+0.180)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1366` → IC=+0.236 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1366 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.188 (n=835)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 11.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.193 (n=565)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 6.0 (IC base=+0.180)

- **PATRÓN** `ibs_15` > `0.619` → IC=+0.254 (n=1177)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.619 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.4198` → IC=+0.172 (n=275)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.4198 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` < `0.1025` → IC=+0.181 (n=764)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.1025 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.106` → IC=+0.260 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.106 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `4681.5356` → IC=+0.181 (n=534)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 4681.5356 (IC base=+0.180)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=398)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.213 (n=193)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0036 (IC base=+0.194)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.194 (n=96)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.005 (IC base=+0.194)

- **PATRÓN** `drift_60min` |x|≤ `0.0587` → IC=+0.278 (n=97)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0587 (IC base=+0.194)

- **PATRÓN** `drift_15min` |x|≤ `0.3775` → IC=+0.217 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3775 (IC base=+0.194)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2237` → IC=+0.245 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2237 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.214 (n=299)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.194)

- **PATRÓN** `ibs_15` > `0.7064` → IC=+0.252 (n=288)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7064 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` > `0.3695` → IC=+0.250 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3695 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` < `0.0989` → IC=+0.200 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0989 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.68` → IC=+0.244 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.68 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `15468.9258` → IC=+0.245 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15468.9258 (IC base=+0.194)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.177 (n=94)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0034 (IC base=+0.139)

- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.154 (n=128)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0057 (IC base=+0.139)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2344` → IC=+0.177 (n=94)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.89€ cuando `delta_ratio_macro` |x|> 0.2344 (IC base=+0.139)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2712` → IC=+0.161 (n=187)

  - _Acción_: Kelly boost +0.81€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2712 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.154 (n=209)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 11.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.146 (n=295)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 17.0 (IC base=+0.139)

- **PATRÓN** `ibs_15` > `0.6842` → IC=+0.256 (n=252)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6842 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` < `0.1433` → IC=+0.161 (n=222)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.1433 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.981` → IC=+0.213 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.981 (IC base=+0.139)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `hora_utc` > `16.0` → IC=-0.136 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=62)

- **FILTRO** `ibs_15` > `0.1909` → IC=-0.224 (n=27)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.1909
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=55)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.209 (n=53)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.1772` → IC=+0.171 (n=159)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.1772 (IC base=+0.143)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0662` → IC=+0.188 (n=142)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.0662 (IC base=+0.143)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3347` → IC=+0.213 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3347 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.177 (n=122)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 8.0 (IC base=+0.143)

- **PATRÓN** `ibs_15` > `0.6` → IC=+0.241 (n=160)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` < `0.5902` → IC=+0.154 (n=183)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.5902 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.389` → IC=+0.379 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.389 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.164 (n=129)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `3008.8466` → IC=+0.257 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3008.8466 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.204 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.143)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `dist_vwap_pct` > `0.5639` → IC=-0.142 (n=118)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.5639
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=624)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.936` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 8.936 (IC base=+0.006)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0157` → IC=+0.256 (n=219)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0157 (IC base=+0.191)

- **PATRÓN** `drift_60min` |x|≤ `0.085` → IC=+0.207 (n=145)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.085 (IC base=+0.191)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0441` → IC=+0.201 (n=329)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0441 (IC base=+0.191)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0965` → IC=+0.287 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0965 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.244 (n=162)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.191)

- **PATRÓN** `ibs_15` > `0.5488` → IC=+0.282 (n=329)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5488 (IC base=+0.191)

- **PATRÓN** `dist_vwap_pct` > `0.1139` → IC=+0.206 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1139 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.93` → IC=+0.245 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.93 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.192 (n=362)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.03 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `2842.8404` → IC=+0.286 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2842.8404 (IC base=+0.191)

- **PATRÓN** `ibs_15` < `0.1143` → IC=+0.168 (n=374)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.84€ cuando `ibs_15` < 0.1143 (IC base=+0.044)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.005` → IC=+0.374 (n=149)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.336)

- **PATRÓN** `drift_60min` |x|≤ `0.1514` → IC=+0.342 (n=289)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1514 (IC base=+0.336)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1435` → IC=+0.351 (n=219)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1435 (IC base=+0.336)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.218` → IC=+0.373 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.218 (IC base=+0.336)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.352 (n=349)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.336)

- **PATRÓN** `ibs_15` > `0.788` → IC=+0.376 (n=328)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.788 (IC base=+0.336)

- **PATRÓN** `dist_vwap_pct` > `0.4098` → IC=+0.371 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4098 (IC base=+0.336)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.588` → IC=+0.341 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.588 (IC base=+0.336)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.343 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.336)

- **PATRÓN** `libro_liquidez` > `3397.72` → IC=+0.351 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3397.72 (IC base=+0.336)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1228` → IC=+0.343 (n=81)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1228 (IC base=+0.337)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.335 (n=162)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.337)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.357 (n=61)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.337)

- **PATRÓN** `drift_60min` |x|≤ `0.1497` → IC=+0.348 (n=162)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1497 (IC base=+0.337)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1497` → IC=+0.347 (n=122)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1497 (IC base=+0.337)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1284` → IC=+0.415 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1284 (IC base=+0.337)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.350 (n=192)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.337)

- **PATRÓN** `ibs_15` > `0.8154` → IC=+0.370 (n=183)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8154 (IC base=+0.337)

- **PATRÓN** `dist_vwap_pct` > `0.3848` → IC=+0.398 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3848 (IC base=+0.337)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.152` → IC=+0.341 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.152 (IC base=+0.337)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.659` → IC=+0.344 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.659 (IC base=+0.337)

- **PATRÓN** `libro_liquidez` > `9641.0136` → IC=+0.363 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9641.0136 (IC base=+0.337)

- **PATRÓN** `ballena_activa_n` < `463.0` → IC=+0.402 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 463.0 (IC base=+0.337)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.369 (n=97)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0051 (IC base=+0.331)

- **PATRÓN** `drift_60min` |x|≤ `0.1546` → IC=+0.331 (n=128)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1546 (IC base=+0.331)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0665` → IC=+0.337 (n=145)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0665 (IC base=+0.331)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.298` → IC=+0.357 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.298 (IC base=+0.331)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.349 (n=157)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.331)

- **PATRÓN** `ibs_15` > `0.7504` → IC=+0.384 (n=145)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7504 (IC base=+0.331)

- **PATRÓN** `dist_vwap_pct` > `0.4248` → IC=+0.348 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4248 (IC base=+0.331)

- **PATRÓN** `dist_vwap_pct` < `0.1061` → IC=+0.350 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1061 (IC base=+0.331)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.144` → IC=+0.355 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.144 (IC base=+0.331)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.347 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.331)

- **PATRÓN** `libro_liquidez` > `3525.4286` → IC=+0.359 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3525.4286 (IC base=+0.331)

- **PATRÓN** `ballena_activa_n` < `139.0` → IC=+0.331 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 139.0 (IC base=+0.331)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0127` → IC=-0.208 (n=556)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0127
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=1670)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.179 (n=714)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=1512)

- **FILTRO** `libro_liquidez` < `3796.8122` → IC=-0.123 (n=1469)

  - _Acción_: SKIP cuando `libro_liquidez` < 3796.8122
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=757)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.138` → IC=+0.256 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.138 (IC base=-0.059)

- **PATRÓN** `ibs_15` > `0.6189` → IC=+0.259 (n=553)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6189 (IC base=-0.059)

- **PATRÓN** `dist_vwap_pct` < `0.1081` → IC=+0.186 (n=342)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.1081 (IC base=-0.059)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1166` → IC=+0.236 (n=833)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1166 (IC base=-0.042)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.182` → IC=+0.241 (n=800)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.182 (IC base=-0.042)

- **PATRÓN** `ibs_15` < `0.361` → IC=+0.281 (n=1250)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.361 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` > `0.8637` → IC=+0.265 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8637 (IC base=-0.042)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.007` → IC=-0.206 (n=335)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=1009)

- **FILTRO** `sigma_h` < `0.0037` → IC=-0.233 (n=443)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0037
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=901)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.205 (n=857)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=487)

- **FILTRO** `sigma_ewma_delta_pct` > `19.957` → IC=-0.240 (n=240)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.957
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=1104)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.175 (n=118)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0027 (IC base=+0.071)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1378` → IC=+0.336 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1378 (IC base=+0.071)

- **PATRÓN** `ibs_15` > `0.8098` → IC=+0.338 (n=115)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8098 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` > `0.0982` → IC=+0.261 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.0982 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` < `0.3306` → IC=+0.265 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3306 (IC base=+0.071)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.6537` → IC=-0.222 (n=88)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6537
  - _Potencial_: sin este filtro IC_bueno=+0.257 (n=270)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.153 (n=341)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.142 (n=269)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0066 (IC base=+0.139)

- **PATRÓN** `sigma_h` > `0.004` → IC=+0.169 (n=240)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.004 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.0772` → IC=+0.211 (n=119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0772 (IC base=+0.139)

- **PATRÓN** `drift_15min` |x|≤ `0.4631` → IC=+0.153 (n=119)

  - _Acción_: Kelly boost +0.76€ cuando `drift_15min` |x|≤ 0.4631 (IC base=+0.139)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3059` → IC=+0.240 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3059 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.185 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 15.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.140 (n=109)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_15` > `0.6537` → IC=+0.257 (n=270)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6537 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` < `0.1041` → IC=+0.177 (n=193)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1041 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.775` → IC=+0.148 (n=211)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 6.775 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=341)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `10550.3134` → IC=+0.194 (n=122)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 10550.3134 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.247 (n=523)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.228)

- **PATRÓN** `drift_60min` |x|≤ `0.3595` → IC=+0.232 (n=460)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3595 (IC base=+0.228)

- **PATRÓN** `drift_15min` |x|≤ `0.7761` → IC=+0.238 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7761 (IC base=+0.228)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1994` → IC=+0.257 (n=237)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1994 (IC base=+0.228)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.240 (n=248)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.228)

- **PATRÓN** `ibs_15` < `0.2758` → IC=+0.286 (n=460)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.2758 (IC base=+0.228)

- **PATRÓN** `dist_vwap_pct` > `0.7403` → IC=+0.268 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7403 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.179` → IC=+0.250 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.179 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.182` → IC=+0.232 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.182 (IC base=+0.228)

- **PATRÓN** `libro_liquidez` > `3578.3819` → IC=+0.229 (n=522)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3578.3819 (IC base=+0.228)

- **PATRÓN** `ballena_activa_n` < `158.0` → IC=+0.229 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 158.0 (IC base=+0.228)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_15min` |x|> `0.8773` → IC=-0.250 (n=134)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8773
  - _Potencial_: sin este filtro IC_bueno=-0.122 (n=403)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.214 (n=204)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.118 (n=333)

- **FILTRO** `sigma_ewma_delta_pct` > `18.158` → IC=-0.134 (n=274)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.158
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=2217)

- **PATRÓN** `ibs_15` > `0.8889` → IC=+0.342 (n=17)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8889 (IC base=-0.155)

- **PATRÓN** `dist_vwap_pct` < `0.1511` → IC=+0.122 (n=43)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.1511 (IC base=-0.155)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1181` → IC=+0.222 (n=167)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1181 (IC base=-0.042)

- **PATRÓN** `ibs_15` < `0.3667` → IC=+0.254 (n=250)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3667 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` < `0.1618` → IC=+0.213 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1618 (IC base=-0.042)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0195` → IC=-0.265 (n=334)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0195
  - _Potencial_: sin este filtro IC_bueno=-0.102 (n=335)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.261 (n=174)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.156 (n=495)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1292` → IC=+0.271 (n=164)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1292 (IC base=-0.045)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1093` → IC=+0.342 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1093 (IC base=-0.045)

- **PATRÓN** `ibs_15` < `0.3457` → IC=+0.313 (n=361)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3457 (IC base=-0.045)

- **PATRÓN** `dist_vwap_pct` > `1.0728` → IC=+0.421 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0728 (IC base=-0.045)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.138 (n=56)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0064 (IC base=+0.105)

- **PATRÓN** `drift_60min` |x|≤ `0.4393` → IC=+0.167 (n=64)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.4393 (IC base=+0.105)

- **PATRÓN** `drift_15min` |x|≤ `0.5868` → IC=+0.189 (n=43)

  - _Acción_: Kelly boost +0.94€ cuando `drift_15min` |x|≤ 0.5868 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `0.1506` → IC=+0.206 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1506 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `13354.4495` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 13354.4495 (IC base=+0.105)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.138 (n=56)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0064 (IC base=+0.105)

- **PATRÓN** `drift_60min` |x|≤ `0.4393` → IC=+0.167 (n=64)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.4393 (IC base=+0.105)

- **PATRÓN** `drift_15min` |x|≤ `0.5868` → IC=+0.189 (n=43)

  - _Acción_: Kelly boost +0.94€ cuando `drift_15min` |x|≤ 0.5868 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `0.1506` → IC=+0.206 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1506 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `13354.4495` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 13354.4495 (IC base=+0.105)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.290 (n=184)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.286)

- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.289 (n=249)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0054 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `0.0563` → IC=+0.317 (n=184)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0563 (IC base=+0.286)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1415` → IC=+0.288 (n=366)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1415 (IC base=+0.286)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.218` → IC=+0.321 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.218 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.304 (n=571)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.286)

- **PATRÓN** `ibs_15` > `0.8374` → IC=+0.324 (n=549)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8374 (IC base=+0.286)

- **PATRÓN** `dist_vwap_pct` > `0.2631` → IC=+0.324 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2631 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.66` → IC=+0.324 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.66 (IC base=+0.286)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.288 (n=673)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `12762.7474` → IC=+0.297 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12762.7474 (IC base=+0.286)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.287 (n=205)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.276)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.282 (n=140)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.276)

- **PATRÓN** `drift_60min` |x|≤ `0.0584` → IC=+0.319 (n=103)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0584 (IC base=+0.276)

- **PATRÓN** `drift_15min` |x|≤ `0.4172` → IC=+0.281 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4172 (IC base=+0.276)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2433` → IC=+0.281 (n=103)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2433 (IC base=+0.276)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3622` → IC=+0.292 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3622 (IC base=+0.276)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.333 (n=148)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.276)

- **PATRÓN** `ibs_15` > `0.965` → IC=+0.331 (n=140)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.965 (IC base=+0.276)

- **PATRÓN** `dist_vwap_pct` > `0.2546` → IC=+0.336 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2546 (IC base=+0.276)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.701` → IC=+0.343 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.701 (IC base=+0.276)

- **PATRÓN** `libro_liquidez` > `15759.911` → IC=+0.309 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15759.911 (IC base=+0.276)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.304 (n=243)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.297)

- **PATRÓN** `sigma_h` > `0.0036` → IC=+0.304 (n=243)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0036 (IC base=+0.297)

- **PATRÓN** `drift_60min` |x|≤ `0.0716` → IC=+0.307 (n=107)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0716 (IC base=+0.297)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1881` → IC=+0.312 (n=110)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1881 (IC base=+0.297)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2925` → IC=+0.339 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2925 (IC base=+0.297)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.342 (n=175)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.297)

- **PATRÓN** `ibs_15` > `0.8527` → IC=+0.341 (n=243)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8527 (IC base=+0.297)

- **PATRÓN** `dist_vwap_pct` > `0.2769` → IC=+0.312 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2769 (IC base=+0.297)

- **PATRÓN** `dist_vwap_pct` < `0.4471` → IC=+0.300 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4471 (IC base=+0.297)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.664` → IC=+0.322 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.664 (IC base=+0.297)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.297)

- **PATRÓN** `libro_liquidez` > `11789.5205` → IC=+0.295 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11789.5205 (IC base=+0.297)

- **PATRÓN** `ballena_activa_n` < `154.0` → IC=+0.297 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 154.0 (IC base=+0.297)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.085` → IC=-0.273 (n=64)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.085
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=195)

- **FILTRO** `sigma_h` > `0.0043` → IC=-0.244 (n=88)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0043
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=171)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.161 (n=107)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=322)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.2171` → IC=-0.167 (n=64)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.2171
  - _Potencial_: sin este filtro IC_bueno=-0.162 (n=66)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1851` → IC=-0.132 (n=74)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1851
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=74)

- **FILTRO** `drift_15min` |x|> `0.2287` → IC=-0.250 (n=18)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.2287
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

### UPDOWN_OU_5M#DOGE#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1055` → IC=-0.289 (n=17)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1055
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `sigma_h` > `0.0068` → IC=-0.262 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=7)

- **FILTRO** `drift_60min` |x|> `0.0858` → IC=-0.200 (n=18)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.0858
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `drift_15min` |x|> `0.3434` → IC=-0.184 (n=17)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3434
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2236` → IC=-0.237 (n=17)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2236
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### UPDOWN_OU_5M#ETH#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2179` → IC=-0.155 (n=27)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2179
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=14)

- **FILTRO** `sigma_h` < `0.0039` → IC=-0.300 (n=18)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0039
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2099` → IC=-0.389 (n=16)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2099
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1066` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1066
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=6)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.0931` → IC=-0.214 (n=19)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0931
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `sigma_h` > `0.0046` → IC=-0.239 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0046
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### WEEKLY_PRICE
- **PATRÓN** `T_h` > `73.926` → IC=+0.140 (n=231)

  - _Acción_: Kelly boost +0.70€ cuando `T_h` > 73.926 (IC base=+0.138)

- **PATRÓN** `ratio` < `0.9932` → IC=+0.319 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9932 (IC base=+0.138)

- **PATRÓN** `T_h` > `145.8408` → IC=+0.407 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.8408 (IC base=+0.350)

- **PATRÓN** `ratio` > `1.01` → IC=+0.386 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.01 (IC base=+0.350)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `144.522` → IC=+0.149 (n=35)

  - _Acción_: Kelly boost +0.74€ cuando `T_h` > 144.522 (IC base=+0.096)

- **PATRÓN** `ratio` < `0.9933` → IC=+0.282 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9933 (IC base=+0.096)

- **PATRÓN** `T_h` > `87.9969` → IC=+0.314 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 87.9969 (IC base=+0.307)

- **PATRÓN** `ratio` > `1.0413` → IC=+0.476 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0413 (IC base=+0.307)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `87.9882` → IC=+0.216 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 87.9882 (IC base=+0.193)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.389 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.193)

- **PATRÓN** `T_h` > `93.2998` → IC=+0.350 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 93.2998 (IC base=+0.331)

- **PATRÓN** `ratio` > `1.0151` → IC=+0.382 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0151 (IC base=+0.331)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1118` → IC=+0.454 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1118 (IC base=+0.405)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.619 sube el IC de +0.180 a +0.254 en UPDOWN_GBM#15min (n=1177). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7064 sube el IC de +0.194 a +0.252 en UPDOWN_GBM#BTC#15min (n=288). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6842 sube el IC de +0.139 a +0.256 en UPDOWN_GBM#ETH#15min (n=252). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.143 a +0.241 en UPDOWN_GBM#SOL#15min (n=160). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5488 sube el IC de +0.191 a +0.282 en UPDOWN_GBM#XRP#15min (n=329). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1143 sube el IC de +0.044 a +0.168 en UPDOWN_GBM#XRP#15min (n=374). Ya aplicado como kelly_boost=+0.84€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6189 sube el IC de -0.059 a +0.259 en UPDOWN_GBM_15M_TARDIO (n=553). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.361 sube el IC de -0.042 a +0.281 en UPDOWN_GBM_15M_TARDIO (n=1250). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.8098 sube el IC de +0.071 a +0.338 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=115). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6537 sube el IC de +0.139 a +0.257 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=270). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.2758 sube el IC de +0.228 a +0.286 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=460). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8889 sube el IC de -0.155 a +0.342 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3667 sube el IC de -0.042 a +0.254 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=250). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3457 sube el IC de -0.045 a +0.313 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=361). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8374 sube el IC de +0.286 a +0.324 en UPDOWN_GBM_IBS_ALTO (n=549). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.965 sube el IC de +0.276 a +0.331 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=140). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8527 sube el IC de +0.297 a +0.341 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=243). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.788 sube el IC de +0.336 a +0.376 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=328). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8154 sube el IC de +0.337 a +0.370 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=183). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7504 sube el IC de +0.331 a +0.384 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=145). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min` — IC=+0.378 n=39. Faltan ~1 resoluciones para umbral n≥40. ETA: ~1h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL` — IC=+0.378 n=39. Faltan ~1 resoluciones para umbral n≥40. ETA: ~1h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1169 | +0.085 | +147.50€ | 2 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1169 | +0.085 | +147.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 844 | +0.091 | +118.37€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 844 | +0.091 | +118.37€ | 3 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 242 | +0.045 | +4.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 242 | +0.045 | +4.70€ | 4 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 57 | +0.178 | +25.94€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 57 | +0.178 | +25.94€ | 0 | 7 |
| ✅ BALLENAS_TARDIAS | 21540 | -0.096 | -3144.28€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1276 | -0.050 | -193.25€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 20264 | -0.099 | -2951.03€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 3326 | -0.100 | -569.22€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 3326 | -0.100 | -569.22€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1276 | -0.050 | -193.25€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1276 | -0.050 | -193.25€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 374 | -0.136 | -161.05€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 374 | -0.136 | -161.05€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 6174 | -0.042 | -613.16€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 6174 | -0.042 | -613.16€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 5713 | -0.098 | -477.75€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 5713 | -0.098 | -477.75€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 4677 | -0.173 | -1129.85€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 4677 | -0.173 | -1129.85€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 13490 | -0.038 | +4179.97€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 3593 | -0.005 | +1831.06€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 9897 | -0.051 | +2348.90€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 13490 | -0.038 | +4179.97€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 3593 | -0.005 | +1831.06€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 9897 | -0.051 | +2348.90€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 1198 | -0.098 | -158.34€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#15min | 104 | -0.038 | -9.03€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 1094 | -0.103 | -149.30€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB#5min | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 682 | -0.083 | -79.96€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#15min | 80 | -0.024 | -3.81€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 602 | -0.091 | -76.15€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH | 338 | -0.138 | -66.29€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#15min | 24 | -0.077 | -5.22€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#5min | 314 | -0.142 | -61.06€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL | 117 | -0.038 | -11.95€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL#5min | 117 | -0.038 | -11.95€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP | 39 | -0.159 | -4.70€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP#5min | 39 | -0.159 | -4.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 78238 | +0.113 | -3991.76€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 12130 | +0.183 | -368.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 301 | -0.120 | -46.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 60482 | +0.100 | -3423.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 5325 | +0.113 | -153.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 10075 | +0.097 | -919.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 41 | -0.151 | -1.09€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 10019 | +0.099 | -906.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 15823 | +0.132 | -305.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 3741 | +0.203 | -111.74€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 10020 | +0.111 | -172.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2020 | +0.113 | +1.11€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 10113 | +0.088 | -990.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 47 | -0.051 | -1.60€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 10051 | +0.089 | -977.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 16733 | +0.124 | -306.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 4687 | +0.173 | -73.27€ | 1 | 7 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 10118 | +0.107 | -170.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 1916 | +0.098 | -53.40€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 15404 | +0.115 | -891.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 3573 | +0.186 | -190.99€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 204 | -0.083 | +7.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 10238 | +0.092 | -607.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1389 | +0.133 | -100.88€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 10090 | +0.103 | -578.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 41 | -0.012 | +10.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 10036 | +0.104 | -588.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 12358 | +0.190 | -843.48€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 12358 | +0.190 | -843.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 3024 | +0.168 | -326.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 3024 | +0.168 | -326.87€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 749 | +0.184 | +0.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 749 | +0.184 | +0.68€ | 4 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 2954 | +0.179 | -263.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 2954 | +0.179 | -263.74€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 2652 | +0.237 | -84.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 2652 | +0.237 | -84.33€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 2900 | +0.191 | -182.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 2900 | +0.191 | -182.98€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 573 | +0.434 | -10.55€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 573 | +0.434 | -10.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 220 | +0.437 | -2.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 220 | +0.437 | -2.05€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 217 | +0.441 | +0.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 217 | +0.441 | +0.28€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 128 | +0.408 | -7.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 128 | +0.408 | -7.74€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 42303 | +0.195 | -3486.61€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 42303 | +0.195 | -3486.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 7365 | +0.171 | -921.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 7365 | +0.171 | -921.50€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 6721 | +0.224 | -239.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 6721 | +0.224 | -239.80€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 7323 | +0.171 | -914.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 7323 | +0.171 | -914.62€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 6818 | +0.216 | -292.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 6818 | +0.216 | -292.17€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 6980 | +0.204 | -462.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 6980 | +0.204 | -462.54€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 7096 | +0.191 | -655.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 7096 | +0.191 | -655.98€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 15871 | +0.124 | +298.02€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 15871 | +0.124 | +298.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 7873 | +0.128 | +194.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 7873 | +0.128 | +194.90€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 7998 | +0.120 | +103.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 7998 | +0.120 | +103.12€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1283 | +0.285 | -31.16€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1283 | +0.285 | -31.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 570 | +0.266 | -31.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 570 | +0.266 | -31.23€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 612 | +0.293 | +0.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 612 | +0.293 | +0.09€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 101 | +0.335 | -0.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 101 | +0.335 | -0.02€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 560 | +0.432 | -6.01€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 560 | +0.432 | -6.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 262 | +0.432 | -3.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 262 | +0.432 | -3.29€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 259 | +0.435 | -2.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 259 | +0.435 | -2.43€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 39 | +0.378 | -0.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 39 | +0.378 | -0.28€ | 0 | 1 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 905 | +0.070 | -44.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 319 | +0.054 | -28.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 586 | +0.078 | -15.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 55 | +0.132 | +4.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 55 | +0.132 | +4.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 707 | +0.078 | -19.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 121 | +0.077 | -4.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 586 | +0.078 | -15.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 143 | +0.003 | -28.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 143 | +0.003 | -28.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 28356 | +0.099 | -808.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 2380 | +0.095 | +35.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 25976 | +0.100 | -844.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 16103 | +0.103 | -222.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 2380 | +0.095 | +35.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 13723 | +0.105 | -258.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 5043 | +0.116 | +47.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 5043 | +0.116 | +47.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 7210 | +0.079 | -633.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 7210 | +0.079 | -633.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 738 | +0.240 | -92.60€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 738 | +0.240 | -92.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 738 | +0.240 | -92.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 738 | +0.240 | -92.60€ | 0 | 4 |
| ✅ GBM_LATE_15M | 20796 | +0.076 | +9391.64€ | 0 | 15 |
| ✅ GBM_LATE_15M#15min | 20796 | +0.076 | +9391.64€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 3417 | +0.193 | +2476.51€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 3417 | +0.193 | +2476.51€ | 0 | 20 |
| ✅ GBM_LATE_15M#BTC | 3073 | +0.174 | +2065.61€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 3073 | +0.174 | +2065.61€ | 0 | 27 |
| ✅ GBM_LATE_15M#DOGE | 3566 | +0.196 | +2625.29€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 3566 | +0.196 | +2625.29€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 3107 | +0.008 | +500.58€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 3107 | +0.008 | +500.58€ | 1 | 13 |
| ✅ GBM_LATE_15M#SOL | 3040 | -0.037 | +646.12€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 3040 | -0.037 | +646.12€ | 4 | 14 |
| ✅ GBM_LATE_15M#XRP | 4593 | -0.048 | +1077.53€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 4593 | -0.048 | +1077.53€ | 4 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 21893 | +0.079 | +10880.81€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 21893 | +0.079 | +10880.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 4055 | +0.013 | +1973.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 4055 | +0.013 | +1973.44€ | 1 | 8 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 4615 | +0.007 | +881.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 4615 | +0.007 | +881.23€ | 1 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 3101 | +0.258 | +3072.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 3101 | +0.258 | +3072.99€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 3473 | -0.010 | +480.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 3473 | -0.010 | +480.75€ | 2 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 3603 | +0.015 | +1271.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 3603 | +0.015 | +1271.60€ | 3 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 3046 | +0.271 | +3200.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 3046 | +0.271 | +3200.81€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 16874 | +0.168 | +12354.83€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 16874 | +0.168 | +12354.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 2506 | +0.206 | +1985.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 2506 | +0.206 | +1985.85€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 2677 | +0.153 | +1919.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 2677 | +0.153 | +1919.31€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 2612 | +0.205 | +2046.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 2612 | +0.205 | +2046.20€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 2800 | +0.140 | +1901.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 2800 | +0.140 | +1901.89€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 3183 | +0.111 | +2061.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 3183 | +0.111 | +2061.90€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 3096 | +0.203 | +2439.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 3096 | +0.203 | +2439.68€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 4309 | +0.126 | +1767.78€ | 0 | 24 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 4309 | +0.126 | +1767.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 175 | +0.116 | +70.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 175 | +0.116 | +70.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1178 | +0.121 | +495.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1178 | +0.121 | +495.81€ | 0 | 20 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 368 | +0.149 | +182.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 368 | +0.149 | +182.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1170 | +0.150 | +539.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1170 | +0.150 | +539.62€ | 0 | 21 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 915 | +0.088 | +260.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 915 | +0.088 | +260.51€ | 1 | 11 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 503 | +0.136 | +218.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 503 | +0.136 | +218.58€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO | 20853 | +0.173 | +15105.81€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#15min | 20853 | +0.173 | +15105.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 3263 | +0.218 | +2721.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 3263 | +0.218 | +2721.48€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 3268 | +0.152 | +2157.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 3268 | +0.152 | +2157.13€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 3384 | +0.222 | +2870.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 3384 | +0.222 | +2870.83€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 3348 | +0.138 | +2180.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 3348 | +0.138 | +2180.52€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 3659 | +0.105 | +2121.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 3659 | +0.105 | +2121.18€ | 0 | 17 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 3931 | +0.202 | +3054.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 3931 | +0.202 | +3054.68€ | 0 | 25 |
| ✅ GBM_LATE_5M | 6001 | +0.140 | +3233.35€ | 1 | 25 |
| ✅ GBM_LATE_5M#5min | 6001 | +0.140 | +3233.35€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 563 | +0.181 | +383.76€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 563 | +0.181 | +383.76€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1589 | +0.138 | +961.60€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1589 | +0.138 | +961.60€ | 0 | 28 |
| ✅ GBM_LATE_5M#DOGE | 888 | +0.171 | +564.16€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 888 | +0.171 | +564.16€ | 0 | 20 |
| ✅ GBM_LATE_5M#ETH | 1832 | +0.146 | +990.59€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 1832 | +0.146 | +990.59€ | 0 | 31 |
| ✅ GBM_LATE_5M#SOL | 324 | +0.025 | +35.49€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 324 | +0.025 | +35.49€ | 2 | 4 |
| ✅ GBM_LATE_5M#XRP | 805 | +0.111 | +297.75€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 805 | +0.111 | +297.75€ | 0 | 0 |
| ✅ GBM_LATE_60M | 1328 | +0.065 | +588.79€ | 2 | 15 |
| ✅ GBM_LATE_60M#60min | 1328 | +0.065 | +588.79€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 473 | +0.083 | +197.75€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 473 | +0.083 | +197.75€ | 1 | 15 |
| ✅ GBM_LATE_60M#ETH | 442 | +0.070 | +225.47€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 442 | +0.070 | +225.47€ | 2 | 15 |
| ✅ GBM_LATE_60M#SOL | 413 | +0.040 | +165.56€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 413 | +0.040 | +165.56€ | 1 | 12 |
| 🚫 GBM_LATE_60M_FADE | 314 | -0.260 | -20.91€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 314 | -0.260 | -20.91€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 118 | -0.217 | -7.46€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 118 | -0.217 | -7.46€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 106 | -0.278 | -9.71€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 106 | -0.278 | -9.71€ | 2 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 90 | -0.283 | -3.74€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 90 | -0.283 | -3.74€ | 4 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 617 | +0.056 | +117.80€ | 2 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 617 | +0.056 | +117.80€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 244 | +0.045 | +36.37€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 244 | +0.045 | +36.37€ | 3 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 181 | +0.035 | +3.29€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 181 | +0.035 | +3.29€ | 3 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 192 | +0.088 | +78.14€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 192 | +0.088 | +78.14€ | 1 | 15 |
| ✅ LATE_WINDOW_5MIN | 70 | +0.264 | +51.39€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 70 | +0.264 | +51.39€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 70 | +0.264 | +51.39€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 70 | +0.264 | +51.39€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 1487 | +0.106 | +438.03€ | 0 | 4 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 1487 | +0.106 | +438.03€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 1487 | +0.106 | +438.03€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 1487 | +0.106 | +438.03€ | 0 | 4 |
| ✅ LIQUIDACIONES_15M | 357 | -0.082 | -33.90€ | 6 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 357 | -0.082 | -33.90€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 89 | -0.071 | -6.27€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 89 | -0.071 | -6.27€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 67 | -0.080 | -7.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 67 | -0.080 | -7.45€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 120 | -0.016 | -3.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 120 | -0.016 | -3.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 1574 | -0.004 | -5.94€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 1574 | -0.004 | -5.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 75 | -0.033 | -5.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 75 | -0.033 | -5.22€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 170 | -0.012 | +5.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 170 | -0.012 | +5.32€ | 5 | 3 |
| ✅ LIQUIDACIONES_5M#DOGE | 102 | -0.048 | -5.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 102 | -0.048 | -5.98€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 661 | +0.019 | +14.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 661 | +0.019 | +14.20€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 460 | -0.006 | -8.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 460 | -0.006 | -8.20€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 106 | -0.056 | -6.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 106 | -0.056 | -6.04€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M | 922 | -0.048 | -28.16€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 922 | -0.048 | -28.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 269 | -0.050 | -13.89€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 269 | -0.050 | -13.89€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 296 | -0.037 | -4.84€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 296 | -0.037 | -4.84€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 357 | -0.054 | -9.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 357 | -0.054 | -9.43€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M | 13608 | -0.010 | -178.28€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 13608 | -0.010 | -178.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 2556 | -0.021 | -48.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 2556 | -0.021 | -48.27€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 2869 | -0.013 | -19.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 2869 | -0.013 | -19.10€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3363 | -0.016 | -59.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3363 | -0.016 | -59.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 23240 | -0.011 | +1005.04€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 23240 | -0.011 | +1005.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 4050 | +0.011 | +510.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 4050 | +0.011 | +510.74€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 3724 | -0.025 | -24.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 3724 | -0.025 | -24.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 4074 | +0.005 | +312.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 4074 | +0.005 | +312.45€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 3502 | -0.047 | -96.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 3502 | -0.047 | -96.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 3888 | -0.013 | +155.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 3888 | -0.013 | +155.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 4002 | +0.001 | +146.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 4002 | +0.001 | +146.87€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 5141 | -0.046 | -134.19€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 5141 | -0.046 | -134.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1201 | +0.000 | -16.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1201 | +0.000 | -16.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1154 | -0.057 | -26.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1154 | -0.057 | -26.93€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 43 | -0.122 | -5.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 43 | -0.122 | -5.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 488 | -0.131 | -27.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 488 | -0.131 | -27.60€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1409 | -0.061 | -32.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1409 | -0.061 | -32.08€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 846 | -0.015 | -25.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 846 | -0.015 | -25.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3339 | +0.004 | -2.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3339 | +0.004 | -2.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 186 | +0.011 | -0.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 186 | +0.011 | -0.87€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 136 | +0.000 | -1.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 136 | +0.000 | -1.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1314 | +0.007 | +7.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1314 | +0.007 | +7.09€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1388 | +0.007 | +0.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1388 | +0.007 | +0.29€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 59888 | -0.073 | +1297.20€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 59888 | -0.073 | +1297.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 10091 | -0.080 | +606.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 10091 | -0.080 | +606.01€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 9335 | -0.090 | -379.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 9335 | -0.090 | -379.13€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 10122 | -0.070 | +538.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 10122 | -0.070 | +538.03€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 8858 | -0.093 | -237.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 8858 | -0.093 | -237.93€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 11056 | -0.049 | +331.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 11056 | -0.049 | +331.23€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 10426 | -0.063 | +438.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 10426 | -0.063 | +438.99€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 6774 | -0.021 | -96.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 6774 | -0.021 | -96.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1529 | -0.019 | -1.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1529 | -0.019 | -1.43€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1002 | -0.020 | -30.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1002 | -0.020 | -30.79€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1506 | -0.015 | -3.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1506 | -0.015 | -3.43€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1004 | -0.039 | -16.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1004 | -0.039 | -16.77€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 737 | -0.021 | -24.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 737 | -0.021 | -24.17€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1012 | +0.112 | +353.04€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#5min | 876 | +0.121 | +340.44€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 203 | +0.134 | +97.97€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 203 | +0.134 | +97.97€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#DOGE | 173 | +0.094 | +40.52€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 173 | +0.094 | +40.52€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 180 | +0.104 | +63.57€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 180 | +0.104 | +63.57€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#SOL | 155 | +0.150 | +81.31€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 155 | +0.150 | +81.31€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 165 | +0.117 | +57.08€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 165 | +0.117 | +57.08€ | 0 | 4 |
| ✅ PRICE_TARGET_GBM | 479 | -0.076 | -5.11€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 211 | -0.120 | -32.46€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 169 | -0.155 | -35.09€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 42 | +0.023 | +2.63€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 171 | -0.067 | +8.48€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 129 | -0.072 | +1.92€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 42 | -0.045 | +6.56€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 97 | +0.005 | +18.88€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 77 | -0.006 | +12.78€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 20 | +0.045 | +6.10€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 375 | -0.097 | -20.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 104 | +0.000 | +15.29€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 561 | -0.221 | -48.01€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 233 | -0.202 | -34.60€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 201 | -0.195 | -32.31€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 32 | -0.235 | -2.29€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 198 | -0.240 | -23.51€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 171 | -0.251 | -27.60€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 27 | -0.155 | +4.08€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL | 130 | -0.220 | +10.10€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#atexpiry | 116 | -0.220 | +7.04€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 14 | -0.131 | +3.06€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 488 | -0.222 | -52.87€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#reach | 73 | -0.207 | +4.86€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 205 | +0.399 | +153.07€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#BTC | 28 | +0.033 | -4.76€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 28 | +0.033 | -4.76€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 49 | +0.363 | +40.96€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 49 | +0.363 | +40.96€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 128 | +0.485 | +116.86€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 128 | +0.485 | +116.86€ | 0 | 9 |
| ✅ RESOLUTION_SNIPER#sniper | 205 | +0.399 | +153.07€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 415 | +0.030 | +10.57€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 415 | +0.030 | +10.57€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 186 | +0.032 | +2.32€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 186 | +0.032 | +2.32€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 26 | +0.107 | +4.41€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 26 | +0.107 | +4.41€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 47 | -0.031 | -4.66€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 47 | -0.031 | -4.66€ | 1 | 0 |
| ✅ STREAK_FADE_15M#XRP | 156 | +0.032 | +8.49€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 156 | +0.032 | +8.49€ | 1 | 2 |
| ✅ STREAK_FADE_5M | 2511 | -0.027 | -116.93€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2511 | -0.027 | -116.93€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 564 | -0.023 | -23.35€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 564 | -0.023 | -23.35€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 153 | -0.042 | -13.91€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 153 | -0.042 | -13.91€ | 3 | 0 |
| ✅ STREAK_FADE_5M#XRP | 990 | -0.034 | -52.72€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 990 | -0.034 | -52.72€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 61 | -0.040 | -3.88€ | 2 | 1 |
| ✅ STREAK_FADE_60M#60min | 61 | -0.040 | -3.88€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 37 | -0.090 | -3.93€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 37 | -0.090 | -3.93€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 24 | +0.038 | +0.06€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 24 | +0.038 | +0.06€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 6754 | +0.024 | +106.02€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 6754 | +0.024 | +106.02€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2118 | +0.021 | +20.41€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2118 | +0.021 | +20.41€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 1419 | +0.031 | +37.15€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 1419 | +0.031 | +37.15€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 1987 | +0.016 | +10.89€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 1987 | +0.016 | +10.89€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1230 | +0.033 | +37.57€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1230 | +0.033 | +37.57€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 6223 | +0.014 | -24.34€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 6223 | +0.014 | -24.34€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 2471 | +0.020 | +3.78€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 2471 | +0.020 | +3.78€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 2460 | +0.016 | -5.42€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 2460 | +0.016 | -5.42€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1292 | -0.002 | -22.70€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1292 | -0.002 | -22.70€ | 2 | 0 |
| ✅ UPDOWN_GBM | 27437 | +0.030 | +1563.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 7410 | +0.060 | +1215.05€ | 0 | 12 |
| ✅ UPDOWN_GBM#240min | 1028 | +0.005 | +8.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 17217 | +0.023 | +338.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 1672 | +0.000 | -0.02€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 2436 | +0.071 | +250.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 328 | +0.136 | +116.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 19 | -0.023 | -0.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 2089 | +0.062 | +134.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 5006 | +0.032 | +324.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 902 | +0.081 | +201.17€ | 0 | 11 |
| ✅ UPDOWN_GBM#BTC#240min | 291 | +0.022 | +7.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 3030 | +0.029 | +109.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 741 | -0.002 | +6.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 42 | -0.114 | +0.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 3236 | +0.034 | +131.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 284 | +0.129 | +92.47€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 16 | +0.000 | -0.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 2936 | +0.025 | +39.31€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 5731 | +0.017 | +223.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 2012 | +0.047 | +221.34€ | 0 | 9 |
| ✅ UPDOWN_GBM#ETH#240min | 278 | +0.007 | +7.95€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 2814 | +0.002 | -4.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 591 | -0.003 | -5.48€ | 2 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 36 | -0.158 | +3.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 6942 | +0.017 | +168.23€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 1962 | +0.023 | +111.33€ | 0 | 11 |
| ✅ UPDOWN_GBM#SOL#240min | 272 | -0.007 | -2.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 4338 | +0.018 | +61.37€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 340 | +0.009 | -0.70€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 30 | -0.156 | -1.10€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 4084 | +0.041 | +467.50€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 1922 | +0.077 | +472.04€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 152 | -0.006 | -2.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 2010 | +0.009 | -1.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 108 | -0.145 | +3.18€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 437 | +0.336 | +124.98€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 437 | +0.336 | +124.98€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 244 | +0.337 | +65.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 244 | +0.337 | +65.59€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 193 | +0.331 | +59.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 193 | +0.331 | +59.38€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 9567 | -0.046 | +2003.00€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 9567 | -0.046 | +2003.00€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 478 | -0.054 | +333.69€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 478 | -0.054 | +333.69€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 1815 | -0.127 | +30.02€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 1815 | -0.127 | +30.02€ | 4 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 175 | +0.133 | +80.93€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 175 | +0.133 | +80.93€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1054 | +0.198 | +606.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1054 | +0.198 | +606.01€ | 2 | 23 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 3028 | -0.062 | +461.49€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 3028 | -0.062 | +461.49€ | 3 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 3017 | -0.076 | +490.87€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 3017 | -0.076 | +490.87€ | 2 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 108 | +0.073 | +17.16€ | 0 | 5 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 108 | +0.073 | +17.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 108 | +0.073 | +17.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 108 | +0.073 | +17.16€ | 0 | 5 |
| ✅ UPDOWN_GBM_IBS_ALTO | 732 | +0.286 | +582.57€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 732 | +0.286 | +582.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 409 | +0.276 | +304.86€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 409 | +0.276 | +304.86€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 323 | +0.297 | +277.71€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 323 | +0.297 | +277.71€ | 0 | 13 |
| ✅ UPDOWN_OU_5M | 688 | -0.110 | -81.33€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 688 | -0.110 | -81.33€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 186 | -0.074 | -13.13€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 186 | -0.074 | -13.13€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 66 | -0.176 | -10.12€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 66 | -0.176 | -10.12€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 58 | -0.200 | -8.54€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 58 | -0.200 | -8.54€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 1998 | +0.305 | +1042.24€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 668 | +0.251 | +109.91€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 723 | +0.294 | +310.36€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 607 | +0.375 | +621.96€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.019 n=387 — no justifica filtro, seguir monitorizando
  - _Datos_: n=387 IC=+0.019 PNL=+19.59€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 468 celda(s) pasan gate riguroso completo de 2070 evaluadas (n>=40) y 3049 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.023 < 0.08 — monitorear
  - _Datos_: n=1960 IC=+0.023 PNL=+112.35€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=723/15 IC=+0.294 PNL=+310.36€ | BTC: n=668/15 IC=+0.251 PNL=+109.91€ | SOL: n=607/15 IC=+0.375 PNL=+621.96€

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 29 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH#60min, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC#60min
  - _Bloqueante_: N_INSUFICIENTE


### ⏳ Acumulando datos

**⏳ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: 40
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Solo 0 ops con ibs_15 (feature añadida 2026-06-27). Esperar n≥40.

**⏳ H-HORA-GBM** — hora_utc causal automático en GBM (forward)
  - _Umbral_: 20
  - _Acción_: El sistema lo aplica automáticamente vía FEATURE_RULES. Verificar en strategy_params.json.
  - _Estado_: Solo 0 ops GBM con hora_utc en features. Esperar n≥20 para patrones.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.103 n=202/60 | contraria IC=+0.149 n=186 | gap=-0.046 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=251, boost estimado=+0.006. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=591/40 IC=-0.003 PNL=-5.48€ | BTC#60min: n=741/40 IC=-0.002 PNL=+6.16€ | SOL#60min: n=340/40 IC=+0.009 PNL=-0.70€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.053 n=274712 | tras_1loss IC=+0.073 n=214436 | tras_2loss IC=+0.041 n=91572/40 | gap=+0.012 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.000 n=0 | contrario_BTC IC=+0.000 n=0/40 | gap=+0.000 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


### 🔒 Bloqueadas (requieren dataset/API)

**🔒 H-OBI** — Orderbook Imbalance como señal
  - _Umbral_: Dataset Jon-Becker + API CLOB con orderbook histórico
  - _Acción_: Implementar s_obi en shadow_predict.py usando L2 orderbook
  - _Estado_: Descargar github.com/Jon-Becker/prediction-market-analysis (36GB). Analizar spread bid/ask e imbalance por mercado en 60min previos a resolución.
  - _Bloqueante_: JON_BECKER_DATASET

**🔒 H-OU-THETA** — Calibrar theta OU con datos históricos
  - _Umbral_: Dataset Jon-Becker con series de precios históricos suficientes
  - _Acción_: Ajustar THETA_OU por par en strategy_params.json (BTC/ETH/SOL independientes)
  - _Estado_: Descargar github.com/Jon-Becker/prediction-market-analysis (36GB). Fit OU sobre series históricas por par y estimar theta por MLE.
  - _Bloqueante_: JON_BECKER_DATASET

**🔒 H-HMM-REGIME** — HMM para régimen de mercado
  - _Umbral_: n≥200 ops GBM forward con hora_utc/ibs_15, o dataset Jon-Becker
  - _Acción_: Implementar hmmlearn sobre features GBM; condicionar estrategia al régimen detectado
  - _Estado_: Descargar github.com/Jon-Becker/prediction-market-analysis (36GB). Entrenar HMM 3-estado sobre (drift_60min, sigma_h) histórico. Validar en forward.
  - _Bloqueante_: JON_BECKER_DATASET

**🔒 H-CROSS-ARB** — Arbitraje Polymarket vs Kalshi
  - _Umbral_: API Kalshi activa + credenciales Polymarket live
  - _Acción_: Extender arb_scanner.py con endpoints Kalshi; comparar mismo evento cross-plataforma
  - _Estado_: Requiere acceso API Kalshi + credenciales Polymarket live
  - _Bloqueante_: API_KALSHI


### 🧪 Hipótesis custom (editables en hipotesis_custom.json)

**🟡 H-24H-GBM-BUYYES-MADRUGADA** — GBM BUY_YES en madrugada europea (05-07h UTC) — señal alcista
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona en horas 05-07h UTC (7-9h Madrid). IC=+0.087 n=14 a las 06h, +0.063 n=11 a las 05h, +0.067 n=17 a las 07h. Hipótesis: apertura europea genera momentum alcista que el GBM captura. La dirección dominante cambia de BUY_NO (madrugada americana 13h) a BUY_YES (apertura europea). Objetivo: cubrir franja horaria 05-07h UTC en el camino hacia operación 24h.
  - _Umbral_: n≥40 en franja 05-07h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → añadir GBM BUY_YES a subtypes_permitidos_live para horas 05-07h UTC
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.191 > 0.08 con n=221 PNL=+148.90€
  - _Datos_: n=221 IC=+0.191 PNL=+148.90€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.200 > 0.08 con n=288 PNL=+191.68€
  - _Datos_: n=288 IC=+0.200 PNL=+191.68€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.243 > 0.08 con n=33 PNL=+24.82€
  - _Datos_: n=33 IC=+0.243 PNL=+24.82€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.344 > 0.1 con n=1667 PNL=+1030.23€
  - _Datos_: n=1667 IC=+0.344 PNL=+1030.23€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=215 IC=+0.076 PNL=+28.90€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=215 IC=+0.076 PNL=+28.90€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=45 IC=+0.202 PNL=+32.49€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=45 IC=+0.202 PNL=+32.49€

**⏳ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: 30
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-OF-02H-BTCSOL** — ORDER_FLOW H=02h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 02h está en el blacklist basado en TODOS los pares. Con BTC+SOL solo, el historial muestra 4/5 (80%) IC=+0.054. ¿Se confirma la señal positiva con más datos?
  - _Umbral_: 15
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 02h del blacklist ORDER_FLOW
  - _Estado_: 3/15 ops en el filtro definido (IC actual=+0.045 PNL=+5.14€)
  - _Datos_: n=3 IC=+0.045 PNL=+5.14€

**⏳ H-CUSTOM-OF-07H-BTCSOL** — ORDER_FLOW H=07h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 07h está en el blacklist. Con BTC+SOL solo, el historial muestra 7/12 (58%) IC=+0.043. El blacklist puede estar basado en pares negativos que ya están excluidos.
  - _Umbral_: 20
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 07h del blacklist ORDER_FLOW
  - _Estado_: 1/20 ops en el filtro definido (IC actual=+0.008 PNL=+1.96€)
  - _Datos_: n=1 IC=+0.008 PNL=+1.96€
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: 07h sigue en ORDER_FLOW_BLACKLIST_HOURS -- mientras siga ahí, nunca genera fila para volver a evaluarse (26-Ago, triage candidatas estancadas)

**〰️ H-CUSTOM-GBM-60MIN-BUYYES** — GBM 60min BUY_YES — ¿edge superior al BUY_NO?
  - _Hipótesis_: Análisis actual muestra BUY_YES 60min: 22/36 (61%) IC=+0.105 vs BUY_NO 60min: 8/14 (57%) IC=+0.044. En 60min parece que BUY_YES es la dirección dominante, al contrario que en 15min.
  - _Umbral_: n≥30 y IC>+0.08
  - _Acción_: Si BUY_YES 60min confirma IC≥0.10 n≥40 → prioridad live por encima de BUY_NO
  - _Estado_: n=1220 IC=+0.003 PNL=-7.59€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1220 IC=+0.003 PNL=-7.59€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=452 IC=-0.007 PNL=+7.57€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=452 IC=-0.007 PNL=+7.57€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=387 IC=+0.019 PNL=+19.59€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=387 IC=+0.019 PNL=+19.59€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.180 > 0.1 con n=1564 PNL=+925.60€
  - _Datos_: n=1564 IC=+0.180 PNL=+925.60€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=900 IC=+0.082 PNL=+203.42€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=900 IC=+0.082 PNL=+203.42€

**⏳ H-CUSTOM-DRIFT15-ZONA-MUERTA** — GBM#15min drift_15min ∈ [-0.3,+0.3] — zona muerta de señal
  - _Hipótesis_: Análisis n=127 GBM#15min: cuando drift_15min está entre -0.3 y +0.3 (mercado sin dirección clara) el IC es negativo (-0.043). Cuando drift>0.3 IC=+0.100 (n=28). Cuando drift<-1 IC=+0.048 (reversión). La señal requiere mercado con dirección clara.
  - _Umbral_: 50
  - _Acción_: Filtrar señales GBM#15min cuando drift_15min ∈ [-0.3, +0.3] — validar con n≥50 antes de implementar
  - _Estado_: 0/50 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: confirmada 2026-07-01 (IC=-0.037 n=52) e implementada en shadow_predict.py (skip si drift_15min∈[-0.3,0.3)) -- verificado 26-Ago con 2177 filas post-TWAP reales, 0 caen en la zona filtrada. Frozen by design, no falta n

**⏳ H-CUSTOM-DRIFT15-MOMENTUM** — GBM#15min drift_15min > 0.3 — zona de momentum (señal fuerte)
  - _Hipótesis_: Cuando drift_15min > 0.3%/h el GBM captura bien la dirección: IC=+0.100 n=28 en todos GBM#15min; IC=+0.152 n=13 solo BTC. El mercado tiene dirección clara y el GBM la sigue. Hipótesis: este rango es donde la señal es real.
  - _Umbral_: 40
  - _Acción_: Si se confirma IC>0.10 con n≥40 → boost ×1.2 en GBM#15min cuando drift_15min>0.3
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: 20
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: 0/20 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=410 IC=+0.019 PNL=+34.16€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=410 IC=+0.019 PNL=+34.16€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=32 IC=+0.000 PNL=-0.67€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=32 IC=+0.000 PNL=-0.67€

**⏳ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: 40
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-FUNDING-NEGATIVE-BUYYES** — Funding rate negativo (<-0.01%/8h) → BUY_YES tiene más edge (short squeeze)
  - _Hipótesis_: Cuando funding < -0.01%/8h, los shorts están pagando por mantener la posición. Históricamente precede squeezes en cripto. Hipótesis: BUY_YES GBM tiene IC superior en régimen de funding negativo.
  - _Umbral_: 30
  - _Acción_: Si se confirma → boost ×1.1 en BUY_YES cuando funding_rate_8h < -0.01
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-LATE-WINDOW-5MIN** — Late-window BTC 5min — arbitraje timing vs Polymarket
  - _Hipótesis_: Inspirado en VyvanseWithMarijuana (36.5% ROI, $42k vol). A T+160-270s dentro de una ventana BTC 5min, si BTC ya se movió >0.3%, Polymarket no ha actualizado precio → edge estructural. Estrategia LATE_WINDOW_5MIN en shadow hasta n≥30. FIX 2026-07-02: la estrategia llevaba 0 predicciones desde su creacion porque HORIZONTE_MIN_HORAS=0.05 (3min) descartaba todo mercado a <3min de expirar — y su zona de entrada (160-270s de una ventana de 5min) deja 30-140s restantes, siempre bajo el suelo. Corregido en shadow_predict (zona late-window marcada _solo_late, 30s-3min, solo evaluada por esta estrategia). El reloj de acumulacion empieza de verdad hoy. Contexto extra: el estudio de ballenas de hoy confirma que comprar el lado ganador a mitad/final de ventana es el playbook comun de los 3 mayores ganadores verificados de estos mercados (Bonereaper +$19.9k/mes, wowitsamazing +$10k/mes, zhangfan151 +$8.7k/mes).
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si IC≥0.08 con n≥30 → proponer pasar a live con stake mínimo (0.50€). Si IC<0 con n≥30 → el lag de Polymarket en BTC es insuficiente.
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.264 n=70) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=70 IC=+0.264 PNL=+51.39€

**⏳ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: 40
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: 40
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: 40
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: 40
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: 40
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: 200
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: 0/200 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-MERCURY-RETROGRADO** — Mercurio retrógrado: ¿rendimiento peor durante la ventana?
  - _Hipótesis_: Mismo origen que H-CUSTOM-MOON-LLENA (paper de Fornero, 43 Jornadas SADAF 2023). Qi, Wang & Zhang (2022, 48 mercados, 1973-2019): rendimientos 3.33%/año más bajos durante Mercurio retrógrado. Kou & Ma (2022) en China (99.8% cuentas retail): hasta -31% anualizado. Ambos estudios confirman que el mecanismo es la creencia/superstición de inversores retail (mayor efecto cuanto más retail y más supersticioso el mercado), no un efecto astral literal — Polymarket encaja en ese perfil. Ventanas 2026 (fuente pública, actualizar cada año): 26-feb a 20-mar, 29-jun a 23-jul, 24-oct a 13-nov.
  - _Umbral_: 100
  - _Acción_: Si IC en mercury_retrogrado=1 < IC en mercury_retrogrado=0 con margen ≥0.05 y ≥2 ventanas distintas cubiertas → considerar boost/filtro. No implementar tras una sola ventana (jun-jul 2026) por more que n sea alto — sería solo un evento, no un patrón.
  - _Estado_: 0/100 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-SMART-MONEY-CONSENSUS** — Consenso de wallets 'smart money' — ¿confirma nuestra dirección?
  - _Hipótesis_: Javi propuso estudiar bots/wallets que operan bien en nuestros mismos mercados. En vez de creer artículos (ya verificamos 2 veces esta semana que las narrativas no aguantan el cruce con datos reales), smart_money_tracker.py mide el track record REAL de wallets activas en BTC/ETH/SOL/XRP Up-or-Down 5/15/60min vía data-api.polymarket.com/positions, filtrado a posiciones 'Up or Down'. Clasifica como 'smart' las wallets con n>=10 posiciones, win_rate>=0.55 y pnl_total>0. smart_money_consensus es el sesgo direccional reciente (Up-Down)/(Up+Down) de esas wallets 'smart' por activo. Hipótesis: si nuestra decisión (BUY_YES/BUY_NO) coincide con el consenso smart money, mejor IC que cuando diverge. RESET METODOLOGICO 2026-07-02: la clasificacion 'smart' original via /positions estaba INVERTIDA para wallets de alta frecuencia (el endpoint solo retiene el residuo perdedor sin redimir; verificado: 'wowitsamazing' figuraba como -$478k y es +$10k/mes en el leaderboard oficial). Desde 2026-07-02T06:12Z el consenso se construye solo con wallets verificadas en el leaderboard oficial (pnl_mes>=$1000, 24 wallets). Los valores de smart_money_consensus capturados en features ANTES de esa fecha provienen de la clasificacion rota — descontar ese tramo al evaluar.
  - _Umbral_: 40
  - _Acción_: Si IC en confluencia (decisión coincide con signo de smart_money_consensus) supera en >=0.05 al IC en divergencia, con n≥40 en cada lado → boost ×1.1-1.2 cuando coincide, considerar reducir stake cuando diverge fuerte.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.130 > 0.02 con n=577 PNL=+238.02€
  - _Datos_: n=577 IC=+0.130 PNL=+238.02€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=140 IC=-0.056 PNL=+31.39€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=140 IC=-0.056 PNL=+31.39€

**⏳ H-CUSTOM-WEEKLY-INRANGE-BUYYES** — WEEKLY_PRICE BUY_YES con in_range=1 — ¿estructuralmente sobrevalorado?
  - _Hipótesis_: Analizado 2026-07-01, n=10 (evidencia mínima): BUY_YES cuando in_range=1 fue 0/3 (todo pérdida). Mecanismo propuesto: acertar un rango de precio estrecho al vencimiento es intrínsecamente poco probable, el mercado puede estar sobrevalorando el 'sí'. Ver H-CUSTOM-WEEKLY-PCTDIST-BUYNO para el lado complementario (BUY_NO con pct_dist alto).
  - _Umbral_: 25
  - _Acción_: Si se confirma con n≥25 → filtro causal in_range==1 + BUY_YES → skip en WEEKLY_PRICE
  - _Estado_: 0/25 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-WEEKLY-PCTDIST-BUYNO** — WEEKLY_PRICE BUY_NO con pct_dist alto — cuanto más lejos del rango, más seguro
  - _Hipótesis_: Analizado 2026-07-01, n=10 (evidencia mínima): BUY_NO con pct_dist>=2.09% fue 4/4 victorias (rango 2.09%-23.4%); BUY_NO con pct_dist<8% (pero fuera del corte anterior) tuvo derrotas. Patrón: cuanto más lejos está el spot del rango objetivo al momento de la predicción, más fiable el BUY_NO. Complementa H-CUSTOM-WEEKLY-INRANGE-BUYYES.
  - _Umbral_: 25
  - _Acción_: Si se confirma con n≥25 → boost ×1.2 en WEEKLY_PRICE BUY_NO cuando pct_dist≥2
  - _Estado_: 0/25 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=9108 IC=+0.049 PNL=+1046.72€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=9108 IC=+0.049 PNL=+1046.72€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.161 < -0.1 con n=169 PNL=+13.66€
  - _Datos_: n=169 IC=-0.161 PNL=+13.66€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=1483 IC=+0.044 PNL=+160.37€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1483 IC=+0.044 PNL=+160.37€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=59 IC=-0.107 PNL=+6.34€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=59 IC=-0.107 PNL=+6.34€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.141 > 0.1 con n=293 PNL=+94.75€
  - _Datos_: n=293 IC=+0.141 PNL=+94.75€

**⏳ H-CUSTOM-ETH15-BUYNO-PRECIO-ALTO** — ETH#15min BUY_NO con precio_yes>0.55 pierde (NO longshot contra favorito)
  - _Hipótesis_: Detectado 2026-07-02: ult.60 shadow ETH15 BUY_NO — py_mkt~0.5 wr=0.67 PNL=+29.3 (n=49); py_mkt 0.6-0.8 wr 0.33-0 PNL=-5.75 (n=9). Filtro RETURN NONE (no SKIP) aplicado en shadow_predict.py (PY_MKT_MAX_BUY_NO_ETH15=0.55) el mismo dia -- bloquea la GENERACIÓN de la fila, no solo la decisión. Esta hipotesis trackea la zona filtrada: si las ops que HABRIAN caido aqui siguen apareciendo en otras estrategias o el IC forward de la zona se vuelve positivo, revisar el filtro. CAVEAT: n=9, muestra chica — el filtro se aplico por asimetria de riesgo (afecta a dinero live), no por significancia. ⚠️ 05-Ago (fix): la clave del filtro decía 'py_mkt', que NUNCA existió ni en features de UPDOWN_GBM (T_h/delta_ratio_macro/drift_15min/drift_60min/pct_spot_vs_ref/sigma_h) ni como columna top-level de results.csv -- corregida a 'precio_yes_mercado' (columna real). Aun así, con la clave correcta esta hipótesis NUNCA podrá acumular n mientras el filtro RETURN NONE siga activo -- es el mismo patrón 'frozen by design' que H-CUSTOM-LATE15-PHOTO-FINISH (más abajo): la propia protección impide generar los datos necesarios para volver a evaluarla. Para monitorearla de verdad haría falta un logger separado que capture la señal SIN aplicar el filtro (mismo patrón que gate_bucket_propio con data/markets histórico) -- no construido, pendiente decisión.
  - _Umbral_: 20
  - _Acción_: Si IC forward de la zona >0 con n>=20 → retirar filtro; si confirma negativo → considerar extender a BTC/SOL 15min
  - _Estado_: 4/20 ops en el filtro definido (IC actual=-0.067 PNL=-2.04€)
  - _Datos_: n=4 IC=-0.067 PNL=-2.04€
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: PY_MKT_MAX_BUY_NO_ETH15=0.55 en shadow_predict.py hace RETURN NONE (bloquea generación, no solo decisión) -- nunca podrá acumular n mientras siga activo. Haría falta un logger separado sin el filtro para monitorear de verdad (no construido, 26-Ago)

**〰️ H-PRECIO-YES-BARATO** — BUY_YES con precio de mercado 0.30-0.40 — mercado infravalora YES
  - _Hipótesis_: Detectado 2026-07-03 en benchmark de calibración del mercado (7d, estrategias GBM): en el bucket precio_yes_mercado [0.3-0.4) la frecuencia real de YES fue 0.45 vs 0.35 implícito (+0.10, n=38). Posible sesgo favorito-longshot suave en binarios de 15min (complemento del LONGSHOT ya activo para BUY_NO con py<0.20). Si se confirma, BUY_YES comprado en esa banda lleva viento de cola estructural del propio mercado, independiente del modelo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → kelly_boost ×1.1 para BUY_YES con precio_yes_mercado en [0.30,0.40), simétrico al longshot BUY_NO existente
  - _Estado_: n=14332 IC=-0.144 PNL=+669.38€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=14332 IC=-0.144 PNL=+669.38€

**⏳ H-CUSTOM-LATE15-PHOTO-FINISH** — GBM_LATE_15M photo finish — entrar pegado al strike es moneda al aire cobrada como favorito
  - _Hipótesis_: Detectado 2026-07-05 validando contra nuestros datos la única idea aprovechable de un artículo-anuncio de copy-bot: GBM_LATE_15M con |drift_ventana_pct|<0.02 tenía IC=-0.145 n=181 (win 35%, -9.70€), estable en ambas mitades temporales (-0.163/-0.127), monótono con la distancia (0.02-0.05: IC=+0.061; ≥0.05: IC=+0.14..0.19) y consistente en crudo y normalizado por sigma (|d_gbm|<0.1 IC=-0.081 n=244). BTC (IC=-0.163 n=90) y ETH (-0.130 n=79) concentraban el daño; SOL/XRP apenas entran en esa zona. Mecanismo: sin distancia real al strike el resultado es ~50/50 pero py_entrada ya cobra favorito. Filtro GBM_LATE_DRIFT_VENT_MIN_PCT=0.02 aplicado en shadow_predict el 2026-07-05. Esta hipótesis trackea la zona filtrada: si vuelven a aparecer ops aquí, el filtro se ha roto.
  - _Umbral_: 200
  - _Acción_: Si aparecen ops nuevas en la zona → el filtro está roto, revisar shadow_predict. Si el buffer [0.02,0.05) se vuelve negativo con n≥60 forward → subir el corte a 0.05.
  - _Estado_: 0/200 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: GBM_LATE_DRIFT_VENT_MIN_PCT=0.02 aplicado en shadow_predict.py desde 2026-07-05 -- bloquea la generación de la zona que esta hipótesis mide. Se mantiene como vigilancia pasiva (si vuelven a aparecer ops en la zona, el filtro se rompió), no como 'acumulando' (26-Ago)

**⏳ H-CUSTOM-PHOTO-FINISH-SNIPER** — Photo finish sniper — comprar el lado rezagado a 1-3c en los últimos segundos (estilo egig)
  - _Hipótesis_: 2026-07-05: wallet 'egig' verificada on-chain (leaderboard oficial +$41k all-time; flujo 23h: -$729 compras / +$2,140 redeems). Forense de 497 trades: compra a 1-3c (mediana 2c) el lado rezagado a mediana 2s del cierre, exclusivamente en photo finishes (dist spot-strike mediana 0.027%). Mecanismo: el mercado cobra los finales de foto como decididos cuando son ~moneda al aire — es el espejo del filtro photo finish que aplicamos a GBM_LATE el mismo día. Win rate implícito ~6% con breakeven 2% (~3x por ticket). photo_finish_logger.py (screen pfinish) acumula dataset en data/shadow/photo_finish_YYYY-MM-DD.csv: libro del lado rezagado a T-10s + outcome oficial vía outcomePrices. CAVEATS a medir: profundidad real del ask a 1-3c (egig compite por asks rancios), frecuencia del setup, y que nuestro T-10s no es su T-2s.
  - _Umbral_: 200
  - _Acción_: Si EV>2x sostenido con n≥200 → proponer watcher de ejecución dedicado (decisión de Javi: toca dinero real y requiere loop sub-5s). Si win rate ≈ ask (mercado calibrado también aquí) → archivar.
  - _Estado_: 0/200 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)
  - _Bloqueante_: REFUTADA_28JUL_TRACKING_SEPARADO: ya evaluada a mano 28-Jul con data/shadow/photo_finish_YYYY-MM-DD.csv directo (ver CLAUDE.md punto 13 protocolo arranque / memoria hipotesis_auto.md) -- este filtro genérico busca strategy='PHOTO_FINISH_SNIPER' en results.csv, pero photo_finish_logger.py escribe a un CSV propio con schema distinto y JAMÁS escribe ahí, así que n=0 estructuralmente para siempre por este motor. No repetir la evaluación por aquí; si se reabre, hacerlo contra el CSV propio como el 28-Jul.

**〰️ H-CUSTOM-LATE15-BTC-BUYNO-COINFLIP** — GBM_LATE_15M BTC#BUY_NO es moneda al aire — candidata a quitar del motor estrella
  - _Hipótesis_: Detectado 2026-07-06 desglosando la estrategia que carga el bankroll shadow (GBM_LATE_15M, +364€): por par×dirección, BTC#BUY_NO es la única tupla sin edge — 90/182 (49.5%) PNL=+8.92€, prácticamente coinflip, arrastrando a la baja el IC medio del subtipo. Contraste con las estrellas del mismo motor: SOL#BUY_NO 66.1% (+86.70€), XRP#BUY_YES 67.4% (+80.35€), SOL#BUY_YES 64.4% (+77.08€). ETH#BUY_NO (53.6%) es débil pero positivo; BTC#BUY_YES (57.8%) sí funciona. Hipótesis: el edge de entrada tardía en 15min es fuerte en SOL/XRP, medio en ETH/BTC alcista, y NULO en BTC bajista (BTC es el par más eficiente/arbitrado). Quitar BTC#BUY_NO sube el IC del subtipo sin perder PNL real. NO afecta live (la whitelist live es SOL/XRP BUY_NO + ETH BUY_YES, BTC no está).
  - _Umbral_: n≥150 y IC<+0.03 (n=182 ya disponible al crearla)
  - _Acción_: Si IC<+0.03 con n≥150 → filtro causal skip GBM_LATE_15M BTC#BUY_NO en shadow_predict (deja de diluir el subtipo). Si IC sube >+0.08 → mantener.
  - _Estado_: n=1588 IC=+0.139 PNL=+847.55€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=1588 IC=+0.139 PNL=+847.55€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=2800 IC=+0.016 PNL=+72.88€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2800 IC=+0.016 PNL=+72.88€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.083 > 0.08 con n=1650 PNL=+847.26€
  - _Datos_: n=1650 IC=+0.083 PNL=+847.26€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.243 < -0.1 con n=1439 PNL=-204.09€
  - _Datos_: n=1439 IC=-0.243 PNL=-204.09€

**⏳ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: 100
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: 0/100 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: 40
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: 40
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: 40
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: 31/40 ops en el filtro definido (IC actual=-0.015 PNL=+4.04€)
  - _Datos_: n=31 IC=-0.015 PNL=+4.04€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.099 n=780) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=780 IC=+0.099 PNL=+204.18€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.412 n=397) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=397 IC=+0.412 PNL=+556.95€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=7359 IC=+0.171 PNL=-922.18€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=7359 IC=+0.171 PNL=-922.18€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.219 > 0.1 con n=112 PNL=+72.18€
  - _Datos_: n=112 IC=+0.219 PNL=+72.18€
