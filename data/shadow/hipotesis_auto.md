# Hipótesis automáticas — 2026-08-28 00:02 UTC
_Generado por shadow_postmortem.py sobre 180719 resoluciones (PNL=+13090.85€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.705` → IC=-0.167 (n=88)

  - _Acción_: SKIP cuando `py_entrada` < 0.705
  - _Potencial_: sin este filtro IC_bueno=+0.276 (n=244)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.286 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.159)

- **PATRÓN** `n_ballena_banda` > `17.0` → IC=+0.169 (n=252)

  - _Acción_: Kelly boost +0.85€ cuando `n_ballena_banda` > 17.0 (IC base=+0.159)

- **PATRÓN** `n_total_lado` > `59.0` → IC=+0.238 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 59.0 (IC base=+0.159)

- **PATRÓN** `banda_hit_calibrado` > `0.8219` → IC=+0.278 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8219 (IC base=+0.159)

- **PATRÓN** `banda_z` > `9.958` → IC=+0.257 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.958 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.195 (n=175)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 11.0 (IC base=+0.159)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.183 (n=260)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.01 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `3148.4626` → IC=+0.239 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3148.4626 (IC base=+0.159)

- **PATRÓN** `ballena_activa_n` < `288.0` → IC=+0.302 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 288.0 (IC base=+0.159)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.136 (n=215)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.5 (IC base=+0.011)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.73` → IC=+0.288 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.199)

- **PATRÓN** `n_ballena_banda` > `19.0` → IC=+0.210 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `n_ballena_banda` > 19.0 (IC base=+0.199)

- **PATRÓN** `n_total_lado` > `52.0` → IC=+0.247 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 52.0 (IC base=+0.199)

- **PATRÓN** `banda_hit_calibrado` > `0.8265` → IC=+0.307 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8265 (IC base=+0.199)

- **PATRÓN** `banda_z` > `11.967` → IC=+0.297 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.967 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.230 (n=150)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.208 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `3838.6557` → IC=+0.263 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3838.6557 (IC base=+0.199)

- **PATRÓN** `ballena_activa_n` < `290.0` → IC=+0.309 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 290.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.126 (n=113)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.495 (IC base=+0.000)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.335` → IC=-0.267 (n=28)

  - _Acción_: SKIP cuando `py_entrada` < 0.335
  - _Potencial_: sin este filtro IC_bueno=+0.197 (n=87)

- **FILTRO** `banda_hit_calibrado` < `0.6284` → IC=-0.218 (n=37)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.6284
  - _Potencial_: sin este filtro IC_bueno=+0.225 (n=78)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.145 (n=91)

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

- **PATRÓN** `py_entrada` > `0.335` → IC=+0.197 (n=87)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.335 (IC base=+0.081)

- **PATRÓN** `banda_hit_calibrado` > `0.6284` → IC=+0.225 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6284 (IC base=+0.081)

- **PATRÓN** `banda_z` > `8.092` → IC=+0.191 (n=40)

  - _Acción_: Kelly boost +0.95€ cuando `banda_z` > 8.092 (IC base=+0.081)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.145 (n=91)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.02 (IC base=+0.081)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.134 (n=69)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.495 (IC base=-0.024)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `147.7` → IC=-0.285 (n=2521)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 147.7
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=7565)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `136.39` → IC=-0.243 (n=309)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 136.39
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=928)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` > `628.69` → IC=-0.188 (n=245)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` > 628.69
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=476)

- **FILTRO** `restante_s_al_confirmar` < `400.88` → IC=-0.247 (n=180)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 400.88
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=541)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `104.55` → IC=-0.410 (n=322)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 104.55
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=968)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `161.14` → IC=-0.172 (n=682)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 161.14
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=2047)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `148.13` → IC=-0.286 (n=588)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 148.13
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=1769)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `120.59` → IC=-0.373 (n=438)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 120.59
  - _Potencial_: sin este filtro IC_bueno=-0.112 (n=1314)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.7` → IC=+0.190 (n=5611)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.7 (IC base=+0.099)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.171 (n=1613)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.01 (IC base=+0.099)

- **PATRÓN** `libro_liquidez` > `2376.0723` → IC=+0.174 (n=1558)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2376.0723 (IC base=+0.099)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.146 (n=3351)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 18.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.157 (n=4359)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 7.0 (IC base=+0.141)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.258 (n=3486)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.187 (n=3014)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.02 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `1888.2922` → IC=+0.178 (n=2524)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 1888.2922 (IC base=+0.141)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.220 (n=637)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.206)

- **PATRÓN** `py_entrada` > `0.785` → IC=+0.382 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.785 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.208 (n=811)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `13027.6931` → IC=+0.216 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13027.6931 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.192 (n=602)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 7.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.187 (n=663)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 17.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` < `0.365` → IC=+0.255 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.365 (IC base=+0.182)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.181 (n=852)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.182)

- **PATRÓN** `libro_liquidez` > `12563.1974` → IC=+0.216 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12563.1974 (IC base=+0.182)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.133 (n=551)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.136 (n=470)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 15.0 (IC base=+0.120)

- **PATRÓN** `py_entrada` > `0.555` → IC=+0.137 (n=546)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` > 0.555 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `4886.5239` → IC=+0.164 (n=206)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 4886.5239 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.192 (n=186)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 7.0 (IC base=+0.132)

- **PATRÓN** `py_entrada` < `0.415` → IC=+0.176 (n=304)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.415 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `4191.7874` → IC=+0.148 (n=288)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 4191.7874 (IC base=+0.132)

### FAVORITO_CONFIRMADO#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.135 (n=1260)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.127 (n=1057)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 15.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` > `0.69` → IC=+0.312 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.282 (n=324)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.276)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.279 (n=486)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.276)

- **PATRÓN** `py_entrada` < `0.195` → IC=+0.411 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.195 (IC base=+0.276)

- **PATRÓN** `libro_liquidez` > `2923.071` → IC=+0.288 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2923.071 (IC base=+0.276)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.141 (n=288)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 8.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.157 (n=284)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 15.0 (IC base=+0.138)

- **PATRÓN** `py_entrada` > `0.655` → IC=+0.252 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.655 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.146 (n=394)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.02 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `1953.7352` → IC=+0.157 (n=322)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 1953.7352 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `4420.281` → IC=+0.157 (n=141)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 4420.281 (IC base=+0.078)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.203 (n=947)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.198 (n=650)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 12.0 (IC base=+0.194)

- **PATRÓN** `py_entrada` > `0.845` → IC=+0.450 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.845 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.258 (n=225)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` < `0.205` → IC=+0.356 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.205 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.229 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `1888.2922` → IC=+0.236 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1888.2922 (IC base=+0.221)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.219 (n=94)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.345 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.239 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `3459.0838` → IC=+0.188 (n=62)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 3459.0838 (IC base=+0.190)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.214 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.144 (n=273)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.02 (IC base=+0.102)

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

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.194 (n=4682)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.191 (n=3941)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.187)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.200 (n=2225)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.187)

- **PATRÓN** `libro_liquidez` > `3146.218` → IC=+0.360 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3146.218 (IC base=+0.187)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.170 (n=1143)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 6.0 (IC base=+0.166)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.179 (n=1011)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.166)

- **PATRÓN** `py_entrada` < `0.72` → IC=+0.174 (n=1015)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.72 (IC base=+0.166)

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
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.171 (n=1132)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 6.0 (IC base=+0.163)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.169 (n=995)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 15.0 (IC base=+0.163)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.168 (n=426)

  - _Acción_: Kelly boost +0.84€ cuando `py_entrada` < 0.7 (IC base=+0.163)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.172 (n=795)

  - _Acción_: Kelly boost +0.86€ cuando `py_entrada` > 0.72 (IC base=+0.163)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.242 (n=1066)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.229)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.319 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.229)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.194 (n=1149)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.184 (n=973)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 15.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.201 (n=574)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.7 (IC base=+0.183)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.455 (n=221)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.445)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.443 (n=210)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.445)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.449 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.445)

- **PATRÓN** `libro_liquidez` > `3355.2252` → IC=+0.462 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3355.2252 (IC base=+0.445)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.445 (n=89)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.441)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.438 (n=79)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.441)

- **PATRÓN** `libro_liquidez` > `12599.6821` → IC=+0.452 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12599.6821 (IC base=+0.441)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.452 (n=81)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.430)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.435 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.430)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.430 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.430)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.429 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.430)

- **PATRÓN** `libro_liquidez` > `3860.0656` → IC=+0.476 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3860.0656 (IC base=+0.430)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.443 (n=51)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.448)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.451 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.448)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.451 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.448)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.442 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.448)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.204 (n=4330)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.191 (n=8996)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 12.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.220 (n=9199)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.191)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.132 (n=2365)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 6.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.130 (n=1657)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 12.0 (IC base=+0.127)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.155 (n=1811)

  - _Acción_: Kelly boost +0.77€ cuando `py_entrada` > 0.71 (IC base=+0.127)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.241 (n=2026)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.235)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.284 (n=1148)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.235)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.194 (n=743)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 18.0 (IC base=+0.165)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.167 (n=1539)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 12.0 (IC base=+0.165)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.205 (n=1044)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.165)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.233 (n=2078)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.228)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.230 (n=971)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.228)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.290 (n=714)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.228)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.231 (n=707)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.217)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.244 (n=1248)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.217)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.196 (n=732)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 18.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.192 (n=1516)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 12.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.212 (n=1589)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.185)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.200 (n=1692)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.133)

- **PATRÓN** `restante_min` < `3.96` → IC=+0.136 (n=1554)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` < 3.96 (IC base=+0.133)

- **PATRÓN** `restante_min` > `4.93` → IC=+0.162 (n=1601)

  - _Acción_: Kelly boost +0.81€ cuando `restante_min` > 4.93 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.150 (n=2243)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 8.0 (IC base=+0.133)

- **PATRÓN** `lag_apertura_s` < `6.48` → IC=+0.158 (n=2048)

  - _Acción_: Kelly boost +0.79€ cuando `lag_apertura_s` < 6.48 (IC base=+0.133)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.203 (n=852)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.140)

- **PATRÓN** `restante_min` < `3.93` → IC=+0.141 (n=778)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` < 3.93 (IC base=+0.140)

- **PATRÓN** `restante_min` > `4.91` → IC=+0.165 (n=827)

  - _Acción_: Kelly boost +0.82€ cuando `restante_min` > 4.91 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.162 (n=1110)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 8.0 (IC base=+0.140)

- **PATRÓN** `lag_apertura_s` < `5.37` → IC=+0.163 (n=772)

  - _Acción_: Kelly boost +0.81€ cuando `lag_apertura_s` < 5.37 (IC base=+0.140)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.197 (n=840)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.38 (IC base=+0.127)

- **PATRÓN** `restante_min` < `4.02` → IC=+0.127 (n=780)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.02 (IC base=+0.127)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.167 (n=845)

  - _Acción_: Kelly boost +0.84€ cuando `restante_min` > 4.94 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.129 (n=2346)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.138 (n=1133)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 8.0 (IC base=+0.127)

- **PATRÓN** `lag_apertura_s` < `3.44` → IC=+0.173 (n=779)

  - _Acción_: Kelly boost +0.87€ cuando `lag_apertura_s` < 3.44 (IC base=+0.127)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.319 (n=527)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.301)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.305 (n=609)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.301)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.378 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.8 (IC base=+0.301)

- **PATRÓN** `libro_liquidez` > `3861.5788` → IC=+0.307 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3861.5788 (IC base=+0.301)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.307 (n=226)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.286)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.288 (n=229)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.286)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.362 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.286)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.287 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `5623.4735` → IC=+0.326 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5623.4735 (IC base=+0.286)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.330 (n=198)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.300)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.310 (n=282)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.300)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.389 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.300)

- **PATRÓN** `libro_liquidez` > `1850.387` → IC=+0.315 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1850.387 (IC base=+0.300)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.379 (n=56)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.354)

- **PATRÓN** `py_entrada` > `0.91` → IC=+0.409 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.91 (IC base=+0.354)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.364 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.354)

- **PATRÓN** `libro_liquidez` > `763.8012` → IC=+0.371 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 763.8012 (IC base=+0.354)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.427 (n=230)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.416)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.425 (n=252)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.416)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.425 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.416)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.429 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.416)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.415 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.416)

- **PATRÓN** `libro_liquidez` > `2089.6231` → IC=+0.429 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2089.6231 (IC base=+0.416)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.422 (n=114)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.414)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.430 (n=112)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.414)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.419 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.414)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.424 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.414)

- **PATRÓN** `libro_liquidez` > `5536.1709` → IC=+0.450 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5536.1709 (IC base=+0.414)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.427 (n=108)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.422)

- **PATRÓN** `hora_utc` < `19.0` → IC=+0.421 (n=125)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 19.0 (IC base=+0.422)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.443 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.422)

- **PATRÓN** `py_entrada` > `0.91` → IC=+0.427 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.91 (IC base=+0.422)

- **PATRÓN** `libro_liquidez` > `1842.491` → IC=+0.442 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1842.491 (IC base=+0.422)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.313 (n=303)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.292)

- **PATRÓN** `py_entrada` > `0.87` → IC=+0.447 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.87 (IC base=+0.292)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.310 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `1692.7461` → IC=+0.342 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1692.7461 (IC base=+0.292)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.313 (n=303)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.292)

- **PATRÓN** `py_entrada` > `0.87` → IC=+0.447 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.87 (IC base=+0.292)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.310 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `1692.7461` → IC=+0.342 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1692.7461 (IC base=+0.292)

### GBM_LATE_15M
- **PATRÓN** `ibs_20min` > `0.9497` → IC=+0.208 (n=788)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9497 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` > `0.189` → IC=+0.230 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.189 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` < `0.9606` → IC=+0.210 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9606 (IC base=+0.067)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.221` → IC=+0.159 (n=951)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 5.221 (IC base=+0.067)

- **PATRÓN** `volumen_regimen` < `0.6304` → IC=+0.212 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6304 (IC base=+0.067)

- **PATRÓN** `volumen_regimen` > `1.0648` → IC=+0.243 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0648 (IC base=+0.067)

- **PATRÓN** `volumen_pendiente_norm` > `0.3076` → IC=+0.161 (n=184)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.3076 (IC base=+0.067)

- **PATRÓN** `volumen_spike_ratio` < `2.443` → IC=+0.148 (n=1132)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.443 (IC base=+0.067)

- **PATRÓN** `ibs_20min` < `0.2167` → IC=+0.132 (n=1595)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.2167 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` < `0.3014` → IC=+0.141 (n=804)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.3014 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` < `0.6279` → IC=+0.153 (n=260)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6279 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` > `1.0494` → IC=+0.142 (n=353)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 1.0494 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.3031` → IC=+0.274 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3031 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` > `2.9116` → IC=+0.230 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9116 (IC base=+0.029)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.235 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 45.0 (IC base=+0.029)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.165 (n=240)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0071 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.163 (n=250)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 8.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.281 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.843` → IC=+0.319 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.843 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.1454` → IC=+0.143 (n=124)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.1454 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.149 (n=331)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.04 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.282 (n=195)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0061 (IC base=+0.260)

- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.290 (n=98)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0073 (IC base=+0.260)

- **PATRÓN** `drift_60min` |x|≤ `0.2372` → IC=+0.291 (n=257)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2372 (IC base=+0.260)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.261 (n=261)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.260)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.277 (n=258)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.260)

- **PATRÓN** `ibs_20min` < `0.4375` → IC=+0.299 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4375 (IC base=+0.260)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.934` → IC=+0.297 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.934 (IC base=+0.260)

