# Hipótesis automáticas — 2026-08-27 17:27 UTC
_Generado por shadow_postmortem.py sobre 177124 resoluciones (PNL=+12854.38€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.705` → IC=-0.167 (n=88)

  - _Acción_: SKIP cuando `py_entrada` < 0.705
  - _Potencial_: sin este filtro IC_bueno=+0.270 (n=237)

- **PATRÓN** `py_entrada` > `0.725` → IC=+0.281 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.725 (IC base=+0.151)

- **PATRÓN** `n_ballena_banda` > `20.0` → IC=+0.165 (n=225)

  - _Acción_: Kelly boost +0.83€ cuando `n_ballena_banda` > 20.0 (IC base=+0.151)

- **PATRÓN** `n_total_lado` > `59.0` → IC=+0.233 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 59.0 (IC base=+0.151)

- **PATRÓN** `banda_hit_calibrado` > `0.8218` → IC=+0.261 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8218 (IC base=+0.151)

- **PATRÓN** `banda_z` > `9.867` → IC=+0.243 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.867 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.182 (n=168)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 11.0 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.151 (n=233)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 16.0 (IC base=+0.151)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.177 (n=255)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.01 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `3140.839` → IC=+0.234 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3140.839 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `288.0` → IC=+0.289 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 288.0 (IC base=+0.151)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.136 (n=215)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.5 (IC base=+0.011)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.73` → IC=+0.278 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.190)

- **PATRÓN** `n_ballena_banda` > `23.0` → IC=+0.203 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `n_ballena_banda` > 23.0 (IC base=+0.190)

- **PATRÓN** `n_total_lado` > `57.0` → IC=+0.248 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 57.0 (IC base=+0.190)

- **PATRÓN** `banda_hit_calibrado` > `0.8213` → IC=+0.270 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8213 (IC base=+0.190)

- **PATRÓN** `banda_z` > `11.921` → IC=+0.282 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.921 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.219 (n=144)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.192 (n=115)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 12.0 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.201 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `3861.4687` → IC=+0.257 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3861.4687 (IC base=+0.190)

- **PATRÓN** `ballena_activa_n` < `295.0` → IC=+0.300 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 295.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.126 (n=113)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.495 (IC base=+0.000)

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
- **FILTRO** `restante_s_al_confirmar` < `147.55` → IC=-0.286 (n=2473)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 147.55
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=7422)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `135.71` → IC=-0.245 (n=308)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 135.71
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=926)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` > `632.83` → IC=-0.185 (n=239)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` > 632.83
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=466)

- **FILTRO** `restante_s_al_confirmar` < `395.99` → IC=-0.258 (n=176)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 395.99
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=529)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `100.84` → IC=-0.421 (n=314)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 100.84
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=943)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `160.91` → IC=-0.179 (n=670)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 160.91
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=2010)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `154.0` → IC=-0.268 (n=575)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 154.0
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=1728)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `119.52` → IC=-0.377 (n=429)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 119.52
  - _Potencial_: sin este filtro IC_bueno=-0.118 (n=1287)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.7` → IC=+0.190 (n=5543)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.7 (IC base=+0.099)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.171 (n=1599)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.01 (IC base=+0.099)

- **PATRÓN** `libro_liquidez` > `2375.6867` → IC=+0.174 (n=1545)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2375.6867 (IC base=+0.099)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.144 (n=3649)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 17.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.157 (n=4359)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 7.0 (IC base=+0.141)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.258 (n=3418)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.188 (n=2982)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.02 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `1878.2911` → IC=+0.180 (n=2496)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 1878.2911 (IC base=+0.141)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.224 (n=650)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.208)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.396 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.208)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.210 (n=798)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `12924.6533` → IC=+0.220 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12924.6533 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.195 (n=589)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 7.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.190 (n=450)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 11.0 (IC base=+0.184)

- **PATRÓN** `py_entrada` < `0.365` → IC=+0.255 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.365 (IC base=+0.184)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.184 (n=839)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.01 (IC base=+0.184)

- **PATRÓN** `libro_liquidez` > `12473.6532` → IC=+0.217 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12473.6532 (IC base=+0.184)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.131 (n=546)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.136 (n=470)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 15.0 (IC base=+0.119)

- **PATRÓN** `py_entrada` > `0.555` → IC=+0.136 (n=542)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` > 0.555 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `4886.5239` → IC=+0.162 (n=205)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 4886.5239 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.192 (n=186)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 7.0 (IC base=+0.134)

- **PATRÓN** `py_entrada` < `0.415` → IC=+0.179 (n=303)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.415 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `4198.5556` → IC=+0.152 (n=285)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4198.5556 (IC base=+0.134)

### FAVORITO_CONFIRMADO#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.135 (n=1238)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.127 (n=1057)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 15.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` > `0.69` → IC=+0.309 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.286 (n=316)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.278)

- **PATRÓN** `py_entrada` < `0.195` → IC=+0.410 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.195 (IC base=+0.278)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.277 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `2932.4561` → IC=+0.289 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2932.4561 (IC base=+0.278)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.157 (n=284)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 15.0 (IC base=+0.138)

- **PATRÓN** `py_entrada` > `0.655` → IC=+0.252 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.655 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.147 (n=392)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.02 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `1959.2014` → IC=+0.158 (n=320)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 1959.2014 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `4420.281` → IC=+0.157 (n=141)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 4420.281 (IC base=+0.076)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.203 (n=934)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.198 (n=825)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 15.0 (IC base=+0.194)

- **PATRÓN** `py_entrada` > `0.84` → IC=+0.445 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.84 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.252 (n=212)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` < `0.205` → IC=+0.355 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.205 (IC base=+0.219)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.230 (n=571)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.219)

- **PATRÓN** `libro_liquidez` > `2076.1538` → IC=+0.237 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2076.1538 (IC base=+0.219)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.216 (n=93)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.343 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.239 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.189)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.214 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.101)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.144 (n=273)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.02 (IC base=+0.101)

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

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.194 (n=4601)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.191 (n=3941)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.187)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.201 (n=2194)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.187)

- **PATRÓN** `libro_liquidez` > `3258.7888` → IC=+0.357 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3258.7888 (IC base=+0.187)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.173 (n=793)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 11.0 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.179 (n=1011)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.184 (n=1126)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` < 0.73 (IC base=+0.168)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.230 (n=61)

- **FILTRO** `py_entrada` > `0.795` → IC=-0.397 (n=27)

  - _Acción_: SKIP cuando `py_entrada` > 0.795
  - _Potencial_: sin este filtro IC_bueno=-0.212 (n=57)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.406 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.332)

- **PATRÓN** `py_entrada` > `0.775` → IC=+0.353 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.775 (IC base=+0.332)

- **PATRÓN** `libro_liquidez` > `2916.5858` → IC=+0.343 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2916.5858 (IC base=+0.332)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.171 (n=1113)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 6.0 (IC base=+0.163)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.169 (n=995)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 15.0 (IC base=+0.163)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.169 (n=421)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` < 0.7 (IC base=+0.163)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.170 (n=783)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.72 (IC base=+0.163)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.240 (n=1049)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.228)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.229 (n=897)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.228)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.318 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.228)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.195 (n=1128)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.184 (n=973)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 15.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.200 (n=564)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.7 (IC base=+0.183)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.455 (n=218)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.444)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.443 (n=210)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.444)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.448 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.444)

- **PATRÓN** `libro_liquidez` > `3363.9486` → IC=+0.461 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3363.9486 (IC base=+0.444)

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
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.442 (n=50)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.447)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.451 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.447)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.450 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.447)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.441 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.447)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.197 (n=11349)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 8.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.221 (n=9006)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.192)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.132 (n=2304)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 6.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.130 (n=1657)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 12.0 (IC base=+0.127)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.155 (n=1763)

  - _Acción_: Kelly boost +0.78€ cuando `py_entrada` > 0.71 (IC base=+0.127)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.245 (n=1971)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.237)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.286 (n=1126)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.237)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.182 (n=813)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 17.0 (IC base=+0.166)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.167 (n=1539)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 12.0 (IC base=+0.166)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.214 (n=750)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.166)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.244 (n=996)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.230)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.290 (n=704)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.230)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.229 (n=770)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.245 (n=1225)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.218)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.196 (n=797)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 17.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.192 (n=1516)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 12.0 (IC base=+0.186)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.212 (n=1546)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.186)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.200 (n=1665)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.133)

- **PATRÓN** `restante_min` < `3.96` → IC=+0.135 (n=1531)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` < 3.96 (IC base=+0.133)

- **PATRÓN** `restante_min` > `4.93` → IC=+0.162 (n=1546)

  - _Acción_: Kelly boost +0.81€ cuando `restante_min` > 4.93 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.150 (n=2243)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 8.0 (IC base=+0.133)

- **PATRÓN** `lag_apertura_s` < `4.43` → IC=+0.159 (n=1519)

  - _Acción_: Kelly boost +0.80€ cuando `lag_apertura_s` < 4.43 (IC base=+0.133)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.204 (n=835)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.139)

- **PATRÓN** `restante_min` < `4.29` → IC=+0.140 (n=1000)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` < 4.29 (IC base=+0.139)

- **PATRÓN** `restante_min` > `4.91` → IC=+0.166 (n=795)

  - _Acción_: Kelly boost +0.83€ cuando `restante_min` > 4.91 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.153 (n=2013)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 15.0 (IC base=+0.139)

- **PATRÓN** `lag_apertura_s` < `5.48` → IC=+0.166 (n=756)

  - _Acción_: Kelly boost +0.83€ cuando `lag_apertura_s` < 5.48 (IC base=+0.139)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=830)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.126)

- **PATRÓN** `restante_min` < `4.02` → IC=+0.126 (n=768)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.02 (IC base=+0.126)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.163 (n=821)

  - _Acción_: Kelly boost +0.82€ cuando `restante_min` > 4.94 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.127 (n=2399)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 5.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.138 (n=1133)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 8.0 (IC base=+0.126)

- **PATRÓN** `lag_apertura_s` < `3.48` → IC=+0.166 (n=764)

  - _Acción_: Kelly boost +0.83€ cuando `lag_apertura_s` < 3.48 (IC base=+0.126)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.317 (n=419)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.302)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.305 (n=527)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.302)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.377 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.8 (IC base=+0.302)

- **PATRÓN** `libro_liquidez` > `3861.5788` → IC=+0.304 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3861.5788 (IC base=+0.302)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.304 (n=223)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.284)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.288 (n=229)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.284)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.360 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.285 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `5623.4735` → IC=+0.324 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5623.4735 (IC base=+0.284)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.337 (n=194)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.303)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.313 (n=281)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.303)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.389 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.303)

- **PATRÓN** `libro_liquidez` > `2046.5008` → IC=+0.326 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2046.5008 (IC base=+0.303)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.379 (n=56)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.352)

- **PATRÓN** `py_entrada` > `0.88` → IC=+0.431 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.88 (IC base=+0.352)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.364 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.352)

- **PATRÓN** `libro_liquidez` > `763.8012` → IC=+0.371 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 763.8012 (IC base=+0.352)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.424 (n=260)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.415)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.425 (n=251)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.415)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.424 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.415)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.428 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.415)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.414 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.415)

- **PATRÓN** `libro_liquidez` > `2103.8839` → IC=+0.428 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2103.8839 (IC base=+0.415)

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
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.426 (n=106)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.421)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.442 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.421)

- **PATRÓN** `py_entrada` > `0.91` → IC=+0.426 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.91 (IC base=+0.421)

- **PATRÓN** `libro_liquidez` > `1842.491` → IC=+0.442 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1842.491 (IC base=+0.421)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.314 (n=299)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.293)

- **PATRÓN** `py_entrada` > `0.87` → IC=+0.446 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.87 (IC base=+0.293)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.308 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `1676.2618` → IC=+0.348 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1676.2618 (IC base=+0.293)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.314 (n=299)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.293)

- **PATRÓN** `py_entrada` > `0.87` → IC=+0.446 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.87 (IC base=+0.293)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.308 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `1676.2618` → IC=+0.348 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1676.2618 (IC base=+0.293)

### GBM_LATE_15M
- **PATRÓN** `ibs_20min` > `0.9475` → IC=+0.211 (n=772)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9475 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` > `0.1852` → IC=+0.229 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1852 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` < `0.9628` → IC=+0.211 (n=528)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9628 (IC base=+0.066)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.219` → IC=+0.165 (n=935)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 5.219 (IC base=+0.066)

- **PATRÓN** `volumen_regimen` < `0.6324` → IC=+0.211 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6324 (IC base=+0.066)

- **PATRÓN** `volumen_regimen` > `1.0648` → IC=+0.242 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0648 (IC base=+0.066)

- **PATRÓN** `volumen_pendiente_norm` > `0.3067` → IC=+0.154 (n=180)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.3067 (IC base=+0.066)

- **PATRÓN** `volumen_spike_ratio` < `2.4328` → IC=+0.146 (n=1101)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.4328 (IC base=+0.066)

- **PATRÓN** `ibs_20min` < `0.2155` → IC=+0.131 (n=1568)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.2155 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` < `0.2947` → IC=+0.141 (n=795)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.2947 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` < `0.6286` → IC=+0.155 (n=256)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6286 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` > `1.06` → IC=+0.140 (n=348)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 1.06 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.3008` → IC=+0.276 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3008 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` < `1.6226` → IC=+0.184 (n=381)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.6226 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` > `2.9099` → IC=+0.229 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9099 (IC base=+0.029)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.228 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 45.0 (IC base=+0.029)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.180 (n=173)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0075 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.154 (n=345)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 11.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.291 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.83` → IC=+0.322 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.83 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.1485` → IC=+0.137 (n=122)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.1485 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.149 (n=314)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.04 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.278 (n=192)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.259)

- **PATRÓN** `sigma_h` > `0.0074` → IC=+0.283 (n=95)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0074 (IC base=+0.259)

- **PATRÓN** `drift_60min` |x|≤ `0.2372` → IC=+0.290 (n=251)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2372 (IC base=+0.259)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.263 (n=272)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.259)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.277 (n=258)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.259)

- **PATRÓN** `ibs_20min` < `0.4388` → IC=+0.298 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4388 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.934` → IC=+0.298 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.934 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` < `0.0585` → IC=+0.265 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0585 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` > `0.3008` → IC=+0.288 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3008 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` < `1.8169` → IC=+0.264 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8169 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` > `1.5851` → IC=+0.268 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5851 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.313 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1977.88` → IC=+0.304 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1977.88 (IC base=+0.259)

