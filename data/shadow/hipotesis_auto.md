# Hipótesis automáticas — 2026-08-29 06:04 UTC
_Generado por shadow_postmortem.py sobre 198011 resoluciones (PNL=+14927.06€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **PATRÓN** `py_entrada` > `0.73` → IC=+0.288 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.167)

- **PATRÓN** `n_ballena_banda` > `19.0` → IC=+0.184 (n=245)

  - _Acción_: Kelly boost +0.92€ cuando `n_ballena_banda` > 19.0 (IC base=+0.167)

- **PATRÓN** `n_total_lado` > `73.0` → IC=+0.260 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 73.0 (IC base=+0.167)

- **PATRÓN** `banda_hit_calibrado` > `0.8187` → IC=+0.301 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8187 (IC base=+0.167)

- **PATRÓN** `banda_z` > `11.557` → IC=+0.296 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.557 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.197 (n=186)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 11.0 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.192 (n=280)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.01 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `3094.168` → IC=+0.234 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3094.168 (IC base=+0.167)

- **PATRÓN** `ballena_activa_n` < `127.0` → IC=+0.305 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 127.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` < `0.835` → IC=+0.123 (n=221)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.835 (IC base=-0.002)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.123 (n=51)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=109)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.291 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.207)

- **PATRÓN** `n_ballena_banda` > `18.0` → IC=+0.225 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `n_ballena_banda` > 18.0 (IC base=+0.207)

- **PATRÓN** `n_total_lado` > `56.0` → IC=+0.255 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 56.0 (IC base=+0.207)

- **PATRÓN** `banda_hit_calibrado` > `0.8197` → IC=+0.303 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8197 (IC base=+0.207)

- **PATRÓN** `banda_z` > `11.871` → IC=+0.295 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.871 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.230 (n=161)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.208 (n=128)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.220 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `3664.7129` → IC=+0.247 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3664.7129 (IC base=+0.207)

- **PATRÓN** `ballena_activa_n` < `242.0` → IC=+0.318 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 242.0 (IC base=+0.207)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.126 (n=113)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.495 (IC base=-0.018)

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

- **PATRÓN** `py_entrada` > `0.335` → IC=+0.195 (n=93)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.335 (IC base=+0.085)

- **PATRÓN** `banda_hit_calibrado` > `0.6329` → IC=+0.238 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6329 (IC base=+0.085)

- **PATRÓN** `banda_z` > `8.441` → IC=+0.197 (n=31)

  - _Acción_: Kelly boost +0.98€ cuando `banda_z` > 8.441 (IC base=+0.085)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.146 (n=97)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.02 (IC base=+0.085)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.134 (n=69)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.495 (IC base=-0.024)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `147.7` → IC=-0.286 (n=2771)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 147.7
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=8317)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `136.39` → IC=-0.269 (n=353)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 136.39
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=1060)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` > `625.57` → IC=-0.165 (n=264)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` > 625.57
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=513)

- **FILTRO** `restante_s_al_confirmar` < `412.47` → IC=-0.209 (n=194)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 412.47
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=583)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `116.1` → IC=-0.384 (n=359)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 116.1
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=1079)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `140.8` → IC=-0.313 (n=641)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 140.8
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=1924)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `156.92` → IC=-0.351 (n=631)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 156.92
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=1284)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.7` → IC=+0.191 (n=5962)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.7 (IC base=+0.096)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.172 (n=1699)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.01 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `2376.0723` → IC=+0.173 (n=1635)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2376.0723 (IC base=+0.096)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.148 (n=3586)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 18.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.159 (n=4893)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 7.0 (IC base=+0.143)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.259 (n=3764)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.190 (n=3176)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.02 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `1912.2134` → IC=+0.182 (n=2663)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 1912.2134 (IC base=+0.143)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.221 (n=705)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.207)

- **PATRÓN** `py_entrada` > `0.785` → IC=+0.389 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.785 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.209 (n=872)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.196 (n=630)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 7.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.201 (n=706)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` < `0.365` → IC=+0.261 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.365 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.192 (n=903)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.01 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `12917.1974` → IC=+0.236 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12917.1974 (IC base=+0.191)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.130 (n=568)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.115)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.130 (n=487)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 15.0 (IC base=+0.115)

- **PATRÓN** `py_entrada` > `0.555` → IC=+0.132 (n=563)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` > 0.555 (IC base=+0.115)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=262)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `4886.5239` → IC=+0.157 (n=208)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 4886.5239 (IC base=+0.115)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.191 (n=192)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 7.0 (IC base=+0.131)

- **PATRÓN** `py_entrada` < `0.415` → IC=+0.171 (n=314)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` < 0.415 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `4140.4788` → IC=+0.149 (n=297)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 4140.4788 (IC base=+0.131)

### FAVORITO_CONFIRMADO#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.136 (n=1323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.129 (n=1124)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 15.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` > `0.69` → IC=+0.317 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.277 (n=460)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.275)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.279 (n=523)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.275)

- **PATRÓN** `py_entrada` < `0.195` → IC=+0.410 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.195 (IC base=+0.275)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.277 (n=532)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.275)

- **PATRÓN** `libro_liquidez` > `2840.5007` → IC=+0.282 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2840.5007 (IC base=+0.275)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.136 (n=341)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.150 (n=292)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 15.0 (IC base=+0.134)

- **PATRÓN** `py_entrada` > `0.655` → IC=+0.256 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.655 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.145 (n=401)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.02 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `1913.3154` → IC=+0.156 (n=329)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 1913.3154 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `4420.281` → IC=+0.157 (n=141)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 4420.281 (IC base=+0.080)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.218 (n=335)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.189 (n=692)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 12.0 (IC base=+0.188)

- **PATRÓN** `py_entrada` > `0.84` → IC=+0.445 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.84 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.241 (n=245)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` < `0.205` → IC=+0.355 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.205 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.223 (n=622)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `1967.759` → IC=+0.226 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1967.759 (IC base=+0.218)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.222 (n=95)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.337 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.183)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.230 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.183)

- **PATRÓN** `py_entrada` < `0.415` → IC=+0.153 (n=436)

  - _Acción_: Kelly boost +0.76€ cuando `py_entrada` < 0.415 (IC base=+0.106)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.149 (n=277)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.02 (IC base=+0.106)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `9.0` → IC=-0.286 (n=82)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=90)

- **FILTRO** `py_entrada` > `0.835` → IC=-0.364 (n=42)

  - _Acción_: SKIP cuando `py_entrada` > 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=130)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.195 (n=4910)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.191 (n=4194)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.188)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.201 (n=2338)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.188)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.170 (n=855)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 11.0 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.176 (n=1213)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 17.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` < `0.72` → IC=+0.177 (n=1069)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.72 (IC base=+0.168)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.222 (n=70)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.212 (n=71)

- **FILTRO** `libro_liquidez` < `8205.705` → IC=-0.354 (n=46)

  - _Acción_: SKIP cuando `libro_liquidez` < 8205.705
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=47)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.420 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.324)

- **PATRÓN** `py_entrada` > `0.845` → IC=+0.372 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.845 (IC base=+0.324)

- **PATRÓN** `libro_liquidez` > `2916.5858` → IC=+0.343 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2916.5858 (IC base=+0.324)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.170 (n=1251)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 5.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.171 (n=1057)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 15.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.169 (n=1192)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` < 0.73 (IC base=+0.167)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.175 (n=829)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` > 0.72 (IC base=+0.167)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.244 (n=1120)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.232)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.320 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.232)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.195 (n=1203)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.182 (n=1035)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 15.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` < `0.72` → IC=+0.192 (n=1026)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.72 (IC base=+0.182)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.458 (n=234)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.449)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.447 (n=226)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.449)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.455 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.449)

- **PATRÓN** `libro_liquidez` > `3351.8902` → IC=+0.464 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3351.8902 (IC base=+0.449)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.449 (n=95)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.445)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.443 (n=85)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.445)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.447 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.445)

- **PATRÓN** `libro_liquidez` > `10024.8272` → IC=+0.469 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10024.8272 (IC base=+0.445)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.456 (n=88)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.438 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.939` → IC=+0.439 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.939 (IC base=+0.436)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.434 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.436)

- **PATRÓN** `libro_liquidez` > `3697.0572` → IC=+0.478 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3697.0572 (IC base=+0.436)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.443 (n=51)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.449)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.452 (n=60)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.449)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.452 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.449)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.443 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.449)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.196 (n=12485)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 8.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.219 (n=10110)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.191)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=2644)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.132 (n=1817)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 12.0 (IC base=+0.131)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.160 (n=1722)

  - _Acción_: Kelly boost +0.80€ cuando `py_entrada` > 0.72 (IC base=+0.131)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.241 (n=2287)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.233)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.271 (n=1607)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.233)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.186 (n=929)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.212 (n=812)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.168)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.233 (n=1990)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.227)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.289 (n=774)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.227)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.217 (n=2059)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.211)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.249 (n=1036)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.211)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.195 (n=784)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 18.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.189 (n=1674)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 12.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.229 (n=839)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.183)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.207 (n=1840)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.133)

- **PATRÓN** `restante_min` < `3.97` → IC=+0.134 (n=1705)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` < 3.97 (IC base=+0.133)

- **PATRÓN** `restante_min` > `4.93` → IC=+0.158 (n=1820)

  - _Acción_: Kelly boost +0.79€ cuando `restante_min` > 4.93 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.151 (n=2268)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 7.0 (IC base=+0.133)

- **PATRÓN** `lag_apertura_s` < `4.23` → IC=+0.159 (n=1706)

  - _Acción_: Kelly boost +0.80€ cuando `lag_apertura_s` < 4.23 (IC base=+0.133)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.211 (n=931)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.139)

- **PATRÓN** `restante_min` > `4.88` → IC=+0.154 (n=1170)

  - _Acción_: Kelly boost +0.77€ cuando `restante_min` > 4.88 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.167 (n=1120)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 7.0 (IC base=+0.139)

- **PATRÓN** `lag_apertura_s` < `7.05` → IC=+0.158 (n=1117)

  - _Acción_: Kelly boost +0.79€ cuando `lag_apertura_s` < 7.05 (IC base=+0.139)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.203 (n=909)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.128)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.166 (n=952)

  - _Acción_: Kelly boost +0.83€ cuando `restante_min` > 4.94 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.129 (n=2663)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 5.0 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.137 (n=1148)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 7.0 (IC base=+0.128)

- **PATRÓN** `lag_apertura_s` < `3.38` → IC=+0.172 (n=854)

  - _Acción_: Kelly boost +0.86€ cuando `lag_apertura_s` < 3.38 (IC base=+0.128)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.316 (n=439)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.296)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.300 (n=637)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.296)

- **PATRÓN** `py_entrada` > `0.825` → IC=+0.377 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.825 (IC base=+0.296)

- **PATRÓN** `libro_liquidez` > `2018.4208` → IC=+0.298 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2018.4208 (IC base=+0.296)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.296 (n=278)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.282)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.282 (n=241)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.282)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.354 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.282)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.286 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `5679.4122` → IC=+0.322 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5679.4122 (IC base=+0.282)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.328 (n=202)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.297)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.307 (n=293)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.297)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.368 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.297)

- **PATRÓN** `libro_liquidez` > `1758.8746` → IC=+0.310 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1758.8746 (IC base=+0.297)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `12.0` → IC=+0.337 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.339)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.346 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.339)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.371 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.339)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.355 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.339)

- **PATRÓN** `libro_liquidez` > `761.0655` → IC=+0.364 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 761.0655 (IC base=+0.339)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.428 (n=275)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.415)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.421 (n=265)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.415)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.422 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.415)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.425 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.415)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.416 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.415)

- **PATRÓN** `libro_liquidez` > `2076.1143` → IC=+0.428 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2076.1143 (IC base=+0.415)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.424 (n=117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.411)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.425 (n=118)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.411)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.415 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.411)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.419 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.411)

- **PATRÓN** `libro_liquidez` > `5536.1709` → IC=+0.451 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5536.1709 (IC base=+0.411)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.430 (n=112)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.420)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.438 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.420)

- **PATRÓN** `py_entrada` > `0.91` → IC=+0.423 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.91 (IC base=+0.420)

- **PATRÓN** `libro_liquidez` > `2076.1143` → IC=+0.452 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2076.1143 (IC base=+0.420)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.307 (n=319)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.283)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.436 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.283)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.299 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.283)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.307 (n=319)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.283)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.436 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.283)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.299 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.283)

### GBM_LATE_15M
- **PATRÓN** `ibs_20min` > `0.9497` → IC=+0.207 (n=855)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9497 (IC base=+0.065)

- **PATRÓN** `dist_vwap_pct` > `0.2046` → IC=+0.229 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2046 (IC base=+0.065)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.268` → IC=+0.157 (n=1016)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 5.268 (IC base=+0.065)

- **PATRÓN** `volumen_regimen` < `0.6297` → IC=+0.212 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6297 (IC base=+0.065)

- **PATRÓN** `volumen_regimen` > `1.0648` → IC=+0.235 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0648 (IC base=+0.065)

- **PATRÓN** `volumen_pendiente_norm` > `0.1707` → IC=+0.153 (n=407)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.1707 (IC base=+0.065)

- **PATRÓN** `volumen_spike_ratio` < `2.4189` → IC=+0.152 (n=1244)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4189 (IC base=+0.065)

- **PATRÓN** `ibs_20min` < `0.1168` → IC=+0.151 (n=1306)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.1168 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` < `0.3136` → IC=+0.143 (n=913)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.3136 (IC base=+0.030)

- **PATRÓN** `volumen_regimen` < `0.6186` → IC=+0.160 (n=286)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.6186 (IC base=+0.030)

- **PATRÓN** `volumen_regimen` > `1.0461` → IC=+0.141 (n=388)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 1.0461 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.3079` → IC=+0.271 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3079 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` > `2.924` → IC=+0.234 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.924 (IC base=+0.030)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.231 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.030)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.179 (n=260)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0071 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.184 (n=213)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 6.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.289 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.02` → IC=+0.321 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.02 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.2159` → IC=+0.170 (n=95)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2159 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.166 (n=387)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.04 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.151 (n=193)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 50.0 (IC base=+0.133)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.256 (n=227)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.252)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.271 (n=304)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.252)

- **PATRÓN** `drift_60min` |x|≤ `0.0752` → IC=+0.319 (n=114)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0752 (IC base=+0.252)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.253 (n=322)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.252)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.258 (n=349)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.252)

- **PATRÓN** `ibs_20min` < `0.4194` → IC=+0.291 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4194 (IC base=+0.252)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.972` → IC=+0.279 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.972 (IC base=+0.252)

- **PATRÓN** `volumen_pendiente_norm` > `0.3058` → IC=+0.316 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3058 (IC base=+0.252)

- **PATRÓN** `volumen_spike_ratio` < `1.88` → IC=+0.253 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.88 (IC base=+0.252)

- **PATRÓN** `volumen_spike_ratio` > `2.8125` → IC=+0.325 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8125 (IC base=+0.252)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.289 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.252)

- **PATRÓN** `libro_liquidez` > `1945.1048` → IC=+0.293 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1945.1048 (IC base=+0.252)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.241 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.252)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.231 (n=191)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.0936` → IC=+0.235 (n=145)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0936 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=436)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` > `0.4047` → IC=+0.224 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4047 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `0.2252` → IC=+0.230 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2252 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.354` → IC=+0.224 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.354 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` < `0.6912` → IC=+0.215 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6912 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` > `1.0803` → IC=+0.234 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0803 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` < `0.0959` → IC=+0.206 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0959 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.2681` → IC=+0.207 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2681 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` < `1.4558` → IC=+0.253 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4558 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `11706.7568` → IC=+0.215 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11706.7568 (IC base=+0.203)

- **PATRÓN** `sigma_h` < `0.0023` → IC=+0.153 (n=168)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0023 (IC base=+0.144)

- **PATRÓN** `sigma_h` > `0.0036` → IC=+0.147 (n=335)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` > 0.0036 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.0766` → IC=+0.157 (n=167)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.0766 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.152 (n=466)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 7.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.154 (n=530)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 18.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.6121` → IC=+0.171 (n=500)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.6121 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` < `0.1378` → IC=+0.168 (n=438)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.1378 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.938` → IC=+0.231 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.938 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `0.6207` → IC=+0.188 (n=168)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.6207 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.0711` → IC=+0.200 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0711 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `1.7548` → IC=+0.173 (n=264)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.7548 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.4105` → IC=+0.166 (n=396)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.4105 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=647)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `14054.4357` → IC=+0.199 (n=227)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 14054.4357 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `217.0` → IC=+0.170 (n=104)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 217.0 (IC base=+0.144)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.208 (n=234)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0077 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.225 (n=191)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.271 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.932` → IC=+0.273 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.932 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` < `0.1358` → IC=+0.142 (n=414)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` < 0.1358 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.4117` → IC=+0.135 (n=61)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.4117 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.5365` → IC=+0.144 (n=290)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.5365 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.6798` → IC=+0.145 (n=435)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.6798 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.176 (n=477)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.04 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.181 (n=202)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 45.0 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0096` → IC=+0.263 (n=399)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0096 (IC base=+0.249)

