# Hipótesis automáticas — 2026-08-18 02:56 UTC
_Generado por shadow_postmortem.py sobre 57600 resoluciones (PNL=+6162.06€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.355` → IC=-0.143 (n=68)

  - _Acción_: SKIP cuando `py_entrada` < 0.355
  - _Potencial_: sin este filtro IC_bueno=+0.173 (n=145)

- **FILTRO** `banda_hit_calibrado` < `0.6142` → IC=-0.227 (n=53)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.6142
  - _Potencial_: sin este filtro IC_bueno=+0.173 (n=160)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.377 (n=63)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.142 (n=205)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.230 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.072)

- **PATRÓN** `n_total_lado` > `74.0` → IC=+0.196 (n=54)

  - _Acción_: Kelly boost +0.98€ cuando `n_total_lado` > 74.0 (IC base=+0.072)

- **PATRÓN** `banda_hit_calibrado` > `0.6142` → IC=+0.173 (n=160)

  - _Acción_: Kelly boost +0.86€ cuando `banda_hit_calibrado` > 0.6142 (IC base=+0.072)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.142 (n=205)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.5 (IC base=+0.018)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `banda_hit_calibrado` < `0.6142` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.6142
  - _Potencial_: sin este filtro IC_bueno=+0.191 (n=82)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.338 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.122 (n=109)

- **PATRÓN** `py_entrada` > `0.705` → IC=+0.242 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.705 (IC base=+0.091)

- **PATRÓN** `n_total_lado` > `94.0` → IC=+0.259 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 94.0 (IC base=+0.091)

- **PATRÓN** `banda_hit_calibrado` > `0.6142` → IC=+0.191 (n=82)

  - _Acción_: Kelly boost +0.95€ cuando `banda_hit_calibrado` > 0.6142 (IC base=+0.091)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.122 (n=109)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.495 (IC base=+0.007)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.278 (n=25)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=80)

- **FILTRO** `banda_hit_calibrado` < `0.6242` → IC=-0.227 (n=31)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.6242
  - _Potencial_: sin este filtro IC_bueno=+0.171 (n=74)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=81)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.353 (n=32)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=68)

- **FILTRO** `n_ballena_banda` < `30.0` → IC=-0.128 (n=49)

  - _Acción_: SKIP cuando `n_ballena_banda` < 30.0
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=51)

- **FILTRO** `hora_utc` < `11.0` → IC=-0.125 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=70)

- **PATRÓN** `py_entrada` > `0.33` → IC=+0.159 (n=80)

  - _Acción_: Kelly boost +0.79€ cuando `py_entrada` > 0.33 (IC base=+0.051)

- **PATRÓN** `banda_hit_calibrado` > `0.6242` → IC=+0.171 (n=74)

  - _Acción_: Kelly boost +0.86€ cuando `banda_hit_calibrado` > 0.6242 (IC base=+0.051)

- **PATRÓN** `banda_z` > `6.715` → IC=+0.136 (n=53)

  - _Acción_: Kelly boost +0.68€ cuando `banda_z` > 6.715 (IC base=+0.051)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.143 (n=68)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.495 (IC base=-0.020)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `141.54` → IC=-0.274 (n=755)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 141.54
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=2267)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `112.74` → IC=-0.398 (n=86)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 112.74
  - _Potencial_: sin este filtro IC_bueno=-0.124 (n=259)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` > `638.05` → IC=-0.278 (n=106)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` > 638.05
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=321)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `92.72` → IC=-0.478 (n=137)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 92.72
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=138)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `242.1` → IC=-0.171 (n=503)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 242.1
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=168)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `138.38` → IC=-0.214 (n=180)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 138.38
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=543)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `176.29` → IC=-0.251 (n=191)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 176.29
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=390)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.7` → IC=+0.201 (n=2020)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.7 (IC base=+0.094)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.161 (n=1129)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.094)

- **PATRÓN** `libro_liquidez` > `2373.5135` → IC=+0.164 (n=1093)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2373.5135 (IC base=+0.094)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.150 (n=3520)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 7.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.149 (n=2585)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 11.0 (IC base=+0.146)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.287 (n=1283)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.186 (n=1935)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.02 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `4025.563` → IC=+0.174 (n=781)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 4025.563 (IC base=+0.146)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.227 (n=119)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` > `0.775` → IC=+0.349 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.775 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.196 (n=429)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.01 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.222 (n=289)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.338 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.194 (n=406)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.01 (IC base=+0.193)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.141 (n=382)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.159 (n=329)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 15.0 (IC base=+0.131)

- **PATRÓN** `py_entrada` > `0.6` → IC=+0.169 (n=176)

  - _Acción_: Kelly boost +0.84€ cuando `py_entrada` > 0.6 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `5033.4098` → IC=+0.165 (n=195)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 5033.4098 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.212 (n=158)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.144)

- **PATRÓN** `py_entrada` < `0.395` → IC=+0.229 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.395 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `5342.6568` → IC=+0.170 (n=201)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 5342.6568 (IC base=+0.144)

### FAVORITO_CONFIRMADO#ETH#15min
- **PATRÓN** `hora_utc` < `12.0` → IC=+0.139 (n=463)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 12.0 (IC base=+0.111)

- **PATRÓN** `py_entrada` > `0.7` → IC=+0.296 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.7 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.309 (n=250)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.291)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.297 (n=249)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.291)

- **PATRÓN** `py_entrada` < `0.195` → IC=+0.427 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.195 (IC base=+0.291)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.295 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `3334.5877` → IC=+0.354 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3334.5877 (IC base=+0.291)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.146 (n=278)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.167 (n=244)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 16.0 (IC base=+0.141)

- **PATRÓN** `py_entrada` > `0.655` → IC=+0.232 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.655 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.146 (n=269)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `2188.8928` → IC=+0.162 (n=267)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2188.8928 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `5697.4897` → IC=+0.190 (n=69)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 5697.4897 (IC base=+0.099)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.179 (n=540)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.187 (n=362)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 12.0 (IC base=+0.172)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.405 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.270 (n=111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.234 (n=156)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.234)

- **PATRÓN** `py_entrada` < `0.37` → IC=+0.314 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.37 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.253 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `913.222` → IC=+0.240 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 913.222 (IC base=+0.234)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `19.0` → IC=+0.253 (n=75)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 19.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.195 (n=149)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 13.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.340 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.195 (n=198)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.03 (IC base=+0.189)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.227 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.106)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.158 (n=255)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.02 (IC base=+0.106)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.85` → IC=-0.400 (n=28)

  - _Acción_: SKIP cuando `py_entrada` > 0.85
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=91)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.196 (n=1108)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 7.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.185 (n=927)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` < 0.7 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.203 (n=869)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `3268.7028` → IC=+0.348 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3268.7028 (IC base=+0.181)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.168 (n=562)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 15.0 (IC base=+0.158)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.180 (n=573)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.73 (IC base=+0.158)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `py_entrada` > `0.795` → IC=-0.393 (n=26)

  - _Acción_: SKIP cuando `py_entrada` > 0.795
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=15)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.417 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.326)

- **PATRÓN** `py_entrada` > `0.835` → IC=+0.370 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.835 (IC base=+0.326)

- **PATRÓN** `libro_liquidez` > `2916.5858` → IC=+0.343 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2916.5858 (IC base=+0.326)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.159 (n=640)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 5.0 (IC base=+0.157)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.179 (n=275)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 7.0 (IC base=+0.157)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.194 (n=217)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.7 (IC base=+0.157)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.157 (n=351)

  - _Acción_: Kelly boost +0.79€ cuando `py_entrada` > 0.73 (IC base=+0.157)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.232 (n=487)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.307 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.219)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min
- **FILTRO** `hora_utc` > `12.0` → IC=-0.250 (n=38)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=40)

- **FILTRO** `py_entrada` > `0.755` → IC=-0.267 (n=58)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=20)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.202 (n=213)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.199 (n=260)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 7.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.206 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.7 (IC base=+0.178)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.435 (n=106)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.412)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.415 (n=104)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.412)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.418 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.412)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.452 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.412)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.409 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.412)

- **PATRÓN** `libro_liquidez` > `3355.2252` → IC=+0.429 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3355.2252 (IC base=+0.412)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `12.0` → IC=+0.412 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.415)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.425 (n=38)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.415)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.429 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.415)

- **PATRÓN** `libro_liquidez` > `6307.444` → IC=+0.409 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6307.444 (IC base=+0.415)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.407 (n=41)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.371)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.380 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.371)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.382 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.371)

- **PATRÓN** `libro_liquidez` > `2004.8341` → IC=+0.384 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2004.8341 (IC base=+0.371)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `py_entrada` < `0.925` → IC=+0.409 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.925 (IC base=+0.425)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.413 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.425)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.204 (n=1422)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.194 (n=1375)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 5.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.227 (n=2700)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.189)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `py_entrada` > `0.73` → IC=+0.130 (n=341)

  - _Acción_: Kelly boost +0.65€ cuando `py_entrada` > 0.73 (IC base=+0.095)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.294 (n=285)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.251)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.257 (n=212)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.251)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.328 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.251)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.149 (n=334)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 15.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.151 (n=325)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 7.0 (IC base=+0.144)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.213 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.144)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.241 (n=311)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.297 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.261 (n=220)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.247)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.250 (n=206)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.247)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.284 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.247)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.255 (n=231)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.207 (n=230)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.255 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.37` → IC=+0.225 (n=533)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.37 (IC base=+0.151)

- **PATRÓN** `restante_min` < `3.77` → IC=+0.170 (n=462)

  - _Acción_: Kelly boost +0.85€ cuando `restante_min` < 3.77 (IC base=+0.151)

- **PATRÓN** `restante_min` > `4.91` → IC=+0.196 (n=475)

  - _Acción_: Kelly boost +0.98€ cuando `restante_min` > 4.91 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.157 (n=1408)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.159 (n=1386)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 17.0 (IC base=+0.151)

- **PATRÓN** `lag_apertura_s` < `5.45` → IC=+0.205 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `lag_apertura_s` < 5.45 (IC base=+0.151)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.37` → IC=+0.238 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.37 (IC base=+0.154)

- **PATRÓN** `restante_min` < `3.71` → IC=+0.184 (n=229)

  - _Acción_: Kelly boost +0.92€ cuando `restante_min` < 3.71 (IC base=+0.154)

- **PATRÓN** `restante_min` > `4.88` → IC=+0.189 (n=242)

  - _Acción_: Kelly boost +0.94€ cuando `restante_min` > 4.88 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=703)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.167 (n=607)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 15.0 (IC base=+0.154)

- **PATRÓN** `lag_apertura_s` < `7.37` → IC=+0.188 (n=229)

  - _Acción_: Kelly boost +0.94€ cuando `lag_apertura_s` < 7.37 (IC base=+0.154)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.206 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.147)

- **PATRÓN** `restante_min` < `3.87` → IC=+0.148 (n=231)

  - _Acción_: Kelly boost +0.74€ cuando `restante_min` < 3.87 (IC base=+0.147)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.212 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `restante_min` > 4.95 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.153 (n=630)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 7.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.160 (n=697)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 17.0 (IC base=+0.147)

- **PATRÓN** `lag_apertura_s` < `3.15` → IC=+0.218 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `lag_apertura_s` < 3.15 (IC base=+0.147)

- **PATRÓN** `profundidad_ratio_no` > `14.9` → IC=+0.190 (n=230)

  - _Acción_: Kelly boost +0.95€ cuando `profundidad_ratio_no` > 14.9 (IC base=+0.147)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.305 (n=413)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.295)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.306 (n=406)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.295)

- **PATRÓN** `py_entrada` > `0.825` → IC=+0.379 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.825 (IC base=+0.295)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.277 (n=173)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.268)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.277 (n=168)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.268)

- **PATRÓN** `py_entrada` < `0.725` → IC=+0.280 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.725 (IC base=+0.268)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.344 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.268)

- **PATRÓN** `libro_liquidez` > `3894.3849` → IC=+0.277 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3894.3849 (IC base=+0.268)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.307 (n=190)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.295)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.309 (n=187)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.295)

- **PATRÓN** `py_entrada` > `0.81` → IC=+0.391 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.81 (IC base=+0.295)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.303 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.295)

- **PATRÓN** `libro_liquidez` > `1876.0591` → IC=+0.315 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1876.0591 (IC base=+0.295)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` < `13.0` → IC=+0.444 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 13.0 (IC base=+0.371)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.409 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.371)

- **PATRÓN** `libro_liquidez` > `943.1727` → IC=+0.372 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 943.1727 (IC base=+0.371)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.404 (n=164)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.405)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.429 (n=166)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.405)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.407 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.405)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.427 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.405)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.402 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.405)

- **PATRÓN** `libro_liquidez` > `2158.1237` → IC=+0.413 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2158.1237 (IC base=+0.405)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.396 (n=75)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.400)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.437 (n=77)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.400)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.411 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.400)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.417 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.400)

- **PATRÓN** `libro_liquidez` > `5722.415` → IC=+0.426 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5722.415 (IC base=+0.400)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.407 (n=73)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.408)

- **PATRÓN** `hora_utc` < `19.0` → IC=+0.416 (n=81)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 19.0 (IC base=+0.408)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.409 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.408)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.423 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.408)

- **PATRÓN** `libro_liquidez` > `1842.491` → IC=+0.432 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1842.491 (IC base=+0.408)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.285 (n=128)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.255)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.418 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.255)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.275 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.255)