- **PATRÓN** `ballena_activa_n` < `66.0` → IC=+0.254 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 66.0 (IC base=+0.259)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.227 (n=258)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.207)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.233 (n=129)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.0953` → IC=+0.240 (n=129)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0953 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.235 (n=391)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `0.4206` → IC=+0.222 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4206 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `0.211` → IC=+0.233 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.211 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.354` → IC=+0.223 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.354 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` < `1.2788` → IC=+0.214 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2788 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` > `1.0851` → IC=+0.234 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0851 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.2657` → IC=+0.241 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2657 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `1.4455` → IC=+0.259 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4455 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `11309.5324` → IC=+0.221 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11309.5324 (IC base=+0.207)

- **PATRÓN** `ballena_activa_n` < `309.0` → IC=+0.203 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 309.0 (IC base=+0.207)

- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.175 (n=149)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0022 (IC base=+0.138)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.139 (n=203)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` > 0.0046 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.0744` → IC=+0.162 (n=149)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.0744 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.148 (n=419)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 7.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.145 (n=452)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 17.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.44` → IC=+0.173 (n=393)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.44 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.1358` → IC=+0.163 (n=378)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1358 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.938` → IC=+0.227 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.938 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.6283` → IC=+0.189 (n=149)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.6283 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `1.0251` → IC=+0.139 (n=203)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 1.0251 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.0931` → IC=+0.213 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0931 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.7452` → IC=+0.180 (n=229)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.7452 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.4117` → IC=+0.158 (n=343)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.4117 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=576)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `13543.6787` → IC=+0.178 (n=203)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 13543.6787 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `221.0` → IC=+0.190 (n=85)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 221.0 (IC base=+0.138)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `hora_utc` < `6.0` → IC=+0.213 (n=165)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.278 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.923` → IC=+0.258 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.923 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` < `0.1063` → IC=+0.126 (n=343)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1063 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.4138` → IC=+0.144 (n=57)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.4138 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.165 (n=407)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.04 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `1914.6584` → IC=+0.146 (n=210)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 1914.6584 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.154 (n=50)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 16.0 (IC base=+0.138)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.297 (n=151)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.256)

- **PATRÓN** `drift_60min` |x|≤ `0.1286` → IC=+0.292 (n=152)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1286 (IC base=+0.256)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.273 (n=231)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.256)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.279 (n=134)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.256)

- **PATRÓN** `ibs_20min` < `0.5391` → IC=+0.291 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5391 (IC base=+0.256)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.047` → IC=+0.292 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.047 (IC base=+0.256)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.743` → IC=+0.259 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.743 (IC base=+0.256)

- **PATRÓN** `volumen_pendiente_norm` > `0.4009` → IC=+0.441 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.4009 (IC base=+0.256)

- **PATRÓN** `volumen_spike_ratio` > `2.6935` → IC=+0.245 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6935 (IC base=+0.256)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.285 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.256)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.229 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 49.0 (IC base=+0.256)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `ibs_20min` > `0.8686` → IC=-0.154 (n=203)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8686
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=614)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.172 (n=65)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=752)

- **PATRÓN** `dist_vwap_pct` > `0.124` → IC=+0.333 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.124 (IC base=-0.034)

- **PATRÓN** `dist_vwap_pct` < `0.0838` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0838 (IC base=-0.034)

- **PATRÓN** `volumen_regimen` < `1.0858` → IC=+0.306 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0858 (IC base=-0.034)

- **PATRÓN** `volumen_regimen` > `0.7026` → IC=+0.311 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7026 (IC base=-0.034)

- **PATRÓN** `volumen_pendiente_norm` > `0.0976` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0976 (IC base=-0.034)

- **PATRÓN** `volumen_spike_ratio` < `1.4376` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4376 (IC base=-0.034)

- **PATRÓN** `volumen_spike_ratio` > `2.1718` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1718 (IC base=-0.034)

- **PATRÓN** `dist_vwap_pct` > `0.1494` → IC=+0.176 (n=32)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.1494 (IC base=-0.051)

- **PATRÓN** `volumen_pendiente_norm` > `0.0733` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0733 (IC base=-0.051)

- **PATRÓN** `volumen_spike_ratio` > `2.3707` → IC=+0.204 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3707 (IC base=-0.051)

- **PATRÓN** `ballena_activa_n` < `138.0` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 138.0 (IC base=-0.051)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `sigma_h` > `0.0102` → IC=-0.159 (n=329)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0102
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=988)

- **FILTRO** `sigma_ewma_delta_pct` > `4.949` → IC=-0.154 (n=278)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.949
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=1039)

- **FILTRO** `volumen_pendiente_norm` < `0.0964` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.0964
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

- **FILTRO** `volumen_spike_ratio` > `1.6234` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.6234
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.197 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0055 (IC base=+0.048)

- **PATRÓN** `drift_60min` |x|≤ `0.2734` → IC=+0.125 (n=62)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.62€ cuando `drift_60min` |x|≤ 0.2734 (IC base=+0.048)

- **PATRÓN** `ibs_20min` > `0.6842` → IC=+0.204 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6842 (IC base=+0.048)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.44` → IC=-0.166 (n=342)

  - _Acción_: SKIP cuando `ibs_20min` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=345)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.152 (n=133)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=554)

- **FILTRO** `ibs_20min` > `0.7857` → IC=-0.171 (n=296)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7857
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=890)

- **FILTRO** `sigma_ewma_delta_pct` > `6.668` → IC=-0.155 (n=195)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.668
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=991)

- **PATRÓN** `dist_vwap_pct` < `0.2396` → IC=+0.175 (n=38)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.2396 (IC base=-0.091)

- **PATRÓN** `volumen_regimen` > `0.6932` → IC=+0.183 (n=39)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 0.6932 (IC base=-0.091)

- **PATRÓN** `dist_vwap_pct` < `0.2029` → IC=+0.222 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2029 (IC base=-0.038)

- **PATRÓN** `volumen_regimen` < `0.6966` → IC=+0.226 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6966 (IC base=-0.038)

- **PATRÓN** `volumen_regimen` > `1.1355` → IC=+0.250 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1355 (IC base=-0.038)

- **PATRÓN** `volumen_spike_ratio` > `1.9721` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.9721 (IC base=-0.038)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.135 (n=1319)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` > 0.0077 (IC base=+0.055)

- **PATRÓN** `ibs_20min` > `0.9463` → IC=+0.248 (n=970)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9463 (IC base=+0.055)

- **PATRÓN** `dist_vwap_pct` > `1.2805` → IC=+0.292 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2805 (IC base=+0.055)

- **PATRÓN** `volumen_regimen` > `1.1726` → IC=+0.202 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1726 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` < `0.1143` → IC=+0.172 (n=1308)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` < 0.1143 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` > `0.2472` → IC=+0.213 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2472 (IC base=+0.055)

- **PATRÓN** `volumen_spike_ratio` < `1.4768` → IC=+0.201 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4768 (IC base=+0.055)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.274 (n=793)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.055)

- **PATRÓN** `ibs_20min` < `0.0956` → IC=+0.185 (n=1226)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.0956 (IC base=+0.038)

- **PATRÓN** `dist_vwap_pct` > `0.7151` → IC=+0.207 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7151 (IC base=+0.038)

- **PATRÓN** `dist_vwap_pct` < `0.2096` → IC=+0.205 (n=748)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2096 (IC base=+0.038)

- **PATRÓN** `volumen_regimen` > `1.2349` → IC=+0.230 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2349 (IC base=+0.038)

- **PATRÓN** `volumen_pendiente_norm` > `0.2516` → IC=+0.359 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2516 (IC base=+0.038)

- **PATRÓN** `volumen_spike_ratio` > `2.9133` → IC=+0.290 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9133 (IC base=+0.038)

- **PATRÓN** `ballena_activa_n` < `60.0` → IC=+0.256 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 60.0 (IC base=+0.038)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2606` → IC=-0.149 (n=189)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2606
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=385)

- **FILTRO** `sigma_ewma_delta_pct` > `2.105` → IC=-0.171 (n=241)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.105
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=545)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.222` → IC=+0.179 (n=110)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 5.222 (IC base=-0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2014` → IC=+0.382 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2014 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` > `2.5866` → IC=+0.250 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5866 (IC base=-0.004)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.458 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=-0.004)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` > `0.8848` → IC=-0.145 (n=277)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8848
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=834)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `drift_60min` |x|≤ `0.1002` → IC=+0.209 (n=201)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1002 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.255 (n=161)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.294 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.027` → IC=+0.298 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.027 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` < `0.1388` → IC=+0.193 (n=353)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.1388 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.4145` → IC=+0.196 (n=54)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.4145 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` < `1.981` → IC=+0.207 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.981 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` > `3.4682` → IC=+0.180 (n=170)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 3.4682 (IC base=+0.185)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.212 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.185)

- **PATRÓN** `libro_liquidez` > `1946.641` → IC=+0.214 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1946.641 (IC base=+0.185)

- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.356 (n=221)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0081 (IC base=+0.336)

- **PATRÓN** `drift_60min` |x|≤ `0.2365` → IC=+0.353 (n=168)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2365 (IC base=+0.336)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.376 (n=176)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.336)

- **PATRÓN** `ibs_20min` < `0.3388` → IC=+0.353 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3388 (IC base=+0.336)

- **PATRÓN** `ibs_20min` > `0.1351` → IC=+0.334 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1351 (IC base=+0.336)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.502` → IC=+0.346 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.502 (IC base=+0.336)

- **PATRÓN** `volumen_pendiente_norm` > `0.3496` → IC=+0.389 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3496 (IC base=+0.336)

- **PATRÓN** `volumen_spike_ratio` < `1.732` → IC=+0.354 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.732 (IC base=+0.336)

- **PATRÓN** `volumen_spike_ratio` > `1.9885` → IC=+0.332 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9885 (IC base=+0.336)

- **PATRÓN** `libro_liquidez` > `1889.461` → IC=+0.372 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1889.461 (IC base=+0.336)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.303 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.336)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.167 (n=118)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=357)

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

- **FILTRO** `libro_spread` > `0.01` → IC=-0.171 (n=68)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=917)

- **PATRÓN** `dist_vwap_pct` > `0.7343` → IC=+0.233 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7343 (IC base=-0.074)

- **PATRÓN** `volumen_spike_ratio` < `1.4` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4 (IC base=-0.074)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7407` → IC=-0.123 (n=436)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7407
  - _Potencial_: sin este filtro IC_bueno=+0.223 (n=225)

- **FILTRO** `ibs_20min` > `0.75` → IC=-0.189 (n=220)

  - _Acción_: SKIP cuando `ibs_20min` > 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=679)

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

- **PATRÓN** `ibs_20min` > `0.8571` → IC=+0.268 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8571 (IC base=-0.005)

- **PATRÓN** `dist_vwap_pct` > `0.3274` → IC=+0.276 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3274 (IC base=-0.005)

- **PATRÓN** `volumen_regimen` < `0.8598` → IC=+0.195 (n=126)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.8598 (IC base=-0.005)

- **PATRÓN** `volumen_regimen` > `1.1463` → IC=+0.242 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1463 (IC base=-0.005)

- **PATRÓN** `volumen_pendiente_norm` < `0.125` → IC=+0.172 (n=175)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` < 0.125 (IC base=-0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2337` → IC=+0.275 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2337 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` < `1.4704` → IC=+0.205 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4704 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` > `2.0468` → IC=+0.183 (n=80)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.0468 (IC base=-0.005)

- **PATRÓN** `ballena_activa_n` < `62.0` → IC=+0.240 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 62.0 (IC base=-0.005)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0246` → IC=+0.328 (n=190)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0246 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.227 (n=214)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.225 (n=503)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` > `0.9` → IC=+0.301 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9 (IC base=+0.219)

- **PATRÓN** `dist_vwap_pct` > `1.4009` → IC=+0.341 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.4009 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.169` → IC=+0.276 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.169 (IC base=+0.219)

- **PATRÓN** `volumen_regimen` > `0.8384` → IC=+0.254 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8384 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` < `0.0802` → IC=+0.224 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0802 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.2775` → IC=+0.276 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2775 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` < `1.4115` → IC=+0.263 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4115 (IC base=+0.219)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.235 (n=606)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.219)

- **PATRÓN** `libro_liquidez` > `2453.0908` → IC=+0.231 (n=570)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2453.0908 (IC base=+0.219)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.278 (n=196)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.267)

- **PATRÓN** `drift_60min` |x|≤ `0.4891` → IC=+0.271 (n=517)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4891 (IC base=+0.267)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.275 (n=549)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.267)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.267 (n=402)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.267)

- **PATRÓN** `ibs_20min` < `0.125` → IC=+0.348 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.125 (IC base=+0.267)

- **PATRÓN** `dist_vwap_pct` < `0.9073` → IC=+0.275 (n=665)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9073 (IC base=+0.267)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.887` → IC=+0.311 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.887 (IC base=+0.267)

- **PATRÓN** `volumen_regimen` > `1.2589` → IC=+0.303 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2589 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` > `0.2431` → IC=+0.372 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2431 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` > `2.1674` → IC=+0.294 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1674 (IC base=+0.267)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.01` → IC=+0.194 (n=842)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.01 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.0884` → IC=+0.160 (n=842)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.0884 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.182 (n=892)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 17.0 (IC base=+0.157)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.159 (n=943)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 6.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.285 (n=1238)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` > `0.8042` → IC=+0.253 (n=593)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8042 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.334` → IC=+0.247 (n=1053)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.334 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` > `0.6892` → IC=+0.176 (n=1564)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.6892 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` > `0.1004` → IC=+0.184 (n=900)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1004 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `2.2702` → IC=+0.156 (n=2000)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.2702 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` > `1.8503` → IC=+0.150 (n=1515)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.8503 (IC base=+0.157)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.168 (n=2043)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.157)

- **PATRÓN** `libro_liquidez` > `3965.0747` → IC=+0.187 (n=841)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 3965.0747 (IC base=+0.157)

- **PATRÓN** `ballena_activa_n` < `119.0` → IC=+0.180 (n=1259)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 119.0 (IC base=+0.157)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.195 (n=1983)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0075 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.4122` → IC=+0.193 (n=2248)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.4122 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.209 (n=1131)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.4105` → IC=+0.235 (n=2248)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4105 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` < `0.2107` → IC=+0.177 (n=1830)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.2107 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.809` → IC=+0.213 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.809 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `1.1724` → IC=+0.163 (n=1804)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1724 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` > `0.8549` → IC=+0.173 (n=1202)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 0.8549 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2892` → IC=+0.249 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2892 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` < `1.8875` → IC=+0.171 (n=1093)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.8875 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.6551` → IC=+0.206 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6551 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `132.0` → IC=+0.183 (n=1065)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 132.0 (IC base=+0.182)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.205 (n=188)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.2679` → IC=+0.152 (n=412)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.2679 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.208 (n=152)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.308 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.063` → IC=+0.332 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.063 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.1485` → IC=+0.180 (n=98)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.1485 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.4355` → IC=+0.130 (n=333)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.4355 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.160 (n=183)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.03 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.253 (n=180)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.255)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.267 (n=204)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.255)

- **PATRÓN** `drift_60min` |x|≤ `0.2611` → IC=+0.301 (n=179)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2611 (IC base=+0.255)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.276 (n=181)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 13.0 (IC base=+0.255)

