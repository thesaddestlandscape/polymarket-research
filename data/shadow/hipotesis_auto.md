# Hipótesis automáticas — 2026-08-27 11:47 UTC
_Generado por shadow_postmortem.py sobre 173952 resoluciones (PNL=+12622.20€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.705` → IC=-0.167 (n=88)

  - _Acción_: SKIP cuando `py_entrada` < 0.705
  - _Potencial_: sin este filtro IC_bueno=+0.270 (n=233)

- **PATRÓN** `py_entrada` > `0.725` → IC=+0.283 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.725 (IC base=+0.150)

- **PATRÓN** `n_ballena_banda` > `20.0` → IC=+0.165 (n=222)

  - _Acción_: Kelly boost +0.83€ cuando `n_ballena_banda` > 20.0 (IC base=+0.150)

- **PATRÓN** `n_total_lado` > `58.0` → IC=+0.238 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 58.0 (IC base=+0.150)

- **PATRÓN** `banda_hit_calibrado` > `0.8214` → IC=+0.261 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8214 (IC base=+0.150)

- **PATRÓN** `banda_z` > `10.822` → IC=+0.259 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 10.822 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.181 (n=164)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 11.0 (IC base=+0.150)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.174 (n=253)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `3111.6433` → IC=+0.241 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3111.6433 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `288.0` → IC=+0.295 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 288.0 (IC base=+0.150)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.136 (n=215)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.5 (IC base=+0.012)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.725` → IC=+0.285 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.725 (IC base=+0.189)

- **PATRÓN** `n_ballena_banda` > `20.0` → IC=+0.200 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `n_ballena_banda` > 20.0 (IC base=+0.189)

- **PATRÓN** `n_total_lado` > `57.0` → IC=+0.250 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 57.0 (IC base=+0.189)

- **PATRÓN** `banda_hit_calibrado` > `0.8211` → IC=+0.281 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8211 (IC base=+0.189)

- **PATRÓN** `banda_z` > `11.827` → IC=+0.282 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.827 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.218 (n=140)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.197 (n=183)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.189)

- **PATRÓN** `libro_liquidez` > `3838.6557` → IC=+0.253 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3838.6557 (IC base=+0.189)

- **PATRÓN** `ballena_activa_n` < `290.0` → IC=+0.305 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 290.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` < `0.795` → IC=+0.124 (n=115)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.795 (IC base=+0.003)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.335` → IC=-0.267 (n=28)

  - _Acción_: SKIP cuando `py_entrada` < 0.335
  - _Potencial_: sin este filtro IC_bueno=+0.193 (n=86)

- **FILTRO** `banda_hit_calibrado` < `0.6284` → IC=-0.218 (n=37)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.6284
  - _Potencial_: sin este filtro IC_bueno=+0.222 (n=77)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.141 (n=90)

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

- **PATRÓN** `py_entrada` > `0.335` → IC=+0.193 (n=86)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.335 (IC base=+0.078)

- **PATRÓN** `banda_hit_calibrado` > `0.6284` → IC=+0.222 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6284 (IC base=+0.078)

- **PATRÓN** `banda_z` > `8.174` → IC=+0.183 (n=39)

  - _Acción_: Kelly boost +0.91€ cuando `banda_z` > 8.174 (IC base=+0.078)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.141 (n=90)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.02 (IC base=+0.078)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.134 (n=69)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.495 (IC base=-0.024)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `147.36` → IC=-0.285 (n=2420)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 147.36
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=7261)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `138.64` → IC=-0.234 (n=302)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 138.64
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=908)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `concentracion_yes` < `1.0` → IC=-0.122 (n=125)

  - _Acción_: SKIP cuando `concentracion_yes` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=571)

- **FILTRO** `n_ballenas` < `8.0` → IC=-0.159 (n=218)

  - _Acción_: SKIP cuando `n_ballenas` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=478)

- **FILTRO** `restante_s_al_confirmar` < `394.82` → IC=-0.267 (n=174)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 394.82
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=522)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `97.92` → IC=-0.428 (n=302)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 97.92
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=908)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `160.37` → IC=-0.182 (n=656)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 160.37
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=1968)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `154.88` → IC=-0.257 (n=565)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 154.88
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=1698)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `117.99` → IC=-0.381 (n=419)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 117.99
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=1259)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.7` → IC=+0.188 (n=5450)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.7 (IC base=+0.098)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.170 (n=1586)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.01 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `2385.1288` → IC=+0.174 (n=1530)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2385.1288 (IC base=+0.098)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.144 (n=3641)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 17.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.157 (n=4359)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 7.0 (IC base=+0.141)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.258 (n=3358)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.189 (n=2955)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.02 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `1861.5529` → IC=+0.180 (n=2471)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 1861.5529 (IC base=+0.141)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.222 (n=641)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.206)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.396 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.208 (n=789)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.197 (n=575)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 7.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.191 (n=448)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 11.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.291 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.185)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.184 (n=825)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.01 (IC base=+0.185)

- **PATRÓN** `libro_liquidez` > `12342.075` → IC=+0.212 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12342.075 (IC base=+0.185)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.131 (n=540)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.136 (n=465)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 15.0 (IC base=+0.118)

- **PATRÓN** `py_entrada` > `0.555` → IC=+0.137 (n=538)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` > 0.555 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `4922.6447` → IC=+0.160 (n=204)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 4922.6447 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.192 (n=186)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 7.0 (IC base=+0.134)

- **PATRÓN** `py_entrada` < `0.415` → IC=+0.179 (n=303)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.415 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `4198.5556` → IC=+0.152 (n=285)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4198.5556 (IC base=+0.134)

### FAVORITO_CONFIRMADO#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.132 (n=1222)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.125 (n=1045)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 15.0 (IC base=+0.122)

- **PATRÓN** `py_entrada` > `0.69` → IC=+0.308 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.293 (n=211)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.280)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.280 (n=476)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.280)

- **PATRÓN** `py_entrada` < `0.195` → IC=+0.420 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.195 (IC base=+0.280)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.280 (n=485)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `2912.4246` → IC=+0.285 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2912.4246 (IC base=+0.280)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.161 (n=281)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 15.0 (IC base=+0.140)

- **PATRÓN** `py_entrada` > `0.655` → IC=+0.252 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.655 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.146 (n=391)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.02 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `1969.6267` → IC=+0.159 (n=318)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 1969.6267 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `4420.281` → IC=+0.157 (n=141)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 4420.281 (IC base=+0.078)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.218 (n=307)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.196 (n=646)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 12.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` > `0.84` → IC=+0.443 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.84 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.256 (n=211)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` < `0.205` → IC=+0.352 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.205 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.231 (n=566)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `2070.6009` → IC=+0.243 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2070.6009 (IC base=+0.221)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `19.0` → IC=+0.265 (n=79)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 19.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.192 (n=105)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 8.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.342 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.239 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.189)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.214 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.103)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.144 (n=273)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.02 (IC base=+0.103)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `10.0` → IC=-0.292 (n=70)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.205 (n=93)

- **FILTRO** `py_entrada` > `0.845` → IC=-0.379 (n=31)

  - _Acción_: SKIP cuando `py_entrada` > 0.845
  - _Potencial_: sin este filtro IC_bueno=-0.209 (n=132)

- **FILTRO** `libro_liquidez` < `7724.7843` → IC=-0.258 (n=122)

  - _Acción_: SKIP cuando `libro_liquidez` < 7724.7843
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=41)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.192 (n=4531)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.189 (n=3887)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.199 (n=2172)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.185)

- **PATRÓN** `libro_liquidez` > `3258.7888` → IC=+0.357 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3258.7888 (IC base=+0.185)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.171 (n=775)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 11.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.178 (n=997)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 15.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.184 (n=1112)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` < 0.73 (IC base=+0.167)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.230 (n=61)

- **FILTRO** `py_entrada` > `0.795` → IC=-0.397 (n=27)

  - _Acción_: SKIP cuando `py_entrada` > 0.795
  - _Potencial_: sin este filtro IC_bueno=-0.212 (n=57)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.417 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.328)

- **PATRÓN** `py_entrada` > `0.835` → IC=+0.372 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.835 (IC base=+0.328)

- **PATRÓN** `libro_liquidez` > `2916.5858` → IC=+0.343 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2916.5858 (IC base=+0.328)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.166 (n=1158)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.161)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.167 (n=983)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 15.0 (IC base=+0.161)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.168 (n=416)

  - _Acción_: Kelly boost +0.84€ cuando `py_entrada` < 0.7 (IC base=+0.161)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.168 (n=775)

  - _Acción_: Kelly boost +0.84€ cuando `py_entrada` > 0.72 (IC base=+0.161)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.239 (n=1033)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.227 (n=885)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.227)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.317 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.227)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.192 (n=1110)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.182 (n=959)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 15.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.198 (n=558)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.7 (IC base=+0.181)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.454 (n=216)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.444)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.446 (n=200)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.444)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.448 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.444)

- **PATRÓN** `libro_liquidez` > `3382.6049` → IC=+0.461 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3382.6049 (IC base=+0.444)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.444 (n=88)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.440)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.438 (n=79)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.440)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.440)

- **PATRÓN** `libro_liquidez` > `12599.6821` → IC=+0.452 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12599.6821 (IC base=+0.440)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.451 (n=80)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.430)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.433 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.430)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.430 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.430)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.429 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.430)

- **PATRÓN** `libro_liquidez` > `3860.0656` → IC=+0.476 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3860.0656 (IC base=+0.430)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.441 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.446)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.449 (n=57)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.446)

- **PATRÓN** `py_entrada` < `0.92` → IC=+0.435 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.92 (IC base=+0.446)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.450 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.446)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.441 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.446)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.203 (n=4688)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.194 (n=8243)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 11.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.221 (n=8830)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.191)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.130 (n=2371)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.131 (n=1517)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 11.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.156 (n=1719)

  - _Acción_: Kelly boost +0.78€ cuando `py_entrada` > 0.71 (IC base=+0.125)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.245 (n=1919)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.238)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.275 (n=1423)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.238)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.181 (n=810)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 17.0 (IC base=+0.165)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.167 (n=1526)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 12.0 (IC base=+0.165)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.216 (n=734)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.165)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.236 (n=1970)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.230)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.291 (n=692)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.230)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.230 (n=768)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.246 (n=1201)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.217)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.195 (n=794)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.194 (n=1391)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 11.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.211 (n=1519)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.185)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.199 (n=1650)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.38 (IC base=+0.133)

- **PATRÓN** `restante_min` < `3.96` → IC=+0.136 (n=1506)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` < 3.96 (IC base=+0.133)

- **PATRÓN** `restante_min` > `4.93` → IC=+0.162 (n=1518)

  - _Acción_: Kelly boost +0.81€ cuando `restante_min` > 4.93 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.151 (n=1987)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 7.0 (IC base=+0.133)

- **PATRÓN** `lag_apertura_s` < `4.44` → IC=+0.160 (n=1494)

  - _Acción_: Kelly boost +0.80€ cuando `lag_apertura_s` < 4.44 (IC base=+0.133)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.203 (n=827)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.141)

- **PATRÓN** `restante_min` > `4.91` → IC=+0.171 (n=778)

  - _Acción_: Kelly boost +0.85€ cuando `restante_min` > 4.91 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.154 (n=1973)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 15.0 (IC base=+0.141)

- **PATRÓN** `lag_apertura_s` < `5.5` → IC=+0.173 (n=744)

  - _Acción_: Kelly boost +0.86€ cuando `lag_apertura_s` < 5.5 (IC base=+0.141)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=823)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.126)

- **PATRÓN** `restante_min` < `4.42` → IC=+0.126 (n=996)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.42 (IC base=+0.126)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.161 (n=808)

  - _Acción_: Kelly boost +0.80€ cuando `restante_min` > 4.94 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.127 (n=2350)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 5.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.136 (n=1006)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 7.0 (IC base=+0.126)

- **PATRÓN** `lag_apertura_s` < `3.48` → IC=+0.163 (n=751)

  - _Acción_: Kelly boost +0.81€ cuando `lag_apertura_s` < 3.48 (IC base=+0.126)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.316 (n=410)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.301)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.305 (n=598)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.301)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.376 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.8 (IC base=+0.301)

- **PATRÓN** `libro_liquidez` > `3861.5788` → IC=+0.302 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3861.5788 (IC base=+0.301)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.288 (n=248)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.282)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.286 (n=227)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.282)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.359 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.282)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.284 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `5603.2188` → IC=+0.312 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5603.2188 (IC base=+0.282)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.334 (n=191)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.302)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.311 (n=278)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.302)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.387 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.302)

- **PATRÓN** `libro_liquidez` > `2046.5008` → IC=+0.325 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2046.5008 (IC base=+0.302)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.391 (n=53)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.359)

- **PATRÓN** `py_entrada` > `0.88` → IC=+0.429 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.88 (IC base=+0.359)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.357 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.359)

- **PATRÓN** `libro_liquidez` > `786.7393` → IC=+0.381 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 786.7393 (IC base=+0.359)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.423 (n=257)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.414)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.424 (n=248)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.414)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.423 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.414)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.428 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.414)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.413 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.414)

- **PATRÓN** `libro_liquidez` > `1842.491` → IC=+0.427 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1842.491 (IC base=+0.414)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.420 (n=111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.412)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.429 (n=111)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.412)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.417 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.412)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.422 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.412)

- **PATRÓN** `libro_liquidez` > `5548.4507` → IC=+0.449 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5548.4507 (IC base=+0.412)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.424 (n=104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.420)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.441 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.420)

- **PATRÓN** `py_entrada` > `0.91` → IC=+0.425 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.91 (IC base=+0.420)

- **PATRÓN** `libro_liquidez` > `1842.491` → IC=+0.441 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1842.491 (IC base=+0.420)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.310 (n=293)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.290)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.440 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.290)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.307 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.290)

- **PATRÓN** `libro_liquidez` > `1619.2143` → IC=+0.339 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1619.2143 (IC base=+0.290)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.310 (n=293)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.290)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.440 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.290)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.307 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.290)

- **PATRÓN** `libro_liquidez` > `1619.2143` → IC=+0.339 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1619.2143 (IC base=+0.290)

### GBM_LATE_15M
- **PATRÓN** `ibs_20min` > `0.9475` → IC=+0.210 (n=759)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9475 (IC base=+0.065)

- **PATRÓN** `dist_vwap_pct` > `0.1852` → IC=+0.230 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1852 (IC base=+0.065)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.212` → IC=+0.166 (n=923)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 5.212 (IC base=+0.065)

- **PATRÓN** `volumen_regimen` < `0.63` → IC=+0.212 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.63 (IC base=+0.065)

- **PATRÓN** `volumen_regimen` > `1.0578` → IC=+0.242 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0578 (IC base=+0.065)

- **PATRÓN** `volumen_pendiente_norm` > `0.3081` → IC=+0.159 (n=177)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.3081 (IC base=+0.065)

- **PATRÓN** `volumen_spike_ratio` < `2.4495` → IC=+0.142 (n=1081)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.4495 (IC base=+0.065)

- **PATRÓN** `ibs_20min` < `0.2147` → IC=+0.133 (n=1544)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.2147 (IC base=+0.031)

- **PATRÓN** `dist_vwap_pct` < `0.2947` → IC=+0.145 (n=784)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.2947 (IC base=+0.031)

- **PATRÓN** `volumen_regimen` < `0.6291` → IC=+0.161 (n=252)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.6291 (IC base=+0.031)

- **PATRÓN** `volumen_regimen` > `1.0603` → IC=+0.142 (n=342)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 1.0603 (IC base=+0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.3023` → IC=+0.271 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3023 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` < `1.6284` → IC=+0.195 (n=368)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.6284 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` > `2.924` → IC=+0.233 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.924 (IC base=+0.031)

- **PATRÓN** `ballena_activa_n` < `219.0` → IC=+0.208 (n=494)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 219.0 (IC base=+0.031)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.180 (n=170)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0075 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.153 (n=344)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 11.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.289 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.81` → IC=+0.323 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.81 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.2139` → IC=+0.147 (n=83)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2139 (IC base=+0.119)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.285 (n=184)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0061 (IC base=+0.267)

- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.298 (n=92)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0073 (IC base=+0.267)

- **PATRÓN** `drift_60min` |x|≤ `0.0693` → IC=+0.340 (n=92)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0693 (IC base=+0.267)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.274 (n=259)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.267)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.276 (n=252)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.267)