- **PATRÓN** `volumen_pendiente_norm` < `0.0601` → IC=+0.266 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0601 (IC base=+0.260)

- **PATRÓN** `volumen_pendiente_norm` > `0.299` → IC=+0.288 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.299 (IC base=+0.260)

- **PATRÓN** `volumen_spike_ratio` < `1.8288` → IC=+0.264 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8288 (IC base=+0.260)

- **PATRÓN** `volumen_spike_ratio` > `1.5851` → IC=+0.269 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5851 (IC base=+0.260)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.315 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.260)

- **PATRÓN** `libro_liquidez` > `1968.0502` → IC=+0.300 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1968.0502 (IC base=+0.260)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.272 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.260)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.229 (n=264)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.207)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.226 (n=133)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.0953` → IC=+0.231 (n=132)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0953 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.234 (n=404)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.207 (n=374)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `0.4206` → IC=+0.221 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4206 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `0.2143` → IC=+0.230 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2143 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.332` → IC=+0.220 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.332 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` < `1.2629` → IC=+0.214 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2629 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` > `1.0844` → IC=+0.236 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0844 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` < `0.0964` → IC=+0.207 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0964 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.267` → IC=+0.227 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.267 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `1.4472` → IC=+0.259 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4472 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `11341.8291` → IC=+0.219 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11341.8291 (IC base=+0.207)

- **PATRÓN** `ballena_activa_n` < `309.0` → IC=+0.204 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 309.0 (IC base=+0.207)

- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.169 (n=152)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0022 (IC base=+0.138)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.139 (n=206)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` > 0.0047 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.0753` → IC=+0.156 (n=152)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.0753 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.147 (n=429)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 7.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.147 (n=454)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 17.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.455` → IC=+0.172 (n=400)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.455 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.1372` → IC=+0.163 (n=378)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1372 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.938` → IC=+0.222 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.938 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.6279` → IC=+0.182 (n=152)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6279 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `1.0218` → IC=+0.144 (n=206)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.0218 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.0934` → IC=+0.203 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0934 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.7479` → IC=+0.174 (n=234)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.7479 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.4105` → IC=+0.157 (n=351)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.4105 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=586)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `13573.7225` → IC=+0.173 (n=206)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 13573.7225 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `218.0` → IC=+0.185 (n=87)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 218.0 (IC base=+0.138)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `hora_utc` < `6.0` → IC=+0.213 (n=165)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.277 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.912` → IC=+0.260 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.912 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` < `0.1415` → IC=+0.130 (n=368)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.1415 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.4138` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.4138 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `1.7273` → IC=+0.130 (n=393)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.7273 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.170 (n=422)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.04 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `1910.5673` → IC=+0.145 (n=215)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 1910.5673 (IC base=+0.141)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.302 (n=155)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0061 (IC base=+0.259)

- **PATRÓN** `drift_60min` |x|≤ `0.1318` → IC=+0.296 (n=155)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1318 (IC base=+0.259)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.279 (n=242)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.259)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.279 (n=134)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.259)

- **PATRÓN** `ibs_20min` < `0.5337` → IC=+0.299 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5337 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.037` → IC=+0.300 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.037 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.578` → IC=+0.264 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.578 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` > `0.4096` → IC=+0.414 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.4096 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` > `2.6796` → IC=+0.247 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6796 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.286 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.259)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.239 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 48.0 (IC base=+0.259)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `ibs_20min` > `0.8686` → IC=-0.157 (n=208)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8686
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=625)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.172 (n=65)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=768)

- **PATRÓN** `dist_vwap_pct` > `0.124` → IC=+0.333 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.124 (IC base=-0.035)

- **PATRÓN** `dist_vwap_pct` < `0.0838` → IC=+0.274 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0838 (IC base=-0.035)

- **PATRÓN** `volumen_regimen` < `1.0858` → IC=+0.284 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0858 (IC base=-0.035)

- **PATRÓN** `volumen_regimen` > `0.7026` → IC=+0.316 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7026 (IC base=-0.035)

- **PATRÓN** `volumen_pendiente_norm` > `0.1582` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1582 (IC base=-0.035)

- **PATRÓN** `volumen_spike_ratio` < `1.4384` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4384 (IC base=-0.035)

- **PATRÓN** `volumen_spike_ratio` > `2.1749` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1749 (IC base=-0.035)

- **PATRÓN** `dist_vwap_pct` > `0.1556` → IC=+0.197 (n=31)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1556 (IC base=-0.050)

- **PATRÓN** `volumen_pendiente_norm` > `0.0733` → IC=+0.260 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0733 (IC base=-0.050)

- **PATRÓN** `volumen_spike_ratio` > `2.4256` → IC=+0.179 (n=26)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 2.4256 (IC base=-0.050)

- **PATRÓN** `ballena_activa_n` < `138.0` → IC=+0.154 (n=53)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 138.0 (IC base=-0.050)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `ibs_20min` > `0.5` → IC=-0.139 (n=643)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=691)

- **FILTRO** `sigma_ewma_delta_pct` > `4.968` → IC=-0.157 (n=281)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.968
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=1053)

- **FILTRO** `volumen_pendiente_norm` < `0.0964` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.0964
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

- **FILTRO** `volumen_spike_ratio` > `1.6234` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.6234
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.197 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0055 (IC base=+0.052)

- **PATRÓN** `drift_60min` |x|≤ `0.2734` → IC=+0.125 (n=62)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.62€ cuando `drift_60min` |x|≤ 0.2734 (IC base=+0.052)

- **PATRÓN** `hora_utc` > `23.0` → IC=+0.203 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 23.0 (IC base=+0.052)

- **PATRÓN** `ibs_20min` > `0.5294` → IC=+0.172 (n=62)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.5294 (IC base=+0.052)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.4378` → IC=-0.171 (n=347)

  - _Acción_: SKIP cuando `ibs_20min` < 0.4378
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=347)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.169 (n=140)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=554)

- **FILTRO** `ibs_20min` > `0.7857` → IC=-0.172 (n=300)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7857
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=903)

- **FILTRO** `sigma_ewma_delta_pct` > `6.668` → IC=-0.155 (n=195)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.668
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=1008)

- **PATRÓN** `dist_vwap_pct` < `0.2396` → IC=+0.175 (n=38)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.2396 (IC base=-0.095)

- **PATRÓN** `volumen_regimen` > `0.6932` → IC=+0.183 (n=39)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 0.6932 (IC base=-0.095)

- **PATRÓN** `dist_vwap_pct` < `0.2029` → IC=+0.222 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2029 (IC base=-0.041)

- **PATRÓN** `volumen_regimen` < `0.6966` → IC=+0.226 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6966 (IC base=-0.041)

- **PATRÓN** `volumen_regimen` > `1.1355` → IC=+0.250 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1355 (IC base=-0.041)

- **PATRÓN** `volumen_spike_ratio` > `1.9721` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.9721 (IC base=-0.041)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.139 (n=1346)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` > 0.0077 (IC base=+0.056)

- **PATRÓN** `ibs_20min` > `0.9467` → IC=+0.247 (n=988)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9467 (IC base=+0.056)

- **PATRÓN** `dist_vwap_pct` > `1.2866` → IC=+0.290 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2866 (IC base=+0.056)

- **PATRÓN** `volumen_regimen` > `1.172` → IC=+0.203 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.172 (IC base=+0.056)

- **PATRÓN** `volumen_pendiente_norm` < `0.1146` → IC=+0.175 (n=1335)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` < 0.1146 (IC base=+0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.2483` → IC=+0.207 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2483 (IC base=+0.056)

- **PATRÓN** `volumen_spike_ratio` < `1.4778` → IC=+0.204 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4778 (IC base=+0.056)

- **PATRÓN** `volumen_spike_ratio` > `2.8232` → IC=+0.174 (n=458)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.8232 (IC base=+0.056)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.277 (n=822)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.056)

- **PATRÓN** `ibs_20min` < `0.0952` → IC=+0.186 (n=1237)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.0952 (IC base=+0.039)

- **PATRÓN** `dist_vwap_pct` > `0.7309` → IC=+0.217 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7309 (IC base=+0.039)

- **PATRÓN** `dist_vwap_pct` < `0.1496` → IC=+0.205 (n=730)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1496 (IC base=+0.039)

- **PATRÓN** `volumen_regimen` > `1.2349` → IC=+0.232 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2349 (IC base=+0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.2539` → IC=+0.361 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2539 (IC base=+0.039)

- **PATRÓN** `volumen_spike_ratio` > `2.9118` → IC=+0.290 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9118 (IC base=+0.039)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.264 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 59.0 (IC base=+0.039)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2636` → IC=-0.157 (n=196)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2636
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=398)

- **FILTRO** `sigma_ewma_delta_pct` > `2.105` → IC=-0.169 (n=243)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.105
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=550)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.222` → IC=+0.167 (n=112)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 5.222 (IC base=-0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2093` → IC=+0.382 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2093 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` > `2.317` → IC=+0.237 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.317 (IC base=-0.003)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.460 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=-0.003)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` > `0.8848` → IC=-0.145 (n=280)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8848
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=841)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `drift_60min` |x|≤ `0.0718` → IC=+0.215 (n=156)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0718 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.196 (n=159)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 18.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.255 (n=161)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.297 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.027` → IC=+0.298 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.027 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` < `0.1441` → IC=+0.199 (n=363)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` < 0.1441 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.4152` → IC=+0.196 (n=54)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.4152 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` < `1.9774` → IC=+0.209 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9774 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `3.453` → IC=+0.184 (n=175)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 3.453 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.218 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `1944.22` → IC=+0.215 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1944.22 (IC base=+0.190)

- **PATRÓN** `sigma_h` < `0.0082` → IC=+0.356 (n=227)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0082 (IC base=+0.341)

- **PATRÓN** `drift_60min` |x|≤ `0.2366` → IC=+0.356 (n=172)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2366 (IC base=+0.341)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.386 (n=174)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.341)

- **PATRÓN** `ibs_20min` < `0.3443` → IC=+0.358 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3443 (IC base=+0.341)

- **PATRÓN** `ibs_20min` > `0.1389` → IC=+0.339 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1389 (IC base=+0.341)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.313` → IC=+0.349 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.313 (IC base=+0.341)

- **PATRÓN** `volumen_pendiente_norm` > `0.3643` → IC=+0.426 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3643 (IC base=+0.341)

- **PATRÓN** `volumen_spike_ratio` < `3.3265` → IC=+0.338 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.3265 (IC base=+0.341)

- **PATRÓN** `volumen_spike_ratio` > `1.9885` → IC=+0.340 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9885 (IC base=+0.341)

- **PATRÓN** `libro_liquidez` > `1881.2284` → IC=+0.375 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1881.2284 (IC base=+0.341)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.324 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.341)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.160 (n=157)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=324)

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
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=926)

- **PATRÓN** `dist_vwap_pct` > `0.7343` → IC=+0.233 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7343 (IC base=-0.073)

- **PATRÓN** `volumen_spike_ratio` < `1.4` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4 (IC base=-0.073)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7429` → IC=-0.126 (n=442)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7429
  - _Potencial_: sin este filtro IC_bueno=+0.222 (n=228)

- **FILTRO** `ibs_20min` > `0.75` → IC=-0.193 (n=223)

  - _Acción_: SKIP cuando `ibs_20min` > 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=683)

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

- **PATRÓN** `ibs_20min` > `0.8542` → IC=+0.271 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8542 (IC base=-0.007)

- **PATRÓN** `dist_vwap_pct` > `0.3412` → IC=+0.273 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3412 (IC base=-0.007)

- **PATRÓN** `volumen_regimen` < `0.8566` → IC=+0.192 (n=128)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.8566 (IC base=-0.007)

- **PATRÓN** `volumen_regimen` > `1.1463` → IC=+0.242 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1463 (IC base=-0.007)

- **PATRÓN** `volumen_pendiente_norm` < `0.0905` → IC=+0.174 (n=173)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` < 0.0905 (IC base=-0.007)

- **PATRÓN** `volumen_pendiente_norm` > `0.231` → IC=+0.275 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.231 (IC base=-0.007)

- **PATRÓN** `volumen_spike_ratio` < `1.4599` → IC=+0.210 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4599 (IC base=-0.007)

- **PATRÓN** `volumen_spike_ratio` > `2.0468` → IC=+0.179 (n=82)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 2.0468 (IC base=-0.007)

- **PATRÓN** `ballena_activa_n` < `62.0` → IC=+0.238 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 62.0 (IC base=-0.007)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0248` → IC=+0.330 (n=192)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0248 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.238 (n=223)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.230 (n=213)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `0.8983` → IC=+0.300 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8983 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` > `1.4017` → IC=+0.344 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.4017 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.172` → IC=+0.277 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.172 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` > `1.0202` → IC=+0.265 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0202 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` < `0.0802` → IC=+0.228 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0802 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.2775` → IC=+0.276 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2775 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` < `1.4115` → IC=+0.266 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4115 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.236 (n=607)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `2451.9374` → IC=+0.230 (n=576)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2451.9374 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.280 (n=198)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.269)

- **PATRÓN** `drift_60min` |x|≤ `0.4831` → IC=+0.273 (n=521)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4831 (IC base=+0.269)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.278 (n=556)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.269)

- **PATRÓN** `ibs_20min` < `0.12` → IC=+0.349 (n=395)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.12 (IC base=+0.269)

- **PATRÓN** `dist_vwap_pct` < `0.9161` → IC=+0.275 (n=668)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9161 (IC base=+0.269)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.826` → IC=+0.315 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.826 (IC base=+0.269)

- **PATRÓN** `volumen_regimen` > `1.2589` → IC=+0.305 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2589 (IC base=+0.269)