- **PATRÓN** `ibs_20min` < `0.4057` → IC=+0.277 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4057 (IC base=+0.255)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.357` → IC=+0.280 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.357 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` < `1.9129` → IC=+0.281 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9129 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` > `2.8655` → IC=+0.296 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8655 (IC base=+0.255)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.332 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.255)

- **PATRÓN** `libro_liquidez` > `1968.0502` → IC=+0.343 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1968.0502 (IC base=+0.255)

- **PATRÓN** `ballena_activa_n` < `82.0` → IC=+0.253 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 82.0 (IC base=+0.255)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.230 (n=120)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.178)

- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.211 (n=119)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0073 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.084` → IC=+0.189 (n=120)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.084 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.205 (n=361)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` > `0.9974` → IC=+0.281 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9974 (IC base=+0.178)

- **PATRÓN** `dist_vwap_pct` > `0.2074` → IC=+0.241 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2074 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.549` → IC=+0.232 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.549 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.515` → IC=+0.178 (n=333)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` < 7.515 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` < `1.2957` → IC=+0.186 (n=358)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 1.2957 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` > `0.8896` → IC=+0.200 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8896 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.2159` → IC=+0.261 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2159 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` < `1.3602` → IC=+0.232 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3602 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `12240.9476` → IC=+0.200 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12240.9476 (IC base=+0.178)

- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.201 (n=152)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0022 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.2201` → IC=+0.175 (n=398)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2201 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.171 (n=414)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 7.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` < `0.4268` → IC=+0.190 (n=453)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.4268 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.1503` → IC=+0.170 (n=446)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.1503 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.387` → IC=+0.233 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.387 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.6405` → IC=+0.232 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6405 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.1709` → IC=+0.220 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1709 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `2.516` → IC=+0.157 (n=345)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.516 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `14438.2519` → IC=+0.154 (n=151)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 14438.2519 (IC base=+0.146)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `drift_60min` |x|≤ `0.1487` → IC=+0.163 (n=241)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.1487 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.169 (n=143)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 16.0 (IC base=+0.156)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.227 (n=141)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.299 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.904` → IC=+0.296 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.904 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` < `0.2288` → IC=+0.147 (n=298)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` < 0.2288 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `1.9884` → IC=+0.211 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9884 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` > `3.6311` → IC=+0.145 (n=136)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 3.6311 (IC base=+0.156)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.207 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `1957.2184` → IC=+0.189 (n=120)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 1957.2184 (IC base=+0.156)

- **PATRÓN** `sigma_h` < `0.0086` → IC=+0.296 (n=214)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0086 (IC base=+0.272)

- **PATRÓN** `drift_60min` |x|≤ `0.3699` → IC=+0.305 (n=213)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3699 (IC base=+0.272)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.311 (n=167)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.272)

- **PATRÓN** `ibs_20min` < `0.3077` → IC=+0.319 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3077 (IC base=+0.272)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.917` → IC=+0.324 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.917 (IC base=+0.272)

- **PATRÓN** `volumen_pendiente_norm` > `0.3746` → IC=+0.431 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3746 (IC base=+0.272)

- **PATRÓN** `volumen_spike_ratio` > `2.0029` → IC=+0.263 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.0029 (IC base=+0.272)

- **PATRÓN** `ballena_activa_n` < `62.0` → IC=+0.236 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 62.0 (IC base=+0.272)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0093` → IC=+0.219 (n=361)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0093 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.0952` → IC=+0.232 (n=121)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0952 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.197 (n=371)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 6.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` > `0.4502` → IC=+0.235 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4502 (IC base=+0.178)

- **PATRÓN** `dist_vwap_pct` > `1.0212` → IC=+0.226 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0212 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.328` → IC=+0.303 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.328 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` > `0.6402` → IC=+0.193 (n=360)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` > 0.6402 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.1005` → IC=+0.234 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1005 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` < `1.4389` → IC=+0.206 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4389 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `2.4658` → IC=+0.220 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4658 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.182 (n=410)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `8700.8274` → IC=+0.203 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8700.8274 (IC base=+0.178)

- **PATRÓN** `ballena_activa_n` < `228.0` → IC=+0.161 (n=296)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 228.0 (IC base=+0.178)

- **PATRÓN** `sigma_h` < `0.0025` → IC=+0.255 (n=145)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0025 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.3806` → IC=+0.162 (n=433)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.3806 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.181 (n=161)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 17.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.151 (n=164)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 5.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.1136` → IC=+0.242 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1136 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` < `0.3304` → IC=+0.161 (n=481)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.3304 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.394` → IC=+0.199 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.394 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.1582` → IC=+0.158 (n=433)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.1582 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` > `0.6146` → IC=+0.161 (n=432)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6146 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.1001` → IC=+0.174 (n=130)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1001 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `1.9018` → IC=+0.180 (n=217)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.9018 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `2.4874` → IC=+0.140 (n=109)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 2.4874 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `10334.4562` → IC=+0.151 (n=144)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 10334.4562 (IC base=+0.144)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **FILTRO** `ibs_20min` > `0.4062` → IC=-0.188 (n=136)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4062
  - _Potencial_: sin este filtro IC_bueno=+0.226 (n=410)

- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.213 (n=228)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0106 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.147 (n=457)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 8.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.8519` → IC=+0.235 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8519 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `1.1346` → IC=+0.291 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1346 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.191` → IC=+0.289 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.191 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.6193` → IC=+0.142 (n=501)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.6193 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` < `0.1612` → IC=+0.134 (n=490)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` < 0.1612 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `2.1351` → IC=+0.124 (n=413)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.1351 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `1.5533` → IC=+0.132 (n=419)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 1.5533 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `3214.2982` → IC=+0.228 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3214.2982 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.176 (n=137)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0049 (IC base=+0.122)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.183 (n=137)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.01 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=142)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.4062` → IC=+0.226 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4062 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` < `0.2188` → IC=+0.139 (n=383)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.2188 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.743` → IC=+0.212 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.743 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.8536` → IC=+0.162 (n=273)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.8536 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.2196` → IC=+0.190 (n=56)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2196 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` > `2.2466` → IC=+0.198 (n=94)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.2466 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `2073.0828` → IC=+0.173 (n=273)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2073.0828 (IC base=+0.122)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0234` → IC=+0.197 (n=242)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0234 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.1645` → IC=+0.188 (n=235)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.1645 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.199 (n=184)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.170 (n=237)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 7.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` > `0.9133` → IC=+0.268 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9133 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` > `1.6506` → IC=+0.268 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.6506 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.097` → IC=+0.248 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.097 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` > `0.8248` → IC=+0.196 (n=356)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` > 0.8248 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.2352` → IC=+0.242 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2352 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `2.146` → IC=+0.181 (n=437)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 2.146 (IC base=+0.168)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.173 (n=564)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `2452.9003` → IC=+0.168 (n=534)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2452.9003 (IC base=+0.168)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.273 (n=170)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.6623` → IC=+0.231 (n=510)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6623 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.224 (n=241)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.253 (n=245)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` < `0.375` → IC=+0.256 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.375 (IC base=+0.218)

- **PATRÓN** `dist_vwap_pct` < `0.2419` → IC=+0.232 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2419 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.181` → IC=+0.281 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.181 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` > `0.7015` → IC=+0.242 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7015 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.28` → IC=+0.341 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.28 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `2.7123` → IC=+0.269 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7123 (IC base=+0.218)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.132 (n=202)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` > 0.0069 (IC base=+0.093)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.190 (n=217)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 16.0 (IC base=+0.093)

- **PATRÓN** `ibs_20min` > `0.6275` → IC=+0.165 (n=398)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.6275 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` > `0.7873` → IC=+0.263 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7873 (IC base=+0.093)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.104` → IC=+0.201 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.104 (IC base=+0.093)

- **PATRÓN** `volumen_pendiente_norm` > `0.1714` → IC=+0.172 (n=117)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1714 (IC base=+0.093)

- **PATRÓN** `libro_liquidez` > `2860.6888` → IC=+0.136 (n=297)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 2860.6888 (IC base=+0.093)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.171 (n=138)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0036 (IC base=+0.077)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.127 (n=199)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 14.0 (IC base=+0.077)

- **PATRÓN** `ibs_20min` < `0.645` → IC=+0.126 (n=410)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` < 0.645 (IC base=+0.077)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.244` → IC=+0.191 (n=134)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 5.244 (IC base=+0.077)

- **PATRÓN** `volumen_regimen` < `0.6471` → IC=+0.134 (n=121)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.6471 (IC base=+0.077)

- **PATRÓN** `volumen_spike_ratio` < `1.8646` → IC=+0.135 (n=236)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.8646 (IC base=+0.077)

- **PATRÓN** `libro_liquidez` > `11100.1618` → IC=+0.140 (n=137)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 11100.1618 (IC base=+0.077)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.123 (n=112)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 40.0 (IC base=+0.077)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.200 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=85)

- **FILTRO** `ibs_20min` < `0.5265` → IC=-0.200 (n=28)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5265
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=85)

- **FILTRO** `libro_liquidez` < `7812.228` → IC=-0.167 (n=37)

  - _Acción_: SKIP cuando `libro_liquidez` < 7812.228
  - _Potencial_: sin este filtro IC_bueno=+0.141 (n=76)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.121 (n=85)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 9.0 (IC base=+0.039)

- **PATRÓN** `ibs_20min` > `0.5265` → IC=+0.121 (n=85)

  - _Acción_: Kelly boost +0.60€ cuando `ibs_20min` > 0.5265 (IC base=+0.039)

- **PATRÓN** `dist_vwap_pct` > `0.7767` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.7767 (IC base=+0.039)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.351` → IC=+0.150 (n=38)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 4.351 (IC base=+0.039)

- **PATRÓN** `libro_liquidez` > `11821.8226` → IC=+0.144 (n=57)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 11821.8226 (IC base=+0.039)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.222 (n=70)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.153)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.203 (n=72)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.3512` → IC=+0.183 (n=159)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.3512 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.161 (n=54)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.190 (n=56)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 4.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.494` → IC=+0.204 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.494 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.3005` → IC=+0.169 (n=158)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.3005 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.323` → IC=+0.318 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.323 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `1.2044` → IC=+0.177 (n=159)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 1.2044 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.0867` → IC=+0.333 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0867 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `1.7117` → IC=+0.206 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7117 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `13545.8692` → IC=+0.157 (n=106)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 13545.8692 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `139.0` → IC=+0.172 (n=56)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 139.0 (IC base=+0.153)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **FILTRO** `drift_60min` |x|> `0.2623` → IC=-0.125 (n=30)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2623
  - _Potencial_: sin este filtro IC_bueno=+0.135 (n=61)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.283 (n=81)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.282)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.309 (n=61)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.282)

- **PATRÓN** `drift_60min` |x|≤ `0.2318` → IC=+0.281 (n=62)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2318 (IC base=+0.282)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.304 (n=95)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.282)

- **PATRÓN** `ibs_20min` > `0.999` → IC=+0.318 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.999 (IC base=+0.282)

- **PATRÓN** `dist_vwap_pct` > `0.1466` → IC=+0.337 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1466 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.561` → IC=+0.380 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.561 (IC base=+0.282)

- **PATRÓN** `volumen_regimen` < `0.701` → IC=+0.384 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.701 (IC base=+0.282)

- **PATRÓN** `volumen_regimen` > `1.0786` → IC=+0.295 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0786 (IC base=+0.282)

- **PATRÓN** `volumen_pendiente_norm` > `0.184` → IC=+0.392 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.184 (IC base=+0.282)

- **PATRÓN** `volumen_spike_ratio` < `2.3129` → IC=+0.297 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3129 (IC base=+0.282)

- **PATRÓN** `volumen_spike_ratio` > `1.5464` → IC=+0.300 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5464 (IC base=+0.282)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.380 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.048)

- **PATRÓN** `drift_60min` |x|≤ `0.2623` → IC=+0.135 (n=61)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.67€ cuando `drift_60min` |x|≤ 0.2623 (IC base=+0.048)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.188 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 11.0 (IC base=+0.048)

- **PATRÓN** `ibs_20min` < `0.645` → IC=+0.148 (n=69)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.645 (IC base=+0.048)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.133` → IC=+0.136 (n=20)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 10.133 (IC base=+0.048)

- **PATRÓN** `volumen_regimen` < `0.7011` → IC=+0.227 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7011 (IC base=+0.048)

- **PATRÓN** `libro_liquidez` > `9336.2451` → IC=+0.260 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9336.2451 (IC base=+0.048)

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
- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.200 (n=1332)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=1107)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.9412` → IC=+0.293 (n=1331)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9412 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `1.0829` → IC=+0.245 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0829 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.357` → IC=+0.247 (n=1220)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.357 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.8785` → IC=+0.147 (n=1385)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.8785 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` > `1.08` → IC=+0.156 (n=942)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 1.08 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.1644` → IC=+0.187 (n=749)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.1644 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.3039` → IC=+0.149 (n=2303)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.3039 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.8572` → IC=+0.160 (n=1745)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.8572 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.156 (n=2379)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `2504.561` → IC=+0.176 (n=1957)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2504.561 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.198 (n=1042)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 71.0 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.220 (n=1757)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.191)

- **PATRÓN** `drift_60min` |x|≤ `0.4726` → IC=+0.202 (n=2635)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4726 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.201 (n=942)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.207 (n=958)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.191)

- **PATRÓN** `ibs_20min` < `0.562` → IC=+0.246 (n=2636)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.562 (IC base=+0.191)

- **PATRÓN** `dist_vwap_pct` < `0.7176` → IC=+0.182 (n=2121)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.7176 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.328` → IC=+0.210 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.328 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.639` → IC=+0.194 (n=2475)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 2.639 (IC base=+0.191)

- **PATRÓN** `volumen_regimen` < `0.6238` → IC=+0.186 (n=657)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.6238 (IC base=+0.191)

- **PATRÓN** `volumen_regimen` > `1.201` → IC=+0.183 (n=657)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.201 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` > `0.2817` → IC=+0.268 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2817 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` > `2.286` → IC=+0.211 (n=878)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.286 (IC base=+0.191)