- **PATRÓN** `libro_liquidez` > `1406.0028` → IC=+0.303 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1406.0028 (IC base=+0.255)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.285 (n=128)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.255)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.418 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.255)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.275 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.255)

- **PATRÓN** `libro_liquidez` > `1406.0028` → IC=+0.303 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1406.0028 (IC base=+0.255)

### GBM_LATE_15M
- **PATRÓN** `hora_utc` < `6.0` → IC=+0.146 (n=393)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 6.0 (IC base=+0.107)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.271 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.107)

- **PATRÓN** `dist_vwap_pct` > `0.5843` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5843 (IC base=+0.107)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.896` → IC=+0.241 (n=561)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.896 (IC base=+0.107)

- **PATRÓN** `volumen_regimen` < `1.3474` → IC=+0.218 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.3474 (IC base=+0.107)

- **PATRÓN** `volumen_regimen` > `1.1466` → IC=+0.242 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1466 (IC base=+0.107)

- **PATRÓN** `volumen_pendiente_norm` > `0.3253` → IC=+0.181 (n=89)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.3253 (IC base=+0.107)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.120 (n=1199)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.06 (IC base=+0.107)

- **PATRÓN** `ibs_20min` < `0.6571` → IC=+0.124 (n=2042)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` < 0.6571 (IC base=+0.079)

- **PATRÓN** `volumen_regimen` < `0.6286` → IC=+0.147 (n=151)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.6286 (IC base=+0.079)

- **PATRÓN** `volumen_regimen` > `0.6936` → IC=+0.137 (n=403)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.6936 (IC base=+0.079)

- **PATRÓN** `volumen_pendiente_norm` > `0.3446` → IC=+0.303 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3446 (IC base=+0.079)

- **PATRÓN** `volumen_spike_ratio` < `3.6856` → IC=+0.220 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.6856 (IC base=+0.079)

- **PATRÓN** `volumen_spike_ratio` > `2.8899` → IC=+0.228 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8899 (IC base=+0.079)

- **PATRÓN** `ballena_activa_n` < `138.0` → IC=+0.305 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 138.0 (IC base=+0.079)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.007` → IC=+0.163 (n=170)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.007 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.183 (n=137)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 6.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.299 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.61` → IC=+0.344 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.61 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.2097` → IC=+0.167 (n=58)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2097 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.172 (n=266)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.06 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.310 (n=119)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0061 (IC base=+0.278)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.323 (n=60)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.278)

- **PATRÓN** `drift_60min` |x|≤ `0.2401` → IC=+0.307 (n=179)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2401 (IC base=+0.278)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.282 (n=186)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.278)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.284 (n=183)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.278)

- **PATRÓN** `ibs_20min` < `0.5657` → IC=+0.322 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5657 (IC base=+0.278)

- **PATRÓN** `volumen_pendiente_norm` < `0.0707` → IC=+0.314 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0707 (IC base=+0.278)

- **PATRÓN** `volumen_pendiente_norm` > `0.2422` → IC=+0.308 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2422 (IC base=+0.278)

- **PATRÓN** `volumen_spike_ratio` < `1.8142` → IC=+0.330 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8142 (IC base=+0.278)

- **PATRÓN** `volumen_spike_ratio` > `1.5873` → IC=+0.297 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5873 (IC base=+0.278)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.315 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `1903.96` → IC=+0.283 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1903.96 (IC base=+0.278)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0018` → IC=+0.281 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0018 (IC base=+0.239)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.281 (n=30)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0034 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.302 (n=79)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 9.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` > `0.9174` → IC=+0.271 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9174 (IC base=+0.239)

- **PATRÓN** `dist_vwap_pct` > `0.6292` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6292 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.549` → IC=+0.330 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.549 (IC base=+0.239)

- **PATRÓN** `volumen_regimen` < `0.6834` → IC=+0.312 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6834 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` < `0.1245` → IC=+0.297 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1245 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `2.7036` → IC=+0.303 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.7036 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `11154.7281` → IC=+0.262 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11154.7281 (IC base=+0.239)

- **PATRÓN** `sigma_h` < `0.0018` → IC=+0.167 (n=70)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0018 (IC base=+0.139)

- **PATRÓN** `sigma_h` > `0.0024` → IC=+0.145 (n=139)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` > 0.0024 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.1916` → IC=+0.161 (n=184)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.1916 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.172 (n=199)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 8.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.4388` → IC=+0.216 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4388 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.599` → IC=+0.250 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.599 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `1.2713` → IC=+0.144 (n=209)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.2713 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `0.8408` → IC=+0.167 (n=139)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.8408 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.1281` → IC=+0.276 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1281 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.5117` → IC=+0.263 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5117 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `5196.667` → IC=+0.140 (n=187)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 5196.667 (IC base=+0.139)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0074` → IC=+0.175 (n=112)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0074 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.198 (n=124)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.282 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.165` → IC=+0.287 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.165 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.425` → IC=+0.184 (n=36)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.425 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.150 (n=364)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.06 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `1912.1779` → IC=+0.143 (n=152)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 1912.1779 (IC base=+0.130)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.340 (n=73)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.290)

- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.313 (n=73)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0073 (IC base=+0.290)

- **PATRÓN** `drift_60min` |x|≤ `0.0863` → IC=+0.327 (n=73)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0863 (IC base=+0.290)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.288 (n=229)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.290)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.301 (n=219)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.290)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.318 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5 (IC base=+0.290)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.177` → IC=+0.300 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.177 (IC base=+0.290)

- **PATRÓN** `volumen_pendiente_norm` > `0.3507` → IC=+0.420 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3507 (IC base=+0.290)

- **PATRÓN** `volumen_spike_ratio` < `5.4027` → IC=+0.271 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 5.4027 (IC base=+0.290)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.297 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.290)

- **PATRÓN** `libro_liquidez` > `1878.7584` → IC=+0.297 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1878.7584 (IC base=+0.290)

### GBM_LATE_15M#ETH#15min
- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.159 (n=39)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0034 (IC base=+0.070)

- **PATRÓN** `ibs_20min` > `0.5669` → IC=+0.190 (n=56)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.5669 (IC base=+0.070)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.581` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.581 (IC base=+0.070)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `volumen_pendiente_norm` < `0.0964` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.0964
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

- **FILTRO** `volumen_spike_ratio` > `1.6234` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.6234
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

- **FILTRO** `volumen_spike_ratio` < `2.8678` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 2.8678
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=6)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.152 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0053 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.475` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` < 4.475 (IC base=+0.151)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.151)

### GBM_LATE_15M#XRP#15min
- **PATRÓN** `volumen_regimen` < `0.7863` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.7863 (IC base=+0.002)

- **PATRÓN** `volumen_regimen` < `0.6961` → IC=+0.265 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6961 (IC base=+0.044)

- **PATRÓN** `volumen_regimen` > `1.3677` → IC=+0.218 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.3677 (IC base=+0.044)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `ibs_20min` > `0.9541` → IC=+0.243 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9541 (IC base=+0.058)

- **PATRÓN** `dist_vwap_pct` > `0.1183` → IC=+0.167 (n=145)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1183 (IC base=+0.058)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.315` → IC=+0.130 (n=915)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 2.315 (IC base=+0.058)

- **PATRÓN** `volumen_pendiente_norm` > `0.339` → IC=+0.184 (n=96)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.339 (IC base=+0.058)

- **PATRÓN** `volumen_spike_ratio` > `2.8942` → IC=+0.176 (n=276)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.8942 (IC base=+0.058)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.342 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 30.0 (IC base=+0.058)

- **PATRÓN** `ibs_20min` < `0.1` → IC=+0.168 (n=824)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.1 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` > `0.5125` → IC=+0.321 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5125 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` > `1.0789` → IC=+0.220 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0789 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.3668` → IC=+0.423 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3668 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` > `3.805` → IC=+0.309 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.805 (IC base=+0.049)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `sigma_ewma_delta_pct` > `5.003` → IC=-0.206 (n=100)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.003
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=521)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.449` → IC=+0.164 (n=111)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 3.449 (IC base=-0.012)

- **PATRÓN** `volumen_pendiente_norm` > `0.0487` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.0487 (IC base=-0.012)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `volumen_regimen` < `0.5727` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.5727 (IC base=-0.003)

- **PATRÓN** `volumen_regimen` > `1.1078` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1078 (IC base=-0.003)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0074` → IC=+0.273 (n=108)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0074 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.0643` → IC=+0.182 (n=108)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.0643 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.243 (n=150)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.301 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.123` → IC=+0.306 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.123 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` < `0.1466` → IC=+0.192 (n=225)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.1466 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.4274` → IC=+0.184 (n=36)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.4274 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` < `4.8288` → IC=+0.165 (n=243)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 4.8288 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `2.7873` → IC=+0.195 (n=162)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.7873 (IC base=+0.179)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.233 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `1899.9284` → IC=+0.211 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1899.9284 (IC base=+0.179)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.420 (n=98)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.369)

- **PATRÓN** `drift_60min` |x|≤ `0.1856` → IC=+0.371 (n=99)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1856 (IC base=+0.369)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.387 (n=139)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.369)

- **PATRÓN** `ibs_20min` < `0.3009` → IC=+0.393 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3009 (IC base=+0.369)

- **PATRÓN** `volumen_pendiente_norm` < `0.2257` → IC=+0.385 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2257 (IC base=+0.369)

- **PATRÓN** `volumen_pendiente_norm` > `0.1228` → IC=+0.409 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1228 (IC base=+0.369)

- **PATRÓN** `volumen_spike_ratio` < `2.9702` → IC=+0.449 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.9702 (IC base=+0.369)

- **PATRÓN** `libro_liquidez` > `1854.8646` → IC=+0.422 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1854.8646 (IC base=+0.369)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` < `0.6102` → IC=-0.132 (n=131)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6102
  - _Potencial_: sin este filtro IC_bueno=+0.129 (n=68)

- **FILTRO** `volumen_regimen` > `0.9213` → IC=-0.309 (n=19)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.9213
  - _Potencial_: sin este filtro IC_bueno=-0.109 (n=21)

- **FILTRO** `libro_liquidez` < `8820.0857` → IC=-0.172 (n=65)

  - _Acción_: SKIP cuando `libro_liquidez` < 8820.0857
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=134)

- **FILTRO** `volumen_regimen` > `0.8548` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8548
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=28)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.152 (n=44)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=669)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **PATRÓN** `ibs_20min` > `0.5926` → IC=+0.156 (n=88)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` > 0.5926 (IC base=-0.006)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.268 (n=97)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0065 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.0896` → IC=+0.146 (n=128)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.0896 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.140 (n=109)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.205 (n=110)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `0.9048` → IC=+0.214 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9048 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `0.3099` → IC=+0.190 (n=56)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.3099 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.516` → IC=+0.204 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.516 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` > `0.8047` → IC=+0.158 (n=194)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.8047 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.3135` → IC=+0.203 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3135 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=293)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.289 (n=249)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.280)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.317 (n=129)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.280)

- **PATRÓN** `ibs_20min` < `0.3` → IC=+0.339 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3 (IC base=+0.280)

- **PATRÓN** `dist_vwap_pct` > `0.5827` → IC=+0.357 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5827 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.138` → IC=+0.283 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.138 (IC base=+0.280)

- **PATRÓN** `volumen_regimen` > `0.7044` → IC=+0.304 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7044 (IC base=+0.280)

- **PATRÓN** `volumen_pendiente_norm` > `0.206` → IC=+0.375 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.206 (IC base=+0.280)

- **PATRÓN** `volumen_spike_ratio` > `3.6746` → IC=+0.295 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.6746 (IC base=+0.280)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.149 (n=394)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0047 (IC base=+0.134)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.198 (n=395)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.007 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.145 (n=401)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.149 (n=519)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 7.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` > `0.9206` → IC=+0.251 (n=781)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9206 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` > `0.2194` → IC=+0.148 (n=251)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.2194 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.418` → IC=+0.244 (n=780)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.418 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` > `0.6297` → IC=+0.130 (n=609)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` > 0.6297 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.1136` → IC=+0.159 (n=379)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.1136 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.141 (n=1306)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.06 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `2637.4126` → IC=+0.150 (n=390)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2637.4126 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `124.0` → IC=+0.138 (n=78)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 124.0 (IC base=+0.134)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.227 (n=1117)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0061 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.3035` → IC=+0.228 (n=1117)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3035 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.262 (n=527)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` < `0.3611` → IC=+0.292 (n=1117)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3611 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.805` → IC=+0.243 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.805 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` < `1.2613` → IC=+0.197 (n=866)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 1.2613 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` > `0.8872` → IC=+0.210 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8872 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.1873` → IC=+0.302 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1873 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` < `1.7` → IC=+0.247 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `3.1492` → IC=+0.253 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.1492 (IC base=+0.220)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.163 (n=99)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0058 (IC base=+0.152)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.196 (n=133)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0071 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.212 (n=130)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.325 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.514` → IC=+0.354 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.514 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.2094` → IC=+0.173 (n=47)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2094 (IC base=+0.152)

- **PATRÓN** `libro_spread` < `0.08` → IC=+0.173 (n=316)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.08 (IC base=+0.152)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.279 (n=102)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.282)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.288 (n=116)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.282)

