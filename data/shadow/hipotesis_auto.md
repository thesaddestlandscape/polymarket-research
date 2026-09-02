# Hipótesis automáticas — 2026-09-02 02:18 UTC
_Generado por shadow_postmortem.py sobre 246736 resoluciones (PNL=+21444.87€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.835` → IC=-0.395 (n=74)

  - _Acción_: SKIP cuando `py_entrada` > 0.835
  - _Potencial_: sin este filtro IC_bueno=+0.131 (n=234)

- **PATRÓN** `py_entrada` > `0.705` → IC=+0.268 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.705 (IC base=+0.162)

- **PATRÓN** `n_ballena_banda` > `19.0` → IC=+0.182 (n=278)

  - _Acción_: Kelly boost +0.91€ cuando `n_ballena_banda` > 19.0 (IC base=+0.162)

- **PATRÓN** `n_total_lado` > `74.0` → IC=+0.255 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 74.0 (IC base=+0.162)

- **PATRÓN** `banda_hit_calibrado` > `0.8038` → IC=+0.257 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8038 (IC base=+0.162)

- **PATRÓN** `banda_z` > `11.871` → IC=+0.271 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.871 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.175 (n=278)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 7.0 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.162 (n=205)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 11.0 (IC base=+0.162)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.184 (n=321)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.01 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `3036.1004` → IC=+0.218 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3036.1004 (IC base=+0.162)

- **PATRÓN** `ballena_activa_n` < `242.0` → IC=+0.257 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 242.0 (IC base=+0.162)

- **PATRÓN** `py_entrada` < `0.835` → IC=+0.131 (n=234)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` < 0.835 (IC base=+0.003)

- **PATRÓN** `ballena_activa_n` < `116.0` → IC=+0.121 (n=27)

  - _Acción_: Kelly boost +0.60€ cuando `ballena_activa_n` < 116.0 (IC base=+0.003)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.133 (n=118)

- **FILTRO** `n_ballena_banda` < `34.0` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `n_ballena_banda` < 34.0
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=116)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.123 (n=51)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=119)

- **PATRÓN** `py_entrada` > `0.705` → IC=+0.278 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.705 (IC base=+0.198)

- **PATRÓN** `n_ballena_banda` > `18.0` → IC=+0.216 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `n_ballena_banda` > 18.0 (IC base=+0.198)

- **PATRÓN** `n_total_lado` > `47.0` → IC=+0.233 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 47.0 (IC base=+0.198)

- **PATRÓN** `banda_hit_calibrado` > `0.8067` → IC=+0.279 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8067 (IC base=+0.198)

- **PATRÓN** `banda_z` > `11.967` → IC=+0.280 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.967 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.211 (n=199)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.209 (n=149)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.211 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `4010.4285` → IC=+0.230 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4010.4285 (IC base=+0.198)

- **PATRÓN** `ballena_activa_n` < `265.0` → IC=+0.272 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 265.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.133 (n=118)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.495 (IC base=-0.023)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.335` → IC=-0.267 (n=28)

  - _Acción_: SKIP cuando `py_entrada` < 0.335
  - _Potencial_: sin este filtro IC_bueno=+0.195 (n=93)

- **FILTRO** `banda_hit_calibrado` < `0.6329` → IC=-0.232 (n=39)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.6329
  - _Potencial_: sin este filtro IC_bueno=+0.238 (n=82)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.146 (n=97)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.353 (n=32)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.134 (n=69)

- **FILTRO** `n_ballena_banda` < `30.0` → IC=-0.128 (n=49)

  - _Acción_: SKIP cuando `n_ballena_banda` < 30.0
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=52)

- **FILTRO** `hora_utc` < `11.0` → IC=-0.125 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=71)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=86)

- **PATRÓN** `py_entrada` > `0.725` → IC=+0.269 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.725 (IC base=+0.085)

- **PATRÓN** `banda_hit_calibrado` > `0.8113` → IC=+0.230 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8113 (IC base=+0.085)

- **PATRÓN** `banda_z` > `8.441` → IC=+0.197 (n=31)

  - _Acción_: Kelly boost +0.98€ cuando `banda_z` > 8.441 (IC base=+0.085)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.146 (n=97)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.02 (IC base=+0.085)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.134 (n=69)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.495 (IC base=-0.024)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `146.18` → IC=-0.294 (n=3391)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 146.18
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=10183)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `150.56` → IC=-0.248 (n=438)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 150.56
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=1316)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `111.25` → IC=-0.409 (n=437)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 111.25
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=1312)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `156.89` → IC=-0.157 (n=927)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 156.89
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=2782)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `136.94` → IC=-0.325 (n=752)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 136.94
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=2258)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `155.6` → IC=-0.372 (n=806)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 155.6
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=1638)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.7` → IC=+0.190 (n=7253)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.7 (IC base=+0.094)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.171 (n=1894)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.01 (IC base=+0.094)

- **PATRÓN** `libro_liquidez` > `2386.174` → IC=+0.172 (n=1817)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2386.174 (IC base=+0.094)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.147 (n=4426)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 18.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.157 (n=5800)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 7.0 (IC base=+0.142)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.258 (n=4491)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.192 (n=3563)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.02 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `1919.9988` → IC=+0.184 (n=3028)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 1919.9988 (IC base=+0.142)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.215 (n=710)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.209 (n=810)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.207)

- **PATRÓN** `py_entrada` > `0.785` → IC=+0.378 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.785 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.209 (n=1016)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `12999.7032` → IC=+0.218 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12999.7032 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.202 (n=756)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.205 (n=833)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` < `0.365` → IC=+0.268 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.365 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.197 (n=1073)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.01 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `12473.6532` → IC=+0.214 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12473.6532 (IC base=+0.196)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.131 (n=532)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 15.0 (IC base=+0.119)

- **PATRÓN** `py_entrada` > `0.595` → IC=+0.161 (n=284)

  - _Acción_: Kelly boost +0.80€ cuando `py_entrada` > 0.595 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.133 (n=268)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `4815.2665` → IC=+0.151 (n=213)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4815.2665 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.196 (n=202)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 7.0 (IC base=+0.132)

- **PATRÓN** `py_entrada` < `0.385` → IC=+0.181 (n=211)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.385 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `4025.563` → IC=+0.153 (n=324)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 4025.563 (IC base=+0.132)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=84)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.137 (n=1314)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 8.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.137 (n=1288)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 15.0 (IC base=+0.131)

- **PATRÓN** `py_entrada` > `0.69` → IC=+0.311 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.278 (n=413)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.270)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.274 (n=622)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.270)

- **PATRÓN** `py_entrada` < `0.195` → IC=+0.413 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.195 (IC base=+0.270)

- **PATRÓN** `libro_liquidez` > `2212.3731` → IC=+0.275 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2212.3731 (IC base=+0.270)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=367)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.158 (n=311)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 15.0 (IC base=+0.139)

- **PATRÓN** `py_entrada` > `0.655` → IC=+0.271 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.655 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.147 (n=426)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.02 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `2022.4564` → IC=+0.163 (n=315)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2022.4564 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.162 (n=143)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.074)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.217 (n=376)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.84` → IC=+0.432 (n=395)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.84 (IC base=+0.185)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.222 (n=271)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.209)

- **PATRÓN** `py_entrada` < `0.215` → IC=+0.349 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.215 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.222 (n=652)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `2120.4177` → IC=+0.231 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2120.4177 (IC base=+0.209)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.223 (n=117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.332 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.192 (n=167)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.02 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `3436.329` → IC=+0.176 (n=66)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 3436.329 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.124 (n=509)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 7.0 (IC base=+0.109)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.216 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.109)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.146 (n=286)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.02 (IC base=+0.109)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.8` → IC=-0.344 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=124)

- **FILTRO** `libro_liquidez` < `10760.7327` → IC=-0.259 (n=139)

  - _Acción_: SKIP cuando `libro_liquidez` < 10760.7327
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=47)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.195 (n=5732)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.193 (n=4845)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.202 (n=2747)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.189)

- **PATRÓN** `libro_liquidez` > `3916.0714` → IC=+0.325 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3916.0714 (IC base=+0.189)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.165 (n=1007)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 11.0 (IC base=+0.164)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.174 (n=1405)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 17.0 (IC base=+0.164)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.179 (n=1491)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.74 (IC base=+0.164)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.244 (n=84)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.236 (n=85)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.420 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.330)

- **PATRÓN** `py_entrada` > `0.835` → IC=+0.380 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.835 (IC base=+0.330)

- **PATRÓN** `libro_liquidez` > `2916.5858` → IC=+0.343 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2916.5858 (IC base=+0.330)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.174 (n=1390)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 6.0 (IC base=+0.169)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.174 (n=1226)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 15.0 (IC base=+0.169)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.172 (n=1490)

  - _Acción_: Kelly boost +0.86€ cuando `py_entrada` < 0.74 (IC base=+0.169)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.181 (n=992)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.72 (IC base=+0.169)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.245 (n=1307)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.235)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.236 (n=1106)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.235)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.312 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.235)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.196 (n=1409)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.186 (n=1197)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 15.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.190 (n=723)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.7 (IC base=+0.183)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.452 (n=266)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.444)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.446 (n=257)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.444)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.479 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.444)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.442 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.444)

- **PATRÓN** `libro_liquidez` > `3363.9486` → IC=+0.457 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3363.9486 (IC base=+0.444)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.444 (n=106)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.437)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.439 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.437)

- **PATRÓN** `libro_liquidez` > `10601.0016` → IC=+0.459 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10601.0016 (IC base=+0.437)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.451 (n=99)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.450 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.436)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.433 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.436)

- **PATRÓN** `libro_liquidez` > `2309.2972` → IC=+0.448 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2309.2972 (IC base=+0.436)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` < `11.0` → IC=+0.457 (n=45)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.444)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.439 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.444)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.444)

- **PATRÓN** `libro_liquidez` > `1927.8949` → IC=+0.438 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1927.8949 (IC base=+0.444)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.197 (n=6717)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.207 (n=15669)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.189)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=3247)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.141)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.171 (n=2246)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.72 (IC base=+0.141)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.230 (n=2733)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.226)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.260 (n=2038)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.226)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.185 (n=1001)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 18.0 (IC base=+0.164)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.182 (n=2668)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.71 (IC base=+0.164)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.236 (n=1404)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.223 (n=1323)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.279 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.223)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=1105)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.243 (n=1326)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.204)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.188 (n=969)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 18.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.190 (n=2037)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 12.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.225 (n=1315)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.183)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.209 (n=2286)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.134)

- **PATRÓN** `restante_min` < `3.98` → IC=+0.146 (n=2115)

  - _Acción_: Kelly boost +0.73€ cuando `restante_min` < 3.98 (IC base=+0.134)

- **PATRÓN** `restante_min` > `4.93` → IC=+0.154 (n=2238)

  - _Acción_: Kelly boost +0.77€ cuando `restante_min` > 4.93 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.150 (n=3084)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 8.0 (IC base=+0.134)

- **PATRÓN** `lag_apertura_s` < `4.25` → IC=+0.158 (n=2106)

  - _Acción_: Kelly boost +0.79€ cuando `lag_apertura_s` < 4.25 (IC base=+0.134)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.212 (n=1158)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.137)

- **PATRÓN** `restante_min` < `3.94` → IC=+0.152 (n=1052)

  - _Acción_: Kelly boost +0.76€ cuando `restante_min` < 3.94 (IC base=+0.137)

- **PATRÓN** `restante_min` > `4.88` → IC=+0.151 (n=1441)

  - _Acción_: Kelly boost +0.75€ cuando `restante_min` > 4.88 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.162 (n=1526)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 8.0 (IC base=+0.137)

- **PATRÓN** `lag_apertura_s` < `7.05` → IC=+0.152 (n=1383)

  - _Acción_: Kelly boost +0.76€ cuando `lag_apertura_s` < 7.05 (IC base=+0.137)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.206 (n=1128)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.130)

- **PATRÓN** `restante_min` < `4.42` → IC=+0.139 (n=1400)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` < 4.42 (IC base=+0.130)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.163 (n=1170)

  - _Acción_: Kelly boost +0.81€ cuando `restante_min` > 4.94 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.132 (n=3327)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.138 (n=1558)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 8.0 (IC base=+0.130)

- **PATRÓN** `lag_apertura_s` < `3.38` → IC=+0.171 (n=1058)

  - _Acción_: Kelly boost +0.85€ cuando `lag_apertura_s` < 3.38 (IC base=+0.130)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.316 (n=486)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.297)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.299 (n=709)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.297)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.367 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.297)

- **PATRÓN** `libro_liquidez` > `1990.9681` → IC=+0.296 (n=606)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1990.9681 (IC base=+0.297)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.288 (n=210)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.278)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.356 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.278)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.278 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `5555.6091` → IC=+0.320 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5555.6091 (IC base=+0.278)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.336 (n=223)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.304)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.312 (n=328)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.304)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.377 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.304)

- **PATRÓN** `libro_liquidez` > `1704.42` → IC=+0.318 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1704.42 (IC base=+0.304)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `12.0` → IC=+0.327 (n=50)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.328)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.346 (n=63)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.328)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.400 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.328)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.344 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.328)

- **PATRÓN** `libro_liquidez` > `662.0852` → IC=+0.359 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 662.0852 (IC base=+0.328)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.436 (n=262)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.420)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.427 (n=258)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.420)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.426 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.420)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.431 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.420)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.421 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.420)

- **PATRÓN** `libro_liquidez` > `2076.021` → IC=+0.431 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2076.021 (IC base=+0.420)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.429 (n=96)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.415)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.425 (n=132)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.415)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.417 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.415)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.426 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.415)

- **PATRÓN** `libro_liquidez` > `5506.0634` → IC=+0.457 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5506.0634 (IC base=+0.415)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.436 (n=124)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.427)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.443 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.427)

- **PATRÓN** `py_entrada` > `0.91` → IC=+0.430 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.91 (IC base=+0.427)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.427 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.427)

- **PATRÓN** `libro_liquidez` > `2031.364` → IC=+0.456 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2031.364 (IC base=+0.427)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.321 (n=154)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.270)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.422 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.270)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.300 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.270)

- **PATRÓN** `libro_liquidez` > `1319.6978` → IC=+0.291 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1319.6978 (IC base=+0.270)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.321 (n=154)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.270)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.422 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.270)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.300 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.270)

- **PATRÓN** `libro_liquidez` > `1319.6978` → IC=+0.291 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1319.6978 (IC base=+0.270)

### GBM_LATE_15M
- **PATRÓN** `ibs_20min` > `0.3476` → IC=+0.123 (n=3249)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` > 0.3476 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` > `0.1712` → IC=+0.223 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1712 (IC base=+0.073)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.439` → IC=+0.146 (n=1242)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 5.439 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` > `1.0855` → IC=+0.235 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0855 (IC base=+0.073)

- **PATRÓN** `volumen_pendiente_norm` > `0.1085` → IC=+0.170 (n=698)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.1085 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` < `2.9333` → IC=+0.166 (n=1892)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.9333 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` > `1.4784` → IC=+0.164 (n=1892)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.4784 (IC base=+0.073)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.194 (n=595)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 34.0 (IC base=+0.073)

- **PATRÓN** `ibs_20min` < `0.4059` → IC=+0.123 (n=3188)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` < 0.4059 (IC base=+0.037)

- **PATRÓN** `volumen_regimen` < `0.6764` → IC=+0.161 (n=479)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.6764 (IC base=+0.037)

- **PATRÓN** `volumen_pendiente_norm` > `0.307` → IC=+0.264 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.307 (IC base=+0.037)

- **PATRÓN** `volumen_spike_ratio` > `2.8959` → IC=+0.217 (n=518)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8959 (IC base=+0.037)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.232 (n=569)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.037)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.007` → IC=+0.173 (n=328)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.007 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.2681` → IC=+0.148 (n=720)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.2681 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.179 (n=347)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 8.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.286 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.44` → IC=+0.295 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.44 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.2285` → IC=+0.212 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2285 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.3307` → IC=+0.124 (n=549)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.3307 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.4538` → IC=+0.142 (n=624)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.4538 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.189 (n=555)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.04 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `61.0` → IC=+0.179 (n=372)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 61.0 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.261 (n=316)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.260)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.286 (n=157)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.260)

- **PATRÓN** `drift_60min` |x|≤ `0.106` → IC=+0.338 (n=208)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.106 (IC base=+0.260)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.264 (n=430)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.260)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.274 (n=498)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.260)

- **PATRÓN** `ibs_20min` < `0.4013` → IC=+0.284 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4013 (IC base=+0.260)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.139` → IC=+0.276 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.139 (IC base=+0.260)

- **PATRÓN** `volumen_pendiente_norm` < `0.0697` → IC=+0.269 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0697 (IC base=+0.260)

- **PATRÓN** `volumen_pendiente_norm` > `0.2986` → IC=+0.354 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2986 (IC base=+0.260)

- **PATRÓN** `volumen_spike_ratio` > `2.8103` → IC=+0.321 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8103 (IC base=+0.260)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.284 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.260)

- **PATRÓN** `libro_liquidez` > `1698.3448` → IC=+0.270 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1698.3448 (IC base=+0.260)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.271 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.260)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.249 (n=189)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.205)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.217 (n=189)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.0937` → IC=+0.237 (n=188)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0937 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=567)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `0.9296` → IC=+0.248 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9296 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `0.1813` → IC=+0.218 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1813 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.325` → IC=+0.222 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.325 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.071` → IC=+0.207 (n=564)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.071 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` < `0.6988` → IC=+0.212 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6988 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` > `1.0855` → IC=+0.225 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0855 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` < `0.1006` → IC=+0.208 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1006 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` < `2.1084` → IC=+0.225 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1084 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `11089.4263` → IC=+0.226 (n=564)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11089.4263 (IC base=+0.205)

- **PATRÓN** `ballena_activa_n` < `386.0` → IC=+0.203 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 386.0 (IC base=+0.205)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.149 (n=631)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0061 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.1746` → IC=+0.156 (n=419)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1746 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.148 (n=566)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 8.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.147 (n=659)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 18.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` < `0.637` → IC=+0.170 (n=628)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.637 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.901` → IC=+0.234 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.901 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.615` → IC=+0.198 (n=210)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 0.615 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.151` → IC=+0.205 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.151 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `2.4168` → IC=+0.165 (n=520)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 2.4168 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `1.4857` → IC=+0.162 (n=465)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.4857 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.146 (n=812)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `12550.5978` → IC=+0.169 (n=418)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 12550.5978 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `234.0` → IC=+0.160 (n=192)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 234.0 (IC base=+0.146)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.007` → IC=+0.187 (n=449)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.007 (IC base=+0.160)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.200 (n=248)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.160)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.263 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.160)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.182` → IC=+0.252 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.182 (IC base=+0.160)

- **PATRÓN** `volumen_pendiente_norm` < `0.1322` → IC=+0.161 (n=565)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` < 0.1322 (IC base=+0.160)

- **PATRÓN** `volumen_spike_ratio` < `3.2867` → IC=+0.153 (n=519)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 3.2867 (IC base=+0.160)