- **PATRÓN** `ibs_20min` < `0.4341` → IC=+0.304 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4341 (IC base=+0.267)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.934` → IC=+0.300 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.934 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` < `0.0585` → IC=+0.279 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0585 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` > `0.2355` → IC=+0.275 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2355 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` < `1.8379` → IC=+0.295 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8379 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` > `2.7441` → IC=+0.314 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7441 (IC base=+0.267)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.324 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.267)

- **PATRÓN** `libro_liquidez` > `1980.3` → IC=+0.308 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1980.3 (IC base=+0.267)

- **PATRÓN** `ballena_activa_n` < `66.0` → IC=+0.275 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 66.0 (IC base=+0.267)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.234 (n=167)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.205)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.219 (n=126)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.0962` → IC=+0.229 (n=127)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0962 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.234 (n=381)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.205 (n=337)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `0.4244` → IC=+0.224 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4244 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `0.2115` → IC=+0.234 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2115 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.274` → IC=+0.233 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.274 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` < `1.2653` → IC=+0.211 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2653 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` > `1.0826` → IC=+0.241 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0826 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.2657` → IC=+0.250 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2657 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` < `1.4455` → IC=+0.253 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4455 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `11282.8623` → IC=+0.221 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11282.8623 (IC base=+0.205)

- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.175 (n=149)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0022 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.0753` → IC=+0.164 (n=147)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.0753 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.151 (n=408)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 7.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.148 (n=441)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 17.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.5988` → IC=+0.164 (n=439)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.5988 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` < `0.1372` → IC=+0.165 (n=371)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1372 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.912` → IC=+0.224 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.912 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.6283` → IC=+0.185 (n=147)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6283 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `1.0251` → IC=+0.142 (n=199)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 1.0251 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.094` → IC=+0.210 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.094 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `1.7569` → IC=+0.181 (n=224)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.7569 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.4122` → IC=+0.159 (n=335)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.4122 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=565)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `14234.0471` → IC=+0.189 (n=146)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 14234.0471 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `223.0` → IC=+0.191 (n=82)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 223.0 (IC base=+0.140)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `drift_60min` |x|≤ `0.099` → IC=+0.134 (n=200)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.67€ cuando `drift_60min` |x|≤ 0.099 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.213 (n=165)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.280 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.923` → IC=+0.258 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.923 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.174 (n=213)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `1915.8272` → IC=+0.149 (n=206)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1915.8272 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.140 (n=48)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 16.0 (IC base=+0.133)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.299 (n=147)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.258)

- **PATRÓN** `drift_60min` |x|≤ `0.1281` → IC=+0.287 (n=148)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1281 (IC base=+0.258)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.261 (n=153)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.258)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.279 (n=134)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.258)

- **PATRÓN** `ibs_20min` < `0.5322` → IC=+0.295 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5322 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.037` → IC=+0.318 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.037 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.576` → IC=+0.258 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.576 (IC base=+0.258)

- **PATRÓN** `volumen_pendiente_norm` > `0.4009` → IC=+0.439 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.4009 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` < `3.5547` → IC=+0.223 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.5547 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` > `2.7408` → IC=+0.241 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7408 (IC base=+0.258)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.283 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.258)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.223 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 47.0 (IC base=+0.258)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `ibs_20min` > `0.8686` → IC=-0.160 (n=201)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8686
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=607)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.162 (n=63)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=745)

- **PATRÓN** `dist_vwap_pct` > `0.124` → IC=+0.333 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.124 (IC base=-0.031)

- **PATRÓN** `dist_vwap_pct` < `0.0838` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0838 (IC base=-0.031)

- **PATRÓN** `volumen_regimen` < `1.0858` → IC=+0.306 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0858 (IC base=-0.031)

- **PATRÓN** `volumen_regimen` > `0.7026` → IC=+0.311 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7026 (IC base=-0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.0976` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0976 (IC base=-0.031)

- **PATRÓN** `volumen_spike_ratio` < `1.4376` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4376 (IC base=-0.031)

- **PATRÓN** `volumen_spike_ratio` > `2.1718` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1718 (IC base=-0.031)

- **PATRÓN** `dist_vwap_pct` > `0.2405` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2405 (IC base=-0.048)

- **PATRÓN** `volumen_pendiente_norm` > `0.064` → IC=+0.250 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.064 (IC base=-0.048)

- **PATRÓN** `volumen_spike_ratio` < `1.5459` → IC=+0.167 (n=31)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.5459 (IC base=-0.048)

- **PATRÓN** `volumen_spike_ratio` > `2.1625` → IC=+0.206 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1625 (IC base=-0.048)

- **PATRÓN** `ballena_activa_n` < `114.0` → IC=+0.184 (n=36)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 114.0 (IC base=-0.048)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.121 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=92)

- **FILTRO** `ibs_20min` > `0.5` → IC=-0.134 (n=623)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=679)

- **FILTRO** `sigma_ewma_delta_pct` > `4.949` → IC=-0.157 (n=275)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.949
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=1027)

- **FILTRO** `volumen_pendiente_norm` < `0.0964` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.0964
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

- **FILTRO** `volumen_spike_ratio` > `1.6234` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.6234
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.197 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0055 (IC base=+0.045)

- **PATRÓN** `drift_60min` |x|≤ `0.2691` → IC=+0.145 (n=60)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.2691 (IC base=+0.045)

- **PATRÓN** `ibs_20min` > `0.6842` → IC=+0.198 (n=41)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.6842 (IC base=+0.045)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.44` → IC=-0.163 (n=339)

  - _Acción_: SKIP cuando `ibs_20min` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=339)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.151 (n=127)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=551)

- **FILTRO** `ibs_20min` > `0.7778` → IC=-0.168 (n=293)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7778
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=880)

- **FILTRO** `sigma_ewma_delta_pct` > `6.668` → IC=-0.155 (n=192)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.668
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=981)

- **PATRÓN** `dist_vwap_pct` < `0.2396` → IC=+0.175 (n=38)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.2396 (IC base=-0.090)

- **PATRÓN** `volumen_regimen` > `0.6932` → IC=+0.183 (n=39)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 0.6932 (IC base=-0.090)

- **PATRÓN** `dist_vwap_pct` < `0.2029` → IC=+0.222 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2029 (IC base=-0.035)

- **PATRÓN** `volumen_regimen` < `0.6966` → IC=+0.226 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6966 (IC base=-0.035)

- **PATRÓN** `volumen_regimen` > `1.1355` → IC=+0.250 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1355 (IC base=-0.035)

- **PATRÓN** `volumen_spike_ratio` > `1.9721` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.9721 (IC base=-0.035)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.134 (n=1297)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` > 0.0076 (IC base=+0.053)

- **PATRÓN** `ibs_20min` > `0.9465` → IC=+0.246 (n=952)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9465 (IC base=+0.053)

- **PATRÓN** `dist_vwap_pct` > `1.2605` → IC=+0.284 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2605 (IC base=+0.053)

- **PATRÓN** `volumen_regimen` > `1.1694` → IC=+0.203 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1694 (IC base=+0.053)

- **PATRÓN** `volumen_pendiente_norm` < `0.1146` → IC=+0.168 (n=1278)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` < 0.1146 (IC base=+0.053)

- **PATRÓN** `volumen_pendiente_norm` > `0.2486` → IC=+0.212 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2486 (IC base=+0.053)

- **PATRÓN** `volumen_spike_ratio` < `1.4786` → IC=+0.197 (n=440)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.4786 (IC base=+0.053)

- **PATRÓN** `volumen_spike_ratio` > `2.837` → IC=+0.172 (n=440)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.837 (IC base=+0.053)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.268 (n=768)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.053)

- **PATRÓN** `ibs_20min` < `0.0952` → IC=+0.186 (n=1213)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.0952 (IC base=+0.039)

- **PATRÓN** `dist_vwap_pct` > `0.7013` → IC=+0.223 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7013 (IC base=+0.039)

- **PATRÓN** `dist_vwap_pct` < `0.2092` → IC=+0.205 (n=745)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2092 (IC base=+0.039)

- **PATRÓN** `volumen_regimen` > `0.6258` → IC=+0.213 (n=762)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6258 (IC base=+0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.2499` → IC=+0.357 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2499 (IC base=+0.039)

- **PATRÓN** `volumen_spike_ratio` > `2.3783` → IC=+0.291 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3783 (IC base=+0.039)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.261 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 59.0 (IC base=+0.039)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2584` → IC=-0.150 (n=184)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2584
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=374)

- **FILTRO** `sigma_ewma_delta_pct` > `2.094` → IC=-0.168 (n=239)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.094
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=540)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.222` → IC=+0.191 (n=108)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 5.222 (IC base=-0.007)

- **PATRÓN** `volumen_pendiente_norm` > `0.2014` → IC=+0.382 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2014 (IC base=-0.007)

- **PATRÓN** `volumen_spike_ratio` > `2.5866` → IC=+0.241 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5866 (IC base=-0.007)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` > `0.8844` → IC=-0.146 (n=275)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8844
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=827)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `drift_60min` |x|≤ `0.0714` → IC=+0.217 (n=150)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0714 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.255 (n=161)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.294 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.02` → IC=+0.297 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.02 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` < `0.1438` → IC=+0.188 (n=344)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` < 0.1438 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.4176` → IC=+0.185 (n=52)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.4176 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` < `1.9958` → IC=+0.193 (n=161)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.9958 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `3.5166` → IC=+0.184 (n=166)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 3.5166 (IC base=+0.181)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.231 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `1910.4284` → IC=+0.207 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1910.4284 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.008` → IC=+0.351 (n=213)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.340)

- **PATRÓN** `drift_60min` |x|≤ `0.2308` → IC=+0.360 (n=162)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2308 (IC base=+0.340)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.386 (n=165)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.340)

- **PATRÓN** `ibs_20min` < `0.3388` → IC=+0.357 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3388 (IC base=+0.340)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.535` → IC=+0.346 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.535 (IC base=+0.340)

- **PATRÓN** `volumen_pendiente_norm` > `0.3474` → IC=+0.389 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3474 (IC base=+0.340)

- **PATRÓN** `volumen_spike_ratio` < `3.3374` → IC=+0.336 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.3374 (IC base=+0.340)

- **PATRÓN** `volumen_spike_ratio` > `1.9918` → IC=+0.346 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9918 (IC base=+0.340)

- **PATRÓN** `libro_liquidez` > `1894.0152` → IC=+0.367 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1894.0152 (IC base=+0.340)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.308 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 30.0 (IC base=+0.340)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.183 (n=102)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=365)

- **FILTRO** `dist_vwap_pct` < `0.7343` → IC=-0.211 (n=43)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.7343
  - _Potencial_: sin este filtro IC_bueno=+0.233 (n=28)

- **FILTRO** `volumen_regimen` > `1.0041` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.0041
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=54)

- **FILTRO** `dist_vwap_pct` < `0.0964` → IC=-0.136 (n=53)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0964
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

- **FILTRO** `volumen_regimen` > `0.8819` → IC=-0.231 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8819
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=49)

- **FILTRO** `volumen_regimen` < `0.6828` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.6828
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=49)

- **FILTRO** `volumen_pendiente_norm` < `0.0424` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.0424
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.162 (n=66)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=913)

- **PATRÓN** `dist_vwap_pct` > `0.7343` → IC=+0.233 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7343 (IC base=-0.076)

- **PATRÓN** `volumen_spike_ratio` < `1.4` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4 (IC base=-0.076)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7368` → IC=-0.124 (n=426)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7368
  - _Potencial_: sin este filtro IC_bueno=+0.213 (n=221)

- **FILTRO** `ibs_20min` > `0.75` → IC=-0.185 (n=217)

  - _Acción_: SKIP cuando `ibs_20min` > 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=677)

- **FILTRO** `dist_vwap_pct` > `0.1326` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1326
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=54)

- **FILTRO** `volumen_regimen` > `1.3339` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.3339
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=53)

- **FILTRO** `volumen_pendiente_norm` < `0.1028` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.1028
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=14)

- **FILTRO** `volumen_spike_ratio` < `2.1818` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 2.1818
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=12)

- **FILTRO** `ballena_activa_n` > `35.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `ballena_activa_n` > 35.0
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=8)

- **PATRÓN** `ibs_20min` > `0.8519` → IC=+0.264 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8519 (IC base=-0.009)

- **PATRÓN** `dist_vwap_pct` > `0.3259` → IC=+0.264 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3259 (IC base=-0.009)

- **PATRÓN** `volumen_regimen` < `0.8598` → IC=+0.188 (n=123)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.8598 (IC base=-0.009)

- **PATRÓN** `volumen_regimen` > `1.1463` → IC=+0.234 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1463 (IC base=-0.009)

- **PATRÓN** `volumen_pendiente_norm` > `0.2343` → IC=+0.269 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2343 (IC base=-0.009)

- **PATRÓN** `volumen_spike_ratio` < `1.4866` → IC=+0.183 (n=58)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.4866 (IC base=-0.009)

- **PATRÓN** `volumen_spike_ratio` > `2.0524` → IC=+0.175 (n=78)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.0524 (IC base=-0.009)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.234 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 50.0 (IC base=-0.009)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.227 (n=214)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.230 (n=213)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` > `0.9` → IC=+0.299 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` > `1.3817` → IC=+0.339 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.3817 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.142` → IC=+0.276 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.142 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` > `0.8384` → IC=+0.251 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8384 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` < `0.0799` → IC=+0.224 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0799 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.278` → IC=+0.276 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.278 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` < `1.4098` → IC=+0.260 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4098 (IC base=+0.216)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.234 (n=604)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `2455.4649` → IC=+0.230 (n=564)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2455.4649 (IC base=+0.216)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.277 (n=258)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.270)

- **PATRÓN** `drift_60min` |x|≤ `0.4891` → IC=+0.275 (n=509)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4891 (IC base=+0.270)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.280 (n=538)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.270)

- **PATRÓN** `ibs_20min` < `0.3675` → IC=+0.309 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3675 (IC base=+0.270)

- **PATRÓN** `dist_vwap_pct` < `0.8801` → IC=+0.275 (n=660)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8801 (IC base=+0.270)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.799` → IC=+0.324 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.799 (IC base=+0.270)

- **PATRÓN** `volumen_regimen` > `1.2602` → IC=+0.305 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2602 (IC base=+0.270)

- **PATRÓN** `volumen_pendiente_norm` > `0.2431` → IC=+0.371 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2431 (IC base=+0.270)

- **PATRÓN** `volumen_spike_ratio` > `2.1674` → IC=+0.300 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1674 (IC base=+0.270)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.190 (n=828)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0099 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.3351` → IC=+0.155 (n=2184)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.3351 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.182 (n=891)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 17.0 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.159 (n=943)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 6.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `0.8889` → IC=+0.258 (n=1654)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8889 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.7901` → IC=+0.247 (n=576)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7901 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.349` → IC=+0.246 (n=1045)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.349 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` > `0.6873` → IC=+0.174 (n=1537)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 0.6873 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.1012` → IC=+0.183 (n=887)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.1012 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `2.2855` → IC=+0.152 (n=1965)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.2855 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `1.8521` → IC=+0.150 (n=1488)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.8521 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.166 (n=2018)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `3191.121` → IC=+0.181 (n=1125)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 3191.121 (IC base=+0.154)

- **PATRÓN** `ballena_activa_n` < `121.0` → IC=+0.173 (n=1224)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 121.0 (IC base=+0.154)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.198 (n=1947)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0075 (IC base=+0.185)

- **PATRÓN** `drift_60min` |x|≤ `0.4145` → IC=+0.197 (n=2209)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.4145 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.213 (n=1115)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` < `0.4098` → IC=+0.237 (n=2209)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4098 (IC base=+0.185)

- **PATRÓN** `dist_vwap_pct` < `0.3554` → IC=+0.176 (n=1929)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.3554 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.745` → IC=+0.213 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.745 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` < `1.1737` → IC=+0.167 (n=1777)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1737 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` > `0.8565` → IC=+0.171 (n=1185)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 0.8565 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.2903` → IC=+0.240 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2903 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` < `1.5764` → IC=+0.180 (n=704)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.5764 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` > `2.6561` → IC=+0.212 (n=533)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6561 (IC base=+0.185)

- **PATRÓN** `ballena_activa_n` < `197.0` → IC=+0.182 (n=1168)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 197.0 (IC base=+0.185)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.208 (n=183)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.2664` → IC=+0.148 (n=404)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.2664 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.208 (n=152)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.306 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.063` → IC=+0.331 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.063 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.2093` → IC=+0.181 (n=67)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2093 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.5605` → IC=+0.125 (n=291)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` > 1.5605 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.167 (n=253)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.04 (IC base=+0.144)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.263 (n=175)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.262)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.280 (n=198)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.262)

- **PATRÓN** `drift_60min` |x|≤ `0.3311` → IC=+0.300 (n=198)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3311 (IC base=+0.262)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.280 (n=175)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 13.0 (IC base=+0.262)

- **PATRÓN** `ibs_20min` < `0.4057` → IC=+0.285 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4057 (IC base=+0.262)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.357` → IC=+0.288 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.357 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` < `1.8801` → IC=+0.304 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8801 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` > `2.8655` → IC=+0.330 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8655 (IC base=+0.262)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.333 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.262)

- **PATRÓN** `libro_liquidez` > `1973.46` → IC=+0.338 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1973.46 (IC base=+0.262)

- **PATRÓN** `ballena_activa_n` < `66.0` → IC=+0.275 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 66.0 (IC base=+0.262)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.230 (n=120)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.177)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.189 (n=117)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0072 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.0853` → IC=+0.183 (n=118)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.0853 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.204 (n=353)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` > `0.9974` → IC=+0.278 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9974 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` > `0.2069` → IC=+0.241 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2069 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.549` → IC=+0.239 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.549 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` < `1.2894` → IC=+0.181 (n=352)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 1.2894 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` > `0.8837` → IC=+0.199 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8837 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.2159` → IC=+0.268 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2159 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` < `1.3655` → IC=+0.227 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3655 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `12172.2264` → IC=+0.199 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12172.2264 (IC base=+0.177)

- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.202 (n=149)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0022 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.2896` → IC=+0.171 (n=445)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.2896 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.175 (n=404)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 7.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` < `0.4173` → IC=+0.187 (n=445)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.4173 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.1544` → IC=+0.171 (n=439)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.1544 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.3` → IC=+0.231 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.3 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.6405` → IC=+0.229 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6405 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.1712` → IC=+0.213 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1712 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.5404` → IC=+0.164 (n=337)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 2.5404 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `14307.4169` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 14307.4169 (IC base=+0.149)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `drift_60min` |x|≤ `0.1483` → IC=+0.164 (n=239)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1483 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.167 (n=142)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 16.0 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.213 (n=120)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.297 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.912` → IC=+0.294 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.912 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` < `0.2288` → IC=+0.143 (n=295)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` < 0.2288 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `1.9887` → IC=+0.199 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9887 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `3.6311` → IC=+0.142 (n=135)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 3.6311 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `1957.7806` → IC=+0.186 (n=119)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 1957.7806 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.293 (n=235)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0094 (IC base=+0.278)