- **PATRÓN** `drift_60min` |x|≤ `0.4596` → IC=+0.258 (n=399)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4596 (IC base=+0.249)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.249 (n=273)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.249)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.264 (n=413)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.249)

- **PATRÓN** `ibs_20min` < `0.5208` → IC=+0.288 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5208 (IC base=+0.249)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.037` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.037 (IC base=+0.249)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.624` → IC=+0.254 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.624 (IC base=+0.249)

- **PATRÓN** `volumen_pendiente_norm` > `0.3846` → IC=+0.407 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3846 (IC base=+0.249)

- **PATRÓN** `volumen_spike_ratio` > `2.5543` → IC=+0.253 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5543 (IC base=+0.249)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.276 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.249)

- **PATRÓN** `libro_liquidez` > `1889.461` → IC=+0.248 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1889.461 (IC base=+0.249)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.230 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 51.0 (IC base=+0.249)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.175 (n=118)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=392)

- **FILTRO** `ibs_20min` < `0.2829` → IC=-0.141 (n=168)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2829
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=342)

- **FILTRO** `ibs_20min` > `0.864` → IC=-0.177 (n=224)

  - _Acción_: SKIP cuando `ibs_20min` > 0.864
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=673)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.172 (n=65)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=832)

- **PATRÓN** `dist_vwap_pct` > `0.124` → IC=+0.300 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.124 (IC base=-0.047)

- **PATRÓN** `volumen_regimen` < `0.6297` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6297 (IC base=-0.047)

- **PATRÓN** `volumen_regimen` > `0.7026` → IC=+0.267 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7026 (IC base=-0.047)

- **PATRÓN** `volumen_pendiente_norm` < `0.114` → IC=+0.235 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.114 (IC base=-0.047)

- **PATRÓN** `volumen_pendiente_norm` > `0.2199` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2199 (IC base=-0.047)

- **PATRÓN** `volumen_spike_ratio` < `1.4292` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4292 (IC base=-0.047)

- **PATRÓN** `volumen_spike_ratio` > `1.8068` → IC=+0.242 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8068 (IC base=-0.047)

- **PATRÓN** `ballena_activa_n` < `111.0` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 111.0 (IC base=-0.047)

- **PATRÓN** `dist_vwap_pct` > `0.1556` → IC=+0.167 (n=34)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1556 (IC base=-0.050)

- **PATRÓN** `volumen_pendiente_norm` > `0.0742` → IC=+0.197 (n=31)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.0742 (IC base=-0.050)

- **PATRÓN** `volumen_spike_ratio` > `1.5315` → IC=+0.143 (n=96)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.5315 (IC base=-0.050)

- **PATRÓN** `ballena_activa_n` < `141.0` → IC=+0.137 (n=89)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 141.0 (IC base=-0.050)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.136 (n=31)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.092 (n=101)

- **FILTRO** `ibs_20min` > `0.5` → IC=-0.137 (n=682)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=726)

- **FILTRO** `sigma_ewma_delta_pct` > `5.018` → IC=-0.154 (n=299)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.018
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=1109)

- **FILTRO** `volumen_pendiente_norm` < `0.0964` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.0964
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

- **FILTRO** `volumen_spike_ratio` > `1.6234` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.6234
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.167 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0056 (IC base=+0.037)

- **PATRÓN** `drift_60min` |x|≤ `0.1248` → IC=+0.167 (n=34)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1248 (IC base=+0.037)

- **PATRÓN** `ibs_20min` > `0.6842` → IC=+0.223 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6842 (IC base=+0.037)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.5333` → IC=-0.160 (n=254)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.5333
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=496)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=175)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=575)

- **FILTRO** `ibs_20min` > `0.7917` → IC=-0.179 (n=316)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7917
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=949)

- **FILTRO** `sigma_ewma_delta_pct` > `6.749` → IC=-0.154 (n=206)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.749
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=1059)

- **PATRÓN** `dist_vwap_pct` < `0.2396` → IC=+0.175 (n=38)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.2396 (IC base=-0.109)

- **PATRÓN** `volumen_regimen` > `0.6932` → IC=+0.183 (n=39)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 0.6932 (IC base=-0.109)

- **PATRÓN** `dist_vwap_pct` < `0.2072` → IC=+0.227 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2072 (IC base=-0.046)

- **PATRÓN** `volumen_regimen` < `0.6966` → IC=+0.230 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6966 (IC base=-0.046)

- **PATRÓN** `volumen_regimen` > `1.1383` → IC=+0.254 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1383 (IC base=-0.046)

- **PATRÓN** `volumen_pendiente_norm` > `0.0858` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0858 (IC base=-0.046)

- **PATRÓN** `volumen_spike_ratio` > `1.6969` → IC=+0.197 (n=31)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.6969 (IC base=-0.046)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.136 (n=1464)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` > 0.0078 (IC base=+0.055)

- **PATRÓN** `ibs_20min` > `0.2752` → IC=+0.120 (n=3225)

  - _Acción_: Kelly boost +0.60€ cuando `ibs_20min` > 0.2752 (IC base=+0.055)

- **PATRÓN** `dist_vwap_pct` > `1.2866` → IC=+0.290 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2866 (IC base=+0.055)

- **PATRÓN** `volumen_regimen` > `1.1649` → IC=+0.213 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1649 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` < `0.1146` → IC=+0.182 (n=1452)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` < 0.1146 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` > `0.249` → IC=+0.202 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.249 (IC base=+0.055)

- **PATRÓN** `volumen_spike_ratio` < `1.4789` → IC=+0.207 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4789 (IC base=+0.055)

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.278 (n=940)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 94.0 (IC base=+0.055)

- **PATRÓN** `ibs_20min` < `0.0909` → IC=+0.194 (n=1307)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.0909 (IC base=+0.040)

- **PATRÓN** `dist_vwap_pct` > `0.8039` → IC=+0.223 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8039 (IC base=+0.040)

- **PATRÓN** `dist_vwap_pct` < `0.2222` → IC=+0.215 (n=816)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2222 (IC base=+0.040)

- **PATRÓN** `volumen_regimen` < `0.8607` → IC=+0.215 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8607 (IC base=+0.040)

- **PATRÓN** `volumen_regimen` > `1.2256` → IC=+0.230 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2256 (IC base=+0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.2573` → IC=+0.347 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2573 (IC base=+0.040)

- **PATRÓN** `volumen_spike_ratio` > `2.8751` → IC=+0.291 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8751 (IC base=+0.040)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.266 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 59.0 (IC base=+0.040)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2469` → IC=-0.157 (n=231)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2469
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=469)

- **FILTRO** `sigma_ewma_delta_pct` > `2.143` → IC=-0.172 (n=248)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.143
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=564)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.451` → IC=+0.167 (n=130)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 5.451 (IC base=+0.000)

- **PATRÓN** `volumen_pendiente_norm` > `0.211` → IC=+0.342 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.211 (IC base=+0.000)

- **PATRÓN** `volumen_spike_ratio` > `2.7084` → IC=+0.242 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7084 (IC base=+0.000)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.397 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.000)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` > `0.8836` → IC=-0.151 (n=296)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8836
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=892)

- **PATRÓN** `volumen_regimen` < `0.5591` → IC=+0.219 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5591 (IC base=-0.043)

- **PATRÓN** `volumen_spike_ratio` < `1.6955` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6955 (IC base=-0.043)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.286 (n=171)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.196)

- **PATRÓN** `drift_60min` |x|≤ `0.0791` → IC=+0.217 (n=171)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0791 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.263 (n=188)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.196)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.289 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.142` → IC=+0.301 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.142 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` < `0.1415` → IC=+0.207 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1415 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` < `2.5143` → IC=+0.205 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5143 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` > `4.1507` → IC=+0.203 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 4.1507 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.222 (n=477)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `1932.8384` → IC=+0.205 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1932.8384 (IC base=+0.196)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.241 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 42.0 (IC base=+0.196)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.332 (n=266)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.324)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.323 (n=201)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.324)

- **PATRÓN** `drift_60min` |x|≤ `0.2495` → IC=+0.333 (n=201)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2495 (IC base=+0.324)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.348 (n=202)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.324)

- **PATRÓN** `ibs_20min` < `0.3333` → IC=+0.342 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3333 (IC base=+0.324)

- **PATRÓN** `ibs_20min` > `0.1265` → IC=+0.328 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1265 (IC base=+0.324)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.607` → IC=+0.334 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.607 (IC base=+0.324)

- **PATRÓN** `volumen_pendiente_norm` < `0.2265` → IC=+0.317 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2265 (IC base=+0.324)

- **PATRÓN** `volumen_pendiente_norm` > `0.3546` → IC=+0.365 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3546 (IC base=+0.324)

- **PATRÓN** `volumen_spike_ratio` < `1.6966` → IC=+0.319 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6966 (IC base=+0.324)

- **PATRÓN** `volumen_spike_ratio` > `2.433` → IC=+0.337 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.433 (IC base=+0.324)

- **PATRÓN** `libro_liquidez` > `1868.3264` → IC=+0.374 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1868.3264 (IC base=+0.324)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.357 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 29.0 (IC base=+0.324)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `sigma_h` > `0.0066` → IC=-0.148 (n=126)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0066
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=382)

- **FILTRO** `hora_utc` < `7.0` → IC=-0.174 (n=127)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=381)

- **FILTRO** `dist_vwap_pct` < `0.2815` → IC=-0.237 (n=36)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.2815
  - _Potencial_: sin este filtro IC_bueno=+0.176 (n=35)

- **FILTRO** `volumen_regimen` > `1.0041` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.0041
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=54)

- **FILTRO** `ibs_20min` > `0.7377` → IC=-0.128 (n=353)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7377
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=688)

- **FILTRO** `dist_vwap_pct` < `0.0964` → IC=-0.136 (n=53)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0964
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

- **FILTRO** `volumen_regimen` > `0.8819` → IC=-0.231 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8819
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=49)

- **FILTRO** `volumen_regimen` < `0.6828` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.6828
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=49)

- **FILTRO** `volumen_pendiente_norm` < `0.1167` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.1167
  - _Potencial_: sin este filtro IC_bueno=+0.214 (n=5)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.176 (n=69)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=972)

- **PATRÓN** `dist_vwap_pct` > `0.7343` → IC=+0.233 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7343 (IC base=-0.082)

- **PATRÓN** `volumen_spike_ratio` < `1.4` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4 (IC base=-0.082)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7468` → IC=-0.136 (n=473)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7468
  - _Potencial_: sin este filtro IC_bueno=+0.220 (n=244)

- **FILTRO** `ibs_20min` > `0.7551` → IC=-0.201 (n=232)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7551
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=698)

- **FILTRO** `dist_vwap_pct` > `0.1326` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1326
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=55)

- **FILTRO** `volumen_regimen` > `1.3339` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.3339
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=54)

- **FILTRO** `volumen_spike_ratio` > `1.334` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.334
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **FILTRO** `volumen_spike_ratio` < `2.3381` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 2.3381
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=12)

- **FILTRO** `ballena_activa_n` > `35.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `ballena_activa_n` > 35.0
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

- **PATRÓN** `ibs_20min` > `0.8592` → IC=+0.275 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8592 (IC base=-0.015)

- **PATRÓN** `dist_vwap_pct` > `0.3308` → IC=+0.275 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3308 (IC base=-0.015)

- **PATRÓN** `volumen_regimen` < `0.8566` → IC=+0.191 (n=137)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.8566 (IC base=-0.015)

- **PATRÓN** `volumen_regimen` > `1.1426` → IC=+0.243 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1426 (IC base=-0.015)

- **PATRÓN** `volumen_pendiente_norm` < `0.1127` → IC=+0.189 (n=191)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.1127 (IC base=-0.015)

- **PATRÓN** `volumen_pendiente_norm` > `0.2642` → IC=+0.267 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2642 (IC base=-0.015)

- **PATRÓN** `volumen_spike_ratio` < `1.4536` → IC=+0.231 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4536 (IC base=-0.015)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.250 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 50.0 (IC base=-0.015)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0201` → IC=+0.318 (n=278)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0201 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.238 (n=235)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.227)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.233 (n=294)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.8915` → IC=+0.310 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8915 (IC base=+0.227)

- **PATRÓN** `dist_vwap_pct` > `1.4218` → IC=+0.344 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.4218 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.223` → IC=+0.277 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.223 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` > `0.8361` → IC=+0.263 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8361 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` < `0.0813` → IC=+0.231 (n=522)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0813 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.2842` → IC=+0.256 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2842 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `1.4264` → IC=+0.254 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4264 (IC base=+0.227)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.235 (n=618)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `3042.758` → IC=+0.252 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3042.758 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.279 (n=211)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.274)

- **PATRÓN** `sigma_h` > `0.0237` → IC=+0.279 (n=211)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0237 (IC base=+0.274)

- **PATRÓN** `drift_60min` |x|≤ `0.2897` → IC=+0.278 (n=422)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2897 (IC base=+0.274)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.281 (n=591)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.274)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.277 (n=218)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.274)

- **PATRÓN** `ibs_20min` < `0.2788` → IC=+0.330 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2788 (IC base=+0.274)

- **PATRÓN** `dist_vwap_pct` < `0.2715` → IC=+0.285 (n=616)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2715 (IC base=+0.274)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.954` → IC=+0.324 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.954 (IC base=+0.274)

- **PATRÓN** `volumen_regimen` < `0.8883` → IC=+0.274 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8883 (IC base=+0.274)

- **PATRÓN** `volumen_regimen` > `1.2535` → IC=+0.307 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2535 (IC base=+0.274)

- **PATRÓN** `volumen_pendiente_norm` > `0.2904` → IC=+0.386 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2904 (IC base=+0.274)

- **PATRÓN** `volumen_spike_ratio` > `2.1671` → IC=+0.290 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1671 (IC base=+0.274)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.191 (n=918)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0103 (IC base=+0.158)

- **PATRÓN** `drift_60min` |x|≤ `0.3367` → IC=+0.161 (n=2425)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.3367 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=2893)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.158)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.283 (n=1347)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` > `0.8227` → IC=+0.251 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8227 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.414` → IC=+0.244 (n=1142)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.414 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` > `0.6873` → IC=+0.174 (n=1702)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 0.6873 (IC base=+0.158)

- **PATRÓN** `volumen_pendiente_norm` > `0.2391` → IC=+0.191 (n=519)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2391 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` < `2.2904` → IC=+0.159 (n=2200)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.2904 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` > `1.8582` → IC=+0.152 (n=1666)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.8582 (IC base=+0.158)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.166 (n=2190)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.158)

- **PATRÓN** `libro_liquidez` > `3194.7571` → IC=+0.181 (n=1249)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 3194.7571 (IC base=+0.158)

- **PATRÓN** `ballena_activa_n` < `107.0` → IC=+0.179 (n=1467)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 107.0 (IC base=+0.158)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.197 (n=1692)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0061 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.0806` → IC=+0.210 (n=842)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0806 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.203 (n=1175)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.183 (n=968)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 5.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` < `0.4107` → IC=+0.239 (n=2524)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4107 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.907` → IC=+0.216 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.907 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `1.1669` → IC=+0.168 (n=1987)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.1669 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` > `0.6199` → IC=+0.169 (n=1986)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 0.6199 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.2919` → IC=+0.252 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2919 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` < `1.5767` → IC=+0.177 (n=840)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.5767 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `2.6688` → IC=+0.207 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6688 (IC base=+0.183)

- **PATRÓN** `ballena_activa_n` < `117.0` → IC=+0.189 (n=1305)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 117.0 (IC base=+0.183)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.209 (n=204)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.2695` → IC=+0.162 (n=451)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.2695 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.210 (n=174)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.305 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.127` → IC=+0.329 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.127 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.2094` → IC=+0.216 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2094 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `1.4427` → IC=+0.141 (n=371)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.4427 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.181 (n=315)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.04 (IC base=+0.154)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.267 (n=247)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.249)

- **PATRÓN** `drift_60min` |x|≤ `0.2611` → IC=+0.286 (n=218)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2611 (IC base=+0.249)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.270 (n=224)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.249)

- **PATRÓN** `ibs_20min` < `0.323` → IC=+0.282 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.323 (IC base=+0.249)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.358` → IC=+0.268 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.358 (IC base=+0.249)