- **PATRÓN** `volumen_spike_ratio` > `1.6876` → IC=+0.172 (n=589)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 1.6876 (IC base=+0.160)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.186 (n=671)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.04 (IC base=+0.160)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.232 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.160)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.252 (n=535)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.01 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.4632` → IC=+0.245 (n=535)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4632 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.242 (n=378)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.267 (n=247)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.3956` → IC=+0.270 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3956 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.545` → IC=+0.296 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.545 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.3816` → IC=+0.333 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3816 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.766` → IC=+0.236 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.766 (IC base=+0.238)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.224 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 51.0 (IC base=+0.238)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.156 (n=152)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=467)

- **FILTRO** `ibs_20min` < `0.2901` → IC=-0.141 (n=204)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2901
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=415)

- **FILTRO** `ibs_20min` > `0.8413` → IC=-0.180 (n=267)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8413
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=805)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.153 (n=70)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=1002)

- **PATRÓN** `dist_vwap_pct` > `0.3391` → IC=+0.308 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3391 (IC base=-0.044)

- **PATRÓN** `volumen_regimen` < `0.6297` → IC=+0.318 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6297 (IC base=-0.044)

- **PATRÓN** `volumen_regimen` > `1.1929` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1929 (IC base=-0.044)

- **PATRÓN** `volumen_pendiente_norm` < `0.1585` → IC=+0.240 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1585 (IC base=-0.044)

- **PATRÓN** `volumen_pendiente_norm` > `0.2199` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2199 (IC base=-0.044)

- **PATRÓN** `volumen_spike_ratio` < `1.435` → IC=+0.357 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.435 (IC base=-0.044)

- **PATRÓN** `volumen_spike_ratio` > `1.9251` → IC=+0.250 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9251 (IC base=-0.044)

- **PATRÓN** `ballena_activa_n` < `126.0` → IC=+0.250 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 126.0 (IC base=-0.044)

- **PATRÓN** `dist_vwap_pct` > `0.2895` → IC=+0.185 (n=52)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.2895 (IC base=-0.045)

- **PATRÓN** `volumen_pendiente_norm` > `0.0659` → IC=+0.188 (n=62)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.0659 (IC base=-0.045)

- **PATRÓN** `volumen_spike_ratio` > `1.573` → IC=+0.123 (n=157)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` > 1.573 (IC base=-0.045)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.134 (n=39)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=127)

- **FILTRO** `ibs_20min` < `0.2759` → IC=-0.179 (n=54)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2759
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=112)

- **FILTRO** `sigma_ewma_delta_pct` > `8.217` → IC=-0.181 (n=186)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.217
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=1450)

- **FILTRO** `volumen_pendiente_norm` < `0.0909` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.0909
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=13)

- **FILTRO** `volumen_spike_ratio` > `1.441` → IC=-0.250 (n=22)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.441
  - _Potencial_: sin este filtro IC_bueno=+0.300 (n=8)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.182 (n=42)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0058 (IC base=+0.036)

- **PATRÓN** `ibs_20min` > `0.2759` → IC=+0.140 (n=112)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` > 0.2759 (IC base=+0.036)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.5274` → IC=-0.170 (n=319)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.5274
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=622)

- **FILTRO** `ibs_20min` < `0.4208` → IC=-0.195 (n=470)

  - _Acción_: SKIP cuando `ibs_20min` < 0.4208
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=471)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.207 (n=206)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=735)

- **FILTRO** `sigma_h` > `0.0245` → IC=-0.141 (n=371)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0245
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=1116)

- **FILTRO** `ibs_20min` > `0.7992` → IC=-0.181 (n=371)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7992
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=1116)

- **FILTRO** `sigma_ewma_delta_pct` > `8.662` → IC=-0.150 (n=181)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.662
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=1306)

- **PATRÓN** `dist_vwap_pct` > `0.5816` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5816 (IC base=-0.108)

- **PATRÓN** `volumen_regimen` > `0.68` → IC=+0.231 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.68 (IC base=-0.108)

- **PATRÓN** `volumen_pendiente_norm` > `0.0744` → IC=+0.267 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0744 (IC base=-0.108)

- **PATRÓN** `volumen_spike_ratio` < `1.5219` → IC=+0.231 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5219 (IC base=-0.108)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.230 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=-0.108)

- **PATRÓN** `volumen_regimen` < `0.6886` → IC=+0.197 (n=74)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 0.6886 (IC base=-0.053)

- **PATRÓN** `volumen_regimen` > `1.295` → IC=+0.259 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.295 (IC base=-0.053)

- **PATRÓN** `volumen_pendiente_norm` > `0.0889` → IC=+0.224 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0889 (IC base=-0.053)

- **PATRÓN** `volumen_spike_ratio` < `2.3188` → IC=+0.167 (n=55)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.3188 (IC base=-0.053)

- **PATRÓN** `volumen_spike_ratio` > `2.7996` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.7996 (IC base=-0.053)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.159 (n=39)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 18.0 (IC base=-0.053)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.143 (n=1840)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.0077 (IC base=+0.059)

- **PATRÓN** `ibs_20min` > `0.2691` → IC=+0.126 (n=4053)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` > 0.2691 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` > `1.2179` → IC=+0.287 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2179 (IC base=+0.059)

- **PATRÓN** `volumen_regimen` > `0.6809` → IC=+0.205 (n=1162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6809 (IC base=+0.059)

- **PATRÓN** `volumen_pendiente_norm` < `0.115` → IC=+0.201 (n=1828)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.115 (IC base=+0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.2536` → IC=+0.216 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2536 (IC base=+0.059)

- **PATRÓN** `volumen_spike_ratio` < `1.4979` → IC=+0.215 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4979 (IC base=+0.059)

- **PATRÓN** `volumen_spike_ratio` > `2.8753` → IC=+0.215 (n=626)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8753 (IC base=+0.059)

- **PATRÓN** `ballena_activa_n` < `91.0` → IC=+0.291 (n=1333)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 91.0 (IC base=+0.059)

- **PATRÓN** `ibs_20min` < `0.5868` → IC=+0.126 (n=3981)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` < 0.5868 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` > `0.8014` → IC=+0.260 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8014 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` < `0.7018` → IC=+0.232 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7018 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` > `1.2273` → IC=+0.247 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2273 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.26` → IC=+0.349 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.26 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` > `2.4256` → IC=+0.279 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4256 (IC base=+0.049)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.279 (n=813)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 51.0 (IC base=+0.049)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2583` → IC=-0.151 (n=333)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2583
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=677)

- **FILTRO** `sigma_ewma_delta_pct` > `2.221` → IC=-0.163 (n=280)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.221
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=611)

- **PATRÓN** `ibs_20min` > `0.7849` → IC=+0.186 (n=253)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.7849 (IC base=+0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.2229` → IC=+0.426 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2229 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` > `2.7831` → IC=+0.281 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7831 (IC base=+0.002)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.398 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.002)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` > `0.7642` → IC=-0.139 (n=477)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7642
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=927)

- **PATRÓN** `dist_vwap_pct` > `0.5454` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5454 (IC base=-0.031)

- **PATRÓN** `volumen_regimen` < `0.5738` → IC=+0.260 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5738 (IC base=-0.031)

- **PATRÓN** `volumen_regimen` > `1.1181` → IC=+0.173 (n=47)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 1.1181 (IC base=-0.031)

- **PATRÓN** `volumen_pendiente_norm` < `0.1438` → IC=+0.182 (n=105)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` < 0.1438 (IC base=-0.031)

- **PATRÓN** `volumen_spike_ratio` < `1.763` → IC=+0.246 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.763 (IC base=-0.031)

- **PATRÓN** `ballena_activa_n` < `246.0` → IC=+0.206 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 246.0 (IC base=-0.031)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.272 (n=296)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.0824` → IC=+0.223 (n=218)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0824 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.244 (n=240)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `0.7083` → IC=+0.250 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7083 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.142` → IC=+0.275 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.142 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` < `0.1413` → IC=+0.225 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1413 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `2.5143` → IC=+0.215 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5143 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `3.294` → IC=+0.224 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.294 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.241 (n=651)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.212)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.336 (n=199)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.312)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.338 (n=295)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.312)

- **PATRÓN** `ibs_20min` < `0.325` → IC=+0.329 (n=437)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.325 (IC base=+0.312)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.516` → IC=+0.317 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.516 (IC base=+0.312)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.494` → IC=+0.315 (n=495)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.494 (IC base=+0.312)

- **PATRÓN** `volumen_pendiente_norm` > `0.3635` → IC=+0.364 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3635 (IC base=+0.312)

- **PATRÓN** `volumen_spike_ratio` < `3.5266` → IC=+0.307 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.5266 (IC base=+0.312)

- **PATRÓN** `volumen_spike_ratio` > `2.4058` → IC=+0.328 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4058 (IC base=+0.312)

- **PATRÓN** `libro_liquidez` > `1836.8021` → IC=+0.345 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1836.8021 (IC base=+0.312)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.304 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 29.0 (IC base=+0.312)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.164 (n=206)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=427)

- **FILTRO** `ibs_20min` < `0.7257` → IC=-0.159 (n=417)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7257
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=216)

- **FILTRO** `volumen_regimen` > `0.9213` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.9213
  - _Potencial_: sin este filtro IC_bueno=+0.076 (n=64)

- **FILTRO** `ibs_20min` > `0.7398` → IC=-0.144 (n=394)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7398
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=767)

- **FILTRO** `volumen_regimen` > `0.8624` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8624
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=49)

- **FILTRO** `volumen_regimen` < `0.6828` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.6828
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=50)

- **FILTRO** `volumen_pendiente_norm` < `0.1167` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.1167
  - _Potencial_: sin este filtro IC_bueno=+0.214 (n=5)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.158 (n=74)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=1087)

- **PATRÓN** `dist_vwap_pct` > `0.4471` → IC=+0.204 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4471 (IC base=-0.083)

- **PATRÓN** `volumen_pendiente_norm` > `0.0567` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.0567 (IC base=-0.083)

- **PATRÓN** `volumen_spike_ratio` < `1.3975` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.3975 (IC base=-0.083)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7797` → IC=-0.146 (n=580)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7797
  - _Potencial_: sin este filtro IC_bueno=+0.259 (n=301)

- **FILTRO** `ibs_20min` > `0.7683` → IC=-0.228 (n=255)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7683
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=767)

- **FILTRO** `sigma_ewma_delta_pct` > `4.656` → IC=-0.149 (n=263)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.656
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=759)

- **FILTRO** `volumen_regimen` > `1.236` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.236
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=64)

- **PATRÓN** `ibs_20min` > `0.9048` → IC=+0.298 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9048 (IC base=-0.007)

- **PATRÓN** `dist_vwap_pct` > `0.5696` → IC=+0.309 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5696 (IC base=-0.007)

- **PATRÓN** `volumen_regimen` < `0.8667` → IC=+0.225 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8667 (IC base=-0.007)

- **PATRÓN** `volumen_regimen` > `1.1463` → IC=+0.280 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1463 (IC base=-0.007)

- **PATRÓN** `volumen_pendiente_norm` < `0.1169` → IC=+0.235 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1169 (IC base=-0.007)

- **PATRÓN** `volumen_pendiente_norm` > `0.2303` → IC=+0.240 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2303 (IC base=-0.007)

- **PATRÓN** `volumen_spike_ratio` < `1.4567` → IC=+0.267 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4567 (IC base=-0.007)

- **PATRÓN** `ballena_activa_n` < `60.0` → IC=+0.278 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 60.0 (IC base=-0.007)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0251` → IC=+0.331 (n=229)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0251 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.246 (n=262)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.244)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.255 (n=328)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.244)

- **PATRÓN** `ibs_20min` > `0.8982` → IC=+0.315 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8982 (IC base=+0.244)

- **PATRÓN** `dist_vwap_pct` > `1.3483` → IC=+0.345 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.3483 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.172` → IC=+0.284 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.172 (IC base=+0.244)

- **PATRÓN** `volumen_regimen` > `0.8427` → IC=+0.283 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8427 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` > `0.2406` → IC=+0.285 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2406 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` < `2.5913` → IC=+0.250 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5913 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` > `2.2494` → IC=+0.248 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2494 (IC base=+0.244)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.254 (n=693)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.244)

- **PATRÓN** `libro_liquidez` > `2472.0173` → IC=+0.250 (n=614)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2472.0173 (IC base=+0.244)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.281 (n=244)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.281)

- **PATRÓN** `sigma_h` > `0.024` → IC=+0.308 (n=243)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.024 (IC base=+0.281)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.288 (n=688)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.281)

- **PATRÓN** `ibs_20min` < `0.3651` → IC=+0.319 (n=728)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3651 (IC base=+0.281)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.262` → IC=+0.320 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.262 (IC base=+0.281)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.914` → IC=+0.281 (n=873)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 8.914 (IC base=+0.281)

- **PATRÓN** `volumen_regimen` < `0.6376` → IC=+0.288 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6376 (IC base=+0.281)

- **PATRÓN** `volumen_regimen` > `1.2686` → IC=+0.308 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2686 (IC base=+0.281)

- **PATRÓN** `volumen_pendiente_norm` > `0.2426` → IC=+0.379 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2426 (IC base=+0.281)

- **PATRÓN** `volumen_spike_ratio` > `2.1844` → IC=+0.301 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1844 (IC base=+0.281)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.204 (n=1135)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0103 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.3304` → IC=+0.169 (n=2994)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.3304 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.171 (n=3411)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 6.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.285 (n=1562)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `1.1148` → IC=+0.244 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1148 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.526` → IC=+0.236 (n=1387)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.526 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` > `0.6258` → IC=+0.169 (n=2321)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 0.6258 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.1056` → IC=+0.185 (n=1250)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.1056 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` < `2.3307` → IC=+0.163 (n=2764)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 2.3307 (IC base=+0.163)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.171 (n=2638)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.01 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `3951.6306` → IC=+0.180 (n=1134)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 3951.6306 (IC base=+0.163)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.182 (n=2033)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 90.0 (IC base=+0.163)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.194 (n=2147)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0063 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.0796` → IC=+0.213 (n=1074)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0796 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.196 (n=1573)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 15.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.183 (n=1475)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 7.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` < `0.4208` → IC=+0.231 (n=3219)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4208 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.929` → IC=+0.222 (n=588)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.929 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` < `1.1714` → IC=+0.170 (n=2452)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.1714 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.2951` → IC=+0.257 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2951 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` < `1.9009` → IC=+0.171 (n=1731)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.9009 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `2.6744` → IC=+0.197 (n=865)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.6744 (IC base=+0.179)

- **PATRÓN** `ballena_activa_n` < `160.0` → IC=+0.177 (n=2178)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 160.0 (IC base=+0.179)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.181 (n=249)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0057 (IC base=+0.170)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.195 (n=257)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.007 (IC base=+0.170)

- **PATRÓN** `drift_60min` |x|≤ `0.2752` → IC=+0.189 (n=563)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.2752 (IC base=+0.170)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.213 (n=249)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.170)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.308 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.54` → IC=+0.320 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.54 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` > `0.2271` → IC=+0.255 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2271 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` < `2.7084` → IC=+0.152 (n=481)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.7084 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` > `1.459` → IC=+0.167 (n=481)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.459 (IC base=+0.170)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.208 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.170)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.261 (n=358)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0044 (IC base=+0.245)

- **PATRÓN** `drift_60min` |x|≤ `0.1661` → IC=+0.305 (n=239)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1661 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.264 (n=379)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` < `0.2708` → IC=+0.267 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2708 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.692` → IC=+0.258 (n=395)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.692 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` < `0.0905` → IC=+0.238 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0905 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.3016` → IC=+0.287 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3016 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` < `1.9129` → IC=+0.254 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9129 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `2.791` → IC=+0.258 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.791 (IC base=+0.245)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.289 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.245)

- **PATRÓN** `libro_liquidez` > `1698.2448` → IC=+0.275 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1698.2448 (IC base=+0.245)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.270 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 36.0 (IC base=+0.245)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.228 (n=167)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.170)

- **PATRÓN** `drift_60min` |x|≤ `0.4039` → IC=+0.178 (n=495)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.4039 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.202 (n=454)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.170)

- **PATRÓN** `ibs_20min` > `0.4579` → IC=+0.220 (n=495)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4579 (IC base=+0.170)

- **PATRÓN** `dist_vwap_pct` > `0.1867` → IC=+0.230 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1867 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.986` → IC=+0.245 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.986 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.52` → IC=+0.171 (n=472)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` < 7.52 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` < `0.6383` → IC=+0.183 (n=165)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6383 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` > `1.0648` → IC=+0.187 (n=225)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` > 1.0648 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` > `0.1658` → IC=+0.191 (n=147)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.1658 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` < `2.1275` → IC=+0.189 (n=410)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 2.1275 (IC base=+0.170)

- **PATRÓN** `libro_liquidez` > `11354.3179` → IC=+0.191 (n=442)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 11354.3179 (IC base=+0.170)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.175 (n=601)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.006 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.2979` → IC=+0.172 (n=601)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.2979 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.174 (n=559)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 7.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.449` → IC=+0.192 (n=601)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.449 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.5985` → IC=+0.157 (n=97)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.5985 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.387` → IC=+0.233 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.387 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `0.6877` → IC=+0.219 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6877 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.1603` → IC=+0.226 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1603 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.4667` → IC=+0.165 (n=493)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 2.4667 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `1.3943` → IC=+0.154 (n=493)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.3943 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `15515.352` → IC=+0.170 (n=201)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 15515.352 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `233.0` → IC=+0.159 (n=136)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 233.0 (IC base=+0.153)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.008` → IC=+0.206 (n=236)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.008 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.2685` → IC=+0.189 (n=457)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.2685 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.194 (n=178)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.169)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.189 (n=175)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 5.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.307 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.331` → IC=+0.282 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.331 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` < `0.226` → IC=+0.159 (n=464)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` < 0.226 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.1328` → IC=+0.162 (n=190)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.1328 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `1.7691` → IC=+0.171 (n=153)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.7691 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `3.2944` → IC=+0.167 (n=208)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 3.2944 (IC base=+0.169)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.194 (n=507)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.04 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `1914.6584` → IC=+0.169 (n=173)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 1914.6584 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.217 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.169)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.248 (n=411)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.230)

- **PATRÓN** `drift_60min` |x|≤ `0.2226` → IC=+0.265 (n=274)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2226 (IC base=+0.230)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.254 (n=286)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.230)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.232 (n=371)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.230)

- **PATRÓN** `ibs_20min` < `0.3724` → IC=+0.272 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3724 (IC base=+0.230)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.563` → IC=+0.321 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.563 (IC base=+0.230)

- **PATRÓN** `volumen_pendiente_norm` > `0.3655` → IC=+0.297 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3655 (IC base=+0.230)

- **PATRÓN** `volumen_spike_ratio` < `1.9412` → IC=+0.220 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9412 (IC base=+0.230)

- **PATRÓN** `volumen_spike_ratio` > `3.1717` → IC=+0.223 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.1717 (IC base=+0.230)

- **PATRÓN** `libro_liquidez` > `1854.8646` → IC=+0.234 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1854.8646 (IC base=+0.230)

- **PATRÓN** `ballena_activa_n` < `60.0` → IC=+0.195 (n=296)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 60.0 (IC base=+0.230)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.206 (n=437)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0074 (IC base=+0.170)

- **PATRÓN** `drift_60min` |x|≤ `0.3518` → IC=+0.188 (n=437)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.3518 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.186 (n=507)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.170)

- **PATRÓN** `ibs_20min` > `0.4362` → IC=+0.215 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4362 (IC base=+0.170)

- **PATRÓN** `dist_vwap_pct` > `0.1444` → IC=+0.204 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1444 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.181` → IC=+0.289 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.181 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` > `0.6402` → IC=+0.185 (n=497)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 0.6402 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` > `0.1068` → IC=+0.210 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1068 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` < `1.435` → IC=+0.169 (n=161)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.435 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` > `2.6255` → IC=+0.212 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6255 (IC base=+0.170)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.172 (n=559)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.01 (IC base=+0.170)

- **PATRÓN** `libro_liquidez` > `12333.533` → IC=+0.226 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12333.533 (IC base=+0.170)

- **PATRÓN** `ballena_activa_n` < `170.0` → IC=+0.155 (n=381)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 170.0 (IC base=+0.170)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.164 (n=519)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0063 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.3801` → IC=+0.151 (n=589)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.3801 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.167 (n=199)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 18.0 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.149 (n=266)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 7.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.5225` → IC=+0.182 (n=589)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.5225 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.301` → IC=+0.192 (n=128)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 12.301 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `1.1598` → IC=+0.140 (n=589)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.1598 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` > `0.6089` → IC=+0.136 (n=589)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 0.6089 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.0848` → IC=+0.178 (n=209)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.0848 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `1.8875` → IC=+0.147 (n=321)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.8875 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `2.5391` → IC=+0.169 (n=161)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.5391 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `11500.9881` → IC=+0.158 (n=197)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 11500.9881 (IC base=+0.130)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.186 (n=297)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0106 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.136 (n=685)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.116)