- **PATRÓN** `ballena_activa_n` < `179.0` → IC=+0.168 (n=1509)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 179.0 (IC base=+0.191)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` > `0.007` → IC=+0.211 (n=216)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.147 (n=482)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 6.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.168 (n=320)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 11.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` > `0.9463` → IC=+0.293 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9463 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.341` → IC=+0.303 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.341 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.2163` → IC=+0.214 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2163 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.9109` → IC=+0.144 (n=262)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.9109 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.190 (n=269)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.04 (IC base=+0.144)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.308 (n=196)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0063 (IC base=+0.268)

- **PATRÓN** `drift_60min` |x|≤ `0.1051` → IC=+0.326 (n=130)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1051 (IC base=+0.268)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.271 (n=278)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.268)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.283 (n=270)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.268)

- **PATRÓN** `ibs_20min` < `0.5819` → IC=+0.318 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5819 (IC base=+0.268)

- **PATRÓN** `volumen_pendiente_norm` < `0.0882` → IC=+0.258 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0882 (IC base=+0.268)

- **PATRÓN** `volumen_pendiente_norm` > `0.2935` → IC=+0.318 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2935 (IC base=+0.268)

- **PATRÓN** `volumen_spike_ratio` > `2.7082` → IC=+0.336 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7082 (IC base=+0.268)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.304 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.268)

- **PATRÓN** `libro_liquidez` > `1981.9929` → IC=+0.320 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1981.9929 (IC base=+0.268)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.254 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 71.0 (IC base=+0.268)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.175 (n=158)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0028 (IC base=+0.153)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.185 (n=157)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0071 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.180 (n=423)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 8.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `0.3232` → IC=+0.208 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3232 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.2504` → IC=+0.234 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2504 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.619` → IC=+0.195 (n=126)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 9.619 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `1.2673` → IC=+0.161 (n=470)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2673 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` > `1.1006` → IC=+0.170 (n=213)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 1.1006 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.2044` → IC=+0.225 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2044 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.0651` → IC=+0.178 (n=371)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 2.0651 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `1.6798` → IC=+0.189 (n=281)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 1.6798 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `11871.8913` → IC=+0.176 (n=313)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 11871.8913 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.193 (n=148)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0022 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.1713` → IC=+0.195 (n=293)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.1713 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.172 (n=409)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 7.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.179 (n=440)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 17.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` < `0.3818` → IC=+0.216 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3818 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` < `0.3017` → IC=+0.178 (n=421)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.3017 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.611` → IC=+0.223 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.611 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `0.6259` → IC=+0.245 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6259 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.1489` → IC=+0.281 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1489 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `1.7416` → IC=+0.197 (n=229)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.7416 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `1.5054` → IC=+0.188 (n=306)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 1.5054 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.167 (n=566)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `13630.0841` → IC=+0.169 (n=146)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 13630.0841 (IC base=+0.167)

- **PATRÓN** `ballena_activa_n` < `309.0` → IC=+0.187 (n=81)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 309.0 (IC base=+0.167)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `hora_utc` < `8.0` → IC=+0.240 (n=179)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` > `0.7044` → IC=+0.264 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7044 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.106` → IC=+0.343 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.106 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` < `0.2259` → IC=+0.185 (n=319)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` < 0.2259 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` < `1.9992` → IC=+0.200 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9992 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `3.6607` → IC=+0.176 (n=143)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 3.6607 (IC base=+0.183)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.211 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `1914.9184` → IC=+0.208 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1914.9184 (IC base=+0.183)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.230 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 59.0 (IC base=+0.183)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.327 (n=125)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.253)

- **PATRÓN** `drift_60min` |x|≤ `0.0973` → IC=+0.264 (n=125)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0973 (IC base=+0.253)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.266 (n=250)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.253)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.287 (n=148)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.253)

- **PATRÓN** `ibs_20min` < `0.5703` → IC=+0.316 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5703 (IC base=+0.253)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.093` → IC=+0.281 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.093 (IC base=+0.253)

- **PATRÓN** `volumen_pendiente_norm` > `0.3451` → IC=+0.295 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3451 (IC base=+0.253)

- **PATRÓN** `volumen_spike_ratio` < `1.7551` → IC=+0.267 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7551 (IC base=+0.253)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.279 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.253)

- **PATRÓN** `ballena_activa_n` < `64.0` → IC=+0.201 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 64.0 (IC base=+0.253)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.159 (n=414)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0072 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.1448` → IC=+0.141 (n=207)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.1448 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.164 (n=429)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 8.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.34` → IC=+0.196 (n=471)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.34 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.8774` → IC=+0.206 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8774 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.433` → IC=+0.205 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.433 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `0.6197` → IC=+0.173 (n=157)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.6197 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` > `1.1962` → IC=+0.167 (n=157)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 1.1962 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.2673` → IC=+0.287 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2673 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `2.4116` → IC=+0.241 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4116 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `5254.2901` → IC=+0.222 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5254.2901 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.175 (n=232)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 166.0 (IC base=+0.141)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.204 (n=130)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.5036` → IC=+0.165 (n=389)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.5036 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.186 (n=278)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 11.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` < `0.0817` → IC=+0.246 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0817 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.1638` → IC=+0.160 (n=195)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1638 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` < `0.6545` → IC=+0.175 (n=414)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.6545 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.842` → IC=+0.217 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.842 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `0.586` → IC=+0.159 (n=130)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.586 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` > `1.1367` → IC=+0.197 (n=130)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` > 1.1367 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.233` → IC=+0.333 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.233 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `1.8136` → IC=+0.182 (n=221)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.8136 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `2.4528` → IC=+0.190 (n=111)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.4528 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `9483.0008` → IC=+0.209 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9483.0008 (IC base=+0.154)

- **PATRÓN** `ballena_activa_n` < `174.0` → IC=+0.209 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 174.0 (IC base=+0.154)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.011` → IC=+0.170 (n=237)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.011 (IC base=+0.099)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.142 (n=356)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 12.0 (IC base=+0.099)

- **PATRÓN** `ibs_20min` > `0.9091` → IC=+0.307 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9091 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` > `0.8201` → IC=+0.247 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8201 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.172` → IC=+0.248 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.172 (IC base=+0.099)

- **PATRÓN** `libro_liquidez` > `2942.126` → IC=+0.285 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2942.126 (IC base=+0.099)

- **PATRÓN** `ballena_activa_n` < `66.0` → IC=+0.176 (n=297)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 66.0 (IC base=+0.099)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.178 (n=209)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.006 (IC base=+0.113)

- **PATRÓN** `drift_60min` |x|≤ `0.5352` → IC=+0.125 (n=475)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.62€ cuando `drift_60min` |x|≤ 0.5352 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.170 (n=219)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 15.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.5882` → IC=+0.196 (n=475)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.5882 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` < `0.4633` → IC=+0.140 (n=429)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.4633 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.042` → IC=+0.133 (n=466)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 3.042 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `0.7061` → IC=+0.149 (n=209)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.7061 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.0719` → IC=+0.159 (n=133)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.0719 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` < `2.0886` → IC=+0.141 (n=288)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.0886 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` > `1.5376` → IC=+0.137 (n=293)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.5376 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `2599.7014` → IC=+0.161 (n=216)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2599.7014 (IC base=+0.113)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0223` → IC=+0.219 (n=279)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0223 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.184 (n=618)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 6.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` > `0.963` → IC=+0.301 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.963 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` > `1.4593` → IC=+0.291 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.4593 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.967` → IC=+0.265 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.967 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` < `0.6105` → IC=+0.181 (n=205)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6105 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` > `1.0357` → IC=+0.206 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0357 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.1687` → IC=+0.250 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1687 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `1.8157` → IC=+0.189 (n=377)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 1.8157 (IC base=+0.176)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.187 (n=647)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.01 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `3093.5671` → IC=+0.186 (n=205)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 3093.5671 (IC base=+0.176)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.219 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.176)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.305 (n=224)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.4796` → IC=+0.227 (n=588)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4796 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.219 (n=621)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` < `0.4912` → IC=+0.275 (n=668)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4912 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` < `1.2245` → IC=+0.223 (n=777)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 1.2245 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.445` → IC=+0.279 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.445 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.03` → IC=+0.214 (n=662)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.03 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` > `1.2349` → IC=+0.242 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2349 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.2794` → IC=+0.321 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2794 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `2.5884` → IC=+0.236 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5884 (IC base=+0.213)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.175 (n=383)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 37.0 (IC base=+0.213)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.148 (n=1005)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.138 (n=484)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0105 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=193)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `0.9312` → IC=+0.167 (n=184)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.9312 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `1.3996` → IC=+0.179 (n=129)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 1.3996 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.119` → IC=+0.189 (n=88)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 10.119 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `0.7051` → IC=+0.146 (n=190)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.7051 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` > `1.0851` → IC=+0.150 (n=195)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 1.0851 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.2718` → IC=+0.218 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2718 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `2.4519` → IC=+0.126 (n=540)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 2.4519 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` > `1.8062` → IC=+0.124 (n=360)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` > 1.8062 (IC base=+0.118)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.122 (n=480)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.01 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `5766.3654` → IC=+0.145 (n=367)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 5766.3654 (IC base=+0.118)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.195 (n=260)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0036 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.3577` → IC=+0.164 (n=674)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.3577 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.168 (n=269)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.194 (n=295)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 4.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` < `0.6323` → IC=+0.149 (n=674)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.6323 (IC base=+0.143)

- **PATRÓN** `ibs_20min` > `0.0862` → IC=+0.152 (n=765)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.0862 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.1712` → IC=+0.149 (n=329)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.1712 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` < `0.3663` → IC=+0.141 (n=742)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.3663 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.117` → IC=+0.147 (n=341)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 4.117 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.051` → IC=+0.149 (n=768)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 6.051 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `1.2185` → IC=+0.155 (n=745)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.2185 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` < `0.0935` → IC=+0.148 (n=685)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` < 0.0935 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.0717` → IC=+0.153 (n=367)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.0717 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `2.4869` → IC=+0.157 (n=757)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.4869 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `1.4126` → IC=+0.148 (n=757)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.4126 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=1005)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `10656.9735` → IC=+0.158 (n=510)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 10656.9735 (IC base=+0.143)

### GBM_LATE_5M#BTC#5min
- **FILTRO** `hora_utc` < `12.0` → IC=-0.156 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=73)

- **FILTRO** `sigma_ewma_delta_pct` > `2.779` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.779
  - _Potencial_: sin este filtro IC_bueno=+0.147 (n=83)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.167 (n=73)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 12.0 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` > `0.5259` → IC=+0.144 (n=57)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.5259 (IC base=+0.071)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.779` → IC=+0.147 (n=83)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 2.779 (IC base=+0.071)

- **PATRÓN** `volumen_regimen` > `0.9375` → IC=+0.210 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9375 (IC base=+0.071)

- **PATRÓN** `volumen_spike_ratio` < `1.7837` → IC=+0.130 (n=52)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.7837 (IC base=+0.071)

- **PATRÓN** `libro_liquidez` > `12550.0528` → IC=+0.150 (n=78)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 12550.0528 (IC base=+0.071)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.167 (n=433)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0065 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.3644` → IC=+0.156 (n=434)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.3644 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.194 (n=158)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.192 (n=167)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 5.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` < `0.1827` → IC=+0.163 (n=191)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.1827 (IC base=+0.142)

- **PATRÓN** `ibs_20min` > `0.3976` → IC=+0.143 (n=289)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.3976 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `0.1787` → IC=+0.165 (n=162)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.1787 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` < `0.3492` → IC=+0.144 (n=462)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.3492 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.318` → IC=+0.156 (n=437)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 6.318 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `1.1906` → IC=+0.158 (n=433)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.1906 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` > `0.6241` → IC=+0.143 (n=432)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.6241 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.0724` → IC=+0.180 (n=201)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.0724 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `2.5254` → IC=+0.153 (n=430)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.5254 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `1.7752` → IC=+0.150 (n=287)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.7752 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `11900.3051` → IC=+0.144 (n=386)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 11900.3051 (IC base=+0.142)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.197 (n=31)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0121 (IC base=+0.098)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.200 (n=38)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.098)

- **PATRÓN** `ibs_20min` > `0.9219` → IC=+0.340 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9219 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.132` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.132 (IC base=+0.098)

- **PATRÓN** `volumen_pendiente_norm` > `0.0759` → IC=+0.179 (n=26)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.0759 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `1668.2006` → IC=+0.129 (n=68)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 1668.2006 (IC base=+0.098)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0089` → IC=+0.197 (n=199)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0089 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.4394` → IC=+0.177 (n=199)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.4394 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.223 (n=81)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` < `0.2929` → IC=+0.157 (n=100)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.2929 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.7919` → IC=+0.195 (n=103)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.7919 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `1.0663` → IC=+0.216 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0663 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.4091` → IC=+0.167 (n=190)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.4091 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.219` → IC=+0.203 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.219 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.678` → IC=+0.152 (n=225)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 6.678 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.6468` → IC=+0.192 (n=76)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.6468 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.0815` → IC=+0.170 (n=101)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.0815 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `1.412` → IC=+0.210 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.412 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `8856.6618` → IC=+0.191 (n=202)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 8856.6618 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0088` → IC=+0.162 (n=220)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0088 (IC base=+0.143)

- **PATRÓN** `sigma_h` > `0.0061` → IC=+0.162 (n=146)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0061 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.497` → IC=+0.176 (n=220)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.497 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.153 (n=73)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 18.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.173 (n=148)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 9.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` < `0.612` → IC=+0.146 (n=193)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.612 (IC base=+0.143)

- **PATRÓN** `ibs_20min` > `0.089` → IC=+0.183 (n=219)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.089 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.1942` → IC=+0.145 (n=91)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.1942 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` < `0.3517` → IC=+0.157 (n=214)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.3517 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.244` → IC=+0.173 (n=111)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 3.244 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `1.1886` → IC=+0.176 (n=220)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 1.1886 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` < `0.1309` → IC=+0.167 (n=223)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` < 0.1309 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `2.1543` → IC=+0.196 (n=189)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.1543 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `1.4479` → IC=+0.168 (n=215)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.4479 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `10298.1112` → IC=+0.180 (n=73)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 10298.1112 (IC base=+0.143)

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
- **FILTRO** `ibs_20min` < `0.6544` → IC=-0.188 (n=46)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6544
  - _Potencial_: sin este filtro IC_bueno=+0.209 (n=139)

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

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.179 (n=154)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0054 (IC base=+0.066)

- **PATRÓN** `ibs_20min` > `0.6544` → IC=+0.209 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6544 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` > `0.1258` → IC=+0.162 (n=75)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.1258 (IC base=+0.066)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.481` → IC=+0.233 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.481 (IC base=+0.066)

- **PATRÓN** `volumen_pendiente_norm` < `0.0725` → IC=+0.250 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0725 (IC base=+0.066)

- **PATRÓN** `volumen_pendiente_norm` > `0.1516` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1516 (IC base=+0.066)

- **PATRÓN** `volumen_spike_ratio` > `1.4971` → IC=+0.300 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4971 (IC base=+0.066)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.153 (n=125)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.02 (IC base=+0.066)

- **PATRÓN** `libro_liquidez` > `2484.2771` → IC=+0.146 (n=77)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 2484.2771 (IC base=+0.066)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.7788` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7788
  - _Potencial_: sin este filtro IC_bueno=+0.208 (n=46)

- **FILTRO** `hora_utc` > `3.0` → IC=-0.188 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=24)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.333 (n=28)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.068)

- **PATRÓN** `ibs_20min` > `0.7788` → IC=+0.208 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7788 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.1642` → IC=+0.177 (n=29)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.1642 (IC base=+0.068)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0068` → IC=-0.333 (n=22)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=-0.144 (n=43)

- **FILTRO** `hora_utc` > `9.0` → IC=-0.318 (n=31)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=34)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.163 (n=81)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0059 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.126 (n=97)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 5.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.357 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` < `0.2422` → IC=+0.229 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2422 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.06` → IC=+0.316 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.06 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `0.6214` → IC=+0.224 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6214 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` > `0.9325` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9325 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `2519.6873` → IC=+0.250 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2519.6873 (IC base=+0.113)

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