- **PATRÓN** `drift_60min` |x|≤ `0.4646` → IC=+0.302 (n=235)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4646 (IC base=+0.278)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.325 (n=158)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.278)

- **PATRÓN** `ibs_20min` < `0.3077` → IC=+0.319 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3077 (IC base=+0.278)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.853` → IC=+0.312 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.853 (IC base=+0.278)

- **PATRÓN** `volumen_pendiente_norm` > `0.363` → IC=+0.426 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.363 (IC base=+0.278)

- **PATRÓN** `volumen_spike_ratio` > `2.0029` → IC=+0.274 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.0029 (IC base=+0.278)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.248 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 59.0 (IC base=+0.278)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0093` → IC=+0.218 (n=356)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0093 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.0955` → IC=+0.235 (n=119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0955 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.199 (n=363)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 6.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` > `0.4502` → IC=+0.239 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4502 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `1.0398` → IC=+0.242 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0398 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.391` → IC=+0.303 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.391 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` > `0.6366` → IC=+0.194 (n=354)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` > 0.6366 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.1005` → IC=+0.239 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1005 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` < `1.4363` → IC=+0.201 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4363 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `2.4571` → IC=+0.224 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4571 (IC base=+0.179)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.182 (n=404)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `8688.9164` → IC=+0.206 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8688.9164 (IC base=+0.179)

- **PATRÓN** `ballena_activa_n` < `156.0` → IC=+0.170 (n=195)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 156.0 (IC base=+0.179)

- **PATRÓN** `sigma_h` < `0.0025` → IC=+0.250 (n=142)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0025 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.3806` → IC=+0.170 (n=425)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.3806 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.182 (n=215)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 14.0 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.151 (n=164)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` < `0.343` → IC=+0.218 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.343 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.5253` → IC=+0.164 (n=498)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.5253 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.227` → IC=+0.207 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.227 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `1.1598` → IC=+0.163 (n=425)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.1598 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` > `0.6177` → IC=+0.158 (n=425)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.6177 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.1018` → IC=+0.167 (n=127)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.1018 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `1.8946` → IC=+0.192 (n=212)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.8946 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `10077.5355` → IC=+0.153 (n=142)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 10077.5355 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `196.0` → IC=+0.135 (n=209)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 196.0 (IC base=+0.150)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **FILTRO** `ibs_20min` > `0.4098` → IC=-0.193 (n=135)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4098
  - _Potencial_: sin este filtro IC_bueno=+0.226 (n=407)

- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.198 (n=223)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0103 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.132 (n=514)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.8538` → IC=+0.233 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8538 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `0.7969` → IC=+0.264 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7969 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.202` → IC=+0.288 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.202 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` > `0.6193` → IC=+0.136 (n=490)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 0.6193 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.2319` → IC=+0.130 (n=98)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` > 0.2319 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` > `1.5596` → IC=+0.131 (n=410)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 1.5596 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `3204.5735` → IC=+0.217 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3204.5735 (IC base=+0.117)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.181 (n=136)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0049 (IC base=+0.121)

- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.188 (n=136)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0098 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=142)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` < `0.4098` → IC=+0.226 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4098 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` < `0.2166` → IC=+0.136 (n=380)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.2166 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.682` → IC=+0.191 (n=79)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 6.682 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` > `0.8537` → IC=+0.163 (n=271)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.8537 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.2198` → IC=+0.184 (n=55)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2198 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` > `2.2636` → IC=+0.205 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2636 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `2065.7928` → IC=+0.174 (n=271)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2065.7928 (IC base=+0.121)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0231` → IC=+0.189 (n=239)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0231 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.1642` → IC=+0.184 (n=232)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.1642 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.199 (n=184)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.164)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.170 (n=237)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 7.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `0.9167` → IC=+0.265 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9167 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `1.6023` → IC=+0.246 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.6023 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.118` → IC=+0.245 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.118 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` > `0.8248` → IC=+0.191 (n=351)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` > 0.8248 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.2353` → IC=+0.242 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2353 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` < `2.1481` → IC=+0.176 (n=430)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 2.1481 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.173 (n=563)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.01 (IC base=+0.164)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.272 (n=169)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.6724` → IC=+0.234 (n=502)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6724 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.224 (n=237)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.253 (n=245)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` < `0.3738` → IC=+0.258 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3738 (IC base=+0.221)

- **PATRÓN** `dist_vwap_pct` < `0.4587` → IC=+0.230 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4587 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.175` → IC=+0.284 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.175 (IC base=+0.221)

- **PATRÓN** `volumen_regimen` > `0.6394` → IC=+0.236 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6394 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.2811` → IC=+0.339 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2811 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `2.7294` → IC=+0.272 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7294 (IC base=+0.221)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `hora_utc` > `16.0` → IC=+0.187 (n=215)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 16.0 (IC base=+0.085)

- **PATRÓN** `ibs_20min` > `0.6275` → IC=+0.158 (n=390)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.6275 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` > `0.7873` → IC=+0.259 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7873 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.235` → IC=+0.194 (n=122)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 8.235 (IC base=+0.085)

- **PATRÓN** `volumen_pendiente_norm` > `0.1727` → IC=+0.175 (n=115)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1727 (IC base=+0.085)

- **PATRÓN** `libro_liquidez` > `2879.0602` → IC=+0.131 (n=291)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2879.0602 (IC base=+0.085)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.172 (n=135)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0036 (IC base=+0.077)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.146 (n=145)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 16.0 (IC base=+0.077)

- **PATRÓN** `ibs_20min` < `0.6327` → IC=+0.127 (n=400)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` < 0.6327 (IC base=+0.077)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.199` → IC=+0.197 (n=130)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 5.199 (IC base=+0.077)

- **PATRÓN** `volumen_regimen` < `0.6508` → IC=+0.147 (n=120)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.6508 (IC base=+0.077)

- **PATRÓN** `volumen_spike_ratio` < `1.8672` → IC=+0.136 (n=229)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.8672 (IC base=+0.077)

- **PATRÓN** `libro_liquidez` > `9264.2772` → IC=+0.139 (n=181)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 9264.2772 (IC base=+0.077)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.214 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=85)

- **FILTRO** `ibs_20min` < `0.4225` → IC=-0.224 (n=27)

  - _Acción_: SKIP cuando `ibs_20min` < 0.4225
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=84)

- **FILTRO** `libro_liquidez` < `6436.909` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `libro_liquidez` < 6436.909
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=84)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.210 (n=29)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.031)

- **PATRÓN** `ibs_20min` > `0.9306` → IC=+0.225 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9306 (IC base=+0.031)

- **PATRÓN** `dist_vwap_pct` > `0.7767` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.7767 (IC base=+0.031)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.351` → IC=+0.150 (n=38)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 4.351 (IC base=+0.031)

- **PATRÓN** `libro_liquidez` > `11800.2375` → IC=+0.138 (n=56)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 11800.2375 (IC base=+0.031)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.222 (n=70)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.156)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.203 (n=72)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.3512` → IC=+0.188 (n=158)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.3512 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.173 (n=53)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.156)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.190 (n=56)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 4.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` < `0.4848` → IC=+0.202 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4848 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `0.4768` → IC=+0.158 (n=36)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.4768 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` < `0.3005` → IC=+0.169 (n=158)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.3005 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.323` → IC=+0.318 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.323 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` < `1.2044` → IC=+0.181 (n=158)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 1.2044 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` > `0.0873` → IC=+0.333 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0873 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `1.7117` → IC=+0.213 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7117 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `13545.8692` → IC=+0.164 (n=105)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 13545.8692 (IC base=+0.156)

- **PATRÓN** `ballena_activa_n` < `139.0` → IC=+0.172 (n=56)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 139.0 (IC base=+0.156)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **FILTRO** `drift_60min` |x|> `0.2707` → IC=-0.145 (n=29)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2707
  - _Potencial_: sin este filtro IC_bueno=+0.172 (n=59)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.293 (n=80)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.281)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.309 (n=61)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.281)

- **PATRÓN** `drift_60min` |x|≤ `0.2275` → IC=+0.278 (n=61)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2275 (IC base=+0.281)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.343 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.281)

- **PATRÓN** `ibs_20min` > `0.6714` → IC=+0.298 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6714 (IC base=+0.281)

- **PATRÓN** `dist_vwap_pct` > `0.1466` → IC=+0.333 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1466 (IC base=+0.281)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.561` → IC=+0.380 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.561 (IC base=+0.281)

- **PATRÓN** `volumen_regimen` < `0.6873` → IC=+0.381 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6873 (IC base=+0.281)

- **PATRÓN** `volumen_pendiente_norm` > `0.184` → IC=+0.392 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.184 (IC base=+0.281)

- **PATRÓN** `volumen_spike_ratio` < `2.3129` → IC=+0.295 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3129 (IC base=+0.281)

- **PATRÓN** `volumen_spike_ratio` > `1.5464` → IC=+0.300 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5464 (IC base=+0.281)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.380 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.067)

- **PATRÓN** `drift_60min` |x|≤ `0.2707` → IC=+0.172 (n=59)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.2707 (IC base=+0.067)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.244 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.067)

- **PATRÓN** `ibs_20min` < `0.5743` → IC=+0.138 (n=67)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` < 0.5743 (IC base=+0.067)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.996` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 5.996 (IC base=+0.067)

- **PATRÓN** `volumen_regimen` < `0.7049` → IC=+0.281 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7049 (IC base=+0.067)

- **PATRÓN** `libro_liquidez` > `9388.7076` → IC=+0.292 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9388.7076 (IC base=+0.067)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` < `0.619` → IC=-0.157 (n=65)

  - _Acción_: SKIP cuando `ibs_20min` < 0.619
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=134)

- **FILTRO** `hora_utc` < `4.0` → IC=-0.190 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=84)

- **FILTRO** `ibs_20min` > `0.6154` → IC=-0.259 (n=27)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6154
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=84)

- **FILTRO** `dist_vwap_pct` > `0.19` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.19
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=91)

- **FILTRO** `volumen_spike_ratio` > `3.1626` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 3.1626
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=67)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.155 (n=56)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.022)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.190 (n=69)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 1.0 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` > `0.4838` → IC=+0.179 (n=26)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.4838 (IC base=+0.022)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.006` → IC=+0.214 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.085)

- **PATRÓN** `ibs_20min` > `0.6522` → IC=+0.143 (n=54)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.6522 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` > `0.2226` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.2226 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.99` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.99 (IC base=+0.085)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=54)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.085)

- **PATRÓN** `ibs_20min` < `0.0773` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0773 (IC base=+0.029)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.008` → IC=+0.201 (n=1312)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.008 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=1104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.9432` → IC=+0.295 (n=1308)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9432 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `1.0669` → IC=+0.249 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0669 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.355` → IC=+0.246 (n=1205)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.355 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `0.8788` → IC=+0.144 (n=1360)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.8788 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` > `1.0795` → IC=+0.157 (n=925)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 1.0795 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.1657` → IC=+0.189 (n=737)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.1657 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.8689` → IC=+0.160 (n=1711)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.8689 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=2345)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `2500.5916` → IC=+0.175 (n=1923)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2500.5916 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.194 (n=1011)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 71.0 (IC base=+0.148)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.223 (n=1724)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.195)

- **PATRÓN** `drift_60min` |x|≤ `0.4679` → IC=+0.205 (n=2586)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4679 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.202 (n=939)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.207 (n=958)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` < `0.5593` → IC=+0.250 (n=2586)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5593 (IC base=+0.195)

- **PATRÓN** `dist_vwap_pct` < `0.7104` → IC=+0.185 (n=2099)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 0.7104 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.346` → IC=+0.220 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.346 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.639` → IC=+0.198 (n=2431)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` < 2.639 (IC base=+0.195)

- **PATRÓN** `volumen_regimen` < `0.6243` → IC=+0.188 (n=648)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.6243 (IC base=+0.195)

- **PATRÓN** `volumen_regimen` > `1.2004` → IC=+0.187 (n=649)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 1.2004 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.2826` → IC=+0.272 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2826 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `2.286` → IC=+0.217 (n=856)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.286 (IC base=+0.195)

- **PATRÓN** `ballena_activa_n` < `180.0` → IC=+0.174 (n=1460)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 180.0 (IC base=+0.195)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` > `0.007` → IC=+0.209 (n=211)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.143 (n=471)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 6.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.167 (n=319)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 11.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.9474` → IC=+0.293 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9474 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.327` → IC=+0.298 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.327 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.2163` → IC=+0.214 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2163 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `1.9158` → IC=+0.140 (n=256)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.9158 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.185 (n=258)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.04 (IC base=+0.141)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.308 (n=191)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.274)

- **PATRÓN** `drift_60min` |x|≤ `0.1054` → IC=+0.328 (n=126)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1054 (IC base=+0.274)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.280 (n=266)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.274)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.282 (n=264)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.274)

- **PATRÓN** `ibs_20min` < `0.5833` → IC=+0.326 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5833 (IC base=+0.274)

- **PATRÓN** `volumen_pendiente_norm` > `0.2944` → IC=+0.333 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2944 (IC base=+0.274)

- **PATRÓN** `volumen_spike_ratio` > `2.7667` → IC=+0.328 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7667 (IC base=+0.274)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.307 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.274)

- **PATRÓN** `libro_liquidez` > `1986.7396` → IC=+0.325 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1986.7396 (IC base=+0.274)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.262 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 71.0 (IC base=+0.274)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.184 (n=153)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0028 (IC base=+0.152)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.190 (n=153)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0069 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.172 (n=461)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 6.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` > `0.3266` → IC=+0.209 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3266 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.2496` → IC=+0.243 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2496 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.619` → IC=+0.198 (n=124)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 9.619 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `1.2673` → IC=+0.157 (n=459)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.2673 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` > `1.099` → IC=+0.176 (n=208)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 1.099 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.2053` → IC=+0.227 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2053 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `2.109` → IC=+0.180 (n=361)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 2.109 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `1.3655` → IC=+0.180 (n=410)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.3655 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `11800.2375` → IC=+0.175 (n=306)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 11800.2375 (IC base=+0.152)

- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.196 (n=146)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0022 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.2658` → IC=+0.185 (n=382)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.2658 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.174 (n=403)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 7.0 (IC base=+0.169)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.181 (n=434)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 17.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` < `0.3782` → IC=+0.216 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3782 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` < `0.7428` → IC=+0.177 (n=481)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.7428 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.621` → IC=+0.225 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.621 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `0.6257` → IC=+0.248 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6257 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.1489` → IC=+0.288 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1489 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `1.7452` → IC=+0.202 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7452 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `1.5054` → IC=+0.191 (n=302)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 1.5054 (IC base=+0.169)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.169 (n=560)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.01 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `12107.4018` → IC=+0.173 (n=197)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 12107.4018 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `310.0` → IC=+0.183 (n=80)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 310.0 (IC base=+0.169)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `hora_utc` < `8.0` → IC=+0.240 (n=179)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.7044` → IC=+0.264 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7044 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.113` → IC=+0.340 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.113 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` < `0.2259` → IC=+0.182 (n=313)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` < 0.2259 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` < `2.0094` → IC=+0.203 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0094 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `3.6777` → IC=+0.176 (n=140)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 3.6777 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.210 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `1854.121` → IC=+0.203 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1854.121 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.320 (n=159)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.261)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.265 (n=253)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.261)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.298 (n=122)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.261)

- **PATRÓN** `ibs_20min` < `0.5703` → IC=+0.326 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5703 (IC base=+0.261)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.065` → IC=+0.305 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.065 (IC base=+0.261)

- **PATRÓN** `volumen_pendiente_norm` > `0.1516` → IC=+0.284 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1516 (IC base=+0.261)

- **PATRÓN** `volumen_spike_ratio` < `1.7663` → IC=+0.281 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7663 (IC base=+0.261)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.278 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.261)

- **PATRÓN** `ballena_activa_n` < `62.0` → IC=+0.203 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 62.0 (IC base=+0.261)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0089` → IC=+0.156 (n=460)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0089 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.1448` → IC=+0.144 (n=203)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.1448 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.167 (n=415)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 8.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` > `0.345` → IC=+0.201 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.345 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `0.3919` → IC=+0.193 (n=190)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.3919 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.485` → IC=+0.197 (n=219)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 4.485 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `0.6219` → IC=+0.173 (n=154)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.6219 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` > `1.1936` → IC=+0.173 (n=154)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 1.1936 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.2691` → IC=+0.284 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2691 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `2.4121` → IC=+0.236 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4121 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `5254.2901` → IC=+0.228 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5254.2901 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.177 (n=224)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 166.0 (IC base=+0.142)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.210 (n=129)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.158)

- **PATRÓN** `drift_60min` |x|≤ `0.5115` → IC=+0.172 (n=382)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.5115 (IC base=+0.158)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.175 (n=340)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 14.0 (IC base=+0.158)

- **PATRÓN** `ibs_20min` < `0.0817` → IC=+0.247 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0817 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` > `0.1635` → IC=+0.163 (n=194)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.1635 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` < `0.6545` → IC=+0.181 (n=405)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.6545 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.454` → IC=+0.231 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.454 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` < `0.597` → IC=+0.177 (n=128)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.597 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` > `1.1367` → IC=+0.200 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1367 (IC base=+0.158)

- **PATRÓN** `volumen_pendiente_norm` > `0.2334` → IC=+0.330 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2334 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` < `1.8125` → IC=+0.185 (n=217)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.8125 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` > `2.4643` → IC=+0.191 (n=108)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.4643 (IC base=+0.158)

- **PATRÓN** `libro_liquidez` > `9483.0008` → IC=+0.210 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9483.0008 (IC base=+0.158)

- **PATRÓN** `ballena_activa_n` < `138.0` → IC=+0.235 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 138.0 (IC base=+0.158)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.165 (n=234)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0109 (IC base=+0.098)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.161 (n=178)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 18.0 (IC base=+0.098)

- **PATRÓN** `ibs_20min` > `0.9091` → IC=+0.309 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9091 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `0.7721` → IC=+0.260 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7721 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.428` → IC=+0.229 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.428 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `2942.126` → IC=+0.282 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2942.126 (IC base=+0.098)