- **PATRÓN** `ibs_20min` > `0.5455` → IC=+0.189 (n=654)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.5455 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` > `1.1473` → IC=+0.255 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1473 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.075` → IC=+0.262 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.075 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` > `0.6257` → IC=+0.130 (n=655)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` > 0.6257 (IC base=+0.116)

- **PATRÓN** `volumen_pendiente_norm` < `0.1661` → IC=+0.135 (n=650)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` < 0.1661 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` < `1.4413` → IC=+0.141 (n=207)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4413 (IC base=+0.116)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.122 (n=506)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.01 (IC base=+0.116)

- **PATRÓN** `libro_liquidez` > `3232.413` → IC=+0.223 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3232.413 (IC base=+0.116)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.153 (n=309)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 40.0 (IC base=+0.116)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.134 (n=255)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0059 (IC base=+0.133)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.175 (n=263)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0094 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.1005` → IC=+0.136 (n=193)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.1005 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.191 (n=270)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 15.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.4362` → IC=+0.233 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4362 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` > `1.0242` → IC=+0.151 (n=64)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 1.0242 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.87` → IC=+0.204 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.87 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `1.1545` → IC=+0.149 (n=579)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.1545 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` > `0.8419` → IC=+0.148 (n=387)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 0.8419 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.2196` → IC=+0.211 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2196 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `1.4461` → IC=+0.149 (n=149)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4461 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `2.3199` → IC=+0.182 (n=149)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.3199 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `1421.8863` → IC=+0.157 (n=517)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 1421.8863 (IC base=+0.133)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0169` → IC=+0.215 (n=451)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0169 (IC base=+0.184)

- **PATRÓN** `drift_60min` |x|≤ `0.1678` → IC=+0.211 (n=299)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1678 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.204 (n=241)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.184)

- **PATRÓN** `ibs_20min` > `0.8919` → IC=+0.262 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8919 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` > `0.1506` → IC=+0.220 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1506 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.25` → IC=+0.249 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.25 (IC base=+0.184)

- **PATRÓN** `volumen_regimen` > `0.8296` → IC=+0.215 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8296 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` > `0.2403` → IC=+0.252 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2403 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` < `2.5635` → IC=+0.203 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5635 (IC base=+0.184)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.188 (n=812)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.02 (IC base=+0.184)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.265 (n=228)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0061 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.0922` → IC=+0.248 (n=228)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0922 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.222 (n=315)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.215)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.259 (n=313)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` < `0.3987` → IC=+0.258 (n=684)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3987 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.46` → IC=+0.269 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.46 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` > `0.6915` → IC=+0.236 (n=611)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6915 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.2819` → IC=+0.315 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2819 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `2.7091` → IC=+0.247 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7091 (IC base=+0.215)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.172 (n=236)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0097 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.3287` → IC=+0.134 (n=621)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.67€ cuando `drift_60min` |x|≤ 0.3287 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.196 (n=327)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 16.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` > `0.9475` → IC=+0.230 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9475 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` > `0.2372` → IC=+0.203 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2372 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.306` → IC=+0.193 (n=187)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 8.306 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` < `0.8783` → IC=+0.147 (n=375)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.8783 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` > `1.1694` → IC=+0.153 (n=188)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 1.1694 (IC base=+0.132)

- **PATRÓN** `volumen_pendiente_norm` > `0.1824` → IC=+0.194 (n=191)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1824 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` < `2.3174` → IC=+0.143 (n=573)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.3174 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` > `1.9` → IC=+0.138 (n=434)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.9 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.145 (n=525)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `3156.1404` → IC=+0.143 (n=320)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 3156.1404 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.183 (n=162)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 12.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` < `0.3103` → IC=+0.132 (n=476)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.3103 (IC base=+0.061)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.163 (n=250)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 18.0 (IC base=+0.061)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **FILTRO** `hora_utc` < `10.0` → IC=-0.186 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.145 (n=108)

- **FILTRO** `ibs_20min` > `0.6326` → IC=-0.132 (n=104)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6326
  - _Potencial_: sin este filtro IC_bueno=+0.150 (n=204)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.145 (n=108)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 10.0 (IC base=+0.066)

- **PATRÓN** `ibs_20min` > `0.5377` → IC=+0.139 (n=106)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 0.5377 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` > `0.7947` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7947 (IC base=+0.066)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.972` → IC=+0.185 (n=52)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 3.972 (IC base=+0.066)

- **PATRÓN** `libro_liquidez` > `16864.0568` → IC=+0.184 (n=36)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 16864.0568 (IC base=+0.066)

- **PATRÓN** `ibs_20min` < `0.6326` → IC=+0.150 (n=204)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.6326 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` > `0.1512` → IC=+0.203 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1512 (IC base=+0.055)

- **PATRÓN** `ballena_activa_n` < `274.0` → IC=+0.152 (n=133)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 274.0 (IC base=+0.055)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.271 (n=107)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.264)

- **PATRÓN** `sigma_h` > `0.0039` → IC=+0.283 (n=141)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0039 (IC base=+0.264)

- **PATRÓN** `drift_60min` |x|≤ `0.0994` → IC=+0.282 (n=53)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0994 (IC base=+0.264)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.289 (n=150)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.264)

- **PATRÓN** `ibs_20min` > `0.7907` → IC=+0.322 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7907 (IC base=+0.264)

- **PATRÓN** `dist_vwap_pct` > `0.1675` → IC=+0.333 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1675 (IC base=+0.264)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.561` → IC=+0.335 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.561 (IC base=+0.264)

- **PATRÓN** `volumen_regimen` < `0.701` → IC=+0.292 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.701 (IC base=+0.264)

- **PATRÓN** `volumen_regimen` > `1.2111` → IC=+0.300 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2111 (IC base=+0.264)

- **PATRÓN** `volumen_pendiente_norm` > `0.1008` → IC=+0.386 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1008 (IC base=+0.264)

- **PATRÓN** `volumen_spike_ratio` < `1.374` → IC=+0.333 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.374 (IC base=+0.264)

- **PATRÓN** `volumen_spike_ratio` > `2.5693` → IC=+0.311 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5693 (IC base=+0.264)

- **PATRÓN** `drift_60min` |x|≤ `0.0956` → IC=+0.192 (n=37)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.0956 (IC base=+0.027)

- **PATRÓN** `libro_liquidez` > `9336.2451` → IC=+0.231 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9336.2451 (IC base=+0.027)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` > `0.4524` → IC=-0.240 (n=48)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4524
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=97)

- **FILTRO** `dist_vwap_pct` > `0.2318` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2318
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=124)

- **FILTRO** `volumen_pendiente_norm` > `0.2236` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.2236
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=107)

- **FILTRO** `volumen_spike_ratio` > `2.8535` → IC=-0.219 (n=30)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.8535
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=93)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.196 (n=77)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 15.0 (IC base=+0.053)

- **PATRÓN** `ibs_20min` > `0.5714` → IC=+0.126 (n=172)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` > 0.5714 (IC base=+0.053)

- **PATRÓN** `dist_vwap_pct` > `0.7416` → IC=+0.241 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7416 (IC base=+0.053)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.979` → IC=+0.151 (n=61)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 6.979 (IC base=+0.053)

- **PATRÓN** `volumen_pendiente_norm` > `0.1727` → IC=+0.151 (n=41)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.1727 (IC base=+0.053)

- **PATRÓN** `volumen_spike_ratio` > `2.2151` → IC=+0.144 (n=71)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.2151 (IC base=+0.053)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 18.0 (IC base=-0.071)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0159` → IC=+0.205 (n=59)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0159 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.2982` → IC=+0.172 (n=114)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.2982 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.208 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` > `0.56` → IC=+0.164 (n=117)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.56 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.1962` → IC=+0.180 (n=48)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.1962 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.275` → IC=+0.181 (n=111)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 3.275 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` > `0.6571` → IC=+0.178 (n=116)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 0.6571 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` < `0.2201` → IC=+0.167 (n=112)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` < 0.2201 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `1.9259` → IC=+0.199 (n=71)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.9259 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.4996` → IC=+0.157 (n=106)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.4996 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.188 (n=94)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.01 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.250 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.144)

- **PATRÓN** `sigma_h` > `0.0135` → IC=+0.196 (n=90)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0135 (IC base=+0.102)

- **PATRÓN** `dist_vwap_pct` > `1.0608` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0608 (IC base=+0.102)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.481` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 8.481 (IC base=+0.102)

- **PATRÓN** `volumen_regimen` > `0.6173` → IC=+0.128 (n=135)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 0.6173 (IC base=+0.102)

- **PATRÓN** `volumen_pendiente_norm` > `0.2451` → IC=+0.204 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2451 (IC base=+0.102)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.136 (n=116)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 18.0 (IC base=+0.102)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.189 (n=2702)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0066 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.170 (n=4072)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 6.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.300 (n=1406)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.161)

- **PATRÓN** `dist_vwap_pct` > `0.2298` → IC=+0.202 (n=1461)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2298 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.396` → IC=+0.229 (n=2060)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.396 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` < `0.8816` → IC=+0.154 (n=1879)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8816 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` > `1.0855` → IC=+0.151 (n=1278)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 1.0855 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` > `0.1667` → IC=+0.190 (n=1086)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.1667 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` > `1.882` → IC=+0.170 (n=2481)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.882 (IC base=+0.161)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.165 (n=3159)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.161)

- **PATRÓN** `libro_liquidez` > `3897.8392` → IC=+0.187 (n=1348)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 3897.8392 (IC base=+0.161)

- **PATRÓN** `ballena_activa_n` < `62.0` → IC=+0.211 (n=1789)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 62.0 (IC base=+0.161)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.205 (n=2530)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.4745` → IC=+0.195 (n=3788)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.4745 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.206 (n=1700)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` < `0.5593` → IC=+0.241 (n=3788)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5593 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.588` → IC=+0.215 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.588 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.68` → IC=+0.191 (n=3550)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 2.68 (IC base=+0.188)

- **PATRÓN** `volumen_regimen` < `0.6202` → IC=+0.177 (n=908)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6202 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.2382` → IC=+0.252 (n=607)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2382 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `2.328` → IC=+0.199 (n=1398)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.328 (IC base=+0.188)

- **PATRÓN** `ballena_activa_n` < `144.0` → IC=+0.175 (n=2662)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 144.0 (IC base=+0.188)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.191 (n=221)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0052 (IC base=+0.179)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.215 (n=300)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.181 (n=666)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 6.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.193 (n=444)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 11.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.330 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.701` → IC=+0.307 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.701 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.218` → IC=+0.265 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.218 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` < `1.5922` → IC=+0.167 (n=256)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.5922 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `1.8938` → IC=+0.175 (n=386)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 1.8938 (IC base=+0.179)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.179)

- **PATRÓN** `ballena_activa_n` < `64.0` → IC=+0.236 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 64.0 (IC base=+0.179)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.281 (n=326)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.272)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.277 (n=487)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.272)

- **PATRÓN** `drift_60min` |x|≤ `0.1095` → IC=+0.310 (n=214)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1095 (IC base=+0.272)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.280 (n=443)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.272)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.278 (n=489)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.272)

- **PATRÓN** `ibs_20min` < `0.405` → IC=+0.305 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.405 (IC base=+0.272)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.268` → IC=+0.287 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.268 (IC base=+0.272)

- **PATRÓN** `volumen_pendiente_norm` > `0.2944` → IC=+0.323 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2944 (IC base=+0.272)

- **PATRÓN** `volumen_spike_ratio` > `1.5024` → IC=+0.292 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5024 (IC base=+0.272)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.284 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.272)

- **PATRÓN** `libro_liquidez` > `1903.13` → IC=+0.281 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1903.13 (IC base=+0.272)

- **PATRÓN** `ballena_activa_n` < `67.0` → IC=+0.267 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 67.0 (IC base=+0.272)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.192 (n=219)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0028 (IC base=+0.157)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.174 (n=219)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0068 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.0925` → IC=+0.165 (n=219)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.0925 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.182 (n=586)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 8.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` > `0.3266` → IC=+0.208 (n=655)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3266 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` > `0.238` → IC=+0.213 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.238 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.756` → IC=+0.198 (n=160)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 9.756 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.374` → IC=+0.166 (n=570)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 4.374 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` < `1.2667` → IC=+0.165 (n=655)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2667 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` > `1.1006` → IC=+0.166 (n=297)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 1.1006 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` < `0.0734` → IC=+0.176 (n=544)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` < 0.0734 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` > `0.1485` → IC=+0.182 (n=177)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.1485 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `2.1133` → IC=+0.179 (n=534)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 2.1133 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` > `1.7187` → IC=+0.180 (n=404)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.7187 (IC base=+0.157)

- **PATRÓN** `libro_liquidez` > `10760.7327` → IC=+0.186 (n=585)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 10760.7327 (IC base=+0.157)

- **PATRÓN** `ballena_activa_n` < `502.0` → IC=+0.172 (n=531)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 502.0 (IC base=+0.157)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.173 (n=618)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0061 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.0816` → IC=+0.199 (n=207)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.0816 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.176 (n=640)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 18.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` < `0.5918` → IC=+0.203 (n=618)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5918 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.046` → IC=+0.210 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.046 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `0.6154` → IC=+0.250 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6154 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.1414` → IC=+0.241 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1414 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `2.4315` → IC=+0.189 (n=522)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 2.4315 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `2.084` → IC=+0.182 (n=237)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.084 (IC base=+0.168)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.168 (n=800)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `11545.7195` → IC=+0.169 (n=412)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 11545.7195 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `287.0` → IC=+0.181 (n=142)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 287.0 (IC base=+0.168)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.270 (n=189)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0093 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.242 (n=265)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` > `0.6907` → IC=+0.266 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6907 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.364` → IC=+0.332 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.364 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` < `0.2199` → IC=+0.213 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2199 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` < `1.9243` → IC=+0.217 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9243 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `4.1507` → IC=+0.201 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 4.1507 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.235 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.204)

- **PATRÓN** `ballena_activa_n` < `62.0` → IC=+0.262 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 62.0 (IC base=+0.204)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.280 (n=193)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.240)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.247 (n=263)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.240)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.273 (n=214)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.4138` → IC=+0.302 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4138 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.578` → IC=+0.283 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.578 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.3642` → IC=+0.279 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3642 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `1.7026` → IC=+0.273 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7026 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `1.9295` → IC=+0.219 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9295 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.239 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `62.0` → IC=+0.210 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 62.0 (IC base=+0.240)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.007` → IC=+0.156 (n=580)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.007 (IC base=+0.143)

- **PATRÓN** `sigma_h` > `0.004` → IC=+0.143 (n=589)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` > 0.004 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.453` → IC=+0.147 (n=659)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.453 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.161 (n=597)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 8.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` > `0.7485` → IC=+0.237 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7485 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.3857` → IC=+0.183 (n=263)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.3857 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.692` → IC=+0.203 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.692 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `0.9051` → IC=+0.170 (n=440)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.9051 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` > `1.2091` → IC=+0.144 (n=220)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.2091 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.1035` → IC=+0.230 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1035 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `2.1819` → IC=+0.204 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1819 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `9596.597` → IC=+0.237 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9596.597 (IC base=+0.143)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.154 (n=492)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0072 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.4492` → IC=+0.152 (n=559)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.4492 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.137 (n=213)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 17.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.176 (n=248)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 7.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` < `0.6727` → IC=+0.174 (n=559)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.6727 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` > `0.2207` → IC=+0.138 (n=238)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.2207 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.341` → IC=+0.219 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.341 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.299` → IC=+0.136 (n=526)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 4.299 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `1.011` → IC=+0.134 (n=492)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.011 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` > `1.1367` → IC=+0.160 (n=186)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 1.1367 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.2803` → IC=+0.276 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2803 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` < `1.8319` → IC=+0.142 (n=333)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.8319 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `2.5341` → IC=+0.169 (n=167)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.5341 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `11732.317` → IC=+0.213 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11732.317 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `186.0` → IC=+0.146 (n=422)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 186.0 (IC base=+0.131)

### GBM_LATE_15M_TARDIO#SOL#15min
- **FILTRO** `ibs_20min` < `0.4808` → IC=-0.183 (n=235)

  - _Acción_: SKIP cuando `ibs_20min` < 0.4808
  - _Potencial_: sin este filtro IC_bueno=+0.184 (n=707)

- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.141 (n=471)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` > 0.0084 (IC base=+0.092)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.136 (n=479)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 12.0 (IC base=+0.092)

- **PATRÓN** `ibs_20min` > `0.4808` → IC=+0.184 (n=707)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.4808 (IC base=+0.092)

- **PATRÓN** `dist_vwap_pct` > `0.8836` → IC=+0.201 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8836 (IC base=+0.092)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.463` → IC=+0.192 (n=352)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 3.463 (IC base=+0.092)

- **PATRÓN** `libro_liquidez` > `2971.9712` → IC=+0.252 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2971.9712 (IC base=+0.092)

- **PATRÓN** `ballena_activa_n` < `63.0` → IC=+0.140 (n=481)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 63.0 (IC base=+0.092)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.178 (n=225)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0058 (IC base=+0.108)

- **PATRÓN** `drift_60min` |x|≤ `0.1269` → IC=+0.161 (n=225)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.1269 (IC base=+0.108)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.135 (n=332)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 15.0 (IC base=+0.108)

- **PATRÓN** `ibs_20min` < `0.5938` → IC=+0.194 (n=674)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.5938 (IC base=+0.108)

- **PATRÓN** `dist_vwap_pct` < `0.2907` → IC=+0.131 (n=561)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.2907 (IC base=+0.108)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.187` → IC=+0.130 (n=660)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` < 3.187 (IC base=+0.108)

- **PATRÓN** `volumen_regimen` < `1.0568` → IC=+0.122 (n=593)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.0568 (IC base=+0.108)

- **PATRÓN** `volumen_pendiente_norm` > `0.0719` → IC=+0.147 (n=216)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.0719 (IC base=+0.108)

- **PATRÓN** `volumen_spike_ratio` < `1.5464` → IC=+0.140 (n=231)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.5464 (IC base=+0.108)

- **PATRÓN** `volumen_spike_ratio` > `1.7857` → IC=+0.122 (n=350)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` > 1.7857 (IC base=+0.108)

- **PATRÓN** `libro_liquidez` > `1270.5029` → IC=+0.137 (n=602)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 1270.5029 (IC base=+0.108)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0165` → IC=+0.229 (n=532)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0165 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.201 (n=713)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `0.9394` → IC=+0.291 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9394 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` > `0.9385` → IC=+0.275 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9385 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.12` → IC=+0.251 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.12 (IC base=+0.194)

- **PATRÓN** `volumen_regimen` > `0.6859` → IC=+0.206 (n=713)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6859 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.2878` → IC=+0.265 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2878 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `1.8415` → IC=+0.201 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8415 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.201 (n=957)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.286 (n=292)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0063 (IC base=+0.217)

- **PATRÓN** `sigma_h` > `0.0253` → IC=+0.231 (n=292)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0253 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.6625` → IC=+0.220 (n=875)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6625 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.219 (n=429)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.217)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.224 (n=919)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.4964` → IC=+0.271 (n=875)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4964 (IC base=+0.217)

- **PATRÓN** `dist_vwap_pct` < `0.1798` → IC=+0.226 (n=780)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1798 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.98` → IC=+0.305 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.98 (IC base=+0.217)