- **PATRÓN** `drift_60min` |x|≤ `0.2252` → IC=+0.317 (n=102)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2252 (IC base=+0.282)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.279 (n=120)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.282)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.307 (n=117)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.282)

- **PATRÓN** `ibs_20min` < `0.0513` → IC=+0.402 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0513 (IC base=+0.282)

- **PATRÓN** `volumen_pendiente_norm` < `0.2802` → IC=+0.304 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2802 (IC base=+0.282)

- **PATRÓN** `volumen_spike_ratio` < `1.8801` → IC=+0.372 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8801 (IC base=+0.282)

- **PATRÓN** `libro_spread` < `0.08` → IC=+0.299 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.08 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `1926.44` → IC=+0.329 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1926.44 (IC base=+0.282)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0018` → IC=+0.258 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0018 (IC base=+0.199)

- **PATRÓN** `sigma_h` > `0.0031` → IC=+0.250 (n=42)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0031 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.278 (n=61)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` > `0.7674` → IC=+0.253 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7674 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` > `0.5406` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5406 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.186` → IC=+0.273 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.186 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `0.6489` → IC=+0.197 (n=31)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.6489 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` > `0.9086` → IC=+0.246 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9086 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.0992` → IC=+0.271 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0992 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `2.5576` → IC=+0.202 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5576 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `1.9813` → IC=+0.227 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9813 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `4929.5343` → IC=+0.226 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4929.5343 (IC base=+0.199)

- **PATRÓN** `sigma_h` < `0.0018` → IC=+0.204 (n=69)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0018 (IC base=+0.195)

- **PATRÓN** `sigma_h` > `0.002` → IC=+0.197 (n=183)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.002 (IC base=+0.195)

- **PATRÓN** `drift_60min` |x|≤ `0.1983` → IC=+0.210 (n=181)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1983 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.259 (n=139)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` < `0.2725` → IC=+0.239 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2725 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.586` → IC=+0.292 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.586 (IC base=+0.195)

- **PATRÓN** `volumen_regimen` < `0.6392` → IC=+0.246 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6392 (IC base=+0.195)

- **PATRÓN** `volumen_regimen` > `0.6986` → IC=+0.197 (n=183)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` > 0.6986 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` < `0.2719` → IC=+0.226 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2719 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.1345` → IC=+0.304 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1345 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` < `1.6337` → IC=+0.283 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6337 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `10758.676` → IC=+0.204 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10758.676 (IC base=+0.195)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.188 (n=91)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0075 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.1483` → IC=+0.169 (n=182)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.1483 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.179 (n=104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 16.0 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.207 (n=97)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.299 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.877` → IC=+0.329 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.877 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` < `0.2317` → IC=+0.130 (n=209)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.2317 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `2.0546` → IC=+0.205 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0546 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `2.7899` → IC=+0.141 (n=140)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 2.7899 (IC base=+0.152)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.208 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `1956.263` → IC=+0.196 (n=90)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 1956.263 (IC base=+0.152)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.326 (n=119)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.318)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.320 (n=120)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0051 (IC base=+0.318)

- **PATRÓN** `drift_60min` |x|≤ `0.1721` → IC=+0.370 (n=90)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1721 (IC base=+0.318)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.325 (n=95)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.318)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.317 (n=129)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.318)

- **PATRÓN** `ibs_20min` < `0.2421` → IC=+0.351 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2421 (IC base=+0.318)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.746` → IC=+0.344 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.746 (IC base=+0.318)

- **PATRÓN** `volumen_pendiente_norm` > `0.3446` → IC=+0.395 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3446 (IC base=+0.318)

- **PATRÓN** `volumen_spike_ratio` < `3.4774` → IC=+0.360 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.4774 (IC base=+0.318)

- **PATRÓN** `volumen_spike_ratio` > `2.1697` → IC=+0.321 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1697 (IC base=+0.318)

- **PATRÓN** `libro_liquidez` > `1869.9762` → IC=+0.372 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1869.9762 (IC base=+0.318)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.002` → IC=+0.315 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.002 (IC base=+0.262)

- **PATRÓN** `sigma_h` > `0.0029` → IC=+0.288 (n=50)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0029 (IC base=+0.262)

- **PATRÓN** `drift_60min` |x|≤ `0.0849` → IC=+0.300 (n=33)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0849 (IC base=+0.262)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.282 (n=76)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.262)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.268 (n=67)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.262)

- **PATRÓN** `ibs_20min` > `0.7754` → IC=+0.318 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7754 (IC base=+0.262)

- **PATRÓN** `dist_vwap_pct` > `0.224` → IC=+0.271 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.224 (IC base=+0.262)

- **PATRÓN** `dist_vwap_pct` < `0.3391` → IC=+0.278 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3391 (IC base=+0.262)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.198` → IC=+0.426 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.198 (IC base=+0.262)

- **PATRÓN** `volumen_regimen` > `0.9021` → IC=+0.308 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9021 (IC base=+0.262)

- **PATRÓN** `volumen_pendiente_norm` > `0.1167` → IC=+0.305 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1167 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` < `1.632` → IC=+0.300 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.632 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` > `3.3172` → IC=+0.300 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.3172 (IC base=+0.262)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.239 (n=201)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.1417` → IC=+0.228 (n=134)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1417 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` < `0.2489` → IC=+0.269 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2489 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.358` → IC=+0.269 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.358 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` < `1.2379` → IC=+0.234 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2379 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` < `0.086` → IC=+0.253 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.086 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` > `0.2284` → IC=+0.346 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2284 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` < `1.9099` → IC=+0.294 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9099 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `4836.9669` → IC=+0.210 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4836.9669 (IC base=+0.206)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **FILTRO** `ibs_20min` > `0.5918` → IC=-0.263 (n=74)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5918
  - _Potencial_: sin este filtro IC_bueno=+0.236 (n=225)

- **PATRÓN** `ibs_20min` > `0.8667` → IC=+0.176 (n=143)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.8667 (IC base=+0.032)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.462` → IC=+0.187 (n=65)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 7.462 (IC base=+0.032)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.240 (n=75)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.111)

- **PATRÓN** `drift_60min` |x|≤ `0.2787` → IC=+0.130 (n=198)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.2787 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.243 (n=103)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` < `0.5918` → IC=+0.236 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5918 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.178` → IC=+0.235 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.178 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` > `0.8838` → IC=+0.151 (n=150)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.8838 (IC base=+0.111)

- **PATRÓN** `volumen_pendiente_norm` > `0.1222` → IC=+0.239 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1222 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` > `2.7817` → IC=+0.206 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7817 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `2147.8152` → IC=+0.240 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2147.8152 (IC base=+0.111)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0067` → IC=+0.263 (n=78)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0067 (IC base=+0.112)

- **PATRÓN** `drift_60min` |x|≤ `0.209` → IC=+0.124 (n=203)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.62€ cuando `drift_60min` |x|≤ 0.209 (IC base=+0.112)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.164 (n=108)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 7.0 (IC base=+0.112)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.215 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.112)

- **PATRÓN** `dist_vwap_pct` > `0.2838` → IC=+0.182 (n=64)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.2838 (IC base=+0.112)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.38` → IC=+0.222 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.38 (IC base=+0.112)

- **PATRÓN** `volumen_pendiente_norm` > `0.3221` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.3221 (IC base=+0.112)

- **PATRÓN** `volumen_spike_ratio` < `1.5866` → IC=+0.147 (n=66)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.5866 (IC base=+0.112)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.275 (n=158)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.263)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.267 (n=213)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.263)

- **PATRÓN** `drift_60min` |x|≤ `0.1297` → IC=+0.264 (n=104)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1297 (IC base=+0.263)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.282 (n=108)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.263)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.293 (n=90)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.263)

- **PATRÓN** `ibs_20min` < `0.3069` → IC=+0.312 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3069 (IC base=+0.263)

- **PATRÓN** `dist_vwap_pct` > `0.2886` → IC=+0.346 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2886 (IC base=+0.263)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.033` → IC=+0.288 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.033 (IC base=+0.263)

- **PATRÓN** `volumen_regimen` > `0.9084` → IC=+0.319 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9084 (IC base=+0.263)

- **PATRÓN** `volumen_pendiente_norm` > `0.2868` → IC=+0.400 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2868 (IC base=+0.263)

- **PATRÓN** `volumen_spike_ratio` > `3.0859` → IC=+0.308 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.0859 (IC base=+0.263)

- **PATRÓN** `libro_liquidez` > `2548.3818` → IC=+0.273 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2548.3818 (IC base=+0.263)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.195 (n=80)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 17.0 (IC base=+0.040)

- **PATRÓN** `ibs_20min` > `0.9824` → IC=+0.164 (n=102)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.9824 (IC base=+0.040)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.989` → IC=+0.247 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.989 (IC base=+0.040)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.310 (n=56)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.043)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.859` → IC=+0.244 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.859 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `1.7388` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.7388 (IC base=+0.043)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=20)

- **FILTRO** `libro_liquidez` < `6436.909` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `libro_liquidez` < 6436.909
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=14)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.265 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.160)

- **PATRÓN** `drift_60min` |x|≤ `0.2699` → IC=+0.206 (n=32)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2699 (IC base=+0.160)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.241 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 13.0 (IC base=+0.160)

- **PATRÓN** `ibs_20min` < `0.2623` → IC=+0.265 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2623 (IC base=+0.160)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.192` → IC=+0.342 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.192 (IC base=+0.160)

- **PATRÓN** `volumen_regimen` < `1.218` → IC=+0.176 (n=32)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 1.218 (IC base=+0.160)

- **PATRÓN** `volumen_regimen` > `0.6412` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 0.6412 (IC base=+0.160)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0024` → IC=+0.237 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0024 (IC base=+0.231)

- **PATRÓN** `sigma_h` > `0.0027` → IC=+0.241 (n=25)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0027 (IC base=+0.231)

- **PATRÓN** `drift_60min` |x|≤ `0.2558` → IC=+0.250 (n=34)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2558 (IC base=+0.231)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.306 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 9.0 (IC base=+0.231)

- **PATRÓN** `ibs_20min` > `0.9601` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9601 (IC base=+0.231)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.738` → IC=+0.452 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.738 (IC base=+0.231)

- **PATRÓN** `volumen_regimen` < `0.9739` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9739 (IC base=+0.231)

- **PATRÓN** `volumen_regimen` > `1.0973` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0973 (IC base=+0.231)

- **PATRÓN** `volumen_pendiente_norm` > `0.1004` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1004 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` > `2.1374` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1374 (IC base=+0.231)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.326 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.103)

- **PATRÓN** `drift_60min` |x|≤ `0.3225` → IC=+0.167 (n=46)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.3225 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.227 (n=31)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.103)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.996` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.996 (IC base=+0.103)

- **PATRÓN** `volumen_regimen` < `0.6933` → IC=+0.283 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6933 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `9336.2451` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9336.2451 (IC base=+0.103)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` > `0.6852` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6852
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=61)

- **FILTRO** `dist_vwap_pct` > `0.19` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.19
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=65)

- **FILTRO** `volumen_pendiente_norm` > `0.1087` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1087
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=39)

- **FILTRO** `libro_liquidez` < `2536.4746` → IC=-0.154 (n=53)

  - _Acción_: SKIP cuando `libro_liquidez` < 2536.4746
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=28)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.144 (n=57)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 1.0 (IC base=+0.017)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.989` → IC=+0.188 (n=30)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 7.989 (IC base=+0.017)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0067` → IC=+0.197 (n=487)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0067 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.148 (n=541)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 17.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.288 (n=611)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` > `0.3318` → IC=+0.171 (n=147)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.3318 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.302` → IC=+0.227 (n=977)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.302 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.1804` → IC=+0.134 (n=331)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.1804 (IC base=+0.113)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.237 (n=1075)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0061 (IC base=+0.232)

- **PATRÓN** `sigma_h` > `0.0038` → IC=+0.238 (n=1217)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0038 (IC base=+0.232)

- **PATRÓN** `drift_60min` |x|≤ `0.1572` → IC=+0.233 (n=811)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1572 (IC base=+0.232)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.243 (n=1097)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.232)

- **PATRÓN** `ibs_20min` < `0.4667` → IC=+0.296 (n=1216)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4667 (IC base=+0.232)