- **PATRÓN** `volumen_pendiente_norm` > `0.2896` → IC=+0.377 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2896 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` > `2.1674` → IC=+0.296 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1674 (IC base=+0.269)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.198 (n=859)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0101 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.3373` → IC=+0.158 (n=2264)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.3373 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.179 (n=960)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.157)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.159 (n=943)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 6.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.282 (n=1263)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` > `0.817` → IC=+0.252 (n=611)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.817 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.352` → IC=+0.242 (n=1070)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.352 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` > `0.6876` → IC=+0.175 (n=1594)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 0.6876 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` > `0.2372` → IC=+0.188 (n=482)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2372 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `2.2771` → IC=+0.155 (n=2043)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.2771 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` > `1.8474` → IC=+0.151 (n=1548)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.8474 (IC base=+0.157)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.166 (n=2083)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.157)

- **PATRÓN** `libro_liquidez` > `3197.0046` → IC=+0.182 (n=1167)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 3197.0046 (IC base=+0.157)

- **PATRÓN** `ballena_activa_n` < `117.0` → IC=+0.180 (n=1306)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 117.0 (IC base=+0.157)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.194 (n=2009)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0076 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.4145` → IC=+0.194 (n=2282)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.4145 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=871)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.41` → IC=+0.236 (n=2282)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.41 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` < `0.2145` → IC=+0.176 (n=1837)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.2145 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.887` → IC=+0.215 (n=437)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.887 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `1.1686` → IC=+0.163 (n=1827)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.1686 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` > `0.853` → IC=+0.172 (n=1218)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 0.853 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2903` → IC=+0.253 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2903 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` < `1.5756` → IC=+0.171 (n=736)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.5756 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.6551` → IC=+0.208 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6551 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `130.0` → IC=+0.187 (n=1092)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 130.0 (IC base=+0.182)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.201 (n=192)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.269` → IC=+0.152 (n=421)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.269 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.208 (n=152)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.298 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.076` → IC=+0.332 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.076 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.2061` → IC=+0.190 (n=69)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2061 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `1.4355` → IC=+0.130 (n=341)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.4355 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.154 (n=189)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.03 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.258 (n=184)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.257)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.269 (n=210)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.257)

- **PATRÓN** `drift_60min` |x|≤ `0.2479` → IC=+0.306 (n=184)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2479 (IC base=+0.257)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.278 (n=192)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.257)

- **PATRÓN** `ibs_20min` < `0.3402` → IC=+0.296 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3402 (IC base=+0.257)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.358` → IC=+0.281 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.358 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` < `1.8801` → IC=+0.288 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8801 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` > `2.8103` → IC=+0.284 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8103 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.333 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `1965.0404` → IC=+0.347 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1965.0404 (IC base=+0.257)

- **PATRÓN** `ballena_activa_n` < `80.0` → IC=+0.257 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 80.0 (IC base=+0.257)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.214 (n=124)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.175)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.196 (n=123)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0072 (IC base=+0.175)

- **PATRÓN** `drift_60min` |x|≤ `0.3392` → IC=+0.177 (n=323)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.3392 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.201 (n=373)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.175)

- **PATRÓN** `ibs_20min` > `0.9998` → IC=+0.274 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9998 (IC base=+0.175)

- **PATRÓN** `dist_vwap_pct` > `0.211` → IC=+0.233 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.211 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.48` → IC=+0.230 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.48 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.439` → IC=+0.178 (n=340)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` < 7.439 (IC base=+0.175)

- **PATRÓN** `volumen_regimen` < `1.2894` → IC=+0.180 (n=367)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 1.2894 (IC base=+0.175)

- **PATRÓN** `volumen_regimen` > `1.0855` → IC=+0.196 (n=166)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` > 1.0855 (IC base=+0.175)

- **PATRÓN** `volumen_pendiente_norm` > `0.1548` → IC=+0.238 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1548 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` < `1.3602` → IC=+0.230 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3602 (IC base=+0.175)

- **PATRÓN** `libro_liquidez` > `12288.7036` → IC=+0.191 (n=244)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 12288.7036 (IC base=+0.175)

- **PATRÓN** `sigma_h` < `0.0023` → IC=+0.203 (n=153)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0023 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.2236` → IC=+0.174 (n=403)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2236 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.167 (n=421)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 7.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.4241` → IC=+0.187 (n=458)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.4241 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` < `0.1525` → IC=+0.170 (n=446)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.1525 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.439` → IC=+0.226 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.439 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `0.6399` → IC=+0.223 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6399 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.0945` → IC=+0.206 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0945 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `2.5404` → IC=+0.156 (n=350)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.5404 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.4105` → IC=+0.139 (n=350)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.4105 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `14471.6447` → IC=+0.152 (n=153)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 14471.6447 (IC base=+0.144)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `drift_60min` |x|≤ `0.1483` → IC=+0.173 (n=246)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.1483 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.192 (n=128)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 17.0 (IC base=+0.159)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.227 (n=141)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.904` → IC=+0.296 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.904 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` < `0.2295` → IC=+0.153 (n=306)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.2295 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` < `1.978` → IC=+0.210 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.978 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` > `3.6311` → IC=+0.148 (n=140)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 3.6311 (IC base=+0.159)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.186 (n=320)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.04 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `1955.5029` → IC=+0.188 (n=123)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 1955.5029 (IC base=+0.159)

- **PATRÓN** `sigma_h` < `0.0098` → IC=+0.287 (n=247)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0098 (IC base=+0.273)

- **PATRÓN** `drift_60min` |x|≤ `0.2102` → IC=+0.326 (n=165)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2102 (IC base=+0.273)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.305 (n=167)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.273)

- **PATRÓN** `ibs_20min` < `0.3077` → IC=+0.324 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3077 (IC base=+0.273)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.917` → IC=+0.329 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.917 (IC base=+0.273)

- **PATRÓN** `volumen_pendiente_norm` > `0.363` → IC=+0.433 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.363 (IC base=+0.273)

- **PATRÓN** `volumen_spike_ratio` > `1.9918` → IC=+0.271 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9918 (IC base=+0.273)

- **PATRÓN** `ballena_activa_n` < `62.0` → IC=+0.238 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 62.0 (IC base=+0.273)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0093` → IC=+0.210 (n=370)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0093 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.0949` → IC=+0.214 (n=124)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0949 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.188 (n=383)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 6.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` > `0.4362` → IC=+0.228 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4362 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.9808` → IC=+0.232 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9808 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.328` → IC=+0.306 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.328 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` > `1.2318` → IC=+0.220 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2318 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.1005` → IC=+0.222 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1005 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` < `1.4299` → IC=+0.180 (n=120)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.4299 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `2.4571` → IC=+0.227 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4571 (IC base=+0.172)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.174 (n=422)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `8687.9043` → IC=+0.202 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8687.9043 (IC base=+0.172)

- **PATRÓN** `ballena_activa_n` < `149.0` → IC=+0.160 (n=204)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 149.0 (IC base=+0.172)

- **PATRÓN** `sigma_h` < `0.0025` → IC=+0.250 (n=146)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0025 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.3806` → IC=+0.161 (n=438)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.3806 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.173 (n=224)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 14.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.151 (n=164)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 5.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` < `0.3411` → IC=+0.211 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3411 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` < `0.1505` → IC=+0.160 (n=445)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.1505 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.272` → IC=+0.198 (n=137)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 10.272 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `1.1582` → IC=+0.157 (n=438)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.1582 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` > `0.6135` → IC=+0.159 (n=438)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6135 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.1001` → IC=+0.177 (n=131)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1001 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `1.9018` → IC=+0.177 (n=221)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.9018 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `10187.0803` → IC=+0.155 (n=146)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 10187.0803 (IC base=+0.143)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.208 (n=231)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.147 (n=468)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 8.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.8519` → IC=+0.233 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8519 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.8776` → IC=+0.270 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8776 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.203` → IC=+0.293 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.203 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.6201` → IC=+0.140 (n=509)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 0.6201 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` < `0.1617` → IC=+0.135 (n=499)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` < 0.1617 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.4397` → IC=+0.127 (n=159)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.4397 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `1.552` → IC=+0.133 (n=426)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.552 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `3227.897` → IC=+0.233 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3227.897 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.181 (n=139)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0049 (IC base=+0.125)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.195 (n=139)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0101 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=149)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` < `0.4` → IC=+0.231 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `0.68` → IC=+0.147 (n=100)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.68 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` < `0.22` → IC=+0.139 (n=383)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.22 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.753` → IC=+0.206 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.753 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` > `0.8432` → IC=+0.160 (n=277)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.8432 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2176` → IC=+0.195 (n=57)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2176 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `2.2636` → IC=+0.211 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2636 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2080.7013` → IC=+0.177 (n=277)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 2080.7013 (IC base=+0.125)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0236` → IC=+0.202 (n=246)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0236 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.1645` → IC=+0.192 (n=238)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1645 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.204 (n=194)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.169)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.178 (n=262)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 8.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `0.907` → IC=+0.269 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.907 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `1.6195` → IC=+0.262 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.6195 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.097` → IC=+0.246 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.097 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` > `0.6079` → IC=+0.181 (n=541)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 0.6079 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.2353` → IC=+0.242 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2353 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `2.1454` → IC=+0.185 (n=443)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 2.1454 (IC base=+0.169)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.174 (n=565)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `2451.004` → IC=+0.170 (n=541)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2451.004 (IC base=+0.169)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.270 (n=228)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0063 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.6622` → IC=+0.232 (n=517)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6622 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=251)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.253 (n=245)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` < `0.381` → IC=+0.257 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.381 (IC base=+0.219)

- **PATRÓN** `dist_vwap_pct` < `0.2448` → IC=+0.232 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2448 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.175` → IC=+0.285 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.175 (IC base=+0.219)

- **PATRÓN** `volumen_regimen` > `0.6252` → IC=+0.238 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6252 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.28` → IC=+0.346 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.28 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` > `2.7294` → IC=+0.273 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7294 (IC base=+0.219)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.007` → IC=+0.124 (n=208)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` > 0.007 (IC base=+0.095)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.188 (n=235)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 16.0 (IC base=+0.095)

- **PATRÓN** `ibs_20min` > `0.6267` → IC=+0.168 (n=410)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.6267 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` > `0.7947` → IC=+0.283 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7947 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.14` → IC=+0.192 (n=128)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 8.14 (IC base=+0.095)

- **PATRÓN** `volumen_pendiente_norm` > `0.1727` → IC=+0.175 (n=121)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1727 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `2844.2987` → IC=+0.133 (n=306)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2844.2987 (IC base=+0.095)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.174 (n=142)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0037 (IC base=+0.070)

- **PATRÓN** `drift_60min` |x|≤ `0.1224` → IC=+0.124 (n=187)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.62€ cuando `drift_60min` |x|≤ 0.1224 (IC base=+0.070)

- **PATRÓN** `ibs_20min` < `0.2975` → IC=+0.153 (n=283)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.2975 (IC base=+0.070)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.835` → IC=+0.177 (n=97)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 7.835 (IC base=+0.070)

- **PATRÓN** `volumen_spike_ratio` < `1.852` → IC=+0.125 (n=246)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 1.852 (IC base=+0.070)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.200 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.122 (n=88)

- **FILTRO** `ibs_20min` < `0.5377` → IC=-0.177 (n=29)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5377
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=87)

- **FILTRO** `libro_liquidez` < `8276.6888` → IC=-0.175 (n=38)

  - _Acción_: SKIP cuando `libro_liquidez` < 8276.6888
  - _Potencial_: sin este filtro IC_bueno=+0.150 (n=78)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.122 (n=88)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 9.0 (IC base=+0.042)

- **PATRÓN** `ibs_20min` > `0.9398` → IC=+0.238 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9398 (IC base=+0.042)

- **PATRÓN** `dist_vwap_pct` > `0.7947` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7947 (IC base=+0.042)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.167` → IC=+0.143 (n=40)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 4.167 (IC base=+0.042)

- **PATRÓN** `libro_liquidez` > `12103.1125` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 12103.1125 (IC base=+0.042)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.216 (n=72)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.138)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.184 (n=74)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0052 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.3581` → IC=+0.173 (n=163)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.3581 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.190 (n=56)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 4.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.494` → IC=+0.190 (n=143)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.494 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.1811` → IC=+0.169 (n=143)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.1811 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.164` → IC=+0.255 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.164 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.1856` → IC=+0.161 (n=163)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.1856 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.1595` → IC=+0.322 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1595 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.7062` → IC=+0.183 (n=102)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.7062 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.4203` → IC=+0.158 (n=153)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.4203 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `153.0` → IC=+0.167 (n=58)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 153.0 (IC base=+0.138)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.286 (n=82)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.286)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.312 (n=62)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `0.2318` → IC=+0.285 (n=63)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2318 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.308 (n=97)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.286)

- **PATRÓN** `ibs_20min` > `0.6752` → IC=+0.302 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6752 (IC base=+0.286)

- **PATRÓN** `dist_vwap_pct` > `0.1466` → IC=+0.337 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1466 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.561` → IC=+0.385 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.561 (IC base=+0.286)

- **PATRÓN** `volumen_regimen` < `0.701` → IC=+0.384 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.701 (IC base=+0.286)

- **PATRÓN** `volumen_pendiente_norm` > `0.1824` → IC=+0.392 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1824 (IC base=+0.286)

- **PATRÓN** `volumen_spike_ratio` < `2.2928` → IC=+0.300 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2928 (IC base=+0.286)

- **PATRÓN** `volumen_spike_ratio` > `1.5284` → IC=+0.305 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5284 (IC base=+0.286)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.352 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.037)

- **PATRÓN** `drift_60min` |x|≤ `0.2474` → IC=+0.125 (n=62)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.62€ cuando `drift_60min` |x|≤ 0.2474 (IC base=+0.037)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.160 (n=48)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 11.0 (IC base=+0.037)

- **PATRÓN** `ibs_20min` < `0.6219` → IC=+0.125 (n=70)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` < 0.6219 (IC base=+0.037)

- **PATRÓN** `volumen_regimen` < `0.6982` → IC=+0.197 (n=31)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.6982 (IC base=+0.037)

- **PATRÓN** `libro_liquidez` > `9264.2772` → IC=+0.269 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9264.2772 (IC base=+0.037)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` < `0.619` → IC=-0.157 (n=65)

  - _Acción_: SKIP cuando `ibs_20min` < 0.619
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=134)

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
- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.196 (n=1361)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0081 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.174 (n=1009)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 18.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.9402` → IC=+0.290 (n=1358)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9402 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `1.1041` → IC=+0.237 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1041 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.512` → IC=+0.227 (n=1754)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.512 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.628` → IC=+0.149 (n=707)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.628 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` > `1.0767` → IC=+0.154 (n=961)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 1.0767 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.165` → IC=+0.181 (n=767)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.165 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.3039` → IC=+0.150 (n=2355)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.3039 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.8603` → IC=+0.159 (n=1784)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.8603 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=2426)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `2502.8212` → IC=+0.175 (n=1996)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2502.8212 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.197 (n=1084)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 71.0 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.220 (n=1795)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.4737` → IC=+0.202 (n=2689)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4737 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.197 (n=1014)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 17.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.207 (n=958)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` < `0.562` → IC=+0.245 (n=2690)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.562 (IC base=+0.190)

- **PATRÓN** `dist_vwap_pct` < `0.727` → IC=+0.181 (n=2144)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.727 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.366` → IC=+0.207 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.366 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.638` → IC=+0.192 (n=2520)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 2.638 (IC base=+0.190)

- **PATRÓN** `volumen_regimen` < `0.6224` → IC=+0.184 (n=668)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6224 (IC base=+0.190)