- **PATRÓN** `volumen_regimen` > `1.233` → IC=+0.245 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.233 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.2857` → IC=+0.309 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2857 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `1.465` → IC=+0.211 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.465 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.197 (n=598)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 35.0 (IC base=+0.217)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.137 (n=1586)

- **PATRÓN** `sigma_h` < `0.0102` → IC=+0.134 (n=1125)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0102 (IC base=+0.123)

- **PATRÓN** `drift_60min` |x|≤ `0.4429` → IC=+0.137 (n=1124)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.4429 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.163 (n=455)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 18.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.92` → IC=+0.192 (n=426)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.92 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.509` → IC=+0.163 (n=197)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 10.509 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.064` → IC=+0.126 (n=1302)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` < 6.064 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.8876` → IC=+0.127 (n=598)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.8876 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.1747` → IC=+0.160 (n=348)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.1747 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.4634` → IC=+0.152 (n=421)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.4634 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.3931` → IC=+0.152 (n=573)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 2.3931 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.185 (n=401)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0037 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.4875` → IC=+0.151 (n=1201)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4875 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.151 (n=474)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.164 (n=459)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 5.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.2009` → IC=+0.159 (n=529)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.2009 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` > `0.1928` → IC=+0.139 (n=471)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.1928 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.225` → IC=+0.147 (n=1202)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 6.225 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `1.0919` → IC=+0.147 (n=1029)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.0919 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` < `0.147` → IC=+0.137 (n=1195)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` < 0.147 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.0688` → IC=+0.149 (n=577)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.0688 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `2.489` → IC=+0.146 (n=1189)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.489 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.794` → IC=+0.140 (n=793)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.794 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.137 (n=1586)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `6002.8639` → IC=+0.141 (n=1201)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 6002.8639 (IC base=+0.134)

### GBM_LATE_5M#BTC#5min
- **FILTRO** `sigma_ewma_delta_pct` > `2.471` → IC=-0.250 (n=26)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.471
  - _Potencial_: sin este filtro IC_bueno=+0.141 (n=179)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.129 (n=114)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 15.0 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` > `0.6469` → IC=+0.134 (n=69)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 0.6469 (IC base=+0.089)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.471` → IC=+0.141 (n=179)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 2.471 (IC base=+0.089)

- **PATRÓN** `volumen_regimen` > `0.8077` → IC=+0.129 (n=103)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 0.8077 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` < `1.4115` → IC=+0.167 (n=52)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.4115 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` > `2.2086` → IC=+0.125 (n=70)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` > 2.2086 (IC base=+0.089)

- **PATRÓN** `libro_liquidez` > `12680.3815` → IC=+0.143 (n=138)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 12680.3815 (IC base=+0.089)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.185 (n=268)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0035 (IC base=+0.124)

- **PATRÓN** `drift_60min` |x|≤ `0.0862` → IC=+0.157 (n=202)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.0862 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.162 (n=232)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.159 (n=212)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 5.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` < `0.1706` → IC=+0.172 (n=266)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.1706 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `0.6484` → IC=+0.179 (n=82)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.6484 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.34` → IC=+0.148 (n=603)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 6.34 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `1.1906` → IC=+0.142 (n=604)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.1906 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.0643` → IC=+0.167 (n=283)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.0643 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `1.396` → IC=+0.155 (n=201)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.396 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `1.7842` → IC=+0.133 (n=401)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 1.7842 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `11213.9231` → IC=+0.130 (n=603)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 11213.9231 (IC base=+0.124)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.222 (n=95)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.156)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.189 (n=130)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0104 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.5715` → IC=+0.163 (n=283)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.5715 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.260 (n=102)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` > `0.9545` → IC=+0.292 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9545 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.706` → IC=+0.261 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.706 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.264` → IC=+0.161 (n=252)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 3.264 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` < `0.0931` → IC=+0.165 (n=258)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` < 0.0931 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` > `0.2139` → IC=+0.158 (n=71)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.2139 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `1.6484` → IC=+0.188 (n=94)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.6484 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` > `2.4219` → IC=+0.177 (n=187)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 2.4219 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `1844.889` → IC=+0.169 (n=252)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 1844.889 (IC base=+0.156)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0078` → IC=+0.142 (n=412)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0078 (IC base=+0.129)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.130 (n=468)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` > 0.0047 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.4858` → IC=+0.145 (n=468)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.4858 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.176 (n=171)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 18.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` > `0.7909` → IC=+0.159 (n=212)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.7909 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` > `1.0249` → IC=+0.176 (n=100)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 1.0249 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` < `0.2526` → IC=+0.136 (n=399)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.2526 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.454` → IC=+0.149 (n=75)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 11.454 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.038` → IC=+0.136 (n=471)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 7.038 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.6468` → IC=+0.152 (n=156)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6468 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.1754` → IC=+0.160 (n=142)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.1754 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `1.4406` → IC=+0.167 (n=154)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.4406 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `1.8547` → IC=+0.149 (n=306)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.8547 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `8331.3362` → IC=+0.136 (n=468)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 8331.3362 (IC base=+0.129)

- **PATRÓN** `sigma_h` < `0.0088` → IC=+0.164 (n=364)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0088 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.5101` → IC=+0.189 (n=364)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.5101 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.143 (n=166)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 16.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.156 (n=257)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 12.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` > `0.1184` → IC=+0.159 (n=364)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.1184 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` < `0.4157` → IC=+0.154 (n=374)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.4157 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.294` → IC=+0.161 (n=178)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 3.294 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `1.2227` → IC=+0.164 (n=364)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2227 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` > `0.7329` → IC=+0.151 (n=325)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.7329 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` < `0.1489` → IC=+0.157 (n=371)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.1489 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `2.1843` → IC=+0.175 (n=315)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 2.1843 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `1.5256` → IC=+0.167 (n=319)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.5256 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `7907.9702` → IC=+0.159 (n=364)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 7907.9702 (IC base=+0.143)

### GBM_LATE_5M#SOL#5min
- **FILTRO** `hora_utc` > `5.0` → IC=-0.143 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=67)

- **FILTRO** `dist_vwap_pct` < `0.7269` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.7269
  - _Potencial_: sin este filtro IC_bueno=+0.190 (n=27)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.341` → IC=+0.141 (n=37)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 2.341 (IC base=+0.016)

- **PATRÓN** `volumen_pendiente_norm` > `0.1303` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1303 (IC base=+0.016)

- **PATRÓN** `dist_vwap_pct` > `0.7269` → IC=+0.190 (n=27)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.7269 (IC base=+0.016)

### GBM_LATE_60M
- **FILTRO** `sigma_h` > `0.0108` → IC=-0.293 (n=56)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0108
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=171)

- **FILTRO** `ibs_20min` > `0.113` → IC=-0.174 (n=93)

  - _Acción_: SKIP cuando `ibs_20min` > 0.113
  - _Potencial_: sin este filtro IC_bueno=+0.176 (n=32)

- **FILTRO** `dist_vwap_pct` > `0.1153` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1153
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=68)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.220 (n=191)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.186 (n=103)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 18.0 (IC base=+0.105)

- **PATRÓN** `ibs_20min` > `0.6845` → IC=+0.255 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6845 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `0.3646` → IC=+0.221 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3646 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.814` → IC=+0.264 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.814 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` < `0.6319` → IC=+0.171 (n=86)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.6319 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` > `0.5821` → IC=+0.163 (n=194)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.5821 (IC base=+0.105)

- **PATRÓN** `volumen_pendiente_norm` < `0.0695` → IC=+0.257 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0695 (IC base=+0.105)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.413 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=+0.105)

- **PATRÓN** `volumen_spike_ratio` > `1.3951` → IC=+0.304 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.3951 (IC base=+0.105)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.195 (n=175)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.02 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `2351.5975` → IC=+0.187 (n=113)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2351.5975 (IC base=+0.105)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.7829` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7829
  - _Potencial_: sin este filtro IC_bueno=+0.253 (n=71)

- **FILTRO** `sigma_h` > `0.0047` → IC=-0.167 (n=25)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=49)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.228 (n=90)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.113)

- **PATRÓN** `drift_60min` |x|≤ `0.1075` → IC=+0.289 (n=17)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1075 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.134 (n=39)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 17.0 (IC base=+0.113)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.167 (n=49)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 10.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` > `0.7829` → IC=+0.253 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7829 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` > `0.1487` → IC=+0.210 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1487 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.525` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.525 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `0.6992` → IC=+0.176 (n=32)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6992 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` < `0.0779` → IC=+0.278 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0779 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.1451` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1451 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` < `1.9335` → IC=+0.281 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9335 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` > `1.6708` → IC=+0.260 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6708 (IC base=+0.113)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0066` → IC=-0.340 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0066
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=47)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.222 (n=77)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.156 (n=59)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 15.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.6789` → IC=+0.300 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6789 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.4736` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4736 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.134` → IC=+0.323 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.134 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `0.8208` → IC=+0.207 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8208 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` > `0.5463` → IC=+0.206 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5463 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` < `0.0801` → IC=+0.321 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0801 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `2.35` → IC=+0.389 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.35 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `2539.8402` → IC=+0.250 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2539.8402 (IC base=+0.141)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `hora_utc` < `11.0` → IC=-0.125 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=64)

- **FILTRO** `volumen_regimen` > `0.8778` → IC=-0.318 (n=20)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8778
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=22)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.230 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.031)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.167 (n=37)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.75 (IC base=+0.031)

- **PATRÓN** `dist_vwap_pct` > `0.492` → IC=+0.147 (n=15)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.492 (IC base=+0.031)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.36` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.36 (IC base=+0.031)

- **PATRÓN** `volumen_regimen` > `0.8458` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 0.8458 (IC base=+0.031)

### GBM_LATE_60M_FADE
- **FILTRO** `sigma_h` < `0.0047` → IC=-0.303 (n=74)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=25)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.443 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=66)

- **FILTRO** `dist_vwap_pct` > `0.0718` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.0718
  - _Potencial_: sin este filtro IC_bueno=-0.274 (n=82)

- **FILTRO** `sigma_h` > `0.0053` → IC=-0.389 (n=25)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.272 (n=77)

- **FILTRO** `dist_vwap_pct` > `0.3683` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3683
  - _Potencial_: sin este filtro IC_bueno=-0.288 (n=83)

- **FILTRO** `volumen_regimen` > `0.8307` → IC=-0.327 (n=50)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8307
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=52)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `sigma_h` < `0.0032` → IC=-0.224 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0032
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `hora_utc` > `6.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=22)

- **FILTRO** `sigma_h` < `0.0031` → IC=-0.288 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0031
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=11)

- **FILTRO** `dist_vwap_pct` < `0.0931` → IC=-0.362 (n=27)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0931
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=15)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.6354` → IC=-0.462 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6354
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **FILTRO** `ibs_20min` > `0.8039` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8039
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=19)

- **FILTRO** `dist_vwap_pct` > `0.0802` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.0802
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=18)

- **FILTRO** `volumen_regimen` > `0.6161` → IC=-0.357 (n=26)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.6161
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `sigma_h` < `0.0064` → IC=-0.262 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0064
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11)

- **FILTRO** `ibs_20min` < `0.5833` → IC=-0.309 (n=19)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5833
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=11)

- **FILTRO** `sigma_h` < `0.0065` → IC=-0.382 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0065
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.441 (n=15)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` < `0.6119` → IC=-0.236 (n=51)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6119
  - _Potencial_: sin este filtro IC_bueno=+0.132 (n=153)

- **FILTRO** `ibs_20min` > `0.4458` → IC=-0.188 (n=46)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4458
  - _Potencial_: sin este filtro IC_bueno=+0.132 (n=142)

- **PATRÓN** `ibs_20min` > `0.6119` → IC=+0.132 (n=153)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` > 0.6119 (IC base=+0.039)

- **PATRÓN** `ibs_20min` < `0.4458` → IC=+0.132 (n=142)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.4458 (IC base=+0.053)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.866` → IC=+0.131 (n=63)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 5.866 (IC base=+0.053)

- **PATRÓN** `libro_liquidez` > `3314.3277` → IC=+0.125 (n=94)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 3314.3277 (IC base=+0.053)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `sigma_h` < `0.0017` → IC=-0.206 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0017
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=55)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=54)

- **FILTRO** `ibs_20min` < `0.5739` → IC=-0.380 (n=23)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5739
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=47)

- **PATRÓN** `sigma_h` > `0.0035` → IC=+0.186 (n=33)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0035 (IC base=+0.116)

- **PATRÓN** `drift_60min` |x|≤ `0.2091` → IC=+0.151 (n=61)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.2091 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.259 (n=27)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.116)

- **PATRÓN** `ibs_20min` < `0.2693` → IC=+0.180 (n=73)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.2693 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.255` → IC=+0.153 (n=47)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 3.255 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` < `0.5658` → IC=+0.204 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5658 (IC base=+0.116)

- **PATRÓN** `libro_liquidez` > `3771.3449` → IC=+0.127 (n=73)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 3771.3449 (IC base=+0.116)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.227 (n=31)

- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.321 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0022 (IC base=+0.085)

- **PATRÓN** `drift_60min` |x|≤ `0.1478` → IC=+0.139 (n=34)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.1478 (IC base=+0.085)

- **PATRÓN** `ibs_20min` > `0.6645` → IC=+0.230 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6645 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.413` → IC=+0.139 (n=34)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 7.413 (IC base=+0.085)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.227 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.992` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.992 (IC base=+0.065)

- **PATRÓN** `volumen_regimen` < `0.8554` → IC=+0.140 (n=23)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.8554 (IC base=+0.065)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.1333` → IC=-0.197 (n=31)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1333
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=16)

- **FILTRO** `dist_vwap_pct` > `0.1937` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1937
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=32)

- **FILTRO** `volumen_regimen` < `0.9057` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9057
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=24)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.196 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0046 (IC base=+0.088)

- **PATRÓN** `drift_60min` |x|≤ `0.1849` → IC=+0.136 (n=42)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.1849 (IC base=+0.088)

- **PATRÓN** `ibs_20min` < `0.7895` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.7895 (IC base=+0.088)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.201` → IC=+0.134 (n=39)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 4.201 (IC base=+0.088)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.227 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.088)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.167 (n=46)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.03 (IC base=+0.088)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `libro_liquidez` > `2501.4019` → IC=+0.133 (n=137)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2501.4019 (IC base=+0.085)

- **PATRÓN** `libro_liquidez` > `2481.5612` → IC=+0.154 (n=151)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 2481.5612 (IC base=+0.112)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `libro_liquidez` > `2501.4019` → IC=+0.133 (n=137)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2501.4019 (IC base=+0.085)

- **PATRÓN** `libro_liquidez` > `2481.5612` → IC=+0.154 (n=151)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 2481.5612 (IC base=+0.112)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9847` → IC=-0.156 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9847
  - _Potencial_: sin este filtro IC_bueno=-0.128 (n=92)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.210 (n=60)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=62)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.102 (n=106)

- **FILTRO** `libro_liquidez` < `2136.6655` → IC=-0.344 (n=30)

  - _Acción_: SKIP cuando `libro_liquidez` < 2136.6655
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=92)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=157)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=18)

- **FILTRO** `libro_liquidez` < `11811.9773` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `libro_liquidez` < 11811.9773
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

- **FILTRO** `hora_utc` > `6.0` → IC=-0.179 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=19)

### LIQUIDACIONES_15M#XRP#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=927)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=90)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.133 (n=47)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=90)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `16.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=42)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_usd_total` < `35093.65` → IC=-0.192 (n=37)

  - _Acción_: SKIP cuando `liq_usd_total` < 35093.65
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=76)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=18)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.167 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=17)

- **FILTRO** `libro_liquidez` < `13988.6712` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 13988.6712
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=17)

- **PATRÓN** `liq_usd_total` > `55522.43` → IC=+0.127 (n=57)

  - _Acción_: Kelly boost +0.64€ cuando `liq_usd_total` > 55522.43 (IC base=+0.004)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.151 (n=41)

  - _Acción_: Kelly boost +0.76€ cuando `py_entrada` < 0.495 (IC base=+0.004)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9215` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9215
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=63)

- **FILTRO** `hora_utc` > `14.0` → IC=-0.167 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=67)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=293)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9593` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9593
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=15)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.318 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=365)

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
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=52)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.7335` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.7335
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=51)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=52)

### LIQUIDACIONES_60M
- **FILTRO** `py_entrada` > `0.56` → IC=-0.167 (n=28)

  - _Acción_: SKIP cuando `py_entrada` > 0.56
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=121)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.141 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=82)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.136 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=27)

- **FILTRO** `py_entrada` > `0.54` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` > 0.54
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=24)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=32)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=89)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=35)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=37)

### MOMENTUM_IBS_15M#BTC#15min
- **FILTRO** `py_entrada` > `0.505` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=308)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=654)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=711)

### MOMENTUM_IBS_15M#SOL#15min
- **FILTRO** `drift_20min_pct` |x|> `0.1713` → IC=-0.130 (n=117)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1713
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=234)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.46` → IC=-0.184 (n=1272)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=3852)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.188 (n=1337)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=4030)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.261 (n=178)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=573)

- **FILTRO** `ibs_20min` < `0.7215` → IC=-0.246 (n=187)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7215
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=564)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.56` → IC=-0.198 (n=210)

  - _Acción_: SKIP cuando `py_entrada` > 0.56
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=672)

- **FILTRO** `ballena_activa_n` > `63.0` → IC=-0.149 (n=220)

  - _Acción_: SKIP cuando `ballena_activa_n` > 63.0
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=662)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=847)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.204 (n=255)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=551)

- **FILTRO** `ibs_20min` < `0.719` → IC=-0.190 (n=201)

  - _Acción_: SKIP cuando `ibs_20min` < 0.719
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=605)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.231 (n=221)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=672)

- **FILTRO** `ibs_20min` > `0.7303` → IC=-0.202 (n=223)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7303
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=670)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.174 (n=219)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=672)

- **FILTRO** `py_entrada` > `0.55` → IC=-0.183 (n=219)

  - _Acción_: SKIP cuando `py_entrada` > 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=674)

### MOMENTUM_IBS_15M_BALLENA#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.148 (n=234)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=633)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.191 (n=208)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=679)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.203 (n=200)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=630)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=815)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.223 (n=204)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=675)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `hora_utc` < `15.0` → IC=-0.357 (n=40)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=139)

- **FILTRO** `hora_utc` > `19.0` → IC=-0.206 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=147)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.306 (n=29)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=150)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=410)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=416)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `19.0` → IC=-0.242 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 19.0
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=12)

- **FILTRO** `hora_utc` < `17.0` → IC=-0.259 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=28)

- **FILTRO** `ibs_20min` > `0.8872` → IC=-0.151 (n=41)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8872
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=14)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `hora_utc` < `19.0` → IC=-0.300 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=13)

- **FILTRO** `drift_20min_pct` |x|> `0.1293` → IC=-0.167 (n=28)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1293
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=57)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `hora_utc` < `19.0` → IC=-0.227 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=12)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `11.0` → IC=-0.300 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=56)

- **FILTRO** `ibs_20min` > `0.8837` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8837
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=38)