- **PATRÓN** `dist_vwap_pct` < `0.1545` → IC=+0.206 (n=824)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1545 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.182` → IC=+0.265 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.182 (IC base=+0.232)

- **PATRÓN** `volumen_regimen` < `0.6196` → IC=+0.211 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6196 (IC base=+0.232)

- **PATRÓN** `volumen_regimen` > `1.0794` → IC=+0.222 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0794 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` > `0.1846` → IC=+0.318 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1846 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` < `1.6686` → IC=+0.317 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6686 (IC base=+0.232)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.186 (n=237)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0063 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.136 (n=358)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 6.0 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.155 (n=247)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 11.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.431` → IC=+0.365 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.431 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.209` → IC=+0.141 (n=51)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.209 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `2.3278` → IC=+0.133 (n=126)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.3278 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.177 (n=249)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.06 (IC base=+0.130)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.317 (n=58)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.293)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.320 (n=59)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.293)

- **PATRÓN** `drift_60min` |x|≤ `0.2132` → IC=+0.344 (n=152)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2132 (IC base=+0.293)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.298 (n=181)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.293)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.304 (n=156)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.293)

- **PATRÓN** `ibs_20min` < `0.5657` → IC=+0.334 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5657 (IC base=+0.293)

- **PATRÓN** `volumen_pendiente_norm` < `0.0708` → IC=+0.331 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0708 (IC base=+0.293)

- **PATRÓN** `volumen_spike_ratio` < `1.9246` → IC=+0.327 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9246 (IC base=+0.293)

- **PATRÓN** `volumen_spike_ratio` > `1.5394` → IC=+0.303 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5394 (IC base=+0.293)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.321 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `1888.7109` → IC=+0.315 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1888.7109 (IC base=+0.293)

### GBM_LATE_15M_TARDIO#BTC#15min
- **FILTRO** `ibs_20min` < `0.4026` → IC=-0.198 (n=61)

  - _Acción_: SKIP cuando `ibs_20min` < 0.4026
  - _Potencial_: sin este filtro IC_bueno=+0.270 (n=124)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.153 (n=93)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0026 (IC base=+0.115)

- **PATRÓN** `sigma_h` > `0.0031` → IC=+0.162 (n=63)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0031 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.208 (n=94)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` > `0.4026` → IC=+0.270 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4026 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` > `0.3609` → IC=+0.333 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3609 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.048` → IC=+0.240 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.048 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` > `0.9223` → IC=+0.153 (n=93)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.9223 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` < `0.1561` → IC=+0.173 (n=96)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` < 0.1561 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` > `0.1037` → IC=+0.167 (n=40)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.1037 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` < `2.9369` → IC=+0.229 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.9369 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `8379.647` → IC=+0.223 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8379.647 (IC base=+0.115)

- **PATRÓN** `sigma_h` < `0.0017` → IC=+0.222 (n=70)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0017 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.2001` → IC=+0.190 (n=185)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.2001 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.195 (n=195)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 8.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` < `0.3939` → IC=+0.226 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3939 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.258` → IC=+0.256 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.258 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `0.6183` → IC=+0.208 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6183 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` > `1.1302` → IC=+0.211 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1302 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.0924` → IC=+0.333 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0924 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` < `1.5399` → IC=+0.292 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5399 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `4746.3381` → IC=+0.188 (n=187)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 4746.3381 (IC base=+0.173)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0074` → IC=+0.245 (n=100)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0074 (IC base=+0.171)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.224 (n=143)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.331 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.932` → IC=+0.351 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.932 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` < `0.2301` → IC=+0.158 (n=229)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` < 0.2301 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `2.2197` → IC=+0.153 (n=99)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.2197 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `4.1293` → IC=+0.173 (n=102)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 4.1293 (IC base=+0.171)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.191 (n=318)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.06 (IC base=+0.171)

- **PATRÓN** `libro_liquidez` > `1914.6584` → IC=+0.179 (n=135)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 1914.6584 (IC base=+0.171)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.364 (n=79)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.297)

- **PATRÓN** `sigma_h` > `0.0074` → IC=+0.297 (n=77)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0074 (IC base=+0.297)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.311 (n=215)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.297)

- **PATRÓN** `ibs_20min` < `0.527` → IC=+0.350 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.527 (IC base=+0.297)

- **PATRÓN** `volumen_pendiente_norm` > `0.4009` → IC=+0.340 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.4009 (IC base=+0.297)

- **PATRÓN** `volumen_spike_ratio` < `3.7526` → IC=+0.310 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.7526 (IC base=+0.297)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.298 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.297)

### GBM_LATE_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_20min` < `0.3094` → IC=-0.250 (n=46)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3094
  - _Potencial_: sin este filtro IC_bueno=+0.199 (n=141)

- **PATRÓN** `sigma_h` < `0.0019` → IC=+0.194 (n=47)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0019 (IC base=+0.087)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.154 (n=53)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `0.3094` → IC=+0.199 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3094 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.4214` → IC=+0.147 (n=15)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.4214 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.602` → IC=+0.216 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.602 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` < `0.7759` → IC=+0.172 (n=62)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.7759 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2893` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2893 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `2.328` → IC=+0.269 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.328 (IC base=+0.087)

- **PATRÓN** `libro_liquidez` > `7922.5621` → IC=+0.235 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7922.5621 (IC base=+0.087)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.233 (n=88)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.0474` → IC=+0.219 (n=30)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0474 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.187 (n=81)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` < `0.0944` → IC=+0.320 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0944 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.0972` → IC=+0.260 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.0972 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.753` → IC=+0.273 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.753 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `0.8847` → IC=+0.222 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8847 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` < `0.0653` → IC=+0.433 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0653 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `2.0592` → IC=+0.344 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0592 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `1.8043` → IC=+0.340 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8043 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `4118.5114` → IC=+0.210 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4118.5114 (IC base=+0.152)

### GBM_LATE_15M_TARDIO#SOL#15min
- **FILTRO** `ibs_20min` < `0.5` → IC=-0.193 (n=73)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.076 (n=236)

- **FILTRO** `ibs_20min` > `0.5833` → IC=-0.186 (n=68)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5833
  - _Potencial_: sin este filtro IC_bueno=+0.256 (n=207)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.230 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.011)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.923` → IC=+0.162 (n=137)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 2.923 (IC base=+0.011)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.174 (n=182)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.006 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.176` → IC=+0.171 (n=138)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.176 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.218 (n=101)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` < `0.5833` → IC=+0.256 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5833 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.1739` → IC=+0.171 (n=168)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.1739 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.282` → IC=+0.250 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.282 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.863` → IC=+0.146 (n=196)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 2.863 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.7176` → IC=+0.188 (n=91)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.7176 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` > `1.1028` → IC=+0.156 (n=94)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 1.1028 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` < `0.1693` → IC=+0.371 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1693 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `1.6077` → IC=+0.370 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6077 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `2.2323` → IC=+0.400 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2323 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `1560.0837` → IC=+0.317 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1560.0837 (IC base=+0.146)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.204 (n=96)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0066 (IC base=+0.123)

- **PATRÓN** `drift_60min` |x|≤ `0.0716` → IC=+0.194 (n=96)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.0716 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.173 (n=111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.176 (n=106)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 6.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.236 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.3174` → IC=+0.272 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3174 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.29` → IC=+0.212 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.29 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.6783` → IC=+0.141 (n=257)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 0.6783 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.3216` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.3216 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `1.7589` → IC=+0.120 (n=214)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_spike_ratio` > 1.7589 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=292)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.293 (n=274)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0063 (IC base=+0.266)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.304 (n=146)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.266)

- **PATRÓN** `ibs_20min` < `0.1549` → IC=+0.376 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1549 (IC base=+0.266)

- **PATRÓN** `dist_vwap_pct` > `0.4019` → IC=+0.395 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4019 (IC base=+0.266)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.952` → IC=+0.346 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.952 (IC base=+0.266)

- **PATRÓN** `volumen_regimen` > `0.9` → IC=+0.308 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` > `0.2863` → IC=+0.379 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2863 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` < `1.5149` → IC=+0.292 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5149 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` > `2.6958` → IC=+0.266 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6958 (IC base=+0.266)

- **PATRÓN** `libro_liquidez` > `2554.1268` → IC=+0.269 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2554.1268 (IC base=+0.266)

### GBM_LATE_5M
- **FILTRO** `sigma_h` < `0.0037` → IC=-0.222 (n=16)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0037
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=35)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.132 (n=112)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.133 (n=96)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.004 (IC base=+0.089)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.181 (n=45)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 4.0 (IC base=+0.089)

- **PATRÓN** `volumen_regimen` < `1.4082` → IC=+0.133 (n=96)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.4082 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` < `2.7539` → IC=+0.146 (n=94)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.7539 (IC base=+0.089)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.132 (n=112)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.089)

- **PATRÓN** `libro_liquidez` > `6100.6498` → IC=+0.133 (n=96)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 6100.6498 (IC base=+0.089)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` > `0.0021` → IC=+0.127 (n=57)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` > 0.0021 (IC base=+0.090)

- **PATRÓN** `drift_60min` |x|≤ `0.0856` → IC=+0.179 (n=26)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.0856 (IC base=+0.090)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.182 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 3.0 (IC base=+0.090)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.005` → IC=+0.141 (n=37)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 3.005 (IC base=+0.090)

- **PATRÓN** `volumen_pendiente_norm` > `0.0834` → IC=+0.136 (n=31)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.0834 (IC base=+0.090)

- **PATRÓN** `volumen_spike_ratio` < `2.2547` → IC=+0.160 (n=51)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.2547 (IC base=+0.090)

- **PATRÓN** `volumen_spike_ratio` > `1.4459` → IC=+0.144 (n=57)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.4459 (IC base=+0.090)

### GBM_LATE_60M
- **FILTRO** `ibs_20min` < `0.6842` → IC=-0.173 (n=50)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6842
  - _Potencial_: sin este filtro IC_bueno=+0.231 (n=102)

- **FILTRO** `drift_60min` |x|> `0.0945` → IC=-0.289 (n=17)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.0945
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=34)

- **FILTRO** `ibs_20min` > `0.6783` → IC=-0.284 (n=35)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6783
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=70)

- **FILTRO** `dist_vwap_pct` > `0.1008` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1008
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=48)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.171 (n=138)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0054 (IC base=+0.054)

- **PATRÓN** `drift_60min` |x|≤ `0.1312` → IC=+0.194 (n=34)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.1312 (IC base=+0.054)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.316 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.054)

- **PATRÓN** `dist_vwap_pct` > `0.1249` → IC=+0.156 (n=59)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1249 (IC base=+0.054)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.183` → IC=+0.229 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.183 (IC base=+0.054)

- **PATRÓN** `volumen_regimen` > `1.1022` → IC=+0.225 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1022 (IC base=+0.054)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `sigma_h` > `0.0037` → IC=-0.157 (n=33)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0037
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=34)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.186 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=34)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.321 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.059)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` > `0.1642` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1642 (IC base=+0.059)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `hora_utc` > `5.0` → IC=-0.360 (n=41)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=22)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.224 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.353 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` < `0.1239` → IC=+0.191 (n=40)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.1239 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.347` → IC=+0.346 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.347 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` < `0.8241` → IC=+0.167 (n=34)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8241 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` > `1.0919` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0919 (IC base=+0.087)

- **PATRÓN** `libro_liquidez` > `2351.5975` → IC=+0.219 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2351.5975 (IC base=+0.087)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.0165` → IC=-0.309 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0165
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=58)

- **FILTRO** `ibs_20min` > `0.2381` → IC=-0.308 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2381
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=12)

- **PATRÓN** `sigma_h` > `0.0136` → IC=+0.237 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0136 (IC base=-0.007)

### GBM_LATE_60M_FADE
- **FILTRO** `drift_60min` |x|> `0.1252` → IC=-0.379 (n=31)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1252
  - _Potencial_: sin este filtro IC_bueno=-0.246 (n=61)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.423 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.212 (n=57)

- **FILTRO** `dist_vwap_pct` < `0.1009` → IC=-0.352 (n=52)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1009
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=43)

- **FILTRO** `dist_vwap_pct` > `0.3507` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3507
  - _Potencial_: sin este filtro IC_bueno=-0.275 (n=78)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `volumen_regimen` < `1.6138` → IC=-0.286 (n=26)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.6138
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `dist_vwap_pct` < `0.0931` → IC=-0.362 (n=27)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0931
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=13)

- **FILTRO** `libro_liquidez` < `4361.6218` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `libro_liquidez` < 4361.6218
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=20)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` < `9.988` → IC=-0.462 (n=24)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 9.988
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **FILTRO** `sigma_h` > `0.0018` → IC=-0.346 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0018
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `drift_60min` |x|> `0.0825` → IC=-0.350 (n=18)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.0825
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `ibs_20min` > `0.6061` → IC=+0.147 (n=131)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.6061 (IC base=+0.057)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.188 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 15.0 (IC base=+0.044)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6942` → IC=-0.333 (n=28)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6942
  - _Potencial_: sin este filtro IC_bueno=+0.177 (n=29)

- **FILTRO** `volumen_regimen` < `0.8896` → IC=-0.133 (n=28)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8896
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=29)

- **PATRÓN** `ibs_20min` > `0.6942` → IC=+0.177 (n=29)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.6942 (IC base=-0.076)

- **PATRÓN** `drift_60min` |x|≤ `0.1318` → IC=+0.167 (n=28)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1318 (IC base=+0.107)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.265 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.107)

- **PATRÓN** `ibs_20min` < `0.1524` → IC=+0.159 (n=39)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.1524 (IC base=+0.107)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.574` → IC=+0.176 (n=32)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 3.574 (IC base=+0.107)

- **PATRÓN** `volumen_regimen` < `0.5802` → IC=+0.147 (n=15)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.5802 (IC base=+0.107)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **PATRÓN** `ibs_20min` > `0.9489` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9489 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.991` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.991 (IC base=+0.167)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `hora_utc` < `16.0` → IC=-0.167 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=14)

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

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `17.0` → IC=-0.333 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=84)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=84)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=84)

- **FILTRO** `libro_liquidez` < `1970.6128` → IC=-0.389 (n=25)

  - _Acción_: SKIP cuando `libro_liquidez` < 1970.6128
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=75)

- **FILTRO** `hora_utc` < `12.0` → IC=-0.156 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=72)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=82)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### LIQUIDACIONES_15M#XRP#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=21)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.150 (n=18)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9732` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9732
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=60)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.204 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.114 (n=55)