- **PATRÓN** `volumen_pendiente_norm` > `0.1762` → IC=+0.274 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1762 (IC base=+0.249)

- **PATRÓN** `volumen_spike_ratio` < `1.9491` → IC=+0.274 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9491 (IC base=+0.249)

- **PATRÓN** `volumen_spike_ratio` > `2.8103` → IC=+0.278 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8103 (IC base=+0.249)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.300 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.249)

- **PATRÓN** `libro_liquidez` > `1936.1048` → IC=+0.312 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1936.1048 (IC base=+0.249)

- **PATRÓN** `ballena_activa_n` < `80.0` → IC=+0.231 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 80.0 (IC base=+0.249)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.194 (n=348)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0062 (IC base=+0.172)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.181 (n=133)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0072 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.4268` → IC=+0.180 (n=395)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.4268 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.199 (n=397)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` > `0.489` → IC=+0.213 (n=395)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.489 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.211` → IC=+0.232 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.211 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.58` → IC=+0.244 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.58 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` < `0.6383` → IC=+0.187 (n=132)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.6383 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` > `1.067` → IC=+0.196 (n=179)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` > 1.067 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.2218` → IC=+0.237 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2218 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` < `1.3655` → IC=+0.242 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3655 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `12757.5102` → IC=+0.191 (n=263)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 12757.5102 (IC base=+0.172)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.171 (n=500)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0059 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.2331` → IC=+0.176 (n=439)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2331 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.172 (n=456)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 7.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` < `0.4297` → IC=+0.197 (n=499)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.4297 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` < `0.1613` → IC=+0.177 (n=499)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1613 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.387` → IC=+0.241 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.387 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `0.6986` → IC=+0.212 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6986 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.1663` → IC=+0.231 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1663 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `2.5679` → IC=+0.167 (n=391)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.5679 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `14953.202` → IC=+0.191 (n=166)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 14953.202 (IC base=+0.152)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.248 (n=133)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.165)

- **PATRÓN** `drift_60min` |x|≤ `0.155` → IC=+0.180 (n=267)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.155 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.191 (n=137)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 17.0 (IC base=+0.165)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.210 (n=136)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.96` → IC=+0.296 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.96 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` < `0.2288` → IC=+0.160 (n=342)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` < 0.2288 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` < `1.9664` → IC=+0.197 (n=150)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.9664 (IC base=+0.165)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.191 (n=360)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.04 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `1943.8205` → IC=+0.181 (n=133)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 1943.8205 (IC base=+0.165)

- **PATRÓN** `sigma_h` < `0.0101` → IC=+0.276 (n=292)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0101 (IC base=+0.254)

- **PATRÓN** `drift_60min` |x|≤ `0.227` → IC=+0.292 (n=195)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.227 (IC base=+0.254)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.282 (n=200)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.254)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.255 (n=296)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.254)

- **PATRÓN** `ibs_20min` < `0.3` → IC=+0.311 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3 (IC base=+0.254)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.131` → IC=+0.353 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.131 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` > `0.3645` → IC=+0.395 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3645 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` > `3.1185` → IC=+0.292 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.1185 (IC base=+0.254)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.009` → IC=+0.208 (n=396)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.009 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.4992` → IC=+0.188 (n=396)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.4992 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.193 (n=405)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 6.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `0.435` → IC=+0.229 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.435 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.9762` → IC=+0.232 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9762 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.407` → IC=+0.323 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.407 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` > `1.2318` → IC=+0.224 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2318 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.1008` → IC=+0.213 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1008 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` < `1.435` → IC=+0.177 (n=128)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.435 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.5007` → IC=+0.231 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5007 (IC base=+0.173)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.172 (n=453)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.01 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `12282.2056` → IC=+0.224 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12282.2056 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `111.0` → IC=+0.178 (n=147)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 111.0 (IC base=+0.173)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.233 (n=159)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.3806` → IC=+0.158 (n=477)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.3806 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.161 (n=322)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 11.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.154 (n=183)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 5.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` < `0.3669` → IC=+0.211 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3669 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.526` → IC=+0.194 (n=109)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 12.526 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `1.1652` → IC=+0.151 (n=477)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1652 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` > `0.5948` → IC=+0.151 (n=477)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.5948 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.1026` → IC=+0.160 (n=148)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.1026 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `1.9099` → IC=+0.179 (n=247)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.9099 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `2.554` → IC=+0.148 (n=123)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 2.554 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `10944.7908` → IC=+0.158 (n=159)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 10944.7908 (IC base=+0.141)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.173 (n=362)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0083 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.141 (n=566)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `0.5556` → IC=+0.183 (n=543)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.5556 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` > `0.9146` → IC=+0.271 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9146 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.191` → IC=+0.287 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.191 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` > `0.6193` → IC=+0.140 (n=543)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 0.6193 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` < `0.1612` → IC=+0.138 (n=534)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` < 0.1612 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `1.4397` → IC=+0.134 (n=170)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.4397 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` > `1.5512` → IC=+0.130 (n=455)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.5512 (IC base=+0.121)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.122 (n=427)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.01 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `3250.9802` → IC=+0.221 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3250.9802 (IC base=+0.121)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.160 (n=154)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.005 (IC base=+0.133)

- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.208 (n=152)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0106 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.203 (n=220)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.4098` → IC=+0.233 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4098 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` > `0.7528` → IC=+0.146 (n=94)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.7528 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.218` → IC=+0.196 (n=179)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 3.218 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `1.1373` → IC=+0.141 (n=455)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.1373 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` > `0.8419` → IC=+0.169 (n=303)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 0.8419 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.2176` → IC=+0.203 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2176 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `2.273` → IC=+0.218 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.273 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `2147.8152` → IC=+0.185 (n=303)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2147.8152 (IC base=+0.133)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0276` → IC=+0.194 (n=191)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.0276 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.1642` → IC=+0.197 (n=252)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.1642 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.202 (n=203)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `0.9053` → IC=+0.268 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9053 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `1.6023` → IC=+0.257 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.6023 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.369` → IC=+0.244 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.369 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` > `0.6073` → IC=+0.183 (n=573)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 0.6073 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.2403` → IC=+0.255 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2403 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `2.4913` → IC=+0.194 (n=534)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 2.4913 (IC base=+0.169)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.172 (n=684)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.02 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `2443.4743` → IC=+0.170 (n=573)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2443.4743 (IC base=+0.169)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.274 (n=246)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.6746` → IC=+0.230 (n=558)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6746 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.225 (n=274)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.257 (n=265)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` < `0.381` → IC=+0.261 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.381 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.225` → IC=+0.283 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.225 (IC base=+0.221)

- **PATRÓN** `volumen_regimen` > `0.6925` → IC=+0.244 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6925 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.349 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `2.7123` → IC=+0.259 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7123 (IC base=+0.221)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.144 (n=363)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.0059 (IC base=+0.109)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.192 (n=258)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 16.0 (IC base=+0.109)

- **PATRÓN** `ibs_20min` > `0.6176` → IC=+0.169 (n=487)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.6176 (IC base=+0.109)

- **PATRÓN** `dist_vwap_pct` > `0.8823` → IC=+0.264 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8823 (IC base=+0.109)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.157` → IC=+0.187 (n=148)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 8.157 (IC base=+0.109)

- **PATRÓN** `volumen_pendiente_norm` > `0.184` → IC=+0.171 (n=147)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.184 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `2574.8106` → IC=+0.135 (n=362)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2574.8106 (IC base=+0.109)

- **PATRÓN** `ibs_20min` < `0.3044` → IC=+0.133 (n=352)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.3044 (IC base=+0.056)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.789` → IC=+0.133 (n=115)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 7.789 (IC base=+0.056)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.147 (n=168)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 20.0 (IC base=+0.056)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.200 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.126 (n=89)

- **FILTRO** `ibs_20min` < `0.5377` → IC=-0.177 (n=29)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5377
  - _Potencial_: sin este filtro IC_bueno=+0.122 (n=88)

- **FILTRO** `libro_liquidez` < `8276.6888` → IC=-0.175 (n=38)

  - _Acción_: SKIP cuando `libro_liquidez` < 8276.6888
  - _Potencial_: sin este filtro IC_bueno=+0.154 (n=79)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.126 (n=89)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 9.0 (IC base=+0.046)

- **PATRÓN** `ibs_20min` > `0.5377` → IC=+0.122 (n=88)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` > 0.5377 (IC base=+0.046)

- **PATRÓN** `dist_vwap_pct` > `0.7932` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7932 (IC base=+0.046)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.167` → IC=+0.151 (n=41)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 4.167 (IC base=+0.046)

- **PATRÓN** `libro_liquidez` > `12103.1125` → IC=+0.156 (n=59)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 12103.1125 (IC base=+0.046)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.198 (n=61)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0026 (IC base=+0.084)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.131 (n=82)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` > 0.0052 (IC base=+0.084)

- **PATRÓN** `ibs_20min` < `0.7521` → IC=+0.139 (n=181)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.7521 (IC base=+0.084)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.82` → IC=+0.191 (n=53)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 6.82 (IC base=+0.084)

- **PATRÓN** `volumen_pendiente_norm` > `0.1481` → IC=+0.308 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1481 (IC base=+0.084)

- **PATRÓN** `ballena_activa_n` < `255.0` → IC=+0.137 (n=100)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 255.0 (IC base=+0.084)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **FILTRO** `drift_60min` |x|> `0.3354` → IC=-0.167 (n=25)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.3354
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `ibs_20min` > `0.6565` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6565
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=78)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.291 (n=89)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.294)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.329 (n=68)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.294)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.326 (n=90)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.294)

- **PATRÓN** `ibs_20min` > `0.8289` → IC=+0.329 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8289 (IC base=+0.294)

- **PATRÓN** `dist_vwap_pct` > `0.1466` → IC=+0.351 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1466 (IC base=+0.294)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.561` → IC=+0.377 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.561 (IC base=+0.294)

- **PATRÓN** `volumen_regimen` < `0.7015` → IC=+0.372 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7015 (IC base=+0.294)

- **PATRÓN** `volumen_regimen` > `1.0786` → IC=+0.312 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0786 (IC base=+0.294)

- **PATRÓN** `volumen_pendiente_norm` > `0.1782` → IC=+0.402 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1782 (IC base=+0.294)

- **PATRÓN** `volumen_spike_ratio` < `2.2928` → IC=+0.305 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2928 (IC base=+0.294)

- **PATRÓN** `volumen_spike_ratio` > `1.5284` → IC=+0.318 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5284 (IC base=+0.294)

- **PATRÓN** `libro_liquidez` > `2687.8872` → IC=+0.296 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2687.8872 (IC base=+0.294)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.293 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.005)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.159 (n=42)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 13.0 (IC base=+0.005)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` < `0.5556` → IC=-0.173 (n=50)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5556
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=152)

- **FILTRO** `hora_utc` < `4.0` → IC=-0.200 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=91)

- **FILTRO** `ibs_20min` > `0.4783` → IC=-0.238 (n=40)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4783
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=79)

- **FILTRO** `dist_vwap_pct` > `0.1977` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1977
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=99)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.161 (n=57)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.029)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.199 (n=71)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 1.0 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` > `0.4993` → IC=+0.179 (n=26)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.4993 (IC base=+0.029)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.100)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.141 (n=62)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` > 0.75 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.745` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.745 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` > `0.8105` → IC=+0.141 (n=62)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 0.8105 (IC base=+0.100)

- **PATRÓN** `volumen_pendiente_norm` > `0.2212` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2212 (IC base=+0.100)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.131 (n=63)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.100)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.210 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.100)

- **PATRÓN** `ibs_20min` < `0.0773` → IC=+0.233 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0773 (IC base=+0.077)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.184 (n=2144)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0065 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.173 (n=1238)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` > `0.9396` → IC=+0.290 (n=1457)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9396 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `1.1148` → IC=+0.243 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1148 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.527` → IC=+0.230 (n=1867)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.527 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `0.8767` → IC=+0.149 (n=1512)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.8767 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` > `1.0761` → IC=+0.151 (n=1028)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 1.0761 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.1644` → IC=+0.180 (n=835)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.1644 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `2.3086` → IC=+0.154 (n=2546)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.3086 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `1.8681` → IC=+0.162 (n=1929)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.8681 (IC base=+0.152)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.157 (n=2562)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `2475.2192` → IC=+0.176 (n=2142)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2475.2192 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `139.0` → IC=+0.192 (n=1617)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 139.0 (IC base=+0.152)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.213 (n=1993)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.4808` → IC=+0.196 (n=2989)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.4808 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.204 (n=1106)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` < `0.56` → IC=+0.243 (n=2989)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.56 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` < `0.4295` → IC=+0.180 (n=2222)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.4295 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.418` → IC=+0.207 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.418 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.657` → IC=+0.193 (n=2811)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 2.657 (IC base=+0.188)

- **PATRÓN** `volumen_regimen` < `0.619` → IC=+0.181 (n=735)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.619 (IC base=+0.188)

- **PATRÓN** `volumen_regimen` > `1.1954` → IC=+0.172 (n=736)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 1.1954 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.287` → IC=+0.269 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.287 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `2.3029` → IC=+0.205 (n=1037)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3029 (IC base=+0.188)

- **PATRÓN** `ballena_activa_n` < `169.0` → IC=+0.167 (n=1863)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 169.0 (IC base=+0.188)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` > `0.007` → IC=+0.224 (n=241)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.156 (n=251)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 15.0 (IC base=+0.156)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.180 (n=357)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 11.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.315 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.347` → IC=+0.308 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.347 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` > `0.2129` → IC=+0.239 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2129 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `1.5836` → IC=+0.131 (n=196)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.5836 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` > `1.9148` → IC=+0.154 (n=296)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.9148 (IC base=+0.156)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.206 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.156)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.272 (n=235)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0061 (IC base=+0.259)

- **PATRÓN** `sigma_h` > `0.0053` → IC=+0.262 (n=313)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0053 (IC base=+0.259)

- **PATRÓN** `drift_60min` |x|≤ `0.1054` → IC=+0.288 (n=154)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1054 (IC base=+0.259)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.264 (n=329)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.259)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.274 (n=308)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.259)

- **PATRÓN** `ibs_20min` < `0.5567` → IC=+0.295 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5567 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.116` → IC=+0.280 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.116 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` > `0.299` → IC=+0.325 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.299 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` > `2.8455` → IC=+0.312 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8455 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.281 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1953.254` → IC=+0.307 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1953.254 (IC base=+0.259)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.167 (n=172)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0029 (IC base=+0.155)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.178 (n=172)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.007 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.4174` → IC=+0.157 (n=514)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.4174 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.182 (n=460)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 8.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` > `0.3271` → IC=+0.209 (n=514)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3271 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.2647` → IC=+0.227 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2647 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.619` → IC=+0.206 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.619 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` < `0.709` → IC=+0.177 (n=227)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.709 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` > `1.088` → IC=+0.172 (n=233)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 1.088 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` < `0.0714` → IC=+0.173 (n=417)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` < 0.0714 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` > `0.2044` → IC=+0.186 (n=100)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2044 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `2.3977` → IC=+0.186 (n=466)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 2.3977 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `1.3655` → IC=+0.174 (n=465)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.3655 (IC base=+0.155)

- **PATRÓN** `libro_liquidez` > `12315.1254` → IC=+0.172 (n=343)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 12315.1254 (IC base=+0.155)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.171 (n=496)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0061 (IC base=+0.166)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.170 (n=225)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0049 (IC base=+0.166)

- **PATRÓN** `drift_60min` |x|≤ `0.2731` → IC=+0.180 (n=436)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.2731 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.172 (n=459)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 7.0 (IC base=+0.166)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.181 (n=515)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 18.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` < `0.569` → IC=+0.203 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.569 (IC base=+0.166)

- **PATRÓN** `dist_vwap_pct` < `0.1465` → IC=+0.181 (n=447)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.1465 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.78` → IC=+0.219 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.78 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` < `0.6208` → IC=+0.232 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6208 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` > `0.2167` → IC=+0.290 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2167 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` < `1.7531` → IC=+0.199 (n=267)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.7531 (IC base=+0.166)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.166 (n=642)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.166)

- **PATRÓN** `libro_liquidez` > `13358.8621` → IC=+0.183 (n=225)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 13358.8621 (IC base=+0.166)

- **PATRÓN** `ballena_activa_n` < `303.0` → IC=+0.176 (n=100)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 303.0 (IC base=+0.166)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.259 (n=193)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0078 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.255 (n=198)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` > `0.7044` → IC=+0.263 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7044 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.217` → IC=+0.350 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.217 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` < `0.222` → IC=+0.192 (n=358)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.222 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` < `1.9671` → IC=+0.199 (n=154)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.9671 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `4.2371` → IC=+0.172 (n=117)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 4.2371 (IC base=+0.186)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.216 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.186)

- **PATRÓN** `libro_liquidez` > `1828.491` → IC=+0.200 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1828.491 (IC base=+0.186)

- **PATRÓN** `ballena_activa_n` < `64.0` → IC=+0.241 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 64.0 (IC base=+0.186)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.304 (n=146)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.1283` → IC=+0.242 (n=192)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1283 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.285 (n=147)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.5472` → IC=+0.299 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5472 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.204` → IC=+0.265 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.204 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.3557` → IC=+0.284 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3557 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.7422` → IC=+0.248 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7422 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `2.3571` → IC=+0.206 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3571 (IC base=+0.238)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.267 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.238)