### MOMENTUM_IBS_5M#BNB#5min
- **FILTRO** `hora_utc` > `17.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=38)

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
- **FILTRO** `hora_utc` < `6.0` → IC=-0.145 (n=2748)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=9893)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.286 (n=3121)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=9520)

- **FILTRO** `ibs_7min` < `0.7111` → IC=-0.248 (n=3158)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7111
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=9483)

- **FILTRO** `ballena_activa_n` > `19.0` → IC=-0.173 (n=4226)

  - _Acción_: SKIP cuando `ballena_activa_n` > 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=8415)

- **FILTRO** `py_entrada` > `0.69` → IC=-0.221 (n=3716)

  - _Acción_: SKIP cuando `py_entrada` > 0.69
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=12247)

- **FILTRO** `ibs_7min` > `0.7273` → IC=-0.168 (n=3982)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7273
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=11981)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.167 (n=542)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=1273)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.328 (n=441)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=1374)

- **FILTRO** `ibs_7min` < `0.2841` → IC=-0.272 (n=598)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2841
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=1217)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.239 (n=439)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=1376)

- **FILTRO** `py_entrada` > `0.53` → IC=-0.140 (n=1819)

  - _Acción_: SKIP cuando `py_entrada` > 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=965)

- **FILTRO** `drift_7min_pct` |x|> `0.1152` → IC=-0.130 (n=945)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1152
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=1839)

- **FILTRO** `ibs_7min` > `0.8367` → IC=-0.181 (n=695)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8367
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=2089)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.147 (n=525)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=1862)

- **FILTRO** `py_entrada` < `0.36` → IC=-0.265 (n=564)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=1823)

- **FILTRO** `ibs_7min` < `0.7717` → IC=-0.191 (n=596)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7717
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=1791)

- **FILTRO** `ballena_activa_n` > `164.0` → IC=-0.194 (n=595)

  - _Acción_: SKIP cuando `ballena_activa_n` > 164.0
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=1792)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.226 (n=600)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=1829)

- **FILTRO** `ballena_activa_n` > `105.0` → IC=-0.180 (n=823)

  - _Acción_: SKIP cuando `ballena_activa_n` > 105.0
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=1606)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.196 (n=461)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.101 (n=1407)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.312 (n=604)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=1264)

- **FILTRO** `ibs_7min` < `0.2097` → IC=-0.285 (n=467)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2097
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=1401)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.243 (n=457)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=1411)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.227 (n=665)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=2161)

- **FILTRO** `ibs_7min` > `0.8113` → IC=-0.171 (n=704)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8113
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=2122)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.146 (n=650)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=1509)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.261 (n=530)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=1629)

- **FILTRO** `ibs_7min` < `0.7509` → IC=-0.199 (n=539)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7509
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=1620)

- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.188 (n=719)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=1440)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.233 (n=714)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=1457)

- **FILTRO** `ibs_7min` > `0.2766` → IC=-0.186 (n=542)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2766
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=1629)

- **FILTRO** `ballena_activa_n` > `34.0` → IC=-0.183 (n=538)

  - _Acción_: SKIP cuando `ballena_activa_n` > 34.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=1633)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.243 (n=567)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=1790)

- **FILTRO** `ibs_7min` < `0.7353` → IC=-0.211 (n=589)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7353
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=1768)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.196 (n=563)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=1794)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.177 (n=741)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=2234)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.127 (n=660)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=1395)

- **FILTRO** `py_entrada` < `0.36` → IC=-0.300 (n=509)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=1546)

- **FILTRO** `ibs_7min` < `0.7315` → IC=-0.248 (n=513)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7315
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=1542)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.229 (n=496)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=1559)

- **FILTRO** `libro_liquidez` < `2681.6088` → IC=-0.138 (n=1356)

  - _Acción_: SKIP cuando `libro_liquidez` < 2681.6088
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=699)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.248 (n=565)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=2213)

- **FILTRO** `ibs_7min` > `0.7907` → IC=-0.157 (n=694)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7907
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2084)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.106` → IC=-0.139 (n=59)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.106
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=116)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=414)

### MOMENTUM_IBS_5M_FADE#DOGE#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=596)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=568)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=436)

### ORDER_FLOW_5M
- **FILTRO** `total_vol_5m` > `215.224` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `total_vol_5m` > 215.224
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **PATRÓN** `delta_ratio` |x|> `0.418` → IC=+0.159 (n=326)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.79€ cuando `delta_ratio` |x|> 0.418 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.145 (n=288)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 11.0 (IC base=+0.126)

- **PATRÓN** `total_vol_5m` < `451.687` → IC=+0.177 (n=156)

  - _Acción_: Kelly boost +0.89€ cuando `total_vol_5m` < 451.687 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.123 (n=218)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `3276.3563` → IC=+0.144 (n=189)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 3276.3563 (IC base=+0.126)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.220 (n=73)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.119)

- **PATRÓN** `total_vol_5m` < `600.958` → IC=+0.128 (n=100)

  - _Acción_: Kelly boost +0.64€ cuando `total_vol_5m` < 600.958 (IC base=+0.119)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3977` → IC=+0.139 (n=81)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio` |x|> 0.3977 (IC base=+0.100)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.127 (n=57)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.02 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `2091.1708` → IC=+0.161 (n=54)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2091.1708 (IC base=+0.100)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4115` → IC=+0.179 (n=54)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.89€ cuando `delta_ratio` |x|> 0.4115 (IC base=+0.109)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.122 (n=72)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` < 12.0 (IC base=+0.109)

- **PATRÓN** `total_vol_5m` < `707.9675` → IC=+0.189 (n=72)

  - _Acción_: Kelly boost +0.95€ cuando `total_vol_5m` < 707.9675 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `7409.4986` → IC=+0.163 (n=81)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 7409.4986 (IC base=+0.109)

- **PATRÓN** `ballena_activa_n` < `153.0` → IC=+0.122 (n=80)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 153.0 (IC base=+0.109)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4012` → IC=+0.212 (n=71)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4012 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.200 (n=78)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.177)

- **PATRÓN** `total_vol_5m` < `6300.756` → IC=+0.192 (n=63)

  - _Acción_: Kelly boost +0.96€ cuando `total_vol_5m` < 6300.756 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `2684.6484` → IC=+0.199 (n=71)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2684.6484 (IC base=+0.177)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.196 (n=54)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 73.0 (IC base=+0.177)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.3998` → IC=+0.136 (n=75)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio` |x|> 0.3998 (IC base=+0.102)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.126 (n=89)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 18.0 (IC base=+0.102)

- **PATRÓN** `total_vol_5m` < `358653.4` → IC=+0.132 (n=74)

  - _Acción_: Kelly boost +0.66€ cuando `total_vol_5m` < 358653.4 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.229 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.102)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.143 (n=68)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 58.0 (IC base=+0.102)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `3.7615` → IC=-0.395 (n=55)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.7615
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=107)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0079` → IC=-0.329 (n=33)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0079
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=35)

- **FILTRO** `T_h` > `87.9756` → IC=-0.429 (n=26)

  - _Acción_: SKIP cuando `T_h` > 87.9756
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=27)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.300 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=-0.129)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `T_h` < `291.9853` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `T_h` < 291.9853
  - _Potencial_: sin este filtro IC_bueno=+0.192 (n=11)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0097` → IC=-0.196 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0097
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=11)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `T_h` > `143.1616` → IC=-0.144 (n=43)

  - _Acción_: SKIP cuando `T_h` > 143.1616
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=132)

- **FILTRO** `pct_vs_K` |x|> `4.5` → IC=-0.205 (n=59)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.5
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=116)

- **FILTRO** `T_h` > `145.7462` → IC=-0.392 (n=35)

  - _Acción_: SKIP cuando `T_h` > 145.7462
  - _Potencial_: sin este filtro IC_bueno=-0.332 (n=111)

- **FILTRO** `pct_vs_K` |x|> `4.3806` → IC=-0.461 (n=49)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.3806
  - _Potencial_: sin este filtro IC_bueno=-0.288 (n=97)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `pct_vs_K` |x|> `1.2216` → IC=-0.182 (n=42)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 1.2216
  - _Potencial_: sin este filtro IC_bueno=+0.283 (n=21)

- **FILTRO** `sigma_h` < `0.0055` → IC=-0.300 (n=33)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0055
  - _Potencial_: sin este filtro IC_bueno=-0.289 (n=17)

- **PATRÓN** `T_h` < `87.9853` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 87.9853 (IC base=-0.023)

- **PATRÓN** `pct_vs_K` |x|≤ `0.8662` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 0.8662 (IC base=-0.023)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `pct_vs_K` |x|> `2.4552` → IC=-0.375 (n=22)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.4552
  - _Potencial_: sin este filtro IC_bueno=-0.130 (n=25)

### RESOLUTION_SNIPER
- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.457 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.382)

- **PATRÓN** `T_h` > `1.2464` → IC=+0.413 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.2464 (IC base=+0.382)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.466 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.382)

### STREAK_FADE_15M
- **FILTRO** `hora_utc` < `6.0` → IC=-0.227 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.145 (n=60)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=114)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.145 (n=60)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 6.0 (IC base=+0.049)

- **PATRÓN** `streak_estiramiento` < `0.4302` → IC=+0.204 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.4302 (IC base=+0.040)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=74)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=77)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=22)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.250 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=120)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=123)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=154)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=235)

- **PATRÓN** `streak_estiramiento` < `0.2913` → IC=+0.207 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.2913 (IC base=+0.045)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=484)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=233)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=324)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=1459)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=828)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=836)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.167 (n=196)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0041 (IC base=+0.123)

- **PATRÓN** `sigma_h` > `0.0064` → IC=+0.156 (n=149)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0064 (IC base=+0.123)

- **PATRÓN** `drift_60min` |x|≤ `0.1649` → IC=+0.127 (n=392)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.63€ cuando `drift_60min` |x|≤ 0.1649 (IC base=+0.123)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0649` → IC=+0.133 (n=445)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio_macro` |x|> 0.0649 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.127 (n=306)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 12.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.127 (n=446)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 17.0 (IC base=+0.123)

- **PATRÓN** `ibs_15` > `0.563` → IC=+0.211 (n=445)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.563 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.4172` → IC=+0.185 (n=106)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.4172 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.353` → IC=+0.229 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.353 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.132 (n=474)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `8808.1502` → IC=+0.175 (n=149)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 8808.1502 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.219 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.123)

### UPDOWN_GBM#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.0829` → IC=-0.131 (n=155)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.0829
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=472)

- **FILTRO** `ibs_15` < `0.2857` → IC=-0.160 (n=151)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=476)

- **FILTRO** `sigma_ewma_delta_pct` > `6.578` → IC=-0.209 (n=53)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.578
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=574)

### UPDOWN_GBM#60min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0803` → IC=-0.239 (n=21)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0803
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=65)

- **FILTRO** `ibs_15` < `0.1725` → IC=-0.250 (n=18)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.1725
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=54)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=32)

### UPDOWN_GBM#BTC#15min
- **FILTRO** `sigma_h` < `0.0047` → IC=-0.167 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=104)

- **FILTRO** `ibs_15` > `0.6218` → IC=-0.146 (n=46)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.6218
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=92)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.172 (n=114)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0043 (IC base=+0.172)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.211 (n=43)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.193` → IC=+0.197 (n=130)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.193 (IC base=+0.172)

- **PATRÓN** `drift_15min` |x|≤ `0.4558` → IC=+0.197 (n=87)

  - _Acción_: Kelly boost +0.98€ cuando `drift_15min` |x|≤ 0.4558 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.202 (n=122)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.179 (n=132)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 17.0 (IC base=+0.172)

- **PATRÓN** `ibs_15` > `0.881` → IC=+0.273 (n=86)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.881 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.3306` → IC=+0.219 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3306 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` < `0.1189` → IC=+0.185 (n=87)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.1189 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.367` → IC=+0.228 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.367 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` < `23.789` → IC=+0.181 (n=139)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` < 23.789 (IC base=+0.172)

### UPDOWN_GBM#BTC#5min
- **FILTRO** `sigma_h` < `0.0035` → IC=-0.180 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0035
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=49)

- **FILTRO** `ibs_15` < `0.1461` → IC=-0.250 (n=18)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.1461
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=54)

- **FILTRO** `libro_liquidez` < `13135.9064` → IC=-0.133 (n=47)

  - _Acción_: SKIP cuando `libro_liquidez` < 13135.9064
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=25)

### UPDOWN_GBM#BTC#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `25.868` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 25.868 (IC base=+0.003)

### UPDOWN_GBM#ETH#15min
- **FILTRO** `ibs_15` < `0.5659` → IC=-0.250 (n=34)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5659
  - _Potencial_: sin este filtro IC_bueno=+0.182 (n=105)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.125 (n=70)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0039 (IC base=+0.074)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1908` → IC=+0.140 (n=48)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio_macro` |x|> 0.1908 (IC base=+0.074)

- **PATRÓN** `ibs_15` > `0.5659` → IC=+0.182 (n=105)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.91€ cuando `ibs_15` > 0.5659 (IC base=+0.074)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.912` → IC=+0.125 (n=46)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` > 8.912 (IC base=+0.074)

### UPDOWN_GBM#ETH#5min
- **FILTRO** `dist_vwap_pct` > `0.1505` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1505
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=83)

- **FILTRO** `ballena_activa_n` > `1.0` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `ballena_activa_n` > 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=35)

- **FILTRO** `drift_15min` |x|> `0.5033` → IC=-0.155 (n=140)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.5033
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=421)

### UPDOWN_GBM#SOL#15min
- **FILTRO** `ibs_15` < `0.4444` → IC=-0.237 (n=17)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.4444
  - _Potencial_: sin este filtro IC_bueno=+0.191 (n=53)

- **PATRÓN** `ibs_15` > `0.4444` → IC=+0.191 (n=53)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.95€ cuando `ibs_15` > 0.4444 (IC base=+0.083)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.477` → IC=+0.326 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.477 (IC base=+0.083)

- **PATRÓN** `libro_liquidez` > `2991.1392` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2991.1392 (IC base=+0.083)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0185` → IC=-0.214 (n=33)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0185
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=66)

- **FILTRO** `drift_60min` |x|> `0.6605` → IC=-0.157 (n=33)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6605
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=66)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.180 (n=23)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=76)

- **FILTRO** `ibs_15` < `0.25` → IC=-0.300 (n=23)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.25
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=76)

### UPDOWN_GBM#SOL#60min
- **FILTRO** `sigma_ewma_delta_pct` < `6.107` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 6.107
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=10)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.214 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0061 (IC base=+0.027)

- **PATRÓN** `ibs_15` > `0.6` → IC=+0.176 (n=35)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.88€ cuando `ibs_15` > 0.6 (IC base=+0.027)

- **PATRÓN** `dist_vwap_pct` < `0.3805` → IC=+0.176 (n=35)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.3805 (IC base=+0.027)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `delta_ratio_macro` |x|> `0.0571` → IC=+0.164 (n=114)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.82€ cuando `delta_ratio_macro` |x|> 0.0571 (IC base=+0.108)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.173 (n=50)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 6.0 (IC base=+0.108)

- **PATRÓN** `ibs_15` > `0.5556` → IC=+0.186 (n=103)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.93€ cuando `ibs_15` > 0.5556 (IC base=+0.108)

- **PATRÓN** `dist_vwap_pct` > `0.3338` → IC=+0.271 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3338 (IC base=+0.108)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.854` → IC=+0.227 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.854 (IC base=+0.108)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.127 (n=116)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.108)

- **PATRÓN** `libro_liquidez` > `2713.7902` → IC=+0.204 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2713.7902 (IC base=+0.108)

- **PATRÓN** `ibs_15` < `0.1304` → IC=+0.167 (n=139)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.83€ cuando `ibs_15` < 0.1304 (IC base=+0.032)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.391 (n=62)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0057 (IC base=+0.326)

- **PATRÓN** `drift_60min` |x|≤ `0.1141` → IC=+0.348 (n=123)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1141 (IC base=+0.326)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0706` → IC=+0.329 (n=185)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0706 (IC base=+0.326)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.354 (n=169)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.326)

- **PATRÓN** `ibs_15` > `0.8299` → IC=+0.374 (n=165)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8299 (IC base=+0.326)

- **PATRÓN** `dist_vwap_pct` > `0.2982` → IC=+0.366 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2982 (IC base=+0.326)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.08` → IC=+0.332 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.08 (IC base=+0.326)

- **PATRÓN** `sigma_ewma_delta_pct` < `18.532` → IC=+0.325 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 18.532 (IC base=+0.326)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.329 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.326)

- **PATRÓN** `libro_liquidez` > `8147.128` → IC=+0.360 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8147.128 (IC base=+0.326)

- **PATRÓN** `ballena_activa_n` < `528.0` → IC=+0.377 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 528.0 (IC base=+0.326)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1934` → IC=+0.325 (n=95)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1934 (IC base=+0.312)

- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.316 (n=36)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0022 (IC base=+0.312)

- **PATRÓN** `sigma_h` > `0.0045` → IC=+0.368 (n=36)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0045 (IC base=+0.312)

- **PATRÓN** `drift_60min` |x|≤ `0.16` → IC=+0.344 (n=94)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.16 (IC base=+0.312)

- **PATRÓN** `drift_15min` |x|≤ `0.376` → IC=+0.342 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.376 (IC base=+0.312)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1021` → IC=+0.316 (n=96)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1021 (IC base=+0.312)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.109` → IC=+0.423 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.109 (IC base=+0.312)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.360 (n=98)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.312)

- **PATRÓN** `ibs_15` > `0.8418` → IC=+0.357 (n=96)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8418 (IC base=+0.312)

- **PATRÓN** `dist_vwap_pct` > `0.2738` → IC=+0.396 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2738 (IC base=+0.312)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.778` → IC=+0.309 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.778 (IC base=+0.312)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.509` → IC=+0.317 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 8.509 (IC base=+0.312)

- **PATRÓN** `libro_liquidez` > `11204.8499` → IC=+0.382 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11204.8499 (IC base=+0.312)

- **PATRÓN** `ballena_activa_n` < `625.0` → IC=+0.417 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 625.0 (IC base=+0.312)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.338 (n=78)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.338)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.368 (n=36)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.338)

- **PATRÓN** `drift_60min` |x|≤ `0.1188` → IC=+0.370 (n=52)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1188 (IC base=+0.338)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1288` → IC=+0.370 (n=52)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1288 (IC base=+0.338)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2029` → IC=+0.361 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2029 (IC base=+0.338)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.340 (n=79)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.338)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.342 (n=36)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.338)

- **PATRÓN** `ibs_15` > `0.743` → IC=+0.412 (n=78)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.743 (IC base=+0.338)

- **PATRÓN** `dist_vwap_pct` < `0.3157` → IC=+0.347 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3157 (IC base=+0.338)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.231` → IC=+0.372 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.231 (IC base=+0.338)

- **PATRÓN** `sigma_ewma_delta_pct` < `19.88` → IC=+0.339 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 19.88 (IC base=+0.338)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.344 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.338)

- **PATRÓN** `libro_liquidez` > `3288.4647` → IC=+0.333 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3288.4647 (IC base=+0.338)

- **PATRÓN** `ballena_activa_n` < `168.0` → IC=+0.342 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 168.0 (IC base=+0.338)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0106` → IC=-0.201 (n=309)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0106
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=930)

- **FILTRO** `ibs_15` < `0.4775` → IC=-0.241 (n=110)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.4775
  - _Potencial_: sin este filtro IC_bueno=+0.175 (n=330)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.134 (n=315)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=924)

- **FILTRO** `sigma_ewma_delta_pct` > `17.972` → IC=-0.155 (n=442)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.972
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=3435)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.299` → IC=+0.153 (n=148)

  - _Acción_: Kelly boost +0.77€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.299 (IC base=-0.068)

- **PATRÓN** `ibs_15` > `0.4775` → IC=+0.175 (n=330)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.87€ cuando `ibs_15` > 0.4775 (IC base=-0.068)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0873` → IC=+0.235 (n=319)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0873 (IC base=-0.067)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0939` → IC=+0.248 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0939 (IC base=-0.067)

- **PATRÓN** `ibs_15` < `0.3542` → IC=+0.283 (n=358)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3542 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` > `0.7834` → IC=+0.226 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7834 (IC base=-0.067)