- **PATRÓN** `volumen_regimen` > `1.1974` → IC=+0.180 (n=667)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 1.1974 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.2827` → IC=+0.263 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2827 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `2.2942` → IC=+0.207 (n=903)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2942 (IC base=+0.190)

- **PATRÓN** `ballena_activa_n` < `178.0` → IC=+0.167 (n=1566)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 178.0 (IC base=+0.190)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` > `0.007` → IC=+0.206 (n=219)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.147 (n=239)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 15.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.174 (n=176)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 6.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.306 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.308` → IC=+0.301 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.308 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.2139` → IC=+0.218 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2139 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `1.9109` → IC=+0.144 (n=268)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.9109 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.194 (n=282)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.04 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.305 (n=203)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.269)

- **PATRÓN** `drift_60min` |x|≤ `0.1044` → IC=+0.324 (n=134)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1044 (IC base=+0.269)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.273 (n=271)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.269)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.283 (n=270)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.269)

- **PATRÓN** `ibs_20min` < `0.5758` → IC=+0.314 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5758 (IC base=+0.269)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.085` → IC=+0.292 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.085 (IC base=+0.269)

- **PATRÓN** `volumen_pendiente_norm` < `0.0877` → IC=+0.261 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0877 (IC base=+0.269)

- **PATRÓN** `volumen_pendiente_norm` > `0.2907` → IC=+0.300 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2907 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` > `2.7082` → IC=+0.329 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7082 (IC base=+0.269)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.308 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.269)

- **PATRÓN** `libro_liquidez` > `1978.9302` → IC=+0.316 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1978.9302 (IC base=+0.269)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.254 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 71.0 (IC base=+0.269)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.169 (n=161)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0028 (IC base=+0.152)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.179 (n=160)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0071 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.178 (n=436)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 8.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` > `0.3232` → IC=+0.207 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3232 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.2561` → IC=+0.231 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2561 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.582` → IC=+0.190 (n=127)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 9.582 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `1.2653` → IC=+0.160 (n=480)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2653 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` > `1.0886` → IC=+0.173 (n=218)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 1.0886 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.2044` → IC=+0.213 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2044 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `2.4168` → IC=+0.186 (n=431)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 2.4168 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `1.3655` → IC=+0.179 (n=431)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 1.3655 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `11985.6464` → IC=+0.174 (n=320)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 11985.6464 (IC base=+0.152)

- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.190 (n=153)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0022 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.1721` → IC=+0.194 (n=299)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.1721 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.168 (n=419)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 7.0 (IC base=+0.164)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.177 (n=463)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 18.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` < `0.3843` → IC=+0.211 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3843 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` < `0.1415` → IC=+0.180 (n=382)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.1415 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.638` → IC=+0.214 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.638 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` < `0.6257` → IC=+0.242 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6257 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.1489` → IC=+0.276 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1489 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` < `2.4777` → IC=+0.190 (n=350)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 2.4777 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` > `1.5054` → IC=+0.182 (n=313)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.5054 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.164 (n=576)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `12242.4641` → IC=+0.172 (n=202)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 12242.4641 (IC base=+0.164)

- **PATRÓN** `ballena_activa_n` < `308.0` → IC=+0.186 (n=84)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 308.0 (IC base=+0.164)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `hora_utc` < `8.0` → IC=+0.240 (n=179)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` > `0.7044` → IC=+0.263 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7044 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.096` → IC=+0.344 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.096 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` < `0.2246` → IC=+0.186 (n=326)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` < 0.2246 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` < `1.9774` → IC=+0.192 (n=141)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.9774 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `3.6431` → IC=+0.176 (n=146)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 3.6431 (IC base=+0.182)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.206 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.182)

- **PATRÓN** `libro_liquidez` > `1910.8884` → IC=+0.207 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1910.8884 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.226 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 59.0 (IC base=+0.182)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.324 (n=129)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.249)

- **PATRÓN** `drift_60min` |x|≤ `0.1262` → IC=+0.254 (n=169)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1262 (IC base=+0.249)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.258 (n=266)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.249)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.287 (n=148)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.249)

- **PATRÓN** `ibs_20min` < `0.5682` → IC=+0.314 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5682 (IC base=+0.249)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.025` → IC=+0.284 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.025 (IC base=+0.249)

- **PATRÓN** `volumen_pendiente_norm` > `0.3507` → IC=+0.300 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3507 (IC base=+0.249)

- **PATRÓN** `volumen_spike_ratio` < `1.7663` → IC=+0.256 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7663 (IC base=+0.249)

- **PATRÓN** `volumen_spike_ratio` > `2.4041` → IC=+0.212 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4041 (IC base=+0.249)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.276 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.249)

- **PATRÓN** `ballena_activa_n` < `65.0` → IC=+0.198 (n=180)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 65.0 (IC base=+0.249)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0089` → IC=+0.156 (n=483)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0089 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.162 (n=445)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 8.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.3436` → IC=+0.193 (n=483)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.3436 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.8501` → IC=+0.217 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8501 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.485` → IC=+0.194 (n=230)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 4.485 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.6195` → IC=+0.175 (n=161)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.6195 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `1.1962` → IC=+0.163 (n=161)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 1.1962 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.2675` → IC=+0.266 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2675 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `2.4121` → IC=+0.235 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4121 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `5139.067` → IC=+0.219 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5139.067 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `165.0` → IC=+0.182 (n=237)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 165.0 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.178 (n=349)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0076 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.5036` → IC=+0.167 (n=397)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.5036 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.186 (n=278)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 11.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.0849` → IC=+0.251 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0849 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.1655` → IC=+0.162 (n=196)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.1655 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.3924` → IC=+0.156 (n=385)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.3924 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.454` → IC=+0.221 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.454 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `0.5857` → IC=+0.159 (n=133)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.5857 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` > `1.1365` → IC=+0.187 (n=132)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 1.1365 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.2334` → IC=+0.333 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2334 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `1.8125` → IC=+0.175 (n=226)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.8125 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `2.4643` → IC=+0.196 (n=113)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.4643 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `9462.6339` → IC=+0.214 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9462.6339 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `138.0` → IC=+0.225 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 138.0 (IC base=+0.153)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.157 (n=243)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0111 (IC base=+0.098)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.125 (n=478)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 8.0 (IC base=+0.098)

- **PATRÓN** `ibs_20min` > `0.9048` → IC=+0.304 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9048 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `0.866` → IC=+0.225 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.866 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.395` → IC=+0.222 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.395 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `2951.497` → IC=+0.289 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2951.497 (IC base=+0.098)

- **PATRÓN** `ballena_activa_n` < `66.0` → IC=+0.168 (n=308)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 66.0 (IC base=+0.098)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.179 (n=213)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.006 (IC base=+0.112)

- **PATRÓN** `drift_60min` |x|≤ `0.5446` → IC=+0.126 (n=484)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.63€ cuando `drift_60min` |x|≤ 0.5446 (IC base=+0.112)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.164 (n=230)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.112)

- **PATRÓN** `ibs_20min` < `0.5909` → IC=+0.198 (n=484)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.5909 (IC base=+0.112)

- **PATRÓN** `dist_vwap_pct` < `0.4736` → IC=+0.141 (n=432)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.4736 (IC base=+0.112)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.042` → IC=+0.132 (n=474)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 3.042 (IC base=+0.112)

- **PATRÓN** `volumen_regimen` < `0.7038` → IC=+0.146 (n=213)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.7038 (IC base=+0.112)

- **PATRÓN** `volumen_pendiente_norm` > `0.072` → IC=+0.159 (n=136)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.072 (IC base=+0.112)

- **PATRÓN** `volumen_spike_ratio` < `2.0886` → IC=+0.138 (n=296)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 2.0886 (IC base=+0.112)

- **PATRÓN** `volumen_spike_ratio` > `1.443` → IC=+0.133 (n=336)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.443 (IC base=+0.112)

- **PATRÓN** `libro_liquidez` > `2610.631` → IC=+0.156 (n=219)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2610.631 (IC base=+0.112)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0227` → IC=+0.216 (n=283)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0227 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.186 (n=631)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` > `0.963` → IC=+0.296 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.963 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` > `1.0241` → IC=+0.286 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0241 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.983` → IC=+0.266 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.983 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` < `0.6079` → IC=+0.187 (n=209)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.6079 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` > `1.0297` → IC=+0.209 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0297 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.1708` → IC=+0.245 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1708 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `1.8188` → IC=+0.186 (n=383)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.8188 (IC base=+0.177)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.188 (n=648)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.01 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `2452.9003` → IC=+0.179 (n=624)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 2452.9003 (IC base=+0.177)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.223 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.177)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.303 (n=227)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.4796` → IC=+0.227 (n=596)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4796 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.220 (n=633)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.213)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.214 (n=721)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` < `0.4912` → IC=+0.275 (n=677)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4912 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` < `1.2446` → IC=+0.222 (n=785)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 1.2446 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.508` → IC=+0.289 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.508 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` > `1.2332` → IC=+0.246 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2332 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.2776` → IC=+0.315 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2776 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `2.5663` → IC=+0.235 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5663 (IC base=+0.213)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.178 (n=392)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 37.0 (IC base=+0.213)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.147 (n=1050)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.137 (n=544)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0106 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.173 (n=224)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 18.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `0.9311` → IC=+0.178 (n=206)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.9311 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.496` → IC=+0.125 (n=563)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` < 3.496 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` > `1.0516` → IC=+0.136 (n=218)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 1.0516 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.2809` → IC=+0.204 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2809 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.4115` → IC=+0.134 (n=203)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.4115 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` > `2.2014` → IC=+0.132 (n=275)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.2014 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `5095.9603` → IC=+0.128 (n=412)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 5095.9603 (IC base=+0.119)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.189 (n=268)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0036 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.3642` → IC=+0.170 (n=703)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.3642 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.161 (n=314)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.194 (n=295)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 4.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` < `0.1903` → IC=+0.152 (n=352)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.1903 (IC base=+0.142)

- **PATRÓN** `ibs_20min` > `0.0855` → IC=+0.150 (n=799)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` > 0.0855 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `0.6358` → IC=+0.156 (n=193)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.6358 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` < `0.3912` → IC=+0.134 (n=761)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.3912 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.057` → IC=+0.142 (n=356)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 4.057 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.072` → IC=+0.150 (n=802)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 6.072 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `1.2036` → IC=+0.154 (n=776)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.2036 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` < `0.0944` → IC=+0.146 (n=718)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` < 0.0944 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.0718` → IC=+0.155 (n=381)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.0718 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `2.4927` → IC=+0.160 (n=791)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.4927 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `1.4169` → IC=+0.149 (n=791)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.4169 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.147 (n=1050)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `10638.1798` → IC=+0.154 (n=533)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 10638.1798 (IC base=+0.142)

### GBM_LATE_5M#BTC#5min
- **FILTRO** `sigma_ewma_delta_pct` > `2.989` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.989
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=95)

- **FILTRO** `volumen_pendiente_norm` > `0.1007` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1007
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=97)

- **FILTRO** `libro_liquidez` < `12272.8392` → IC=-0.200 (n=28)

  - _Acción_: SKIP cuando `libro_liquidez` < 12272.8392
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=87)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.130 (n=79)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 14.0 (IC base=+0.056)

- **PATRÓN** `volumen_regimen` > `0.915` → IC=+0.214 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.915 (IC base=+0.056)

- **PATRÓN** `libro_liquidez` > `12272.8392` → IC=+0.140 (n=87)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 12272.8392 (IC base=+0.056)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.168 (n=447)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0065 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.3655` → IC=+0.157 (n=447)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.3655 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.187 (n=177)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.192 (n=167)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 5.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` < `0.18` → IC=+0.163 (n=197)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.18 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.3894` → IC=+0.143 (n=298)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.3894 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.6099` → IC=+0.175 (n=78)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.6099 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.34` → IC=+0.156 (n=452)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 6.34 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `1.1847` → IC=+0.155 (n=447)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.1847 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` > `0.6241` → IC=+0.141 (n=447)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.6241 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.0724` → IC=+0.184 (n=207)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.0724 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `2.5395` → IC=+0.153 (n=445)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.5395 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `1.7842` → IC=+0.144 (n=296)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.7842 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `11911.1172` → IC=+0.146 (n=399)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 11911.1172 (IC base=+0.141)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.212 (n=57)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0091 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.262 (n=61)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` < `0.4706` → IC=+0.210 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4706 (IC base=+0.152)

- **PATRÓN** `ibs_20min` > `0.9583` → IC=+0.371 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9583 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.371` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.371 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.061` → IC=+0.151 (n=81)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 4.061 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.1831` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1831 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `3.2525` → IC=+0.167 (n=85)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 3.2525 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `1.5216` → IC=+0.163 (n=84)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.5216 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `1720.343` → IC=+0.178 (n=85)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 1720.343 (IC base=+0.152)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.179 (n=247)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0094 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.4407` → IC=+0.162 (n=217)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.4407 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `19.0` → IC=+0.203 (n=89)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 19.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.143 (n=110)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 5.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` > `0.803` → IC=+0.193 (n=112)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.803 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `0.9785` → IC=+0.210 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9785 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` < `0.4059` → IC=+0.150 (n=215)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.4059 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.126` → IC=+0.175 (n=38)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 11.126 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.985` → IC=+0.143 (n=211)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 2.985 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `0.6442` → IC=+0.182 (n=83)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6442 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` > `0.8929` → IC=+0.151 (n=164)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.8929 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.1741` → IC=+0.162 (n=75)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.1741 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `1.412` → IC=+0.207 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.412 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `1.8053` → IC=+0.148 (n=160)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.8053 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `8959.8986` → IC=+0.171 (n=220)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 8959.8986 (IC base=+0.142)

- **PATRÓN** `sigma_h` < `0.0088` → IC=+0.153 (n=226)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0088 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.5088` → IC=+0.180 (n=226)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.5088 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.145 (n=105)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 16.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.167 (n=154)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 10.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.612` → IC=+0.142 (n=199)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.612 (IC base=+0.137)

- **PATRÓN** `ibs_20min` > `0.0864` → IC=+0.175 (n=226)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.0864 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.198` → IC=+0.145 (n=91)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.198 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.3536` → IC=+0.146 (n=224)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.3536 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.157` → IC=+0.164 (n=114)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 3.157 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `0.6473` → IC=+0.244 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6473 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` < `0.1309` → IC=+0.160 (n=230)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` < 0.1309 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.1543` → IC=+0.190 (n=195)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 2.1543 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.4448` → IC=+0.161 (n=222)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.4448 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `10283.2146` → IC=+0.167 (n=76)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 10283.2146 (IC base=+0.137)

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

- **FILTRO** `volumen_regimen` > `0.903` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.903
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=19)

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

- **FILTRO** `ibs_20min` > `0.6429` → IC=-0.340 (n=48)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6429
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=50)

- **FILTRO** `ibs_20min` < `0.3707` → IC=-0.308 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3707
  - _Potencial_: sin este filtro IC_bueno=-0.289 (n=74)

- **FILTRO** `dist_vwap_pct` < `0.1009` → IC=-0.354 (n=53)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1009
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=45)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `ibs_20min` < `0.6047` → IC=-0.259 (n=27)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6047
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **FILTRO** `sigma_h` < `0.0019` → IC=-0.318 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0019
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=21)

- **FILTRO** `hora_utc` < `12.0` → IC=-0.318 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=21)

- **FILTRO** `ibs_20min` > `0.6267` → IC=-0.364 (n=20)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6267
  - _Potencial_: sin este filtro IC_bueno=-0.152 (n=21)

- **FILTRO** `dist_vwap_pct` < `0.0931` → IC=-0.362 (n=27)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0931
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=14)

- **FILTRO** `libro_liquidez` < `4361.6218` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `libro_liquidez` < 4361.6218
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=21)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.6354` → IC=-0.462 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6354
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **FILTRO** `ibs_20min` > `0.8144` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8144
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=17)