- **PATRÓN** `ballena_activa_n` < `67.0` → IC=+0.173 (n=289)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 67.0 (IC base=+0.098)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.179 (n=207)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.006 (IC base=+0.117)

- **PATRÓN** `drift_60min` |x|≤ `0.2678` → IC=+0.138 (n=313)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.2678 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.181 (n=214)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 15.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.5833` → IC=+0.199 (n=469)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.5833 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` < `0.454` → IC=+0.138 (n=426)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.454 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.062` → IC=+0.138 (n=459)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 3.062 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.7113` → IC=+0.146 (n=207)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.7113 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.0724` → IC=+0.159 (n=130)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.0724 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `2.0886` → IC=+0.146 (n=283)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.0886 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` > `1.5376` → IC=+0.147 (n=287)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.5376 (IC base=+0.117)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.122 (n=488)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2581.4636` → IC=+0.165 (n=213)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2581.4636 (IC base=+0.117)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0267` → IC=+0.217 (n=203)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0267 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.195 (n=231)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 17.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` > `0.9643` → IC=+0.299 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9643 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `1.4377` → IC=+0.287 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.4377 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.967` → IC=+0.263 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.967 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` < `0.6105` → IC=+0.178 (n=203)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.6105 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` > `1.0357` → IC=+0.203 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0357 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.1708` → IC=+0.246 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1708 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `1.8195` → IC=+0.187 (n=372)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 1.8195 (IC base=+0.172)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.187 (n=646)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.01 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `3098.1206` → IC=+0.188 (n=203)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 3098.1206 (IC base=+0.172)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.305 (n=224)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.4796` → IC=+0.230 (n=579)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4796 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.223 (n=607)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` < `0.49` → IC=+0.277 (n=658)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.49 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` < `1.2129` → IC=+0.224 (n=769)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 1.2129 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.527` → IC=+0.274 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.527 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.03` → IC=+0.216 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.03 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` > `1.2349` → IC=+0.251 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2349 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.2826` → IC=+0.318 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2826 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `2.5884` → IC=+0.236 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5884 (IC base=+0.215)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.180 (n=370)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 37.0 (IC base=+0.215)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.153 (n=974)

- **PATRÓN** `sigma_h` < `0.0099` → IC=+0.131 (n=442)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0099 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.160 (n=186)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.114)

- **PATRÓN** `ibs_20min` > `0.9382` → IC=+0.153 (n=168)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.9382 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` > `1.367` → IC=+0.196 (n=123)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 1.367 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.261` → IC=+0.183 (n=80)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 10.261 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` < `0.6122` → IC=+0.145 (n=139)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.6122 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` > `1.0851` → IC=+0.144 (n=189)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.0851 (IC base=+0.114)

- **PATRÓN** `volumen_pendiente_norm` > `0.2719` → IC=+0.194 (n=70)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2719 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` < `1.4017` → IC=+0.151 (n=164)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4017 (IC base=+0.114)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.126 (n=455)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `7550.3789` → IC=+0.150 (n=335)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 7550.3789 (IC base=+0.114)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.196 (n=248)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0035 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.3507` → IC=+0.165 (n=654)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.3507 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.169 (n=267)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.194 (n=295)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 4.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.6273` → IC=+0.157 (n=653)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.6273 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.0855` → IC=+0.157 (n=742)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.0855 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.1705` → IC=+0.165 (n=314)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.1705 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.3612` → IC=+0.142 (n=730)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.3612 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.056` → IC=+0.153 (n=332)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 4.056 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.009` → IC=+0.151 (n=743)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 6.009 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `1.2157` → IC=+0.160 (n=727)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2157 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` < `0.0935` → IC=+0.150 (n=664)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` < 0.0935 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.0712` → IC=+0.158 (n=355)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.0712 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.4869` → IC=+0.164 (n=734)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 2.4869 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.5136` → IC=+0.150 (n=656)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.5136 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=974)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `10656.5501` → IC=+0.162 (n=495)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 10656.5501 (IC base=+0.147)

### GBM_LATE_5M#BTC#5min
- **FILTRO** `hora_utc` < `12.0` → IC=-0.156 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=+0.156 (n=62)

- **FILTRO** `sigma_ewma_delta_pct` > `3.972` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 3.972
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=74)

- **FILTRO** `volumen_pendiente_norm` > `0.0971` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0971
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=76)

- **FILTRO** `libro_liquidez` < `12272.8392` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `libro_liquidez` < 12272.8392
  - _Potencial_: sin este filtro IC_bueno=+0.134 (n=69)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.156 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 12.0 (IC base=+0.053)

- **PATRÓN** `dist_vwap_pct` > `0.572` → IC=+0.141 (n=51)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.572 (IC base=+0.053)

- **PATRÓN** `volumen_regimen` > `0.9327` → IC=+0.176 (n=32)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.9327 (IC base=+0.053)

- **PATRÓN** `libro_liquidez` > `12272.8392` → IC=+0.134 (n=69)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 12272.8392 (IC base=+0.053)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.166 (n=420)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0063 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.3507` → IC=+0.154 (n=420)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.3507 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.194 (n=158)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.225 (n=140)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.7523` → IC=+0.154 (n=420)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.7523 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.1787` → IC=+0.175 (n=152)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.1787 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.22` → IC=+0.164 (n=423)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` < 6.22 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `1.1834` → IC=+0.159 (n=420)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.1834 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` > `0.6188` → IC=+0.149 (n=420)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.6188 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.1496` → IC=+0.192 (n=128)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.1496 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.5395` → IC=+0.162 (n=418)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.5395 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.7842` → IC=+0.150 (n=278)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.7842 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `11854.8179` → IC=+0.152 (n=375)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 11854.8179 (IC base=+0.147)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `ibs_20min` > `0.8876` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.8876 (IC base=+0.054)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0096` → IC=+0.184 (n=226)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0096 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.4407` → IC=+0.172 (n=199)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.4407 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.223 (n=81)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` < `0.2929` → IC=+0.157 (n=100)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.2929 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.7919` → IC=+0.192 (n=102)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.7919 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `1.1055` → IC=+0.212 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1055 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.4091` → IC=+0.167 (n=190)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.4091 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.264` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 11.264 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.861` → IC=+0.152 (n=225)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 6.861 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.6468` → IC=+0.192 (n=76)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.6468 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.1754` → IC=+0.176 (n=69)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1754 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `1.412` → IC=+0.210 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.412 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `8856.6618` → IC=+0.190 (n=201)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 8856.6618 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0088` → IC=+0.164 (n=218)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0088 (IC base=+0.147)

- **PATRÓN** `sigma_h` > `0.0061` → IC=+0.167 (n=145)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0061 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.4941` → IC=+0.182 (n=218)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.4941 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.153 (n=73)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 18.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.173 (n=148)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 9.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.0864` → IC=+0.186 (n=218)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.0864 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.1925` → IC=+0.156 (n=91)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1925 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.3474` → IC=+0.159 (n=212)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.3474 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.157` → IC=+0.185 (n=109)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 3.157 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `1.1886` → IC=+0.182 (n=218)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 1.1886 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` < `0.1304` → IC=+0.167 (n=223)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` < 0.1304 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.1612` → IC=+0.200 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1612 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.4479` → IC=+0.174 (n=213)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.4479 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `10298.1112` → IC=+0.180 (n=73)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 10298.1112 (IC base=+0.147)

### GBM_LATE_5M#SOL#5min
- **FILTRO** `libro_liquidez` < `2854.2595` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_liquidez` < 2854.2595
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=63)

- **FILTRO** `sigma_h` < `0.011` → IC=-0.196 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.011
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=21)

- **FILTRO** `sigma_ewma_delta_pct` < `3.941` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 3.941
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=25)

### GBM_LATE_60M
- **FILTRO** `ibs_20min` < `0.649` → IC=-0.202 (n=45)

  - _Acción_: SKIP cuando `ibs_20min` < 0.649
  - _Potencial_: sin este filtro IC_bueno=+0.203 (n=136)

- **FILTRO** `sigma_h` > `0.0111` → IC=-0.282 (n=53)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0111
  - _Potencial_: sin este filtro IC_bueno=-0.142 (n=160)

- **FILTRO** `ibs_20min` > `0.1926` → IC=-0.194 (n=83)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1926
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=28)

- **FILTRO** `dist_vwap_pct` > `0.1067` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1067
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=54)

- **FILTRO** `volumen_regimen` < `0.6601` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.6601
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=84)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.182 (n=152)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0054 (IC base=+0.061)

- **PATRÓN** `ibs_20min` > `0.649` → IC=+0.203 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.649 (IC base=+0.061)

- **PATRÓN** `dist_vwap_pct` > `0.1249` → IC=+0.149 (n=72)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.1249 (IC base=+0.061)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.41` → IC=+0.227 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.41 (IC base=+0.061)

- **PATRÓN** `volumen_pendiente_norm` < `0.0725` → IC=+0.233 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0725 (IC base=+0.061)

- **PATRÓN** `volumen_spike_ratio` > `1.4971` → IC=+0.278 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4971 (IC base=+0.061)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.145 (n=122)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.02 (IC base=+0.061)

- **PATRÓN** `libro_liquidez` > `1977.9398` → IC=+0.137 (n=100)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 1977.9398 (IC base=+0.061)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.7788` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7788
  - _Potencial_: sin este filtro IC_bueno=+0.202 (n=45)

- **FILTRO** `hora_utc` > `3.0` → IC=-0.188 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=24)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.333 (n=28)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.064)

- **PATRÓN** `ibs_20min` > `0.7788` → IC=+0.202 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7788 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` > `0.1487` → IC=+0.177 (n=29)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.1487 (IC base=+0.064)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.414` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 16.414 (IC base=+0.064)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0068` → IC=-0.333 (n=22)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=-0.144 (n=43)

- **FILTRO** `hora_utc` > `9.0` → IC=-0.318 (n=31)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=34)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.171 (n=80)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0059 (IC base=+0.107)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.123 (n=83)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 7.0 (IC base=+0.107)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.350 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.107)

- **PATRÓN** `dist_vwap_pct` < `0.2422` → IC=+0.224 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2422 (IC base=+0.107)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.06` → IC=+0.312 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.06 (IC base=+0.107)

- **PATRÓN** `volumen_regimen` < `0.6214` → IC=+0.224 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6214 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2519.6873` → IC=+0.241 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2519.6873 (IC base=+0.107)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.0165` → IC=-0.309 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0165
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=59)

- **FILTRO** `ibs_20min` > `0.4286` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4286
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=19)

### GBM_LATE_60M_FADE
- **FILTRO** `drift_60min` |x|> `0.1243` → IC=-0.382 (n=32)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1243
  - _Potencial_: sin este filtro IC_bueno=-0.238 (n=63)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.462 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.233 (n=73)

- **FILTRO** `dist_vwap_pct` < `0.1009` → IC=-0.354 (n=53)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1009
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=45)

- **FILTRO** `dist_vwap_pct` > `0.3507` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3507
  - _Potencial_: sin este filtro IC_bueno=-0.281 (n=80)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `ibs_20min` < `0.6047` → IC=-0.259 (n=27)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6047
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **FILTRO** `sigma_h` < `0.0019` → IC=-0.318 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0019
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=21)

- **FILTRO** `dist_vwap_pct` < `0.0931` → IC=-0.362 (n=27)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0931
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=14)

- **FILTRO** `sigma_ewma_delta_pct` > `4.524` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.524
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=26)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.6354` → IC=-0.462 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6354
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=18)

- **FILTRO** `ibs_20min` > `0.8144` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8144
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=17)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `sigma_h` < `0.0064` → IC=-0.262 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0064
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

- **FILTRO** `ibs_20min` < `0.5833` → IC=-0.309 (n=19)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5833
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

- **FILTRO** `sigma_h` < `0.0065` → IC=-0.382 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0065
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **FILTRO** `dist_vwap_pct` < `0.3782` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.3782
  - _Potencial_: sin este filtro IC_bueno=-0.300 (n=8)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.441 (n=15)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` < `0.5842` → IC=-0.245 (n=45)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5842
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=138)

- **FILTRO** `dist_vwap_pct` > `0.5824` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.5824
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=136)

- **PATRÓN** `ibs_20min` > `0.5842` → IC=+0.143 (n=138)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.5842 (IC base=+0.046)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.149 (n=55)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 15.0 (IC base=+0.023)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `hora_utc` > `6.0` → IC=-0.125 (n=38)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=20)

- **FILTRO** `ibs_20min` < `0.3927` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3927
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=39)

- **PATRÓN** `ibs_20min` > `0.7184` → IC=+0.177 (n=29)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.7184 (IC base=-0.067)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.214 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.084)

- **PATRÓN** `ibs_20min` < `0.3803` → IC=+0.144 (n=57)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.3803 (IC base=+0.084)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.328` → IC=+0.134 (n=39)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 3.328 (IC base=+0.084)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.321 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0022 (IC base=+0.100)

- **PATRÓN** `drift_60min` |x|≤ `0.1478` → IC=+0.147 (n=32)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.1478 (IC base=+0.100)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.100)

- **PATRÓN** `ibs_20min` > `0.8029` → IC=+0.243 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8029 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.517` → IC=+0.167 (n=31)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 6.517 (IC base=+0.100)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.219 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.100)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.143 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=14)

- **FILTRO** `ibs_20min` > `0.0435` → IC=-0.145 (n=29)

  - _Acción_: SKIP cuando `ibs_20min` > 0.0435
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=11)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.227 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.095)

- **PATRÓN** `drift_60min` |x|≤ `0.1849` → IC=+0.159 (n=39)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1849 (IC base=+0.095)

- **PATRÓN** `ibs_20min` < `0.7333` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7333 (IC base=+0.095)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.256 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.095)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.160 (n=45)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.03 (IC base=+0.095)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.130 (n=117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 6.0 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `2576.372` → IC=+0.199 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2576.372 (IC base=+0.105)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.147 (n=131)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 18.0 (IC base=+0.128)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.140 (n=48)

  - _Acción_: Kelly boost +0.70€ cuando `py_entrada` < 0.495 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `2478.2261` → IC=+0.161 (n=122)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2478.2261 (IC base=+0.128)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.130 (n=117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 6.0 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `2576.372` → IC=+0.199 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2576.372 (IC base=+0.105)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.147 (n=131)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 18.0 (IC base=+0.128)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.140 (n=48)

  - _Acción_: Kelly boost +0.70€ cuando `py_entrada` < 0.495 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `2478.2261` → IC=+0.161 (n=122)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2478.2261 (IC base=+0.128)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `9.0` → IC=-0.185 (n=71)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=43)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=98)

- **FILTRO** `libro_liquidez` < `2110.4161` → IC=-0.367 (n=28)

  - _Acción_: SKIP cuando `libro_liquidez` < 2110.4161
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=86)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=82)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `11321.3584` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `libro_liquidez` < 11321.3584
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=16)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.136 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

### LIQUIDACIONES_15M#XRP#15min
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
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=457)

- **FILTRO** `hora_utc` < `7.0` → IC=-0.142 (n=121)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=421)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=88)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9427` → IC=-0.311 (n=35)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9427
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=74)

- **FILTRO** `ballena_activa_n` > `558.0` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `ballena_activa_n` > 558.0
  - _Potencial_: sin este filtro IC_bueno=-0.212 (n=57)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_usd_total` < `37956.41` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `liq_usd_total` < 37956.41
  - _Potencial_: sin este filtro IC_bueno=+0.158 (n=36)

- **PATRÓN** `liq_usd_total` > `102277.19` → IC=+0.204 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 102277.19 (IC base=+0.013)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `liq_imbalance_60min` |x|≤ `0.8738` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.8738
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=48)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.155 (n=27)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=36)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=46)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=136)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.318 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **PATRÓN** `liq_usd_total` > `10618.69` → IC=+0.148 (n=52)

  - _Acción_: Kelly boost +0.74€ cuando `liq_usd_total` > 10618.69 (IC base=+0.058)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.122 (n=117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 8.0 (IC base=+0.058)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `liq_usd_total` < `24810.11` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `liq_usd_total` < 24810.11
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

### LIQUIDACIONES_5M#XRP#5min
- **FILTRO** `liq_usd_total` < `5231.58` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `liq_usd_total` < 5231.58
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=19)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=21)

### LIQUIDACIONES_60M
- **FILTRO** `py_entrada` > `0.56` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `py_entrada` > 0.56
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=90)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.128 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=55)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=78)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=26)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=25)

### MOMENTUM_IBS_15M#BNB#15min
- **FILTRO** `libro_liquidez` < `2179.6408` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `libro_liquidez` < 2179.6408
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=126)

### MOMENTUM_IBS_15M#DOGE#15min
- **FILTRO** `ibs_20min` > `0.955` → IC=-0.196 (n=90)

  - _Acción_: SKIP cuando `ibs_20min` > 0.955
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=272)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=424)