### MOMENTUM_IBS_15M
- **FILTRO** `hora_utc` < `14.0` → IC=-0.405 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=148)

- **PATRÓN** `hora_utc` > `20.0` → IC=+0.196 (n=44)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 20.0 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.305 (n=39)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.152)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.167 (n=103)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` > 0.505 (IC base=+0.152)

- **PATRÓN** `drift_20min_pct` |x|≤ `0.0609` → IC=+0.250 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `drift_20min_pct` |x|≤ 0.0609 (IC base=+0.152)

- **PATRÓN** `ibs_20min` < `0.2179` → IC=+0.173 (n=105)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.2179 (IC base=+0.152)

- **PATRÓN** `ibs_20min` > `0.0075` → IC=+0.164 (n=105)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.0075 (IC base=+0.152)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=108)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `14143.4538` → IC=+0.200 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14143.4538 (IC base=+0.152)

### MOMENTUM_IBS_15M#BNB#15min
- **FILTRO** `libro_liquidez` < `2239.29` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_liquidez` < 2239.29
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=15)

### MOMENTUM_IBS_15M#SOL#15min
- **FILTRO** `ibs_20min` > `0.7059` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7059
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=10)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `hora_utc` < `15.0` → IC=-0.203 (n=35)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=109)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.156 (n=30)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=114)

- **FILTRO** `ibs_20min` < `0.7647` → IC=-0.203 (n=35)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7647
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=109)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.271 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.098)

- **PATRÓN** `ibs_20min` > `0.1758` → IC=+0.167 (n=61)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.1758 (IC base=+0.098)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.125 (n=118)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 6.0 (IC base=+0.098)

### MOMENTUM_IBS_15M_BALLENA#SOL#15min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.167 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=13)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `hora_utc` < `16.0` → IC=-0.294 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=88)

- **FILTRO** `hora_utc` > `19.0` → IC=-0.206 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=88)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.159 (n=39)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=51)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=69)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `hora_utc` < `18.0` → IC=-0.333 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=11)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `ibs_20min` < `0.2368` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2368
  - _Potencial_: sin este filtro IC_bueno=+0.250 (n=6)

### MOMENTUM_IBS_5M
- **PATRÓN** `drift_7min_pct` |x|≤ `0.0394` → IC=+0.163 (n=90)

  - _Acción_: Kelly boost +0.82€ cuando `drift_7min_pct` |x|≤ 0.0394 (IC base=+0.050)

### MOMENTUM_IBS_5M#BNB#5min
- **FILTRO** `hora_utc` > `17.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=38)

### MOMENTUM_IBS_5M#BTC#5min
- **FILTRO** `hora_utc` > `18.0` → IC=-0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 18.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=43)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.143 (n=40)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 17.0 (IC base=+0.033)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.167 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 15.0 (IC base=-0.007)

### MOMENTUM_IBS_5M#DOGE#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=38)

- **PATRÓN** `drift_7min_pct` |x|≤ `0.0781` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `drift_7min_pct` |x|≤ 0.0781 (IC base=+0.058)

### MOMENTUM_IBS_5M#ETH#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=33)

- **PATRÓN** `drift_7min_pct` |x|≤ `0.0379` → IC=+0.278 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `drift_7min_pct` |x|≤ 0.0379 (IC base=+0.059)

### MOMENTUM_IBS_5M#SOL#5min
- **PATRÓN** `hora_utc` < `16.0` → IC=+0.222 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.147)

- **PATRÓN** `drift_7min_pct` |x|≤ `0.1053` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `drift_7min_pct` |x|≤ 0.1053 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `3973.5795` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3973.5795 (IC base=+0.147)

### MOMENTUM_IBS_5M_BALLENA
- **FILTRO** `hora_utc` < `14.0` → IC=-0.194 (n=106)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=323)

- **FILTRO** `hora_utc` > `20.0` → IC=-0.127 (n=124)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=305)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.225 (n=107)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=322)

- **FILTRO** `ibs_7min` < `0.8507` → IC=-0.192 (n=141)

  - _Acción_: SKIP cuando `ibs_7min` < 0.8507
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=288)

- **FILTRO** `ballena_activa_n` > `17.0` → IC=-0.170 (n=107)

  - _Acción_: SKIP cuando `ballena_activa_n` > 17.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=322)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.42` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=51)

- **FILTRO** `libro_liquidez` < `2244.0498` → IC=-0.132 (n=55)

  - _Acción_: SKIP cuando `libro_liquidez` < 2244.0498
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=19)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.167 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 15.0 (IC base=+0.064)

- **PATRÓN** `py_entrada` < `0.56` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.56 (IC base=+0.064)

- **PATRÓN** `ballena_activa_n` < `5.0` → IC=+0.136 (n=20)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 5.0 (IC base=+0.064)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.180 (n=23)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=71)

- **FILTRO** `hora_utc` > `1.0` → IC=-0.179 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=19)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `14.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=54)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=54)

- **FILTRO** `ibs_7min` < `0.7041` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7041
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=54)

- **FILTRO** `libro_liquidez` < `2496.9172` → IC=-0.257 (n=35)

  - _Acción_: SKIP cuando `libro_liquidez` < 2496.9172
  - _Potencial_: sin este filtro IC_bueno=+0.132 (n=36)

- **FILTRO** `py_entrada` > `0.54` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `py_entrada` > 0.54
  - _Potencial_: sin este filtro IC_bueno=+0.090 (n=37)

- **PATRÓN** `libro_liquidez` > `2496.9172` → IC=+0.132 (n=36)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2496.9172 (IC base=-0.062)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.214 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=30)

- **FILTRO** `py_entrada` < `0.42` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=38)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=31)

- **FILTRO** `libro_liquidez` < `4155.3031` → IC=-0.200 (n=28)

  - _Acción_: SKIP cuando `libro_liquidez` < 4155.3031
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=28)

- **FILTRO** `hora_utc` > `2.0` → IC=-0.149 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 2.0
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=18)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=36)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.200 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=54)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=55)

- **FILTRO** `ibs_7min` < `0.92` → IC=-0.184 (n=36)

  - _Acción_: SKIP cuando `ibs_7min` < 0.92
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=36)

- **FILTRO** `ballena_activa_n` > `18.0` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `ballena_activa_n` > 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=55)

- **FILTRO** `libro_liquidez` < `3120.6604` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 3120.6604
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=54)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.182 (n=42)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 18.0 (IC base=+0.094)

- **PATRÓN** `py_entrada` < `0.59` → IC=+0.153 (n=47)

  - _Acción_: Kelly boost +0.77€ cuando `py_entrada` < 0.59 (IC base=+0.094)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.151 (n=41)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 15.0 (IC base=+0.094)

- **PATRÓN** `libro_liquidez` > `4353.0344` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4353.0344 (IC base=+0.094)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=47)

- **FILTRO** `ibs_7min` < `0.7479` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7479
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=47)

- **FILTRO** `ballena_activa_n` > `16.0` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `ballena_activa_n` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=47)

- **FILTRO** `libro_liquidez` < `1961.2126` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_liquidez` < 1961.2126
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=42)

- **PATRÓN** `hora_utc` < `20.0` → IC=+0.128 (n=49)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 20.0 (IC base=+0.052)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.130 (n=44)

  - _Acción_: Kelly boost +0.65€ cuando `py_entrada` < 0.505 (IC base=+0.052)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **PATRÓN** `ibs_7min` > `1.0` → IC=+0.176 (n=35)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_7min` > 1.0 (IC base=+0.083)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=47)

- **FILTRO** `libro_liquidez` < `10979.2198` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `libro_liquidez` < 10979.2198
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=42)

- **PATRÓN** `hora_utc` > `20.0` → IC=+0.182 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 20.0 (IC base=+0.054)

- **PATRÓN** `drift_7min_pct` |x|≤ `0.0404` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `drift_7min_pct` |x|≤ 0.0404 (IC base=+0.016)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `drift_7min_pct` |x|> `0.0631` → IC=-0.167 (n=28)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.0631
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=58)

- **PATRÓN** `ibs_7min` < `0.8933` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_7min` < 0.8933 (IC base=+0.059)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `hora_utc` < `20.0` → IC=-0.156 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=17)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.155 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 15.0 (IC base=+0.061)

### ORDER_FLOW_5M
- **FILTRO** `total_vol_5m` > `215.224` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `total_vol_5m` > 215.224
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **PATRÓN** `delta_ratio` |x|> `0.3994` → IC=+0.148 (n=123)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.74€ cuando `delta_ratio` |x|> 0.3994 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.147 (n=49)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 18.0 (IC base=+0.128)

- **PATRÓN** `total_vol_5m` < `389.535` → IC=+0.271 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 389.535 (IC base=+0.128)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `7.2125` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.2125
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=38)

- **FILTRO** `pct_vs_K` |x|> `4.6307` → IC=-0.469 (n=30)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.6307
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=61)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `pct_vs_K` |x|> `2.6035` → IC=-0.462 (n=24)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.6035
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=13)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0132` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0132
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `T_h` > `144.5498` → IC=-0.397 (n=27)

  - _Acción_: SKIP cuando `T_h` > 144.5498
  - _Potencial_: sin este filtro IC_bueno=-0.133 (n=28)

- **FILTRO** `sigma_h` > `0.0034` → IC=-0.333 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=14)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` > `0.0034` → IC=-0.324 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0034
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `T_h` > `95.1632` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `T_h` > 95.1632
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **FILTRO** `sigma_h` > `0.0033` → IC=-0.237 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=6)

### STREAK_FADE_5M
- **FILTRO** `hora_utc` > `14.0` → IC=-0.156 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=70)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=73)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.214 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=-0.020)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `4.0` → IC=-0.143 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=14)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.196 (n=21)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=23)

- **FILTRO** `streak_estiramiento` > `0.5167` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.5167
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=23)

### STREAK_MOM_5M
- **PATRÓN** `streak_estiramiento` < `0.3309` → IC=+0.176 (n=32)

  - _Acción_: Kelly boost +0.88€ cuando `streak_estiramiento` < 0.3309 (IC base=+0.035)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.174 (n=41)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 25.0 (IC base=+0.035)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `hora_utc` > `8.0` → IC=-0.167 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=35)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.198 (n=41)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 10.0 (IC base=+0.083)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `py_entrada` < 0.495 (IC base=+0.083)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=58)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.227 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.100)

- **PATRÓN** `streak_len` < `3.0` → IC=+0.167 (n=58)

  - _Acción_: Kelly boost +0.83€ cuando `streak_len` < 3.0 (IC base=+0.100)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=647)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=354)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=362)

### UPDOWN_GBM#15min
- **FILTRO** `ibs_15` < `0.5675` → IC=-0.164 (n=135)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5675
  - _Potencial_: sin este filtro IC_bueno=+0.222 (n=275)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.123 (n=205)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` > 0.0047 (IC base=+0.095)

- **PATRÓN** `ibs_15` > `0.5675` → IC=+0.222 (n=275)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5675 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` > `0.4172` → IC=+0.182 (n=61)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.4172 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.09` → IC=+0.222 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.09 (IC base=+0.095)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.163 (n=191)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.0058 (IC base=+0.111)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0816` → IC=+0.141 (n=285)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.71€ cuando `delta_ratio_macro` |x|> 0.0816 (IC base=+0.111)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.152 (n=271)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 16.0 (IC base=+0.111)

- **PATRÓN** `ibs_15` < `0.4842` → IC=+0.156 (n=286)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.78€ cuando `ibs_15` < 0.4842 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` > `0.3215` → IC=+0.210 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3215 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.778` → IC=+0.134 (n=285)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 10.778 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `3080.4592` → IC=+0.151 (n=130)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3080.4592 (IC base=+0.111)

### UPDOWN_GBM#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0054` → IC=-0.152 (n=182)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0054
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=62)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.0711` → IC=-0.135 (n=61)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.0711
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=183)

- **FILTRO** `ibs_15` < `0.0909` → IC=-0.274 (n=60)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.0909
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=184)

- **FILTRO** `dist_vwap_pct` > `0.2843` → IC=-0.133 (n=47)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2843
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=177)

- **FILTRO** `sigma_ewma_delta_pct` > `5.327` → IC=-0.188 (n=62)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.327
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=182)

### UPDOWN_GBM#60min
- **FILTRO** `hora_utc` < `11.0` → IC=-0.269 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=126)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.0016` → IC=-0.200 (n=28)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0016
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=30)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.132 (n=74)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.03 (IC base=+0.000)

### UPDOWN_GBM#BTC#15min
- **FILTRO** `sigma_ewma_delta_pct` < `30.951` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 30.951
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=5)

- **PATRÓN** `sigma_h` > `0.0021` → IC=+0.131 (n=63)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` > 0.0021 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.152 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 4.0 (IC base=+0.111)

- **PATRÓN** `ibs_15` > `0.9362` → IC=+0.206 (n=32)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9362 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` > `0.3722` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3722 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` < `0.1019` → IC=+0.183 (n=39)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.1019 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `10246.118` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 10246.118 (IC base=+0.111)

### UPDOWN_GBM#BTC#5min
- **FILTRO** `sigma_h` < `0.0034` → IC=-0.214 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11)

- **FILTRO** `ibs_15` < `0.0668` → IC=-0.324 (n=15)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.0668
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=15)

- **PATRÓN** `sigma_ewma_delta_pct` > `1.941` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 1.941 (IC base=+0.068)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `ibs_15` < `0.9182` → IC=-0.150 (n=38)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.9182
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=21)

### UPDOWN_GBM#ETH#15min
- **FILTRO** `ibs_15` < `0.6973` → IC=-0.152 (n=44)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6973
  - _Potencial_: sin este filtro IC_bueno=+0.330 (n=45)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1329` → IC=+0.223 (n=45)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1329 (IC base=+0.093)