- **FILTRO** `dist_vwap_pct` > `0.0755` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.0755
  - _Potencial_: sin este filtro IC_bueno=-0.283 (n=81)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.344 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=36)

- **FILTRO** `ibs_20min` < `0.3707` → IC=-0.308 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3707
  - _Potencial_: sin este filtro IC_bueno=-0.289 (n=74)

- **FILTRO** `dist_vwap_pct` < `0.1009` → IC=-0.354 (n=53)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1009
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=45)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `ibs_20min` < `0.4953` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `ibs_20min` < 0.4953
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=13)

- **FILTRO** `sigma_h` < `0.0019` → IC=-0.318 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0019
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=21)

- **FILTRO** `ibs_20min` > `0.6267` → IC=-0.364 (n=20)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6267
  - _Potencial_: sin este filtro IC_bueno=-0.152 (n=21)

- **FILTRO** `dist_vwap_pct` < `0.0931` → IC=-0.362 (n=27)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0931
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=14)

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

- **FILTRO** `ibs_20min` < `0.7391` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7391
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.441 (n=15)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` < `0.5882` → IC=-0.250 (n=46)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5882
  - _Potencial_: sin este filtro IC_bueno=+0.150 (n=138)

- **FILTRO** `dist_vwap_pct` > `0.5824` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.5824
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=138)

- **PATRÓN** `ibs_20min` > `0.5882` → IC=+0.150 (n=138)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` > 0.5882 (IC base=+0.048)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.3927` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3927
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=40)

- **PATRÓN** `ibs_20min` > `0.7184` → IC=+0.188 (n=30)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.7184 (IC base=-0.057)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.214 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.090)

- **PATRÓN** `ibs_20min` < `0.3803` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.3803 (IC base=+0.090)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.519` → IC=+0.150 (n=38)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 3.519 (IC base=+0.090)

- **PATRÓN** `volumen_regimen` < `1.0741` → IC=+0.123 (n=51)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.0741 (IC base=+0.090)

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
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.133 (n=118)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 6.0 (IC base=+0.108)

- **PATRÓN** `libro_liquidez` > `2501.4019` → IC=+0.172 (n=114)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2501.4019 (IC base=+0.108)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.140 (n=134)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 18.0 (IC base=+0.123)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.128 (n=49)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.495 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `2493.9311` → IC=+0.159 (n=124)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 2493.9311 (IC base=+0.123)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.133 (n=118)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 6.0 (IC base=+0.108)

- **PATRÓN** `libro_liquidez` > `2501.4019` → IC=+0.172 (n=114)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2501.4019 (IC base=+0.108)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.140 (n=134)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 18.0 (IC base=+0.123)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.128 (n=49)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.495 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `2493.9311` → IC=+0.159 (n=124)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 2493.9311 (IC base=+0.123)

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

### LIQUIDACIONES_5M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=488)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=88)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9427` → IC=-0.311 (n=35)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9427
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=74)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=88)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_usd_total` < `37956.41` → IC=-0.125 (n=38)

  - _Acción_: SKIP cuando `liq_usd_total` < 37956.41
  - _Potencial_: sin este filtro IC_bueno=+0.175 (n=38)

- **PATRÓN** `liq_n` > `11.0` → IC=+0.136 (n=20)

  - _Acción_: Kelly boost +0.68€ cuando `liq_n` > 11.0 (IC base=+0.026)

- **PATRÓN** `liq_usd_total` > `37956.41` → IC=+0.175 (n=38)

  - _Acción_: Kelly boost +0.88€ cuando `liq_usd_total` > 37956.41 (IC base=+0.026)

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
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=144)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.318 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **PATRÓN** `liq_n` > `2.0` → IC=+0.132 (n=93)

  - _Acción_: Kelly boost +0.66€ cuando `liq_n` > 2.0 (IC base=+0.074)

- **PATRÓN** `liq_usd_total` > `9904.97` → IC=+0.149 (n=55)

  - _Acción_: Kelly boost +0.75€ cuando `liq_usd_total` > 9904.97 (IC base=+0.074)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.138 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 8.0 (IC base=+0.074)

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
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=94)

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
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=27)

- **PATRÓN** `liq_imbalance_60min` |x|> `1.0` → IC=+0.121 (n=27)

  - _Acción_: Kelly boost +0.60€ cuando `liq_imbalance_60min` |x|> 1.0 (IC base=+0.023)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=25)

### MOMENTUM_IBS_15M#BNB#15min
- **FILTRO** `libro_liquidez` < `2179.6408` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `libro_liquidez` < 2179.6408
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=126)

### MOMENTUM_IBS_15M#DOGE#15min
- **FILTRO** `ibs_20min` > `0.9515` → IC=-0.192 (n=92)

  - _Acción_: SKIP cuando `ibs_20min` > 0.9515
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=280)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=438)

### MOMENTUM_IBS_15M#SOL#15min
- **FILTRO** `drift_20min_pct` |x|> `0.1784` → IC=-0.137 (n=100)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1784
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=196)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.46` → IC=-0.167 (n=845)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=2623)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.218 (n=820)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=2612)

- **FILTRO** `ibs_20min` > `0.2737` → IC=-0.183 (n=857)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2737
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=2575)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.242 (n=122)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=379)

- **FILTRO** `ibs_20min` < `0.7325` → IC=-0.185 (n=125)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7325
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=376)

- **FILTRO** `ibs_20min` > `0.1844` → IC=-0.126 (n=295)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1844
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=296)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.231 (n=139)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=432)

- **FILTRO** `ballena_activa_n` > `79.0` → IC=-0.174 (n=142)

  - _Acción_: SKIP cuando `ballena_activa_n` > 79.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=429)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.133 (n=115)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=412)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.175 (n=229)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=298)

- **FILTRO** `ibs_20min` < `0.7248` → IC=-0.177 (n=131)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7248
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=396)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.203 (n=193)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=382)

- **FILTRO** `ibs_20min` > `0.7531` → IC=-0.210 (n=143)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7531
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=432)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.129 (n=141)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=480)

- **FILTRO** `py_entrada` > `0.52` → IC=-0.190 (n=143)

  - _Acción_: SKIP cuando `py_entrada` > 0.52
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=464)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.160 (n=151)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=456)

### MOMENTUM_IBS_15M_BALLENA#SOL#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.231 (n=132)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=408)

- **FILTRO** `drift_20min_pct` |x|> `0.2824` → IC=-0.149 (n=183)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.2824
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=357)

- **FILTRO** `ibs_20min` > `0.2794` → IC=-0.184 (n=134)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2794
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=406)

- **FILTRO** `ballena_activa_n` > `3.0` → IC=-0.145 (n=243)

  - _Acción_: SKIP cuando `ballena_activa_n` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=297)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.214 (n=138)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=445)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=568)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.242 (n=184)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=364)

- **FILTRO** `ibs_20min` > `0.2857` → IC=-0.243 (n=134)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=414)

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
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=6141)

- **FILTRO** `py_entrada` < `0.36` → IC=-0.282 (n=2066)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=6526)

- **FILTRO** `ibs_7min` < `0.734` → IC=-0.230 (n=2146)

  - _Acción_: SKIP cuando `ibs_7min` < 0.734
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=6446)

- **FILTRO** `ballena_activa_n` > `19.0` → IC=-0.172 (n=2907)

  - _Acción_: SKIP cuando `ballena_activa_n` > 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=5685)

- **FILTRO** `py_entrada` > `0.69` → IC=-0.231 (n=2422)

  - _Acción_: SKIP cuando `py_entrada` > 0.69
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=8011)

- **FILTRO** `ibs_7min` > `0.7254` → IC=-0.174 (n=2608)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7254
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=7825)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.328 (n=282)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=875)

- **FILTRO** `ibs_7min` < `0.9787` → IC=-0.202 (n=762)

  - _Acción_: SKIP cuando `ibs_7min` < 0.9787
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=395)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.254 (n=286)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=871)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.235 (n=424)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=1368)

- **FILTRO** `drift_7min_pct` |x|> `0.1376` → IC=-0.155 (n=609)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1376
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=1183)

- **FILTRO** `ibs_7min` > `0.8406` → IC=-0.190 (n=447)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8406
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=1345)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.155 (n=355)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=1320)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.253 (n=391)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=1284)

- **FILTRO** `ibs_7min` < `0.7974` → IC=-0.169 (n=418)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7974
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=1257)

- **FILTRO** `ballena_activa_n` > `156.0` → IC=-0.186 (n=418)

  - _Acción_: SKIP cuando `ballena_activa_n` > 156.0
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=1257)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.230 (n=394)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=1297)

- **FILTRO** `ballena_activa_n` > `94.0` → IC=-0.164 (n=569)

  - _Acción_: SKIP cuando `ballena_activa_n` > 94.0
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=1122)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.201 (n=296)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=937)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.312 (n=396)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=837)

- **FILTRO** `ibs_7min` < `0.2127` → IC=-0.284 (n=308)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2127
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=925)

- **FILTRO** `ballena_activa_n` > `16.0` → IC=-0.279 (n=297)

  - _Acción_: SKIP cuando `ballena_activa_n` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=936)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.257 (n=393)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=1423)

- **FILTRO** `ibs_7min` > `0.8214` → IC=-0.192 (n=453)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8214
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=1363)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.151 (n=434)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=1010)

- **FILTRO** `py_entrada` < `0.45` → IC=-0.206 (n=722)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=722)

- **FILTRO** `ibs_7min` < `0.7541` → IC=-0.183 (n=361)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7541
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=1083)

- **FILTRO** `ballena_activa_n` > `43.0` → IC=-0.216 (n=350)

  - _Acción_: SKIP cuando `ballena_activa_n` > 43.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=1094)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.134 (n=463)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=976)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.282 (n=337)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=1102)

- **FILTRO** `ibs_7min` > `0.1878` → IC=-0.164 (n=489)

  - _Acción_: SKIP cuando `ibs_7min` > 0.1878
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=950)

- **FILTRO** `ballena_activa_n` > `26.0` → IC=-0.186 (n=482)

  - _Acción_: SKIP cuando `ballena_activa_n` > 26.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=957)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.221 (n=410)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=1241)

- **FILTRO** `ibs_7min` < `0.7727` → IC=-0.189 (n=410)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7727
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=1241)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.183 (n=405)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1246)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.185 (n=478)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=1450)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.38` → IC=-0.285 (n=343)

  - _Acción_: SKIP cuando `py_entrada` < 0.38
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=1089)

- **FILTRO** `ibs_7min` < `0.7541` → IC=-0.200 (n=358)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7541
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=1074)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.221 (n=353)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=1079)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.267 (n=363)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=1404)

- **FILTRO** `ibs_7min` > `0.8278` → IC=-0.164 (n=441)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8278
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=1326)

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
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=248)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=435)

### ORDER_FLOW_5M
- **FILTRO** `total_vol_5m` > `215.224` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `total_vol_5m` > 215.224
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **PATRÓN** `delta_ratio` |x|> `0.4497` → IC=+0.170 (n=98)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.85€ cuando `delta_ratio` |x|> 0.4497 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.150 (n=101)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 15.0 (IC base=+0.123)

- **PATRÓN** `total_vol_5m` < `451.5692` → IC=+0.220 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 451.5692 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `3566.692` → IC=+0.171 (n=74)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 3566.692 (IC base=+0.123)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.271 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.148)

- **PATRÓN** `total_vol_5m` < `637.367` → IC=+0.167 (n=67)

  - _Acción_: Kelly boost +0.83€ cuando `total_vol_5m` < 637.367 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.172 (n=62)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 53.0 (IC base=+0.148)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `hora_utc` > `12.0` → IC=+0.167 (n=28)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 12.0 (IC base=+0.103)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.128 (n=41)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.02 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `2069.5174` → IC=+0.125 (n=38)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 2069.5174 (IC base=+0.103)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `hora_utc` < `8.0` → IC=+0.222 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=27)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `3221.1629` → IC=+0.197 (n=31)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 3221.1629 (IC base=+0.125)

### ORDER_FLOW_5M#XRP#5min
- **FILTRO** `delta_ratio` |x|≤ `0.401` → IC=-0.136 (n=20)
  - _Por qué funciona_: delta_ratio bajo → order flow débil; señal insuficiente para batir el spread
  - _Acción_: SKIP cuando `delta_ratio` |x|≤ 0.401
  - _Potencial_: sin este filtro IC_bueno=+0.122 (n=43)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` < `0.0084` → IC=-0.180 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0084
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=71)

- **FILTRO** `sigma_h` > `0.0084` → IC=-0.312 (n=83)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0084
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=86)

- **FILTRO** `T_h` > `98.7549` → IC=-0.381 (n=65)

  - _Acción_: SKIP cuando `T_h` > 98.7549
  - _Potencial_: sin este filtro IC_bueno=-0.235 (n=66)

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

### PRICE_TARGET_GBM_FADE
- **FILTRO** `T_h` > `144.6113` → IC=-0.328 (n=27)

  - _Acción_: SKIP cuando `T_h` > 144.6113
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=83)

- **FILTRO** `T_h` < `95.1632` → IC=-0.457 (n=21)

  - _Acción_: SKIP cuando `T_h` < 95.1632
  - _Potencial_: sin este filtro IC_bueno=-0.303 (n=64)

- **PATRÓN** `pct_vs_K` |x|≤ `1.4454` → IC=+0.192 (n=37)

  - _Acción_: Kelly boost +0.96€ cuando `pct_vs_K` |x|≤ 1.4454 (IC base=-0.036)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **PATRÓN** `T_h` < `95.1632` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 95.1632 (IC base=+0.122)