### MOMENTUM_IBS_15M#SOL#15min
- **FILTRO** `drift_20min_pct` |x|> `0.1837` → IC=-0.130 (n=98)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1837
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=193)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.46` → IC=-0.168 (n=818)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=2555)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.210 (n=796)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=2567)

- **FILTRO** `ibs_20min` > `0.2725` → IC=-0.175 (n=840)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2725
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=2523)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.238 (n=120)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=370)

- **FILTRO** `ibs_20min` < `0.7294` → IC=-0.185 (n=122)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7294
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=368)

- **FILTRO** `ibs_20min` > `0.2721` → IC=-0.136 (n=196)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2721
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=381)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.225 (n=136)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=426)

- **FILTRO** `ballena_activa_n` > `78.0` → IC=-0.162 (n=140)

  - _Acción_: SKIP cuando `ballena_activa_n` > 78.0
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=422)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.133 (n=115)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=394)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.179 (n=219)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=290)

- **FILTRO** `ibs_20min` < `0.7273` → IC=-0.195 (n=126)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7273
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=383)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.198 (n=190)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=374)

- **FILTRO** `ibs_20min` > `0.7531` → IC=-0.204 (n=140)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7531
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=424)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` > `0.52` → IC=-0.181 (n=139)

  - _Acción_: SKIP cuando `py_entrada` > 0.52
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=457)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.158 (n=144)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=452)

### MOMENTUM_IBS_15M_BALLENA#SOL#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.216 (n=125)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=403)

- **FILTRO** `drift_20min_pct` |x|> `0.2833` → IC=-0.146 (n=179)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.2833
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=349)

- **FILTRO** `ibs_20min` > `0.2778` → IC=-0.167 (n=130)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2778
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=398)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.151 (n=127)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=401)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.217 (n=136)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=429)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=550)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.278 (n=133)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=403)

- **FILTRO** `ibs_20min` > `0.278` → IC=-0.226 (n=133)

  - _Acción_: SKIP cuando `ibs_20min` > 0.278
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=403)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `hora_utc` < `16.0` → IC=-0.300 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=126)

- **FILTRO** `hora_utc` > `19.0` → IC=-0.206 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=127)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=375)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=381)

### MOMENTUM_IBS_15M_FADE#BNB#15min
- **FILTRO** `libro_liquidez` < `2063.3848` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 2063.3848
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=55)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `ibs_20min` < `1.0` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `ibs_20min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=19)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `hora_utc` < `19.0` → IC=-0.300 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=13)

- **FILTRO** `drift_20min_pct` |x|> `0.0299` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.0299
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **FILTRO** `ibs_20min` < `0.0752` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `ibs_20min` < 0.0752
  - _Potencial_: sin este filtro IC_bueno=-0.222 (n=16)

- **FILTRO** `libro_liquidez` < `15251.0076` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `libro_liquidez` < 15251.0076
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=11)

- **FILTRO** `drift_20min_pct` |x|> `0.1906` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1906
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=58)

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

- **FILTRO** `drift_7min_pct` |x|> `0.0725` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.0725
  - _Potencial_: sin este filtro IC_bueno=+0.133 (n=28)

- **PATRÓN** `drift_7min_pct` |x|≤ `0.0331` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_7min_pct` |x|≤ 0.0331 (IC base=-0.026)

### MOMENTUM_IBS_5M#BTC#5min
- **FILTRO** `hora_utc` > `18.0` → IC=-0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 18.0
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=88)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.143 (n=40)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 17.0 (IC base=+0.033)

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
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=630)

### MOMENTUM_IBS_5M_BALLENA
- **FILTRO** `hora_utc` < `8.0` → IC=-0.143 (n=2451)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=5924)

- **FILTRO** `py_entrada` < `0.36` → IC=-0.282 (n=2021)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=6354)

- **FILTRO** `ibs_7min` < `0.7333` → IC=-0.232 (n=2087)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7333
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=6288)

- **FILTRO** `ballena_activa_n` > `19.0` → IC=-0.172 (n=2841)

  - _Acción_: SKIP cuando `ballena_activa_n` > 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=5534)

- **FILTRO** `py_entrada` > `0.69` → IC=-0.229 (n=2355)

  - _Acción_: SKIP cuando `py_entrada` > 0.69
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=7820)

- **FILTRO** `ibs_7min` > `0.72` → IC=-0.174 (n=2542)

  - _Acción_: SKIP cuando `ibs_7min` > 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=7633)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.330 (n=275)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=853)

- **FILTRO** `ibs_7min` < `0.9787` → IC=-0.201 (n=744)

  - _Acción_: SKIP cuando `ibs_7min` < 0.9787
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=384)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.255 (n=280)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=848)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.229 (n=411)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=1332)

- **FILTRO** `drift_7min_pct` |x|> `0.1381` → IC=-0.151 (n=592)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1381
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=1151)

- **FILTRO** `ibs_7min` > `0.8406` → IC=-0.186 (n=435)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8406
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=1308)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.155 (n=355)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=1286)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.254 (n=384)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=1257)

- **FILTRO** `ibs_7min` < `0.7976` → IC=-0.168 (n=410)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7976
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=1231)

- **FILTRO** `ballena_activa_n` > `157.0` → IC=-0.184 (n=409)

  - _Acción_: SKIP cuando `ballena_activa_n` > 157.0
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=1232)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.219 (n=411)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=1245)

- **FILTRO** `ballena_activa_n` > `131.0` → IC=-0.172 (n=413)

  - _Acción_: SKIP cuando `ballena_activa_n` > 131.0
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=1243)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.201 (n=296)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=905)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.316 (n=389)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=812)

- **FILTRO** `ibs_7min` < `0.2097` → IC=-0.285 (n=300)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2097
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=901)

- **FILTRO** `ballena_activa_n` > `16.0` → IC=-0.278 (n=295)

  - _Acción_: SKIP cuando `ballena_activa_n` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=906)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.261 (n=379)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=1389)

- **FILTRO** `ibs_7min` > `0.8192` → IC=-0.195 (n=441)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8192
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=1327)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.151 (n=434)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=976)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.258 (n=333)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=1077)

- **FILTRO** `ibs_7min` < `0.7565` → IC=-0.184 (n=352)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7565
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=1058)

- **FILTRO** `ballena_activa_n` > `43.0` → IC=-0.218 (n=342)

  - _Acción_: SKIP cuando `ballena_activa_n` > 43.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=1068)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.133 (n=456)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=948)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.286 (n=321)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=1083)

- **FILTRO** `ibs_7min` > `0.1866` → IC=-0.164 (n=477)

  - _Acción_: SKIP cuando `ibs_7min` > 0.1866
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=927)

- **FILTRO** `ballena_activa_n` > `26.0` → IC=-0.192 (n=475)

  - _Acción_: SKIP cuando `ballena_activa_n` > 26.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=929)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.42` → IC=-0.226 (n=400)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=1202)

- **FILTRO** `ibs_7min` < `0.7759` → IC=-0.192 (n=400)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7759
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=1202)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.181 (n=399)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1203)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.188 (n=460)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=1424)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.134 (n=394)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=999)

- **FILTRO** `py_entrada` < `0.38` → IC=-0.282 (n=333)

  - _Acción_: SKIP cuando `py_entrada` < 0.38
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1060)

- **FILTRO** `ibs_7min` < `0.7532` → IC=-0.206 (n=348)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7532
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=1045)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.221 (n=345)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=1048)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.269 (n=353)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=1367)

- **FILTRO** `ibs_7min` > `0.8333` → IC=-0.166 (n=429)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8333
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=1291)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.121 (n=566)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=1154)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=149)

- **FILTRO** `drift_7min_pct` |x|> `0.106` → IC=-0.139 (n=59)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.106
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=116)

- **FILTRO** `ibs_7min` > `0.0606` → IC=-0.133 (n=58)

  - _Acción_: SKIP cuando `ibs_7min` > 0.0606
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=117)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=412)

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
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=435)

### ORDER_FLOW_5M
- **FILTRO** `total_vol_5m` > `215.224` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `total_vol_5m` > 215.224
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **PATRÓN** `delta_ratio` |x|> `0.45` → IC=+0.184 (n=96)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.92€ cuando `delta_ratio` |x|> 0.45 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.157 (n=97)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 15.0 (IC base=+0.122)

- **PATRÓN** `total_vol_5m` < `422.506` → IC=+0.222 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 422.506 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `3582.6278` → IC=+0.158 (n=71)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 3582.6278 (IC base=+0.122)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.283 (n=44)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.152)

- **PATRÓN** `total_vol_5m` < `600.958` → IC=+0.176 (n=66)

  - _Acción_: Kelly boost +0.88€ cuando `total_vol_5m` < 600.958 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.156 (n=59)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 52.0 (IC base=+0.152)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `hora_utc` < `8.0` → IC=+0.222 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=27)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `3221.1629` → IC=+0.197 (n=31)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 3221.1629 (IC base=+0.125)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` < `0.0084` → IC=-0.180 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0084
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=71)

- **FILTRO** `T_h` > `63.9866` → IC=-0.345 (n=95)

  - _Acción_: SKIP cuando `T_h` > 63.9866
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=32)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0069` → IC=-0.357 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0069
  - _Potencial_: sin este filtro IC_bueno=+0.239 (n=21)

- **FILTRO** `T_h` > `87.9981` → IC=-0.458 (n=22)

  - _Acción_: SKIP cuando `T_h` > 87.9981
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=24)

- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.239 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=-0.151)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0129` → IC=-0.184 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0129
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.006` → IC=-0.129 (n=68)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.006
  - _Potencial_: sin este filtro IC_bueno=+0.132 (n=36)

- **FILTRO** `T_h` > `144.6177` → IC=-0.352 (n=25)

  - _Acción_: SKIP cuando `T_h` > 144.6177
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=79)

- **FILTRO** `T_h` < `87.9947` → IC=-0.452 (n=19)

  - _Acción_: SKIP cuando `T_h` < 87.9947
  - _Potencial_: sin este filtro IC_bueno=-0.297 (n=62)

- **PATRÓN** `pct_vs_K` |x|≤ `1.4454` → IC=+0.176 (n=35)

  - _Acción_: Kelly boost +0.88€ cuando `pct_vs_K` |x|≤ 1.4454 (IC base=-0.038)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` < `0.005` → IC=-0.180 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `T_h` > `111.9957` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `T_h` > 111.9957
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=17)

- **FILTRO** `sigma_h` < `0.0055` → IC=-0.328 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0055
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

### STREAK_FADE_15M
- **FILTRO** `hora_utc` < `4.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=32)

- **FILTRO** `streak_estiramiento` > `0.4429` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.4429
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=18)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=78)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.177 (n=29)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 34.0 (IC base=+0.015)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.188 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=40)

- **FILTRO** `streak_estiramiento` > `0.5402` → IC=-0.133 (n=28)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.5402
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=15)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=53)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `hora_utc` > `4.0` → IC=-0.167 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.250 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=87)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=96)

- **FILTRO** `streak_estiramiento` > `0.6136` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.6136
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=53)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=97)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=141)

- **PATRÓN** `streak_estiramiento` < `0.2979` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.2979 (IC base=+0.006)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=296)

- **PATRÓN** `streak_len` < `3.0` → IC=+0.139 (n=153)

  - _Acción_: Kelly boost +0.69€ cuando `streak_len` < 3.0 (IC base=+0.068)

- **PATRÓN** `streak_estiramiento` < `0.3335` → IC=+0.149 (n=35)

  - _Acción_: Kelly boost +0.74€ cuando `streak_estiramiento` < 0.3335 (IC base=+0.010)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=158)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=213)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.129 (n=157)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 14.0 (IC base=+0.070)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=1186)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=672)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=680)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.146 (n=128)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0029 (IC base=+0.115)

- **PATRÓN** `drift_60min` |x|≤ `0.188` → IC=+0.122 (n=382)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.61€ cuando `drift_60min` |x|≤ 0.188 (IC base=+0.115)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0679` → IC=+0.125 (n=382)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.62€ cuando `delta_ratio_macro` |x|> 0.0679 (IC base=+0.115)

- **PATRÓN** `ibs_15` > `0.5275` → IC=+0.203 (n=382)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5275 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` > `0.3848` → IC=+0.173 (n=102)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.3848 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.629` → IC=+0.245 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.629 (IC base=+0.115)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=399)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.01 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `2964.2504` → IC=+0.146 (n=255)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 2964.2504 (IC base=+0.115)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 73.0 (IC base=+0.115)

- **PATRÓN** `ibs_15` < `0.1154` → IC=+0.140 (n=440)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.70€ cuando `ibs_15` < 0.1154 (IC base=+0.026)

### UPDOWN_GBM#5min
- **FILTRO** `ibs_15` < `0.2222` → IC=-0.223 (n=117)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.2222
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=362)

- **FILTRO** `sigma_ewma_delta_pct` > `6.565` → IC=-0.209 (n=53)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.565
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=426)

### UPDOWN_GBM#60min
- **FILTRO** `sigma_h` < `0.0053` → IC=-0.222 (n=16)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=50)

- **FILTRO** `ibs_15` < `0.16` → IC=-0.289 (n=17)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.16
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=35)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=12)

### UPDOWN_GBM#BTC#15min
- **FILTRO** `ibs_15` > `0.7305` → IC=-0.262 (n=19)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.7305
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=60)

- **FILTRO** `ibs_15` < `0.3308` → IC=-0.179 (n=26)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.3308
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=53)

- **FILTRO** `libro_liquidez` < `13878.9673` → IC=-0.286 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 13878.9673
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=53)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.160 (n=95)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0035 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.0862` → IC=+0.200 (n=48)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0862 (IC base=+0.148)

- **PATRÓN** `drift_15min` |x|≤ `0.4599` → IC=+0.176 (n=72)

  - _Acción_: Kelly boost +0.88€ cuando `drift_15min` |x|≤ 0.4599 (IC base=+0.148)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2616` → IC=+0.210 (n=36)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2616 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.176 (n=109)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 4.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.161 (n=110)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 16.0 (IC base=+0.148)

- **PATRÓN** `ibs_15` > `0.9375` → IC=+0.284 (n=49)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9375 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.3017` → IC=+0.186 (n=49)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.3017 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` < `0.5371` → IC=+0.164 (n=120)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.5371 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.945` → IC=+0.197 (n=64)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 6.945 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `12448.5931` → IC=+0.158 (n=36)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 12448.5931 (IC base=+0.148)

### UPDOWN_GBM#BTC#5min
- **FILTRO** `sigma_h` < `0.0032` → IC=-0.184 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0032
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=36)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1001` → IC=-0.184 (n=17)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1001
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=36)

- **FILTRO** `hora_utc` < `4.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=37)

- **FILTRO** `ibs_15` < `0.1271` → IC=-0.289 (n=17)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.1271
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=36)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `hora_utc` < `11.0` → IC=-0.132 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=78)

### UPDOWN_GBM#ETH#15min
- **FILTRO** `ibs_15` < `0.617` → IC=-0.237 (n=36)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.617
  - _Potencial_: sin este filtro IC_bueno=+0.240 (n=75)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.132 (n=74)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0044 (IC base=+0.084)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2085` → IC=+0.200 (n=38)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2085 (IC base=+0.084)

- **PATRÓN** `ibs_15` > `0.617` → IC=+0.240 (n=75)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.617 (IC base=+0.084)

- **PATRÓN** `dist_vwap_pct` < `0.0857` → IC=+0.146 (n=46)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.0857 (IC base=+0.084)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.937` → IC=+0.192 (n=37)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 8.937 (IC base=+0.084)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.128 (n=178)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.0053 (IC base=+0.018)

### UPDOWN_GBM#ETH#5min
- **FILTRO** `hora_utc` > `8.0` → IC=-0.167 (n=25)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=60)

- **FILTRO** `dist_vwap_pct` > `0.1635` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1635
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=70)

- **FILTRO** `drift_15min` |x|> `0.5452` → IC=-0.173 (n=108)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.5452
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=328)

### UPDOWN_GBM#ETH#60min
- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=45)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.020)

### UPDOWN_GBM#SOL#15min
- **FILTRO** `ibs_15` < `0.6` → IC=-0.177 (n=29)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.265 (n=32)

- **PATRÓN** `ibs_15` > `0.6` → IC=+0.265 (n=32)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6 (IC base=+0.056)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.477` → IC=+0.318 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.477 (IC base=+0.056)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0076` → IC=-0.167 (n=34)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0076
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=35)

- **FILTRO** `ibs_15` < `0.2` → IC=-0.395 (n=17)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=52)

### UPDOWN_GBM#SOL#60min
- **FILTRO** `sigma_h` > `0.0127` → IC=-0.214 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0127
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=38)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.265 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=-0.009)

- **PATRÓN** `ibs_15` > `0.5` → IC=+0.129 (n=33)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.64€ cuando `ibs_15` > 0.5 (IC base=-0.009)

- **PATRÓN** `dist_vwap_pct` < `0.3805` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` < 0.3805 (IC base=-0.009)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `hora_utc` < `6.0` → IC=+0.167 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 6.0 (IC base=+0.096)

- **PATRÓN** `ibs_15` > `0.5556` → IC=+0.185 (n=90)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.92€ cuando `ibs_15` > 0.5556 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.3338` → IC=+0.281 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3338 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.845` → IC=+0.235 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.845 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `2451.9374` → IC=+0.141 (n=101)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 2451.9374 (IC base=+0.096)

- **PATRÓN** `ibs_15` < `0.1282` → IC=+0.216 (n=107)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1282 (IC base=+0.050)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.404 (n=50)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0057 (IC base=+0.315)

- **PATRÓN** `drift_60min` |x|≤ `0.1957` → IC=+0.324 (n=151)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1957 (IC base=+0.315)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1528` → IC=+0.332 (n=99)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1528 (IC base=+0.315)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3943` → IC=+0.389 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3943 (IC base=+0.315)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.337 (n=139)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.315)