- **FILTRO** `dist_vwap_pct` < `0.2821` → IC=-0.286 (n=26)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.2821
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **FILTRO** `sigma_ewma_delta_pct` < `5.949` → IC=-0.318 (n=20)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 5.949
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=13)

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
  - _Potencial_: sin este filtro IC_bueno=+0.145 (n=139)

- **FILTRO** `dist_vwap_pct` > `0.5824` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.5824
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=138)

- **PATRÓN** `ibs_20min` > `0.5882` → IC=+0.145 (n=139)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.5882 (IC base=+0.045)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `sigma_h` < `0.0017` → IC=-0.206 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0017
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=45)

- **FILTRO** `ibs_20min` < `0.3927` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3927
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=41)

- **FILTRO** `volumen_regimen` < `0.6858` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.6858
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=45)

- **PATRÓN** `ibs_20min` > `0.7184` → IC=+0.188 (n=30)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.7184 (IC base=-0.065)

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
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.128 (n=119)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `2501.4019` → IC=+0.172 (n=114)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2501.4019 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.130 (n=44)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 18.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.140 (n=134)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 18.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.128 (n=49)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.495 (IC base=+0.125)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.124 (n=107)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.505 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2478.2261` → IC=+0.153 (n=125)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 2478.2261 (IC base=+0.125)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.128 (n=119)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `2501.4019` → IC=+0.172 (n=114)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2501.4019 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.130 (n=44)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 18.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.140 (n=134)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 18.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.128 (n=49)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.495 (IC base=+0.125)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.124 (n=107)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.505 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2478.2261` → IC=+0.153 (n=125)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 2478.2261 (IC base=+0.125)

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

### LIQUIDACIONES_15M#XRP#15min
- **FILTRO** `liq_n` < `7.0` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `liq_n` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=509)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=88)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9427` → IC=-0.311 (n=35)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9427
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=74)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.265 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.209 (n=77)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=88)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_usd_total` < `18442.74` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `liq_usd_total` < 18442.74
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=53)

- **FILTRO** `libro_liquidez` < `13988.6712` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 13988.6712
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

- **PATRÓN** `liq_n` > `11.0` → IC=+0.136 (n=20)

  - _Acción_: Kelly boost +0.68€ cuando `liq_n` > 11.0 (IC base=+0.025)

- **PATRÓN** `liq_usd_total` > `46708.62` → IC=+0.159 (n=39)

  - _Acción_: Kelly boost +0.79€ cuando `liq_usd_total` > 46708.62 (IC base=+0.025)

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
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=149)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.318 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **PATRÓN** `liq_n` > `2.0` → IC=+0.135 (n=94)

  - _Acción_: Kelly boost +0.68€ cuando `liq_n` > 2.0 (IC base=+0.081)

- **PATRÓN** `liq_usd_total` > `9741.83` → IC=+0.161 (n=57)

  - _Acción_: Kelly boost +0.81€ cuando `liq_usd_total` > 9741.83 (IC base=+0.081)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.144 (n=130)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 8.0 (IC base=+0.081)

### LIQUIDACIONES_5M#SOL#5min
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
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=95)

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
- **FILTRO** `ibs_20min` > `0.9474` → IC=-0.177 (n=94)

  - _Acción_: SKIP cuando `ibs_20min` > 0.9474
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=284)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=450)

### MOMENTUM_IBS_15M#SOL#15min
- **FILTRO** `drift_20min_pct` |x|> `0.178` → IC=-0.131 (n=101)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.178
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=199)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.46` → IC=-0.169 (n=868)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=2681)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.215 (n=838)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=2687)

- **FILTRO** `ibs_20min` > `0.2733` → IC=-0.178 (n=880)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2733
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=2645)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.232 (n=125)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=388)

- **FILTRO** `ibs_20min` < `0.7312` → IC=-0.169 (n=128)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7312
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=385)

- **FILTRO** `ibs_20min` > `0.1844` → IC=-0.121 (n=304)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1844
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=305)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.214 (n=145)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=440)

- **FILTRO** `ibs_20min` > `0.2175` → IC=-0.155 (n=146)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2175
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=439)

- **FILTRO** `ballena_activa_n` > `78.0` → IC=-0.169 (n=146)

  - _Acción_: SKIP cuando `ballena_activa_n` > 78.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=439)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.133 (n=115)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=425)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.179 (n=235)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=305)

- **FILTRO** `ibs_20min` < `0.7273` → IC=-0.186 (n=135)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7273
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=405)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.202 (n=199)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=392)

- **FILTRO** `ibs_20min` > `0.7475` → IC=-0.211 (n=147)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7475
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=444)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.128 (n=146)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=487)

- **FILTRO** `py_entrada` > `0.52` → IC=-0.182 (n=152)

  - _Acción_: SKIP cuando `py_entrada` > 0.52
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=469)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.169 (n=152)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=469)

### MOMENTUM_IBS_15M_BALLENA#SOL#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.235 (n=134)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=421)

- **FILTRO** `drift_20min_pct` |x|> `0.2852` → IC=-0.147 (n=188)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.2852
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=367)

- **FILTRO** `ibs_20min` > `0.2778` → IC=-0.176 (n=137)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2778
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=418)

- **FILTRO** `ballena_activa_n` > `3.0` → IC=-0.144 (n=248)

  - _Acción_: SKIP cuando `ballena_activa_n` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=307)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.205 (n=144)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=452)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=581)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.237 (n=188)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=376)

- **FILTRO** `ibs_20min` > `0.2857` → IC=-0.236 (n=138)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=426)

### MOMENTUM_IBS_15M_FADE
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
- **FILTRO** `hora_utc` < `7.0` → IC=-0.139 (n=2131)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=6707)

- **FILTRO** `py_entrada` < `0.36` → IC=-0.284 (n=2134)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=6704)

- **FILTRO** `ibs_7min` < `0.7333` → IC=-0.232 (n=2203)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7333
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=6635)

- **FILTRO** `ballena_activa_n` > `19.0` → IC=-0.174 (n=2999)

  - _Acción_: SKIP cuando `ballena_activa_n` > 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=5839)

- **FILTRO** `py_entrada` > `0.69` → IC=-0.231 (n=2482)

  - _Acción_: SKIP cuando `py_entrada` > 0.69
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=8235)

- **FILTRO** `ibs_7min` > `0.7245` → IC=-0.174 (n=2679)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7245
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=8038)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.318 (n=289)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=903)

- **FILTRO** `ibs_7min` < `0.9787` → IC=-0.201 (n=785)

  - _Acción_: SKIP cuando `ibs_7min` < 0.9787
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=407)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.253 (n=294)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=898)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.231 (n=437)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=1409)

- **FILTRO** `drift_7min_pct` |x|> `0.1355` → IC=-0.152 (n=627)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1355
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=1219)

- **FILTRO** `ibs_7min` > `0.3` → IC=-0.174 (n=627)

  - _Acción_: SKIP cuando `ibs_7min` > 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=1219)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.37` → IC=-0.256 (n=404)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=1316)

- **FILTRO** `ibs_7min` < `0.797` → IC=-0.180 (n=429)

  - _Acción_: SKIP cuando `ibs_7min` < 0.797
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=1291)

- **FILTRO** `ballena_activa_n` > `158.0` → IC=-0.191 (n=428)

  - _Acción_: SKIP cuando `ballena_activa_n` > 158.0
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=1292)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.227 (n=408)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=1317)

- **FILTRO** `ballena_activa_n` > `94.0` → IC=-0.160 (n=584)

  - _Acción_: SKIP cuando `ballena_activa_n` > 94.0
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=1141)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.201 (n=296)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=977)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.316 (n=405)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=868)

- **FILTRO** `ibs_7min` < `0.2143` → IC=-0.284 (n=318)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2143
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=955)

- **FILTRO** `ballena_activa_n` > `16.0` → IC=-0.282 (n=306)

  - _Acción_: SKIP cuando `ballena_activa_n` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=967)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.260 (n=406)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=1466)

- **FILTRO** `ibs_7min` > `0.8214` → IC=-0.195 (n=467)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8214
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=1405)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.156 (n=321)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=1164)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.214 (n=711)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=774)

- **FILTRO** `ibs_7min` < `0.7565` → IC=-0.186 (n=371)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7565
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=1114)

- **FILTRO** `ballena_activa_n` > `42.0` → IC=-0.204 (n=370)

  - _Acción_: SKIP cuando `ballena_activa_n` > 42.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=1115)

- **FILTRO** `hora_utc` > `18.0` → IC=-0.141 (n=318)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=1159)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.278 (n=349)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=1128)

- **FILTRO** `ibs_7min` > `0.1878` → IC=-0.161 (n=502)

  - _Acción_: SKIP cuando `ibs_7min` > 0.1878
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=975)

- **FILTRO** `ballena_activa_n` > `26.0` → IC=-0.180 (n=492)

  - _Acción_: SKIP cuando `ballena_activa_n` > 26.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=985)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.228 (n=420)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=1277)

- **FILTRO** `ibs_7min` < `0.7727` → IC=-0.196 (n=422)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7727
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1275)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.189 (n=413)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=1284)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.189 (n=484)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=1494)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.38` → IC=-0.290 (n=360)

  - _Acción_: SKIP cuando `py_entrada` < 0.38
  - _Potencial_: sin este filtro IC_bueno=-0.000 (n=1111)

- **FILTRO** `ibs_7min` < `0.7532` → IC=-0.210 (n=367)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7532
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=1104)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.223 (n=363)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=1108)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.266 (n=378)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=1441)

- **FILTRO** `ibs_7min` > `0.8158` → IC=-0.167 (n=454)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8158
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=1365)

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

- **PATRÓN** `delta_ratio` |x|> `0.4489` → IC=+0.179 (n=104)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio` |x|> 0.4489 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.150 (n=161)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 11.0 (IC base=+0.122)

- **PATRÓN** `total_vol_5m` < `451.687` → IC=+0.204 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 451.687 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `3582.6278` → IC=+0.154 (n=79)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 3582.6278 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.123 (n=136)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 47.0 (IC base=+0.122)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `12.0` → IC=+0.255 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.142)

- **PATRÓN** `total_vol_5m` < `302.608` → IC=+0.173 (n=47)

  - _Acción_: Kelly boost +0.87€ cuando `total_vol_5m` < 302.608 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.167 (n=64)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 53.0 (IC base=+0.142)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `hora_utc` > `12.0` → IC=+0.157 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 12.0 (IC base=+0.103)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.136 (n=42)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.02 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `2025.6726` → IC=+0.167 (n=46)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2025.6726 (IC base=+0.103)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4208` → IC=+0.206 (n=15)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4208 (IC base=+0.122)

- **PATRÓN** `total_vol_5m` < `498.822` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 498.822 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `8777.9174` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 8777.9174 (IC base=+0.122)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4055` → IC=+0.194 (n=34)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.97€ cuando `delta_ratio` |x|> 0.4055 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `3221.1629` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 3221.1629 (IC base=+0.135)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.136 (n=20)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 33.0 (IC base=+0.043)

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
- **FILTRO** `hora_utc` < `5.0` → IC=-0.333 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=33)

- **FILTRO** `ballena_activa_n` > `67.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `ballena_activa_n` > 67.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=30)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=83)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.176 (n=32)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 34.0 (IC base=+0.028)

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

- **FILTRO** `hora_utc` < `15.0` → IC=-0.132 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=11)

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
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=147)

- **PATRÓN** `streak_estiramiento` < `0.291` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `streak_estiramiento` < 0.291 (IC base=+0.011)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=309)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=164)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.090 (n=220)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.129 (n=157)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 14.0 (IC base=+0.074)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=1209)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=694)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=702)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.149 (n=129)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.003 (IC base=+0.116)

- **PATRÓN** `drift_60min` |x|≤ `0.1648` → IC=+0.129 (n=340)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.1648 (IC base=+0.116)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0676` → IC=+0.127 (n=387)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.64€ cuando `delta_ratio_macro` |x|> 0.0676 (IC base=+0.116)

- **PATRÓN** `ibs_15` > `0.5275` → IC=+0.204 (n=386)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5275 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` > `0.3859` → IC=+0.179 (n=104)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.3859 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.629` → IC=+0.242 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.629 (IC base=+0.116)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.123 (n=404)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.01 (IC base=+0.116)

- **PATRÓN** `libro_liquidez` > `2967.0429` → IC=+0.149 (n=257)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 2967.0429 (IC base=+0.116)

### UPDOWN_GBM#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.0717` → IC=-0.127 (n=124)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.0717
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=373)

- **FILTRO** `ibs_15` < `0.2368` → IC=-0.214 (n=124)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.2368
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=373)

- **FILTRO** `sigma_ewma_delta_pct` > `6.565` → IC=-0.209 (n=53)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.565
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=444)

### UPDOWN_GBM#60min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1032` → IC=-0.222 (n=16)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1032
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=52)

- **FILTRO** `sigma_h` < `0.0058` → IC=-0.237 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0058
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=51)

- **FILTRO** `ibs_15` < `0.16` → IC=-0.289 (n=17)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.16
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=37)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=14)

### UPDOWN_GBM#BTC#15min
- **FILTRO** `hora_utc` > `17.0` → IC=-0.265 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=69)

- **FILTRO** `ibs_15` > `0.7185` → IC=-0.227 (n=20)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.7185
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=64)

- **FILTRO** `ibs_15` < `0.3405` → IC=-0.190 (n=27)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.3405
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=57)

- **FILTRO** `libro_liquidez` < `13914.5646` → IC=-0.293 (n=27)

  - _Acción_: SKIP cuando `libro_liquidez` < 13914.5646
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=57)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.157 (n=97)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0036 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.1945` → IC=+0.179 (n=110)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.1945 (IC base=+0.155)

- **PATRÓN** `drift_15min` |x|≤ `0.4671` → IC=+0.184 (n=74)

  - _Acción_: Kelly boost +0.92€ cuando `drift_15min` |x|≤ 0.4671 (IC base=+0.155)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2616` → IC=+0.218 (n=37)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2616 (IC base=+0.155)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1483` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1483 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.184 (n=112)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 4.0 (IC base=+0.155)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.172 (n=56)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 6.0 (IC base=+0.155)

- **PATRÓN** `ibs_15` > `0.9375` → IC=+0.288 (n=50)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9375 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.3054` → IC=+0.198 (n=51)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.3054 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` < `0.5427` → IC=+0.164 (n=120)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.5427 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.945` → IC=+0.202 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.945 (IC base=+0.155)