- **PATRÓN** `ballena_activa_n` < `65.0` → IC=+0.184 (n=229)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 65.0 (IC base=+0.238)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0088` → IC=+0.155 (n=517)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0088 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.1463` → IC=+0.143 (n=228)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.1463 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.167 (n=467)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 8.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` > `0.34` → IC=+0.197 (n=516)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.34 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `0.8449` → IC=+0.220 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8449 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.485` → IC=+0.191 (n=247)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 4.485 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `0.9021` → IC=+0.169 (n=345)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.9021 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` > `1.2073` → IC=+0.155 (n=172)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 1.2073 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.2693` → IC=+0.271 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2693 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `2.4777` → IC=+0.241 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4777 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `5099.5365` → IC=+0.223 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5099.5365 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `160.0` → IC=+0.179 (n=260)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 160.0 (IC base=+0.142)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.168 (n=396)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0075 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.4941` → IC=+0.162 (n=450)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.4941 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.177 (n=215)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 7.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` < `0.298` → IC=+0.215 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.298 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.1635` → IC=+0.154 (n=203)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.1635 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.454` → IC=+0.212 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.454 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.479` → IC=+0.146 (n=425)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 4.479 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.5827` → IC=+0.165 (n=150)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.5827 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` > `1.1367` → IC=+0.178 (n=150)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 1.1367 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.2392` → IC=+0.272 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2392 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `1.8319` → IC=+0.163 (n=262)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.8319 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `2.4896` → IC=+0.192 (n=131)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.4896 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `9816.3464` → IC=+0.194 (n=204)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 9816.3464 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `196.0` → IC=+0.178 (n=330)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 196.0 (IC base=+0.146)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.144 (n=259)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.0113 (IC base=+0.095)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.138 (n=390)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 12.0 (IC base=+0.095)

- **PATRÓN** `ibs_20min` > `0.4841` → IC=+0.180 (n=570)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.4841 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` > `0.9047` → IC=+0.230 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9047 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.554` → IC=+0.240 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.554 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `2992.2942` → IC=+0.266 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2992.2942 (IC base=+0.095)

- **PATRÓN** `ballena_activa_n` < `66.0` → IC=+0.158 (n=346)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 66.0 (IC base=+0.095)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.181 (n=180)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0056 (IC base=+0.113)

- **PATRÓN** `drift_60min` |x|≤ `0.1246` → IC=+0.158 (n=179)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1246 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.165 (n=252)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.5915` → IC=+0.197 (n=535)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.5915 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` < `0.4927` → IC=+0.136 (n=509)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.4927 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.062` → IC=+0.134 (n=525)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 3.062 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `0.7113` → IC=+0.147 (n=236)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.7113 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.0706` → IC=+0.158 (n=156)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.0706 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` < `2.108` → IC=+0.137 (n=340)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 2.108 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` > `1.443` → IC=+0.135 (n=387)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.443 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `2706.698` → IC=+0.165 (n=243)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2706.698 (IC base=+0.113)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0228` → IC=+0.211 (n=303)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0228 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=699)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.9583` → IC=+0.300 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9583 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `1.0241` → IC=+0.286 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0241 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.118` → IC=+0.248 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.118 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` > `1.0297` → IC=+0.215 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0297 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.1694` → IC=+0.247 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1694 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `1.4407` → IC=+0.185 (n=618)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.4407 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.186 (n=792)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.02 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `3057.3626` → IC=+0.184 (n=223)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 3057.3626 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.219 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.296 (n=243)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.6698` → IC=+0.225 (n=724)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6698 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.221 (n=672)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.223 (n=771)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` < `0.4964` → IC=+0.281 (n=724)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4964 (IC base=+0.219)

- **PATRÓN** `dist_vwap_pct` < `0.2557` → IC=+0.231 (n=690)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2557 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.648` → IC=+0.300 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.648 (IC base=+0.219)

- **PATRÓN** `volumen_regimen` > `1.2349` → IC=+0.242 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2349 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.2833` → IC=+0.320 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2833 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` > `2.2118` → IC=+0.229 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2118 (IC base=+0.219)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.189 (n=448)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 37.0 (IC base=+0.219)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.146 (n=1276)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.122 (n=791)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0112 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.160 (n=301)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 18.0 (IC base=+0.111)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.126 (n=423)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 5.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` > `0.9174` → IC=+0.172 (n=300)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.9174 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.223` → IC=+0.154 (n=134)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 10.223 (IC base=+0.111)

- **PATRÓN** `volumen_pendiente_norm` > `0.2444` → IC=+0.167 (n=163)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2444 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` < `1.4469` → IC=+0.157 (n=295)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.4469 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` > `2.6271` → IC=+0.143 (n=295)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.6271 (IC base=+0.111)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.196 (n=324)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0037 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.3784` → IC=+0.167 (n=853)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.3784 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.156 (n=373)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.193 (n=347)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 4.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` < `0.1951` → IC=+0.160 (n=427)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1951 (IC base=+0.142)

- **PATRÓN** `ibs_20min` > `0.093` → IC=+0.143 (n=969)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.093 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `0.1925` → IC=+0.153 (n=355)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.1925 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.061` → IC=+0.155 (n=969)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 6.061 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `1.2058` → IC=+0.152 (n=943)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.2058 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` < `0.1461` → IC=+0.149 (n=970)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` < 0.1461 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `2.5254` → IC=+0.159 (n=961)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.5254 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `1.4206` → IC=+0.150 (n=960)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.4206 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.146 (n=1276)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `10602.7113` → IC=+0.148 (n=646)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 10602.7113 (IC base=+0.142)

### GBM_LATE_5M#BTC#5min
- **FILTRO** `sigma_ewma_delta_pct` > `2.672` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.672
  - _Potencial_: sin este filtro IC_bueno=+0.114 (n=138)

- **FILTRO** `volumen_pendiente_norm` > `0.1007` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1007
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=143)

- **PATRÓN** `hora_utc` > `19.0` → IC=+0.198 (n=41)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 19.0 (IC base=+0.064)

- **PATRÓN** `volumen_spike_ratio` < `1.5333` → IC=+0.161 (n=54)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.5333 (IC base=+0.064)

- **PATRÓN** `libro_liquidez` > `12574.1361` → IC=+0.142 (n=121)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 12574.1361 (IC base=+0.064)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.201 (n=232)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0036 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.3891` → IC=+0.150 (n=527)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.3891 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.181 (n=202)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.180 (n=198)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.1703` → IC=+0.171 (n=232)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.1703 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.6795` → IC=+0.189 (n=59)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.6795 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.265` → IC=+0.159 (n=526)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` < 6.265 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `1.1834` → IC=+0.156 (n=527)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.1834 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.0692` → IC=+0.167 (n=247)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.0692 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.538` → IC=+0.153 (n=525)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.538 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.8045` → IC=+0.148 (n=350)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.8045 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `12015.9861` → IC=+0.147 (n=471)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 12015.9861 (IC base=+0.139)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.007` → IC=+0.162 (n=66)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.007 (IC base=+0.143)

- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.169 (n=131)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0088 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.4353` → IC=+0.146 (n=173)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.4353 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.235 (n=66)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` < `0.4648` → IC=+0.163 (n=87)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.4648 (IC base=+0.143)

- **PATRÓN** `ibs_20min` > `0.9524` → IC=+0.250 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9524 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.742` → IC=+0.281 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.742 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.328` → IC=+0.144 (n=172)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 3.328 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` < `0.0837` → IC=+0.146 (n=176)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` < 0.0837 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.3013` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.3013 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `1.7585` → IC=+0.148 (n=86)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.7585 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `2.2677` → IC=+0.159 (n=130)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.2677 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `1862.9166` → IC=+0.167 (n=196)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 1862.9166 (IC base=+0.143)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0093` → IC=+0.164 (n=310)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0093 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.5359` → IC=+0.147 (n=310)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.5359 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.192 (n=115)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 18.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` > `0.803` → IC=+0.171 (n=141)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.803 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` > `0.8995` → IC=+0.176 (n=72)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.8995 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` < `0.2184` → IC=+0.139 (n=264)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.2184 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.974` → IC=+0.173 (n=47)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 10.974 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.953` → IC=+0.139 (n=311)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 6.953 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `1.0996` → IC=+0.146 (n=272)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.0996 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` < `0.1188` → IC=+0.134 (n=279)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` < 0.1188 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.1758` → IC=+0.143 (n=96)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.1758 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `1.4338` → IC=+0.170 (n=101)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.4338 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `2.5263` → IC=+0.131 (n=101)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.5263 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `8994.0735` → IC=+0.156 (n=277)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 8994.0735 (IC base=+0.130)

- **PATRÓN** `sigma_h` < `0.0088` → IC=+0.151 (n=279)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0088 (IC base=+0.138)

- **PATRÓN** `sigma_h` > `0.0061` → IC=+0.138 (n=186)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` > 0.0061 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.5119` → IC=+0.183 (n=279)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.5119 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.168 (n=188)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 10.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.619` → IC=+0.140 (n=245)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.619 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.1102` → IC=+0.158 (n=279)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.1102 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.1463` → IC=+0.154 (n=105)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.1463 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.438` → IC=+0.186 (n=49)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 11.438 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.1886` → IC=+0.158 (n=279)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.1886 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` < `0.1338` → IC=+0.162 (n=282)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` < 0.1338 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.1791` → IC=+0.179 (n=241)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 2.1791 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.4499` → IC=+0.163 (n=274)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.4499 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `8854.787` → IC=+0.138 (n=249)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 8854.787 (IC base=+0.138)

### GBM_LATE_5M#SOL#5min
- **FILTRO** `hora_utc` > `6.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=64)

- **FILTRO** `libro_liquidez` < `2949.8034` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `libro_liquidez` < 2949.8034
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=63)

- **FILTRO** `sigma_h` < `0.011` → IC=-0.196 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.011
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=21)

- **FILTRO** `sigma_ewma_delta_pct` < `3.941` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 3.941
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=25)

### GBM_LATE_60M
- **FILTRO** `ibs_20min` < `0.6839` → IC=-0.198 (n=51)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6839
  - _Potencial_: sin este filtro IC_bueno=+0.242 (n=153)

- **FILTRO** `sigma_h` > `0.011` → IC=-0.286 (n=54)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.011
  - _Potencial_: sin este filtro IC_bueno=-0.120 (n=164)

- **FILTRO** `ibs_20min` > `0.1429` → IC=-0.182 (n=86)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1429
  - _Potencial_: sin este filtro IC_bueno=+0.156 (n=30)

- **FILTRO** `dist_vwap_pct` > `0.1153` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1153
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=59)

- **FILTRO** `volumen_regimen` > `1.2318` → IC=-0.200 (n=28)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.2318
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=88)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.199 (n=164)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0054 (IC base=+0.082)

- **PATRÓN** `drift_60min` |x|≤ `0.1312` → IC=+0.194 (n=60)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.1312 (IC base=+0.082)

- **PATRÓN** `ibs_20min` > `0.6839` → IC=+0.242 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6839 (IC base=+0.082)

- **PATRÓN** `dist_vwap_pct` > `0.1247` → IC=+0.171 (n=77)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1247 (IC base=+0.082)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.949` → IC=+0.240 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.949 (IC base=+0.082)

- **PATRÓN** `volumen_regimen` < `0.64` → IC=+0.157 (n=68)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.64 (IC base=+0.082)

- **PATRÓN** `volumen_regimen` > `1.1731` → IC=+0.160 (n=51)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 1.1731 (IC base=+0.082)

- **PATRÓN** `volumen_pendiente_norm` < `0.0847` → IC=+0.278 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0847 (IC base=+0.082)

- **PATRÓN** `volumen_pendiente_norm` > `0.2582` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2582 (IC base=+0.082)

- **PATRÓN** `volumen_spike_ratio` < `2.0129` → IC=+0.265 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0129 (IC base=+0.082)

- **PATRÓN** `volumen_spike_ratio` > `1.4608` → IC=+0.325 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4608 (IC base=+0.082)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.176 (n=137)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.02 (IC base=+0.082)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.8088` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8088
  - _Potencial_: sin este filtro IC_bueno=+0.236 (n=51)

- **FILTRO** `sigma_h` > `0.005` → IC=-0.192 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=47)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.344 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.085)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.157 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 7.0 (IC base=+0.085)

- **PATRÓN** `ibs_20min` > `0.8088` → IC=+0.236 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8088 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` > `0.1487` → IC=+0.188 (n=30)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1487 (IC base=+0.085)

- **PATRÓN** `volumen_regimen` < `0.9151` → IC=+0.125 (n=38)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 0.9151 (IC base=+0.085)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0066` → IC=-0.340 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0066
  - _Potencial_: sin este filtro IC_bueno=-0.096 (n=45)

- **FILTRO** `hora_utc` > `4.0` → IC=-0.326 (n=44)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=24)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.193 (n=86)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0059 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.152 (n=90)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 7.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.134 (n=99)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 17.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` > `0.6789` → IC=+0.294 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6789 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` < `0.1239` → IC=+0.237 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1239 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.134` → IC=+0.311 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.134 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.6219` → IC=+0.250 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6219 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` > `1.0933` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0933 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `2484.2771` → IC=+0.267 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2484.2771 (IC base=+0.134)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.123 (n=51)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.188 (n=30)

- **FILTRO** `ibs_20min` > `0.2` → IC=-0.300 (n=28)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=10)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.188 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=-0.006)

### GBM_LATE_60M_FADE
- **FILTRO** `drift_60min` |x|> `0.1243` → IC=-0.382 (n=32)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1243
  - _Potencial_: sin este filtro IC_bueno=-0.238 (n=63)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.462 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.233 (n=73)

- **FILTRO** `ibs_20min` > `0.6429` → IC=-0.340 (n=48)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6429
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=50)

- **FILTRO** `dist_vwap_pct` < `0.1009` → IC=-0.354 (n=53)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1009
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=45)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `volumen_regimen` < `1.2353` → IC=-0.300 (n=23)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.2353
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=13)

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

- **FILTRO** `dist_vwap_pct` > `0.0802` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.0802
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=15)

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

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.441 (n=15)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` < `0.5964` → IC=-0.255 (n=47)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5964
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=141)

- **FILTRO** `dist_vwap_pct` > `0.2258` → IC=-0.145 (n=29)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2258
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=135)

- **PATRÓN** `ibs_20min` > `0.5964` → IC=+0.136 (n=141)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 0.5964 (IC base=+0.037)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.161 (n=60)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 15.0 (IC base=+0.042)

- **PATRÓN** `ibs_20min` < `0.3387` → IC=+0.122 (n=109)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` < 0.3387 (IC base=+0.042)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.945` → IC=+0.206 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.945 (IC base=+0.042)

- **PATRÓN** `libro_liquidez` > `3314.3277` → IC=+0.131 (n=82)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 3314.3277 (IC base=+0.042)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `sigma_h` < `0.0017` → IC=-0.206 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0017
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=48)

- **FILTRO** `hora_utc` > `16.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=48)

- **FILTRO** `ibs_20min` < `0.4975` → IC=-0.409 (n=20)

  - _Acción_: SKIP cuando `ibs_20min` < 0.4975
  - _Potencial_: sin este filtro IC_bueno=+0.078 (n=43)

- **PATRÓN** `ibs_20min` > `0.7305` → IC=+0.147 (n=32)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.7305 (IC base=-0.085)

- **PATRÓN** `sigma_h` > `0.0035` → IC=+0.177 (n=29)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0035 (IC base=+0.112)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.250 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.112)