- **PATRÓN** `pct_vs_K` |x|≤ `1.4281` → IC=+0.333 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 1.4281 (IC base=+0.122)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` < `0.005` → IC=-0.180 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=13)

- **FILTRO** `T_h` > `111.9866` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `T_h` > 111.9866
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=19)

- **FILTRO** `sigma_h` < `0.0045` → IC=-0.357 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0045
  - _Potencial_: sin este filtro IC_bueno=-0.273 (n=20)

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
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=79)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.188 (n=30)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 34.0 (IC base=+0.019)

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
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=143)

- **PATRÓN** `streak_estiramiento` < `0.2989` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `streak_estiramiento` < 0.2989 (IC base=+0.006)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=300)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=162)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=214)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.129 (n=157)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 14.0 (IC base=+0.071)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=1197)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=683)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=691)

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

### UPDOWN_GBM#5min
- **FILTRO** `ibs_15` < `0.225` → IC=-0.215 (n=121)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.225
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=364)

- **FILTRO** `sigma_ewma_delta_pct` > `6.578` → IC=-0.209 (n=53)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.578
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=432)

### UPDOWN_GBM#60min
- **FILTRO** `sigma_h` < `0.0053` → IC=-0.222 (n=16)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=51)

- **FILTRO** `ibs_15` < `0.16` → IC=-0.289 (n=17)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.16
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=36)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=13)

### UPDOWN_GBM#BTC#15min
- **FILTRO** `sigma_h` < `0.0041` → IC=-0.273 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0041
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=62)

- **FILTRO** `ibs_15` > `0.7185` → IC=-0.227 (n=20)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.7185
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=62)

- **FILTRO** `ibs_15` < `0.3405` → IC=-0.190 (n=27)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.3405
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=55)

- **FILTRO** `libro_liquidez` < `13914.5646` → IC=-0.293 (n=27)

  - _Acción_: SKIP cuando `libro_liquidez` < 13914.5646
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=55)

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
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0174` → IC=-0.132 (n=36)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0174
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=19)

- **FILTRO** `hora_utc` < `4.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=39)

- **FILTRO** `ibs_15` < `0.1461` → IC=-0.250 (n=18)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.1461
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=37)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `ibs_15` < `0.8291` → IC=-0.140 (n=48)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8291
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=48)

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

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.123 (n=181)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0054 (IC base=+0.016)

### UPDOWN_GBM#ETH#5min
- **FILTRO** `hora_utc` > `8.0` → IC=-0.167 (n=25)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=60)

- **FILTRO** `dist_vwap_pct` > `0.1635` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1635
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=70)

- **FILTRO** `drift_15min` |x|> `0.5413` → IC=-0.155 (n=111)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.5413
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=335)

### UPDOWN_GBM#ETH#60min
- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=45)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.026)

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
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=36)

- **FILTRO** `ibs_15` < `0.2` → IC=-0.395 (n=17)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=53)

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

- **PATRÓN** `ibs_15` < `0.1282` → IC=+0.209 (n=108)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1282 (IC base=+0.049)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.005` → IC=+0.401 (n=69)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.317)

- **PATRÓN** `drift_60min` |x|≤ `0.0582` → IC=+0.349 (n=51)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0582 (IC base=+0.317)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1528` → IC=+0.333 (n=100)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1528 (IC base=+0.317)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3802` → IC=+0.390 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3802 (IC base=+0.317)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.339 (n=141)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.317)

- **PATRÓN** `ibs_15` > `0.809` → IC=+0.375 (n=134)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.809 (IC base=+0.317)

- **PATRÓN** `dist_vwap_pct` > `0.447` → IC=+0.370 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.447 (IC base=+0.317)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.354` → IC=+0.347 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.354 (IC base=+0.317)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.318 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.317)

- **PATRÓN** `libro_liquidez` > `7959.8654` → IC=+0.385 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7959.8654 (IC base=+0.317)

- **PATRÓN** `ballena_activa_n` < `463.0` → IC=+0.386 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 463.0 (IC base=+0.317)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1971` → IC=+0.305 (n=75)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1971 (IC base=+0.291)

- **PATRÓN** `sigma_h` > `0.0045` → IC=+0.403 (n=29)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0045 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.16` → IC=+0.318 (n=75)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.16 (IC base=+0.291)

- **PATRÓN** `drift_15min` |x|≤ `0.4136` → IC=+0.325 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4136 (IC base=+0.291)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1371` → IC=+0.441 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1371 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.329 (n=80)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.291)

- **PATRÓN** `ibs_15` > `0.8374` → IC=+0.333 (n=76)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8374 (IC base=+0.291)

- **PATRÓN** `dist_vwap_pct` > `0.4267` → IC=+0.389 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4267 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.871` → IC=+0.304 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.871 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.39` → IC=+0.292 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.39 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `8557.9163` → IC=+0.378 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8557.9163 (IC base=+0.291)

- **PATRÓN** `ballena_activa_n` < `480.0` → IC=+0.444 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 480.0 (IC base=+0.291)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.339 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.343)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.406 (n=30)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.343)

- **PATRÓN** `drift_60min` |x|≤ `0.1189` → IC=+0.370 (n=44)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1189 (IC base=+0.343)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1322` → IC=+0.391 (n=44)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1322 (IC base=+0.343)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2773` → IC=+0.361 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2773 (IC base=+0.343)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.348 (n=44)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.343)

- **PATRÓN** `hora_utc` < `19.0` → IC=+0.338 (n=72)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 19.0 (IC base=+0.343)

- **PATRÓN** `ibs_15` > `0.7914` → IC=+0.434 (n=59)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7914 (IC base=+0.343)

- **PATRÓN** `dist_vwap_pct` < `0.3445` → IC=+0.347 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3445 (IC base=+0.343)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.937` → IC=+0.409 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.937 (IC base=+0.343)

- **PATRÓN** `libro_liquidez` > `3261.6008` → IC=+0.370 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3261.6008 (IC base=+0.343)

- **PATRÓN** `ballena_activa_n` < `198.0` → IC=+0.367 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 198.0 (IC base=+0.343)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0096` → IC=-0.156 (n=251)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0096
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=760)

- **FILTRO** `ibs_15` < `0.6867` → IC=-0.158 (n=200)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6867
  - _Potencial_: sin este filtro IC_bueno=+0.272 (n=200)

- **FILTRO** `sigma_ewma_delta_pct` > `17.413` → IC=-0.173 (n=344)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.413
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=2541)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3537` → IC=+0.157 (n=138)

  - _Acción_: Kelly boost +0.79€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3537 (IC base=-0.059)

- **PATRÓN** `ibs_15` > `0.6867` → IC=+0.272 (n=200)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6867 (IC base=-0.059)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1274` → IC=+0.255 (n=108)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1274 (IC base=-0.082)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.068` → IC=+0.329 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.068 (IC base=-0.082)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.317 (n=162)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.082)

- **PATRÓN** `dist_vwap_pct` < `0.1254` → IC=+0.255 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1254 (IC base=-0.082)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0076` → IC=-0.248 (n=157)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0076
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=475)

- **FILTRO** `sigma_h` < `0.0035` → IC=-0.219 (n=208)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0035
  - _Potencial_: sin este filtro IC_bueno=-0.209 (n=424)

- **FILTRO** `sigma_ewma_delta_pct` > `19.957` → IC=-0.265 (n=117)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.957
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=515)

- **FILTRO** `libro_liquidez` < `16111.8336` → IC=-0.221 (n=474)

  - _Acción_: SKIP cuando `libro_liquidez` < 16111.8336
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=158)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.121 (n=56)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.60€ cuando `sigma_h` < 0.0029 (IC base=+0.015)

- **PATRÓN** `ibs_15` > `0.8545` → IC=+0.441 (n=15)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8545 (IC base=+0.015)

- **PATRÓN** `dist_vwap_pct` < `0.3854` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.3854 (IC base=+0.015)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.4479` → IC=-0.367 (n=43)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.4479
  - _Potencial_: sin este filtro IC_bueno=+0.187 (n=132)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=158)

- **PATRÓN** `drift_60min` |x|≤ `0.0603` → IC=+0.174 (n=44)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.0603 (IC base=+0.048)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3537` → IC=+0.243 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3537 (IC base=+0.048)

- **PATRÓN** `ibs_15` > `0.4479` → IC=+0.187 (n=132)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.93€ cuando `ibs_15` > 0.4479 (IC base=+0.048)

- **PATRÓN** `libro_liquidez` > `9861.0594` → IC=+0.210 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9861.0594 (IC base=+0.048)

- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1058` → IC=+0.250 (n=66)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1058 (IC base=+0.235)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.240 (n=98)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.235)

- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.261 (n=65)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0062 (IC base=+0.235)

- **PATRÓN** `drift_15min` |x|≤ `0.4277` → IC=+0.271 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4277 (IC base=+0.235)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1405` → IC=+0.291 (n=65)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1405 (IC base=+0.235)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3038` → IC=+0.242 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3038 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.271 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.235)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.306 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.235)

- **PATRÓN** `ibs_15` < `0.3299` → IC=+0.320 (n=98)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3299 (IC base=+0.235)

- **PATRÓN** `dist_vwap_pct` < `0.1185` → IC=+0.253 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1185 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` < `11.326` → IC=+0.262 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 11.326 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `12530.3004` → IC=+0.266 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12530.3004 (IC base=+0.235)

- **PATRÓN** `ballena_activa_n` < `210.0` → IC=+0.257 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 210.0 (IC base=+0.235)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0105` → IC=-0.242 (n=60)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0105
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=184)

- **FILTRO** `drift_15min` |x|> `0.7757` → IC=-0.210 (n=60)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.7757
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=184)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=223)

- **FILTRO** `sigma_ewma_delta_pct` > `15.847` → IC=-0.149 (n=112)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 15.847
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=884)

- **PATRÓN** `ibs_15` > `0.8125` → IC=+0.206 (n=15)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8125 (IC base=-0.106)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `drift_15min` |x|> `1.1396` → IC=-0.250 (n=62)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.1396
  - _Potencial_: sin este filtro IC_bueno=-0.104 (n=190)

- **FILTRO** `sigma_ewma_delta_pct` > `14.492` → IC=-0.194 (n=34)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 14.492
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=218)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.161 (n=54)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.135 (n=198)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.281 (n=158)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.279)

- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.307 (n=107)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0055 (IC base=+0.279)

- **PATRÓN** `drift_60min` |x|≤ `0.0529` → IC=+0.327 (n=79)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0529 (IC base=+0.279)

- **PATRÓN** `drift_15min` |x|≤ `0.8433` → IC=+0.278 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.8433 (IC base=+0.279)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1881` → IC=+0.326 (n=107)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1881 (IC base=+0.279)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3802` → IC=+0.320 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3802 (IC base=+0.279)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.310 (n=245)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.279)

- **PATRÓN** `ibs_15` > `0.9641` → IC=+0.353 (n=107)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9641 (IC base=+0.279)

- **PATRÓN** `dist_vwap_pct` > `0.2998` → IC=+0.348 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2998 (IC base=+0.279)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.866` → IC=+0.278 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.866 (IC base=+0.279)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.907` → IC=+0.278 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 8.907 (IC base=+0.279)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.279 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `12344.7964` → IC=+0.340 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12344.7964 (IC base=+0.279)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.271 (n=59)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.258)

- **PATRÓN** `sigma_h` > `0.006` → IC=+0.283 (n=44)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.258)

- **PATRÓN** `drift_60min` |x|≤ `0.1871` → IC=+0.285 (n=133)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1871 (IC base=+0.258)

- **PATRÓN** `drift_15min` |x|≤ `0.6671` → IC=+0.265 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.6671 (IC base=+0.258)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1464` → IC=+0.289 (n=88)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1464 (IC base=+0.258)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3906` → IC=+0.297 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3906 (IC base=+0.258)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.300 (n=53)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.258)

- **PATRÓN** `ibs_15` > `0.9676` → IC=+0.323 (n=60)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9676 (IC base=+0.258)

- **PATRÓN** `dist_vwap_pct` > `0.3041` → IC=+0.336 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3041 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` > `24.679` → IC=+0.281 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 24.679 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.866` → IC=+0.266 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.866 (IC base=+0.258)

- **PATRÓN** `libro_liquidez` > `13599.3486` → IC=+0.326 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13599.3486 (IC base=+0.258)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.302 (n=104)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.300)

- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.296 (n=47)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0062 (IC base=+0.300)

- **PATRÓN** `drift_60min` |x|≤ `0.0603` → IC=+0.333 (n=46)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0603 (IC base=+0.300)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1879` → IC=+0.378 (n=47)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1879 (IC base=+0.300)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2968` → IC=+0.347 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2968 (IC base=+0.300)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.335 (n=107)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.300)

- **PATRÓN** `ibs_15` > `0.8687` → IC=+0.342 (n=93)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8687 (IC base=+0.300)

- **PATRÓN** `dist_vwap_pct` > `0.6362` → IC=+0.420 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6362 (IC base=+0.300)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.888` → IC=+0.311 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.888 (IC base=+0.300)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.313 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.300)

- **PATRÓN** `libro_liquidez` > `10575.7678` → IC=+0.419 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10575.7678 (IC base=+0.300)

- **PATRÓN** `ballena_activa_n` < `263.0` → IC=+0.324 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 263.0 (IC base=+0.300)

### UPDOWN_OU_5M
- **FILTRO** `sigma_h` > `0.0062` → IC=-0.239 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0062
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=64)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1219` → IC=-0.177 (n=94)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1219
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=283)

- **FILTRO** `sigma_h` > `0.007` → IC=-0.156 (n=94)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=283)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1533` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1533
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=12)

- **FILTRO** `ballena_activa_n` > `34.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `ballena_activa_n` > 34.0
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=50)

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
- **PATRÓN** `T_h` < `57.6124` → IC=+0.237 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 57.6124 (IC base=+0.100)

- **PATRÓN** `ratio` < `0.972` → IC=+0.457 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.972 (IC base=+0.100)

- **PATRÓN** `T_h` > `146.1003` → IC=+0.435 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1003 (IC base=+0.341)

- **PATRÓN** `ratio` < `1.0183` → IC=+0.210 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 1.0183 (IC base=+0.341)

- **PATRÓN** `ratio` > `1.0147` → IC=+0.173 (n=47)

  - _Acción_: Kelly boost +0.87€ cuando `ratio` > 1.0147 (IC base=+0.341)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` < `111.9965` → IC=+0.157 (n=33)

  - _Acción_: Kelly boost +0.79€ cuando `T_h` < 111.9965 (IC base=+0.091)

- **PATRÓN** `T_h` < `87.9965` → IC=+0.341 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 87.9965 (IC base=+0.261)