- **PATRÓN** `ballena_activa_n` < `128.0` → IC=+0.221 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 128.0 (IC base=-0.067)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0074` → IC=-0.243 (n=204)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0074
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=616)

- **FILTRO** `sigma_h` < `0.0037` → IC=-0.224 (n=270)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0037
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=550)

- **FILTRO** `hora_utc` > `17.0` → IC=-0.225 (n=176)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=644)

- **FILTRO** `sigma_ewma_delta_pct` > `19.521` → IC=-0.248 (n=153)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.521
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=667)

- **FILTRO** `libro_liquidez` < `15916.5141` → IC=-0.214 (n=541)

  - _Acción_: SKIP cuando `libro_liquidez` < 15916.5141
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=279)

- **PATRÓN** `ibs_15` > `0.5837` → IC=+0.250 (n=34)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5837 (IC base=+0.023)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.5006` → IC=-0.292 (n=51)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5006
  - _Potencial_: sin este filtro IC_bueno=+0.192 (n=154)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=188)

- **PATRÓN** `drift_60min` |x|≤ `0.0629` → IC=+0.222 (n=52)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0629 (IC base=+0.070)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3537` → IC=+0.220 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3537 (IC base=+0.070)

- **PATRÓN** `ibs_15` > `0.5006` → IC=+0.192 (n=154)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.96€ cuando `ibs_15` > 0.5006 (IC base=+0.070)

- **PATRÓN** `libro_liquidez` > `10550.3134` → IC=+0.208 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10550.3134 (IC base=+0.070)

- **PATRÓN** `sigma_h` < `0.0079` → IC=+0.263 (n=184)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0079 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.4521` → IC=+0.231 (n=184)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4521 (IC base=+0.220)

- **PATRÓN** `drift_15min` |x|≤ `0.6005` → IC=+0.220 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.6005 (IC base=+0.220)

- **PATRÓN** `delta_ratio_macro` |x|> `0.099` → IC=+0.235 (n=164)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.099 (IC base=+0.220)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0928` → IC=+0.235 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0928 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `19.0` → IC=+0.294 (n=61)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 19.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.291 (n=65)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.220)

- **PATRÓN** `ibs_15` < `0.3764` → IC=+0.285 (n=184)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3764 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` > `0.8693` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8693 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.717` → IC=+0.250 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.717 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `3621.1646` → IC=+0.224 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3621.1646 (IC base=+0.220)

- **PATRÓN** `ballena_activa_n` < `184.0` → IC=+0.224 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 184.0 (IC base=+0.220)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1627` → IC=-0.170 (n=104)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1627
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=203)

- **FILTRO** `drift_15min` |x|> `0.8298` → IC=-0.256 (n=76)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8298
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=231)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.143 (n=113)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.102 (n=194)

- **PATRÓN** `ibs_15` > `0.8125` → IC=+0.222 (n=16)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8125 (IC base=-0.118)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0746` → IC=+0.153 (n=70)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio_macro` |x|> 0.0746 (IC base=-0.048)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1752` → IC=+0.186 (n=49)

  - _Acción_: Kelly boost +0.93€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1752 (IC base=-0.048)

- **PATRÓN** `ibs_15` < `0.3667` → IC=+0.228 (n=79)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3667 (IC base=-0.048)

- **PATRÓN** `dist_vwap_pct` < `0.2889` → IC=+0.188 (n=75)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.2889 (IC base=-0.048)

- **PATRÓN** `ballena_activa_n` < `38.0` → IC=+0.141 (n=51)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 38.0 (IC base=-0.048)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0224` → IC=-0.267 (n=114)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0224
  - _Potencial_: sin este filtro IC_bueno=-0.122 (n=223)

- **FILTRO** `drift_15min` |x|> `1.1539` → IC=-0.244 (n=84)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.1539
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=253)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.250 (n=82)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.146 (n=255)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0862` → IC=+0.306 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0862 (IC base=-0.065)

- **PATRÓN** `ibs_15` < `0.1277` → IC=+0.289 (n=55)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1277 (IC base=-0.065)

- **PATRÓN** `ibs_15` > `0.3273` → IC=+0.328 (n=27)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.3273 (IC base=-0.065)

- **PATRÓN** `dist_vwap_pct` > `0.1973` → IC=+0.340 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1973 (IC base=-0.065)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.289 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=-0.065)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.291 (n=304)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.291)

- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.300 (n=138)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0054 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.337 (n=102)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.291)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1333` → IC=+0.309 (n=202)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1333 (IC base=+0.291)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.109` → IC=+0.355 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.109 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.321 (n=277)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.291)

- **PATRÓN** `ibs_15` > `0.8348` → IC=+0.320 (n=303)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8348 (IC base=+0.291)

- **PATRÓN** `dist_vwap_pct` > `0.3186` → IC=+0.352 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3186 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` < `18.902` → IC=+0.294 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 18.902 (IC base=+0.291)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.295 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `13620.7369` → IC=+0.354 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13620.7369 (IC base=+0.291)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.288 (n=116)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0036 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.302 (n=79)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.284)

- **PATRÓN** `drift_60min` |x|≤ `0.16` → IC=+0.305 (n=152)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.16 (IC base=+0.284)

- **PATRÓN** `drift_15min` |x|≤ `0.6436` → IC=+0.286 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.6436 (IC base=+0.284)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1342` → IC=+0.312 (n=115)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1342 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.343 (n=81)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.284)

- **PATRÓN** `ibs_15` > `0.968` → IC=+0.342 (n=80)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.968 (IC base=+0.284)

- **PATRÓN** `dist_vwap_pct` > `0.346` → IC=+0.361 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.346 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.101` → IC=+0.309 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.101 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.121` → IC=+0.289 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.121 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `15415.1121` → IC=+0.367 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15415.1121 (IC base=+0.284)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.304 (n=131)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0074 (IC base=+0.295)

- **PATRÓN** `sigma_h` > `0.0041` → IC=+0.298 (n=117)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0041 (IC base=+0.295)

- **PATRÓN** `drift_60min` |x|≤ `0.0662` → IC=+0.333 (n=58)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0662 (IC base=+0.295)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0501` → IC=+0.304 (n=131)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0501 (IC base=+0.295)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1055` → IC=+0.379 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1055 (IC base=+0.295)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.337 (n=127)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.295)

- **PATRÓN** `ibs_15` > `0.8661` → IC=+0.333 (n=118)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8661 (IC base=+0.295)

- **PATRÓN** `dist_vwap_pct` > `0.0921` → IC=+0.332 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.0921 (IC base=+0.295)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.292` → IC=+0.297 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.292 (IC base=+0.295)

- **PATRÓN** `sigma_ewma_delta_pct` < `19.173` → IC=+0.306 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 19.173 (IC base=+0.295)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.312 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.295)

- **PATRÓN** `libro_liquidez` > `10408.2229` → IC=+0.339 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10408.2229 (IC base=+0.295)

- **PATRÓN** `ballena_activa_n` < `195.0` → IC=+0.320 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 195.0 (IC base=+0.295)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0825` → IC=-0.275 (n=69)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0825
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=135)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.170 (n=107)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=58)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.174` → IC=-0.123 (n=59)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.174
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=60)

- **FILTRO** `sigma_h` > `0.0034` → IC=-0.200 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=20)

- **FILTRO** `drift_15min` |x|> `0.2287` → IC=-0.250 (n=18)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.2287
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

### UPDOWN_OU_5M#DOGE#5min
- **FILTRO** `drift_15min` |x|> `0.3434` → IC=-0.184 (n=17)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3434
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### UPDOWN_OU_5M#ETH#5min
- **FILTRO** `sigma_h` < `0.0033` → IC=-0.324 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1979` → IC=-0.382 (n=15)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1979
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `sigma_h` < `0.0054` → IC=-0.184 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0054
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

### WEEKLY_PRICE
- **PATRÓN** `T_h` < `63.9936` → IC=+0.239 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 63.9936 (IC base=+0.100)

- **PATRÓN** `ratio` < `0.9922` → IC=+0.348 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9922 (IC base=+0.100)

- **PATRÓN** `T_h` > `146.0287` → IC=+0.422 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0287 (IC base=+0.343)

- **PATRÓN** `ratio` > `1.0104` → IC=+0.302 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0104 (IC base=+0.343)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` < `63.9997` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `T_h` < 63.9997 (IC base=+0.085)

- **PATRÓN** `ratio` < `0.973` → IC=+0.395 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.085)

- **PATRÓN** `T_h` < `87.9882` → IC=+0.297 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 87.9882 (IC base=+0.276)