- **PATRÓN** `ibs_20min` < `0.3387` → IC=+0.192 (n=63)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.3387 (IC base=+0.112)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.519` → IC=+0.182 (n=42)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 3.519 (IC base=+0.112)

- **PATRÓN** `volumen_regimen` < `1.1843` → IC=+0.146 (n=63)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.1843 (IC base=+0.112)

- **PATRÓN** `libro_liquidez` > `3965.7979` → IC=+0.138 (n=56)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 3965.7979 (IC base=+0.112)

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
- **PATRÓN** `libro_liquidez` > `2490.1288` → IC=+0.156 (n=123)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2490.1288 (IC base=+0.094)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.135 (n=143)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 18.0 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2534.6244` → IC=+0.156 (n=120)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2534.6244 (IC base=+0.117)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `libro_liquidez` > `2490.1288` → IC=+0.156 (n=123)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2490.1288 (IC base=+0.094)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.135 (n=143)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 18.0 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2534.6244` → IC=+0.156 (n=120)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2534.6244 (IC base=+0.117)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `9.0` → IC=-0.185 (n=71)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=46)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=101)

- **FILTRO** `libro_liquidez` < `2114.4748` → IC=-0.339 (n=29)

  - _Acción_: SKIP cuando `libro_liquidez` < 2114.4748
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=88)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=106)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=15)

- **FILTRO** `libro_liquidez` < `11321.3584` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `libro_liquidez` < 11321.3584
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=16)

- **FILTRO** `hora_utc` > `9.0` → IC=-0.167 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=10)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

- **FILTRO** `libro_liquidez` < `13267.3` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_liquidez` < 13267.3
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=8)

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
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=627)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=89)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9444` → IC=-0.289 (n=36)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9444
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=74)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=89)

### LIQUIDACIONES_5M#BNB#5min
- **PATRÓN** `py_entrada` < `0.5` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.5 (IC base=+0.065)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_usd_total` < `26874.22` → IC=-0.156 (n=30)

  - _Acción_: SKIP cuando `liq_usd_total` < 26874.22
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=61)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=17)

- **FILTRO** `libro_liquidez` < `15381.0964` → IC=-0.231 (n=24)

  - _Acción_: SKIP cuando `libro_liquidez` < 15381.0964
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `ballena_activa_n` > `630.0` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `ballena_activa_n` > 630.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=8)

- **PATRÓN** `liq_usd_total` > `99462.85` → IC=+0.136 (n=31)

  - _Acción_: Kelly boost +0.68€ cuando `liq_usd_total` > 99462.85 (IC base=+0.005)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `liq_imbalance_60min` |x|≤ `0.8749` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.8749
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=48)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=45)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=185)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9593` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9593
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=15)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.318 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

- **PATRÓN** `liq_n` > `3.0` → IC=+0.122 (n=72)

  - _Acción_: Kelly boost +0.61€ cuando `liq_n` > 3.0 (IC base=+0.067)

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
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=30)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=30)

### LIQUIDACIONES_60M
- **FILTRO** `py_entrada` > `0.56` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `py_entrada` > 0.56
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=106)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.128 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=58)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=29)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=80)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=29)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=29)

### MOMENTUM_IBS_15M#BNB#15min
- **FILTRO** `libro_liquidez` < `2179.6408` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `libro_liquidez` < 2179.6408
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=126)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=507)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.46` → IC=-0.173 (n=975)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=2934)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.209 (n=990)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=3007)

- **FILTRO** `ibs_20min` > `0.2705` → IC=-0.175 (n=999)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2705
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=2998)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.229 (n=138)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=425)

- **FILTRO** `ibs_20min` < `0.7361` → IC=-0.169 (n=140)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7361
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=423)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.155 (n=166)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=531)

- **FILTRO** `ibs_20min` > `0.75` → IC=-0.159 (n=174)

  - _Acción_: SKIP cuando `ibs_20min` > 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=523)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.202 (n=159)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=488)

- **FILTRO** `ballena_activa_n` > `42.0` → IC=-0.127 (n=218)

  - _Acción_: SKIP cuando `ballena_activa_n` > 42.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=429)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.131 (n=185)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=413)

- **FILTRO** `py_entrada` < `0.43` → IC=-0.203 (n=190)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=408)

- **FILTRO** `ibs_20min` < `0.7244` → IC=-0.182 (n=149)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7244
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=449)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.224 (n=161)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=510)

- **FILTRO** `ibs_20min` > `0.7289` → IC=-0.228 (n=167)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7289
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=504)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.132 (n=183)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=518)

- **FILTRO** `py_entrada` > `0.52` → IC=-0.182 (n=171)

  - _Acción_: SKIP cuando `py_entrada` > 0.52
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=526)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.155 (n=172)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=525)

### MOMENTUM_IBS_15M_BALLENA#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.126 (n=193)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=478)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.218 (n=154)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=488)

- **FILTRO** `ibs_20min` > `0.2778` → IC=-0.173 (n=157)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2778
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=485)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.167 (n=157)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=485)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.216 (n=160)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=492)

- **FILTRO** `ibs_20min` < `0.755` → IC=-0.148 (n=163)

  - _Acción_: SKIP cuando `ibs_20min` < 0.755
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=489)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=637)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.238 (n=208)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=435)

- **FILTRO** `ibs_20min` > `0.2727` → IC=-0.204 (n=160)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2727
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=483)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `hora_utc` > `19.0` → IC=-0.206 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=128)

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
- **FILTRO** `hora_utc` < `19.0` → IC=-0.132 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 19.0
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=12)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.143 (n=2915)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=6955)

- **FILTRO** `py_entrada` < `0.36` → IC=-0.282 (n=2431)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=7439)

- **FILTRO** `ibs_7min` < `0.7274` → IC=-0.236 (n=2467)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7274
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=7403)

- **FILTRO** `ballena_activa_n` > `19.0` → IC=-0.173 (n=3311)

  - _Acción_: SKIP cuando `ballena_activa_n` > 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=6559)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.221 (n=3016)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=9068)

- **FILTRO** `ibs_7min` > `0.7197` → IC=-0.172 (n=3020)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7197
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=9064)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.314 (n=336)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=1011)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.190 (n=945)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=402)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.248 (n=320)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=1027)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.225 (n=503)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=1583)

- **FILTRO** `drift_7min_pct` |x|> `0.1304` → IC=-0.141 (n=709)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1304
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=1377)

- **FILTRO** `ibs_7min` > `0.2991` → IC=-0.167 (n=709)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2991
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=1377)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.143 (n=429)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=1474)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.255 (n=459)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=1444)

- **FILTRO** `ibs_7min` < `0.7899` → IC=-0.190 (n=475)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7899
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=1428)

- **FILTRO** `ballena_activa_n` > `163.0` → IC=-0.193 (n=473)

  - _Acción_: SKIP cuando `ballena_activa_n` > 163.0
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=1430)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.220 (n=470)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=1433)

- **FILTRO** `ballena_activa_n` > `98.0` → IC=-0.166 (n=639)

  - _Acción_: SKIP cuando `ballena_activa_n` > 98.0
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=1264)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.187 (n=464)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=967)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.309 (n=460)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=971)

- **FILTRO** `ibs_7min` < `0.2184` → IC=-0.288 (n=356)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2184
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=1075)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.270 (n=350)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=1081)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.248 (n=462)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=1662)

- **FILTRO** `ibs_7min` > `0.8117` → IC=-0.185 (n=529)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8117
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=1595)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.150 (n=515)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=1147)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.214 (n=795)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=867)

- **FILTRO** `ibs_7min` < `0.7565` → IC=-0.191 (n=415)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7565
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=1247)

- **FILTRO** `ballena_activa_n` > `41.0` → IC=-0.198 (n=415)

  - _Acción_: SKIP cuando `ballena_activa_n` > 41.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=1247)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.265 (n=398)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=1263)

- **FILTRO** `ibs_7min` > `0.1846` → IC=-0.168 (n=564)

  - _Acción_: SKIP cuando `ibs_7min` > 0.1846
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=1097)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.172 (n=555)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=1106)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.230 (n=465)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1446)

- **FILTRO** `ibs_7min` < `0.7692` → IC=-0.201 (n=469)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7692
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=1442)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.182 (n=467)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=1444)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.182 (n=542)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=1696)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.143 (n=458)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=1158)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.302 (n=393)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=1223)

- **FILTRO** `ibs_7min` < `0.75` → IC=-0.233 (n=402)

  - _Acción_: SKIP cuando `ibs_7min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=1214)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.234 (n=392)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=1224)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.271 (n=418)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=1654)

- **FILTRO** `ibs_7min` > `0.8` → IC=-0.168 (n=516)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=1556)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.128 (n=664)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=1408)

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

- **PATRÓN** `delta_ratio` |x|> `0.3987` → IC=+0.134 (n=359)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio` |x|> 0.3987 (IC base=+0.115)

- **PATRÓN** `total_vol_5m` < `459.6089` → IC=+0.167 (n=112)

  - _Acción_: Kelly boost +0.83€ cuando `total_vol_5m` < 459.6089 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `3219.7168` → IC=+0.151 (n=130)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3219.7168 (IC base=+0.115)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.237 (n=55)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.130 (n=71)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 53.0 (IC base=+0.119)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3996` → IC=+0.125 (n=54)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.62€ cuando `delta_ratio` |x|> 0.3996 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `2022.4544` → IC=+0.125 (n=54)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 2022.4544 (IC base=+0.095)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4194` → IC=+0.167 (n=22)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.83€ cuando `delta_ratio` |x|> 0.4194 (IC base=+0.100)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.167 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 8.0 (IC base=+0.100)

- **PATRÓN** `total_vol_5m` < `533.1536` → IC=+0.176 (n=32)

  - _Acción_: Kelly boost +0.88€ cuando `total_vol_5m` < 533.1536 (IC base=+0.100)

- **PATRÓN** `ballena_activa_n` < `158.0` → IC=+0.125 (n=46)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 158.0 (IC base=+0.100)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3997` → IC=+0.214 (n=47)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.3997 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.222 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.141)

- **PATRÓN** `total_vol_5m` < `12213.535` → IC=+0.153 (n=47)

  - _Acción_: Kelly boost +0.77€ cuando `total_vol_5m` < 12213.535 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `3299.6255` → IC=+0.159 (n=42)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 3299.6255 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `70.0` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 70.0 (IC base=+0.141)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.3964` → IC=+0.129 (n=60)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.65€ cuando `delta_ratio` |x|> 0.3964 (IC base=+0.061)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.157 (n=33)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.061)

- **PATRÓN** `libro_liquidez` > `3395.535` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 3395.535 (IC base=+0.061)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` < `0.0084` → IC=-0.180 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0084
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=71)

- **FILTRO** `T_h` > `63.9853` → IC=-0.345 (n=101)

  - _Acción_: SKIP cuando `T_h` > 63.9853
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=35)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0068` → IC=-0.364 (n=42)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=+0.283 (n=21)

- **FILTRO** `T_h` > `87.9957` → IC=-0.460 (n=23)

  - _Acción_: SKIP cuando `T_h` > 87.9957
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=25)

- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.283 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=-0.146)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `T_h` > `144.5498` → IC=-0.339 (n=29)

  - _Acción_: SKIP cuando `T_h` > 144.5498
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=90)

- **FILTRO** `T_h` < `135.9851` → IC=-0.436 (n=45)

  - _Acción_: SKIP cuando `T_h` < 135.9851
  - _Potencial_: sin este filtro IC_bueno=-0.266 (n=45)

- **PATRÓN** `pct_vs_K` |x|≤ `1.3968` → IC=+0.250 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 1.3968 (IC base=-0.054)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.192 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0048 (IC base=+0.092)

- **PATRÓN** `T_h` < `111.9808` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `T_h` < 111.9808 (IC base=+0.092)

- **PATRÓN** `pct_vs_K` |x|≤ `1.4454` → IC=+0.308 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 1.4454 (IC base=+0.092)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `T_h` > `87.9957` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `T_h` > 87.9957
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=20)

- **FILTRO** `sigma_h` < `0.0045` → IC=-0.357 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0045
  - _Potencial_: sin este filtro IC_bueno=-0.292 (n=22)

### STREAK_FADE_15M
- **FILTRO** `ballena_activa_n` > `67.0` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `ballena_activa_n` > 67.0
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=35)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=91)

- **PATRÓN** `streak_estiramiento` < `0.4674` → IC=+0.395 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.4674 (IC base=+0.052)

- **PATRÓN** `ballena_activa_n` < `82.0` → IC=+0.132 (n=74)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 82.0 (IC base=+0.052)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `ballena_activa_n` > `18.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `ballena_activa_n` > 18.0
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=58)

- **FILTRO** `streak_estiramiento` > `0.4326` → IC=-0.136 (n=31)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.4326
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=16)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=57)

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
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=93)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=102)

- **FILTRO** `streak_estiramiento` > `0.6102` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.6102
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=58)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=103)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=176)

- **PATRÓN** `streak_estiramiento` < `0.3153` → IC=+0.176 (n=32)

  - _Acción_: Kelly boost +0.88€ cuando `streak_estiramiento` < 0.3153 (IC base=+0.012)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=352)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=180)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=249)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.162 (n=75)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 5.0 (IC base=+0.068)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=1259)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=713)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=721)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.154 (n=131)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.003 (IC base=+0.115)

- **PATRÓN** `drift_60min` |x|≤ `0.1648` → IC=+0.126 (n=346)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.63€ cuando `drift_60min` |x|≤ 0.1648 (IC base=+0.115)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0679` → IC=+0.123 (n=393)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.61€ cuando `delta_ratio_macro` |x|> 0.0679 (IC base=+0.115)

- **PATRÓN** `ibs_15` > `0.5294` → IC=+0.202 (n=394)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5294 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` > `0.3946` → IC=+0.176 (n=103)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.3946 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.763` → IC=+0.247 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.763 (IC base=+0.115)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=412)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.01 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `7519.476` → IC=+0.162 (n=131)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 7519.476 (IC base=+0.115)

### UPDOWN_GBM#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1012` → IC=-0.126 (n=185)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1012
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=376)

- **FILTRO** `ibs_15` < `0.2689` → IC=-0.176 (n=140)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.2689
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=421)

- **FILTRO** `sigma_ewma_delta_pct` > `6.666` → IC=-0.209 (n=53)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.666
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=508)

### UPDOWN_GBM#60min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0347` → IC=-0.192 (n=24)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0347
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=49)

- **FILTRO** `ibs_15` < `0.2105` → IC=-0.214 (n=19)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.2105
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=40)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=19)

### UPDOWN_GBM#BTC#15min
- **FILTRO** `sigma_h` < `0.0041` → IC=-0.260 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0041
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=69)

- **FILTRO** `hora_utc` > `16.0` → IC=-0.239 (n=21)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=71)

- **FILTRO** `ibs_15` > `0.7088` → IC=-0.167 (n=22)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.7088
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=70)

- **FILTRO** `ibs_15` < `0.2983` → IC=-0.180 (n=23)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.2983
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=69)

- **FILTRO** `libro_liquidez` < `13630.9549` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `libro_liquidez` < 13630.9549
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=69)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.160 (n=101)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0038 (IC base=+0.156)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.200 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.1944` → IC=+0.184 (n=115)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.1944 (IC base=+0.156)

- **PATRÓN** `drift_15min` |x|≤ `0.4671` → IC=+0.183 (n=77)

  - _Acción_: Kelly boost +0.92€ cuando `drift_15min` |x|≤ 0.4671 (IC base=+0.156)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2457` → IC=+0.200 (n=38)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2457 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.181 (n=117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 4.0 (IC base=+0.156)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.167 (n=118)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 17.0 (IC base=+0.156)

- **PATRÓN** `ibs_15` > `0.8791` → IC=+0.256 (n=76)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8791 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `0.3217` → IC=+0.211 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3217 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` < `0.546` → IC=+0.164 (n=126)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.546 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.029` → IC=+0.200 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.029 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `11757.2155` → IC=+0.185 (n=52)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 11757.2155 (IC base=+0.156)

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
- **FILTRO** `hora_utc` < `11.0` → IC=-0.167 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=82)

### UPDOWN_GBM#ETH#15min
- **FILTRO** `ibs_15` < `0.622` → IC=-0.244 (n=37)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.622
  - _Potencial_: sin este filtro IC_bueno=+0.231 (n=76)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.123 (n=75)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0044 (IC base=+0.074)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2085` → IC=+0.183 (n=39)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.91€ cuando `delta_ratio_macro` |x|> 0.2085 (IC base=+0.074)

- **PATRÓN** `ibs_15` > `0.622` → IC=+0.231 (n=76)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.622 (IC base=+0.074)

- **PATRÓN** `sigma_ewma_delta_pct` > `15.362` → IC=+0.188 (n=30)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 15.362 (IC base=+0.074)

### UPDOWN_GBM#ETH#5min
- **FILTRO** `hora_utc` < `3.0` → IC=-0.200 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=81)

- **FILTRO** `dist_vwap_pct` > `0.1505` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1505
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=83)

- **FILTRO** `ballena_activa_n` > `1.0` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `ballena_activa_n` > 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=35)

- **FILTRO** `drift_15min` |x|> `0.5041` → IC=-0.145 (n=136)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.5041
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=412)

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
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0264` → IC=-0.224 (n=27)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0264
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=55)