- **PATRÓN** `ibs_15` > `0.8066` → IC=+0.374 (n=133)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8066 (IC base=+0.315)

- **PATRÓN** `dist_vwap_pct` > `0.5461` → IC=+0.357 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5461 (IC base=+0.315)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.354` → IC=+0.345 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.354 (IC base=+0.315)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.316 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.315)

- **PATRÓN** `libro_liquidez` > `7885.1862` → IC=+0.365 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7885.1862 (IC base=+0.315)

- **PATRÓN** `ballena_activa_n` < `540.0` → IC=+0.385 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 540.0 (IC base=+0.315)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1421` → IC=+0.321 (n=37)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1421 (IC base=+0.289)

- **PATRÓN** `sigma_h` > `0.0045` → IC=+0.400 (n=28)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0045 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.16` → IC=+0.316 (n=74)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.16 (IC base=+0.289)

- **PATRÓN** `drift_15min` |x|≤ `0.4136` → IC=+0.321 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4136 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.327 (n=79)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.289)

- **PATRÓN** `ibs_15` > `0.7518` → IC=+0.326 (n=84)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7518 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` > `0.4264` → IC=+0.385 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4264 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.145` → IC=+0.300 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.145 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `8508.8052` → IC=+0.378 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8508.8052 (IC base=+0.289)

- **PATRÓN** `ballena_activa_n` < `480.0` → IC=+0.444 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 480.0 (IC base=+0.289)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.339 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.341)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.406 (n=30)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.341)

- **PATRÓN** `drift_60min` |x|≤ `0.1189` → IC=+0.370 (n=44)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1189 (IC base=+0.341)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1435` → IC=+0.389 (n=43)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1435 (IC base=+0.341)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.361 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.341)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.344 (n=43)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.341)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.344 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.341)

- **PATRÓN** `ibs_15` > `0.7914` → IC=+0.433 (n=58)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7914 (IC base=+0.341)

- **PATRÓN** `dist_vwap_pct` < `0.156` → IC=+0.340 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.156 (IC base=+0.341)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.937` → IC=+0.406 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.937 (IC base=+0.341)

- **PATRÓN** `libro_liquidez` > `3261.6008` → IC=+0.367 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3261.6008 (IC base=+0.341)

- **PATRÓN** `ballena_activa_n` < `162.0` → IC=+0.350 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 162.0 (IC base=+0.341)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0078` → IC=-0.138 (n=338)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0078
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=657)

- **FILTRO** `ibs_15` < `0.4545` → IC=-0.270 (n=98)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.4545
  - _Potencial_: sin este filtro IC_bueno=+0.165 (n=299)

- **FILTRO** `sigma_ewma_delta_pct` > `17.423` → IC=-0.176 (n=341)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.423
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=2491)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3537` → IC=+0.152 (n=136)

  - _Acción_: Kelly boost +0.76€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3537 (IC base=-0.058)

- **PATRÓN** `ibs_15` > `0.4545` → IC=+0.165 (n=299)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.82€ cuando `ibs_15` > 0.4545 (IC base=-0.058)

- **PATRÓN** `delta_ratio_macro` |x|> `0.133` → IC=+0.267 (n=101)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.133 (IC base=-0.079)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1083` → IC=+0.357 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1083 (IC base=-0.079)

- **PATRÓN** `ibs_15` < `0.3315` → IC=+0.337 (n=151)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3315 (IC base=-0.079)

- **PATRÓN** `dist_vwap_pct` < `0.5986` → IC=+0.251 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5986 (IC base=-0.079)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0074` → IC=-0.239 (n=155)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0074
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=468)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.215 (n=205)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.205 (n=418)

- **FILTRO** `hora_utc` > `16.0` → IC=-0.247 (n=152)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=471)

- **FILTRO** `sigma_ewma_delta_pct` > `19.957` → IC=-0.265 (n=117)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.957
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=506)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.4479` → IC=-0.367 (n=43)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.4479
  - _Potencial_: sin este filtro IC_bueno=+0.189 (n=130)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=156)

- **PATRÓN** `drift_60min` |x|≤ `0.0629` → IC=+0.196 (n=44)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.0629 (IC base=+0.049)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3537` → IC=+0.239 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3537 (IC base=+0.049)

- **PATRÓN** `ibs_15` > `0.4479` → IC=+0.189 (n=130)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.95€ cuando `ibs_15` > 0.4479 (IC base=+0.049)

- **PATRÓN** `libro_liquidez` > `9861.0594` → IC=+0.221 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9861.0594 (IC base=+0.049)

- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1045` → IC=+0.269 (n=63)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1045 (IC base=+0.260)

- **PATRÓN** `sigma_h` > `0.0061` → IC=+0.312 (n=62)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0061 (IC base=+0.260)

- **PATRÓN** `drift_15min` |x|≤ `0.4204` → IC=+0.258 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4204 (IC base=+0.260)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1465` → IC=+0.297 (n=62)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1465 (IC base=+0.260)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1083` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1083 (IC base=+0.260)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.297 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.260)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.306 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.260)

- **PATRÓN** `ibs_15` < `0.3345` → IC=+0.353 (n=93)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3345 (IC base=+0.260)

- **PATRÓN** `dist_vwap_pct` > `0.1514` → IC=+0.259 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1514 (IC base=+0.260)

- **PATRÓN** `dist_vwap_pct` < `0.3293` → IC=+0.264 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3293 (IC base=+0.260)

- **PATRÓN** `sigma_ewma_delta_pct` < `11.326` → IC=+0.288 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 11.326 (IC base=+0.260)

- **PATRÓN** `libro_liquidez` > `12249.9576` → IC=+0.318 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12249.9576 (IC base=+0.260)

- **PATRÓN** `ballena_activa_n` < `206.0` → IC=+0.285 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 206.0 (IC base=+0.260)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_15min` |x|> `0.7725` → IC=-0.194 (n=60)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.7725
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=181)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.099 (n=220)

- **FILTRO** `sigma_ewma_delta_pct` > `15.711` → IC=-0.158 (n=109)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 15.711
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=867)

- **PATRÓN** `ibs_15` > `0.8125` → IC=+0.206 (n=15)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8125 (IC base=-0.105)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `hora_utc` > `6.0` → IC=-0.195 (n=162)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=84)

- **FILTRO** `sigma_ewma_delta_pct` > `14.4` → IC=-0.176 (n=32)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 14.4
  - _Potencial_: sin este filtro IC_bueno=-0.134 (n=214)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=50)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=196)

- **FILTRO** `libro_liquidez` < `2584.4484` → IC=-0.199 (n=81)

  - _Acción_: SKIP cuando `libro_liquidez` < 2584.4484
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=165)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.304 (n=105)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0054 (IC base=+0.281)

- **PATRÓN** `drift_60min` |x|≤ `0.0529` → IC=+0.325 (n=78)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0529 (IC base=+0.281)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1378` → IC=+0.314 (n=154)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1378 (IC base=+0.281)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3906` → IC=+0.330 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3906 (IC base=+0.281)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.313 (n=239)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.281)

- **PATRÓN** `ibs_15` > `0.9647` → IC=+0.360 (n=105)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9647 (IC base=+0.281)

- **PATRÓN** `dist_vwap_pct` > `0.2994` → IC=+0.354 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2994 (IC base=+0.281)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.866` → IC=+0.288 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.866 (IC base=+0.281)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.888` → IC=+0.281 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.888 (IC base=+0.281)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.280 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.281)

- **PATRÓN** `libro_liquidez` > `12303.8128` → IC=+0.348 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12303.8128 (IC base=+0.281)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.267 (n=58)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.260)

- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.304 (n=44)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0057 (IC base=+0.260)

- **PATRÓN** `drift_60min` |x|≤ `0.1837` → IC=+0.280 (n=130)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1837 (IC base=+0.260)

- **PATRÓN** `drift_15min` |x|≤ `0.6671` → IC=+0.261 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.6671 (IC base=+0.260)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1438` → IC=+0.286 (n=87)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1438 (IC base=+0.260)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1386` → IC=+0.333 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1386 (IC base=+0.260)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.277 (n=119)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.260)

- **PATRÓN** `ibs_15` > `0.9676` → IC=+0.336 (n=59)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9676 (IC base=+0.260)

- **PATRÓN** `dist_vwap_pct` > `0.3017` → IC=+0.347 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3017 (IC base=+0.260)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.789` → IC=+0.306 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.789 (IC base=+0.260)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.866` → IC=+0.264 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.866 (IC base=+0.260)

- **PATRÓN** `libro_liquidez` > `13561.3229` → IC=+0.326 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13561.3229 (IC base=+0.260)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.308 (n=102)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0072 (IC base=+0.303)

- **PATRÓN** `sigma_h` > `0.0061` → IC=+0.312 (n=46)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0061 (IC base=+0.303)

- **PATRÓN** `drift_60min` |x|≤ `0.0603` → IC=+0.333 (n=46)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0603 (IC base=+0.303)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1881` → IC=+0.375 (n=46)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1881 (IC base=+0.303)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3048` → IC=+0.360 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3048 (IC base=+0.303)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.348 (n=97)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.303)

- **PATRÓN** `ibs_15` > `0.8687` → IC=+0.349 (n=91)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8687 (IC base=+0.303)

- **PATRÓN** `dist_vwap_pct` > `0.6525` → IC=+0.417 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6525 (IC base=+0.303)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.888` → IC=+0.308 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.888 (IC base=+0.303)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.564` → IC=+0.302 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.564 (IC base=+0.303)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.311 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.303)

- **PATRÓN** `libro_liquidez` > `10575.7678` → IC=+0.417 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10575.7678 (IC base=+0.303)

- **PATRÓN** `ballena_activa_n` < `263.0` → IC=+0.319 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 263.0 (IC base=+0.303)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1143` → IC=-0.259 (n=27)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1143
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=53)

- **FILTRO** `sigma_h` > `0.0065` → IC=-0.214 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0065
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=61)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1222` → IC=-0.184 (n=93)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1222
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=283)

- **FILTRO** `sigma_h` > `0.007` → IC=-0.163 (n=93)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=283)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1533` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1533
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=11)

- **FILTRO** `ballena_activa_n` > `34.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `ballena_activa_n` > 34.0
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=49)

### UPDOWN_OU_5M#DOGE#5min
- **FILTRO** `drift_15min` |x|> `0.3434` → IC=-0.184 (n=17)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3434
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `sigma_h` < `0.0054` → IC=-0.167 (n=16)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0054
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### WEEKLY_PRICE
- **PATRÓN** `T_h` < `63.9936` → IC=+0.237 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 63.9936 (IC base=+0.083)

- **PATRÓN** `ratio` < `0.9722` → IC=+0.452 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9722 (IC base=+0.083)

- **PATRÓN** `T_h` > `146.1038` → IC=+0.441 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1038 (IC base=+0.342)

- **PATRÓN** `ratio` < `1.0177` → IC=+0.250 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 1.0177 (IC base=+0.342)

- **PATRÓN** `ratio` > `1.0126` → IC=+0.174 (n=44)

  - _Acción_: Kelly boost +0.87€ cuando `ratio` > 1.0126 (IC base=+0.342)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` < `111.9957` → IC=+0.335 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 111.9957 (IC base=+0.262)