- **PATRÓN** `ratio` > `1.0104` → IC=+0.292 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0104 (IC base=+0.276)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` < `63.9918` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 63.9918 (IC base=+0.143)

- **PATRÓN** `ratio` < `0.9766` → IC=+0.462 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9766 (IC base=+0.143)

- **PATRÓN** `T_h` > `103.3918` → IC=+0.324 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 103.3918 (IC base=+0.313)

- **PATRÓN** `ratio` > `1.0131` → IC=+0.300 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0131 (IC base=+0.313)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `127.3918` → IC=+0.429 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 127.3918 (IC base=+0.411)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-SIGMA-SOL-60MIN**: `UPDOWN_GBM#SOL#60min` gana cuando sigma_h < 0.0061 (IC=+0.214 n=19). Implementar como filtro pre-predicción en shadow_predict.py.
- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.563 sube el IC de +0.123 a +0.211 en UPDOWN_GBM#15min (n=445). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.881 sube el IC de +0.172 a +0.273 en UPDOWN_GBM#BTC#15min (n=86). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5659 sube el IC de +0.074 a +0.182 en UPDOWN_GBM#ETH#15min (n=105). Ya aplicado como kelly_boost=+0.91€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.4444 sube el IC de +0.083 a +0.191 en UPDOWN_GBM#SOL#15min (n=53). Ya aplicado como kelly_boost=+0.95€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5556 sube el IC de +0.108 a +0.186 en UPDOWN_GBM#XRP#15min (n=103). Ya aplicado como kelly_boost=+0.93€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1304 sube el IC de +0.032 a +0.167 en UPDOWN_GBM#XRP#15min (n=139). Ya aplicado como kelly_boost=+0.83€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#60min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.027 a +0.176 en UPDOWN_GBM#SOL#60min (n=35). Ya aplicado como kelly_boost=+0.88€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.4775 sube el IC de -0.068 a +0.175 en UPDOWN_GBM_15M_TARDIO (n=330). Ya aplicado como kelly_boost=+0.87€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3542 sube el IC de -0.067 a +0.283 en UPDOWN_GBM_15M_TARDIO (n=358). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.5837 sube el IC de +0.023 a +0.250 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=34). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5006 sube el IC de +0.070 a +0.192 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=154). Ya aplicado como kelly_boost=+0.96€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3764 sube el IC de +0.220 a +0.285 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=184). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8125 sube el IC de -0.118 a +0.222 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=16). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3667 sube el IC de -0.048 a +0.228 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=79). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.1277 sube el IC de -0.065 a +0.289 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=55). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS > 0.3273 sube el IC de -0.065 a +0.328 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=27). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8348 sube el IC de +0.291 a +0.320 en UPDOWN_GBM_IBS_ALTO (n=303). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.968 sube el IC de +0.284 a +0.342 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=80). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8661 sube el IC de +0.295 a +0.333 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=118). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.8299 sube el IC de +0.326 a +0.374 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=165). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8418 sube el IC de +0.312 a +0.357 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=96). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.743 sube el IC de +0.338 a +0.412 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=78). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min` — IC=+0.361 n=34. Faltan ~6 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL` — IC=+0.361 n=34. Faltan ~6 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `BALLENAS_CONFIRMADAS_15M#XRP#15min` — IC=+0.147 n=32. Faltan ~8 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `BALLENAS_CONFIRMADAS_15M#XRP` — IC=+0.147 n=32. Faltan ~8 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `LATE_WINDOW_5MIN` — IC=+0.210 n=36. Faltan ~4 resoluciones para umbral n≥40. ETA: ~3h.
- **LIVE-CANDIDATA**: `LATE_WINDOW_5MIN#BTC#5min` — IC=+0.210 n=36. Faltan ~4 resoluciones para umbral n≥40. ETA: ~3h.
- **LIVE-CANDIDATA**: `LATE_WINDOW_5MIN#BTC` — IC=+0.210 n=36. Faltan ~4 resoluciones para umbral n≥40. ETA: ~3h.
- **LIVE-CANDIDATA**: `LATE_WINDOW_5MIN#5min` — IC=+0.210 n=36. Faltan ~4 resoluciones para umbral n≥40. ETA: ~3h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 717 | +0.094 | +37.36€ | 1 | 12 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 717 | +0.094 | +37.36€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 7 | +0.058 | +3.13€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 7 | +0.058 | +3.13€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 456 | +0.116 | +25.97€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 456 | +0.116 | +25.97€ | 3 | 11 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 222 | +0.036 | -0.81€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 222 | +0.036 | -0.81€ | 7 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 32 | +0.147 | +9.06€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 32 | +0.147 | +9.06€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 13574 | -0.107 | -2303.77€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 908 | -0.003 | -129.86€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 12666 | -0.114 | -2173.91€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 1754 | -0.073 | -332.34€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 1754 | -0.073 | -332.34€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 908 | -0.003 | -129.86€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 908 | -0.003 | -129.86€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 1749 | -0.157 | -528.38€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 1749 | -0.157 | -528.38€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 3709 | -0.061 | -350.83€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 3709 | -0.061 | -350.83€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 3010 | -0.120 | -309.36€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 3010 | -0.120 | -309.36€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 2444 | -0.187 | -653.00€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 2444 | -0.187 | -653.00€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 3096 | -0.062 | +1347.91€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 876 | -0.006 | +443.33€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 2220 | -0.084 | +904.58€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 3096 | -0.062 | +1347.91€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 876 | -0.006 | +443.33€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 2220 | -0.084 | +904.58€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 72 | -0.122 | -20.61€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 72 | -0.122 | -20.61€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 72 | -0.122 | -20.61€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 72 | -0.122 | -20.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 43551 | +0.113 | -2792.81€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 7455 | +0.186 | -236.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 136 | -0.101 | -56.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 32375 | +0.096 | -2446.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 3585 | +0.118 | -53.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 5433 | +0.076 | -786.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 24 | -0.115 | -1.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#240min | 9 | -0.143 | -7.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 5400 | +0.078 | -776.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 8799 | +0.131 | -200.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 2163 | +0.201 | -75.14€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 5376 | +0.106 | -159.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 1218 | +0.129 | +55.78€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 5442 | +0.081 | -695.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 26 | +0.036 | +0.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#240min | 6 | -0.075 | -4.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 5410 | +0.081 | -691.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 9465 | +0.127 | -129.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 2744 | +0.172 | -5.12€ | 1 | 7 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 5404 | +0.111 | -86.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 1305 | +0.098 | -28.94€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 8990 | +0.127 | -602.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 2479 | +0.195 | -153.79€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 64 | +0.000 | -11.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 5385 | +0.097 | -355.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1062 | +0.132 | -80.60€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 5422 | +0.104 | -378.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 19 | -0.023 | -0.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 5400 | +0.105 | -376.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 7404 | +0.176 | -577.04€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 7404 | +0.176 | -577.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 1872 | +0.164 | -207.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 1872 | +0.164 | -207.47€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 144 | -0.130 | -0.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 144 | -0.130 | -0.72€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 1848 | +0.169 | -197.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 1848 | +0.169 | -197.13€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 1660 | +0.235 | -42.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 1660 | +0.235 | -42.81€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 1801 | +0.183 | -142.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 1801 | +0.183 | -142.66€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 372 | +0.444 | +1.82€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 372 | +0.444 | +1.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 141 | +0.437 | -0.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 141 | +0.437 | -0.20€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 139 | +0.436 | -0.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 139 | +0.436 | -0.38€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 88 | +0.444 | +2.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 88 | +0.444 | +2.17€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 23018 | +0.189 | -2137.96€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 23018 | +0.189 | -2137.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 4111 | +0.141 | -686.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 4111 | +0.141 | -686.20€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 3616 | +0.226 | -126.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 3616 | +0.226 | -126.17€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 3971 | +0.164 | -525.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 3971 | +0.164 | -525.65€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 3670 | +0.223 | -133.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 3670 | +0.223 | -133.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 3788 | +0.203 | -261.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 3788 | +0.203 | -261.98€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 3862 | +0.183 | -404.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 3862 | +0.183 | -404.42€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 8421 | +0.134 | +327.36€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 8421 | +0.134 | +327.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 4190 | +0.137 | +188.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 4190 | +0.137 | +188.09€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 4231 | +0.130 | +139.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 4231 | +0.130 | +139.26€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 903 | +0.297 | -0.64€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 903 | +0.297 | -0.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 390 | +0.278 | -11.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 390 | +0.278 | -11.50€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 422 | +0.304 | +12.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 422 | +0.304 | +12.00€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 91 | +0.328 | -1.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 91 | +0.328 | -1.15€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 386 | +0.420 | -12.27€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 386 | +0.420 | -12.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 175 | +0.415 | -7.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 175 | +0.415 | -7.26€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 177 | +0.427 | -4.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 177 | +0.427 | -4.15€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 34 | +0.361 | -0.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 34 | +0.361 | -0.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 396 | +0.101 | -1.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 127 | +0.081 | -7.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 269 | +0.109 | +6.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 21 | +0.109 | +1.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 21 | +0.109 | +1.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 316 | +0.116 | +10.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 47 | +0.153 | +4.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 269 | +0.109 | +6.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 59 | +0.008 | -12.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 59 | +0.008 | -12.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 11989 | +0.094 | -447.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 1103 | +0.074 | -22.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 10886 | +0.097 | -424.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 7374 | +0.097 | -169.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 1103 | +0.074 | -22.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 6271 | +0.101 | -146.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 1299 | +0.116 | +26.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 1299 | +0.116 | +26.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 3316 | +0.080 | -304.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 3316 | +0.080 | -304.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 542 | +0.270 | -53.26€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 542 | +0.270 | -53.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 542 | +0.270 | -53.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 542 | +0.270 | -53.26€ | 0 | 4 |
| ✅ GBM_LATE_15M | 10704 | +0.051 | +4198.07€ | 0 | 13 |
| ✅ GBM_LATE_15M#15min | 10704 | +0.051 | +4198.07€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 1587 | +0.192 | +1126.69€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 1587 | +0.192 | +1126.69€ | 0 | 23 |
| ✅ GBM_LATE_15M#BTC | 1587 | +0.174 | +1013.28€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 1587 | +0.174 | +1013.28€ | 0 | 27 |
| ✅ GBM_LATE_15M#DOGE | 1609 | +0.195 | +1161.30€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 1609 | +0.195 | +1161.30€ | 0 | 18 |
| ✅ GBM_LATE_15M#ETH | 1691 | -0.045 | +69.99€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 1691 | -0.045 | +69.99€ | 4 | 11 |
| ✅ GBM_LATE_15M#SOL | 1802 | -0.050 | +389.35€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 1802 | -0.050 | +389.35€ | 5 | 2 |
| ✅ GBM_LATE_15M#XRP | 2428 | -0.074 | +437.46€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 2428 | -0.074 | +437.46€ | 6 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 11433 | +0.054 | +4943.47€ | 0 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 11433 | +0.054 | +4943.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 1901 | -0.012 | +794.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 1901 | -0.012 | +794.61€ | 2 | 4 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 2498 | -0.031 | +250.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 2498 | -0.031 | +250.97€ | 1 | 6 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 1452 | +0.252 | +1400.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 1452 | +0.252 | +1400.47€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 1794 | -0.056 | -25.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 1794 | -0.056 | -25.47€ | 8 | 3 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 1903 | -0.025 | +611.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 1903 | -0.025 | +611.84€ | 4 | 8 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 1885 | +0.263 | +1911.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 1885 | +0.263 | +1911.05€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 8827 | +0.171 | +6218.93€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 8827 | +0.171 | +6218.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 1226 | +0.200 | +930.49€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 1226 | +0.200 | +930.49€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 1460 | +0.161 | +999.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 1460 | +0.161 | +999.57€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 1239 | +0.196 | +930.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 1239 | +0.196 | +930.29€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 1447 | +0.149 | +906.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 1447 | +0.149 | +906.58€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 1643 | +0.124 | +1034.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 1643 | +0.124 | +1034.70€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 1812 | +0.200 | +1417.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 1812 | +0.200 | +1417.31€ | 0 | 19 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 1890 | +0.096 | +557.54€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 1890 | +0.096 | +557.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 58 | +0.083 | +12.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 58 | +0.083 | +12.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 449 | +0.059 | +103.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 449 | +0.059 | +103.25€ | 2 | 8 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 305 | +0.148 | +149.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 305 | +0.148 | +149.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 356 | +0.168 | +143.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 356 | +0.168 | +143.15€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 371 | +0.004 | +23.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 371 | +0.004 | +23.21€ | 4 | 7 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 351 | +0.123 | +125.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 351 | +0.123 | +125.65€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO | 10441 | +0.174 | +7394.81€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#15min | 10441 | +0.174 | +7394.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 1528 | +0.219 | +1269.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 1528 | +0.219 | +1269.64€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 1696 | +0.163 | +1161.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 1696 | +0.163 | +1161.88€ | 0 | 28 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 1526 | +0.223 | +1292.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 1526 | +0.223 | +1292.42€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 1622 | +0.138 | +966.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 1622 | +0.138 | +966.76€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 1840 | +0.100 | +946.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 1840 | +0.100 | +946.01€ | 1 | 18 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 2229 | +0.206 | +1758.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 2229 | +0.206 | +1758.10€ | 0 | 21 |
| ✅ GBM_LATE_5M | 3303 | +0.128 | +1536.46€ | 1 | 24 |
| ✅ GBM_LATE_5M#5min | 3303 | +0.128 | +1536.46€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 156 | +0.203 | +114.09€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 156 | +0.203 | +114.09€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1009 | +0.117 | +485.86€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1009 | +0.117 | +485.86€ | 1 | 19 |
| ✅ GBM_LATE_5M#DOGE | 393 | +0.166 | +234.82€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 393 | +0.166 | +234.82€ | 0 | 12 |
| ✅ GBM_LATE_5M#ETH | 1108 | +0.135 | +510.75€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 1108 | +0.135 | +510.75€ | 0 | 27 |
| ✅ GBM_LATE_5M#SOL | 155 | +0.016 | +13.46€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 155 | +0.016 | +13.46€ | 2 | 3 |
| ✅ GBM_LATE_5M#XRP | 482 | +0.114 | +177.49€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 482 | +0.114 | +177.49€ | 0 | 0 |
| ✅ GBM_LATE_60M | 607 | +0.007 | +177.38€ | 3 | 12 |
| ✅ GBM_LATE_60M#60min | 607 | +0.007 | +177.38€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 209 | +0.045 | +48.32€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 209 | +0.045 | +48.32€ | 2 | 12 |
| ✅ GBM_LATE_60M#ETH | 221 | +0.038 | +85.85€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 221 | +0.038 | +85.85€ | 1 | 10 |
| ✅ GBM_LATE_60M#SOL | 177 | -0.075 | +43.21€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 177 | -0.075 | +43.21€ | 2 | 5 |
| 🚫 GBM_LATE_60M_FADE | 201 | -0.298 | -32.12€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 201 | -0.298 | -32.12€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 79 | -0.253 | -7.31€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 79 | -0.253 | -7.31€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 68 | -0.357 | -20.58€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 68 | -0.357 | -20.58€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 54 | -0.268 | -4.23€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 54 | -0.268 | -4.23€ | 4 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 392 | +0.046 | +30.99€ | 2 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 392 | +0.046 | +30.99€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 167 | +0.044 | +25.73€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 167 | +0.044 | +25.73€ | 3 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 95 | +0.077 | +2.03€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 95 | +0.077 | +2.03€ | 1 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 130 | +0.023 | +3.22€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 130 | +0.023 | +3.22€ | 3 | 6 |
| ✅ LATE_WINDOW_5MIN | 36 | +0.210 | +12.46€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 36 | +0.210 | +12.46€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 36 | +0.210 | +12.46€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 36 | +0.210 | +12.46€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 428 | +0.100 | +108.57€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 428 | +0.100 | +108.57€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 428 | +0.100 | +108.57€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 428 | +0.100 | +108.57€ | 0 | 2 |
| ✅ LIQUIDACIONES_15M | 300 | -0.086 | -32.20€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 300 | -0.086 | -32.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 71 | -0.103 | -9.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 71 | -0.103 | -9.18€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 62 | -0.047 | -4.85€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 62 | -0.047 | -4.85€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 88 | +0.000 | -1.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 88 | +0.000 | -1.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 50 | -0.173 | -9.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 50 | -0.173 | -9.93€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 1123 | -0.017 | -25.91€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 1123 | -0.017 | -25.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 65 | -0.022 | -4.19€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 65 | -0.022 | -4.19€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 146 | -0.034 | -4.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 146 | -0.034 | -4.94€ | 4 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 87 | -0.096 | -9.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 87 | -0.096 | -9.54€ | 2 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 339 | +0.007 | +5.83€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 339 | +0.007 | +5.83€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 405 | -0.001 | -5.85€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 405 | -0.001 | -5.85€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 81 | -0.078 | -7.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 81 | -0.078 | -7.22€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M | 542 | -0.005 | +1.61€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 542 | -0.005 | +1.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 166 | -0.036 | -9.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 166 | -0.036 | -9.80€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 166 | +0.012 | +4.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 166 | +0.012 | +4.30€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 210 | +0.005 | +7.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 210 | +0.005 | +7.11€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 6168 | -0.003 | -81.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 6168 | -0.003 | -81.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 533 | -0.003 | +2.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 533 | -0.003 | +2.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 642 | -0.014 | -15.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 642 | -0.014 | -15.01€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 1368 | +0.009 | -13.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 1368 | +0.009 | -13.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 1396 | +0.002 | +5.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 1396 | +0.002 | +5.40€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 984 | -0.014 | -31.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 984 | -0.014 | -31.73€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1245 | -0.006 | -29.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1245 | -0.006 | -29.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 10491 | -0.035 | +409.51€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 10491 | -0.035 | +409.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 1684 | -0.030 | +177.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 1684 | -0.030 | +177.05€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 1861 | -0.033 | -25.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 1861 | -0.033 | -25.78€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 1699 | -0.043 | +152.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 1699 | -0.043 | +152.19€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 1784 | -0.040 | -19.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 1784 | -0.040 | -19.28€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 1754 | -0.035 | +73.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 1754 | -0.035 | +73.79€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 1709 | -0.031 | +51.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 1709 | -0.031 | +51.53€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 610 | -0.082 | -55.22€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 610 | -0.082 | -55.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 104 | -0.038 | -5.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 104 | -0.038 | -5.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 96 | -0.143 | -13.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 96 | -0.143 | -13.40€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 36 | -0.105 | -4.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 36 | -0.105 | -4.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 116 | -0.136 | -15.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 116 | -0.136 | -15.81€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 157 | -0.047 | -8.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 157 | -0.047 | -8.64€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 101 | -0.044 | -7.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 101 | -0.044 | -7.92€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M | 3174 | +0.004 | -4.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3174 | +0.004 | -4.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 126 | -0.039 | -1.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 126 | -0.039 | -1.34€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 185 | +0.008 | -2.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 185 | +0.008 | -2.27€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE | 136 | +0.000 | -1.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 136 | +0.000 | -1.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1163 | +0.008 | +8.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1163 | +0.008 | +8.30€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1386 | +0.006 | -1.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1386 | +0.006 | -1.47€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 178 | -0.006 | -5.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 178 | -0.006 | -5.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 28604 | -0.078 | +566.37€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 28604 | -0.078 | +566.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 4599 | -0.090 | +401.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 4599 | -0.090 | +401.69€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 4816 | -0.076 | -75.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 4816 | -0.076 | -75.76€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 4694 | -0.083 | +162.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 4694 | -0.083 | +162.94€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 4330 | -0.100 | -232.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 4330 | -0.100 | -232.23€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 5332 | -0.056 | +77.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 5332 | -0.056 | +77.40€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 4833 | -0.071 | +232.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 4833 | -0.071 | +232.33€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 6053 | -0.011 | -119.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 6053 | -0.011 | -119.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 992 | -0.018 | -21.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 992 | -0.018 | -21.41€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1219 | -0.000 | -13.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1219 | -0.000 | -13.75€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1002 | -0.020 | -30.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1002 | -0.020 | -30.79€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1320 | -0.002 | -11.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1320 | -0.002 | -11.44€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 794 | -0.015 | -18.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 794 | -0.015 | -18.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 726 | -0.021 | -24.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 726 | -0.021 | -24.40€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 689 | +0.109 | +218.26€ | 1 | 5 |
| ✅ ORDER_FLOW_5M#5min | 553 | +0.122 | +205.66€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 132 | +0.119 | +55.17€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 132 | +0.119 | +55.17€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#DOGE | 108 | +0.100 | +26.44€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 108 | +0.100 | +26.44€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#ETH | 108 | +0.109 | +38.36€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 108 | +0.109 | +38.36€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 94 | +0.177 | +57.07€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 94 | +0.177 | +57.07€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 111 | +0.102 | +28.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 111 | +0.102 | +28.62€ | 0 | 5 |
| ✅ PRICE_TARGET_GBM | 327 | -0.126 | -14.43€ | 1 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC | 142 | -0.201 | -34.46€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC#atexpiry | 112 | -0.263 | -36.23€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 30 | +0.031 | +1.77€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 124 | -0.103 | -0.11€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 87 | -0.129 | -7.25€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 37 | -0.038 | +7.13€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 61 | +0.008 | +20.14€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 44 | -0.022 | +13.06€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 17 | +0.067 | +7.08€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 243 | -0.173 | -30.41€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 84 | +0.012 | +15.98€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 321 | -0.218 | -8.08€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 137 | -0.169 | -7.35€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 113 | -0.152 | -6.07€ | 2 | 2 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 24 | -0.231 | -1.28€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 119 | -0.285 | -21.28€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 97 | -0.308 | -25.66€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 22 | -0.167 | +4.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 65 | -0.187 | +20.54€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 52 | -0.185 | +16.98€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 13 | -0.108 | +3.57€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 262 | -0.220 | -14.76€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#reach | 59 | -0.205 | +6.68€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 91 | +0.360 | +33.83€ | 0 | 3 |
| ✅ RESOLUTION_SNIPER#BTC | 17 | -0.022 | -2.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 17 | -0.022 | -2.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 23 | +0.340 | +5.79€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 23 | +0.340 | +5.79€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 51 | +0.481 | +30.99€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 51 | +0.481 | +30.99€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#sniper | 91 | +0.360 | +33.83€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 217 | +0.043 | +3.60€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 217 | +0.043 | +3.60€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 93 | +0.058 | +3.83€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 93 | +0.058 | +3.83€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 17 | +0.067 | +2.67€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 17 | +0.067 | +2.67€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 22 | +0.083 | -0.06€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 22 | +0.083 | -0.06€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP | 85 | +0.006 | -2.84€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 85 | +0.006 | -2.84€ | 0 | 0 |
| ✅ STREAK_FADE_5M | 1678 | -0.026 | -79.97€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 1678 | -0.026 | -79.97€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 651 | -0.010 | -16.06€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 651 | -0.010 | -16.06€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 553 | -0.026 | -25.13€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 553 | -0.026 | -25.13€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 141 | -0.038 | -12.96€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 141 | -0.038 | -12.96€ | 2 | 0 |
| ✅ STREAK_FADE_5M#XRP | 333 | -0.052 | -25.82€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 333 | -0.052 | -25.82€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 43 | -0.011 | -1.01€ | 0 | 0 |
| ✅ STREAK_FADE_60M#60min | 43 | -0.011 | -1.01€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 26 | -0.107 | -3.37€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 26 | -0.107 | -3.37€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 17 | +0.112 | +2.36€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 17 | +0.112 | +2.36€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 3399 | +0.027 | +69.47€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 3399 | +0.027 | +69.47€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 1118 | +0.023 | +12.32€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 1118 | +0.023 | +12.32€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 665 | +0.046 | +32.65€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 665 | +0.046 | +32.65€ | 1 | 1 |
| ✅ STREAK_MOM_5M#SOL | 1017 | +0.016 | +2.98€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 1017 | +0.016 | +2.98€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 599 | +0.029 | +21.52€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 599 | +0.029 | +21.52€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 3865 | +0.011 | -23.63€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 3865 | +0.011 | -23.63€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 1478 | +0.015 | -5.76€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 1478 | +0.015 | -5.76€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 1527 | +0.017 | -0.63€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 1527 | +0.017 | -0.63€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 860 | -0.005 | -17.24€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 860 | -0.005 | -17.24€ | 2 | 0 |
| ✅ UPDOWN_GBM | 8328 | +0.006 | +195.61€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 2957 | +0.037 | +267.30€ | 0 | 12 |
| ✅ UPDOWN_GBM#240min | 335 | +0.007 | -1.10€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 4487 | -0.010 | -64.99€ | 3 | 0 |
| ✅ UPDOWN_GBM#60min | 502 | -0.004 | -5.09€ | 3 | 0 |
| ✅ UPDOWN_GBM#BNB | 196 | +0.091 | +38.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 179 | +0.119 | +42.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 8 | -0.040 | -1.01€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 9 | -0.102 | -2.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 1711 | +0.017 | +89.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 310 | +0.090 | +67.37€ | 2 | 11 |
| ✅ UPDOWN_GBM#BTC#240min | 101 | +0.063 | +7.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 1115 | +0.001 | +20.12€ | 3 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 167 | -0.021 | -6.72€ | 0 | 1 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 911 | -0.007 | -6.55€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 126 | +0.086 | +24.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 9 | +0.021 | +0.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 776 | -0.023 | -31.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 1864 | -0.004 | -9.82€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 875 | +0.014 | +17.42€ | 1 | 4 |
| ✅ UPDOWN_GBM#ETH#240min | 94 | +0.042 | +3.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 660 | -0.033 | -28.57€ | 3 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 220 | +0.004 | -1.33€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 2370 | +0.002 | +1.82€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 762 | +0.003 | +3.44€ | 1 | 3 |
| ✅ UPDOWN_GBM#SOL#240min | 86 | -0.011 | -3.55€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 1395 | +0.005 | -0.90€ | 4 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 115 | +0.004 | +2.96€ | 1 | 3 |
| ✅ UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 1274 | +0.013 | +83.78€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 705 | +0.049 | +112.15€ | 0 | 8 |
| ✅ UPDOWN_GBM#XRP#240min | 37 | -0.167 | -7.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 532 | -0.022 | -21.25€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 245 | +0.326 | +59.80€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 245 | +0.326 | +59.80€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 142 | +0.312 | +25.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 142 | +0.312 | +25.25€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 103 | +0.338 | +34.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 103 | +0.338 | +34.55€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 5116 | -0.068 | +1024.43€ | 4 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 5116 | -0.068 | +1024.43€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 305 | -0.051 | +341.15€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 305 | -0.051 | +341.15€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 1038 | -0.155 | -89.37€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 1038 | -0.155 | -89.37€ | 5 | 1 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 80 | +0.049 | +9.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 80 | +0.049 | +9.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 449 | +0.152 | +224.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 449 | +0.152 | +224.05€ | 2 | 16 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 1671 | -0.061 | +317.07€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 1671 | -0.061 | +317.07€ | 3 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 1573 | -0.089 | +221.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 1573 | -0.089 | +221.70€ | 3 | 5 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 42 | +0.023 | -0.97€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 42 | +0.023 | -0.97€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 42 | +0.023 | -0.97€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 42 | +0.023 | -0.97€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 404 | +0.291 | +325.61€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 404 | +0.291 | +325.61€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 230 | +0.284 | +179.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 230 | +0.284 | +179.53€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 174 | +0.295 | +146.08€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 174 | +0.295 | +146.08€ | 0 | 13 |
| ✅ UPDOWN_OU_5M | 630 | -0.095 | -70.17€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#5min | 630 | -0.095 | -70.17€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 310 | -0.077 | -35.00€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 310 | -0.077 | -35.00€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 157 | -0.041 | -7.21€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 157 | -0.041 | -7.21€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 31 | -0.197 | -6.72€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 31 | -0.197 | -6.72€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 51 | -0.141 | -6.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 51 | -0.141 | -6.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 48 | -0.180 | -7.92€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 48 | -0.180 | -7.92€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 1302 | +0.292 | +566.93€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 411 | +0.219 | +19.52€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 424 | +0.272 | +119.01€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 467 | +0.372 | +428.39€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.089) — sin ventaja clara. oversold(IBS<0.3): IC=+0.022 n=2996 | neutral: IC=+0.001 n=3236 | overbought(IBS>0.7): IC=+0.090 n=3256
  - _Datos_: n=9873 IC=+0.039 PNL=+973.18€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: (cache 407s) 98 celda(s) GATE OK de 2370 trackeadas

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.003 < 0.08 — monitorear
  - _Datos_: n=762 IC=+0.003 PNL=+3.44€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=424/15 IC=+0.272 PNL=+119.01€ | BTC: n=411/15 IC=+0.219 PNL=+19.52€ | SOL: n=467/15 IC=+0.372 PNL=+428.39€

**🟡 H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.070 n=137924 | tras_1loss IC=+0.047 n=108506 | tras_2loss IC=+0.010 n=49107/40 | gap=+0.060 (umbral 0.05)

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 20 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH#60min, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC
  - _Bloqueante_: N_INSUFICIENTE


### ⏳ Acumulando datos

**⏳ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: 15
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: Falta 11 ops más en GBM@18h (IC actual=-0.067)
  - _Datos_: n=4 IC=-0.067 PNL=-3.02€

**⏳ H-HORA-GBM** — hora_utc causal automático en GBM (forward)
  - _Umbral_: n≥20 forward con hora_utc + alguna hora con n≥15 IC<-0.10 o >+0.10
  - _Acción_: El sistema lo aplica automáticamente vía FEATURE_RULES. Verificar en strategy_params.json.
  - _Estado_: 8266 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.082 n=53/60 | contraria IC=+0.048 n=29 | gap=+0.033 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=137, boost estimado=+0.007. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 94 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=220/40 IC=+0.004 PNL=-1.33€ | BTC#60min: n=167/40 IC=-0.021 PNL=-6.72€ | SOL#60min: n=115/40 IC=+0.004 PNL=+2.96€

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=-0.004 n=834 | contrario_BTC IC=-0.018 n=672/40 | gap=-0.014 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.200 > 0.08 con n=78 PNL=+52.02€
  - _Datos_: n=78 IC=+0.200 PNL=+52.02€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.145 > 0.08 con n=108 PNL=+34.13€
  - _Datos_: n=108 IC=+0.145 PNL=+34.13€

**⏳ H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: 25
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: 22/25 ops en el filtro definido (IC actual=+0.250 PNL=+16.04€)
  - _Datos_: n=22 IC=+0.250 PNL=+16.04€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.335 > 0.1 con n=1105 PNL=+573.42€
  - _Datos_: n=1105 IC=+0.335 PNL=+573.42€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=74 IC=+0.053 PNL=+13.80€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=74 IC=+0.053 PNL=+13.80€

**⏳ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: 30
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: 26/30 ops en el filtro definido (IC actual=+0.214 PNL=+19.08€)
  - _Datos_: n=26 IC=+0.214 PNL=+19.08€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=8051 IC=+0.003 PNL=+142.00€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=8051 IC=+0.003 PNL=+142.00€