- **FILTRO** `drift_60min` |x|> `0.7937` → IC=-0.155 (n=27)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.7937
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=55)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1015` → IC=-0.155 (n=27)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1015
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=55)

- **FILTRO** `ibs_15` < `0.2222` → IC=-0.409 (n=20)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.2222
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=62)

### UPDOWN_GBM#SOL#60min
- **FILTRO** `sigma_h` > `0.0127` → IC=-0.214 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0127
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=39)

- **FILTRO** `sigma_ewma_delta_pct` < `3.393` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 3.393
  - _Potencial_: sin este filtro IC_bueno=+0.375 (n=6)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.265 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=-0.017)

- **PATRÓN** `dist_vwap_pct` < `0.3805` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.3805 (IC base=-0.017)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.140 (n=48)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 15.0 (IC base=+0.097)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.160 (n=48)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 6.0 (IC base=+0.097)

- **PATRÓN** `ibs_15` > `0.5556` → IC=+0.181 (n=92)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.90€ cuando `ibs_15` > 0.5556 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.3338` → IC=+0.288 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3338 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.845` → IC=+0.240 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.845 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `2496.2216` → IC=+0.160 (n=92)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2496.2216 (IC base=+0.097)

- **PATRÓN** `ibs_15` < `0.125` → IC=+0.204 (n=113)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.125 (IC base=+0.046)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.005` → IC=+0.372 (n=76)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.311)

- **PATRÓN** `drift_60min` |x|≤ `0.1159` → IC=+0.341 (n=111)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1159 (IC base=+0.311)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1505` → IC=+0.330 (n=110)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1505 (IC base=+0.311)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.343 (n=151)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.311)

- **PATRÓN** `ibs_15` > `0.8171` → IC=+0.353 (n=148)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8171 (IC base=+0.311)

- **PATRÓN** `dist_vwap_pct` > `0.4534` → IC=+0.354 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4534 (IC base=+0.311)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.649` → IC=+0.322 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.649 (IC base=+0.311)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.311 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.311)

- **PATRÓN** `libro_liquidez` > `7269.9168` → IC=+0.331 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7269.9168 (IC base=+0.311)

- **PATRÓN** `ballena_activa_n` < `528.0` → IC=+0.363 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 528.0 (IC base=+0.311)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1971` → IC=+0.300 (n=83)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1971 (IC base=+0.287)

- **PATRÓN** `sigma_h` < `0.0024` → IC=+0.295 (n=42)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0024 (IC base=+0.287)

- **PATRÓN** `sigma_h` > `0.0045` → IC=+0.353 (n=32)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0045 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.162` → IC=+0.312 (n=83)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.162 (IC base=+0.287)

- **PATRÓN** `drift_15min` |x|≤ `0.4155` → IC=+0.318 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4155 (IC base=+0.287)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1236` → IC=+0.405 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1236 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.322 (n=99)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.287)

- **PATRÓN** `ibs_15` > `0.838` → IC=+0.337 (n=84)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.838 (IC base=+0.287)

- **PATRÓN** `dist_vwap_pct` > `0.4531` → IC=+0.385 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4531 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.389` → IC=+0.294 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 8.389 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `9210.2084` → IC=+0.322 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9210.2084 (IC base=+0.287)

- **PATRÓN** `ballena_activa_n` < `581.0` → IC=+0.405 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 581.0 (IC base=+0.287)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.353 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.335)

- **PATRÓN** `sigma_h` > `0.006` → IC=+0.357 (n=33)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.335)

- **PATRÓN** `drift_60min` |x|≤ `0.1189` → IC=+0.380 (n=48)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1189 (IC base=+0.335)

- **PATRÓN** `delta_ratio_macro` |x|> `0.13` → IC=+0.380 (n=48)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.13 (IC base=+0.335)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2773` → IC=+0.354 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2773 (IC base=+0.335)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.338 (n=66)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.335)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.331 (n=63)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.335)

- **PATRÓN** `ibs_15` > `0.8055` → IC=+0.409 (n=64)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8055 (IC base=+0.335)

- **PATRÓN** `dist_vwap_pct` < `0.3445` → IC=+0.348 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3445 (IC base=+0.335)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.86` → IC=+0.372 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.86 (IC base=+0.335)

- **PATRÓN** `libro_liquidez` > `3271.2182` → IC=+0.340 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3271.2182 (IC base=+0.335)

- **PATRÓN** `ballena_activa_n` < `183.0` → IC=+0.353 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 183.0 (IC base=+0.335)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.01` → IC=-0.184 (n=270)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=814)

- **FILTRO** `ibs_15` < `0.5391` → IC=-0.215 (n=135)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5391
  - _Potencial_: sin este filtro IC_bueno=+0.188 (n=277)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.120 (n=285)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=799)

- **FILTRO** `sigma_ewma_delta_pct` > `17.671` → IC=-0.177 (n=367)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.671
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=2805)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3622` → IC=+0.138 (n=147)

  - _Acción_: Kelly boost +0.69€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3622 (IC base=-0.066)

- **PATRÓN** `ibs_15` > `0.5391` → IC=+0.188 (n=277)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.94€ cuando `ibs_15` > 0.5391 (IC base=-0.066)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1402` → IC=+0.253 (n=148)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1402 (IC base=-0.077)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1081` → IC=+0.287 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1081 (IC base=-0.077)

- **PATRÓN** `ibs_15` < `0.3696` → IC=+0.317 (n=222)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3696 (IC base=-0.077)

- **PATRÓN** `dist_vwap_pct` < `0.1348` → IC=+0.255 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1348 (IC base=-0.077)

- **PATRÓN** `ballena_activa_n` < `64.0` → IC=+0.256 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 64.0 (IC base=-0.077)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0075` → IC=-0.250 (n=170)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0075
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=513)

- **FILTRO** `sigma_h` < `0.0036` → IC=-0.218 (n=225)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0036
  - _Potencial_: sin este filtro IC_bueno=-0.209 (n=458)

- **FILTRO** `hora_utc` > `16.0` → IC=-0.262 (n=170)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=513)

- **FILTRO** `sigma_ewma_delta_pct` > `19.708` → IC=-0.269 (n=128)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.708
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=555)

- **FILTRO** `libro_liquidez` < `15450.3532` → IC=-0.224 (n=450)

  - _Acción_: SKIP cuando `libro_liquidez` < 15450.3532
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=233)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.151 (n=61)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0029 (IC base=+0.013)

- **PATRÓN** `ibs_15` > `0.7496` → IC=+0.292 (n=22)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7496 (IC base=+0.013)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.4704` → IC=-0.354 (n=46)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.4704
  - _Potencial_: sin este filtro IC_bueno=+0.188 (n=139)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=168)

- **PATRÓN** `drift_60min` |x|≤ `0.0629` → IC=+0.194 (n=47)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.0629 (IC base=+0.051)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3743` → IC=+0.205 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3743 (IC base=+0.051)

- **PATRÓN** `ibs_15` > `0.4704` → IC=+0.188 (n=139)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.94€ cuando `ibs_15` > 0.4704 (IC base=+0.051)

- **PATRÓN** `libro_liquidez` > `10425.7161` → IC=+0.192 (n=63)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 10425.7161 (IC base=+0.051)

- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1041` → IC=+0.259 (n=81)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1041 (IC base=+0.242)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.256 (n=121)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.242)

- **PATRÓN** `drift_15min` |x|≤ `0.4267` → IC=+0.267 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4267 (IC base=+0.242)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1523` → IC=+0.271 (n=81)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1523 (IC base=+0.242)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.304` → IC=+0.264 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.304 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.242 (n=91)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.242)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.333 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.242)

- **PATRÓN** `ibs_15` < `0.3696` → IC=+0.329 (n=121)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3696 (IC base=+0.242)

- **PATRÓN** `dist_vwap_pct` < `0.1242` → IC=+0.260 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1242 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.486` → IC=+0.269 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.486 (IC base=+0.242)

- **PATRÓN** `libro_liquidez` > `13769.0298` → IC=+0.267 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13769.0298 (IC base=+0.242)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0108` → IC=-0.246 (n=65)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0108
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=198)

- **FILTRO** `drift_15min` |x|> `0.7912` → IC=-0.231 (n=65)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.7912
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=198)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.129 (n=95)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=168)

- **FILTRO** `ibs_15` > `0.2796` → IC=-0.136 (n=20)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.2796
  - _Potencial_: sin este filtro IC_bueno=+0.221 (n=41)

- **PATRÓN** `ibs_15` > `0.8125` → IC=+0.206 (n=15)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8125 (IC base=-0.111)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0839` → IC=+0.151 (n=41)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio_macro` |x|> 0.0839 (IC base=-0.059)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2219` → IC=+0.192 (n=37)

  - _Acción_: Kelly boost +0.96€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2219 (IC base=-0.059)

- **PATRÓN** `ibs_15` < `0.2796` → IC=+0.221 (n=41)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.2796 (IC base=-0.059)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `drift_15min` |x|> `1.1429` → IC=-0.250 (n=70)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.1429
  - _Potencial_: sin este filtro IC_bueno=-0.131 (n=212)

- **FILTRO** `sigma_ewma_delta_pct` > `15.037` → IC=-0.225 (n=38)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 15.037
  - _Potencial_: sin este filtro IC_bueno=-0.150 (n=244)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.278 (n=25)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.149 (n=257)

- **FILTRO** `libro_liquidez` < `2491.4834` → IC=-0.236 (n=70)

  - _Acción_: SKIP cuando `libro_liquidez` < 2491.4834
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=212)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1734` → IC=+0.426 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1734 (IC base=-0.069)

- **PATRÓN** `ibs_15` > `0.122` → IC=+0.371 (n=29)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.122 (IC base=-0.069)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.280 (n=262)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.280)

- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.293 (n=119)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0054 (IC base=+0.280)

- **PATRÓN** `drift_60min` |x|≤ `0.0529` → IC=+0.333 (n=88)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0529 (IC base=+0.280)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1879` → IC=+0.311 (n=120)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1879 (IC base=+0.280)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1236` → IC=+0.354 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1236 (IC base=+0.280)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.310 (n=272)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.280)

- **PATRÓN** `ibs_15` > `0.9676` → IC=+0.351 (n=119)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9676 (IC base=+0.280)

- **PATRÓN** `dist_vwap_pct` > `0.5182` → IC=+0.367 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5182 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.643` → IC=+0.287 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.643 (IC base=+0.280)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.280 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `11963.9388` → IC=+0.318 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11963.9388 (IC base=+0.280)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.304 (n=49)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0057 (IC base=+0.268)

- **PATRÓN** `drift_60min` |x|≤ `0.162` → IC=+0.295 (n=130)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.162 (IC base=+0.268)

- **PATRÓN** `drift_15min` |x|≤ `0.6649` → IC=+0.273 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.6649 (IC base=+0.268)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2616` → IC=+0.304 (n=49)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2616 (IC base=+0.268)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1236` → IC=+0.333 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1236 (IC base=+0.268)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.295 (n=154)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.268)

- **PATRÓN** `ibs_15` > `0.9691` → IC=+0.312 (n=67)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9691 (IC base=+0.268)

- **PATRÓN** `dist_vwap_pct` > `0.3582` → IC=+0.364 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3582 (IC base=+0.268)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.453` → IC=+0.271 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.453 (IC base=+0.268)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.509` → IC=+0.287 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 8.509 (IC base=+0.268)

- **PATRÓN** `libro_liquidez` > `13337.4554` → IC=+0.312 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13337.4554 (IC base=+0.268)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.303 (n=115)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0074 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.0637` → IC=+0.349 (n=51)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0637 (IC base=+0.292)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0676` → IC=+0.317 (n=102)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0676 (IC base=+0.292)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3141` → IC=+0.326 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3141 (IC base=+0.292)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.325 (n=118)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.292)

- **PATRÓN** `ibs_15` > `0.8702` → IC=+0.327 (n=102)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8702 (IC base=+0.292)

- **PATRÓN** `dist_vwap_pct` > `0.6569` → IC=+0.380 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6569 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.127` → IC=+0.298 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.127 (IC base=+0.292)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.301 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `9979.9504` → IC=+0.370 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9979.9504 (IC base=+0.292)

- **PATRÓN** `ballena_activa_n` < `107.0` → IC=+0.367 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 107.0 (IC base=+0.292)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.096` → IC=-0.255 (n=47)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.096
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=94)

- **FILTRO** `sigma_h` > `0.0056` → IC=-0.257 (n=35)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0056
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=106)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1212` → IC=-0.170 (n=98)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1212
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=298)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.154 (n=53)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=27)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0878` → IC=-0.214 (n=19)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0878
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=61)

- **FILTRO** `drift_15min` |x|> `0.2326` → IC=-0.222 (n=16)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.2326
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=18)

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
- **PATRÓN** `T_h` < `79.3918` → IC=+0.222 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 79.3918 (IC base=+0.100)

- **PATRÓN** `ratio` < `0.972` → IC=+0.460 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.972 (IC base=+0.100)

- **PATRÓN** `T_h` > `146.0966` → IC=+0.431 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0966 (IC base=+0.342)

- **PATRÓN** `ratio` < `1.0189` → IC=+0.214 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 1.0189 (IC base=+0.342)

- **PATRÓN** `ratio` > `1.0147` → IC=+0.198 (n=51)

  - _Acción_: Kelly boost +0.99€ cuando `ratio` > 1.0147 (IC base=+0.342)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` < `57.6124` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `T_h` < 57.6124 (IC base=+0.094)

- **PATRÓN** `T_h` < `111.9558` → IC=+0.335 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 111.9558 (IC base=+0.266)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` < `113.3454` → IC=+0.242 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 113.3454 (IC base=+0.138)

- **PATRÓN** `T_h` < `87.9969` → IC=+0.322 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 87.9969 (IC base=+0.306)