- **PATRÓN** `libro_liquidez` > `12448.5931` → IC=+0.167 (n=37)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 12448.5931 (IC base=+0.155)

### UPDOWN_GBM#BTC#5min
- **FILTRO** `sigma_h` < `0.0038` → IC=-0.145 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0038
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=29)

- **FILTRO** `ibs_15` < `0.1693` → IC=-0.214 (n=19)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.1693
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=39)

- **FILTRO** `libro_liquidez` < `13319.0258` → IC=-0.122 (n=43)

  - _Acción_: SKIP cuando `libro_liquidez` < 13319.0258
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=15)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `hora_utc` > `19.0` → IC=-0.132 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=80)

- **FILTRO** `ibs_15` < `0.6848` → IC=-0.192 (n=24)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6848
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=73)

### UPDOWN_GBM#ETH#15min
- **FILTRO** `ibs_15` < `0.617` → IC=-0.237 (n=36)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.617
  - _Potencial_: sin este filtro IC_bueno=+0.231 (n=76)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.121 (n=85)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.60€ cuando `sigma_h` < 0.0049 (IC base=+0.079)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2671` → IC=+0.200 (n=28)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2671 (IC base=+0.079)

- **PATRÓN** `ibs_15` > `0.617` → IC=+0.231 (n=76)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.617 (IC base=+0.079)

- **PATRÓN** `dist_vwap_pct` < `0.092` → IC=+0.133 (n=47)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.092 (IC base=+0.079)

- **PATRÓN** `sigma_ewma_delta_pct` > `15.544` → IC=+0.188 (n=30)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 15.544 (IC base=+0.079)

### UPDOWN_GBM#ETH#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1911` → IC=-0.172 (n=56)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1911
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=29)

- **FILTRO** `dist_vwap_pct` > `0.1635` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1635
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=70)

- **FILTRO** `drift_15min` |x|> `0.532` → IC=-0.158 (n=115)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.532
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=346)

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
- **FILTRO** `ibs_15` < `0.2` → IC=-0.395 (n=17)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=57)

- **FILTRO** `sigma_ewma_delta_pct` < `2.988` → IC=-0.155 (n=56)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 2.988
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=18)

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
- **PATRÓN** `delta_ratio_macro` |x|> `0.0597` → IC=+0.135 (n=102)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio_macro` |x|> 0.0597 (IC base=+0.099)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.140 (n=48)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 15.0 (IC base=+0.099)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.167 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 6.0 (IC base=+0.099)

- **PATRÓN** `ibs_15` > `0.4444` → IC=+0.167 (n=103)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.83€ cuando `ibs_15` > 0.4444 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` > `0.3587` → IC=+0.281 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3587 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.569` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.569 (IC base=+0.099)

- **PATRÓN** `libro_liquidez` > `2503.3208` → IC=+0.156 (n=91)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2503.3208 (IC base=+0.099)

- **PATRÓN** `ibs_15` < `0.1282` → IC=+0.209 (n=108)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1282 (IC base=+0.050)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.005` → IC=+0.389 (n=70)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.316)

- **PATRÓN** `drift_60min` |x|≤ `0.1957` → IC=+0.327 (n=154)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1957 (IC base=+0.316)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1528` → IC=+0.337 (n=102)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1528 (IC base=+0.316)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.337 (n=145)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.316)

- **PATRÓN** `ibs_15` > `0.8116` → IC=+0.370 (n=137)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8116 (IC base=+0.316)

- **PATRÓN** `dist_vwap_pct` > `0.156` → IC=+0.342 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.156 (IC base=+0.316)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.354` → IC=+0.341 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.354 (IC base=+0.316)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.317 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.316)

- **PATRÓN** `libro_liquidez` > `8216.2794` → IC=+0.368 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8216.2794 (IC base=+0.316)

- **PATRÓN** `ballena_activa_n` < `540.0` → IC=+0.380 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 540.0 (IC base=+0.316)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.197` → IC=+0.308 (n=76)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.197 (IC base=+0.295)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.403 (n=29)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.295)

- **PATRÓN** `drift_60min` |x|≤ `0.16` → IC=+0.321 (n=76)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.16 (IC base=+0.295)

- **PATRÓN** `drift_15min` |x|≤ `0.4136` → IC=+0.325 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4136 (IC base=+0.295)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1236` → IC=+0.441 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1236 (IC base=+0.295)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.333 (n=82)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.295)

- **PATRÓN** `ibs_15` > `0.8374` → IC=+0.338 (n=78)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8374 (IC base=+0.295)

- **PATRÓN** `dist_vwap_pct` > `0.4311` → IC=+0.393 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4311 (IC base=+0.295)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.816` → IC=+0.308 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.816 (IC base=+0.295)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.39` → IC=+0.295 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.39 (IC base=+0.295)

- **PATRÓN** `libro_liquidez` > `8657.61` → IC=+0.381 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8657.61 (IC base=+0.295)

- **PATRÓN** `ballena_activa_n` < `480.0` → IC=+0.447 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 480.0 (IC base=+0.295)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.344 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.335)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.379 (n=31)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.335)

- **PATRÓN** `drift_60min` |x|≤ `0.1189` → IC=+0.372 (n=45)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1189 (IC base=+0.335)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1322` → IC=+0.394 (n=45)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1322 (IC base=+0.335)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.365 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.335)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.333 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.335)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.344 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.335)

- **PATRÓN** `ibs_15` > `0.8044` → IC=+0.419 (n=60)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8044 (IC base=+0.335)

- **PATRÓN** `dist_vwap_pct` < `0.3445` → IC=+0.350 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3445 (IC base=+0.335)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.011` → IC=+0.405 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.011 (IC base=+0.335)

- **PATRÓN** `libro_liquidez` > `3261.6008` → IC=+0.351 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3261.6008 (IC base=+0.335)

- **PATRÓN** `ballena_activa_n` < `188.0` → IC=+0.339 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 188.0 (IC base=+0.335)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0097` → IC=-0.165 (n=255)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0097
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=769)

- **FILTRO** `ibs_15` < `0.6897` → IC=-0.155 (n=201)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6897
  - _Potencial_: sin este filtro IC_bueno=+0.269 (n=201)

- **FILTRO** `sigma_ewma_delta_pct` > `17.437` → IC=-0.168 (n=347)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.437
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=2586)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.357` → IC=+0.160 (n=139)

  - _Acción_: Kelly boost +0.80€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.357 (IC base=-0.059)

- **PATRÓN** `ibs_15` > `0.6897` → IC=+0.269 (n=201)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6897 (IC base=-0.059)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1301` → IC=+0.263 (n=112)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1301 (IC base=-0.082)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0665` → IC=+0.291 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0665 (IC base=-0.082)

- **PATRÓN** `ibs_15` < `0.3357` → IC=+0.325 (n=169)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3357 (IC base=-0.082)

- **PATRÓN** `dist_vwap_pct` < `0.2198` → IC=+0.255 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2198 (IC base=-0.082)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0075` → IC=-0.245 (n=159)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0075
  - _Potencial_: sin este filtro IC_bueno=-0.201 (n=480)

- **FILTRO** `sigma_h` < `0.0035` → IC=-0.222 (n=210)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0035
  - _Potencial_: sin este filtro IC_bueno=-0.208 (n=429)

- **FILTRO** `sigma_ewma_delta_pct` > `19.895` → IC=-0.265 (n=117)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.895
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=522)

- **FILTRO** `libro_liquidez` < `16157.8203` → IC=-0.219 (n=479)

  - _Acción_: SKIP cuando `libro_liquidez` < 16157.8203
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=160)

- **PATRÓN** `ibs_15` > `0.8545` → IC=+0.441 (n=15)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8545 (IC base=+0.017)

- **PATRÓN** `dist_vwap_pct` < `0.3854` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.3854 (IC base=+0.017)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.4592` → IC=-0.348 (n=44)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.4592
  - _Potencial_: sin este filtro IC_bueno=+0.181 (n=133)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=160)

- **PATRÓN** `drift_60min` |x|≤ `0.0629` → IC=+0.181 (n=45)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.0629 (IC base=+0.048)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3719` → IC=+0.236 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3719 (IC base=+0.048)

- **PATRÓN** `ibs_15` > `0.4592` → IC=+0.181 (n=133)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.91€ cuando `ibs_15` > 0.4592 (IC base=+0.048)

- **PATRÓN** `libro_liquidez` > `9861.0594` → IC=+0.198 (n=61)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 9861.0594 (IC base=+0.048)

- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1045` → IC=+0.257 (n=68)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1045 (IC base=+0.237)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.250 (n=90)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.007 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0061` → IC=+0.243 (n=68)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0061 (IC base=+0.237)

- **PATRÓN** `drift_15min` |x|≤ `0.4361` → IC=+0.278 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4361 (IC base=+0.237)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1369` → IC=+0.286 (n=68)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1369 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.275 (n=38)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.306 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.237)

- **PATRÓN** `ibs_15` < `0.3299` → IC=+0.327 (n=102)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3299 (IC base=+0.237)

- **PATRÓN** `dist_vwap_pct` < `0.1207` → IC=+0.262 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1207 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.486` → IC=+0.264 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.486 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `12545.3929` → IC=+0.250 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12545.3929 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `209.0` → IC=+0.257 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 209.0 (IC base=+0.237)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_15min` |x|> `0.7757` → IC=-0.214 (n=61)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.7757
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=184)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.102 (n=224)

- **FILTRO** `sigma_ewma_delta_pct` > `15.88` → IC=-0.147 (n=114)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 15.88
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=903)

- **PATRÓN** `ibs_15` > `0.8125` → IC=+0.206 (n=15)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8125 (IC base=-0.107)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `drift_15min` |x|> `1.1396` → IC=-0.242 (n=64)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.1396
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=193)

- **FILTRO** `sigma_ewma_delta_pct` > `14.492` → IC=-0.184 (n=36)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 14.492
  - _Potencial_: sin este filtro IC_bueno=-0.137 (n=221)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.172 (n=59)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.135 (n=198)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.282 (n=241)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.280)

- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.293 (n=109)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0055 (IC base=+0.280)

- **PATRÓN** `drift_60min` |x|≤ `0.0537` → IC=+0.331 (n=81)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0537 (IC base=+0.280)

- **PATRÓN** `drift_15min` |x|≤ `0.8513` → IC=+0.282 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.8513 (IC base=+0.280)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1879` → IC=+0.330 (n=110)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1879 (IC base=+0.280)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1222` → IC=+0.354 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1222 (IC base=+0.280)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.310 (n=251)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.280)

- **PATRÓN** `ibs_15` > `0.9652` → IC=+0.356 (n=109)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9652 (IC base=+0.280)

- **PATRÓN** `dist_vwap_pct` > `0.3017` → IC=+0.345 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3017 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.888` → IC=+0.282 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.888 (IC base=+0.280)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.280 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `12445.3624` → IC=+0.342 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12445.3624 (IC base=+0.280)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.274 (n=60)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.264)

- **PATRÓN** `sigma_h` > `0.006` → IC=+0.287 (n=45)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.264)

- **PATRÓN** `drift_60min` |x|≤ `0.1873` → IC=+0.290 (n=136)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1873 (IC base=+0.264)

- **PATRÓN** `drift_15min` |x|≤ `0.6649` → IC=+0.277 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.6649 (IC base=+0.264)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1449` → IC=+0.293 (n=90)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1449 (IC base=+0.264)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1224` → IC=+0.346 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1224 (IC base=+0.264)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.315 (n=63)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.264)

- **PATRÓN** `ibs_15` > `0.9676` → IC=+0.328 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9676 (IC base=+0.264)

- **PATRÓN** `dist_vwap_pct` > `0.3186` → IC=+0.357 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3186 (IC base=+0.264)

- **PATRÓN** `sigma_ewma_delta_pct` > `24.523` → IC=+0.288 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 24.523 (IC base=+0.264)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.866` → IC=+0.272 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.866 (IC base=+0.264)

- **PATRÓN** `libro_liquidez` > `13620.7369` → IC=+0.330 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13620.7369 (IC base=+0.264)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.306 (n=106)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0076 (IC base=+0.296)

- **PATRÓN** `drift_60min` |x|≤ `0.0637` → IC=+0.337 (n=47)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0637 (IC base=+0.296)

- **PATRÓN** `drift_15min` |x|≤ `0.9353` → IC=+0.296 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.9353 (IC base=+0.296)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1843` → IC=+0.380 (n=48)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1843 (IC base=+0.296)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3059` → IC=+0.352 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3059 (IC base=+0.296)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.329 (n=109)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.296)

- **PATRÓN** `ibs_15` > `0.8702` → IC=+0.333 (n=94)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8702 (IC base=+0.296)

- **PATRÓN** `dist_vwap_pct` > `0.6525` → IC=+0.380 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6525 (IC base=+0.296)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.952` → IC=+0.296 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.952 (IC base=+0.296)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.664` → IC=+0.296 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.664 (IC base=+0.296)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.308 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.296)

- **PATRÓN** `libro_liquidez` > `10584.3604` → IC=+0.392 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10584.3604 (IC base=+0.296)