- **PATRÓN** `ibs_15` > `0.6973` → IC=+0.330 (n=45)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6973 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` < `0.1005` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1005 (IC base=+0.093)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.937` → IC=+0.188 (n=30)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 8.937 (IC base=+0.093)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.200 (n=68)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.173)

- **PATRÓN** `sigma_h` > `0.0043` → IC=+0.198 (n=51)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0043 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.4769` → IC=+0.183 (n=77)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.4769 (IC base=+0.173)

- **PATRÓN** `drift_15min` |x|≤ `0.6513` → IC=+0.185 (n=52)

  - _Acción_: Kelly boost +0.93€ cuando `drift_15min` |x|≤ 0.6513 (IC base=+0.173)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1143` → IC=+0.176 (n=69)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio_macro` |x|> 0.1143 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.196 (n=77)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 4.0 (IC base=+0.173)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.194 (n=83)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 16.0 (IC base=+0.173)

- **PATRÓN** `ibs_15` < `0.2005` → IC=+0.214 (n=68)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.2005 (IC base=+0.173)

- **PATRÓN** `ibs_15` > `0.0304` → IC=+0.209 (n=77)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.0304 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.1668` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1668 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` < `23.395` → IC=+0.218 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 23.395 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `10693.7296` → IC=+0.321 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10693.7296 (IC base=+0.173)

### UPDOWN_GBM#ETH#5min
- **FILTRO** `ibs_15` < `0.0101` → IC=-0.237 (n=17)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.0101
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=37)

- **FILTRO** `dist_vwap_pct` > `0.1774` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1774
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=39)

- **FILTRO** `sigma_ewma_delta_pct` > `5.626` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.626
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=30)

- **PATRÓN** `hora_utc` < `1.0` → IC=+0.147 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 1.0 (IC base=+0.083)

### UPDOWN_GBM#SOL#15min
- **FILTRO** `ibs_15` < `0.6` → IC=-0.177 (n=29)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.242 (n=29)

- **PATRÓN** `ibs_15` > `0.6` → IC=+0.242 (n=29)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6 (IC base=+0.033)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.764` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.764 (IC base=+0.033)

- **PATRÓN** `sigma_h` > `0.0061` → IC=+0.186 (n=33)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0061 (IC base=+0.052)

- **PATRÓN** `ibs_15` < `0.0769` → IC=+0.184 (n=17)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.92€ cuando `ibs_15` < 0.0769 (IC base=+0.052)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.131` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 7.131 (IC base=+0.052)

- **PATRÓN** `libro_liquidez` > `3279.489` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3279.489 (IC base=+0.052)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `ibs_15` < `0.5385` → IC=-0.242 (n=29)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5385
  - _Potencial_: sin este filtro IC_bueno=+0.147 (n=15)

- **FILTRO** `dist_vwap_pct` < `0.1891` → IC=-0.167 (n=31)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1891
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=13)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.231 (n=24)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.092)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.176 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 12.0 (IC base=+0.092)

- **PATRÓN** `ibs_15` < `0.0714` → IC=+0.333 (n=16)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.0714 (IC base=+0.092)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.092)

### UPDOWN_GBM#SOL#60min
- **FILTRO** `sigma_h` > `0.0061` → IC=-0.222 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0061
  - _Potencial_: sin este filtro IC_bueno=+0.237 (n=17)

- **FILTRO** `hora_utc` < `16.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=10)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.005` → IC=+0.163 (n=96)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.005 (IC base=+0.081)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0626` → IC=+0.133 (n=96)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio_macro` |x|> 0.0626 (IC base=+0.081)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.167 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 6.0 (IC base=+0.081)

- **PATRÓN** `ibs_15` > `0.4444` → IC=+0.153 (n=96)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.77€ cuando `ibs_15` > 0.4444 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` > `0.4266` → IC=+0.241 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4266 (IC base=+0.081)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.277` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.277 (IC base=+0.081)

- **PATRÓN** `libro_liquidez` > `2503.3208` → IC=+0.136 (n=86)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 2503.3208 (IC base=+0.081)

- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.233 (n=43)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.174` → IC=+0.244 (n=41)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.174 (IC base=+0.127)

- **PATRÓN** `drift_15min` |x|≤ `0.4542` → IC=+0.151 (n=41)

  - _Acción_: Kelly boost +0.76€ cuando `drift_15min` |x|≤ 0.4542 (IC base=+0.127)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0776` → IC=+0.174 (n=93)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.87€ cuando `delta_ratio_macro` |x|> 0.0776 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `20.0` → IC=+0.201 (n=95)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 20.0 (IC base=+0.127)

- **PATRÓN** `ibs_15` < `0.1724` → IC=+0.238 (n=63)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1724 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `0.1294` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1294 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.47` → IC=+0.199 (n=81)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` < 5.47 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `2515.6876` → IC=+0.174 (n=93)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2515.6876 (IC base=+0.127)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1971` → IC=+0.243 (n=68)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1971 (IC base=+0.231)

- **PATRÓN** `sigma_h` < `0.0025` → IC=+0.278 (n=52)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0025 (IC base=+0.231)

- **PATRÓN** `drift_60min` |x|≤ `0.1599` → IC=+0.257 (n=68)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1599 (IC base=+0.231)

- **PATRÓN** `drift_15min` |x|≤ `0.4034` → IC=+0.250 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4034 (IC base=+0.231)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2085` → IC=+0.257 (n=35)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2085 (IC base=+0.231)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.321 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.231)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.246 (n=69)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 13.0 (IC base=+0.231)

- **PATRÓN** `ibs_15` > `0.7061` → IC=+0.285 (n=77)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7061 (IC base=+0.231)

- **PATRÓN** `dist_vwap_pct` > `0.3516` → IC=+0.315 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3516 (IC base=+0.231)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.854` → IC=+0.271 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.854 (IC base=+0.231)

- **PATRÓN** `libro_liquidez` > `3141.8886` → IC=+0.232 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3141.8886 (IC base=+0.231)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1971` → IC=+0.245 (n=45)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1971 (IC base=+0.196)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.236 (n=51)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.196)

- **PATRÓN** `drift_60min` |x|≤ `0.1567` → IC=+0.223 (n=45)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1567 (IC base=+0.196)

- **PATRÓN** `drift_15min` |x|≤ `0.4681` → IC=+0.250 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4681 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.226 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.196)

- **PATRÓN** `ibs_15` < `0.984` → IC=+0.198 (n=51)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.99€ cuando `ibs_15` < 0.984 (IC base=+0.196)

- **PATRÓN** `ibs_15` > `0.8936` → IC=+0.250 (n=34)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8936 (IC base=+0.196)

- **PATRÓN** `dist_vwap_pct` > `0.2982` → IC=+0.342 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2982 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.854` → IC=+0.206 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.854 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.139` → IC=+0.192 (n=37)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 12.139 (IC base=+0.196)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `dist_vwap_pct` < `0.059` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.059 (IC base=+0.284)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `ibs_15` < `0.5408` → IC=-0.271 (n=103)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5408
  - _Potencial_: sin este filtro IC_bueno=+0.243 (n=103)

- **FILTRO** `sigma_ewma_delta_pct` > `12.785` → IC=-0.142 (n=205)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 12.785
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=850)

- **PATRÓN** `ibs_15` > `0.5408` → IC=+0.243 (n=103)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5408 (IC base=-0.035)

- **PATRÓN** `ibs_15` < `0.2364` → IC=+0.328 (n=27)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.2364 (IC base=-0.045)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.236 (n=70)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=168)

- **FILTRO** `hora_utc` > `16.0` → IC=-0.209 (n=53)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=185)

- **FILTRO** `sigma_ewma_delta_pct` < `9.186` → IC=-0.215 (n=135)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 9.186
  - _Potencial_: sin este filtro IC_bueno=-0.138 (n=103)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.4477` → IC=-0.384 (n=41)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.4477
  - _Potencial_: sin este filtro IC_bueno=+0.174 (n=41)

- **FILTRO** `dist_vwap_pct` > `0.1594` → IC=-0.176 (n=32)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1594
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=50)

- **PATRÓN** `ibs_15` > `0.4477` → IC=+0.174 (n=41)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.87€ cuando `ibs_15` > 0.4477 (IC base=-0.107)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.265 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.260 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.094` → IC=+0.278 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.094 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `3786.4324` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3786.4324 (IC base=+0.204)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_ewma_delta_pct` > `13.905` → IC=-0.190 (n=56)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 13.905
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=315)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.078` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.078 (IC base=+0.018)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` < `0.0049` → IC=-0.128 (n=41)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0049
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=86)

- **FILTRO** `libro_liquidez` < `2503.3208` → IC=-0.198 (n=41)

  - _Acción_: SKIP cuando `libro_liquidez` < 2503.3208
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=86)

- **FILTRO** `sigma_ewma_delta_pct` > `7.734` → IC=-0.159 (n=80)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.734
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=268)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` > `0.0023` → IC=+0.247 (n=89)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0023 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.1819` → IC=+0.255 (n=100)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1819 (IC base=+0.239)

- **PATRÓN** `drift_15min` |x|≤ `0.625` → IC=+0.244 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.625 (IC base=+0.239)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2085` → IC=+0.308 (n=45)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2085 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.272 (n=99)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.239)

- **PATRÓN** `ibs_15` > `0.9325` → IC=+0.309 (n=66)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9325 (IC base=+0.239)

- **PATRÓN** `dist_vwap_pct` > `0.3696` → IC=+0.312 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3696 (IC base=+0.239)

- **PATRÓN** `dist_vwap_pct` < `0.0929` → IC=+0.293 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0929 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.501` → IC=+0.250 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.501 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.438` → IC=+0.237 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.438 (IC base=+0.239)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.2061` → IC=+0.223 (n=63)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.2061 (IC base=+0.218)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.238 (n=63)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.218)

- **PATRÓN** `sigma_h` > `0.0021` → IC=+0.241 (n=56)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0021 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.1837` → IC=+0.254 (n=63)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1837 (IC base=+0.218)

- **PATRÓN** `drift_15min` |x|≤ `0.6592` → IC=+0.238 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.6592 (IC base=+0.218)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2087` → IC=+0.242 (n=29)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2087 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.276 (n=56)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.218)

- **PATRÓN** `ibs_15` < `0.9998` → IC=+0.227 (n=64)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.9998 (IC base=+0.218)

- **PATRÓN** `ibs_15` > `0.9358` → IC=+0.273 (n=42)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9358 (IC base=+0.218)

- **PATRÓN** `dist_vwap_pct` > `0.3582` → IC=+0.357 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3582 (IC base=+0.218)

- **PATRÓN** `dist_vwap_pct` < `0.0966` → IC=+0.250 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0966 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `14.018` → IC=+0.233 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 14.018 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.495` → IC=+0.223 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.495 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `5349.0852` → IC=+0.227 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5349.0852 (IC base=+0.218)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` > `0.0027` → IC=+0.300 (n=33)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0027 (IC base=+0.265)

- **PATRÓN** `drift_60min` |x|≤ `0.1348` → IC=+0.271 (n=33)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1348 (IC base=+0.265)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1995` → IC=+0.395 (n=17)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1995 (IC base=+0.265)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.293 (n=27)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.265)

- **PATRÓN** `ibs_15` > `0.9678` → IC=+0.395 (n=17)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9678 (IC base=+0.265)

- **PATRÓN** `dist_vwap_pct` < `0.0774` → IC=+0.292 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0774 (IC base=+0.265)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.98` → IC=+0.283 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.98 (IC base=+0.265)

- **PATRÓN** `sigma_ewma_delta_pct` < `16.771` → IC=+0.278 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 16.771 (IC base=+0.265)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.047` → IC=-0.180 (n=23)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.047
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

- **FILTRO** `sigma_h` > `0.0028` → IC=-0.196 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0028
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `drift_60min` |x|> `0.1471` → IC=-0.206 (n=15)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1471
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1227` → IC=-0.176 (n=69)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1227
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=210)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0931` → IC=-0.278 (n=16)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0931
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `sigma_h` > `0.0045` → IC=-0.289 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0045
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

### WEEKLY_PRICE
- **PATRÓN** `T_h` < `111.9997` → IC=+0.138 (n=56)

  - _Acción_: Kelly boost +0.69€ cuando `T_h` < 111.9997 (IC base=+0.004)

- **PATRÓN** `T_h` > `146.1132` → IC=+0.453 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1132 (IC base=+0.355)

- **PATRÓN** `ratio` > `1.016` → IC=+0.450 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.016 (IC base=+0.355)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` < `100.962` → IC=+0.343 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 100.962 (IC base=+0.281)