- **PATRÓN** `T_h` > `145.7688` → IC=+0.324 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7688 (IC base=+0.306)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `135.9824` → IC=+0.436 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 135.9824 (IC base=+0.413)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-SIGMA-SOL-60MIN**: `UPDOWN_GBM#SOL#60min` gana cuando sigma_h < 0.0058 (IC=+0.265 n=15). Implementar como filtro pre-predicción en shadow_predict.py.
- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5294 sube el IC de +0.115 a +0.202 en UPDOWN_GBM#15min (n=394). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.8791 sube el IC de +0.156 a +0.256 en UPDOWN_GBM#BTC#15min (n=76). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.622 sube el IC de +0.074 a +0.231 en UPDOWN_GBM#ETH#15min (n=76). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.056 a +0.265 en UPDOWN_GBM#SOL#15min (n=32). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5556 sube el IC de +0.097 a +0.181 en UPDOWN_GBM#XRP#15min (n=92). Ya aplicado como kelly_boost=+0.90€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.125 sube el IC de +0.046 a +0.204 en UPDOWN_GBM#XRP#15min (n=113). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.5391 sube el IC de -0.066 a +0.188 en UPDOWN_GBM_15M_TARDIO (n=277). Ya aplicado como kelly_boost=+0.94€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3696 sube el IC de -0.077 a +0.317 en UPDOWN_GBM_15M_TARDIO (n=222). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7496 sube el IC de +0.013 a +0.292 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=22). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.4704 sube el IC de +0.051 a +0.188 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=139). Ya aplicado como kelly_boost=+0.94€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3696 sube el IC de +0.242 a +0.329 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=121). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8125 sube el IC de -0.111 a +0.206 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=15). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.2796 sube el IC de -0.059 a +0.221 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=41). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS > 0.122 sube el IC de -0.069 a +0.371 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=29). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.9676 sube el IC de +0.280 a +0.351 en UPDOWN_GBM_IBS_ALTO (n=119). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.9691 sube el IC de +0.268 a +0.312 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=67). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8702 sube el IC de +0.292 a +0.327 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=102). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.8171 sube el IC de +0.311 a +0.353 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=148). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.838 sube el IC de +0.287 a +0.337 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=84). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.8055 sube el IC de +0.335 a +0.409 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=64). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#SOL#sniper` — IC=+0.474 n=36. Faltan ~4 resoluciones para umbral n≥40. ETA: ~3h.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#SOL` — IC=+0.474 n=36. Faltan ~4 resoluciones para umbral n≥40. ETA: ~3h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min` — IC=+0.357 n=33. Faltan ~7 resoluciones para umbral n≥40. ETA: ~5h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL` — IC=+0.357 n=33. Faltan ~7 resoluciones para umbral n≥40. ETA: ~5h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min` — IC=+0.147 n=32. Faltan ~8 resoluciones para umbral n≥40. ETA: ~6h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 649 | +0.091 | +45.57€ | 0 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 649 | +0.091 | +45.57€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 397 | +0.117 | +35.95€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 397 | +0.117 | +35.95€ | 1 | 11 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 222 | +0.036 | -0.81€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 222 | +0.036 | -0.81€ | 7 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 29 | +0.177 | +10.93€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 29 | +0.177 | +10.93€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 11088 | -0.097 | -1845.15€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 777 | -0.047 | -129.15€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 10311 | -0.100 | -1715.99€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 1413 | -0.043 | -280.41€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 1413 | -0.043 | -280.41€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 777 | -0.047 | -129.15€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 777 | -0.047 | -129.15€ | 2 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 1438 | -0.143 | -427.68€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 1438 | -0.143 | -427.68€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 2980 | -0.064 | -292.65€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 2980 | -0.064 | -292.65€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 2565 | -0.101 | -248.04€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 2565 | -0.101 | -248.04€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 1915 | -0.166 | -467.22€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 1915 | -0.166 | -467.22€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 919 | -0.057 | +447.98€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 260 | +0.000 | +105.50€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 659 | -0.079 | +342.48€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 919 | -0.057 | +447.98€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 260 | +0.000 | +105.50€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 659 | -0.079 | +342.48€ | 0 | 0 |
| 🚫 CANDIDATA9_BOT_CONSENSO | 19 | -0.204 | -9.74€ | 0 | 0 |
| 🚫 CANDIDATA9_BOT_CONSENSO#5min | 19 | -0.204 | -9.74€ | 0 | 0 |
| 🚫 CANDIDATA9_BOT_CONSENSO#BTC | 19 | -0.204 | -9.74€ | 0 | 0 |
| 🚫 CANDIDATA9_BOT_CONSENSO#BTC#5min | 19 | -0.204 | -9.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 36051 | +0.115 | -2236.51€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 6491 | +0.186 | -224.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 114 | -0.086 | -47.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 26121 | +0.098 | -1909.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 3325 | +0.119 | -54.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 4382 | +0.069 | -692.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 22 | -0.083 | +0.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#240min | 5 | -0.089 | -6.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 4355 | +0.071 | -687.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 7375 | +0.134 | -148.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 1840 | +0.199 | -83.43€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 4347 | +0.110 | -94.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 1146 | +0.127 | +51.08€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 4392 | +0.083 | -522.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 23 | +0.060 | +2.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 4368 | +0.083 | -522.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 7913 | +0.127 | -122.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 2357 | +0.169 | -13.82€ | 0 | 8 |
| 🚫 FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 4349 | +0.113 | -71.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 1195 | +0.100 | -29.15€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 7610 | +0.133 | -468.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 2232 | +0.200 | -129.75€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 52 | +0.018 | -8.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 4342 | +0.100 | -254.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 984 | +0.132 | -76.76€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#XRP | 4379 | +0.108 | -281.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 17 | -0.022 | -0.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 4360 | +0.108 | -280.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 6389 | +0.175 | -486.94€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 6389 | +0.175 | -486.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 1613 | +0.168 | -170.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 1613 | +0.168 | -170.43€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 127 | -0.120 | +1.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 127 | -0.120 | +1.42€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 1588 | +0.167 | -171.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 1588 | +0.167 | -171.46€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 1434 | +0.233 | -37.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 1434 | +0.233 | -37.30€ | 0 | 2 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 1548 | +0.182 | -122.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 1548 | +0.182 | -122.92€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 329 | +0.449 | +5.36€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 329 | +0.449 | +5.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 125 | +0.445 | +2.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 125 | +0.445 | +2.16€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 124 | +0.436 | +0.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 124 | +0.436 | +0.18€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 76 | +0.449 | +2.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 76 | +0.449 | +2.79€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 18582 | +0.191 | -1638.77€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 18582 | +0.191 | -1638.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 3372 | +0.131 | -598.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 3372 | +0.131 | -598.77€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 2909 | +0.233 | -68.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 2909 | +0.233 | -68.55€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 3179 | +0.168 | -384.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 3179 | +0.168 | -384.20€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 2955 | +0.227 | -97.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 2955 | +0.227 | -97.53€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 3035 | +0.211 | -171.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 3035 | +0.211 | -171.86€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 3132 | +0.183 | -317.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 3132 | +0.183 | -317.86€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 6798 | +0.133 | +253.21€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 6798 | +0.133 | +253.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 3383 | +0.139 | +159.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 3383 | +0.139 | +159.38€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 3415 | +0.128 | +93.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 3415 | +0.128 | +93.82€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 818 | +0.296 | -0.61€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 818 | +0.296 | -0.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 351 | +0.282 | -7.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 351 | +0.282 | -7.18€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 382 | +0.297 | +5.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 382 | +0.297 | +5.36€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 85 | +0.339 | +1.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 85 | +0.339 | +1.21€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 350 | +0.415 | -14.68€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 350 | +0.415 | -14.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 156 | +0.411 | -7.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 156 | +0.411 | -7.49€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 161 | +0.420 | -6.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 161 | +0.420 | -6.21€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 33 | +0.357 | -0.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 33 | +0.357 | -0.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 284 | +0.084 | -7.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 86 | +0.091 | -2.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 198 | +0.080 | -5.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 12 | +0.086 | +1.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 12 | +0.086 | +1.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 230 | +0.090 | -2.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 32 | +0.147 | +2.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 198 | +0.080 | -5.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 42 | +0.023 | -6.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 42 | +0.023 | -6.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 8273 | +0.095 | -291.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 800 | +0.072 | -17.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 7473 | +0.097 | -273.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 5394 | +0.097 | -110.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 800 | +0.072 | -17.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 4594 | +0.101 | -92.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 465 | +0.119 | +8.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 465 | +0.119 | +8.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 2414 | +0.086 | -189.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 2414 | +0.086 | -189.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 463 | +0.283 | -32.80€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 463 | +0.283 | -32.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 463 | +0.283 | -32.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 463 | +0.283 | -32.80€ | 0 | 3 |
| ✅ GBM_LATE_15M | 8637 | +0.044 | +2802.01€ | 0 | 14 |
| ✅ GBM_LATE_15M#15min | 8637 | +0.044 | +2802.01€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 1214 | +0.178 | +786.74€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 1214 | +0.178 | +786.74€ | 0 | 20 |
| ✅ GBM_LATE_15M#BTC | 1243 | +0.172 | +723.16€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 1243 | +0.172 | +723.16€ | 0 | 27 |
| ✅ GBM_LATE_15M#DOGE | 1218 | +0.193 | +858.85€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 1218 | +0.193 | +858.85€ | 0 | 22 |
| ✅ GBM_LATE_15M#ETH | 1407 | -0.049 | +31.07€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 1407 | -0.049 | +31.07€ | 4 | 12 |
| ✅ GBM_LATE_15M#SOL | 1540 | -0.050 | +144.25€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 1540 | -0.050 | +144.25€ | 5 | 3 |
| ✅ GBM_LATE_15M#XRP | 2015 | -0.070 | +257.94€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 2015 | -0.070 | +257.94€ | 4 | 7 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 9514 | +0.047 | +3763.94€ | 0 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 9514 | +0.047 | +3763.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 1512 | -0.015 | +675.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 1512 | -0.015 | +675.38€ | 2 | 4 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 2066 | -0.040 | +166.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 2066 | -0.040 | +166.19€ | 1 | 2 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 1082 | +0.243 | +1004.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 1082 | +0.243 | +1004.05€ | 0 | 24 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 1549 | -0.055 | -26.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 1549 | -0.055 | -26.65€ | 10 | 2 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 1647 | -0.028 | +343.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 1647 | -0.028 | +343.06€ | 7 | 8 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 1658 | +0.251 | +1601.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 1658 | +0.251 | +1601.91€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 7037 | +0.170 | +4880.87€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 7037 | +0.170 | +4880.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 929 | +0.189 | +666.49€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 929 | +0.189 | +666.49€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 1190 | +0.161 | +786.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 1190 | +0.161 | +786.07€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 920 | +0.203 | +715.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 920 | +0.203 | +715.19€ | 0 | 18 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 1162 | +0.155 | +731.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 1162 | +0.155 | +731.60€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 1330 | +0.127 | +834.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 1330 | +0.127 | +834.04€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 1506 | +0.195 | +1147.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 1506 | +0.195 | +1147.48€ | 0 | 20 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 1427 | +0.083 | +320.41€ | 0 | 10 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 1427 | +0.083 | +320.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 56 | +0.086 | +14.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 56 | +0.086 | +14.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 358 | +0.072 | +81.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 358 | +0.072 | +81.80€ | 3 | 11 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 223 | +0.144 | +102.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 223 | +0.144 | +102.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 237 | +0.170 | +72.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 237 | +0.170 | +72.89€ | 2 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 321 | -0.020 | +4.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 321 | -0.020 | +4.04€ | 4 | 3 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 232 | +0.090 | +44.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 232 | +0.090 | +44.77€ | 0 | 8 |
| ✅ GBM_LATE_15M_TARDIO | 8267 | +0.169 | +5579.77€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#15min | 8267 | +0.169 | +5579.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 1165 | +0.198 | +869.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 1165 | +0.198 | +869.33€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 1345 | +0.161 | +865.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 1345 | +0.161 | +865.52€ | 0 | 28 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 1143 | +0.213 | +922.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 1143 | +0.213 | +922.27€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 1287 | +0.144 | +748.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 1287 | +0.144 | +748.82€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 1473 | +0.103 | +754.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 1473 | +0.103 | +754.70€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 1854 | +0.200 | +1419.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 1854 | +0.200 | +1419.13€ | 0 | 22 |
| ✅ GBM_LATE_5M | 2488 | +0.127 | +1119.66€ | 1 | 22 |
| ✅ GBM_LATE_5M#5min | 2488 | +0.127 | +1119.66€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 95 | +0.222 | +72.24€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 95 | +0.222 | +72.24€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 863 | +0.125 | +427.92€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 863 | +0.125 | +427.92€ | 2 | 15 |
| ✅ GBM_LATE_5M#DOGE | 273 | +0.158 | +149.74€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 273 | +0.158 | +149.74€ | 0 | 13 |
| ✅ GBM_LATE_5M#ETH | 783 | +0.134 | +343.67€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 783 | +0.134 | +343.67€ | 0 | 27 |
| ✅ GBM_LATE_5M#SOL | 126 | -0.023 | -1.19€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 126 | -0.023 | -1.19€ | 4 | 0 |
| ✅ GBM_LATE_5M#XRP | 348 | +0.114 | +127.28€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 348 | +0.114 | +127.28€ | 0 | 0 |
| ✅ GBM_LATE_60M | 544 | -0.017 | +114.45€ | 5 | 12 |
| ✅ GBM_LATE_60M#60min | 544 | -0.017 | +114.45€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 187 | +0.018 | +11.67€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 187 | +0.018 | +11.67€ | 2 | 5 |
| ✅ GBM_LATE_60M#ETH | 197 | +0.023 | +75.91€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 197 | +0.023 | +75.91€ | 2 | 9 |
| ✅ GBM_LATE_60M#SOL | 160 | -0.105 | +26.87€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 160 | -0.105 | +26.87€ | 2 | 1 |
| 🚫 GBM_LATE_60M_FADE | 195 | -0.302 | -33.28€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 195 | -0.302 | -33.28€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 77 | -0.260 | -7.87€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 77 | -0.260 | -7.87€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 65 | -0.351 | -19.05€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 65 | -0.351 | -19.05€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 53 | -0.282 | -6.35€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 53 | -0.282 | -6.35€ | 4 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 352 | +0.040 | +2.35€ | 2 | 5 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 352 | +0.040 | +2.35€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 146 | +0.027 | +7.39€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 146 | +0.027 | +7.39€ | 3 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 89 | +0.071 | -0.57€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 89 | +0.071 | -0.57€ | 0 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 117 | +0.029 | -4.47€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 117 | +0.029 | -4.47€ | 0 | 5 |
| ✅ LATE_WINDOW_5MIN | 25 | +0.278 | +10.54€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 25 | +0.278 | +10.54€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 25 | +0.278 | +10.54€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 25 | +0.278 | +10.54€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 341 | +0.106 | +93.18€ | 0 | 3 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 341 | +0.106 | +93.18€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 341 | +0.106 | +93.18€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 341 | +0.106 | +93.18€ | 0 | 3 |
| ✅ LIQUIDACIONES_15M | 244 | -0.098 | -29.25€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 244 | -0.098 | -29.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 60 | -0.081 | -6.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 60 | -0.081 | -6.52€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 23 | -0.180 | -4.83€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 23 | -0.180 | -4.83€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 49 | -0.088 | -6.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 49 | -0.088 | -6.46€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 59 | +0.008 | +0.13€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 59 | +0.008 | +0.13€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 48 | -0.180 | -9.97€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 48 | -0.180 | -9.97€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 822 | -0.015 | -15.29€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 822 | -0.015 | -15.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 50 | +0.019 | -1.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 50 | +0.019 | -1.14€ | 0 | 1 |
| ✅ LIQUIDACIONES_5M#BTC | 123 | -0.044 | -5.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 123 | -0.044 | -5.35€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 68 | -0.100 | -7.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 68 | -0.100 | -7.86€ | 2 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 231 | +0.024 | +9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 231 | +0.024 | +9.92€ | 3 | 1 |
| ✅ LIQUIDACIONES_5M#SOL | 291 | +0.002 | -3.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 291 | +0.002 | -3.75€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 59 | -0.107 | -7.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 59 | -0.107 | -7.11€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M | 477 | -0.007 | -1.90€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 477 | -0.007 | -1.90€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 151 | -0.036 | -10.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 151 | -0.036 | -10.11€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 145 | +0.003 | +2.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 145 | +0.003 | +2.06€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 181 | +0.008 | +6.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 181 | +0.008 | +6.15€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 4978 | -0.002 | -78.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 4978 | -0.002 | -78.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 523 | -0.005 | +1.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 523 | -0.005 | +1.93€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 599 | +0.004 | -9.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 599 | +0.004 | -9.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 933 | -0.004 | -25.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 933 | -0.004 | -25.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 1084 | +0.011 | +16.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 1084 | +0.011 | +16.15€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 925 | -0.008 | -31.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 925 | -0.008 | -31.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 914 | -0.013 | -30.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 914 | -0.013 | -30.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 7906 | -0.036 | +176.88€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 7906 | -0.036 | +176.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 1260 | -0.032 | +129.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 1260 | -0.032 | +129.39€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 1371 | -0.031 | -14.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 1371 | -0.031 | -14.74€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 1269 | -0.047 | +80.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 1269 | -0.047 | +80.06€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 1398 | -0.034 | -33.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 1398 | -0.034 | -33.51€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 1313 | -0.041 | +32.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 1313 | -0.041 | +32.55€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 1295 | -0.034 | -16.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 1295 | -0.034 | -16.87€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 556 | -0.061 | -42.52€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 556 | -0.061 | -42.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 104 | -0.038 | -5.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 104 | -0.038 | -5.15€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 67 | -0.065 | -5.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 67 | -0.065 | -5.01€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 36 | -0.105 | -4.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 36 | -0.105 | -4.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 108 | -0.118 | -14.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 108 | -0.118 | -14.05€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 140 | -0.028 | -6.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 140 | -0.028 | -6.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 101 | -0.044 | -7.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 101 | -0.044 | -7.92€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M | 3170 | +0.004 | -5.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3170 | +0.004 | -5.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 126 | -0.039 | -1.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 126 | -0.039 | -1.34€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 185 | +0.008 | -2.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 185 | +0.008 | -2.27€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 136 | +0.000 | -1.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 136 | +0.000 | -1.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1160 | +0.008 | +7.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1160 | +0.008 | +7.79€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1385 | +0.006 | -2.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1385 | +0.006 | -2.03€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 178 | -0.006 | -5.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 178 | -0.006 | -5.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 21954 | -0.076 | +395.98€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 21954 | -0.076 | +395.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 3433 | -0.089 | +413.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 3433 | -0.089 | +413.39€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 3806 | -0.068 | -47.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 3806 | -0.068 | -47.52€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 3555 | -0.083 | +65.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 3555 | -0.083 | +65.03€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 3323 | -0.097 | -171.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 3323 | -0.097 | -171.62€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 4149 | -0.050 | +39.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 4149 | -0.050 | +39.28€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 3688 | -0.077 | +97.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 3688 | -0.077 | +97.42€ | 7 | 0 |
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
| ✅ ORDER_FLOW_5M | 516 | +0.093 | +123.64€ | 1 | 3 |
| ✅ ORDER_FLOW_5M#5min | 380 | +0.105 | +111.05€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 103 | +0.119 | +42.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 103 | +0.119 | +42.48€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#DOGE | 72 | +0.095 | +15.72€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 72 | +0.095 | +15.72€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#ETH | 63 | +0.100 | +17.40€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 63 | +0.100 | +17.40€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 62 | +0.141 | +26.22€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 62 | +0.141 | +26.22€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 80 | +0.061 | +9.23€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 80 | +0.061 | +9.23€ | 0 | 3 |
| ✅ PRICE_TARGET_GBM | 268 | -0.159 | -23.41€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC | 120 | -0.238 | -35.09€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC#atexpiry | 105 | -0.266 | -34.36€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 15 | -0.022 | -0.74€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 101 | -0.131 | -3.37€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 82 | -0.143 | -6.34€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 19 | -0.068 | +2.97€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 47 | -0.010 | +15.05€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 40 | +0.000 | +14.48€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 7 | -0.019 | +0.57€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 227 | -0.177 | -26.22€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 41 | -0.058 | +2.80€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE | 209 | -0.187 | +19.09€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 85 | -0.098 | +17.95€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 83 | -0.088 | +18.97€ | 0 | 3 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 84 | -0.279 | -16.66€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 80 | -0.281 | -18.05€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 40 | -0.167 | +17.79€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 38 | -0.150 | +19.63€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#atexpiry | 201 | -0.180 | +20.56€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#reach | 8 | -0.120 | -1.47€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 73 | +0.327 | +17.70€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC | 17 | -0.022 | -2.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 17 | -0.022 | -2.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 20 | +0.318 | +2.90€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 20 | +0.318 | +2.90€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 36 | +0.474 | +17.74€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 36 | +0.474 | +17.74€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#sniper | 73 | +0.327 | +17.70€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 170 | +0.023 | +0.18€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 170 | +0.023 | +0.18€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 71 | +0.007 | -3.58€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 71 | +0.007 | -3.58€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 10 | +0.000 | -0.13€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 10 | +0.000 | -0.13€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 17 | +0.112 | +3.15€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 17 | +0.112 | +3.15€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP | 72 | +0.013 | +0.74€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 72 | +0.013 | +0.74€ | 1 | 0 |
| ✅ STREAK_FADE_5M | 1229 | -0.021 | -56.05€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 1229 | -0.021 | -56.05€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 405 | -0.018 | -13.68€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 405 | -0.018 | -13.68€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 449 | -0.005 | -11.72€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 449 | -0.005 | -11.72€ | 3 | 0 |
| ✅ STREAK_FADE_5M#SOL | 132 | -0.037 | -12.47€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 132 | -0.037 | -12.47€ | 2 | 0 |
| ✅ STREAK_FADE_5M#XRP | 243 | -0.047 | -18.19€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 243 | -0.047 | -18.19€ | 4 | 0 |
| ✅ STREAK_FADE_60M | 34 | +0.000 | -0.62€ | 0 | 0 |
| ✅ STREAK_FADE_60M#60min | 34 | +0.000 | -0.62€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 20 | -0.091 | -2.33€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 20 | -0.091 | -2.33€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 14 | +0.087 | +1.71€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 14 | +0.087 | +1.71€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 2585 | +0.030 | +60.56€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 2585 | +0.030 | +60.56€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 861 | +0.033 | +17.41€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 861 | +0.033 | +17.41€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 489 | +0.025 | +11.59€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 489 | +0.025 | +11.59€ | 1 | 1 |
| ✅ STREAK_MOM_5M#SOL | 764 | +0.027 | +9.58€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 764 | +0.027 | +9.58€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 471 | +0.035 | +21.98€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 471 | +0.035 | +21.98€ | 2 | 1 |
| ✅ STRUCT_NO_15M | 3323 | +0.011 | -22.81€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 3323 | +0.011 | -22.81€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 1278 | +0.013 | -7.79€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 1278 | +0.013 | -7.79€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 1300 | +0.018 | +0.00€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 1300 | +0.018 | +0.00€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 745 | -0.005 | -15.02€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 745 | -0.005 | -15.02€ | 2 | 0 |
| ✅ UPDOWN_GBM | 6884 | +0.003 | +132.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 2452 | +0.041 | +226.32€ | 0 | 8 |
| ✅ UPDOWN_GBM#240min | 279 | +0.009 | -1.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 3696 | -0.018 | -83.36€ | 3 | 0 |
| ✅ UPDOWN_GBM#60min | 410 | -0.010 | -8.19€ | 3 | 0 |
| ✅ UPDOWN_GBM#BNB | 196 | +0.091 | +38.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 179 | +0.119 | +42.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 8 | -0.040 | -1.01€ | 0 | 0 |
| 🚫 UPDOWN_GBM#BNB#5min | 9 | -0.102 | -2.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 1562 | +0.011 | +59.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 244 | +0.073 | +39.80€ | 5 | 12 |
| ✅ UPDOWN_GBM#BTC#240min | 82 | +0.048 | +4.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 1087 | +0.002 | +20.07€ | 3 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 131 | -0.034 | -6.65€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 826 | -0.005 | -1.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 123 | +0.100 | +28.45€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 9 | +0.021 | +0.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 694 | -0.024 | -30.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 1657 | -0.002 | -7.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 731 | +0.021 | +16.64€ | 1 | 4 |
| ✅ UPDOWN_GBM#ETH#240min | 81 | +0.054 | +3.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 647 | -0.033 | -28.44€ | 4 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 183 | +0.013 | +1.19€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 1690 | -0.010 | -25.14€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 588 | -0.003 | -5.44€ | 1 | 2 |
| ✅ UPDOWN_GBM#SOL#240min | 66 | +0.000 | -2.33€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 928 | -0.011 | -14.52€ | 4 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 96 | -0.020 | -2.73€ | 2 | 2 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 951 | +0.010 | +70.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 587 | +0.059 | +104.71€ | 0 | 7 |
| ✅ UPDOWN_GBM#XRP#240min | 33 | -0.157 | -6.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 331 | -0.059 | -27.77€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 220 | +0.311 | +42.59€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 220 | +0.311 | +42.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 125 | +0.287 | +13.42€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 125 | +0.287 | +13.42€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 95 | +0.335 | +29.18€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 95 | +0.335 | +29.18€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 4256 | -0.074 | +856.84€ | 4 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 4256 | -0.074 | +856.84€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 303 | -0.051 | +341.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 303 | -0.051 | +341.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 866 | -0.165 | -100.84€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 866 | -0.165 | -100.84€ | 5 | 2 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 78 | +0.062 | +12.88€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 78 | +0.062 | +12.88€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 346 | +0.141 | +164.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 346 | +0.141 | +164.70€ | 2 | 15 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 1372 | -0.069 | +234.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 1372 | -0.069 | +234.11€ | 4 | 4 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 1291 | -0.089 | +204.76€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 1291 | -0.089 | +204.76€ | 4 | 2 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 33 | -0.014 | -2.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 33 | -0.014 | -2.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 33 | -0.014 | -2.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 33 | -0.014 | -2.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 348 | +0.280 | +262.78€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 348 | +0.280 | +262.78€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 196 | +0.268 | +140.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 196 | +0.268 | +140.05€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 152 | +0.292 | +122.73€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 152 | +0.292 | +122.73€ | 0 | 11 |
| ✅ UPDOWN_OU_5M | 537 | -0.084 | -54.58€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#5min | 537 | -0.084 | -54.58€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 284 | -0.063 | -28.78€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 284 | -0.063 | -28.78€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 114 | -0.009 | -0.75€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 114 | -0.009 | -0.75€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 30 | -0.188 | -6.21€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 30 | -0.188 | -6.21€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 41 | -0.151 | -5.75€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 41 | -0.151 | -5.75€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 37 | -0.192 | -6.28€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 37 | -0.192 | -6.28€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 31 | -0.197 | -6.80€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 31 | -0.197 | -6.80€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 1134 | +0.290 | +476.00€ | 0 | 5 |
| ✅ WEEKLY_PRICE#BTC | 342 | +0.209 | +2.62€ | 0 | 2 |
| ✅ WEEKLY_PRICE#ETH | 359 | +0.265 | +92.97€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 433 | +0.371 | +380.41€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.081) — sin ventaja clara. oversold(IBS<0.3): IC=+0.019 n=2455 | neutral: IC=-0.001 n=2630 | overbought(IBS>0.7): IC=+0.080 n=2710
  - _Datos_: n=8130 IC=+0.034 PNL=+712.51€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: (cache 790s) 31 celda(s) GATE OK de 2182 trackeadas

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=-0.003 < 0.08 — monitorear
  - _Datos_: n=588 IC=-0.003 PNL=-5.44€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=359/15 IC=+0.265 PNL=+92.97€ | BTC: n=342/15 IC=+0.209 PNL=+2.62€ | SOL: n=433/15 IC=+0.371 PNL=+380.41€