- **PATRÓN** `ballena_activa_n` < `261.0` → IC=+0.313 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 261.0 (IC base=+0.296)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1065` → IC=-0.258 (n=31)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1065
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=63)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1218` → IC=-0.180 (n=95)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1218
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=290)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1324` → IC=-0.158 (n=36)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1324
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=13)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `drift_15min` |x|> `0.2326` → IC=-0.222 (n=16)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.2326
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=18)

- **PATRÓN** `drift_60min` |x|≤ `0.0961` → IC=+0.147 (n=15)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.0961 (IC base=+0.100)

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
- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5275 sube el IC de +0.116 a +0.204 en UPDOWN_GBM#15min (n=386). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.9375 sube el IC de +0.155 a +0.288 en UPDOWN_GBM#BTC#15min (n=50). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.617 sube el IC de +0.079 a +0.231 en UPDOWN_GBM#ETH#15min (n=76). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.056 a +0.265 en UPDOWN_GBM#SOL#15min (n=32). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.4444 sube el IC de +0.099 a +0.167 en UPDOWN_GBM#XRP#15min (n=103). Ya aplicado como kelly_boost=+0.83€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1282 sube el IC de +0.050 a +0.209 en UPDOWN_GBM#XRP#15min (n=108). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6897 sube el IC de -0.059 a +0.269 en UPDOWN_GBM_15M_TARDIO (n=201). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3357 sube el IC de -0.082 a +0.325 en UPDOWN_GBM_15M_TARDIO (n=169). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.8545 sube el IC de +0.017 a +0.441 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=15). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.4592 sube el IC de +0.048 a +0.181 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=133). Ya aplicado como kelly_boost=+0.91€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3299 sube el IC de +0.237 a +0.327 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=102). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8125 sube el IC de -0.107 a +0.206 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=15). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.9652 sube el IC de +0.280 a +0.356 en UPDOWN_GBM_IBS_ALTO (n=109). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.9676 sube el IC de +0.264 a +0.328 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8702 sube el IC de +0.296 a +0.333 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=94). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.8116 sube el IC de +0.316 a +0.370 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=137). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8374 sube el IC de +0.295 a +0.338 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=78). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.8044 sube el IC de +0.335 a +0.419 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=60). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min` — IC=+0.353 n=32. Faltan ~8 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL` — IC=+0.353 n=32. Faltan ~8 resoluciones para umbral n≥40. ETA: ~6h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 616 | +0.091 | +49.55€ | 1 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 616 | +0.091 | +49.55€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 371 | +0.117 | +38.03€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 371 | +0.117 | +38.03€ | 0 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 216 | +0.032 | +0.59€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 216 | +0.032 | +0.59€ | 7 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 29 | +0.177 | +10.93€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 29 | +0.177 | +10.93€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 10086 | -0.094 | -1597.85€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 721 | -0.071 | -127.98€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 9365 | -0.096 | -1469.87€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 1237 | -0.011 | -211.81€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 1237 | -0.011 | -211.81€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 721 | -0.071 | -127.98€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 721 | -0.071 | -127.98€ | 2 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 1290 | -0.163 | -415.20€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 1290 | -0.163 | -415.20€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 2729 | -0.068 | -262.92€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 2729 | -0.068 | -262.92€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 2357 | -0.076 | -151.68€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 2357 | -0.076 | -151.68€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 1752 | -0.177 | -428.25€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 1752 | -0.177 | -428.25€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 120 | -0.082 | +41.62€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 33 | -0.014 | +14.93€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 87 | -0.107 | +26.68€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 120 | -0.082 | +41.62€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 33 | -0.014 | +14.93€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 87 | -0.107 | +26.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 33382 | +0.116 | -2071.38€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 6101 | +0.186 | -225.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 108 | -0.109 | -51.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 23939 | +0.098 | -1750.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 3234 | +0.120 | -43.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 4019 | +0.066 | -669.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 21 | -0.065 | +2.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#240min | 5 | -0.089 | -6.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 3993 | +0.067 | -665.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 6874 | +0.134 | -142.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 1727 | +0.194 | -104.71€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 3984 | +0.112 | -75.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 1121 | +0.131 | +59.63€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 4025 | +0.082 | -494.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 21 | +0.065 | +3.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 4003 | +0.082 | -495.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 7375 | +0.128 | -103.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 2218 | +0.167 | -22.08€ | 0 | 7 |
| 🚫 FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 3986 | +0.115 | -46.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 1159 | +0.100 | -26.30€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 7074 | +0.136 | -413.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 2097 | +0.205 | -103.53€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 47 | -0.010 | -11.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 3976 | +0.101 | -222.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 954 | +0.132 | -76.35€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 4015 | +0.109 | -247.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 17 | -0.022 | -0.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 3997 | +0.110 | -245.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 6041 | +0.173 | -473.37€ | 3 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 6041 | +0.173 | -473.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 1523 | +0.166 | -163.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 1523 | +0.166 | -163.11€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 116 | -0.119 | +1.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 116 | -0.119 | +1.15€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 1503 | +0.163 | -171.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 1503 | +0.163 | -171.18€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 1355 | +0.230 | -38.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 1355 | +0.230 | -38.95€ | 0 | 2 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 1465 | +0.183 | -115.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 1465 | +0.183 | -115.04€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 307 | +0.445 | +2.91€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 307 | +0.445 | +2.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 116 | +0.441 | +1.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 116 | +0.441 | +1.07€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 113 | +0.430 | -0.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 113 | +0.430 | -0.95€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 75 | +0.448 | +2.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 75 | +0.448 | +2.65€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 17103 | +0.191 | -1500.98€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 17103 | +0.191 | -1500.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 3127 | +0.127 | -573.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 3127 | +0.127 | -573.95€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 2663 | +0.235 | -58.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 2663 | +0.235 | -58.66€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 2934 | +0.165 | -367.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 2934 | +0.165 | -367.33€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 2720 | +0.228 | -86.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 2720 | +0.228 | -86.64€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 2780 | +0.217 | -131.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 2780 | +0.217 | -131.15€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 2879 | +0.185 | -283.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 2879 | +0.185 | -283.25€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 6198 | +0.133 | +225.84€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 6198 | +0.133 | +225.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 3086 | +0.140 | +147.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 3086 | +0.140 | +147.66€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 3112 | +0.127 | +78.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 3112 | +0.127 | +78.18€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 783 | +0.301 | +8.16€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 783 | +0.301 | +8.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 335 | +0.286 | -3.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 335 | +0.286 | -3.85€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 368 | +0.300 | +7.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 368 | +0.300 | +7.71€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 80 | +0.354 | +4.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 80 | +0.354 | +4.30€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 333 | +0.416 | -12.57€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 333 | +0.416 | -12.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 149 | +0.414 | -6.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 149 | +0.414 | -6.25€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 152 | +0.422 | -5.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 152 | +0.422 | -5.16€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 32 | +0.353 | -1.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 32 | +0.353 | -1.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 249 | +0.102 | +0.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 72 | +0.149 | +5.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 177 | +0.081 | -5.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 8 | +0.120 | +4.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 8 | +0.120 | +4.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 205 | +0.094 | -1.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 28 | +0.167 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 177 | +0.081 | -5.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 36 | +0.079 | -2.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 36 | +0.079 | -2.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 6947 | +0.096 | -242.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 701 | +0.058 | -34.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 6246 | +0.100 | -207.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 4688 | +0.095 | -111.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 701 | +0.058 | -34.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 3987 | +0.102 | -76.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 163 | +0.094 | -4.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 163 | +0.094 | -4.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 2096 | +0.096 | -126.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 2096 | +0.096 | -126.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 441 | +0.292 | -21.91€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 441 | +0.292 | -21.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 441 | +0.292 | -21.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 441 | +0.292 | -21.91€ | 0 | 4 |
| ✅ GBM_LATE_15M | 7980 | +0.043 | +2537.31€ | 0 | 15 |
| ✅ GBM_LATE_15M#15min | 7980 | +0.043 | +2537.31€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 1094 | +0.172 | +679.80€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 1094 | +0.172 | +679.80€ | 0 | 20 |
| ✅ GBM_LATE_15M#BTC | 1132 | +0.170 | +644.53€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 1132 | +0.170 | +644.53€ | 0 | 31 |
| ✅ GBM_LATE_15M#DOGE | 1098 | +0.192 | +768.89€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 1098 | +0.192 | +768.89€ | 0 | 19 |
| ✅ GBM_LATE_15M#ETH | 1302 | -0.044 | +42.38€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 1302 | -0.044 | +42.38€ | 2 | 11 |
| ✅ GBM_LATE_15M#SOL | 1457 | -0.049 | +124.66€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 1457 | -0.049 | +124.66€ | 4 | 4 |
| ✅ GBM_LATE_15M#XRP | 1897 | -0.061 | +277.05€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 1897 | -0.061 | +277.05€ | 4 | 6 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 8897 | +0.047 | +3545.80€ | 0 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 8897 | +0.047 | +3545.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 1387 | -0.017 | +678.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 1387 | -0.017 | +678.03€ | 2 | 4 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 1936 | -0.039 | +156.74€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 1936 | -0.039 | +156.74€ | 1 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 966 | +0.244 | +898.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 966 | +0.244 | +898.01€ | 0 | 22 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 1475 | -0.046 | +5.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 1475 | -0.046 | +5.13€ | 8 | 2 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 1576 | -0.023 | +335.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 1576 | -0.023 | +335.10€ | 7 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 1557 | +0.246 | +1472.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 1557 | +0.246 | +1472.78€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 6472 | +0.169 | +4419.02€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 6472 | +0.169 | +4419.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 838 | +0.183 | +584.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 838 | +0.183 | +584.15€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 1098 | +0.158 | +716.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 1098 | +0.158 | +716.34€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 820 | +0.206 | +648.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 820 | +0.206 | +648.08€ | 0 | 18 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 1075 | +0.157 | +677.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 1075 | +0.157 | +677.17€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 1231 | +0.124 | +721.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 1231 | +0.124 | +721.92€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 1410 | +0.194 | +1071.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 1410 | +0.194 | +1071.37€ | 0 | 22 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 1176 | +0.083 | +260.65€ | 0 | 12 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 1176 | +0.083 | +260.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 56 | +0.086 | +14.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 56 | +0.086 | +14.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 332 | +0.105 | +107.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 332 | +0.105 | +107.04€ | 3 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 113 | +0.143 | +49.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 113 | +0.143 | +49.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 217 | +0.180 | +74.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 217 | +0.180 | +74.83€ | 1 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 310 | -0.022 | -0.74€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 310 | -0.022 | -0.74€ | 4 | 3 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 148 | +0.060 | +14.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 148 | +0.060 | +14.84€ | 0 | 6 |
| ✅ GBM_LATE_15M_TARDIO | 7576 | +0.169 | +5028.65€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#15min | 7576 | +0.169 | +5028.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 1047 | +0.194 | +767.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 1047 | +0.194 | +767.32€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 1233 | +0.158 | +766.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 1233 | +0.158 | +766.28€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 1036 | +0.216 | +849.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 1036 | +0.216 | +849.79€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 1171 | +0.146 | +685.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 1171 | +0.146 | +685.62€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 1355 | +0.104 | +658.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 1355 | +0.104 | +658.90€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 1734 | +0.196 | +1300.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 1734 | +0.196 | +1300.75€ | 0 | 23 |
| ✅ GBM_LATE_5M | 1889 | +0.132 | +877.56€ | 1 | 26 |
| ✅ GBM_LATE_5M#5min | 1889 | +0.132 | +877.56€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 95 | +0.222 | +72.24€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 95 | +0.222 | +72.24€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 710 | +0.128 | +364.10€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 710 | +0.128 | +364.10€ | 3 | 17 |
| ✅ GBM_LATE_5M#DOGE | 121 | +0.175 | +68.08€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 121 | +0.175 | +68.08€ | 0 | 10 |
| ✅ GBM_LATE_5M#ETH | 629 | +0.140 | +284.09€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 629 | +0.140 | +284.09€ | 0 | 29 |
| ✅ GBM_LATE_5M#SOL | 125 | -0.020 | +0.12€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 125 | -0.020 | +0.12€ | 3 | 0 |
| ✅ GBM_LATE_5M#XRP | 209 | +0.140 | +88.94€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 209 | +0.140 | +88.94€ | 0 | 0 |
| ✅ GBM_LATE_60M | 520 | -0.035 | +86.81€ | 5 | 9 |
| ✅ GBM_LATE_60M#60min | 520 | -0.035 | +86.81€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 179 | +0.003 | +5.34€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 179 | +0.003 | +5.34€ | 2 | 3 |
| ✅ GBM_LATE_60M#ETH | 187 | -0.003 | +57.88€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 187 | -0.003 | +57.88€ | 2 | 8 |
| ✅ GBM_LATE_60M#SOL | 154 | -0.115 | +23.59€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 154 | -0.115 | +23.59€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE | 195 | -0.302 | -33.28€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 195 | -0.302 | -33.28€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 77 | -0.260 | -7.87€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 77 | -0.260 | -7.87€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 65 | -0.351 | -19.05€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 65 | -0.351 | -19.05€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 53 | -0.282 | -6.35€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 53 | -0.282 | -6.35€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 338 | +0.035 | +0.54€ | 2 | 1 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 338 | +0.035 | +0.54€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 136 | +0.022 | +5.04€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 136 | +0.022 | +5.04€ | 3 | 5 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 85 | +0.063 | -0.03€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 85 | +0.063 | -0.03€ | 0 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 117 | +0.029 | -4.47€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 117 | +0.029 | -4.47€ | 2 | 5 |
| ✅ LATE_WINDOW_5MIN | 18 | +0.225 | +5.31€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 18 | +0.225 | +5.31€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 18 | +0.225 | +5.31€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 18 | +0.225 | +5.31€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 318 | +0.116 | +95.73€ | 0 | 7 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 318 | +0.116 | +95.73€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 318 | +0.116 | +95.73€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 318 | +0.116 | +95.73€ | 0 | 7 |
| ✅ LIQUIDACIONES_15M | 216 | -0.110 | -29.46€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 216 | -0.110 | -29.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 55 | -0.132 | -9.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 55 | -0.132 | -9.15€ | 2 | 0 |
| 🚫 LIQUIDACIONES_15M#DOGE | 22 | -0.208 | -5.32€ | 0 | 0 |
| 🚫 LIQUIDACIONES_15M#DOGE#15min | 22 | -0.208 | -5.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 44 | -0.043 | -3.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 44 | -0.043 | -3.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 44 | +0.000 | -0.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 44 | +0.000 | -0.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 46 | -0.167 | -8.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 46 | -0.167 | -8.95€ | 2 | 0 |
| ✅ LIQUIDACIONES_5M | 703 | -0.021 | -9.68€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 703 | -0.021 | -9.68€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 41 | -0.058 | -4.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 41 | -0.058 | -4.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 110 | -0.036 | -1.13€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 110 | -0.036 | -1.13€ | 2 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 67 | -0.094 | -7.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 67 | -0.094 | -7.35€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 194 | +0.025 | +14.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 194 | +0.025 | +14.45€ | 2 | 3 |
| ✅ LIQUIDACIONES_5M#SOL | 241 | +0.006 | -2.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 241 | +0.006 | -2.55€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 50 | -0.154 | -8.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 50 | -0.154 | -8.60€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M | 455 | -0.008 | -2.94€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 455 | -0.008 | -2.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 143 | -0.038 | -10.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 143 | -0.038 | -10.45€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 141 | +0.004 | +1.89€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 141 | +0.004 | +1.89€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M#SOL | 171 | +0.009 | +5.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 171 | +0.009 | +5.62€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 4654 | -0.002 | -74.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 4654 | -0.002 | -74.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 520 | -0.008 | +0.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 520 | -0.008 | +0.39€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 598 | +0.005 | -8.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 598 | +0.005 | -8.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 822 | -0.007 | -26.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 822 | -0.007 | -26.80€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 962 | +0.012 | +17.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 962 | +0.012 | +17.45€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 840 | -0.002 | -25.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 840 | -0.002 | -25.17€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 912 | -0.014 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 912 | -0.014 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 7074 | -0.036 | +172.72€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 7074 | -0.036 | +172.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 1122 | -0.032 | +130.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 1122 | -0.032 | +130.07€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 1248 | -0.035 | -29.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 1248 | -0.035 | -29.00€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 1131 | -0.045 | +90.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 1131 | -0.045 | +90.73€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 1254 | -0.034 | -33.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 1254 | -0.034 | -33.57€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 1159 | -0.042 | +23.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 1159 | -0.042 | +23.17€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 1160 | -0.031 | -8.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 1160 | -0.031 | -8.69€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 555 | -0.060 | -42.01€ | 3 | 0 |
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
| ✅ MOMENTUM_IBS_5M | 3168 | +0.004 | -4.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3168 | +0.004 | -4.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 126 | -0.039 | -1.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 126 | -0.039 | -1.34€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 185 | +0.008 | -2.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 185 | +0.008 | -2.27€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 136 | +0.000 | -1.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 136 | +0.000 | -1.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1158 | +0.009 | +8.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1158 | +0.009 | +8.81€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1385 | +0.006 | -2.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1385 | +0.006 | -2.03€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 178 | -0.006 | -5.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 178 | -0.006 | -5.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 19555 | -0.076 | +263.83€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 19555 | -0.076 | +263.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 3038 | -0.090 | +356.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 3038 | -0.090 | +356.79€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 3445 | -0.064 | -36.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 3445 | -0.064 | -36.33€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 3145 | -0.086 | +16.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 3145 | -0.086 | +16.65€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 2962 | -0.098 | -182.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 2962 | -0.098 | -182.13€ | 8 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 3675 | -0.049 | -22.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 3675 | -0.049 | -22.60€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 3290 | -0.075 | +131.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 3290 | -0.075 | +131.44€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 6012 | -0.010 | -119.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 6012 | -0.010 | -119.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 992 | -0.018 | -21.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 992 | -0.018 | -21.41€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1204 | +0.000 | -15.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1204 | +0.000 | -15.38€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1001 | -0.019 | -30.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1001 | -0.019 | -30.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1310 | -0.002 | -14.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1310 | -0.002 | -14.24€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 780 | -0.010 | -14.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 780 | -0.010 | -14.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 725 | -0.020 | -23.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 725 | -0.020 | -23.89€ | 2 | 0 |
| ✅ ORDER_FLOW_5M | 451 | +0.096 | +113.61€ | 1 | 5 |
| ✅ ORDER_FLOW_5M#5min | 315 | +0.112 | +101.02€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 93 | +0.142 | +46.64€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 93 | +0.142 | +46.64€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#DOGE | 61 | +0.103 | +14.28€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 61 | +0.103 | +14.28€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#ETH | 43 | +0.122 | +15.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 43 | +0.122 | +15.24€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#SOL | 50 | +0.135 | +18.82€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 50 | +0.135 | +18.82€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#XRP | 68 | +0.043 | +6.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 68 | +0.043 | +6.04€ | 0 | 1 |
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
| ✅ STREAK_FADE_15M | 155 | -0.003 | -9.03€ | 3 | 1 |
| ✅ STREAK_FADE_15M#15min | 155 | -0.003 | -9.03€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 63 | -0.023 | -7.48€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 63 | -0.023 | -7.48€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 10 | +0.000 | -0.13€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 10 | +0.000 | -0.13€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 16 | +0.089 | +1.68€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 16 | +0.089 | +1.68€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP | 66 | -0.015 | -3.10€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 66 | -0.015 | -3.10€ | 0 | 0 |
| ✅ STREAK_FADE_5M | 1118 | -0.023 | -54.25€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 1118 | -0.023 | -54.25€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 392 | -0.023 | -15.21€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 392 | -0.023 | -15.21€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 394 | -0.008 | -11.31€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 394 | -0.008 | -11.31€ | 3 | 0 |
| ✅ STREAK_FADE_5M#SOL | 132 | -0.037 | -12.47€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 132 | -0.037 | -12.47€ | 2 | 0 |
| ✅ STREAK_FADE_5M#XRP | 200 | -0.045 | -15.27€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 200 | -0.045 | -15.27€ | 4 | 0 |
| ✅ STREAK_FADE_60M | 31 | -0.045 | -1.98€ | 0 | 0 |
| ✅ STREAK_FADE_60M#60min | 31 | -0.045 | -1.98€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 19 | -0.113 | -2.76€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 19 | -0.113 | -2.76€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 12 | +0.043 | +0.78€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 12 | +0.043 | +0.78€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 2307 | +0.030 | +50.94€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 2307 | +0.030 | +50.94€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 763 | +0.032 | +14.30€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 763 | +0.032 | +14.30€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 426 | +0.026 | +8.37€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 426 | +0.026 | +8.37€ | 1 | 1 |
| ✅ STREAK_MOM_5M#SOL | 692 | +0.029 | +9.35€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 692 | +0.029 | +9.35€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 426 | +0.035 | +18.91€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 426 | +0.035 | +18.91€ | 2 | 1 |
| ✅ STRUCT_NO_15M | 3193 | +0.009 | -28.33€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 3193 | +0.009 | -28.33€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 1228 | +0.011 | -8.85€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 1228 | +0.011 | -8.85€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 1239 | +0.016 | -2.26€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 1239 | +0.016 | -2.26€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 726 | -0.008 | -17.21€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 726 | -0.008 | -17.21€ | 2 | 0 |
| ✅ UPDOWN_GBM | 6252 | +0.004 | +145.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 2302 | +0.044 | +228.31€ | 0 | 8 |
| ✅ UPDOWN_GBM#240min | 262 | +0.015 | +2.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 3252 | -0.019 | -75.77€ | 3 | 0 |
| ✅ UPDOWN_GBM#60min | 389 | -0.014 | -8.80€ | 4 | 0 |
| ✅ UPDOWN_GBM#BNB | 196 | +0.091 | +38.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 179 | +0.119 | +42.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 8 | -0.040 | -1.01€ | 0 | 0 |
| 🚫 UPDOWN_GBM#BNB#5min | 9 | -0.102 | -2.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 1395 | +0.016 | +63.61€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 230 | +0.073 | +35.65€ | 4 | 12 |
| ✅ UPDOWN_GBM#BTC#240min | 76 | +0.064 | +6.23€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 945 | +0.009 | +27.03€ | 3 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 126 | -0.039 | -7.13€ | 2 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 781 | -0.007 | -1.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 122 | +0.105 | +29.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 9 | +0.021 | +0.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 650 | -0.029 | -31.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 1478 | +0.003 | +4.86€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 669 | +0.025 | +21.46€ | 1 | 5 |
| ✅ UPDOWN_GBM#ETH#240min | 76 | +0.077 | +6.33€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 546 | -0.031 | -23.33€ | 3 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 172 | +0.011 | +0.78€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 1521 | -0.013 | -25.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 536 | -0.004 | -4.08€ | 1 | 2 |
| ✅ UPDOWN_GBM#SOL#240min | 61 | -0.024 | -3.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 821 | -0.013 | -14.38€ | 2 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 91 | -0.027 | -2.45€ | 1 | 3 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 879 | +0.009 | +67.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 566 | +0.062 | +103.67€ | 0 | 8 |
| ✅ UPDOWN_GBM#XRP#240min | 32 | -0.147 | -5.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 281 | -0.080 | -30.60€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 204 | +0.316 | +40.65€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 204 | +0.316 | +40.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 115 | +0.295 | +13.71€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 115 | +0.295 | +13.71€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 89 | +0.335 | +26.94€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 89 | +0.335 | +26.94€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 3957 | -0.076 | +807.80€ | 3 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 3957 | -0.076 | +807.80€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 303 | -0.051 | +341.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 303 | -0.051 | +341.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 813 | -0.164 | -94.72€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 813 | -0.164 | -94.72€ | 4 | 2 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 77 | +0.070 | +14.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 77 | +0.070 | +14.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 312 | +0.131 | +138.86€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 312 | +0.131 | +138.86€ | 2 | 16 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 1262 | -0.074 | +203.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 1262 | -0.074 | +203.77€ | 3 | 1 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 1190 | -0.087 | +204.08€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 1190 | -0.087 | +204.08€ | 3 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 30 | +0.000 | -1.64€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 30 | +0.000 | -1.64€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 30 | +0.000 | -1.64€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 30 | +0.000 | -1.64€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 320 | +0.280 | +240.39€ | 0 | 12 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 320 | +0.280 | +240.39€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 180 | +0.264 | +125.18€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 180 | +0.264 | +125.18€ | 0 | 12 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 140 | +0.296 | +115.20€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 140 | +0.296 | +115.20€ | 0 | 13 |
| ✅ UPDOWN_OU_5M | 479 | -0.078 | -43.66€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#5min | 479 | -0.078 | -43.66€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 268 | -0.048 | -23.64€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 268 | -0.048 | -23.64€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 77 | +0.019 | +4.60€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 77 | +0.019 | +4.60€ | 1 | 1 |
| ✅ UPDOWN_OU_5M#DOGE | 30 | -0.188 | -6.21€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 30 | -0.188 | -6.21€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 37 | -0.167 | -5.83€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 37 | -0.167 | -5.83€ | 0 | 0 |
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
  - _Estado_: Spread bajo (0.089) — sin ventaja clara. oversold(IBS<0.3): IC=+0.012 n=2211 | neutral: IC=-0.001 n=2383 | overbought(IBS>0.7): IC=+0.088 n=2459
  - _Datos_: n=7370 IC=+0.034 PNL=+648.67€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: (cache 411s) 24 celda(s) GATE OK de 2107 trackeadas

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=-0.004 < 0.08 — monitorear
  - _Datos_: n=536 IC=-0.004 PNL=-4.08€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=346/15 IC=+0.262 PNL=+82.89€ | BTC: n=329/15 IC=+0.204 PNL=-2.32€ | SOL: n=425/15 IC=+0.371 PNL=+370.23€

**🟡 H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.076 n=101443 | tras_1loss IC=+0.045 n=78971 | tras_2loss IC=+0.009 n=35844/40 | gap=+0.067 (umbral 0.05)

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
  - _Estado_: 6190 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.100 n=43/60 | contraria IC=+0.000 n=24 | gap=+0.100 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=66, boost estimado=+0.022. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 50 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=172/40 IC=+0.011 PNL=+0.78€ | BTC#60min: n=126/40 IC=-0.039 PNL=-7.13€ | SOL#60min: n=91/40 IC=-0.027 PNL=-2.45€

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=-0.013 n=664 | contrario_BTC IC=-0.014 n=504/40 | gap=-0.000 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: 13/25 ops en el filtro definido (IC actual=+0.238 PNL=+15.01€)
  - _Datos_: n=13 IC=+0.238 PNL=+15.01€

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
  - _Estado_: n=58 IC=+0.033 PNL=+10.85€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=58 IC=+0.033 PNL=+10.85€

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
  - _Estado_: n=6005 IC=+0.001 PNL=+95.96€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=6005 IC=+0.001 PNL=+95.96€

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
  - _Estado_: n=321 IC=+0.005 PNL=-0.91€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=321 IC=+0.005 PNL=-0.91€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=68 IC=-0.100 PNL=-7.88€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=68 IC=-0.100 PNL=-7.88€

**🔴 H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.089 < -0.08 con n=105 PNL=-9.28€
  - _Datos_: n=105 IC=-0.089 PNL=-9.28€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.116 > 0.1 con n=514 PNL=+121.06€
  - _Datos_: n=514 IC=+0.116 PNL=+121.06€

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
  - _Estado_: n=230 IC=+0.073 PNL=+35.65€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=230 IC=+0.073 PNL=+35.65€

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
  - _Estado_: n=1341 IC=+0.026 PNL=+80.99€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1341 IC=+0.026 PNL=+80.99€

**⏳ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: 23/30 ops en el filtro definido (IC actual=-0.220 PNL=-4.57€)
  - _Datos_: n=23 IC=-0.220 PNL=-4.57€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=72 IC=-0.013 PNL=+9.33€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=72 IC=-0.013 PNL=+9.33€

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
  - _Estado_: n=2192 IC=-0.019 PNL=-50.32€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2192 IC=-0.019 PNL=-50.32€

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
  - _Estado_: 18/30 ops en el filtro definido (IC actual=+0.225 PNL=+5.31€)
  - _Datos_: n=18 IC=+0.225 PNL=+5.31€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=1663 IC=+0.022 PNL=+98.77€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1663 IC=+0.022 PNL=+98.77€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=449 IC=+0.032 PNL=-0.41€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=449 IC=+0.032 PNL=-0.41€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.089 > 0.08 con n=110 PNL=+21.89€
  - _Datos_: n=110 IC=+0.089 PNL=+21.89€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.139 > 0.08 con n=120 PNL=+2.46€
  - _Datos_: n=120 IC=+0.139 PNL=+2.46€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.117 > 0.08 con n=118 PNL=+37.72€
  - _Datos_: n=118 IC=+0.117 PNL=+37.72€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=13361 IC=+0.100 PNL=+3819.65€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=13361 IC=+0.100 PNL=+3819.65€

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
  - _Estado_: n=834 IC=+0.030 PNL=+50.48€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=834 IC=+0.030 PNL=+50.48€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.125 > 0.02 con n=238 PNL=+70.72€
  - _Datos_: n=238 IC=+0.125 PNL=+70.72€

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
  - _Estado_: n=1532 IC=+0.023 PNL=+82.03€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=1532 IC=+0.023 PNL=+82.03€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.166 > 0.1 con n=779 PNL=+287.45€
  - _Datos_: n=779 IC=+0.166 PNL=+287.45€

**⏳ H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: 40
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: 26/40 ops en el filtro definido (IC actual=-0.286 PNL=-6.93€)
  - _Datos_: n=26 IC=-0.286 PNL=-6.93€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=431 IC=+0.050 PNL=+60.61€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=431 IC=+0.050 PNL=+60.61€

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
  - _Estado_: n=67 IC=+0.051 PNL=-0.68€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=67 IC=+0.051 PNL=-0.68€

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
  - _Estado_: n=4644 IC=-0.142 PNL=+201.56€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4644 IC=-0.142 PNL=+201.56€

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
  - _Estado_: n=605 IC=+0.138 PNL=+240.22€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=605 IC=+0.138 PNL=+240.22€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.116 > 0.08 con n=514 PNL=+121.06€
  - _Datos_: n=514 IC=+0.116 PNL=+121.06€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.155 > 0.08 con n=146 PNL=+43.51€
  - _Datos_: n=146 IC=+0.155 PNL=+43.51€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.231 < -0.1 con n=503 PNL=-49.62€
  - _Datos_: n=503 IC=-0.231 PNL=-49.62€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=1212 IC=+0.139 PNL=+623.16€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=1212 IC=+0.139 PNL=+623.16€

**⏳ H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: 40
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: 26/40 ops en el filtro definido (IC actual=+0.071 PNL=+4.01€)
  - _Datos_: n=26 IC=+0.071 PNL=+4.01€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=669 IC=-0.020 PNL=+54.42€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=669 IC=-0.020 PNL=+54.42€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.176 > 0.08 con n=578 PNL=+333.53€
  - _Datos_: n=578 IC=+0.176 PNL=+333.53€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=1005 IC=-0.051 PNL=+164.02€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1005 IC=-0.051 PNL=+164.02€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.112 > 0.08 con n=253 PNL=-35.60€
  - _Datos_: n=253 IC=+0.112 PNL=-35.60€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.244 > 0.08 con n=1454 PNL=-124.71€
  - _Datos_: n=1454 IC=+0.244 PNL=-124.71€

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
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.125 n=166) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=166 IC=+0.125 PNL=+50.82€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.351 > 0.08 con n=72 PNL=+50.11€
  - _Datos_: n=72 IC=+0.351 PNL=+50.11€

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
  - _Estado_: n=3127 IC=+0.127 PNL=-573.95€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=3127 IC=+0.127 PNL=-573.95€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.182 > 0.1 con n=42 PNL=+22.66€
  - _Datos_: n=42 IC=+0.182 PNL=+22.66€