- **PATRÓN** `pct_dist` |x|≤ `0.6014` → IC=+0.284 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `pct_dist` |x|≤ 0.6014 (IC base=+0.262)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` < `82.5234` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 82.5234 (IC base=+0.123)

- **PATRÓN** `T_h` < `111.9838` → IC=+0.312 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 111.9838 (IC base=+0.302)

- **PATRÓN** `T_h` > `145.7785` → IC=+0.309 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7785 (IC base=+0.302)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1118` → IC=+0.454 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1118 (IC base=+0.415)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-SIGMA-SOL-60MIN**: `UPDOWN_GBM#SOL#60min` gana cuando sigma_h < 0.0058 (IC=+0.265 n=15). Implementar como filtro pre-predicción en shadow_predict.py.
- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5275 sube el IC de +0.115 a +0.203 en UPDOWN_GBM#15min (n=382). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.9375 sube el IC de +0.148 a +0.284 en UPDOWN_GBM#BTC#15min (n=49). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.617 sube el IC de +0.084 a +0.240 en UPDOWN_GBM#ETH#15min (n=75). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.056 a +0.265 en UPDOWN_GBM#SOL#15min (n=32). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5556 sube el IC de +0.096 a +0.185 en UPDOWN_GBM#XRP#15min (n=90). Ya aplicado como kelly_boost=+0.92€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1282 sube el IC de +0.050 a +0.216 en UPDOWN_GBM#XRP#15min (n=107). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.4545 sube el IC de -0.058 a +0.165 en UPDOWN_GBM_15M_TARDIO (n=299). Ya aplicado como kelly_boost=+0.82€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3315 sube el IC de -0.079 a +0.337 en UPDOWN_GBM_15M_TARDIO (n=151). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.4479 sube el IC de +0.049 a +0.189 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=130). Ya aplicado como kelly_boost=+0.95€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3345 sube el IC de +0.260 a +0.353 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=93). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8125 sube el IC de -0.105 a +0.206 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=15). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.9647 sube el IC de +0.281 a +0.360 en UPDOWN_GBM_IBS_ALTO (n=105). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.9676 sube el IC de +0.260 a +0.336 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=59). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8687 sube el IC de +0.303 a +0.349 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=91). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.8066 sube el IC de +0.315 a +0.374 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=133). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.7518 sube el IC de +0.289 a +0.326 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=84). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7914 sube el IC de +0.341 a +0.433 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=58). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min` — IC=+0.348 n=31. Faltan ~9 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL` — IC=+0.348 n=31. Faltan ~9 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `ORDER_FLOW_5M#ETH#5min` — IC=+0.125 n=38. Faltan ~2 resoluciones para umbral n≥40. ETA: ~1h.
- **LIVE-CANDIDATA**: `ORDER_FLOW_5M#ETH` — IC=+0.125 n=38. Faltan ~2 resoluciones para umbral n≥40. ETA: ~1h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min` — IC=+0.105 n=36. Faltan ~4 resoluciones para umbral n≥40. ETA: ~3h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH` — IC=+0.105 n=36. Faltan ~4 resoluciones para umbral n≥40. ETA: ~3h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 604 | +0.086 | +46.18€ | 1 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 604 | +0.086 | +46.18€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 360 | +0.111 | +35.17€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 360 | +0.111 | +35.17€ | 0 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 215 | +0.030 | +0.07€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 215 | +0.030 | +0.07€ | 7 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 29 | +0.177 | +10.93€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 29 | +0.177 | +10.93€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 9681 | -0.099 | -1524.50€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 696 | -0.085 | -128.45€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 8985 | -0.100 | -1396.05€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 1210 | -0.010 | -203.15€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 1210 | -0.010 | -203.15€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 696 | -0.085 | -128.45€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 696 | -0.085 | -128.45€ | 3 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 1210 | -0.174 | -404.50€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 1210 | -0.174 | -404.50€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 2624 | -0.072 | -252.87€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 2624 | -0.072 | -252.87€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 2263 | -0.070 | -107.58€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 2263 | -0.070 | -107.58€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 1678 | -0.195 | -427.95€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 1678 | -0.195 | -427.95€ | 1 | 0 |
| ✅ FAVORITO_CONFIRMADO | 32273 | +0.115 | -2033.13€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 5942 | +0.186 | -217.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 107 | -0.105 | -50.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 23030 | +0.097 | -1725.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 3194 | +0.120 | -39.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 3866 | +0.064 | -652.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 21 | -0.065 | +2.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#240min | 5 | -0.089 | -6.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 3840 | +0.066 | -648.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 6663 | +0.133 | -150.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 1678 | +0.195 | -97.81€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 3833 | +0.110 | -87.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 1110 | +0.130 | +57.05€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 3874 | +0.082 | -476.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 21 | +0.065 | +3.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 3852 | +0.082 | -477.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 7151 | +0.128 | -89.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 2163 | +0.166 | -20.99€ | 0 | 8 |
| 🚫 FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 3834 | +0.116 | -36.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 1142 | +0.101 | -23.60€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL | 6856 | +0.136 | -401.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 2042 | +0.203 | -103.41€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 46 | +0.000 | -9.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 3826 | +0.101 | -215.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 942 | +0.132 | -73.29€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 3863 | +0.106 | -262.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 17 | -0.022 | -0.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 3845 | +0.106 | -260.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 5890 | +0.172 | -474.02€ | 3 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 5890 | +0.172 | -474.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 1481 | +0.167 | -157.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 1481 | +0.167 | -157.21€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 114 | -0.129 | +1.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 114 | -0.129 | +1.04€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 1468 | +0.161 | -172.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 1468 | +0.161 | -172.99€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 1322 | +0.227 | -42.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 1322 | +0.227 | -42.79€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 1426 | +0.181 | -115.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 1426 | +0.181 | -115.82€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 302 | +0.444 | +2.19€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 302 | +0.444 | +2.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 115 | +0.440 | +0.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 115 | +0.440 | +0.97€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 112 | +0.430 | -1.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 112 | +0.430 | -1.12€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 72 | +0.446 | +2.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 72 | +0.446 | +2.20€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 16448 | +0.191 | -1439.27€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 16448 | +0.191 | -1439.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 3014 | +0.125 | -559.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 3014 | +0.125 | -559.35€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 2556 | +0.238 | -47.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 2556 | +0.238 | -47.95€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 2821 | +0.165 | -355.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 2821 | +0.165 | -355.03€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 2612 | +0.230 | -76.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 2612 | +0.230 | -76.09€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 2673 | +0.217 | -126.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 2673 | +0.217 | -126.30€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 2772 | +0.185 | -274.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 2772 | +0.185 | -274.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 5970 | +0.133 | +216.84€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 5970 | +0.133 | +216.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 2969 | +0.141 | +147.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 2969 | +0.141 | +147.05€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 3001 | +0.126 | +69.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 3001 | +0.126 | +69.79€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 766 | +0.301 | +7.25€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 766 | +0.301 | +7.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 329 | +0.282 | -7.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 329 | +0.282 | -7.05€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 361 | +0.302 | +9.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 361 | +0.302 | +9.23€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 76 | +0.359 | +5.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 76 | +0.359 | +5.06€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 325 | +0.414 | -13.70€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 325 | +0.414 | -13.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 146 | +0.412 | -6.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 146 | +0.412 | -6.63€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 148 | +0.420 | -5.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 148 | +0.420 | -5.76€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 31 | +0.348 | -1.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 31 | +0.348 | -1.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 236 | +0.101 | +0.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 70 | +0.139 | +4.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 166 | +0.083 | -4.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 8 | +0.120 | +4.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 8 | +0.120 | +4.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 194 | +0.097 | -0.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 28 | +0.167 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 166 | +0.083 | -4.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 34 | +0.056 | -3.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 34 | +0.056 | -3.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 6391 | +0.097 | -208.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 654 | +0.064 | -24.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 5737 | +0.101 | -184.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 4393 | +0.097 | -95.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 654 | +0.064 | -24.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 3739 | +0.102 | -70.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 36 | +0.105 | +0.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 36 | +0.105 | +0.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 1962 | +0.098 | -114.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 1962 | +0.098 | -114.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 431 | +0.290 | -22.34€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 431 | +0.290 | -22.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 431 | +0.290 | -22.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 431 | +0.290 | -22.34€ | 0 | 4 |
| ✅ GBM_LATE_15M | 7712 | +0.044 | +2457.67€ | 0 | 15 |
| ✅ GBM_LATE_15M#15min | 7712 | +0.044 | +2457.67€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 1045 | +0.171 | +648.83€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 1045 | +0.171 | +648.83€ | 0 | 19 |
| ✅ GBM_LATE_15M#BTC | 1088 | +0.171 | +620.71€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 1088 | +0.171 | +620.71€ | 0 | 28 |
| ✅ GBM_LATE_15M#DOGE | 1049 | +0.186 | +709.41€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 1049 | +0.186 | +709.41€ | 0 | 19 |
| ✅ GBM_LATE_15M#ETH | 1258 | -0.042 | +47.46€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 1258 | -0.042 | +47.46€ | 2 | 12 |
| ✅ GBM_LATE_15M#SOL | 1421 | -0.046 | +133.25€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 1421 | -0.046 | +133.25€ | 5 | 3 |
| ✅ GBM_LATE_15M#XRP | 1851 | -0.055 | +298.01€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 1851 | -0.055 | +298.01€ | 4 | 6 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 8654 | +0.045 | +3398.65€ | 0 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 8654 | +0.045 | +3398.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 1337 | -0.018 | +648.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 1337 | -0.018 | +648.58€ | 2 | 3 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 1889 | -0.039 | +152.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 1889 | -0.039 | +152.38€ | 1 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 918 | +0.237 | +828.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 918 | +0.237 | +828.39€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 1446 | -0.046 | +3.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 1446 | -0.046 | +3.18€ | 8 | 2 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 1541 | -0.022 | +340.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 1541 | -0.022 | +340.08€ | 7 | 8 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 1523 | +0.244 | +1426.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 1523 | +0.244 | +1426.04€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 6253 | +0.169 | +4264.52€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 6253 | +0.169 | +4264.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 801 | +0.184 | +559.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 801 | +0.184 | +559.57€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 1061 | +0.161 | +708.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 1061 | +0.161 | +708.36€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 789 | +0.203 | +615.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 789 | +0.203 | +615.67€ | 0 | 18 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 1038 | +0.164 | +674.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 1038 | +0.164 | +674.28€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 1195 | +0.119 | +676.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 1195 | +0.119 | +676.01€ | 1 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 1369 | +0.192 | +1030.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 1369 | +0.192 | +1030.62€ | 0 | 21 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 1113 | +0.081 | +250.06€ | 0 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 1113 | +0.081 | +250.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 56 | +0.086 | +14.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 56 | +0.086 | +14.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 321 | +0.113 | +119.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 321 | +0.113 | +119.29€ | 3 | 19 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 69 | +0.091 | +20.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 69 | +0.091 | +20.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 209 | +0.192 | +81.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 209 | +0.192 | +81.50€ | 1 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 310 | -0.022 | -0.74€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 310 | -0.022 | -0.74€ | 5 | 3 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 148 | +0.060 | +14.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 148 | +0.060 | +14.84€ | 0 | 6 |
| ✅ GBM_LATE_15M_TARDIO | 7293 | +0.170 | +4846.46€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#15min | 7293 | +0.170 | +4846.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 998 | +0.192 | +723.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 998 | +0.192 | +723.20€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 1189 | +0.161 | +738.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 1189 | +0.161 | +738.80€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 988 | +0.220 | +827.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 988 | +0.220 | +827.93€ | 0 | 17 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 1122 | +0.149 | +648.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 1122 | +0.149 | +648.08€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 1310 | +0.107 | +654.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 1310 | +0.107 | +654.16€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 1686 | +0.195 | +1254.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 1686 | +0.195 | +1254.28€ | 0 | 22 |
| ✅ GBM_LATE_5M | 1658 | +0.134 | +787.06€ | 1 | 28 |
| ✅ GBM_LATE_5M#5min | 1658 | +0.134 | +787.06€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 79 | +0.191 | +48.83€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 79 | +0.191 | +48.83€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 651 | +0.134 | +354.00€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 651 | +0.134 | +354.00€ | 4 | 17 |
| ✅ GBM_LATE_5M#DOGE | 58 | +0.083 | +10.84€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 58 | +0.083 | +10.84€ | 0 | 1 |
| ✅ GBM_LATE_5M#ETH | 590 | +0.149 | +285.44€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 590 | +0.149 | +285.44€ | 0 | 27 |
| ✅ GBM_LATE_5M#SOL | 125 | -0.020 | +0.12€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 125 | -0.020 | +0.12€ | 3 | 0 |
| ✅ GBM_LATE_5M#XRP | 155 | +0.181 | +87.83€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 155 | +0.181 | +87.83€ | 0 | 0 |
| ✅ GBM_LATE_60M | 516 | -0.039 | +84.47€ | 5 | 8 |
| ✅ GBM_LATE_60M#60min | 516 | -0.039 | +84.47€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 178 | +0.000 | +5.18€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 178 | +0.000 | +5.18€ | 2 | 4 |
| ✅ GBM_LATE_60M#ETH | 185 | -0.008 | +56.38€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 185 | -0.008 | +56.38€ | 2 | 7 |
| ✅ GBM_LATE_60M#SOL | 153 | -0.119 | +22.91€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 153 | -0.119 | +22.91€ | 2 | 0 |
| 🚫 GBM_LATE_60M_FADE | 195 | -0.302 | -33.28€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 195 | -0.302 | -33.28€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 77 | -0.260 | -7.87€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 77 | -0.260 | -7.87€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 65 | -0.351 | -19.05€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 65 | -0.351 | -19.05€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 53 | -0.282 | -6.35€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 53 | -0.282 | -6.35€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 334 | +0.036 | +0.23€ | 2 | 2 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 334 | +0.036 | +0.23€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 133 | +0.018 | +3.58€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 133 | +0.018 | +3.58€ | 2 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 84 | +0.070 | +1.11€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 84 | +0.070 | +1.11€ | 0 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 117 | +0.029 | -4.47€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 117 | +0.029 | -4.47€ | 2 | 5 |
| ✅ LATE_WINDOW_5MIN | 14 | +0.175 | +4.14€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 14 | +0.175 | +4.14€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 14 | +0.175 | +4.14€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 14 | +0.175 | +4.14€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 312 | +0.118 | +96.92€ | 0 | 5 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 312 | +0.118 | +96.92€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 312 | +0.118 | +96.92€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 312 | +0.118 | +96.92€ | 0 | 5 |
| ✅ LIQUIDACIONES_15M | 216 | -0.110 | -29.46€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 216 | -0.110 | -29.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 55 | -0.132 | -9.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 55 | -0.132 | -9.15€ | 2 | 0 |
| 🚫 LIQUIDACIONES_15M#DOGE | 22 | -0.208 | -5.32€ | 0 | 0 |
| 🚫 LIQUIDACIONES_15M#DOGE#15min | 22 | -0.208 | -5.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 44 | -0.043 | -3.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 44 | -0.043 | -3.91€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 44 | +0.000 | -0.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 44 | +0.000 | -0.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 46 | -0.167 | -8.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 46 | -0.167 | -8.95€ | 2 | 0 |
| ✅ LIQUIDACIONES_5M | 651 | -0.036 | -25.63€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 651 | -0.036 | -25.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 39 | -0.037 | -3.48€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 39 | -0.037 | -3.48€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 104 | -0.047 | -2.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 104 | -0.047 | -2.14€ | 1 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 67 | -0.094 | -7.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 67 | -0.094 | -7.35€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 181 | +0.003 | +2.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 181 | +0.003 | +2.63€ | 2 | 2 |
| ✅ LIQUIDACIONES_5M#SOL | 210 | -0.014 | -6.71€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 210 | -0.014 | -6.71€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 50 | -0.154 | -8.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 50 | -0.154 | -8.60€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M | 443 | -0.008 | -3.54€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 443 | -0.008 | -3.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 139 | -0.032 | -9.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 139 | -0.032 | -9.52€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 140 | +0.000 | +1.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 140 | +0.000 | +1.28€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 164 | +0.006 | +4.70€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 164 | +0.006 | +4.70€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 4533 | -0.003 | -76.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 4533 | -0.003 | -76.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 520 | -0.008 | +0.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 520 | -0.008 | +0.39€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 598 | +0.005 | -8.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 598 | +0.005 | -8.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 784 | -0.008 | -26.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 784 | -0.008 | -26.29€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 914 | +0.013 | +17.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 914 | +0.013 | +17.88€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 805 | -0.007 | -28.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 805 | -0.007 | -28.28€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 912 | -0.014 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 912 | -0.014 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 6736 | -0.033 | +222.96€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 6736 | -0.033 | +222.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 1067 | -0.025 | +140.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 1067 | -0.025 | +140.61€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 1198 | -0.033 | -25.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 1198 | -0.033 | -25.76€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 1073 | -0.041 | +103.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 1073 | -0.041 | +103.07€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 1203 | -0.033 | -28.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 1203 | -0.033 | -28.54€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 1094 | -0.038 | +39.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 1094 | -0.038 | +39.16€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 1101 | -0.030 | -5.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 1101 | -0.030 | -5.58€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 555 | -0.060 | -42.01€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 555 | -0.060 | -42.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 104 | -0.038 | -5.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 104 | -0.038 | -5.15€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 66 | -0.059 | -4.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 66 | -0.059 | -4.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 36 | -0.105 | -4.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 36 | -0.105 | -4.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 108 | -0.118 | -14.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 108 | -0.118 | -14.05€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 140 | -0.028 | -6.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 140 | -0.028 | -6.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 101 | -0.044 | -7.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 101 | -0.044 | -7.92€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M | 3166 | +0.004 | -5.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3166 | +0.004 | -5.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 126 | -0.039 | -1.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 126 | -0.039 | -1.34€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 185 | +0.008 | -2.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 185 | +0.008 | -2.27€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 136 | +0.000 | -1.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 136 | +0.000 | -1.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1156 | +0.008 | +7.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1156 | +0.008 | +7.78€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1385 | +0.006 | -2.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1385 | +0.006 | -2.03€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 178 | -0.006 | -5.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 178 | -0.006 | -5.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 18550 | -0.074 | +286.28€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 18550 | -0.074 | +286.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 2871 | -0.090 | +325.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 2871 | -0.090 | +325.42€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 3297 | -0.061 | -5.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 3297 | -0.061 | -5.25€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 2969 | -0.086 | +9.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 2969 | -0.086 | +9.50€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 2814 | -0.099 | -194.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 2814 | -0.099 | -194.08€ | 8 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 3486 | -0.047 | +1.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 3486 | -0.047 | +1.29€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 3113 | -0.070 | +149.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 3113 | -0.070 | +149.40€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 6012 | -0.010 | -119.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 6012 | -0.010 | -119.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 992 | -0.018 | -21.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 992 | -0.018 | -21.41€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1204 | +0.000 | -15.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1204 | +0.000 | -15.38€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1001 | -0.019 | -30.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1001 | -0.019 | -30.28€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1310 | -0.002 | -14.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1310 | -0.002 | -14.24€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 780 | -0.010 | -14.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 780 | -0.010 | -14.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 725 | -0.020 | -23.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 725 | -0.020 | -23.89€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 420 | +0.095 | +103.13€ | 1 | 4 |
| ✅ ORDER_FLOW_5M#5min | 284 | +0.112 | +90.53€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 87 | +0.152 | +46.88€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 87 | +0.152 | +46.88€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#DOGE | 51 | +0.085 | +9.73€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 51 | +0.085 | +9.73€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 38 | +0.125 | +13.55€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 38 | +0.125 | +13.55€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL | 46 | +0.125 | +14.98€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 46 | +0.125 | +14.98€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 62 | +0.047 | +5.39€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 62 | +0.047 | +5.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 259 | -0.159 | -20.62€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC | 115 | -0.235 | -33.14€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC#atexpiry | 100 | -0.265 | -32.41€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 15 | -0.022 | -0.74€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 99 | -0.134 | -3.00€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 80 | -0.146 | -5.97€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 19 | -0.068 | +2.97€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 45 | -0.011 | +15.52€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 38 | +0.000 | +14.95€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 7 | -0.019 | +0.57€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 218 | -0.177 | -23.43€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 41 | -0.058 | +2.80€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE | 185 | -0.174 | +23.59€ | 3 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 77 | -0.082 | +20.24€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 75 | -0.071 | +21.26€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 73 | -0.260 | -9.78€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 69 | -0.261 | -11.17€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 35 | -0.176 | +13.13€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 33 | -0.157 | +14.96€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#atexpiry | 177 | -0.165 | +25.06€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#reach | 8 | -0.120 | -1.47€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 59 | +0.287 | +11.42€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC | 17 | -0.022 | -2.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 17 | -0.022 | -2.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 17 | +0.246 | +1.95€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 17 | +0.246 | +1.95€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 25 | +0.463 | +12.41€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 25 | +0.463 | +12.41€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#sniper | 59 | +0.287 | +11.42€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 148 | -0.020 | -12.36€ | 3 | 1 |
| ✅ STREAK_FADE_15M#15min | 148 | -0.020 | -12.36€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 62 | -0.031 | -7.97€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 62 | -0.031 | -7.97€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 10 | +0.000 | -0.13€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 10 | +0.000 | -0.13€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 13 | +0.065 | +2.23€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 13 | +0.065 | +2.23€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP | 63 | -0.038 | -6.49€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 63 | -0.038 | -6.49€ | 0 | 0 |
| ✅ STREAK_FADE_5M | 1097 | -0.025 | -55.62€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 1097 | -0.025 | -55.62€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 390 | -0.025 | -16.23€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 390 | -0.025 | -16.23€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 380 | -0.008 | -11.13€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 380 | -0.008 | -11.13€ | 3 | 0 |
| ✅ STREAK_FADE_5M#SOL | 132 | -0.037 | -12.47€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 132 | -0.037 | -12.47€ | 2 | 0 |
| ✅ STREAK_FADE_5M#XRP | 195 | -0.048 | -15.79€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 195 | -0.048 | -15.79€ | 4 | 0 |
| ✅ STREAK_FADE_60M | 29 | -0.081 | -3.00€ | 0 | 0 |
| ✅ STREAK_FADE_60M#60min | 29 | -0.081 | -3.00€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 18 | -0.135 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 18 | -0.135 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 11 | +0.021 | +0.31€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 11 | +0.021 | +0.31€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 2208 | +0.034 | +58.76€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 2208 | +0.034 | +58.76€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 733 | +0.036 | +16.62€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 733 | +0.036 | +16.62€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 403 | +0.024 | +6.35€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 403 | +0.024 | +6.35€ | 1 | 1 |
| ✅ STREAK_MOM_5M#SOL | 659 | +0.039 | +16.57€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 659 | +0.039 | +16.57€ | 1 | 2 |
| ✅ STREAK_MOM_5M#XRP | 413 | +0.035 | +19.24€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 413 | +0.035 | +19.24€ | 2 | 1 |
| ✅ STRUCT_NO_15M | 3120 | +0.008 | -29.41€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 3120 | +0.008 | -29.41€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 1205 | +0.010 | -9.73€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 1205 | +0.010 | -9.73€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 1211 | +0.017 | -0.82€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 1211 | +0.017 | -0.82€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 704 | -0.011 | -18.86€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 704 | -0.011 | -18.86€ | 2 | 0 |
| ✅ UPDOWN_GBM | 6086 | +0.006 | +152.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 2254 | +0.046 | +229.59€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 254 | +0.016 | +2.17€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 3150 | -0.018 | -69.45€ | 2 | 0 |
| ✅ UPDOWN_GBM#60min | 381 | -0.017 | -9.76€ | 3 | 0 |
| ✅ UPDOWN_GBM#BNB | 195 | +0.094 | +38.97€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 179 | +0.119 | +42.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 7 | -0.019 | -0.50€ | 0 | 0 |
| 🚫 UPDOWN_GBM#BNB#5min | 9 | -0.102 | -2.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 1339 | +0.017 | +58.97€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 222 | +0.071 | +29.44€ | 3 | 11 |
| ✅ UPDOWN_GBM#BTC#240min | 73 | +0.073 | +6.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 902 | +0.010 | +27.97€ | 4 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 124 | -0.040 | -7.15€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 769 | -0.004 | +0.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 122 | +0.105 | +29.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 9 | +0.021 | +0.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 638 | -0.027 | -29.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 1425 | +0.006 | +12.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 649 | +0.030 | +27.88€ | 1 | 6 |
| ✅ UPDOWN_GBM#ETH#240min | 74 | +0.079 | +5.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 521 | -0.028 | -21.16€ | 3 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 166 | +0.006 | -0.16€ | 0 | 1 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 1485 | -0.012 | -23.78€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 521 | -0.001 | -2.47€ | 1 | 2 |
| ✅ UPDOWN_GBM#SOL#240min | 59 | -0.041 | -4.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 802 | -0.012 | -13.81€ | 2 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 91 | -0.027 | -2.45€ | 1 | 3 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 871 | +0.009 | +67.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 561 | +0.061 | +103.12€ | 0 | 6 |
| ✅ UPDOWN_GBM#XRP#240min | 32 | -0.147 | -5.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 278 | -0.079 | -30.10€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 198 | +0.315 | +39.12€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 198 | +0.315 | +39.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 112 | +0.289 | +10.72€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 112 | +0.289 | +10.72€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 86 | +0.341 | +28.40€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 86 | +0.341 | +28.40€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 3827 | -0.073 | +838.85€ | 3 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 3827 | -0.073 | +838.85€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 303 | -0.051 | +341.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 303 | -0.051 | +341.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 787 | -0.162 | -85.37€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 787 | -0.162 | -85.37€ | 4 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 77 | +0.070 | +14.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 77 | +0.070 | +14.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 296 | +0.138 | +143.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 296 | +0.138 | +143.77€ | 2 | 17 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 1217 | -0.072 | +213.27€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 1217 | -0.072 | +213.27€ | 3 | 1 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 1147 | -0.084 | +211.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 1147 | -0.084 | +211.38€ | 4 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 30 | +0.000 | -1.64€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 30 | +0.000 | -1.64€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 30 | +0.000 | -1.64€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 30 | +0.000 | -1.64€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 308 | +0.281 | +228.57€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 308 | +0.281 | +228.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 173 | +0.260 | +111.83€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 173 | +0.260 | +111.83€ | 0 | 12 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 135 | +0.303 | +116.75€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 135 | +0.303 | +116.75€ | 0 | 13 |
| ✅ UPDOWN_OU_5M | 456 | -0.074 | -39.36€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 456 | -0.074 | -39.36€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 261 | -0.044 | -22.10€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 261 | -0.044 | -22.10€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 63 | +0.038 | +6.34€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 63 | +0.038 | +6.34€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 30 | -0.188 | -6.21€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 30 | -0.188 | -6.21€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 35 | -0.149 | -4.81€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 35 | -0.149 | -4.81€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 36 | -0.184 | -5.77€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 36 | -0.184 | -5.77€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 31 | -0.197 | -6.80€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 31 | -0.197 | -6.80€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 1070 | +0.286 | +432.37€ | 0 | 5 |
| ✅ WEEKLY_PRICE#BTC | 319 | +0.201 | -2.54€ | 0 | 2 |
| ✅ WEEKLY_PRICE#ETH | 333 | +0.258 | +73.24€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 418 | +0.371 | +361.66€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.086) — sin ventaja clara. oversold(IBS<0.3): IC=+0.012 n=2157 | neutral: IC=+0.002 n=2297 | overbought(IBS>0.7): IC=+0.088 n=2391
  - _Datos_: n=7158 IC=+0.035 PNL=+639.87€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: (cache 547s) 21 celda(s) GATE OK de 2077 trackeadas

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=-0.001 < 0.08 — monitorear
  - _Datos_: n=521 IC=-0.001 PNL=-2.47€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=333/15 IC=+0.258 PNL=+73.24€ | BTC: n=319/15 IC=+0.201 PNL=-2.54€ | SOL: n=418/15 IC=+0.371 PNL=+361.66€