**🟡 H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.074 n=110977 | tras_1loss IC=+0.045 n=86733 | tras_2loss IC=+0.008 n=39361/40 | gap=+0.066 (umbral 0.05)

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
  - _Estado_: 6822 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.104 n=46/60 | contraria IC=+0.018 n=25 | gap=+0.086 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=87, boost estimado=+0.002. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 62 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=183/40 IC=+0.013 PNL=+1.19€ | BTC#60min: n=131/40 IC=-0.034 PNL=-6.65€ | SOL#60min: n=96/40 IC=-0.020 PNL=-2.73€

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=-0.012 n=750 | contrario_BTC IC=-0.022 n=573/40 | gap=-0.010 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.184 > 0.08 con n=74 PNL=+44.34€
  - _Datos_: n=74 IC=+0.184 PNL=+44.34€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.139 > 0.08 con n=95 PNL=+26.15€
  - _Datos_: n=95 IC=+0.139 PNL=+26.15€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.333 > 0.1 con n=962 PNL=+478.54€
  - _Datos_: n=962 IC=+0.333 PNL=+478.54€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=62 IC=+0.031 PNL=+10.83€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=62 IC=+0.031 PNL=+10.83€

**⏳ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: 30
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: 17/30 ops en el filtro definido (IC actual=+0.157 PNL=+9.40€)
  - _Datos_: n=17 IC=+0.157 PNL=+9.40€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=6620 IC=-0.001 PNL=+80.98€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=6620 IC=-0.001 PNL=+80.98€

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
  - _Estado_: n=337 IC=+0.004 PNL=-2.01€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=337 IC=+0.004 PNL=-2.01€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=73 IC=-0.073 PNL=-6.17€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=73 IC=-0.073 PNL=-6.17€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=116 IC=-0.076 PNL=-9.41€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=116 IC=-0.076 PNL=-9.41€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.115 > 0.1 con n=523 PNL=+121.39€
  - _Datos_: n=523 IC=+0.115 PNL=+121.39€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=187 IC=+0.077 PNL=+40.75€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=187 IC=+0.077 PNL=+40.75€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=244 IC=+0.073 PNL=+39.80€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=244 IC=+0.073 PNL=+39.80€

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
  - _Estado_: n=1422 IC=+0.024 PNL=+79.50€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1422 IC=+0.024 PNL=+79.50€

**⏳ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: 26/30 ops en el filtro definido (IC actual=-0.214 PNL=-5.03€)
  - _Datos_: n=26 IC=-0.214 PNL=-5.03€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=79 IC=-0.018 PNL=+8.79€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=79 IC=-0.018 PNL=+8.79€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=93 IC=+0.037 PNL=+8.60€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=93 IC=+0.037 PNL=+8.60€

**⏳ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: 15
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: 6/15 ops en el filtro definido (IC actual=+0.037 PNL=+1.09€)
  - _Datos_: n=6 IC=+0.037 PNL=+1.09€

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=2287 IC=-0.022 PNL=-59.11€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2287 IC=-0.022 PNL=-59.11€

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
  - _Estado_: 25/30 ops en el filtro definido (IC actual=+0.278 PNL=+10.54€)
  - _Datos_: n=25 IC=+0.278 PNL=+10.54€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=1797 IC=+0.020 PNL=+96.01€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1797 IC=+0.020 PNL=+96.01€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=465 IC=+0.037 PNL=+2.90€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=465 IC=+0.037 PNL=+2.90€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.093 > 0.08 con n=133 PNL=+25.90€
  - _Datos_: n=133 IC=+0.093 PNL=+25.90€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.136 > 0.08 con n=127 PNL=+3.86€
  - _Datos_: n=127 IC=+0.136 PNL=+3.86€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.123 > 0.08 con n=120 PNL=+38.35€
  - _Datos_: n=120 IC=+0.123 PNL=+38.35€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=19551 IC=+0.100 PNL=+5810.63€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=19551 IC=+0.100 PNL=+5810.63€

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
  - _Estado_: n=899 IC=+0.027 PNL=+47.49€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=899 IC=+0.027 PNL=+47.49€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.112 > 0.02 con n=279 PNL=+73.75€
  - _Datos_: n=279 IC=+0.112 PNL=+73.75€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.443 > 0.1 con n=612 PNL=+523.69€
  - _Datos_: n=612 IC=+0.443 PNL=+523.69€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=1628 IC=+0.017 PNL=+71.06€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=1628 IC=+0.017 PNL=+71.06€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.165 > 0.1 con n=797 PNL=+290.48€
  - _Datos_: n=797 IC=+0.165 PNL=+290.48€

**⏳ H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: 40
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: 32/40 ops en el filtro definido (IC actual=-0.235 PNL=-5.42€)
  - _Datos_: n=32 IC=-0.235 PNL=-5.42€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=450 IC=+0.046 PNL=+62.10€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=450 IC=+0.046 PNL=+62.10€

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
  - _Estado_: n=70 IC=+0.056 PNL=+1.65€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=70 IC=+0.056 PNL=+1.65€

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
  - _Estado_: n=5178 IC=-0.146 PNL=+182.46€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=5178 IC=-0.146 PNL=+182.46€

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
  - _Estado_: n=666 IC=+0.144 PNL=+294.77€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=666 IC=+0.144 PNL=+294.77€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.115 > 0.08 con n=523 PNL=+121.39€
  - _Datos_: n=523 IC=+0.115 PNL=+121.39€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=725 IC=-0.001 PNL=-1.08€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=725 IC=-0.001 PNL=-1.08€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.084 > 0.08 con n=697 PNL=+361.41€
  - _Datos_: n=697 IC=+0.084 PNL=+361.41€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.156 > 0.08 con n=152 PNL=+46.12€
  - _Datos_: n=152 IC=+0.156 PNL=+46.12€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.240 < -0.1 con n=582 PNL=-79.18€
  - _Datos_: n=582 IC=-0.240 PNL=-79.18€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=1378 IC=+0.127 PNL=+691.27€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=1378 IC=+0.127 PNL=+691.27€

**⏳ H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: 40
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: 32/40 ops en el filtro definido (IC actual=+0.059 PNL=+3.73€)
  - _Datos_: n=32 IC=+0.059 PNL=+3.73€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=724 IC=-0.029 PNL=+39.82€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=724 IC=-0.029 PNL=+39.82€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.180 > 0.08 con n=629 PNL=+375.44€
  - _Datos_: n=629 IC=+0.180 PNL=+375.44€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=1059 IC=-0.063 PNL=+141.47€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1059 IC=-0.063 PNL=+141.47€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.115 > 0.08 con n=273 PNL=-38.79€
  - _Datos_: n=273 IC=+0.115 PNL=-38.79€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.236 > 0.08 con n=1561 PNL=-150.79€
  - _Datos_: n=1561 IC=+0.236 PNL=-150.79€

**⏳ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: 11/40 ops en el filtro definido (IC actual=-0.021 PNL=+0.98€)
  - _Datos_: n=11 IC=-0.021 PNL=+0.98€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.117 n=178) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=178 IC=+0.117 PNL=+50.22€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.357 > 0.08 con n=75 PNL=+51.31€
  - _Datos_: n=75 IC=+0.357 PNL=+51.31€

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.429 n=237) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=237 IC=+0.429 PNL=+320.82€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=3372 IC=+0.131 PNL=-598.77€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=3372 IC=+0.131 PNL=-598.77€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.182 > 0.1 con n=42 PNL=+22.66€
  - _Datos_: n=42 IC=+0.182 PNL=+22.66€