- **PATRÓN** `pct_dist` |x|≤ `0.6014` → IC=+0.276 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `pct_dist` |x|≤ 0.6014 (IC base=+0.281)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `111.9838` → IC=+0.328 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9838 (IC base=+0.318)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `135.9977` → IC=+0.440 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 135.9977 (IC base=+0.426)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#SOL#5min**: dentro de BUY_NO, IBS < 0.0714 sube el IC de +0.092 a +0.333 en UPDOWN_GBM#SOL#5min (n=16). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5675 sube el IC de +0.095 a +0.222 en UPDOWN_GBM#15min (n=275). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_NO, IBS < 0.4842 sube el IC de +0.111 a +0.156 en UPDOWN_GBM#15min (n=286). Ya aplicado como kelly_boost=+0.78€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.9362 sube el IC de +0.111 a +0.206 en UPDOWN_GBM#BTC#15min (n=32). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6973 sube el IC de +0.093 a +0.330 en UPDOWN_GBM#ETH#15min (n=45). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_NO, IBS < 0.2005 sube el IC de +0.173 a +0.214 en UPDOWN_GBM#ETH#15min (n=68). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_NO, IBS > 0.0304 sube el IC de +0.173 a +0.209 en UPDOWN_GBM#ETH#15min (n=77). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.033 a +0.242 en UPDOWN_GBM#SOL#15min (n=29). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_NO, IBS < 0.0769 sube el IC de +0.052 a +0.184 en UPDOWN_GBM#SOL#15min (n=17). Ya aplicado como kelly_boost=+0.92€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.4444 sube el IC de +0.081 a +0.153 en UPDOWN_GBM#XRP#15min (n=96). Ya aplicado como kelly_boost=+0.77€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1724 sube el IC de +0.127 a +0.238 en UPDOWN_GBM#XRP#15min (n=63). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.5408 sube el IC de -0.035 a +0.243 en UPDOWN_GBM_15M_TARDIO (n=103). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.2364 sube el IC de -0.045 a +0.328 en UPDOWN_GBM_15M_TARDIO (n=27). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.4477 sube el IC de -0.107 a +0.174 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=41). Ya aplicado como kelly_boost=+0.87€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.9325 sube el IC de +0.239 a +0.309 en UPDOWN_GBM_IBS_ALTO (n=66). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS < 0.9998 sube el IC de +0.218 a +0.227 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=64). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.9358 sube el IC de +0.218 a +0.273 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=42). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.9678 sube el IC de +0.265 a +0.395 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7061 sube el IC de +0.231 a +0.285 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=77). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS < 0.984 sube el IC de +0.196 a +0.198 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=51). Ya aplicado como kelly_boost=+0.99€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8936 sube el IC de +0.196 a +0.250 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=34). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min` — IC=+0.284 n=35. Faltan ~5 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH` — IC=+0.284 n=35. Faltan ~5 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min` — IC=+0.425 n=38. Faltan ~2 resoluciones para umbral n≥40. ETA: ~1h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL` — IC=+0.425 n=38. Faltan ~2 resoluciones para umbral n≥40. ETA: ~1h.
- **LIVE-CANDIDATA**: `UPDOWN_GBM#BTC#240min` — IC=+0.088 n=32. Faltan ~8 resoluciones para umbral n≥40. ETA: ~6h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 481 | +0.042 | +37.07€ | 3 | 4 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 481 | +0.042 | +37.07€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 252 | +0.043 | +24.96€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 252 | +0.043 | +24.96€ | 2 | 4 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 205 | +0.017 | -1.09€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 205 | +0.017 | -1.09€ | 6 | 4 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 24 | +0.231 | +13.21€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 24 | +0.231 | +13.21€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 3022 | -0.124 | -496.76€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 427 | -0.004 | -12.17€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 2595 | -0.144 | -484.58€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 345 | -0.195 | -105.16€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 345 | -0.195 | -105.16€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 427 | -0.004 | -12.17€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 427 | -0.004 | -12.17€ | 1 | 0 |
| 🚫 BALLENAS_TARDIAS#DOGE | 275 | -0.208 | -154.97€ | 0 | 0 |
| 🚫 BALLENAS_TARDIAS#DOGE#5min | 275 | -0.208 | -154.97€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 671 | -0.148 | -40.89€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 671 | -0.148 | -40.89€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 723 | -0.034 | -94.93€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 723 | -0.034 | -94.93€ | 1 | 0 |
| 🚫 BALLENAS_TARDIAS#XRP | 581 | -0.215 | -88.63€ | 0 | 0 |
| 🚫 BALLENAS_TARDIAS#XRP#5min | 581 | -0.215 | -88.63€ | 1 | 0 |
| ✅ FAVORITO_CONFIRMADO | 13056 | +0.114 | -792.10€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 3200 | +0.180 | -111.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 97 | -0.106 | -47.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 7207 | +0.082 | -647.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 2552 | +0.131 | +14.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 1219 | +0.027 | -276.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 13 | -0.065 | -2.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 1202 | +0.031 | -268.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 3023 | +0.141 | -1.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 872 | +0.192 | -38.62€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 40 | -0.119 | -21.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 1200 | +0.113 | -3.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 911 | +0.139 | +62.35€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 1216 | +0.048 | -226.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 9 | -0.021 | -3.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 1206 | +0.049 | -220.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 3270 | +0.126 | -47.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 1181 | +0.160 | -23.40€ | 0 | 7 |
| 🚫 FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 1198 | +0.103 | -15.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 879 | +0.116 | -0.02€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 3114 | +0.134 | -200.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 1113 | +0.196 | -45.35€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 39 | +0.012 | -7.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 1200 | +0.078 | -99.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 762 | +0.137 | -47.52€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 1214 | +0.117 | -41.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 12 | +0.043 | +1.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 1201 | +0.118 | -41.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3277 | +0.163 | -302.43€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 3277 | +0.163 | -302.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 823 | +0.158 | -102.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 823 | +0.158 | -102.35€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 70 | -0.069 | -1.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 70 | -0.069 | -1.64€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 815 | +0.157 | -103.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 815 | +0.157 | -103.97€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 724 | +0.219 | -38.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 724 | +0.219 | -38.33€ | 0 | 2 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 2 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 766 | +0.178 | -69.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 766 | +0.178 | -69.89€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 157 | +0.412 | -9.29€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 157 | +0.412 | -9.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 57 | +0.415 | -1.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 57 | +0.415 | -1.78€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 60 | +0.371 | -7.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 60 | +0.371 | -7.73€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 38 | +0.425 | +0.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 38 | +0.425 | +0.18€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 5154 | +0.189 | -477.81€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 5154 | +0.189 | -477.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 974 | +0.095 | -219.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 974 | +0.095 | -219.22€ | 0 | 1 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 796 | +0.251 | -4.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 796 | +0.251 | -4.59€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 913 | +0.144 | -144.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 913 | +0.144 | -144.06€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 837 | +0.222 | -34.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 837 | +0.222 | -34.68€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 793 | +0.247 | -7.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 793 | +0.247 | -7.95€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 841 | +0.200 | -67.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 841 | +0.200 | -67.31€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1832 | +0.151 | +103.04€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 1832 | +0.151 | +103.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 912 | +0.154 | +58.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 912 | +0.154 | +58.07€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 920 | +0.147 | +44.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 920 | +0.147 | +44.97€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 520 | +0.295 | -1.80€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 520 | +0.295 | -1.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 218 | +0.268 | -11.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 218 | +0.268 | -11.70€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 242 | +0.295 | +3.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 242 | +0.295 | +3.44€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 60 | +0.371 | +6.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 60 | +0.371 | +6.46€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 218 | +0.405 | -12.46€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 218 | +0.405 | -12.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 98 | +0.400 | -6.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 98 | +0.400 | -6.41€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 96 | +0.408 | -6.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 96 | +0.408 | -6.19€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 24 | +0.346 | +0.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 24 | +0.346 | +0.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 235 | +0.255 | -29.59€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 235 | +0.255 | -29.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 235 | +0.255 | -29.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 235 | +0.255 | -29.59€ | 0 | 4 |
| ✅ GBM_LATE_15M | 4233 | +0.089 | +1475.15€ | 0 | 15 |
| ✅ GBM_LATE_15M#15min | 4233 | +0.089 | +1475.15€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 733 | +0.173 | +452.26€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 733 | +0.173 | +452.26€ | 0 | 18 |
| ✅ GBM_LATE_15M#BTC | 395 | +0.170 | +173.96€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 395 | +0.170 | +173.96€ | 0 | 21 |
| ✅ GBM_LATE_15M#DOGE | 734 | +0.193 | +505.44€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 734 | +0.193 | +505.44€ | 0 | 18 |
| ✅ GBM_LATE_15M#ETH | 570 | +0.004 | +24.04€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 570 | +0.004 | +24.04€ | 0 | 3 |
| ✅ GBM_LATE_15M#SOL | 816 | +0.011 | +85.12€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 816 | +0.011 | +85.12€ | 3 | 3 |
| ✅ GBM_LATE_15M#XRP | 985 | +0.031 | +234.33€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 985 | +0.031 | +234.33€ | 0 | 3 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 5235 | +0.052 | +1567.29€ | 0 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 5235 | +0.052 | +1567.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 1006 | -0.026 | +194.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 1006 | -0.026 | +194.24€ | 1 | 2 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 991 | -0.001 | +119.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 991 | -0.001 | +119.47€ | 0 | 2 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 627 | +0.239 | +571.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 627 | +0.239 | +571.08€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 912 | -0.009 | +22.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 912 | -0.009 | +22.42€ | 5 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 942 | +0.004 | +83.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 942 | +0.004 | +83.63€ | 0 | 1 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 757 | +0.201 | +576.45€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 757 | +0.201 | +576.45€ | 0 | 18 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 3047 | +0.176 | +2063.28€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 3047 | +0.176 | +2063.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 543 | +0.190 | +388.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 543 | +0.190 | +388.92€ | 0 | 17 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 394 | +0.197 | +264.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 394 | +0.197 | +264.00€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 539 | +0.208 | +431.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 539 | +0.208 | +431.81€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 366 | +0.223 | +278.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 366 | +0.223 | +278.89€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 583 | +0.073 | +234.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 583 | +0.073 | +234.93€ | 1 | 11 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 622 | +0.189 | +464.74€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 622 | +0.189 | +464.74€ | 0 | 20 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 519 | +0.041 | +43.16€ | 0 | 6 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 519 | +0.041 | +43.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 87 | +0.051 | -1.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 87 | +0.051 | -1.04€ | 2 | 7 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 111 | +0.164 | +45.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 111 | +0.164 | +45.68€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 224 | -0.013 | +3.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 224 | -0.013 | +3.57€ | 4 | 2 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 97 | +0.015 | -5.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 97 | +0.015 | -5.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO | 3554 | +0.168 | +2284.33€ | 0 | 17 |
| ✅ GBM_LATE_15M_TARDIO#15min | 3554 | +0.168 | +2284.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 704 | +0.184 | +485.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 704 | +0.184 | +485.23€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 464 | +0.150 | +239.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 464 | +0.150 | +239.82€ | 1 | 21 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 704 | +0.227 | +606.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 704 | +0.227 | +606.97€ | 0 | 16 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 303 | +0.113 | +118.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 303 | +0.113 | +118.72€ | 1 | 20 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 584 | +0.075 | +232.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 584 | +0.075 | +232.39€ | 2 | 15 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 795 | +0.198 | +601.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 795 | +0.198 | +601.21€ | 0 | 21 |
| ✅ GBM_LATE_5M | 178 | +0.056 | +19.86€ | 2 | 6 |
| ✅ GBM_LATE_5M#5min | 178 | +0.056 | +19.86€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 86 | +0.045 | +3.90€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 86 | +0.045 | +3.90€ | 0 | 7 |
| ✅ GBM_LATE_5M#ETH | 40 | +0.167 | +15.81€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 40 | +0.167 | +15.81€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL | 42 | -0.068 | -1.47€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 42 | -0.068 | -1.47€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP | 10 | +0.083 | +1.62€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 10 | +0.083 | +1.62€ | 0 | 0 |
| ✅ GBM_LATE_60M | 481 | -0.051 | +55.91€ | 4 | 6 |
| ✅ GBM_LATE_60M#60min | 481 | -0.051 | +55.91€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 167 | -0.003 | +6.30€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 167 | -0.003 | +6.30€ | 2 | 3 |
| ✅ GBM_LATE_60M#ETH | 170 | -0.035 | +32.45€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 170 | -0.035 | +32.45€ | 1 | 7 |
| ✅ GBM_LATE_60M#SOL | 144 | -0.123 | +17.15€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 144 | -0.123 | +17.15€ | 2 | 1 |
| 🚫 GBM_LATE_60M_FADE | 189 | -0.301 | -32.44€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 189 | -0.301 | -32.44€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 75 | -0.253 | -6.85€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 75 | -0.253 | -6.85€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 64 | -0.348 | -18.54€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 64 | -0.348 | -18.54€ | 2 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 50 | -0.288 | -7.05€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 50 | -0.288 | -7.05€ | 1 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 297 | +0.052 | +11.71€ | 0 | 2 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 297 | +0.052 | +11.71€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 116 | +0.017 | +5.71€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 116 | +0.017 | +5.71€ | 2 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 65 | +0.142 | +9.31€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 65 | +0.142 | +9.31€ | 0 | 2 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 116 | +0.034 | -3.31€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 116 | +0.034 | -3.31€ | 1 | 5 |
| ✅ LEADLAG_BTC_XRP_15M | 44 | +0.130 | +8.50€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 44 | +0.130 | +8.50€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 44 | +0.130 | +8.50€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 44 | +0.130 | +8.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M | 202 | -0.113 | -29.52€ | 6 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 202 | -0.113 | -29.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 48 | -0.120 | -8.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 48 | -0.120 | -8.11€ | 1 | 0 |
| 🚫 LIQUIDACIONES_15M#DOGE | 22 | -0.208 | -5.32€ | 0 | 0 |
| 🚫 LIQUIDACIONES_15M#DOGE#15min | 22 | -0.208 | -5.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 42 | -0.023 | -2.84€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 42 | -0.023 | -2.84€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 39 | -0.037 | -2.70€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 39 | -0.037 | -2.70€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 46 | -0.167 | -8.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 46 | -0.167 | -8.95€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 75 | -0.162 | -13.48€ | 2 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 75 | -0.162 | -13.48€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 21 | -0.109 | -2.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 21 | -0.109 | -2.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE | 8 | -0.040 | -1.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 8 | -0.040 | -1.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 16 | -0.089 | -2.24€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 16 | -0.089 | -2.24€ | 0 | 0 |
| 🚫 LIQUIDACIONES_5M#SOL | 15 | -0.199 | -4.64€ | 0 | 0 |
| 🚫 LIQUIDACIONES_5M#SOL#5min | 15 | -0.199 | -4.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 14 | -0.131 | -3.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 14 | -0.131 | -3.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M | 291 | +0.012 | -2.30€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 291 | +0.012 | -2.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 99 | -0.005 | -7.41€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 99 | -0.005 | -7.41€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 93 | +0.016 | +1.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 93 | +0.016 | +1.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 99 | +0.025 | +3.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 99 | +0.025 | +3.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M | 306 | +0.058 | +22.27€ | 1 | 8 |
| ✅ MOMENTUM_IBS_15M#15min | 306 | +0.058 | +22.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 50 | +0.019 | +4.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 50 | +0.019 | +4.10€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 50 | +0.077 | +5.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 50 | +0.077 | +5.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 50 | +0.019 | -2.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 50 | +0.019 | -2.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 51 | +0.141 | +18.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 51 | +0.141 | +18.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 53 | +0.009 | -3.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 53 | +0.009 | -3.54€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 52 | +0.074 | +0.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 52 | +0.074 | +0.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 321 | +0.026 | +36.94€ | 3 | 3 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 321 | +0.026 | +36.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 52 | +0.056 | +26.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 52 | +0.056 | +26.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 53 | -0.045 | -4.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 53 | -0.045 | -4.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 55 | +0.079 | +10.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 55 | +0.079 | +10.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 53 | +0.064 | +4.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 53 | +0.064 | +4.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 53 | -0.027 | -2.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 53 | -0.027 | -2.00€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 55 | +0.026 | +1.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 55 | +0.026 | +1.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 210 | -0.108 | -25.70€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 210 | -0.108 | -25.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 25 | -0.093 | -3.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 25 | -0.093 | -3.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 39 | -0.110 | -4.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 39 | -0.110 | -4.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 26 | -0.143 | -4.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 26 | -0.143 | -4.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 47 | -0.153 | -8.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 47 | -0.153 | -8.12€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 39 | -0.061 | -2.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 39 | -0.061 | -2.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 34 | -0.056 | -2.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 34 | -0.056 | -2.24€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 797 | +0.008 | +13.83€ | 0 | 1 |
| ✅ MOMENTUM_IBS_5M#5min | 797 | +0.008 | +13.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 108 | -0.027 | -0.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 108 | -0.027 | -0.17€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC | 140 | +0.014 | -3.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 140 | +0.014 | -3.10€ | 1 | 2 |
| ✅ MOMENTUM_IBS_5M#DOGE | 105 | +0.023 | +3.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 105 | +0.023 | +3.06€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#ETH | 154 | +0.006 | +5.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 154 | +0.006 | +5.18€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#SOL | 158 | +0.031 | +13.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 158 | +0.031 | +13.85€ | 0 | 3 |
| ✅ MOMENTUM_IBS_5M#XRP | 132 | -0.007 | -5.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 132 | -0.007 | -5.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 746 | -0.041 | -25.14€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 746 | -0.041 | -25.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 111 | -0.031 | +12.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 111 | -0.031 | +12.91€ | 2 | 3 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 139 | -0.046 | -7.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 139 | -0.046 | -7.26€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 126 | -0.039 | -15.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 126 | -0.039 | -15.75€ | 5 | 1 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 109 | -0.113 | -15.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 109 | -0.113 | -15.34€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 134 | -0.015 | +4.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 134 | -0.015 | +4.82€ | 5 | 4 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 127 | -0.012 | -4.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 127 | -0.012 | -4.53€ | 4 | 2 |
| ✅ MOMENTUM_IBS_5M_FADE | 848 | +0.015 | +4.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 848 | +0.015 | +4.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 137 | +0.054 | +10.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 137 | +0.054 | +10.94€ | 0 | 1 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 134 | +0.037 | -0.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 134 | +0.037 | -0.71€ | 2 | 2 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 141 | -0.004 | -2.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 141 | -0.004 | -2.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 152 | +0.006 | -0.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 152 | +0.006 | -0.10€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 146 | -0.027 | -5.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 146 | -0.027 | -5.16€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 138 | +0.029 | +1.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 138 | +0.029 | +1.94€ | 0 | 1 |
| ✅ ORDER_FLOW_5M | 200 | +0.069 | +27.53€ | 1 | 3 |
| ✅ ORDER_FLOW_5M#5min | 64 | +0.091 | +14.94€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 15 | +0.199 | +14.80€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 15 | +0.199 | +14.80€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE | 12 | +0.000 | +0.12€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 12 | +0.000 | +0.12€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL | 19 | +0.023 | -0.91€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 19 | +0.023 | -0.91€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP | 15 | +0.022 | -0.45€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 15 | +0.022 | -0.45€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 215 | -0.131 | -6.45€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 87 | -0.174 | -18.74€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 74 | -0.184 | -15.78€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 13 | -0.065 | -2.96€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 86 | -0.136 | -1.92€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 71 | -0.144 | -3.15€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 15 | -0.066 | +1.23€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 42 | -0.023 | +14.21€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 37 | +0.013 | +15.46€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 5 | -0.054 | -1.25€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 182 | -0.130 | -3.47€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 33 | -0.129 | -2.99€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 109 | -0.275 | -25.44€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 45 | -0.202 | -6.50€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 43 | -0.189 | -5.48€ | 1 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 49 | -0.265 | -11.29€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 47 | -0.255 | -10.27€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL | 15 | -0.331 | -7.65€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#atexpiry | 14 | -0.306 | -7.14€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 104 | -0.264 | -22.89€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 5 | -0.089 | -2.55€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 48 | +0.240 | +4.75€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC | 17 | -0.022 | -2.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 17 | -0.022 | -2.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 15 | +0.199 | +1.27€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 15 | +0.199 | +1.27€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 16 | +0.356 | +6.43€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 16 | +0.356 | +6.43€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#sniper | 48 | +0.240 | +4.75€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 33 | -0.129 | -10.93€ | 0 | 0 |
| ✅ STREAK_FADE_15M#15min | 33 | -0.129 | -10.93€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 16 | -0.044 | -4.12€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 16 | -0.044 | -4.12€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP | 14 | -0.131 | -5.62€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 14 | -0.131 | -5.62€ | 0 | 0 |
| ✅ STREAK_FADE_5M | 302 | -0.036 | -22.15€ | 2 | 1 |
| ✅ STREAK_FADE_5M#5min | 302 | -0.036 | -22.15€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 66 | +0.029 | +1.83€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 66 | +0.029 | +1.83€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 111 | -0.013 | -7.03€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 111 | -0.013 | -7.03€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 58 | -0.083 | -8.21€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 58 | -0.083 | -8.21€ | 1 | 0 |
| ✅ STREAK_FADE_5M#XRP | 67 | -0.094 | -8.73€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 67 | -0.094 | -8.73€ | 2 | 0 |
| ✅ STREAK_FADE_60M | 15 | -0.066 | -1.71€ | 0 | 0 |
| ✅ STREAK_FADE_60M#60min | 15 | -0.066 | -1.71€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 9 | -0.061 | -1.63€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 9 | -0.061 | -1.63€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 513 | +0.034 | +11.33€ | 0 | 2 |
| ✅ STREAK_MOM_5M#5min | 513 | +0.034 | +11.33€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 152 | +0.013 | -0.31€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 152 | +0.013 | -0.31€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 109 | +0.013 | +1.76€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 109 | +0.013 | +1.76€ | 1 | 2 |
| ✅ STREAK_MOM_5M#SOL | 133 | +0.041 | +1.65€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 133 | +0.041 | +1.65€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP | 119 | +0.070 | +8.22€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 119 | +0.070 | +8.22€ | 1 | 2 |
| ✅ STRUCT_NO_15M | 1749 | +0.012 | -10.69€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 1749 | +0.012 | -10.69€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 666 | +0.007 | -7.44€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 666 | +0.007 | -7.44€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 697 | +0.014 | -3.00€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 697 | +0.014 | -3.00€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 386 | +0.015 | -0.25€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 386 | +0.015 | -0.25€ | 2 | 0 |
| ✅ UPDOWN_GBM | 1777 | +0.026 | +124.97€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 791 | +0.103 | +171.06€ | 1 | 11 |
| ✅ UPDOWN_GBM#240min | 110 | +0.036 | +2.36€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 583 | -0.038 | -37.29€ | 5 | 0 |
| ✅ UPDOWN_GBM#60min | 246 | -0.024 | -10.64€ | 2 | 1 |
| ✅ UPDOWN_GBM#BNB | 71 | +0.075 | +9.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 65 | +0.097 | +10.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 315 | -0.005 | -11.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 115 | +0.056 | -3.88€ | 1 | 6 |
| ✅ UPDOWN_GBM#BTC#240min | 32 | +0.088 | +3.11€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 65 | -0.037 | -2.86€ | 2 | 1 |
| ✅ UPDOWN_GBM#BTC#60min | 85 | -0.063 | -9.73€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 238 | +0.021 | +12.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 46 | +0.208 | +25.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 192 | -0.026 | -13.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 424 | +0.054 | +46.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 191 | +0.137 | +50.70€ | 1 | 16 |
| ✅ UPDOWN_GBM#ETH#240min | 33 | +0.071 | +1.51€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 88 | -0.033 | -3.68€ | 3 | 1 |
| ✅ UPDOWN_GBM#ETH#60min | 97 | +0.005 | -1.72€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 318 | +0.003 | +9.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 123 | +0.044 | +9.41€ | 1 | 6 |
| ✅ UPDOWN_GBM#SOL#240min | 28 | +0.000 | -0.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 91 | -0.005 | +0.04€ | 2 | 4 |
| ✅ UPDOWN_GBM#SOL#60min | 64 | -0.015 | +0.81€ | 2 | 0 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 409 | +0.035 | +60.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 251 | +0.105 | +78.45€ | 0 | 16 |
| ✅ UPDOWN_GBM#XRP#240min | 16 | -0.089 | -2.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 142 | -0.069 | -15.97€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 102 | +0.231 | -6.04€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 102 | +0.231 | -6.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 67 | +0.196 | -11.69€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 67 | +0.196 | -11.69€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 35 | +0.284 | +5.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 35 | +0.284 | +5.65€ | 0 | 1 |
| ✅ UPDOWN_GBM_15M_TARDIO | 1513 | -0.042 | +173.74€ | 2 | 2 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 1513 | -0.042 | +173.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 95 | -0.077 | -2.62€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 95 | -0.077 | -2.62€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 301 | -0.134 | -0.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 301 | -0.134 | -0.56€ | 3 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 35 | -0.041 | -2.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 35 | -0.041 | -2.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 124 | +0.000 | +20.83€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 124 | +0.000 | +20.83€ | 2 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 483 | +0.003 | +98.39€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 483 | +0.003 | +98.39€ | 1 | 1 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 475 | -0.033 | +59.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 475 | -0.033 | +59.74€ | 3 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 5 | -0.054 | -1.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 5 | -0.054 | -1.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 5 | -0.054 | -1.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 5 | -0.054 | -1.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 132 | +0.239 | +57.14€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 132 | +0.239 | +57.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 83 | +0.218 | +25.60€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 83 | +0.218 | +25.60€ | 0 | 14 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 49 | +0.265 | +31.54€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 49 | +0.265 | +31.54€ | 0 | 8 |
| ✅ UPDOWN_OU_5M | 311 | -0.062 | -24.92€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 311 | -0.062 | -24.92€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 200 | -0.015 | -12.34€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 200 | -0.015 | -12.34€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 17 | +0.067 | +3.83€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 17 | +0.067 | +3.83€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#DOGE | 15 | -0.154 | -3.57€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#DOGE#5min | 15 | -0.154 | -3.57€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 28 | -0.167 | -4.42€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 28 | -0.167 | -4.42€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 28 | -0.200 | -4.70€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 28 | -0.200 | -4.70€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 23 | -0.140 | -3.72€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 23 | -0.140 | -3.72€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 910 | +0.285 | +386.45€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 270 | +0.199 | +8.22€ | 0 | 2 |
| ✅ WEEKLY_PRICE#ETH | 289 | +0.256 | +69.14€ | 0 | 1 |
| ✅ WEEKLY_PRICE#SOL | 351 | +0.372 | +309.10€ | 0 | 1 |