**🟡 H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.076 n=97678 | tras_1loss IC=+0.045 n=75973 | tras_2loss IC=+0.008 n=34531/40 | gap=+0.068 (umbral 0.05)

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 19 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC, UPDOWN_GBM#SOL
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
  - _Estado_: 6024 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.128 n=41/60 | contraria IC=-0.020 n=23 | gap=+0.148 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=59, boost estimado=+0.020. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 46/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=166/40 IC=+0.006 PNL=-0.16€ | BTC#60min: n=124/40 IC=-0.040 PNL=-7.15€ | SOL#60min: n=91/40 IC=-0.027 PNL=-2.45€

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=-0.013 n=651 | contrario_BTC IC=-0.013 n=476/40 | gap=+0.000 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.180 > 0.08 con n=73 PNL=+42.34€
  - _Datos_: n=73 IC=+0.180 PNL=+42.34€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.135 > 0.08 con n=94 PNL=+25.23€
  - _Datos_: n=94 IC=+0.135 PNL=+25.23€

**⏳ H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: 25
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: 11/25 ops en el filtro definido (IC actual=+0.190 PNL=+11.09€)
  - _Datos_: n=11 IC=+0.190 PNL=+11.09€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.332 > 0.1 con n=909 PNL=+438.10€
  - _Datos_: n=909 IC=+0.332 PNL=+438.10€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=53 IC=+0.045 PNL=+11.43€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=53 IC=+0.045 PNL=+11.43€

**⏳ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: 30
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: 15/30 ops en el filtro definido (IC actual=+0.110 PNL=+5.52€)
  - _Datos_: n=15 IC=+0.110 PNL=+5.52€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=5839 IC=+0.002 PNL=+102.37€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=5839 IC=+0.002 PNL=+102.37€

**⏳ H-CUSTOM-OF-02H-BTCSOL** — ORDER_FLOW H=02h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 02h está en el blacklist basado en TODOS los pares. Con BTC+SOL solo, el historial muestra 4/5 (80%) IC=+0.054. ¿Se confirma la señal positiva con más datos?
  - _Umbral_: 15
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 02h del blacklist ORDER_FLOW
  - _Estado_: 1/15 ops en el filtro definido (IC actual=+0.008 PNL=+1.22€)
  - _Datos_: n=1 IC=+0.008 PNL=+1.22€

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
  - _Estado_: n=315 IC=+0.005 PNL=-0.79€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=315 IC=+0.005 PNL=-0.79€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=66 IC=-0.118 PNL=-8.97€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=66 IC=-0.118 PNL=-8.97€

**🔴 H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.102 < -0.08 con n=101 PNL=-10.33€
  - _Datos_: n=101 IC=-0.102 PNL=-10.33€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.115 > 0.1 con n=509 PNL=+114.18€
  - _Datos_: n=509 IC=+0.115 PNL=+114.18€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=174 IC=+0.074 PNL=+39.40€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=174 IC=+0.074 PNL=+39.40€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=222 IC=+0.071 PNL=+29.44€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=222 IC=+0.071 PNL=+29.44€

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
  - _Estado_: n=1307 IC=+0.030 PNL=+84.16€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1307 IC=+0.030 PNL=+84.16€

**⏳ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: 22/30 ops en el filtro definido (IC actual=-0.208 PNL=-4.06€)
  - _Datos_: n=22 IC=-0.208 PNL=-4.06€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=71 IC=-0.007 PNL=+9.84€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=71 IC=-0.007 PNL=+9.84€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=88 IC=+0.022 PNL=+6.19€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=88 IC=+0.022 PNL=+6.19€

**⏳ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: 15
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: 5/15 ops en el filtro definido (IC actual=+0.018 PNL=+0.47€)
  - _Datos_: n=5 IC=+0.018 PNL=+0.47€

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=2164 IC=-0.017 PNL=-46.20€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2164 IC=-0.017 PNL=-46.20€

**🟡 H-FUNDING-NEGATIVE-BUYYES** — Funding rate negativo (<-0.01%/8h) → BUY_YES tiene más edge (short squeeze)
  - _Hipótesis_: Cuando funding < -0.01%/8h, los shorts están pagando por mantener la posición. Históricamente precede squeezes en cripto. Hipótesis: BUY_YES GBM tiene IC superior en régimen de funding negativo.
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si se confirma → boost ×1.1 en BUY_YES cuando funding_rate_8h < -0.01
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.214 > 0.08 con n=33 PNL=+9.78€
  - _Datos_: n=33 IC=+0.214 PNL=+9.78€

**⏳ H-LATE-WINDOW-5MIN** — Late-window BTC 5min — arbitraje timing vs Polymarket
  - _Hipótesis_: Inspirado en VyvanseWithMarijuana (36.5% ROI, $42k vol). A T+160-270s dentro de una ventana BTC 5min, si BTC ya se movió >0.3%, Polymarket no ha actualizado precio → edge estructural. Estrategia LATE_WINDOW_5MIN en shadow hasta n≥30. FIX 2026-07-02: la estrategia llevaba 0 predicciones desde su creacion porque HORIZONTE_MIN_HORAS=0.05 (3min) descartaba todo mercado a <3min de expirar — y su zona de entrada (160-270s de una ventana de 5min) deja 30-140s restantes, siempre bajo el suelo. Corregido en shadow_predict (zona late-window marcada _solo_late, 30s-3min, solo evaluada por esta estrategia). El reloj de acumulacion empieza de verdad hoy. Contexto extra: el estudio de ballenas de hoy confirma que comprar el lado ganador a mitad/final de ventana es el playbook comun de los 3 mayores ganadores verificados de estos mercados (Bonereaper +$19.9k/mes, wowitsamazing +$10k/mes, zhangfan151 +$8.7k/mes).
  - _Umbral_: 30
  - _Acción_: Si IC≥0.08 con n≥30 → proponer pasar a live con stake mínimo (0.50€). Si IC<0 con n≥30 → el lag de Polymarket en BTC es insuficiente.
  - _Estado_: 14/30 ops en el filtro definido (IC actual=+0.175 PNL=+4.14€)
  - _Datos_: n=14 IC=+0.175 PNL=+4.14€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=1621 IC=+0.026 PNL=+106.43€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1621 IC=+0.026 PNL=+106.43€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=440 IC=+0.032 PNL=-1.19€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=440 IC=+0.032 PNL=-1.19€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.088 > 0.08 con n=95 PNL=+18.02€
  - _Datos_: n=95 IC=+0.088 PNL=+18.02€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.147 > 0.08 con n=117 PNL=+2.60€
  - _Datos_: n=117 IC=+0.147 PNL=+2.60€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.112 > 0.08 con n=114 PNL=+33.20€
  - _Datos_: n=114 IC=+0.112 PNL=+33.20€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=11025 IC=+0.099 PNL=+3101.56€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=11025 IC=+0.099 PNL=+3101.56€

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
  - _Estado_: n=816 IC=+0.028 PNL=+48.67€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=816 IC=+0.028 PNL=+48.67€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.128 > 0.02 con n=216 PNL=+65.90€
  - _Datos_: n=216 IC=+0.128 PNL=+65.90€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=94 IC=-0.094 PNL=+19.83€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=94 IC=-0.094 PNL=+19.83€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.440 > 0.1 con n=581 PNL=+479.95€
  - _Datos_: n=581 IC=+0.440 PNL=+479.95€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=1498 IC=+0.023 PNL=+76.68€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=1498 IC=+0.023 PNL=+76.68€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.166 > 0.1 con n=770 PNL=+280.85€
  - _Datos_: n=770 IC=+0.166 PNL=+280.85€

**⏳ H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: 40
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: 24/40 ops en el filtro definido (IC actual=-0.269 PNL=-5.91€)
  - _Datos_: n=24 IC=-0.269 PNL=-5.91€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=427 IC=+0.050 PNL=+61.80€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=427 IC=+0.050 PNL=+61.80€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=30 IC=-0.188 PNL=+2.99€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=30 IC=-0.188 PNL=+2.99€

**〰️ H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: n=62 IC=+0.047 PNL=-6.40€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=62 IC=+0.047 PNL=-6.40€

**⏳ H-CUSTOM-ETH15-BUYNO-PRECIO-ALTO** — ETH#15min BUY_NO con precio_yes>0.55 pierde (NO longshot contra favorito)
  - _Hipótesis_: Detectado 2026-07-02: ult.60 shadow ETH15 BUY_NO — py_mkt~0.5 wr=0.67 PNL=+29.3 (n=49); py_mkt 0.6-0.8 wr 0.33-0 PNL=-5.75 (n=9). Filtro RETURN NONE (no SKIP) aplicado en shadow_predict.py (PY_MKT_MAX_BUY_NO_ETH15=0.55) el mismo dia -- bloquea la GENERACIÓN de la fila, no solo la decisión. Esta hipotesis trackea la zona filtrada: si las ops que HABRIAN caido aqui siguen apareciendo en otras estrategias o el IC forward de la zona se vuelve positivo, revisar el filtro. CAVEAT: n=9, muestra chica — el filtro se aplico por asimetria de riesgo (afecta a dinero live), no por significancia. ⚠️ 05-Ago (fix): la clave del filtro decía 'py_mkt', que NUNCA existió ni en features de UPDOWN_GBM (T_h/delta_ratio_macro/drift_15min/drift_60min/pct_spot_vs_ref/sigma_h) ni como columna top-level de results.csv -- corregida a 'precio_yes_mercado' (columna real). Aun así, con la clave correcta esta hipótesis NUNCA podrá acumular n mientras el filtro RETURN NONE siga activo -- es el mismo patrón 'frozen by design' que H-CUSTOM-LATE15-PHOTO-FINISH (más abajo): la propia protección impide generar los datos necesarios para volver a evaluarla. Para monitorearla de verdad haría falta un logger separado que capture la señal SIN aplicar el filtro (mismo patrón que gate_bucket_propio con data/markets histórico) -- no construido, pendiente decisión.
  - _Umbral_: 20
  - _Acción_: Si IC forward de la zona >0 con n>=20 → retirar filtro; si confirma negativo → considerar extender a BTC/SOL 15min
  - _Estado_: 0/20 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: PY_MKT_MAX_BUY_NO_ETH15=0.55 en shadow_predict.py hace RETURN NONE (bloquea generación, no solo decisión) -- nunca podrá acumular n mientras siga activo. Haría falta un logger separado sin el filtro para monitorear de verdad (no construido, 26-Ago)

**〰️ H-PRECIO-YES-BARATO** — BUY_YES con precio de mercado 0.30-0.40 — mercado infravalora YES
  - _Hipótesis_: Detectado 2026-07-03 en benchmark de calibración del mercado (7d, estrategias GBM): en el bucket precio_yes_mercado [0.3-0.4) la frecuencia real de YES fue 0.45 vs 0.35 implícito (+0.10, n=38). Posible sesgo favorito-longshot suave en binarios de 15min (complemento del LONGSHOT ya activo para BUY_NO con py<0.20). Si se confirma, BUY_YES comprado en esa banda lleva viento de cola estructural del propio mercado, independiente del modelo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → kelly_boost ×1.1 para BUY_YES con precio_yes_mercado en [0.30,0.40), simétrico al longshot BUY_NO existente
  - _Estado_: n=4389 IC=-0.140 PNL=+215.65€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4389 IC=-0.140 PNL=+215.65€

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
  - _Estado_: n=584 IC=+0.140 PNL=+235.72€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=584 IC=+0.140 PNL=+235.72€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.115 > 0.08 con n=509 PNL=+114.18€
  - _Datos_: n=509 IC=+0.115 PNL=+114.18€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=624 IC=+0.002 PNL=+5.20€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=624 IC=+0.002 PNL=+5.20€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.091 > 0.08 con n=617 PNL=+338.09€
  - _Datos_: n=617 IC=+0.091 PNL=+338.09€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.148 > 0.08 con n=143 PNL=+36.78€
  - _Datos_: n=143 IC=+0.148 PNL=+36.78€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.231 < -0.1 con n=477 PNL=-49.72€
  - _Datos_: n=477 IC=-0.231 PNL=-49.72€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=1158 IC=+0.137 PNL=+586.36€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=1158 IC=+0.137 PNL=+586.36€

**⏳ H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: 40
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: 23/40 ops en el filtro definido (IC actual=+0.060 PNL=+2.13€)
  - _Datos_: n=23 IC=+0.060 PNL=+2.13€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=646 IC=-0.023 PNL=+44.34€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=646 IC=-0.023 PNL=+44.34€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.177 > 0.08 con n=553 PNL=+322.51€
  - _Datos_: n=553 IC=+0.177 PNL=+322.51€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=981 IC=-0.045 PNL=+173.24€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=981 IC=-0.045 PNL=+173.24€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.121 > 0.08 con n=246 PNL=-28.55€
  - _Datos_: n=246 IC=+0.121 PNL=-28.55€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.242 > 0.08 con n=1408 PNL=-121.04€
  - _Datos_: n=1408 IC=+0.242 PNL=-121.04€

**⏳ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: 10/40 ops en el filtro definido (IC actual=+0.000 PNL=+2.51€)
  - _Datos_: n=10 IC=+0.000 PNL=+2.51€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.128 n=162) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=162 IC=+0.128 PNL=+51.70€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.347 > 0.08 con n=70 PNL=+49.38€
  - _Datos_: n=70 IC=+0.347 PNL=+49.38€

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.433 n=223) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=223 IC=+0.433 PNL=+302.61€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=3014 IC=+0.125 PNL=-559.34€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=3014 IC=+0.125 PNL=-559.34€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.174 > 0.1 con n=41 PNL=+21.67€
  - _Datos_: n=41 IC=+0.174 PNL=+21.67€