- **PATRÓN** `pct_dist` |x|≤ `0.6014` → IC=+0.288 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `pct_dist` |x|≤ 0.6014 (IC base=+0.261)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` < `76.962` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 76.962 (IC base=+0.143)

- **PATRÓN** `T_h` < `111.9558` → IC=+0.322 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 111.9558 (IC base=+0.302)

- **PATRÓN** `T_h` > `145.7723` → IC=+0.314 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7723 (IC base=+0.302)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `135.9824` → IC=+0.436 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 135.9824 (IC base=+0.414)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-SIGMA-SOL-60MIN**: `UPDOWN_GBM#SOL#60min` gana cuando sigma_h < 0.0058 (IC=+0.265 n=15). Implementar como filtro pre-predicción en shadow_predict.py.
- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5275 sube el IC de +0.115 a +0.203 en UPDOWN_GBM#15min (n=382). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.9375 sube el IC de +0.148 a +0.284 en UPDOWN_GBM#BTC#15min (n=49). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.617 sube el IC de +0.084 a +0.240 en UPDOWN_GBM#ETH#15min (n=75). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.056 a +0.265 en UPDOWN_GBM#SOL#15min (n=32). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5556 sube el IC de +0.096 a +0.185 en UPDOWN_GBM#XRP#15min (n=90). Ya aplicado como kelly_boost=+0.92€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1282 sube el IC de +0.049 a +0.209 en UPDOWN_GBM#XRP#15min (n=108). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6867 sube el IC de -0.059 a +0.272 en UPDOWN_GBM_15M_TARDIO (n=200). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.082 a +0.317 en UPDOWN_GBM_15M_TARDIO (n=162). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.8545 sube el IC de +0.015 a +0.441 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=15). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.4479 sube el IC de +0.048 a +0.187 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=132). Ya aplicado como kelly_boost=+0.93€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3299 sube el IC de +0.235 a +0.320 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=98). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8125 sube el IC de -0.106 a +0.206 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=15). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.9641 sube el IC de +0.279 a +0.353 en UPDOWN_GBM_IBS_ALTO (n=107). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.9676 sube el IC de +0.258 a +0.323 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=60). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8687 sube el IC de +0.300 a +0.342 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=93). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.809 sube el IC de +0.317 a +0.375 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=134). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8374 sube el IC de +0.291 a +0.333 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=76). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7914 sube el IC de +0.343 a +0.434 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=59). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min` — IC=+0.353 n=32. Faltan ~8 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL` — IC=+0.353 n=32. Faltan ~8 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `ORDER_FLOW_5M#ETH#5min` — IC=+0.134 n=39. Faltan ~1 resoluciones para umbral n≥40. ETA: ~1h.
- **LIVE-CANDIDATA**: `ORDER_FLOW_5M#ETH` — IC=+0.134 n=39. Faltan ~1 resoluciones para umbral n≥40. ETA: ~1h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 609 | +0.086 | +45.60€ | 1 | 11 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 609 | +0.086 | +45.60€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 365 | +0.110 | +34.60€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 365 | +0.110 | +34.60€ | 0 | 11 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 215 | +0.030 | +0.07€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 215 | +0.030 | +0.07€ | 7 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 29 | +0.177 | +10.93€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 29 | +0.177 | +10.93€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 9895 | -0.096 | -1552.15€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 705 | -0.080 | -128.33€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 9190 | -0.097 | -1423.83€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 1234 | -0.011 | -210.58€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 1234 | -0.011 | -210.58€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 705 | -0.080 | -128.33€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 705 | -0.080 | -128.33€ | 2 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 1257 | -0.167 | -406.46€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 1257 | -0.167 | -406.46€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 2680 | -0.070 | -260.59€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 2680 | -0.070 | -260.59€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 2303 | -0.071 | -123.51€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 2303 | -0.071 | -123.51€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 1716 | -0.183 | -422.69€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 1716 | -0.183 | -422.69€ | 1 | 0 |
| ✅ FAVORITO_CONFIRMADO | 32804 | +0.115 | -2059.12€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 6019 | +0.186 | -217.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 107 | -0.105 | -50.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 23462 | +0.098 | -1741.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 3216 | +0.119 | -50.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 3938 | +0.065 | -660.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 21 | -0.065 | +2.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#240min | 5 | -0.089 | -6.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 3912 | +0.067 | -656.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 6764 | +0.134 | -141.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 1701 | +0.196 | -95.51€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 3905 | +0.111 | -80.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 1116 | +0.130 | +56.96€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 3946 | +0.082 | -487.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 21 | +0.065 | +3.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 3924 | +0.082 | -488.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 7258 | +0.128 | -94.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 2188 | +0.167 | -18.71€ | 0 | 7 |
| 🚫 FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 3907 | +0.116 | -38.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 1151 | +0.099 | -29.04€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL | 6963 | +0.135 | -421.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 2071 | +0.204 | -107.22€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 46 | +0.000 | -9.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 3897 | +0.100 | -226.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 949 | +0.131 | -78.17€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#XRP | 3935 | +0.108 | -253.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 17 | -0.022 | -0.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 3917 | +0.109 | -251.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 5960 | +0.174 | -465.18€ | 3 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 5960 | +0.174 | -465.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 1499 | +0.168 | -156.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 1499 | +0.168 | -156.18€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 116 | -0.119 | +1.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 116 | -0.119 | +1.15€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 1484 | +0.163 | -169.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 1484 | +0.163 | -169.70€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 1338 | +0.228 | -41.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 1338 | +0.228 | -41.07€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 1444 | +0.183 | -113.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 1444 | +0.183 | -113.14€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 304 | +0.444 | +2.55€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 304 | +0.444 | +2.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 115 | +0.440 | +0.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 115 | +0.440 | +0.97€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 112 | +0.430 | -1.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 112 | +0.430 | -1.12€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 74 | +0.447 | +2.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 74 | +0.447 | +2.56€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 16757 | +0.192 | -1447.59€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 16757 | +0.192 | -1447.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 3066 | +0.127 | -564.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 3066 | +0.127 | -564.18€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 2608 | +0.237 | -47.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 2608 | +0.237 | -47.62€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 2877 | +0.166 | -359.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 2877 | +0.166 | -359.61€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 2660 | +0.230 | -77.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 2660 | +0.230 | -77.61€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 2723 | +0.218 | -123.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 2723 | +0.218 | -123.49€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 2823 | +0.186 | -275.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 2823 | +0.186 | -275.09€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 6071 | +0.133 | +213.76€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 6071 | +0.133 | +213.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 3021 | +0.139 | +143.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 3021 | +0.139 | +143.10€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 3050 | +0.126 | +70.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 3050 | +0.126 | +70.65€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 775 | +0.302 | +8.84€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 775 | +0.302 | +8.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 332 | +0.284 | -5.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 332 | +0.284 | -5.40€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 364 | +0.303 | +10.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 364 | +0.303 | +10.41€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 79 | +0.352 | +3.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 79 | +0.352 | +3.83€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 328 | +0.415 | -13.20€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 328 | +0.415 | -13.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 146 | +0.412 | -6.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 146 | +0.412 | -6.63€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 150 | +0.421 | -5.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 150 | +0.421 | -5.42€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 32 | +0.353 | -1.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 32 | +0.353 | -1.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 243 | +0.104 | +1.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 71 | +0.144 | +5.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 172 | +0.086 | -3.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 8 | +0.120 | +4.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 8 | +0.120 | +4.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 200 | +0.099 | +0.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 28 | +0.167 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 172 | +0.086 | -3.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 35 | +0.068 | -2.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 35 | +0.068 | -2.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 6643 | +0.097 | -213.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 676 | +0.060 | -29.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 5967 | +0.102 | -183.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 4526 | +0.097 | -98.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 676 | +0.060 | -29.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 3850 | +0.103 | -69.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 93 | +0.100 | -0.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 93 | +0.100 | -0.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 2024 | +0.099 | -113.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 2024 | +0.099 | -113.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 437 | +0.293 | -20.83€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 437 | +0.293 | -20.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 437 | +0.293 | -20.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 437 | +0.293 | -20.83€ | 0 | 4 |
| ✅ GBM_LATE_15M | 7839 | +0.043 | +2487.81€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 7839 | +0.043 | +2487.81€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 1068 | +0.171 | +661.02€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 1068 | +0.171 | +661.02€ | 0 | 20 |
| ✅ GBM_LATE_15M#BTC | 1109 | +0.171 | +631.88€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 1109 | +0.171 | +631.88€ | 0 | 29 |
| ✅ GBM_LATE_15M#DOGE | 1072 | +0.188 | +734.48€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 1072 | +0.188 | +734.48€ | 0 | 19 |
| ✅ GBM_LATE_15M#ETH | 1278 | -0.044 | +42.36€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 1278 | -0.044 | +42.36€ | 2 | 11 |
| ✅ GBM_LATE_15M#SOL | 1439 | -0.048 | +126.77€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 1439 | -0.048 | +126.77€ | 4 | 3 |
| ✅ GBM_LATE_15M#XRP | 1873 | -0.057 | +291.29€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 1873 | -0.057 | +291.29€ | 4 | 6 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 8775 | +0.046 | +3480.92€ | 0 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 8775 | +0.046 | +3480.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 1360 | -0.018 | +675.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 1360 | -0.018 | +675.71€ | 2 | 4 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 1913 | -0.039 | +154.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 1913 | -0.039 | +154.82€ | 1 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 941 | +0.239 | +857.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 941 | +0.239 | +857.56€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 1460 | -0.046 | +7.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 1460 | -0.046 | +7.71€ | 8 | 2 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 1560 | -0.021 | +344.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 1560 | -0.021 | +344.07€ | 7 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 1541 | +0.243 | +1441.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 1541 | +0.243 | +1441.05€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 6359 | +0.169 | +4347.35€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 6359 | +0.169 | +4347.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 819 | +0.183 | +570.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 819 | +0.183 | +570.78€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 1079 | +0.161 | +716.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 1079 | +0.161 | +716.93€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 802 | +0.203 | +625.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 802 | +0.203 | +625.15€ | 0 | 18 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 1056 | +0.160 | +678.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 1056 | +0.160 | +678.50€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 1213 | +0.123 | +708.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 1213 | +0.123 | +708.20€ | 1 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 1390 | +0.193 | +1047.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 1390 | +0.193 | +1047.79€ | 0 | 22 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 1139 | +0.086 | +265.90€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 1139 | +0.086 | +265.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 56 | +0.086 | +14.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 56 | +0.086 | +14.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 324 | +0.114 | +118.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 324 | +0.114 | +118.08€ | 3 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 88 | +0.156 | +42.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 88 | +0.156 | +42.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 213 | +0.184 | +76.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 213 | +0.184 | +76.93€ | 1 | 19 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 310 | -0.022 | -0.74€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 310 | -0.022 | -0.74€ | 5 | 3 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 148 | +0.060 | +14.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 148 | +0.060 | +14.84€ | 0 | 6 |
| ✅ GBM_LATE_15M_TARDIO | 7426 | +0.169 | +4946.34€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#15min | 7426 | +0.169 | +4946.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 1021 | +0.192 | +740.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 1021 | +0.192 | +740.37€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 1210 | +0.160 | +762.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 1210 | +0.160 | +762.09€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 1011 | +0.218 | +837.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 1011 | +0.218 | +837.14€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 1145 | +0.147 | +672.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 1145 | +0.147 | +672.11€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 1330 | +0.106 | +659.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 1330 | +0.106 | +659.20€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 1709 | +0.196 | +1275.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 1709 | +0.196 | +1275.41€ | 0 | 23 |
| ✅ GBM_LATE_5M | 1753 | +0.133 | +815.18€ | 1 | 29 |
| ✅ GBM_LATE_5M#5min | 1753 | +0.133 | +815.18€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 91 | +0.210 | +64.35€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 91 | +0.210 | +64.35€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 679 | +0.131 | +358.09€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 679 | +0.131 | +358.09€ | 2 | 21 |
| ✅ GBM_LATE_5M#DOGE | 97 | +0.126 | +33.63€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 97 | +0.126 | +33.63€ | 0 | 6 |
| ✅ GBM_LATE_5M#ETH | 593 | +0.147 | +281.83€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 593 | +0.147 | +281.83€ | 0 | 28 |
| ✅ GBM_LATE_5M#SOL | 125 | -0.020 | +0.12€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 125 | -0.020 | +0.12€ | 3 | 0 |
| ✅ GBM_LATE_5M#XRP | 168 | +0.153 | +77.16€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 168 | +0.153 | +77.16€ | 0 | 0 |
| ✅ GBM_LATE_60M | 520 | -0.035 | +86.81€ | 5 | 9 |
| ✅ GBM_LATE_60M#60min | 520 | -0.035 | +86.81€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 179 | +0.003 | +5.34€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 179 | +0.003 | +5.34€ | 2 | 3 |
| ✅ GBM_LATE_60M#ETH | 187 | -0.003 | +57.88€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 187 | -0.003 | +57.88€ | 2 | 8 |
| ✅ GBM_LATE_60M#SOL | 154 | -0.115 | +23.59€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 154 | -0.115 | +23.59€ | 2 | 0 |
| 🚫 GBM_LATE_60M_FADE | 195 | -0.302 | -33.28€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 195 | -0.302 | -33.28€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 77 | -0.260 | -7.87€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 77 | -0.260 | -7.87€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 65 | -0.351 | -19.05€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 65 | -0.351 | -19.05€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 53 | -0.282 | -6.35€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 53 | -0.282 | -6.35€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 337 | +0.037 | +1.82€ | 2 | 1 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 337 | +0.037 | +1.82€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 135 | +0.025 | +6.31€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 135 | +0.025 | +6.31€ | 1 | 5 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 85 | +0.063 | -0.03€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 85 | +0.063 | -0.03€ | 0 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 117 | +0.029 | -4.47€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 117 | +0.029 | -4.47€ | 2 | 5 |
| ✅ LATE_WINDOW_5MIN | 17 | +0.201 | +4.34€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 17 | +0.201 | +4.34€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 17 | +0.201 | +4.34€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 17 | +0.201 | +4.34€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 316 | +0.116 | +96.47€ | 0 | 5 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 316 | +0.116 | +96.47€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 316 | +0.116 | +96.47€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 316 | +0.116 | +96.47€ | 0 | 5 |
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
| ✅ LIQUIDACIONES_15M#XRP#15min | 46 | -0.167 | -8.95€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 682 | -0.029 | -17.52€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 682 | -0.029 | -17.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 41 | -0.058 | -4.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 41 | -0.058 | -4.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 108 | -0.036 | -1.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 108 | -0.036 | -1.01€ | 1 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 67 | -0.094 | -7.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 67 | -0.094 | -7.35€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 189 | +0.018 | +10.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 189 | +0.018 | +10.31€ | 2 | 3 |
| ✅ LIQUIDACIONES_5M#SOL | 227 | -0.011 | -6.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 227 | -0.011 | -6.38€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 50 | -0.154 | -8.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 50 | -0.154 | -8.60€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M | 449 | -0.005 | -1.98€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 449 | -0.005 | -1.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 142 | -0.035 | -9.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 142 | -0.035 | -9.94€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 141 | +0.004 | +1.89€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 141 | +0.004 | +1.89€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M#SOL | 166 | +0.012 | +6.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 166 | +0.012 | +6.06€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 4592 | -0.003 | -76.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 4592 | -0.003 | -76.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 520 | -0.008 | +0.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 520 | -0.008 | +0.39€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 598 | +0.005 | -8.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 598 | +0.005 | -8.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 802 | -0.007 | -26.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 802 | -0.007 | -26.55€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 937 | +0.009 | +14.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 937 | +0.009 | +14.16€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 823 | -0.002 | -24.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 823 | -0.002 | -24.45€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 912 | -0.014 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 912 | -0.014 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 6900 | -0.036 | +177.58€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 6900 | -0.036 | +177.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 1092 | -0.032 | +124.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 1092 | -0.032 | +124.63€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 1222 | -0.037 | -33.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 1222 | -0.037 | -33.74€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 1102 | -0.042 | +98.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 1102 | -0.042 | +98.11€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 1228 | -0.034 | -31.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 1228 | -0.034 | -31.93€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 1125 | -0.040 | +31.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 1125 | -0.040 | +31.29€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 1131 | -0.030 | -10.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 1131 | -0.030 | -10.79€ | 4 | 0 |
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
| ✅ MOMENTUM_IBS_5M | 3167 | +0.004 | -4.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3167 | +0.004 | -4.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 126 | -0.039 | -1.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 126 | -0.039 | -1.34€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 185 | +0.008 | -2.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 185 | +0.008 | -2.27€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 136 | +0.000 | -1.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 136 | +0.000 | -1.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1157 | +0.008 | +8.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1157 | +0.008 | +8.29€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1385 | +0.006 | -2.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1385 | +0.006 | -2.03€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 178 | -0.006 | -5.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 178 | -0.006 | -5.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 19025 | -0.075 | +268.66€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 19025 | -0.075 | +268.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 2949 | -0.091 | +325.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 2949 | -0.091 | +325.29€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 3366 | -0.062 | -16.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 3366 | -0.062 | -16.99€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 3049 | -0.086 | +18.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 3049 | -0.086 | +18.74€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 2883 | -0.100 | -194.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 2883 | -0.100 | -194.71€ | 8 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 3579 | -0.048 | -0.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 3579 | -0.048 | -0.74€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 3199 | -0.073 | +137.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 3199 | -0.073 | +137.08€ | 5 | 0 |
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
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 725 | -0.020 | -23.89€ | 2 | 0 |
| ✅ ORDER_FLOW_5M | 429 | +0.096 | +107.64€ | 1 | 4 |
| ✅ ORDER_FLOW_5M#5min | 293 | +0.114 | +95.05€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 89 | +0.148 | +46.80€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 89 | +0.148 | +46.80€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#DOGE | 56 | +0.103 | +13.06€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 56 | +0.103 | +13.06€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#ETH | 39 | +0.134 | +15.32€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 39 | +0.134 | +15.32€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL | 46 | +0.125 | +14.98€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 46 | +0.125 | +14.98€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 63 | +0.038 | +4.88€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 63 | +0.038 | +4.88€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM | 263 | -0.160 | -22.11€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC | 117 | -0.239 | -34.16€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC#atexpiry | 102 | -0.269 | -33.43€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 15 | -0.022 | -0.74€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 99 | -0.134 | -3.00€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 80 | -0.146 | -5.97€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 19 | -0.068 | +2.97€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 47 | -0.010 | +15.05€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 40 | +0.000 | +14.48€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 7 | -0.019 | +0.57€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 222 | -0.179 | -24.92€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 41 | -0.058 | +2.80€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE | 195 | -0.175 | +26.88€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 79 | -0.080 | +22.40€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 77 | -0.070 | +23.42€ | 0 | 2 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 79 | -0.265 | -12.00€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 75 | -0.266 | -13.39€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 37 | -0.167 | +16.48€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 35 | -0.149 | +18.31€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#atexpiry | 187 | -0.167 | +28.35€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#reach | 8 | -0.120 | -1.47€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 64 | +0.303 | +13.85€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC | 17 | -0.022 | -2.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 17 | -0.022 | -2.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 19 | +0.294 | +2.30€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 19 | +0.294 | +2.30€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 28 | +0.467 | +14.50€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 28 | +0.467 | +14.50€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#sniper | 64 | +0.303 | +13.85€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 149 | -0.017 | -10.97€ | 3 | 1 |
| ✅ STREAK_FADE_15M#15min | 149 | -0.017 | -10.97€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 62 | -0.031 | -7.97€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 62 | -0.031 | -7.97€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 10 | +0.000 | -0.13€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 10 | +0.000 | -0.13€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 13 | +0.065 | +2.23€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 13 | +0.065 | +2.23€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP | 64 | -0.030 | -5.10€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 64 | -0.030 | -5.10€ | 0 | 0 |
| ✅ STREAK_FADE_5M | 1103 | -0.023 | -53.67€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 1103 | -0.023 | -53.67€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 392 | -0.023 | -15.21€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 392 | -0.023 | -15.21€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 384 | -0.005 | -10.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 384 | -0.005 | -10.20€ | 3 | 0 |
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
| ✅ STREAK_MOM_5M | 2248 | +0.032 | +52.30€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 2248 | +0.032 | +52.30€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 744 | +0.034 | +15.01€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 744 | +0.034 | +15.01€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 412 | +0.024 | +6.81€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 412 | +0.024 | +6.81€ | 1 | 1 |
| ✅ STREAK_MOM_5M#SOL | 674 | +0.033 | +11.63€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 674 | +0.033 | +11.63€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 418 | +0.033 | +18.86€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 418 | +0.033 | +18.86€ | 2 | 1 |
| ✅ STRUCT_NO_15M | 3155 | +0.008 | -29.55€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 3155 | +0.008 | -29.55€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 1216 | +0.010 | -10.46€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 1216 | +0.010 | -10.46€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 1224 | +0.017 | -0.55€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 1224 | +0.017 | -0.55€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 715 | -0.011 | -18.53€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 715 | -0.011 | -18.53€ | 2 | 0 |
| ✅ UPDOWN_GBM | 6168 | +0.005 | +145.31€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 2276 | +0.044 | +224.63€ | 0 | 8 |
| ✅ UPDOWN_GBM#240min | 260 | +0.015 | +2.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 3200 | -0.019 | -74.02€ | 2 | 0 |
| ✅ UPDOWN_GBM#60min | 385 | -0.012 | -7.73€ | 3 | 0 |
| ✅ UPDOWN_GBM#BNB | 196 | +0.091 | +38.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 179 | +0.119 | +42.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 8 | -0.040 | -1.01€ | 0 | 0 |
| 🚫 UPDOWN_GBM#BNB#5min | 9 | -0.102 | -2.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 1368 | +0.015 | +57.55€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 225 | +0.073 | +29.93€ | 4 | 11 |
| ✅ UPDOWN_GBM#BTC#240min | 75 | +0.071 | +7.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 925 | +0.007 | +25.15€ | 3 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 125 | -0.035 | -6.62€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 777 | -0.006 | -0.98€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 122 | +0.105 | +29.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 9 | +0.021 | +0.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 646 | -0.028 | -30.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 1450 | +0.005 | +11.17€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 659 | +0.028 | +26.14€ | 1 | 6 |
| ✅ UPDOWN_GBM#ETH#240min | 76 | +0.077 | +6.33€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 531 | -0.029 | -22.25€ | 3 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 169 | +0.015 | +1.34€ | 0 | 1 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 1500 | -0.013 | -25.32€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 527 | -0.005 | -4.50€ | 1 | 2 |
| ✅ UPDOWN_GBM#SOL#240min | 60 | -0.032 | -4.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 810 | -0.012 | -13.81€ | 2 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 91 | -0.027 | -2.45€ | 1 | 3 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 875 | +0.009 | +66.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 564 | +0.060 | +101.43€ | 0 | 6 |
| ✅ UPDOWN_GBM#XRP#240min | 32 | -0.147 | -5.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 279 | -0.076 | -29.58€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 200 | +0.317 | +40.58€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 200 | +0.317 | +40.58€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 113 | +0.291 | +11.99€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 113 | +0.291 | +11.99€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 87 | +0.343 | +28.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 87 | +0.343 | +28.59€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 3896 | -0.076 | +807.58€ | 3 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 3896 | -0.076 | +807.58€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 303 | -0.051 | +341.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 303 | -0.051 | +341.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 801 | -0.165 | -94.45€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 801 | -0.165 | -94.45€ | 4 | 3 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 77 | +0.070 | +14.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 77 | +0.070 | +14.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 305 | +0.129 | +136.52€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 305 | +0.129 | +136.52€ | 2 | 17 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 1240 | -0.075 | +201.88€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 1240 | -0.075 | +201.88€ | 4 | 1 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 1170 | -0.086 | +207.83€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 1170 | -0.086 | +207.83€ | 3 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 30 | +0.000 | -1.64€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 30 | +0.000 | -1.64€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 30 | +0.000 | -1.64€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 30 | +0.000 | -1.64€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 314 | +0.279 | +234.47€ | 0 | 13 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 314 | +0.279 | +234.47€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 176 | +0.258 | +117.61€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 176 | +0.258 | +117.61€ | 0 | 12 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 138 | +0.300 | +116.86€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 138 | +0.300 | +116.86€ | 0 | 12 |
| ✅ UPDOWN_OU_5M | 462 | -0.071 | -34.49€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#5min | 462 | -0.071 | -34.49€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 263 | -0.047 | -23.12€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 263 | -0.047 | -23.12€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 67 | +0.065 | +12.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 67 | +0.065 | +12.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 30 | -0.188 | -6.21€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 30 | -0.188 | -6.21€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 35 | -0.149 | -4.81€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 35 | -0.149 | -4.81€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 36 | -0.184 | -5.77€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 36 | -0.184 | -5.77€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 31 | -0.197 | -6.80€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 31 | -0.197 | -6.80€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 1100 | +0.288 | +450.80€ | 0 | 5 |
| ✅ WEEKLY_PRICE#BTC | 329 | +0.204 | -2.32€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 346 | +0.262 | +82.89€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 425 | +0.371 | +370.23€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.088) — sin ventaja clara. oversold(IBS<0.3): IC=+0.010 n=2184 | neutral: IC=+0.001 n=2341 | overbought(IBS>0.7): IC=+0.089 n=2424
  - _Datos_: n=7265 IC=+0.035 PNL=+637.96€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: (cache 785s) 24 celda(s) GATE OK de 2093 trackeadas

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=-0.005 < 0.08 — monitorear
  - _Datos_: n=527 IC=-0.005 PNL=-4.50€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=346/15 IC=+0.262 PNL=+82.89€ | BTC: n=329/15 IC=+0.204 PNL=-2.32€ | SOL: n=425/15 IC=+0.371 PNL=+370.23€