**⏳ H-CUSTOM-OF-02H-BTCSOL** — ORDER_FLOW H=02h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 02h está en el blacklist basado en TODOS los pares. Con BTC+SOL solo, el historial muestra 4/5 (80%) IC=+0.054. ¿Se confirma la señal positiva con más datos?
  - _Umbral_: 15
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 02h del blacklist ORDER_FLOW
  - _Estado_: 2/15 ops en el filtro definido (IC actual=+0.025 PNL=+3.18€)
  - _Datos_: n=2 IC=+0.025 PNL=+3.18€

**⏳ H-CUSTOM-OF-07H-BTCSOL** — ORDER_FLOW H=07h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 07h está en el blacklist. Con BTC+SOL solo, el historial muestra 7/12 (58%) IC=+0.043. El blacklist puede estar basado en pares negativos que ya están excluidos.
  - _Umbral_: 20
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 07h del blacklist ORDER_FLOW
  - _Estado_: 0/20 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: 07h sigue en ORDER_FLOW_BLACKLIST_HOURS -- mientras siga ahí, nunca genera fila para volver a evaluarse (26-Ago, triage candidatas estancadas)

**〰️ H-CUSTOM-GBM-60MIN-BUYYES** — GBM 60min BUY_YES — ¿edge superior al BUY_NO?
  - _Hipótesis_: Análisis actual muestra BUY_YES 60min: 22/36 (61%) IC=+0.105 vs BUY_NO 60min: 8/14 (57%) IC=+0.044. En 60min parece que BUY_YES es la dirección dominante, al contrario que en 15min.
  - _Umbral_: n≥30 y IC>+0.08
  - _Acción_: Si BUY_YES 60min confirma IC≥0.10 n≥40 → prioridad live por encima de BUY_NO
  - _Estado_: n=416 IC=+0.010 PNL=+1.34€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=416 IC=+0.010 PNL=+1.34€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=86 IC=-0.068 PNL=-6.43€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=86 IC=-0.068 PNL=-6.43€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=149 IC=-0.030 PNL=-1.68€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=149 IC=-0.030 PNL=-1.68€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.123 > 0.1 con n=593 PNL=+167.24€
  - _Datos_: n=593 IC=+0.123 PNL=+167.24€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=194 IC=+0.076 PNL=+41.53€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=194 IC=+0.076 PNL=+41.53€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=310 IC=+0.090 PNL=+67.37€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=310 IC=+0.090 PNL=+67.37€

**⏳ H-CUSTOM-DRIFT15-ZONA-MUERTA** — GBM#15min drift_15min ∈ [-0.3,+0.3] — zona muerta de señal
  - _Hipótesis_: Análisis n=127 GBM#15min: cuando drift_15min está entre -0.3 y +0.3 (mercado sin dirección clara) el IC es negativo (-0.043). Cuando drift>0.3 IC=+0.100 (n=28). Cuando drift<-1 IC=+0.048 (reversión). La señal requiere mercado con dirección clara.
  - _Umbral_: 50
  - _Acción_: Filtrar señales GBM#15min cuando drift_15min ∈ [-0.3, +0.3] — validar con n≥50 antes de implementar
  - _Estado_: 0/50 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: confirmada 2026-07-01 (IC=-0.037 n=52) e implementada en shadow_predict.py (skip si drift_15min∈[-0.3,0.3)) -- verificado 26-Ago con 2177 filas post-TWAP reales, 0 caen en la zona filtrada. Frozen by design, no falta n

**〰️ H-CUSTOM-DRIFT15-MOMENTUM** — GBM#15min drift_15min > 0.3 — zona de momentum (señal fuerte)
  - _Hipótesis_: Cuando drift_15min > 0.3%/h el GBM captura bien la dirección: IC=+0.100 n=28 en todos GBM#15min; IC=+0.152 n=13 solo BTC. El mercado tiene dirección clara y el GBM la sigue. Hipótesis: este rango es donde la señal es real.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma IC>0.10 con n≥40 → boost ×1.2 en GBM#15min cuando drift_15min>0.3
  - _Estado_: n=1708 IC=+0.028 PNL=+123.19€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1708 IC=+0.028 PNL=+123.19€

**〰️ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: n=32 IC=-0.265 PNL=-8.09€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=32 IC=-0.265 PNL=-8.09€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=93 IC=-0.037 PNL=+6.73€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=93 IC=-0.037 PNL=+6.73€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=113 IC=+0.039 PNL=+9.48€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=113 IC=+0.039 PNL=+9.48€

**⏳ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: 15
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: 8/15 ops en el filtro definido (IC actual=+0.080 PNL=+2.13€)
  - _Datos_: n=8 IC=+0.080 PNL=+2.13€

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=2327 IC=-0.022 PNL=-61.75€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2327 IC=-0.022 PNL=-61.75€

**🟡 H-FUNDING-NEGATIVE-BUYYES** — Funding rate negativo (<-0.01%/8h) → BUY_YES tiene más edge (short squeeze)
  - _Hipótesis_: Cuando funding < -0.01%/8h, los shorts están pagando por mantener la posición. Históricamente precede squeezes en cripto. Hipótesis: BUY_YES GBM tiene IC superior en régimen de funding negativo.
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si se confirma → boost ×1.1 en BUY_YES cuando funding_rate_8h < -0.01
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.175 > 0.08 con n=38 PNL=+9.28€
  - _Datos_: n=38 IC=+0.175 PNL=+9.28€

**🔶 H-LATE-WINDOW-5MIN** — Late-window BTC 5min — arbitraje timing vs Polymarket
  - _Hipótesis_: Inspirado en VyvanseWithMarijuana (36.5% ROI, $42k vol). A T+160-270s dentro de una ventana BTC 5min, si BTC ya se movió >0.3%, Polymarket no ha actualizado precio → edge estructural. Estrategia LATE_WINDOW_5MIN en shadow hasta n≥30. FIX 2026-07-02: la estrategia llevaba 0 predicciones desde su creacion porque HORIZONTE_MIN_HORAS=0.05 (3min) descartaba todo mercado a <3min de expirar — y su zona de entrada (160-270s de una ventana de 5min) deja 30-140s restantes, siempre bajo el suelo. Corregido en shadow_predict (zona late-window marcada _solo_late, 30s-3min, solo evaluada por esta estrategia). El reloj de acumulacion empieza de verdad hoy. Contexto extra: el estudio de ballenas de hoy confirma que comprar el lado ganador a mitad/final de ventana es el playbook comun de los 3 mayores ganadores verificados de estos mercados (Bonereaper +$19.9k/mes, wowitsamazing +$10k/mes, zhangfan151 +$8.7k/mes).
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si IC≥0.08 con n≥30 → proponer pasar a live con stake mínimo (0.50€). Si IC<0 con n≥30 → el lag de Polymarket en BTC es insuficiente.
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.210 n=36) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=36 IC=+0.210 PNL=+12.46€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=2193 IC=+0.016 PNL=+95.77€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2193 IC=+0.016 PNL=+95.77€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=574 IC=+0.038 PNL=+14.73€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=574 IC=+0.038 PNL=+14.73€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.106 > 0.08 con n=196 PNL=+50.80€
  - _Datos_: n=196 IC=+0.106 PNL=+50.80€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.115 > 0.08 con n=141 PNL=+7.31€
  - _Datos_: n=141 IC=+0.115 PNL=+7.31€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.142 > 0.08 con n=135 PNL=+49.07€
  - _Datos_: n=135 IC=+0.142 PNL=+49.07€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=26986 IC=+0.102 PNL=+8484.48€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=26986 IC=+0.102 PNL=+8484.48€

**〰️ H-CUSTOM-MERCURY-RETROGRADO** — Mercurio retrógrado: ¿rendimiento peor durante la ventana?
  - _Hipótesis_: Mismo origen que H-CUSTOM-MOON-LLENA (paper de Fornero, 43 Jornadas SADAF 2023). Qi, Wang & Zhang (2022, 48 mercados, 1973-2019): rendimientos 3.33%/año más bajos durante Mercurio retrógrado. Kou & Ma (2022) en China (99.8% cuentas retail): hasta -31% anualizado. Ambos estudios confirman que el mecanismo es la creencia/superstición de inversores retail (mayor efecto cuanto más retail y más supersticioso el mercado), no un efecto astral literal — Polymarket encaja en ese perfil. Ventanas 2026 (fuente pública, actualizar cada año): 26-feb a 20-mar, 29-jun a 23-jul, 24-oct a 13-nov.
  - _Umbral_: n≥100 PERO ADEMÁS necesita cubrir al menos 2-3 ventanas de retrogradación distintas (no solo la de jun-jul 2026) — esperar mínimo hasta después de la ventana de oct-nov 2026
  - _Acción_: Si IC en mercury_retrogrado=1 < IC en mercury_retrogrado=0 con margen ≥0.05 y ≥2 ventanas distintas cubiertas → considerar boost/filtro. No implementar tras una sola ventana (jun-jul 2026) por more que n sea alto — sería solo un evento, no un patrón.
  - _Estado_: n=1792 IC=+0.109 PNL=+195.82€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=1792 IC=+0.109 PNL=+195.82€

**〰️ H-CUSTOM-SMART-MONEY-CONSENSUS** — Consenso de wallets 'smart money' — ¿confirma nuestra dirección?
  - _Hipótesis_: Javi propuso estudiar bots/wallets que operan bien en nuestros mismos mercados. En vez de creer artículos (ya verificamos 2 veces esta semana que las narrativas no aguantan el cruce con datos reales), smart_money_tracker.py mide el track record REAL de wallets activas en BTC/ETH/SOL/XRP Up-or-Down 5/15/60min vía data-api.polymarket.com/positions, filtrado a posiciones 'Up or Down'. Clasifica como 'smart' las wallets con n>=10 posiciones, win_rate>=0.55 y pnl_total>0. smart_money_consensus es el sesgo direccional reciente (Up-Down)/(Up+Down) de esas wallets 'smart' por activo. Hipótesis: si nuestra decisión (BUY_YES/BUY_NO) coincide con el consenso smart money, mejor IC que cuando diverge. RESET METODOLOGICO 2026-07-02: la clasificacion 'smart' original via /positions estaba INVERTIDA para wallets de alta frecuencia (el endpoint solo retiene el residuo perdedor sin redimir; verificado: 'wowitsamazing' figuraba como -$478k y es +$10k/mes en el leaderboard oficial). Desde 2026-07-02T06:12Z el consenso se construye solo con wallets verificadas en el leaderboard oficial (pnl_mes>=$1000, 24 wallets). Los valores de smart_money_consensus capturados en features ANTES de esa fecha provienen de la clasificacion rota — descontar ese tramo al evaluar.
  - _Umbral_: n≥40 y IC>+0.08 — además necesita que existan wallets 'smart' acumuladas (0 al empezar, se van descubriendo cada ciclo)
  - _Acción_: Si IC en confluencia (decisión coincide con signo de smart_money_consensus) supera en >=0.05 al IC en divergencia, con n≥40 en cada lado → boost ×1.1-1.2 cuando coincide, considerar reducir stake cuando diverge fuerte.
  - _Estado_: n=1148 IC=+0.031 PNL=+67.35€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1148 IC=+0.031 PNL=+67.35€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.128 > 0.02 con n=377 PNL=+135.80€
  - _Datos_: n=377 IC=+0.128 PNL=+135.80€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=127 IC=-0.043 PNL=+34.76€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=127 IC=-0.043 PNL=+34.76€

**〰️ H-CUSTOM-WEEKLY-INRANGE-BUYYES** — WEEKLY_PRICE BUY_YES con in_range=1 — ¿estructuralmente sobrevalorado?
  - _Hipótesis_: Analizado 2026-07-01, n=10 (evidencia mínima): BUY_YES cuando in_range=1 fue 0/3 (todo pérdida). Mecanismo propuesto: acertar un rango de precio estrecho al vencimiento es intrínsecamente poco probable, el mercado puede estar sobrevalorando el 'sí'. Ver H-CUSTOM-WEEKLY-PCTDIST-BUYNO para el lado complementario (BUY_NO con pct_dist alto).
  - _Umbral_: n≥25 y IC<-0.10 para confirmar (evidencia inicial es de solo 3 ops)
  - _Acción_: Si se confirma con n≥25 → filtro causal in_range==1 + BUY_YES → skip en WEEKLY_PRICE
  - _Estado_: n=81 IC=-0.030 PNL=+3.88€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=81 IC=-0.030 PNL=+3.88€

**🟡 H-CUSTOM-WEEKLY-PCTDIST-BUYNO** — WEEKLY_PRICE BUY_NO con pct_dist alto — cuanto más lejos del rango, más seguro
  - _Hipótesis_: Analizado 2026-07-01, n=10 (evidencia mínima): BUY_NO con pct_dist>=2.09% fue 4/4 victorias (rango 2.09%-23.4%); BUY_NO con pct_dist<8% (pero fuera del corte anterior) tuvo derrotas. Patrón: cuanto más lejos está el spot del rango objetivo al momento de la predicción, más fiable el BUY_NO. Complementa H-CUSTOM-WEEKLY-INRANGE-BUYYES.
  - _Umbral_: n≥25 y IC>+0.10 para confirmar
  - _Acción_: Si se confirma con n≥25 → boost ×1.2 en WEEKLY_PRICE BUY_NO cuando pct_dist≥2
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.445 > 0.1 con n=683 PNL=+602.86€
  - _Datos_: n=683 IC=+0.445 PNL=+602.86€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=1880 IC=+0.023 PNL=+119.65€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=1880 IC=+0.023 PNL=+119.65€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.166 > 0.1 con n=888 PNL=+340.94€
  - _Datos_: n=888 IC=+0.166 PNL=+340.94€

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.211 < -0.1 con n=43 PNL=-2.82€
  - _Datos_: n=43 IC=-0.211 PNL=-2.82€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=554 IC=+0.032 PNL=+58.35€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=554 IC=+0.032 PNL=+58.35€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=30 IC=-0.188 PNL=+2.99€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=30 IC=-0.188 PNL=+2.99€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.119 > 0.1 con n=103 PNL=+18.94€
  - _Datos_: n=103 IC=+0.119 PNL=+18.94€

**⏳ H-CUSTOM-ETH15-BUYNO-PRECIO-ALTO** — ETH#15min BUY_NO con precio_yes>0.55 pierde (NO longshot contra favorito)
  - _Hipótesis_: Detectado 2026-07-02: ult.60 shadow ETH15 BUY_NO — py_mkt~0.5 wr=0.67 PNL=+29.3 (n=49); py_mkt 0.6-0.8 wr 0.33-0 PNL=-5.75 (n=9). Filtro RETURN NONE (no SKIP) aplicado en shadow_predict.py (PY_MKT_MAX_BUY_NO_ETH15=0.55) el mismo dia -- bloquea la GENERACIÓN de la fila, no solo la decisión. Esta hipotesis trackea la zona filtrada: si las ops que HABRIAN caido aqui siguen apareciendo en otras estrategias o el IC forward de la zona se vuelve positivo, revisar el filtro. CAVEAT: n=9, muestra chica — el filtro se aplico por asimetria de riesgo (afecta a dinero live), no por significancia. ⚠️ 05-Ago (fix): la clave del filtro decía 'py_mkt', que NUNCA existió ni en features de UPDOWN_GBM (T_h/delta_ratio_macro/drift_15min/drift_60min/pct_spot_vs_ref/sigma_h) ni como columna top-level de results.csv -- corregida a 'precio_yes_mercado' (columna real). Aun así, con la clave correcta esta hipótesis NUNCA podrá acumular n mientras el filtro RETURN NONE siga activo -- es el mismo patrón 'frozen by design' que H-CUSTOM-LATE15-PHOTO-FINISH (más abajo): la propia protección impide generar los datos necesarios para volver a evaluarla. Para monitorearla de verdad haría falta un logger separado que capture la señal SIN aplicar el filtro (mismo patrón que gate_bucket_propio con data/markets histórico) -- no construido, pendiente decisión.
  - _Umbral_: 20
  - _Acción_: Si IC forward de la zona >0 con n>=20 → retirar filtro; si confirma negativo → considerar extender a BTC/SOL 15min
  - _Estado_: 2/20 ops en el filtro definido (IC actual=-0.025 PNL=-1.02€)
  - _Datos_: n=2 IC=-0.025 PNL=-1.02€
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: PY_MKT_MAX_BUY_NO_ETH15=0.55 en shadow_predict.py hace RETURN NONE (bloquea generación, no solo decisión) -- nunca podrá acumular n mientras siga activo. Haría falta un logger separado sin el filtro para monitorear de verdad (no construido, 26-Ago)

**〰️ H-PRECIO-YES-BARATO** — BUY_YES con precio de mercado 0.30-0.40 — mercado infravalora YES
  - _Hipótesis_: Detectado 2026-07-03 en benchmark de calibración del mercado (7d, estrategias GBM): en el bucket precio_yes_mercado [0.3-0.4) la frecuencia real de YES fue 0.45 vs 0.35 implícito (+0.10, n=38). Posible sesgo favorito-longshot suave en binarios de 15min (complemento del LONGSHOT ya activo para BUY_NO con py<0.20). Si se confirma, BUY_YES comprado en esa banda lleva viento de cola estructural del propio mercado, independiente del modelo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → kelly_boost ×1.1 para BUY_YES con precio_yes_mercado en [0.30,0.40), simétrico al longshot BUY_NO existente
  - _Estado_: n=6793 IC=-0.148 PNL=+186.05€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=6793 IC=-0.148 PNL=+186.05€

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
  - _Estado_: n=836 IC=+0.146 PNL=+431.96€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=836 IC=+0.146 PNL=+431.96€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.125 > 0.08 con n=577 PNL=+163.86€
  - _Datos_: n=577 IC=+0.125 PNL=+163.86€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=809 IC=-0.003 PNL=-1.04€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=809 IC=-0.003 PNL=-1.04€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.080 > 0.08 con n=815 PNL=+416.15€
  - _Datos_: n=815 IC=+0.080 PNL=+416.15€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.172 > 0.08 con n=172 PNL=+66.33€
  - _Datos_: n=172 IC=+0.172 PNL=+66.33€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.248 < -0.1 con n=755 PNL=-125.61€
  - _Datos_: n=755 IC=-0.248 PNL=-125.61€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=1896 IC=+0.122 PNL=+975.37€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=1896 IC=+0.122 PNL=+975.37€

**🟡 H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: n≥40 en cada rama (contrario y alineado) para separar señal de ruido
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.096 > 0.08 con n=45 PNL=+13.21€
  - _Datos_: n=45 IC=+0.096 PNL=+13.21€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=861 IC=-0.019 PNL=+75.52€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=861 IC=-0.019 PNL=+75.52€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.176 > 0.08 con n=763 PNL=+463.04€
  - _Datos_: n=763 IC=+0.176 PNL=+463.04€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=1279 IC=-0.067 PNL=+263.33€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1279 IC=-0.067 PNL=+263.33€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.116 > 0.08 con n=295 PNL=-37.93€
  - _Datos_: n=295 IC=+0.116 PNL=-37.93€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.233 > 0.08 con n=1867 PNL=-180.95€
  - _Datos_: n=1867 IC=+0.233 PNL=-180.95€

**⏳ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: 15/40 ops en el filtro definido (IC actual=-0.022 PNL=+2.89€)
  - _Datos_: n=15 IC=-0.022 PNL=+2.89€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.112 n=225) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=225 IC=+0.112 PNL=+61.99€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.317 > 0.08 con n=91 PNL=+52.16€
  - _Datos_: n=91 IC=+0.317 PNL=+52.16€

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.426 n=268) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=268 IC=+0.426 PNL=+369.33€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=4111 IC=+0.141 PNL=-686.20€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=4111 IC=+0.141 PNL=-686.20€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.241 > 0.1 con n=56 PNL=+38.56€
  - _Datos_: n=56 IC=+0.241 PNL=+38.56€