**🟡 H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.076 n=99471 | tras_1loss IC=+0.045 n=77351 | tras_2loss IC=+0.008 n=35147/40 | gap=+0.068 (umbral 0.05)

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
  - _Estado_: 6106 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.128 n=41/60 | contraria IC=+0.000 n=24 | gap=+0.128 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=60, boost estimado=+0.020. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 46/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=169/40 IC=+0.015 PNL=+1.34€ | BTC#60min: n=125/40 IC=-0.035 PNL=-6.62€ | SOL#60min: n=91/40 IC=-0.027 PNL=-2.45€

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=-0.014 n=659 | contrario_BTC IC=-0.015 n=487/40 | gap=-0.001 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.331 > 0.1 con n=933 PNL=+451.25€
  - _Datos_: n=933 IC=+0.331 PNL=+451.25€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=55 IC=+0.026 PNL=+10.36€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=55 IC=+0.026 PNL=+10.36€

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
  - _Estado_: n=5921 IC=+0.001 PNL=+95.64€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=5921 IC=+0.001 PNL=+95.64€

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
  - _Estado_: n=318 IC=+0.009 PNL=+0.72€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=318 IC=+0.009 PNL=+0.72€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=67 IC=-0.109 PNL=-8.45€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=67 IC=-0.109 PNL=-8.45€

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
  - _Estado_: n=225 IC=+0.073 PNL=+29.93€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=225 IC=+0.073 PNL=+29.93€

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
  - _Estado_: n=1324 IC=+0.028 PNL=+79.71€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1324 IC=+0.028 PNL=+79.71€

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
  - _Estado_: n=2185 IC=-0.018 PNL=-49.78€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2185 IC=-0.018 PNL=-49.78€

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
  - _Estado_: 17/30 ops en el filtro definido (IC actual=+0.201 PNL=+4.34€)
  - _Datos_: n=17 IC=+0.201 PNL=+4.34€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=1643 IC=+0.023 PNL=+101.46€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1643 IC=+0.023 PNL=+101.46€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=444 IC=+0.034 PNL=-0.14€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=444 IC=+0.034 PNL=-0.14€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.092 > 0.08 con n=101 PNL=+20.85€
  - _Datos_: n=101 IC=+0.092 PNL=+20.85€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.142 > 0.08 con n=118 PNL=+2.09€
  - _Datos_: n=118 IC=+0.142 PNL=+2.09€

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
  - _Estado_: n=12139 IC=+0.099 PNL=+3445.48€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=12139 IC=+0.099 PNL=+3445.48€

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
  - _Estado_: n=825 IC=+0.030 PNL=+50.11€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=825 IC=+0.030 PNL=+50.11€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.128 > 0.02 con n=221 PNL=+65.57€
  - _Datos_: n=221 IC=+0.128 PNL=+65.57€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.441 > 0.1 con n=594 PNL=+497.80€
  - _Datos_: n=594 IC=+0.441 PNL=+497.80€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=1510 IC=+0.025 PNL=+80.46€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=1510 IC=+0.025 PNL=+80.46€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.165 > 0.1 con n=771 PNL=+280.34€
  - _Datos_: n=771 IC=+0.165 PNL=+280.34€

**⏳ H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: 40
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: 25/40 ops en el filtro definido (IC actual=-0.278 PNL=-6.42€)
  - _Datos_: n=25 IC=-0.278 PNL=-6.42€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=430 IC=+0.049 PNL=+60.11€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=430 IC=+0.049 PNL=+60.11€

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
  - _Estado_: n=4505 IC=-0.142 PNL=+197.49€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4505 IC=-0.142 PNL=+197.49€

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
  - _Estado_: n=595 IC=+0.138 PNL=+236.75€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=595 IC=+0.138 PNL=+236.75€

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
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.227 < -0.1 con n=496 PNL=-42.13€
  - _Datos_: n=496 IC=-0.227 PNL=-42.13€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=1175 IC=+0.140 PNL=+604.90€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=1175 IC=+0.140 PNL=+604.90€

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
  - _Estado_: n=655 IC=-0.022 PNL=+51.09€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=655 IC=-0.022 PNL=+51.09€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.177 > 0.08 con n=564 PNL=+326.90€
  - _Datos_: n=564 IC=+0.177 PNL=+326.90€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=993 IC=-0.048 PNL=+171.64€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=993 IC=-0.048 PNL=+171.64€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.115 > 0.08 con n=250 PNL=-33.01€
  - _Datos_: n=250 IC=+0.115 PNL=-33.01€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.243 > 0.08 con n=1437 PNL=-123.68€
  - _Datos_: n=1437 IC=+0.243 PNL=-123.68€

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
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.123 n=165) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=165 IC=+0.123 PNL=+49.58€

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
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.431 n=230) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=230 IC=+0.431 PNL=+311.18€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=3066 IC=+0.127 PNL=-564.18€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=3066 IC=+0.127 PNL=-564.18€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.174 > 0.1 con n=41 PNL=+21.67€
  - _Datos_: n=41 IC=+0.174 PNL=+21.67€
