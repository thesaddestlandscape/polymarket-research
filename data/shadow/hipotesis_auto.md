# Hipótesis automáticas — 2026-09-05 22:28 UTC
_Generado por shadow_postmortem.py sobre 301442 resoluciones (PNL=+29478.96€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.705` → IC=-0.141 (n=143)

  - _Acción_: SKIP cuando `py_entrada` < 0.705
  - _Potencial_: sin este filtro IC_bueno=+0.268 (n=325)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.392 (n=81)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.133 (n=328)

- **PATRÓN** `py_entrada` > `0.705` → IC=+0.268 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.705 (IC base=+0.143)

- **PATRÓN** `n_ballena_banda` > `20.0` → IC=+0.142 (n=314)

  - _Acción_: Kelly boost +0.71€ cuando `n_ballena_banda` > 20.0 (IC base=+0.143)

- **PATRÓN** `n_total_lado` > `72.0` → IC=+0.245 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 72.0 (IC base=+0.143)

- **PATRÓN** `banda_hit_calibrado` > `0.6174` → IC=+0.239 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6174 (IC base=+0.143)

- **PATRÓN** `banda_z` > `11.557` → IC=+0.273 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.557 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.172 (n=242)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 11.0 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.165 (n=365)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `3111.6433` → IC=+0.185 (n=160)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 3111.6433 (IC base=+0.143)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.133 (n=328)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.5 (IC base=+0.028)

- **PATRÓN** `ballena_activa_n` < `124.0` → IC=+0.132 (n=104)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 124.0 (IC base=+0.028)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=198)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=223)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.267 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.168)

- **PATRÓN** `n_total_lado` > `68.0` → IC=+0.240 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 68.0 (IC base=+0.168)

- **PATRÓN** `banda_hit_calibrado` > `0.6183` → IC=+0.262 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6183 (IC base=+0.168)

- **PATRÓN** `banda_z` > `11.557` → IC=+0.271 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.557 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.203 (n=180)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.168)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.183 (n=285)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `2957.7064` → IC=+0.178 (n=169)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 2957.7064 (IC base=+0.168)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.125 (n=198)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.495 (IC base=+0.020)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.250 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 93.0 (IC base=+0.020)

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

- **FILTRO** `n_ballena_banda` < `30.0` → IC=-0.128 (n=49)

  - _Acción_: SKIP cuando `n_ballena_banda` < 30.0
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=52)

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
- **FILTRO** `restante_s_al_confirmar` < `147.55` → IC=-0.300 (n=4024)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 147.55
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=12073)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `132.7` → IC=-0.325 (n=545)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 132.7
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=1636)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` > `628.69` → IC=-0.158 (n=337)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` > 628.69
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=657)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `119.1` → IC=-0.399 (n=531)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 119.1
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=1593)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `157.35` → IC=-0.159 (n=1066)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 157.35
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=3198)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `145.55` → IC=-0.311 (n=899)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 145.55
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=2700)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `160.75` → IC=-0.374 (n=967)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 160.75
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=1968)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.7` → IC=+0.192 (n=8403)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.7 (IC base=+0.097)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.162 (n=2159)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `2364.1007` → IC=+0.163 (n=2070)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2364.1007 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.146 (n=6038)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.150 (n=7084)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 7.0 (IC base=+0.138)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.253 (n=5323)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.179 (n=4141)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.02 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `1939.4936` → IC=+0.171 (n=3547)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 1939.4936 (IC base=+0.138)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.214 (n=928)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.205 (n=946)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.785` → IC=+0.372 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.785 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.203 (n=1182)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `13015.441` → IC=+0.218 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13015.441 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.202 (n=891)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.201 (n=981)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.288 (n=669)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.192 (n=1255)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.01 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `12435.1084` → IC=+0.204 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12435.1084 (IC base=+0.191)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.126 (n=693)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 5.0 (IC base=+0.111)

- **PATRÓN** `py_entrada` > `0.62` → IC=+0.173 (n=221)

  - _Acción_: Kelly boost +0.86€ cuando `py_entrada` > 0.62 (IC base=+0.111)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.130 (n=271)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `4800.0243` → IC=+0.151 (n=216)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4800.0243 (IC base=+0.111)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.190 (n=224)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 7.0 (IC base=+0.131)

- **PATRÓN** `py_entrada` < `0.41` → IC=+0.180 (n=348)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.41 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `4061.5587` → IC=+0.159 (n=332)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 4061.5587 (IC base=+0.131)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=105)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=1757)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.138 (n=1475)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 15.0 (IC base=+0.132)

- **PATRÓN** `py_entrada` > `0.69` → IC=+0.308 (n=587)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.259 (n=683)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.252)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.253 (n=780)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.252)

- **PATRÓN** `py_entrada` < `0.205` → IC=+0.393 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.205 (IC base=+0.252)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.257 (n=783)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.252)

- **PATRÓN** `libro_liquidez` > `1926.6564` → IC=+0.267 (n=745)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1926.6564 (IC base=+0.252)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.139 (n=377)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 7.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.143 (n=362)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 15.0 (IC base=+0.133)

- **PATRÓN** `py_entrada` > `0.66` → IC=+0.263 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.66 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.145 (n=485)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.02 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `1771.1035` → IC=+0.150 (n=361)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1771.1035 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `4449.086` → IC=+0.167 (n=145)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 4449.086 (IC base=+0.076)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.214 (n=417)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.84` → IC=+0.424 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.84 (IC base=+0.182)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.198 (n=756)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 7.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.197 (n=848)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 17.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` < `0.235` → IC=+0.340 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.235 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.204 (n=727)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `939.5107` → IC=+0.196 (n=831)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 939.5107 (IC base=+0.195)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.201 (n=105)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.169)

- **PATRÓN** `py_entrada` > `0.725` → IC=+0.332 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.725 (IC base=+0.169)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.186 (n=173)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.02 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `3435.4625` → IC=+0.176 (n=69)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 3435.4625 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.127 (n=558)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 7.0 (IC base=+0.111)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.226 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.111)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.142 (n=300)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.02 (IC base=+0.111)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.8` → IC=-0.344 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=129)

- **FILTRO** `libro_liquidez` < `11360.7096` → IC=-0.266 (n=143)

  - _Acción_: SKIP cuando `libro_liquidez` < 11360.7096
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=48)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.197 (n=6632)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.198 (n=5590)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 15.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.205 (n=3178)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `5949.6974` → IC=+0.304 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5949.6974 (IC base=+0.191)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.182 (n=1440)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 15.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.181 (n=1698)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.74 (IC base=+0.168)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.400 (n=38)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.296)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.329 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.296)

- **PATRÓN** `libro_liquidez` > `5339.6996` → IC=+0.300 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5339.6996 (IC base=+0.296)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.179 (n=1591)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 6.0 (IC base=+0.173)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.181 (n=1408)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.173)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.174 (n=1694)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.74 (IC base=+0.173)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.188 (n=1131)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.72 (IC base=+0.173)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.246 (n=1423)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.235)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.237 (n=1269)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.235)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.315 (n=537)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.198 (n=1622)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.192 (n=1376)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.186)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.193 (n=835)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.7 (IC base=+0.186)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.187 (n=698)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.73 (IC base=+0.186)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.448 (n=304)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.441)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.443 (n=279)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.481 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.441)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.439 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.441)

- **PATRÓN** `libro_liquidez` > `8027.017` → IC=+0.453 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8027.017 (IC base=+0.441)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.443 (n=121)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.439 (n=113)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.450 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.439)

- **PATRÓN** `libro_liquidez` > `10827.9786` → IC=+0.464 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10827.9786 (IC base=+0.439)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.450 (n=117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.452 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.438)

- **PATRÓN** `libro_liquidez` > `2350.8723` → IC=+0.446 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2350.8723 (IC base=+0.438)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.426 (n=66)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.428)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.462 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.428)

- **PATRÓN** `py_entrada` < `0.932` → IC=+0.423 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.932 (IC base=+0.428)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.433 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.428)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `3.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.194 (n=18822)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 8.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.210 (n=19071)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.191)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.159 (n=3699)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 6.0 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.156 (n=2631)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 12.0 (IC base=+0.154)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.179 (n=3318)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` > 0.71 (IC base=+0.154)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.229 (n=1643)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.228 (n=1212)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.259 (n=2408)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.225)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.181 (n=1207)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 18.0 (IC base=+0.166)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.167 (n=2532)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 12.0 (IC base=+0.166)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=3317)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.166)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.231 (n=1688)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.227 (n=1231)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.274 (n=1196)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.221)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.216 (n=1146)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.241 (n=1617)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.202)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.187 (n=3160)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 8.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.189 (n=2472)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 12.0 (IC base=+0.184)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.236 (n=1334)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.184)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.206 (n=2707)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.129)

- **PATRÓN** `restante_min` < `4.0` → IC=+0.138 (n=2519)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` < 4.0 (IC base=+0.129)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.158 (n=2533)

  - _Acción_: Kelly boost +0.79€ cuando `restante_min` > 4.94 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.145 (n=3688)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 8.0 (IC base=+0.129)

- **PATRÓN** `lag_apertura_s` < `3.85` → IC=+0.157 (n=2521)

  - _Acción_: Kelly boost +0.79€ cuando `lag_apertura_s` < 3.85 (IC base=+0.129)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.212 (n=1352)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.135)

- **PATRÓN** `restante_min` < `3.95` → IC=+0.145 (n=1250)

  - _Acción_: Kelly boost +0.73€ cuando `restante_min` < 3.95 (IC base=+0.135)

- **PATRÓN** `restante_min` > `4.88` → IC=+0.150 (n=1737)

  - _Acción_: Kelly boost +0.75€ cuando `restante_min` > 4.88 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.153 (n=2643)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 12.0 (IC base=+0.135)

- **PATRÓN** `lag_apertura_s` < `6.89` → IC=+0.149 (n=1646)

  - _Acción_: Kelly boost +0.74€ cuando `lag_apertura_s` < 6.89 (IC base=+0.135)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.200 (n=1355)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.123)

- **PATRÓN** `restante_min` < `4.44` → IC=+0.128 (n=1685)

  - _Acción_: Kelly boost +0.64€ cuando `restante_min` < 4.44 (IC base=+0.123)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.165 (n=1280)

  - _Acción_: Kelly boost +0.83€ cuando `restante_min` > 4.95 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.124 (n=3831)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.132 (n=1874)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 8.0 (IC base=+0.123)

- **PATRÓN** `lag_apertura_s` < `3.29` → IC=+0.166 (n=1275)

  - _Acción_: Kelly boost +0.83€ cuando `lag_apertura_s` < 3.29 (IC base=+0.123)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.319 (n=538)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.291)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.379 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `1731.8091` → IC=+0.295 (n=750)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1731.8091 (IC base=+0.291)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.294 (n=290)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.277)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.278 (n=124)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.277)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.356 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.277)

- **PATRÓN** `libro_liquidez` > `5497.3627` → IC=+0.291 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5497.3627 (IC base=+0.277)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.340 (n=248)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.295)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.374 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.295)

- **PATRÓN** `libro_liquidez` > `1710.7648` → IC=+0.321 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1710.7648 (IC base=+0.295)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.331 (n=75)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.325)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.353 (n=66)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.325)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.370 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.325)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.346 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.325)

- **PATRÓN** `libro_liquidez` > `763.8012` → IC=+0.364 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 763.8012 (IC base=+0.325)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.437 (n=346)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.422)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.429 (n=293)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.422)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.428 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.422)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.433 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.422)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.424 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.422)

- **PATRÓN** `libro_liquidez` > `1978.5089` → IC=+0.435 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1978.5089 (IC base=+0.422)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.433 (n=148)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.419)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.428 (n=150)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.419)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.424 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.419)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.428 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.419)

- **PATRÓN** `libro_liquidez` > `5433.9622` → IC=+0.461 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5433.9622 (IC base=+0.419)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.436 (n=154)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.426)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.439 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.426)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.429 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.426)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.428 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.426)

- **PATRÓN** `libro_liquidez` > `1953.4041` → IC=+0.452 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1953.4041 (IC base=+0.426)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` < `12.0` → IC=+0.364 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.372)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.444 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.372)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.311 (n=167)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.255)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.407 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.255)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.273 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.255)

- **PATRÓN** `libro_liquidez` > `1063.7596` → IC=+0.269 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1063.7596 (IC base=+0.255)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.311 (n=167)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.255)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.407 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.255)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.273 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.255)

- **PATRÓN** `libro_liquidez` > `1063.7596` → IC=+0.269 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1063.7596 (IC base=+0.255)

### GBM_LATE_15M
- **PATRÓN** `ibs_20min` > `0.9517` → IC=+0.212 (n=1344)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9517 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.2583` → IC=+0.226 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2583 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` < `0.1712` → IC=+0.226 (n=665)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1712 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.733` → IC=+0.155 (n=1543)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 5.733 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` < `0.7026` → IC=+0.234 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7026 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` > `1.0844` → IC=+0.242 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0844 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.1712` → IC=+0.191 (n=711)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.1712 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` < `2.8651` → IC=+0.182 (n=2461)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 2.8651 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `1.4721` → IC=+0.180 (n=2461)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.4721 (IC base=+0.087)

- **PATRÓN** `ibs_20min` < `0.402` → IC=+0.126 (n=3839)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` < 0.402 (IC base=+0.041)

- **PATRÓN** `dist_vwap_pct` < `0.3335` → IC=+0.142 (n=1430)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.3335 (IC base=+0.041)

- **PATRÓN** `volumen_regimen` < `0.8548` → IC=+0.144 (n=923)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.8548 (IC base=+0.041)

- **PATRÓN** `volumen_regimen` > `1.0494` → IC=+0.145 (n=627)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 1.0494 (IC base=+0.041)

- **PATRÓN** `volumen_pendiente_norm` > `0.1721` → IC=+0.226 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1721 (IC base=+0.041)

- **PATRÓN** `volumen_spike_ratio` > `1.9355` → IC=+0.195 (n=1446)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 1.9355 (IC base=+0.041)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.217 (n=860)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.041)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.197 (n=305)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0076 (IC base=+0.162)

- **PATRÓN** `drift_60min` |x|≤ `0.2955` → IC=+0.167 (n=906)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.2955 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.201 (n=430)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.162)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.270 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.663` → IC=+0.281 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.663 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` > `0.23` → IC=+0.239 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.23 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` < `2.6507` → IC=+0.151 (n=808)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.6507 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` > `1.5555` → IC=+0.155 (n=722)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.5555 (IC base=+0.162)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.198 (n=764)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.162)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.194 (n=370)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 43.0 (IC base=+0.162)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.249 (n=417)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.241)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.254 (n=558)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.1822` → IC=+0.290 (n=417)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1822 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.244 (n=573)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.248 (n=625)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.4122` → IC=+0.275 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4122 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.393` → IC=+0.259 (n=629)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.393 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` < `0.0688` → IC=+0.237 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0688 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.2883` → IC=+0.338 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2883 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `2.8125` → IC=+0.298 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8125 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.262 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `1724.5869` → IC=+0.258 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1724.5869 (IC base=+0.241)

- **PATRÓN** `ballena_activa_n` < `67.0` → IC=+0.241 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 67.0 (IC base=+0.241)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.247 (n=310)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.214)

- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.220 (n=234)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0066 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.2029` → IC=+0.232 (n=468)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2029 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.233 (n=706)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` > `0.3717` → IC=+0.226 (n=701)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3717 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` > `0.8265` → IC=+0.218 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8265 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` < `0.4548` → IC=+0.216 (n=645)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4548 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.309` → IC=+0.228 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.309 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` < `1.2524` → IC=+0.220 (n=701)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2524 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` > `1.0855` → IC=+0.225 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0855 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` < `0.0983` → IC=+0.216 (n=663)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0983 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` < `1.4797` → IC=+0.243 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4797 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `10981.291` → IC=+0.237 (n=701)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10981.291 (IC base=+0.214)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.153 (n=758)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0061 (IC base=+0.144)

- **PATRÓN** `sigma_h` > `0.0029` → IC=+0.148 (n=677)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0029 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.0782` → IC=+0.161 (n=252)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.0782 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.147 (n=678)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 8.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.146 (n=535)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 12.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.6604` → IC=+0.170 (n=756)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.6604 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` < `0.1366` → IC=+0.170 (n=643)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.1366 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.516` → IC=+0.229 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.516 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `0.6125` → IC=+0.165 (n=252)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.6125 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.1496` → IC=+0.211 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1496 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `1.7274` → IC=+0.164 (n=432)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.7274 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.4035` → IC=+0.162 (n=648)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.4035 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `12567.3384` → IC=+0.150 (n=504)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 12567.3384 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `211.0` → IC=+0.179 (n=188)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 211.0 (IC base=+0.144)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.196 (n=287)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0097 (IC base=+0.169)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.201 (n=413)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.249 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.389` → IC=+0.278 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.389 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` < `0.104` → IC=+0.165 (n=709)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` < 0.104 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.3817` → IC=+0.161 (n=110)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.3817 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `3.1353` → IC=+0.161 (n=680)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 3.1353 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `1.8855` → IC=+0.182 (n=691)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.8855 (IC base=+0.169)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.192 (n=910)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.04 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.196 (n=544)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 48.0 (IC base=+0.169)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.230 (n=712)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.221)

- **PATRÓN** `sigma_h` > `0.0064` → IC=+0.223 (n=636)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0064 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.236 (n=351)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.234 (n=325)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` < `0.0268` → IC=+0.279 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0268 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.005` → IC=+0.234 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.005 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.3736` → IC=+0.304 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3736 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` < `1.6985` → IC=+0.214 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6985 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `2.4031` → IC=+0.211 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4031 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.235 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.221)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.207 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.221)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `ibs_20min` > `0.8166` → IC=-0.184 (n=308)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8166
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=926)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.149 (n=72)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=1162)

- **PATRÓN** `dist_vwap_pct` < `0.5765` → IC=+0.314 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5765 (IC base=-0.026)

- **PATRÓN** `volumen_regimen` < `0.5962` → IC=+0.379 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5962 (IC base=-0.026)

- **PATRÓN** `volumen_regimen` > `1.1929` → IC=+0.288 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1929 (IC base=-0.026)

- **PATRÓN** `volumen_pendiente_norm` < `0.1153` → IC=+0.283 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1153 (IC base=-0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.2291` → IC=+0.294 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2291 (IC base=-0.026)

- **PATRÓN** `volumen_spike_ratio` < `1.435` → IC=+0.375 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.435 (IC base=-0.026)

- **PATRÓN** `volumen_spike_ratio` > `1.9125` → IC=+0.287 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9125 (IC base=-0.026)

- **PATRÓN** `ballena_activa_n` < `154.0` → IC=+0.294 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 154.0 (IC base=-0.026)

- **PATRÓN** `dist_vwap_pct` > `0.1431` → IC=+0.144 (n=85)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.1431 (IC base=-0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.2781` → IC=+0.219 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2781 (IC base=-0.039)

- **PATRÓN** `volumen_spike_ratio` > `1.8136` → IC=+0.141 (n=154)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.8136 (IC base=-0.039)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.143 (n=40)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=157)

- **FILTRO** `ibs_20min` < `0.2941` → IC=-0.157 (n=65)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2941
  - _Potencial_: sin este filtro IC_bueno=+0.142 (n=132)

- **FILTRO** `sigma_ewma_delta_pct` > `8.412` → IC=-0.184 (n=213)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.412
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=1652)

- **FILTRO** `volumen_spike_ratio` > `1.4181` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.4181
  - _Potencial_: sin este filtro IC_bueno=+0.237 (n=17)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.173 (n=50)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0057 (IC base=+0.043)

- **PATRÓN** `ibs_20min` > `0.2941` → IC=+0.142 (n=132)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.2941 (IC base=+0.043)

- **PATRÓN** `dist_vwap_pct` < `0.6236` → IC=+0.312 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6236 (IC base=+0.043)

- **PATRÓN** `volumen_regimen` > `0.7776` → IC=+0.362 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7776 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` > `1.5596` → IC=+0.284 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5596 (IC base=+0.043)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.389 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `1.4181` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4181 (IC base=-0.061)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.5039` → IC=-0.158 (n=381)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.5039
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=740)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.183 (n=156)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=965)

- **FILTRO** `ibs_20min` > `0.7902` → IC=-0.193 (n=447)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7902
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=1342)

- **FILTRO** `sigma_ewma_delta_pct` > `8.947` → IC=-0.134 (n=203)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.947
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=1586)

- **PATRÓN** `dist_vwap_pct` > `0.6657` → IC=+0.342 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6657 (IC base=-0.095)

- **PATRÓN** `dist_vwap_pct` < `0.2396` → IC=+0.226 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2396 (IC base=-0.095)

- **PATRÓN** `volumen_regimen` > `0.6895` → IC=+0.273 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6895 (IC base=-0.095)

- **PATRÓN** `volumen_pendiente_norm` > `0.066` → IC=+0.321 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.066 (IC base=-0.095)

- **PATRÓN** `volumen_spike_ratio` < `1.4974` → IC=+0.250 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4974 (IC base=-0.095)

- **PATRÓN** `volumen_spike_ratio` > `2.442` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.442 (IC base=-0.095)

- **PATRÓN** `dist_vwap_pct` > `0.1575` → IC=+0.195 (n=93)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1575 (IC base=-0.047)

- **PATRÓN** `dist_vwap_pct` < `0.2336` → IC=+0.207 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2336 (IC base=-0.047)

- **PATRÓN** `volumen_regimen` > `1.0971` → IC=+0.281 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0971 (IC base=-0.047)

- **PATRÓN** `volumen_pendiente_norm` > `0.2594` → IC=+0.235 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2594 (IC base=-0.047)

- **PATRÓN** `volumen_spike_ratio` < `2.5738` → IC=+0.192 (n=154)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 2.5738 (IC base=-0.047)

- **PATRÓN** `volumen_spike_ratio` > `1.5056` → IC=+0.171 (n=153)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.5056 (IC base=-0.047)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.189 (n=101)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 22.0 (IC base=-0.047)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.173 (n=1670)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0093 (IC base=+0.079)

- **PATRÓN** `ibs_20min` > `0.3118` → IC=+0.149 (n=4995)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.3118 (IC base=+0.079)

- **PATRÓN** `dist_vwap_pct` > `1.1818` → IC=+0.293 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1818 (IC base=+0.079)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.486` → IC=+0.123 (n=2644)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` > 2.486 (IC base=+0.079)

- **PATRÓN** `volumen_regimen` > `0.682` → IC=+0.223 (n=1461)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.682 (IC base=+0.079)

- **PATRÓN** `volumen_pendiente_norm` > `0.2513` → IC=+0.250 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2513 (IC base=+0.079)

- **PATRÓN** `volumen_spike_ratio` < `1.4854` → IC=+0.233 (n=841)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4854 (IC base=+0.079)

- **PATRÓN** `volumen_spike_ratio` > `2.8017` → IC=+0.224 (n=841)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8017 (IC base=+0.079)

- **PATRÓN** `ballena_activa_n` < `102.0` → IC=+0.293 (n=1983)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 102.0 (IC base=+0.079)

- **PATRÓN** `ibs_20min` < `0.5848` → IC=+0.128 (n=4787)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` < 0.5848 (IC base=+0.051)

- **PATRÓN** `dist_vwap_pct` > `0.7641` → IC=+0.245 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7641 (IC base=+0.051)

- **PATRÓN** `dist_vwap_pct` < `0.2222` → IC=+0.218 (n=1170)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2222 (IC base=+0.051)

- **PATRÓN** `volumen_regimen` < `0.7067` → IC=+0.218 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7067 (IC base=+0.051)

- **PATRÓN** `volumen_regimen` > `1.224` → IC=+0.241 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.224 (IC base=+0.051)

- **PATRÓN** `volumen_pendiente_norm` > `0.2584` → IC=+0.336 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2584 (IC base=+0.051)

- **PATRÓN** `volumen_spike_ratio` > `2.4133` → IC=+0.257 (n=673)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4133 (IC base=+0.051)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.253 (n=1332)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 69.0 (IC base=+0.051)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.3291` → IC=-0.141 (n=419)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3291
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=853)

- **FILTRO** `sigma_ewma_delta_pct` > `2.487` → IC=-0.162 (n=374)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.487
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=821)

- **PATRÓN** `ibs_20min` > `0.8425` → IC=+0.250 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8425 (IC base=+0.037)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.685` → IC=+0.174 (n=237)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 6.685 (IC base=+0.037)

- **PATRÓN** `volumen_pendiente_norm` > `0.2202` → IC=+0.312 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2202 (IC base=+0.037)

- **PATRÓN** `volumen_spike_ratio` < `1.8686` → IC=+0.245 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8686 (IC base=+0.037)

- **PATRÓN** `volumen_spike_ratio` > `1.4726` → IC=+0.226 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4726 (IC base=+0.037)

- **PATRÓN** `ballena_activa_n` < `86.0` → IC=+0.281 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 86.0 (IC base=+0.037)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` > `0.8608` → IC=-0.156 (n=408)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8608
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=1231)

- **PATRÓN** `dist_vwap_pct` > `0.8325` → IC=+0.146 (n=97)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.8325 (IC base=-0.008)

- **PATRÓN** `volumen_spike_ratio` < `1.7029` → IC=+0.143 (n=250)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.7029 (IC base=-0.008)

- **PATRÓN** `ballena_activa_n` < `260.0` → IC=+0.139 (n=120)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 260.0 (IC base=-0.008)

- **PATRÓN** `dist_vwap_pct` < `0.1406` → IC=+0.183 (n=203)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.1406 (IC base=-0.021)

- **PATRÓN** `volumen_regimen` < `0.8421` → IC=+0.176 (n=137)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.8421 (IC base=-0.021)

- **PATRÓN** `volumen_regimen` > `1.1253` → IC=+0.200 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1253 (IC base=-0.021)

- **PATRÓN** `volumen_pendiente_norm` > `0.2573` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2573 (IC base=-0.021)

- **PATRÓN** `volumen_spike_ratio` < `1.7377` → IC=+0.225 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7377 (IC base=-0.021)

- **PATRÓN** `volumen_spike_ratio` > `1.4228` → IC=+0.185 (n=160)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.4228 (IC base=-0.021)

- **PATRÓN** `ballena_activa_n` < `262.0` → IC=+0.209 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 262.0 (IC base=-0.021)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.259 (n=723)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0062 (IC base=+0.229)

- **PATRÓN** `drift_60min` |x|≤ `0.0848` → IC=+0.234 (n=269)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0848 (IC base=+0.229)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.254 (n=384)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.229)

- **PATRÓN** `ibs_20min` > `0.712` → IC=+0.260 (n=719)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.712 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.394` → IC=+0.293 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.394 (IC base=+0.229)

- **PATRÓN** `volumen_pendiente_norm` < `0.221` → IC=+0.235 (n=749)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.221 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` < `2.3922` → IC=+0.231 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3922 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` > `1.7188` → IC=+0.235 (n=720)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7188 (IC base=+0.229)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.257 (n=847)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.229)

- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.312 (n=526)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0062 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.316 (n=394)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.289)

- **PATRÓN** `ibs_20min` < `0.35` → IC=+0.302 (n=590)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.35 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.709` → IC=+0.314 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.709 (IC base=+0.289)

- **PATRÓN** `volumen_pendiente_norm` > `0.35` → IC=+0.329 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.35 (IC base=+0.289)

- **PATRÓN** `volumen_spike_ratio` < `1.6624` → IC=+0.280 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6624 (IC base=+0.289)

- **PATRÓN** `volumen_spike_ratio` > `2.3438` → IC=+0.296 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3438 (IC base=+0.289)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.302 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `1847.3847` → IC=+0.289 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1847.3847 (IC base=+0.289)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.267 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 30.0 (IC base=+0.289)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.143 (n=250)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=572)

- **FILTRO** `ibs_20min` < `0.5867` → IC=-0.163 (n=411)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5867
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=411)

- **FILTRO** `ibs_20min` > `0.8665` → IC=-0.157 (n=319)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8665
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=960)

- **FILTRO** `volumen_regimen` > `0.8624` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8624
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=50)

- **FILTRO** `volumen_regimen` < `0.6828` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.6828
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=51)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.140 (n=84)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=1195)

- **PATRÓN** `dist_vwap_pct` > `1.3501` → IC=+0.333 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.3501 (IC base=-0.049)

- **PATRÓN** `volumen_regimen` < `0.8912` → IC=+0.170 (n=101)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.8912 (IC base=-0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.1662` → IC=+0.300 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1662 (IC base=-0.049)

- **PATRÓN** `volumen_spike_ratio` < `2.2544` → IC=+0.225 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2544 (IC base=-0.049)

- **PATRÓN** `volumen_spike_ratio` > `1.3713` → IC=+0.225 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.3713 (IC base=-0.049)

- **PATRÓN** `ballena_activa_n` < `158.0` → IC=+0.262 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 158.0 (IC base=-0.049)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.84` → IC=-0.130 (n=716)

  - _Acción_: SKIP cuando `ibs_20min` < 0.84
  - _Potencial_: sin este filtro IC_bueno=+0.290 (n=370)

- **FILTRO** `ibs_20min` > `0.75` → IC=-0.232 (n=304)

  - _Acción_: SKIP cuando `ibs_20min` > 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=923)

- **FILTRO** `sigma_ewma_delta_pct` > `4.678` → IC=-0.143 (n=306)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.678
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=921)

- **PATRÓN** `ibs_20min` > `0.84` → IC=+0.290 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.84 (IC base=+0.014)

- **PATRÓN** `dist_vwap_pct` > `0.2099` → IC=+0.299 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2099 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` < `0.8684` → IC=+0.265 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8684 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` > `1.1627` → IC=+0.280 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1627 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` < `0.1143` → IC=+0.259 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1143 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` > `0.274` → IC=+0.292 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.274 (IC base=+0.014)

- **PATRÓN** `volumen_spike_ratio` < `1.4432` → IC=+0.305 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4432 (IC base=+0.014)

- **PATRÓN** `volumen_spike_ratio` > `2.3419` → IC=+0.261 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3419 (IC base=+0.014)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.308 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 59.0 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` < `0.7154` → IC=+0.172 (n=62)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.7154 (IC base=-0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.2452` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2452 (IC base=-0.026)

- **PATRÓN** `ballena_activa_n` < `65.0` → IC=+0.164 (n=108)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 65.0 (IC base=-0.026)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0136` → IC=+0.336 (n=522)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0136 (IC base=+0.256)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.261 (n=371)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.256)

- **PATRÓN** `ibs_20min` > `0.8983` → IC=+0.326 (n=522)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8983 (IC base=+0.256)

- **PATRÓN** `dist_vwap_pct` > `0.1699` → IC=+0.316 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1699 (IC base=+0.256)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.191` → IC=+0.291 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.191 (IC base=+0.256)

- **PATRÓN** `volumen_regimen` > `0.8427` → IC=+0.296 (n=522)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8427 (IC base=+0.256)

- **PATRÓN** `volumen_pendiente_norm` > `0.2406` → IC=+0.295 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2406 (IC base=+0.256)

- **PATRÓN** `volumen_spike_ratio` < `2.5676` → IC=+0.263 (n=723)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5676 (IC base=+0.256)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.260 (n=885)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.256)

- **PATRÓN** `libro_liquidez` > `2452.7664` → IC=+0.258 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2452.7664 (IC base=+0.256)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.282 (n=282)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0063 (IC base=+0.272)

- **PATRÓN** `sigma_h` > `0.0239` → IC=+0.296 (n=282)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0239 (IC base=+0.272)

- **PATRÓN** `drift_60min` |x|≤ `0.3089` → IC=+0.272 (n=564)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3089 (IC base=+0.272)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.280 (n=804)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.272)

- **PATRÓN** `ibs_20min` < `0.384` → IC=+0.310 (n=846)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.384 (IC base=+0.272)

- **PATRÓN** `dist_vwap_pct` > `0.5389` → IC=+0.288 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5389 (IC base=+0.272)

- **PATRÓN** `dist_vwap_pct` < `0.2035` → IC=+0.272 (n=761)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2035 (IC base=+0.272)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.354` → IC=+0.293 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.354 (IC base=+0.272)

- **PATRÓN** `volumen_regimen` > `1.2589` → IC=+0.306 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2589 (IC base=+0.272)

- **PATRÓN** `volumen_pendiente_norm` > `0.2896` → IC=+0.375 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2896 (IC base=+0.272)

- **PATRÓN** `volumen_spike_ratio` < `2.5744` → IC=+0.261 (n=688)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5744 (IC base=+0.272)

- **PATRÓN** `volumen_spike_ratio` > `2.1862` → IC=+0.283 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1862 (IC base=+0.272)

- **PATRÓN** `libro_liquidez` > `2544.7076` → IC=+0.272 (n=564)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2544.7076 (IC base=+0.272)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.267 (n=589)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.272)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.205 (n=1403)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0105 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.3396` → IC=+0.170 (n=3700)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.3396 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.170 (n=4235)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 6.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` > `0.7` → IC=+0.223 (n=3763)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `1.1036` → IC=+0.231 (n=667)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1036 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.13` → IC=+0.249 (n=876)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.13 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` < `1.2233` → IC=+0.155 (n=2833)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.2233 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` > `0.6308` → IC=+0.161 (n=2833)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6308 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.1049` → IC=+0.188 (n=1590)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.1049 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` < `2.313` → IC=+0.163 (n=3462)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 2.313 (IC base=+0.163)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.163 (n=4257)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.03 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `3889.6241` → IC=+0.172 (n=1402)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 3889.6241 (IC base=+0.163)

- **PATRÓN** `ballena_activa_n` < `140.0` → IC=+0.181 (n=3112)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 140.0 (IC base=+0.163)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.179 (n=3431)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0083 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.0785` → IC=+0.202 (n=1301)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0785 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.193 (n=1879)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 15.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` < `0.4412` → IC=+0.221 (n=3899)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4412 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` < `0.2204` → IC=+0.165 (n=2909)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.2204 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.085` → IC=+0.209 (n=698)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.085 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` < `1.1727` → IC=+0.161 (n=2919)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.1727 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` > `0.6226` → IC=+0.155 (n=2919)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 0.6226 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.2931` → IC=+0.242 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2931 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `2.653` → IC=+0.191 (n=1090)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.653 (IC base=+0.171)

- **PATRÓN** `ballena_activa_n` < `152.0` → IC=+0.165 (n=2858)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 152.0 (IC base=+0.171)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.187 (n=314)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0057 (IC base=+0.181)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.211 (n=323)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.3049` → IC=+0.206 (n=708)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3049 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.221 (n=510)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.296 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.602` → IC=+0.298 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.602 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2271` → IC=+0.265 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2271 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` < `2.6388` → IC=+0.173 (n=625)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 2.6388 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `1.4557` → IC=+0.174 (n=624)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.4557 (IC base=+0.181)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.217 (n=605)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.200 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 45.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.254 (n=404)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.228)

- **PATRÓN** `drift_60min` |x|≤ `0.1683` → IC=+0.309 (n=301)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1683 (IC base=+0.228)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.249 (n=472)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.228)

- **PATRÓN** `ibs_20min` < `0.2708` → IC=+0.257 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2708 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.039` → IC=+0.239 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.039 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` < `0.0675` → IC=+0.221 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0675 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` > `0.2921` → IC=+0.300 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2921 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` < `1.4284` → IC=+0.223 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4284 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` > `2.7329` → IC=+0.246 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7329 (IC base=+0.228)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.256 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.228)

- **PATRÓN** `libro_liquidez` > `1703.72` → IC=+0.259 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1703.72 (IC base=+0.228)

- **PATRÓN** `ballena_activa_n` < `64.0` → IC=+0.223 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 64.0 (IC base=+0.228)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.231 (n=206)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.2878` → IC=+0.169 (n=542)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.2878 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.213 (n=430)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` > `0.4738` → IC=+0.209 (n=616)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4738 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `0.2619` → IC=+0.227 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2619 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.777` → IC=+0.240 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.777 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` < `1.2757` → IC=+0.168 (n=616)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.2757 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` > `1.0769` → IC=+0.174 (n=280)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 1.0769 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.2311` → IC=+0.202 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2311 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` < `1.3944` → IC=+0.202 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3944 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `11191.459` → IC=+0.189 (n=551)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 11191.459 (IC base=+0.163)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.180 (n=707)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0061 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.0596` → IC=+0.213 (n=235)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0596 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.178 (n=648)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 7.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` < `0.4911` → IC=+0.193 (n=705)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.4911 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` < `0.1424` → IC=+0.175 (n=688)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1424 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.3` → IC=+0.245 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.3 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` < `0.6922` → IC=+0.221 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6922 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` > `0.1584` → IC=+0.216 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1584 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `1.7277` → IC=+0.160 (n=398)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.7277 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` > `1.3961` → IC=+0.166 (n=597)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.3961 (IC base=+0.157)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.157 (n=910)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.157)

- **PATRÓN** `libro_liquidez` > `15630.8052` → IC=+0.158 (n=235)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 15630.8052 (IC base=+0.157)

- **PATRÓN** `ballena_activa_n` < `241.0` → IC=+0.163 (n=170)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 241.0 (IC base=+0.157)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.210 (n=222)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0095 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.179` → IC=+0.197 (n=444)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.179 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.189 (n=226)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.189 (n=300)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 7.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.298 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.437` → IC=+0.294 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.437 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.1321` → IC=+0.192 (n=251)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.1321 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `1.8983` → IC=+0.175 (n=537)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 1.8983 (IC base=+0.177)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.199 (n=693)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.177)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.231 (n=530)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.216)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.216 (n=241)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0092 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.2179` → IC=+0.228 (n=354)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2179 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.240 (n=364)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` < `0.3662` → IC=+0.250 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3662 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.703` → IC=+0.256 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.703 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.3655` → IC=+0.273 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3655 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` < `1.8957` → IC=+0.208 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8957 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` > `3.6446` → IC=+0.214 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.6446 (IC base=+0.216)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.187 (n=561)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0071 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.1196` → IC=+0.172 (n=282)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.1196 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.170 (n=653)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 6.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` > `0.4254` → IC=+0.198 (n=637)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.4254 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.1491` → IC=+0.179 (n=446)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.1491 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.407` → IC=+0.262 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.407 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `0.887` → IC=+0.156 (n=425)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.887 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` > `1.2156` → IC=+0.188 (n=213)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` > 1.2156 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.2936` → IC=+0.222 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2936 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `2.6202` → IC=+0.184 (n=207)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.6202 (IC base=+0.152)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=710)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `8686.469` → IC=+0.193 (n=425)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 8686.469 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `135.0` → IC=+0.146 (n=382)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 135.0 (IC base=+0.152)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.148 (n=692)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0076 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.3757` → IC=+0.142 (n=691)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.3757 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.172 (n=230)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 18.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.137 (n=315)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 7.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` < `0.5426` → IC=+0.175 (n=691)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.5426 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` < `0.6069` → IC=+0.137 (n=806)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.6069 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.385` → IC=+0.217 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.385 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `1.1639` → IC=+0.132 (n=691)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.1639 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` > `0.6135` → IC=+0.130 (n=690)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` > 0.6135 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.1024` → IC=+0.174 (n=237)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1024 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.5436` → IC=+0.140 (n=256)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.5436 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `2.512` → IC=+0.148 (n=194)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 2.512 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `5230.1415` → IC=+0.136 (n=460)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 5230.1415 (IC base=+0.125)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.189 (n=265)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0117 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.129 (n=833)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 5.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` > `0.5263` → IC=+0.188 (n=793)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.5263 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` > `1.1246` → IC=+0.245 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1246 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.303` → IC=+0.266 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.303 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `3182.2806` → IC=+0.200 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3182.2806 (IC base=+0.111)

- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.161 (n=240)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0105 (IC base=+0.123)

- **PATRÓN** `drift_60min` |x|≤ `0.0982` → IC=+0.143 (n=242)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.0982 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.183 (n=332)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 15.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` < `0.4737` → IC=+0.212 (n=723)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4737 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `1.0375` → IC=+0.148 (n=89)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 1.0375 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` < `0.1817` → IC=+0.136 (n=641)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.1817 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.282` → IC=+0.159 (n=291)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 3.282 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `1.1889` → IC=+0.136 (n=721)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.1889 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.8584` → IC=+0.129 (n=480)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 0.8584 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.2717` → IC=+0.211 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2717 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.4487` → IC=+0.131 (n=196)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.4487 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.3673` → IC=+0.185 (n=195)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.3673 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `3163.4851` → IC=+0.161 (n=240)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 3163.4851 (IC base=+0.123)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0174` → IC=+0.219 (n=525)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0174 (IC base=+0.194)

- **PATRÓN** `drift_60min` |x|≤ `0.1669` → IC=+0.219 (n=347)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1669 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=828)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.197 (n=701)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 15.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `0.7321` → IC=+0.246 (n=703)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7321 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` > `0.268` → IC=+0.225 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.268 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.172` → IC=+0.240 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.172 (IC base=+0.194)

- **PATRÓN** `volumen_regimen` > `0.6887` → IC=+0.212 (n=703)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6887 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.0832` → IC=+0.249 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0832 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` < `2.5276` → IC=+0.212 (n=747)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5276 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.196 (n=871)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.02 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.260 (n=269)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.0904` → IC=+0.220 (n=269)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0904 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.211 (n=365)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.225 (n=373)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` < `0.425` → IC=+0.245 (n=806)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.425 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` < `0.2538` → IC=+0.206 (n=822)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2538 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.931` → IC=+0.242 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.931 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` > `0.6912` → IC=+0.228 (n=719)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6912 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` > `0.2797` → IC=+0.319 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2797 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` > `2.658` → IC=+0.203 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.658 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.202 (n=725)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `2506.3298` → IC=+0.206 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2506.3298 (IC base=+0.201)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.167 (n=412)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0077 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.167 (n=865)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 8.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.4375` → IC=+0.169 (n=908)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.4375 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.9443` → IC=+0.215 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9443 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.66` → IC=+0.175 (n=419)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 3.66 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.8708` → IC=+0.159 (n=491)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8708 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `1.1751` → IC=+0.152 (n=245)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 1.1751 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.1705` → IC=+0.180 (n=251)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.1705 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.2604` → IC=+0.147 (n=751)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.2604 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.8202` → IC=+0.146 (n=569)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.8202 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.161 (n=705)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `9553.1781` → IC=+0.185 (n=303)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 9553.1781 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.1735` → IC=+0.154 (n=229)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.1735 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.151 (n=262)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 16.0 (IC base=+0.074)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` > `0.0032` → IC=+0.128 (n=143)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` > 0.0032 (IC base=+0.093)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.165 (n=162)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 10.0 (IC base=+0.093)

- **PATRÓN** `ibs_20min` > `0.9156` → IC=+0.193 (n=73)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.9156 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` > `0.8823` → IC=+0.225 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8823 (IC base=+0.093)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.645` → IC=+0.171 (n=77)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 3.645 (IC base=+0.093)

- **PATRÓN** `volumen_regimen` < `0.6919` → IC=+0.167 (n=70)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.6919 (IC base=+0.093)

- **PATRÓN** `volumen_spike_ratio` < `2.3852` → IC=+0.138 (n=150)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 2.3852 (IC base=+0.093)

- **PATRÓN** `libro_liquidez` > `8646.4701` → IC=+0.158 (n=159)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 8646.4701 (IC base=+0.093)

- **PATRÓN** `ballena_activa_n` < `150.0` → IC=+0.174 (n=44)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 150.0 (IC base=+0.093)

- **PATRÓN** `ibs_20min` < `0.6326` → IC=+0.154 (n=270)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.6326 (IC base=+0.082)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.093` → IC=+0.161 (n=57)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 9.093 (IC base=+0.082)

- **PATRÓN** `volumen_pendiente_norm` > `0.1595` → IC=+0.211 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1595 (IC base=+0.082)

- **PATRÓN** `ballena_activa_n` < `146.0` → IC=+0.170 (n=92)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 146.0 (IC base=+0.082)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.268 (n=166)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.259)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.312 (n=83)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.259)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.289 (n=249)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.259)

- **PATRÓN** `ibs_20min` > `0.3797` → IC=+0.280 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3797 (IC base=+0.259)

- **PATRÓN** `dist_vwap_pct` > `0.15` → IC=+0.281 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.15 (IC base=+0.259)

- **PATRÓN** `dist_vwap_pct` < `0.4543` → IC=+0.258 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4543 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.12` → IC=+0.295 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.12 (IC base=+0.259)

- **PATRÓN** `volumen_regimen` < `0.8258` → IC=+0.268 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8258 (IC base=+0.259)

- **PATRÓN** `volumen_regimen` > `1.1544` → IC=+0.324 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1544 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` > `0.0976` → IC=+0.357 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0976 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` < `1.3716` → IC=+0.262 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3716 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` > `2.0629` → IC=+0.332 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.0629 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.263 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.259)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` < `0.5806` → IC=-0.172 (n=62)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5806
  - _Potencial_: sin este filtro IC_bueno=+0.090 (n=186)

- **FILTRO** `ibs_20min` > `0.4146` → IC=-0.214 (n=54)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4146
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=106)

- **FILTRO** `dist_vwap_pct` > `0.2281` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2281
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=139)

- **FILTRO** `volumen_pendiente_norm` > `0.2176` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.2176
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=121)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.156 (n=94)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 14.0 (IC base=+0.024)

- **PATRÓN** `ibs_20min` > `0.8462` → IC=+0.175 (n=124)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.8462 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` > `0.6843` → IC=+0.214 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6843 (IC base=+0.024)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 20.0 (IC base=-0.031)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0226` → IC=+0.146 (n=142)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0226 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.31` → IC=+0.161 (n=125)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.31 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.186 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 16.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.136 (n=53)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 6.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` > `0.4` → IC=+0.162 (n=143)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.4 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` > `0.2912` → IC=+0.149 (n=55)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.2912 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` < `0.6865` → IC=+0.142 (n=174)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.6865 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.317` → IC=+0.169 (n=122)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` < 3.317 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.9833` → IC=+0.138 (n=125)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.9833 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` > `0.6571` → IC=+0.151 (n=127)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6571 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` < `0.2154` → IC=+0.156 (n=123)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.2154 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `1.899` → IC=+0.179 (n=79)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.899 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.4996` → IC=+0.142 (n=118)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.4996 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.177 (n=97)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.01 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.208 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=+0.134)

- **PATRÓN** `sigma_h` > `0.0152` → IC=+0.213 (n=99)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0152 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.141 (n=51)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.141 (n=104)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 10.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` < `0.0588` → IC=+0.135 (n=50)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.0588 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.129 (n=68)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` > 0.5 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `0.9736` → IC=+0.350 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9736 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.507` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.507 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` > `0.6197` → IC=+0.149 (n=149)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.6197 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2451` → IC=+0.242 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2451 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `1.5677` → IC=+0.138 (n=136)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.5677 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2567.2585` → IC=+0.143 (n=68)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 2567.2585 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.158 (n=112)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 16.0 (IC base=+0.125)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.200 (n=2306)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.173 (n=5114)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 6.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `0.4837` → IC=+0.211 (n=5084)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4837 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` > `1.047` → IC=+0.221 (n=711)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.047 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.474` → IC=+0.227 (n=2544)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.474 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` < `0.8868` → IC=+0.159 (n=2334)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8868 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` > `0.168` → IC=+0.198 (n=1391)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.168 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` > `1.8746` → IC=+0.173 (n=3168)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 1.8746 (IC base=+0.165)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.166 (n=4759)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.02 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `3813.5418` → IC=+0.182 (n=1695)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 3813.5418 (IC base=+0.165)

- **PATRÓN** `ballena_activa_n` < `63.0` → IC=+0.211 (n=2494)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 63.0 (IC base=+0.165)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.191 (n=4643)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0109 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.478` → IC=+0.189 (n=4643)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.478 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.187 (n=2262)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 15.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.193 (n=2083)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 7.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` < `0.56` → IC=+0.235 (n=4648)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.56 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` < `0.4381` → IC=+0.166 (n=3258)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.4381 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.718` → IC=+0.212 (n=664)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.718 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.718` → IC=+0.184 (n=4320)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 2.718 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `0.6227` → IC=+0.167 (n=1091)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.6227 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` > `1.1939` → IC=+0.163 (n=1090)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 1.1939 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.237` → IC=+0.244 (n=765)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.237 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `2.3025` → IC=+0.194 (n=1783)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.3025 (IC base=+0.183)

- **PATRÓN** `ballena_activa_n` < `138.0` → IC=+0.175 (n=3515)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 138.0 (IC base=+0.183)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.195 (n=283)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0052 (IC base=+0.192)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.239 (n=381)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.218 (n=406)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.192)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.321 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.908` → IC=+0.311 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.908 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` > `0.2282` → IC=+0.273 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2282 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` < `1.4696` → IC=+0.202 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4696 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` > `2.2967` → IC=+0.178 (n=343)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 2.2967 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.238 (n=693)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.192)

- **PATRÓN** `ballena_activa_n` < `82.0` → IC=+0.245 (n=504)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 82.0 (IC base=+0.192)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.268 (n=555)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.257)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.262 (n=632)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.257)

- **PATRÓN** `drift_60min` |x|≤ `0.1914` → IC=+0.294 (n=421)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1914 (IC base=+0.257)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.262 (n=577)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.257)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.263 (n=635)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.257)

- **PATRÓN** `ibs_20min` < `0.4174` → IC=+0.297 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4174 (IC base=+0.257)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.611` → IC=+0.272 (n=638)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.611 (IC base=+0.257)

- **PATRÓN** `volumen_pendiente_norm` > `0.2958` → IC=+0.319 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2958 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` > `1.5076` → IC=+0.271 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5076 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.273 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `1730.7134` → IC=+0.268 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1730.7134 (IC base=+0.257)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.264 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 73.0 (IC base=+0.257)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.183 (n=276)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0029 (IC base=+0.155)

- **PATRÓN** `sigma_h` > `0.0067` → IC=+0.162 (n=276)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0067 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.178 (n=740)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 8.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` > `0.4544` → IC=+0.209 (n=738)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4544 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.2181` → IC=+0.205 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2181 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.756` → IC=+0.187 (n=199)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 9.756 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.322` → IC=+0.164 (n=722)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` < 4.322 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` < `1.2673` → IC=+0.164 (n=826)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2673 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` < `0.0706` → IC=+0.166 (n=699)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` < 0.0706 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` > `0.147` → IC=+0.196 (n=225)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.147 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `2.3936` → IC=+0.170 (n=776)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 2.3936 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `1.7258` → IC=+0.180 (n=517)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.7258 (IC base=+0.155)

- **PATRÓN** `libro_liquidez` > `10616.3534` → IC=+0.181 (n=738)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 10616.3534 (IC base=+0.155)

- **PATRÓN** `ballena_activa_n` < `466.0` → IC=+0.173 (n=618)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 466.0 (IC base=+0.155)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.179 (n=739)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0061 (IC base=+0.168)

- **PATRÓN** `sigma_h` > `0.0029` → IC=+0.171 (n=661)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0029 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.2658` → IC=+0.183 (n=651)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.2658 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.168 (n=660)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 8.0 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.174 (n=529)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 12.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` < `0.6154` → IC=+0.208 (n=739)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6154 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` < `0.1406` → IC=+0.187 (n=643)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.1406 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.843` → IC=+0.218 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.843 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `0.618` → IC=+0.223 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.618 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.1438` → IC=+0.231 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1438 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `1.4033` → IC=+0.196 (n=215)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.4033 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `2.0524` → IC=+0.194 (n=292)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.0524 (IC base=+0.168)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.167 (n=954)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `289.0` → IC=+0.190 (n=182)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 289.0 (IC base=+0.168)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0074` → IC=+0.231 (n=496)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0074 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.246 (n=352)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.6825` → IC=+0.260 (n=665)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6825 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.274` → IC=+0.322 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.274 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` < `0.2198` → IC=+0.214 (n=680)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2198 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `3.196` → IC=+0.206 (n=590)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.196 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `1.7188` → IC=+0.207 (n=670)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7188 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.238 (n=780)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `1467.9084` → IC=+0.214 (n=744)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1467.9084 (IC base=+0.210)

- **PATRÓN** `ballena_activa_n` < `65.0` → IC=+0.253 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 65.0 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.260 (n=248)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.232)

- **PATRÓN** `sigma_h` > `0.009` → IC=+0.243 (n=337)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.009 (IC base=+0.232)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.237 (n=363)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.232)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.257 (n=265)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.232)

- **PATRÓN** `ibs_20min` < `0.3966` → IC=+0.274 (n=654)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3966 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.554` → IC=+0.271 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.554 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` > `0.3568` → IC=+0.292 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3568 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` < `3.0458` → IC=+0.232 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.0458 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` > `2.3266` → IC=+0.216 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3266 (IC base=+0.232)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.241 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.232)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.205 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 25.0 (IC base=+0.232)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.154 (n=744)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0069 (IC base=+0.140)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.140 (n=847)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` > 0.0033 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.155 (n=764)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 8.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.7314` → IC=+0.237 (n=564)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7314 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.3645` → IC=+0.184 (n=337)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.3645 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.314` → IC=+0.166 (n=378)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 4.314 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.8944` → IC=+0.166 (n=564)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8944 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `1.2022` → IC=+0.144 (n=282)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.2022 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.2746` → IC=+0.229 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2746 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `2.5084` → IC=+0.190 (n=269)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.5084 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=920)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `9488.8794` → IC=+0.238 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9488.8794 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.170 (n=222)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0032 (IC base=+0.124)

- **PATRÓN** `drift_60min` |x|≤ `0.4364` → IC=+0.141 (n=659)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.4364 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.147 (n=253)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.162 (n=291)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` < `0.6768` → IC=+0.172 (n=659)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.6768 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` < `0.3968` → IC=+0.126 (n=664)

  - _Acción_: Kelly boost +0.63€ cuando `dist_vwap_pct` < 0.3968 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.298` → IC=+0.209 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.298 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `0.6018` → IC=+0.126 (n=220)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 0.6018 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` > `1.142` → IC=+0.140 (n=220)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 1.142 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.2795` → IC=+0.257 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2795 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `1.4531` → IC=+0.139 (n=597)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.4531 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `9489.0705` → IC=+0.174 (n=299)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 9489.0705 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `191.0` → IC=+0.134 (n=512)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 191.0 (IC base=+0.124)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.138 (n=592)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` > 0.0079 (IC base=+0.094)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.135 (n=595)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 12.0 (IC base=+0.094)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.178 (n=890)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.4706 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` > `0.8687` → IC=+0.180 (n=226)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.8687 (IC base=+0.094)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.403` → IC=+0.216 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.403 (IC base=+0.094)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.122 (n=620)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.01 (IC base=+0.094)

- **PATRÓN** `libro_liquidez` > `2947.9426` → IC=+0.255 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2947.9426 (IC base=+0.094)

- **PATRÓN** `ballena_activa_n` < `63.0` → IC=+0.134 (n=664)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 63.0 (IC base=+0.094)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.178 (n=281)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0057 (IC base=+0.116)

- **PATRÓN** `drift_60min` |x|≤ `0.1269` → IC=+0.182 (n=278)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.1269 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.147 (n=403)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 15.0 (IC base=+0.116)

- **PATRÓN** `ibs_20min` < `0.587` → IC=+0.194 (n=834)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.587 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` < `0.5012` → IC=+0.136 (n=801)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.5012 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.241` → IC=+0.127 (n=810)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` < 3.241 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` < `0.7144` → IC=+0.146 (n=368)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.7144 (IC base=+0.116)

- **PATRÓN** `volumen_pendiente_norm` > `0.0745` → IC=+0.176 (n=288)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.0745 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` < `1.5628` → IC=+0.140 (n=301)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.5628 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` > `2.1802` → IC=+0.131 (n=310)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.1802 (IC base=+0.116)

- **PATRÓN** `libro_liquidez` > `2635.8438` → IC=+0.147 (n=378)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 2635.8438 (IC base=+0.116)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0279` → IC=+0.241 (n=315)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0279 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.213 (n=992)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.204 (n=832)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.301 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `0.172` → IC=+0.249 (n=576)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.172 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.172` → IC=+0.249 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.172 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` > `0.6933` → IC=+0.213 (n=842)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6933 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.2373` → IC=+0.253 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2373 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` > `1.8278` → IC=+0.210 (n=594)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8278 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.210 (n=1040)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.203)

- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.274 (n=347)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.205)

- **PATRÓN** `sigma_h` > `0.0253` → IC=+0.226 (n=348)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0253 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.209 (n=984)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.210 (n=1094)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.257 (n=1052)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` < `0.1793` → IC=+0.209 (n=900)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1793 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.376` → IC=+0.270 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.376 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` > `1.232` → IC=+0.239 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.232 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.2857` → IC=+0.288 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2857 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `1.4555` → IC=+0.195 (n=864)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.4555 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.209 (n=944)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.185 (n=759)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 35.0 (IC base=+0.205)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.129 (n=1814)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.133 (n=1458)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0103 (IC base=+0.121)

- **PATRÓN** `drift_60min` |x|≤ `0.5538` → IC=+0.132 (n=1657)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.66€ cuando `drift_60min` |x|≤ 0.5538 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.169 (n=569)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 18.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `0.9277` → IC=+0.193 (n=552)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.9277 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.472` → IC=+0.145 (n=260)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 10.472 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.792` → IC=+0.122 (n=1435)

  - _Acción_: Kelly boost +0.61€ cuando `sigma_ewma_delta_pct` < 2.792 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.1727` → IC=+0.154 (n=455)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.1727 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `1.4605` → IC=+0.139 (n=547)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.4605 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` > `1.8939` → IC=+0.144 (n=1093)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.8939 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `8643.8042` → IC=+0.128 (n=751)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 8643.8042 (IC base=+0.121)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.175 (n=459)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0039 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.5002` → IC=+0.147 (n=1372)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.5002 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.156 (n=510)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.156 (n=463)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 4.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` < `0.1983` → IC=+0.148 (n=604)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.1983 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `0.7584` → IC=+0.131 (n=234)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` > 0.7584 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.329` → IC=+0.137 (n=1366)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 6.329 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `1.2252` → IC=+0.133 (n=1306)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.2252 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` < `0.1489` → IC=+0.128 (n=1374)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.1489 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.0693` → IC=+0.149 (n=648)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.0693 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `2.5013` → IC=+0.136 (n=1357)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.5013 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `1.8071` → IC=+0.136 (n=905)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.8071 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.129 (n=1814)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7723.2634` → IC=+0.134 (n=1226)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 7723.2634 (IC base=+0.126)

### GBM_LATE_5M#BTC#5min
- **FILTRO** `sigma_ewma_delta_pct` > `2.471` → IC=-0.250 (n=26)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.471
  - _Potencial_: sin este filtro IC_bueno=+0.144 (n=189)

- **PATRÓN** `hora_utc` > `19.0` → IC=+0.156 (n=59)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 19.0 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.471` → IC=+0.144 (n=189)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 2.471 (IC base=+0.095)

- **PATRÓN** `volumen_regimen` > `0.9375` → IC=+0.145 (n=74)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 0.9375 (IC base=+0.095)

- **PATRÓN** `volumen_spike_ratio` < `1.4115` → IC=+0.179 (n=54)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.4115 (IC base=+0.095)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.175 (n=278)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0035 (IC base=+0.112)

- **PATRÓN** `drift_60min` |x|≤ `0.0863` → IC=+0.140 (n=209)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.0863 (IC base=+0.112)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.156 (n=239)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.112)

- **PATRÓN** `ibs_20min` < `0.1703` → IC=+0.158 (n=276)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.1703 (IC base=+0.112)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.372` → IC=+0.138 (n=623)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 6.372 (IC base=+0.112)

- **PATRÓN** `volumen_regimen` < `0.8677` → IC=+0.145 (n=418)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.8677 (IC base=+0.112)

- **PATRÓN** `volumen_pendiente_norm` > `0.0635` → IC=+0.153 (n=295)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.0635 (IC base=+0.112)

- **PATRÓN** `volumen_spike_ratio` < `1.4014` → IC=+0.144 (n=209)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4014 (IC base=+0.112)

- **PATRÓN** `libro_liquidez` > `11116.1452` → IC=+0.124 (n=626)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 11116.1452 (IC base=+0.112)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.205 (n=137)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.147)

- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.181 (n=186)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0106 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.2811` → IC=+0.166 (n=273)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.2811 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.190 (n=375)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 9.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.9849` → IC=+0.227 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9849 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.299` → IC=+0.219 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.299 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.0922` → IC=+0.157 (n=173)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.0922 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `3.5224` → IC=+0.159 (n=408)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 3.5224 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.8314` → IC=+0.153 (n=364)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.8314 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `2289.2732` → IC=+0.176 (n=137)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2289.2732 (IC base=+0.147)

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

- **PATRÓN** `libro_liquidez` > `2362.106` → IC=+0.281 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2362.106 (IC base=+0.254)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.256 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 25.0 (IC base=+0.254)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0089` → IC=+0.147 (n=571)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0089 (IC base=+0.134)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.135 (n=570)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` > 0.0046 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.4713` → IC=+0.146 (n=571)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.4713 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.195 (n=195)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 18.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.139 (n=267)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 6.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` > `0.185` → IC=+0.147 (n=570)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.185 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` > `1.0394` → IC=+0.172 (n=129)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 1.0394 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` < `0.4266` → IC=+0.141 (n=539)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.4266 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.989` → IC=+0.143 (n=573)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 6.989 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `1.116` → IC=+0.145 (n=502)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.116 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.0834` → IC=+0.151 (n=253)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.0834 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `1.4338` → IC=+0.168 (n=188)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.4338 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.8023` → IC=+0.136 (n=374)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.8023 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.135 (n=496)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `8352.5828` → IC=+0.145 (n=570)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 8352.5828 (IC base=+0.134)

- **PATRÓN** `sigma_h` < `0.0088` → IC=+0.169 (n=427)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0088 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.4064` → IC=+0.208 (n=375)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4064 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.154 (n=154)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.162 (n=291)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 10.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.1076` → IC=+0.164 (n=426)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.1076 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.7273` → IC=+0.158 (n=472)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.7273 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.986` → IC=+0.181 (n=70)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 10.986 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `1.2227` → IC=+0.171 (n=426)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.2227 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` > `0.7338` → IC=+0.152 (n=380)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.7338 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` < `0.1472` → IC=+0.155 (n=433)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.1472 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.0698` → IC=+0.167 (n=187)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.0698 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.1713` → IC=+0.172 (n=367)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 2.1713 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.4487` → IC=+0.168 (n=417)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.4487 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `8169.7182` → IC=+0.164 (n=426)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 8169.7182 (IC base=+0.150)

### GBM_LATE_5M#SOL#5min
- **FILTRO** `ibs_20min` < `0.4444` → IC=-0.224 (n=27)

  - _Acción_: SKIP cuando `ibs_20min` < 0.4444
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=83)

- **FILTRO** `dist_vwap_pct` < `0.7269` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.7269
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=28)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=+0.008)

### GBM_LATE_60M
- **FILTRO** `ibs_20min` < `0.6383` → IC=-0.160 (n=101)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6383
  - _Potencial_: sin este filtro IC_bueno=+0.212 (n=304)

- **FILTRO** `sigma_h` > `0.01` → IC=-0.297 (n=67)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=202)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.223 (n=81)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=188)

- **FILTRO** `dist_vwap_pct` > `0.1531` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1531
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=110)

- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.188 (n=264)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0055 (IC base=+0.092)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.160 (n=148)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 18.0 (IC base=+0.092)

- **PATRÓN** `ibs_20min` > `0.6383` → IC=+0.212 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6383 (IC base=+0.092)

- **PATRÓN** `dist_vwap_pct` > `0.8439` → IC=+0.189 (n=43)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.8439 (IC base=+0.092)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.712` → IC=+0.245 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.712 (IC base=+0.092)

- **PATRÓN** `volumen_regimen` < `0.8192` → IC=+0.144 (n=203)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.8192 (IC base=+0.092)

- **PATRÓN** `volumen_regimen` > `0.5803` → IC=+0.121 (n=304)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_regimen` > 0.5803 (IC base=+0.092)

- **PATRÓN** `volumen_pendiente_norm` > `0.2731` → IC=+0.321 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2731 (IC base=+0.092)

- **PATRÓN** `volumen_spike_ratio` < `1.9975` → IC=+0.165 (n=180)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.9975 (IC base=+0.092)

- **PATRÓN** `volumen_spike_ratio` > `1.4935` → IC=+0.154 (n=183)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.4935 (IC base=+0.092)

- **PATRÓN** `libro_spread` < `0.023` → IC=+0.155 (n=247)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.023 (IC base=+0.092)

- **PATRÓN** `libro_liquidez` > `1069.2998` → IC=+0.159 (n=250)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 1069.2998 (IC base=+0.092)

- **PATRÓN** `ibs_20min` < `0.0916` → IC=+0.227 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0916 (IC base=-0.113)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.229 (n=116)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.110)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.146 (n=63)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 16.0 (IC base=+0.110)

- **PATRÓN** `ibs_20min` > `0.7829` → IC=+0.228 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7829 (IC base=+0.110)

- **PATRÓN** `dist_vwap_pct` > `0.157` → IC=+0.184 (n=55)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.157 (IC base=+0.110)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.251` → IC=+0.210 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.251 (IC base=+0.110)

- **PATRÓN** `volumen_regimen` < `0.8725` → IC=+0.171 (n=68)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.8725 (IC base=+0.110)

- **PATRÓN** `volumen_pendiente_norm` > `0.1451` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1451 (IC base=+0.110)

- **PATRÓN** `volumen_spike_ratio` < `2.2071` → IC=+0.212 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2071 (IC base=+0.110)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.160 (n=98)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.110)

- **PATRÓN** `drift_60min` |x|≤ `0.0744` → IC=+0.167 (n=22)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.0744 (IC base=-0.028)

- **PATRÓN** `ibs_20min` < `0.6326` → IC=+0.150 (n=38)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.6326 (IC base=-0.028)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` < `0.6789` → IC=-0.143 (n=54)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6789
  - _Potencial_: sin este filtro IC_bueno=+0.268 (n=110)

- **FILTRO** `sigma_h` > `0.0071` → IC=-0.370 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0071
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=66)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.227 (n=42)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=45)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.167 (n=103)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.005 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.146 (n=80)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 15.0 (IC base=+0.104)

- **PATRÓN** `ibs_20min` > `0.6789` → IC=+0.268 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6789 (IC base=+0.104)

- **PATRÓN** `dist_vwap_pct` > `0.4909` → IC=+0.190 (n=27)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.4909 (IC base=+0.104)

- **PATRÓN** `dist_vwap_pct` < `0.1483` → IC=+0.154 (n=108)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1483 (IC base=+0.104)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.837` → IC=+0.294 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.837 (IC base=+0.104)

- **PATRÓN** `volumen_regimen` < `0.791` → IC=+0.159 (n=83)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.791 (IC base=+0.104)

- **PATRÓN** `volumen_regimen` > `0.6214` → IC=+0.134 (n=110)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` > 0.6214 (IC base=+0.104)

- **PATRÓN** `volumen_pendiente_norm` > `0.2254` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2254 (IC base=+0.104)

- **PATRÓN** `volumen_spike_ratio` < `1.7889` → IC=+0.141 (n=51)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.7889 (IC base=+0.104)

- **PATRÓN** `volumen_spike_ratio` > `1.4589` → IC=+0.167 (n=76)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.4589 (IC base=+0.104)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.157 (n=129)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.02 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `1276.6106` → IC=+0.204 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1276.6106 (IC base=+0.104)

- **PATRÓN** `ibs_20min` < `0.1005` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1005 (IC base=-0.118)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `ibs_20min` < `0.6667` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6667
  - _Potencial_: sin este filtro IC_bueno=+0.175 (n=81)

- **FILTRO** `ibs_20min` > `0.1111` → IC=-0.300 (n=38)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1111
  - _Potencial_: sin este filtro IC_bueno=+0.188 (n=14)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.179 (n=54)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 18.0 (IC base=+0.050)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.175 (n=81)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.6667 (IC base=+0.050)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.203` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.203 (IC base=+0.050)

- **PATRÓN** `volumen_regimen` > `1.0843` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 1.0843 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` > `0.0856` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0856 (IC base=+0.050)

- **PATRÓN** `volumen_spike_ratio` < `2.1762` → IC=+0.142 (n=65)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.1762 (IC base=+0.050)

- **PATRÓN** `libro_liquidez` > `376.737` → IC=+0.152 (n=67)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 376.737 (IC base=+0.050)

### GBM_LATE_60M_FADE
- **FILTRO** `drift_60min` |x|> `0.1905` → IC=-0.362 (n=27)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1905
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=82)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.466 (n=27)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.221 (n=84)

- **FILTRO** `dist_vwap_pct` > `0.2352` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2352
  - _Potencial_: sin este filtro IC_bueno=-0.273 (n=95)

- **FILTRO** `dist_vwap_pct` > `0.4614` → IC=-0.389 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4614
  - _Potencial_: sin este filtro IC_bueno=-0.288 (n=97)

- **FILTRO** `sigma_ewma_delta_pct` > `3.662` → IC=-0.308 (n=50)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 3.662
  - _Potencial_: sin este filtro IC_bueno=-0.300 (n=63)

- **FILTRO** `volumen_spike_ratio` > `1.721` → IC=-0.441 (n=15)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.721
  - _Potencial_: sin este filtro IC_bueno=-0.333 (n=16)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `sigma_h` < `0.0036` → IC=-0.250 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0036
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=11)

- **FILTRO** `ibs_20min` < `0.5407` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5407
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11)

- **FILTRO** `sigma_h` < `0.0033` → IC=-0.278 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=12)

- **FILTRO** `dist_vwap_pct` < `0.1009` → IC=-0.362 (n=27)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1009
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=19)

- **FILTRO** `volumen_regimen` > `1.0011` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.0011
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=31)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.6354` → IC=-0.462 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6354
  - _Potencial_: sin este filtro IC_bueno=-0.233 (n=13)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.350 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=19)

- **FILTRO** `ibs_20min` > `0.8039` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8039
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=19)

- **FILTRO** `dist_vwap_pct` > `0.0802` → IC=-0.309 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.0802
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=18)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `drift_60min` |x|> `0.1073` → IC=-0.382 (n=15)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1073
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=17)

- **FILTRO** `sigma_h` < `0.0065` → IC=-0.382 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0065
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=15)

- **FILTRO** `volumen_regimen` < `1.1715` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.1715
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` < `0.6331` → IC=-0.246 (n=57)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6331
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=174)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.151 (n=81)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 15.0 (IC base=+0.053)

- **PATRÓN** `ibs_20min` < `0.251` → IC=+0.138 (n=150)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` < 0.251 (IC base=+0.053)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.717` → IC=+0.122 (n=72)

  - _Acción_: Kelly boost +0.61€ cuando `sigma_ewma_delta_pct` > 5.717 (IC base=+0.053)

- **PATRÓN** `volumen_pendiente_norm` > `0.0687` → IC=+0.152 (n=44)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.0687 (IC base=+0.053)

- **PATRÓN** `libro_liquidez` > `2923.7123` → IC=+0.126 (n=113)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 2923.7123 (IC base=+0.053)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=63)

- **FILTRO** `ibs_20min` < `0.3927` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3927
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=60)

- **FILTRO** `volumen_regimen` < `0.7102` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7102
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=60)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.258 (n=31)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.109)

- **PATRÓN** `ibs_20min` < `0.1622` → IC=+0.189 (n=72)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.1622 (IC base=+0.109)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.265` → IC=+0.134 (n=80)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 10.265 (IC base=+0.109)

- **PATRÓN** `volumen_regimen` < `0.5658` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.5658 (IC base=+0.109)

- **PATRÓN** `volumen_spike_ratio` > `1.6024` → IC=+0.138 (n=45)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.6024 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `3671.9914` → IC=+0.139 (n=81)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 3671.9914 (IC base=+0.109)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=39)

- **PATRÓN** `sigma_h` < `0.0025` → IC=+0.281 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0025 (IC base=+0.057)

- **PATRÓN** `drift_60min` |x|≤ `0.2013` → IC=+0.134 (n=39)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.67€ cuando `drift_60min` |x|≤ 0.2013 (IC base=+0.057)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.057)

- **PATRÓN** `ibs_20min` > `0.8029` → IC=+0.191 (n=40)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.8029 (IC base=+0.057)

- **PATRÓN** `dist_vwap_pct` < `0.1039` → IC=+0.128 (n=41)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` < 0.1039 (IC base=+0.057)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.159 (n=39)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.057)

- **PATRÓN** `libro_liquidez` > `2339.7005` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 2339.7005 (IC base=+0.057)

- **PATRÓN** `hora_utc` > `19.0` → IC=+0.167 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 19.0 (IC base=+0.038)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.007` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.007 (IC base=+0.038)

- **PATRÓN** `libro_liquidez` > `2418.7992` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2418.7992 (IC base=+0.038)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `dist_vwap_pct` > `0.147` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.147
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=35)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.173 (n=47)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.7917 (IC base=+0.068)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.122 (n=239)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 6.0 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2754.2307` → IC=+0.185 (n=106)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2754.2307 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2251.4926` → IC=+0.128 (n=272)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 2251.4926 (IC base=+0.093)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.122 (n=239)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 6.0 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2754.2307` → IC=+0.185 (n=106)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2754.2307 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2251.4926` → IC=+0.128 (n=272)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 2251.4926 (IC base=+0.093)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `11.0` → IC=-0.198 (n=61)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=64)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=109)

- **FILTRO** `libro_liquidez` < `2306.3177` → IC=-0.318 (n=31)

  - _Acción_: SKIP cuando `libro_liquidez` < 2306.3177
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=94)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=171)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=157)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=18)

- **FILTRO** `libro_liquidez` < `11811.9773` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `libro_liquidez` < 11811.9773
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=15)

- **FILTRO** `libro_liquidez` < `14445.5423` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `libro_liquidez` < 14445.5423
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=14)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

### LIQUIDACIONES_15M#XRP#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=1086)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=91)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.140 (n=48)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=91)

- **FILTRO** `libro_liquidez` < `10665.27` → IC=-0.233 (n=84)

  - _Acción_: SKIP cuando `libro_liquidez` < 10665.27
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=28)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `16.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=48)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_usd_total` < `35151.71` → IC=-0.200 (n=38)

  - _Acción_: SKIP cuando `liq_usd_total` < 35151.71
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=79)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=19)

- **FILTRO** `libro_liquidez` < `15405.8709` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `libro_liquidez` < 15405.8709
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **PATRÓN** `liq_usd_total` > `59480.98` → IC=+0.156 (n=59)

  - _Acción_: Kelly boost +0.78€ cuando `liq_usd_total` > 59480.98 (IC base=+0.013)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.160 (n=45)

  - _Acción_: Kelly boost +0.80€ cuando `py_entrada` < 0.495 (IC base=+0.013)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9534` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9534
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=72)

- **FILTRO** `hora_utc` > `14.0` → IC=-0.167 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=79)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=374)

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
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=407)

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
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=63)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=63)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=166)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=166)

- **FILTRO** `py_entrada` > `0.555` → IC=-0.167 (n=43)

  - _Acción_: SKIP cuando `py_entrada` > 0.555
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=138)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=124)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=124)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.125 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=93)

- **FILTRO** `hora_utc` > `16.0` → IC=-0.167 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=39)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=43)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=41)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=52)

### MOMENTUM_IBS_15M#BNB#15min
- **FILTRO** `libro_liquidez` < `2179.3878` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `libro_liquidez` < 2179.3878
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=127)

### MOMENTUM_IBS_15M#BTC#15min
- **FILTRO** `py_entrada` > `0.505` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=397)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=744)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=810)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.46` → IC=-0.174 (n=1613)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=4944)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.183 (n=1624)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=5140)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.42` → IC=-0.224 (n=255)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=784)

- **FILTRO** `ibs_20min` < `0.7378` → IC=-0.190 (n=259)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7378
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=780)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.162 (n=291)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=898)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.56` → IC=-0.186 (n=259)

  - _Acción_: SKIP cuando `py_entrada` > 0.56
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=796)

- **FILTRO** `ballena_activa_n` > `58.0` → IC=-0.157 (n=263)

  - _Acción_: SKIP cuando `ballena_activa_n` > 58.0
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=792)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.182 (n=357)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=736)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.215 (n=286)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=874)

- **FILTRO** `ibs_20min` > `0.7083` → IC=-0.194 (n=289)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7083
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=871)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.174 (n=256)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=836)

- **FILTRO** `py_entrada` > `0.56` → IC=-0.172 (n=263)

  - _Acción_: SKIP cuando `py_entrada` > 0.56
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=801)

### MOMENTUM_IBS_15M_BALLENA#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.140 (n=292)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=811)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.184 (n=248)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=769)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=1002)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.201 (n=289)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=869)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `hora_utc` < `16.0` → IC=-0.340 (n=48)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=217)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=547)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=553)

### MOMENTUM_IBS_15M_FADE#BNB#15min
- **FILTRO** `hora_utc` > `17.0` → IC=-0.167 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.182 (n=20)

- **FILTRO** `libro_liquidez` < `2024.7167` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_liquidez` < 2024.7167
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=62)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.182 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 17.0 (IC base=+0.012)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `19.0` → IC=-0.242 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 19.0
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=13)

- **FILTRO** `py_entrada` > `0.625` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `py_entrada` > 0.625
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=64)

- **FILTRO** `drift_20min_pct` |x|> `0.2121` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.2121
  - _Potencial_: sin este filtro IC_bueno=-0.131 (n=63)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `ibs_20min` < `0.0989` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `ibs_20min` < 0.0989
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=17)

- **FILTRO** `py_entrada` > `0.645` → IC=-0.306 (n=34)

  - _Acción_: SKIP cuando `py_entrada` > 0.645
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=104)

- **FILTRO** `ibs_20min` > `0.9803` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `ibs_20min` > 0.9803
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=104)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `hora_utc` < `19.0` → IC=-0.227 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 19.0
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=38)

- **PATRÓN** `libro_liquidez` > `4506.3723` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 4506.3723 (IC base=-0.050)

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
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=40)

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

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.157 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 16.0 (IC base=+0.033)

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
- **FILTRO** `py_entrada` < `0.35` → IC=-0.279 (n=3837)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=11952)

- **FILTRO** `ibs_7min` < `0.7155` → IC=-0.234 (n=3947)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7155
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=11842)

- **FILTRO** `ballena_activa_n` > `18.0` → IC=-0.168 (n=5319)

  - _Acción_: SKIP cuando `ballena_activa_n` > 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=10470)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.222 (n=4879)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=15124)

- **FILTRO** `ibs_7min` > `0.7143` → IC=-0.173 (n=4983)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7143
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=15020)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.308 (n=562)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=1774)

- **FILTRO** `ibs_7min` < `0.7089` → IC=-0.250 (n=770)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7089
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=1566)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.219 (n=556)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=1780)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.244 (n=860)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=2612)

- **FILTRO** `drift_7min_pct` |x|> `0.1143` → IC=-0.134 (n=1177)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1143
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=2295)

- **FILTRO** `ibs_7min` > `0.8361` → IC=-0.200 (n=867)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8361
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=2605)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.137 (n=635)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=2278)

- **FILTRO** `py_entrada` < `0.36` → IC=-0.261 (n=704)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=2209)

- **FILTRO** `ibs_7min` < `0.7734` → IC=-0.189 (n=728)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7734
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=2185)

- **FILTRO** `ballena_activa_n` > `166.0` → IC=-0.176 (n=726)

  - _Acción_: SKIP cuando `ballena_activa_n` > 166.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=2187)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.242 (n=712)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=2222)

- **FILTRO** `ballena_activa_n` > `107.0` → IC=-0.170 (n=995)

  - _Acción_: SKIP cuando `ballena_activa_n` > 107.0
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=1939)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.183 (n=740)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.099 (n=1583)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.302 (n=737)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=1586)

- **FILTRO** `ibs_7min` < `0.2222` → IC=-0.289 (n=580)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2222
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=1743)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.240 (n=552)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=1771)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.225 (n=861)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=2762)

- **FILTRO** `ibs_7min` > `0.2797` → IC=-0.158 (n=1231)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2797
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=2392)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.141 (n=808)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=1855)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.262 (n=636)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=2027)

- **FILTRO** `ibs_7min` < `0.7561` → IC=-0.185 (n=665)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7561
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=1998)

- **FILTRO** `ballena_activa_n` > `37.0` → IC=-0.180 (n=661)

  - _Acción_: SKIP cuando `ballena_activa_n` > 37.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=2002)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.235 (n=882)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=1817)

- **FILTRO** `ibs_7min` > `0.2762` → IC=-0.177 (n=674)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2762
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=2025)

- **FILTRO** `ballena_activa_n` > `33.0` → IC=-0.186 (n=667)

  - _Acción_: SKIP cuando `ballena_activa_n` > 33.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=2032)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.237 (n=718)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=2235)

- **FILTRO** `ibs_7min` < `0.7368` → IC=-0.202 (n=732)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7368
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2221)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.177 (n=888)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=2860)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.126 (n=615)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=1986)

- **FILTRO** `py_entrada` < `0.36` → IC=-0.293 (n=627)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=1974)

- **FILTRO** `ibs_7min` < `0.74` → IC=-0.229 (n=648)

  - _Acción_: SKIP cuando `ibs_7min` < 0.74
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=1953)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.224 (n=629)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=1972)

- **FILTRO** `py_entrada` > `0.69` → IC=-0.207 (n=851)

  - _Acción_: SKIP cuando `py_entrada` > 0.69
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=2676)

- **FILTRO** `ibs_7min` > `0.76` → IC=-0.156 (n=878)

  - _Acción_: SKIP cuando `ibs_7min` > 0.76
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=2649)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=118)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=852)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.122 (n=43)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=435)

### MOMENTUM_IBS_5M_FADE#DOGE#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=596)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=568)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=38)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=483)

### ORDER_FLOW_5M
- **FILTRO** `total_vol_5m` > `215.224` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `total_vol_5m` > 215.224
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **PATRÓN** `delta_ratio` |x|> `0.3988` → IC=+0.146 (n=546)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.73€ cuando `delta_ratio` |x|> 0.3988 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.141 (n=438)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 6.0 (IC base=+0.131)

- **PATRÓN** `total_vol_5m` < `459.6089` → IC=+0.167 (n=175)

  - _Acción_: Kelly boost +0.83€ cuando `total_vol_5m` < 459.6089 (IC base=+0.131)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.128 (n=256)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `3336.2388` → IC=+0.153 (n=214)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3336.2388 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `63.0` → IC=+0.131 (n=385)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 63.0 (IC base=+0.131)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.276 (n=56)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.127)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `libro_liquidez` > `2005.686` → IC=+0.121 (n=85)

  - _Acción_: Kelly boost +0.60€ cuando `libro_liquidez` > 2005.686 (IC base=+0.094)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4139` → IC=+0.194 (n=60)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.97€ cuando `delta_ratio` |x|> 0.4139 (IC base=+0.112)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.145 (n=60)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 8.0 (IC base=+0.112)

- **PATRÓN** `total_vol_5m` < `655.7948` → IC=+0.191 (n=79)

  - _Acción_: Kelly boost +0.96€ cuando `total_vol_5m` < 655.7948 (IC base=+0.112)

- **PATRÓN** `libro_liquidez` > `7354.4583` → IC=+0.141 (n=90)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 7354.4583 (IC base=+0.112)

- **PATRÓN** `ballena_activa_n` < `152.0` → IC=+0.133 (n=88)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 152.0 (IC base=+0.112)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4038` → IC=+0.202 (n=82)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4038 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.174 (n=41)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 15.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.196 (n=90)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 18.0 (IC base=+0.176)

- **PATRÓN** `total_vol_5m` < `5831.176` → IC=+0.189 (n=72)

  - _Acción_: Kelly boost +0.95€ cuando `total_vol_5m` < 5831.176 (IC base=+0.176)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.180 (n=48)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `3762.2112` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3762.2112 (IC base=+0.176)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.3956` → IC=+0.143 (n=96)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.71€ cuando `delta_ratio` |x|> 0.3956 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.159 (n=86)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 14.0 (IC base=+0.128)

- **PATRÓN** `total_vol_5m` < `258575.4` → IC=+0.167 (n=64)

  - _Acción_: Kelly boost +0.83€ cuando `total_vol_5m` < 258575.4 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.246 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `3207.3582` → IC=+0.174 (n=44)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 3207.3582 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.167 (n=76)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 54.0 (IC base=+0.128)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `3.488` → IC=-0.381 (n=65)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.488
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=127)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `T_h` > `39.9942` → IC=-0.386 (n=42)

  - _Acción_: SKIP cuando `T_h` > 39.9942
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=21)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.321 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=-0.125)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0083` → IC=-0.224 (n=27)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0083
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `T_h` > `135.9956` → IC=-0.167 (n=49)

  - _Acción_: SKIP cuando `T_h` > 135.9956
  - _Potencial_: sin este filtro IC_bueno=-0.101 (n=161)

- **FILTRO** `pct_vs_K` |x|> `5.2098` → IC=-0.259 (n=52)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 5.2098
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=158)

- **FILTRO** `T_h` > `145.7058` → IC=-0.367 (n=43)

  - _Acción_: SKIP cuando `T_h` > 145.7058
  - _Potencial_: sin este filtro IC_bueno=-0.307 (n=133)

- **FILTRO** `pct_vs_K` |x|> `4.3703` → IC=-0.434 (n=59)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.3703
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=117)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `T_h` > `87.9918` → IC=-0.179 (n=51)

  - _Acción_: SKIP cuando `T_h` > 87.9918
  - _Potencial_: sin este filtro IC_bueno=+0.133 (n=28)

- **FILTRO** `pct_vs_K` |x|> `3.6199` → IC=-0.447 (n=17)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.6199
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=62)

- **FILTRO** `T_h` > `144.6172` → IC=-0.318 (n=20)

  - _Acción_: SKIP cuando `T_h` > 144.6172
  - _Potencial_: sin este filtro IC_bueno=-0.261 (n=44)

- **FILTRO** `pct_vs_K` |x|> `4.2908` → IC=-0.441 (n=15)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.2908
  - _Potencial_: sin este filtro IC_bueno=-0.226 (n=49)

- **PATRÓN** `pct_vs_K` |x|≤ `0.8662` → IC=+0.300 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 0.8662 (IC base=-0.068)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `T_h` < `87.9808` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `T_h` < 87.9808
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=40)

- **FILTRO** `sigma_h` > `0.0085` → IC=-0.382 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0085
  - _Potencial_: sin este filtro IC_bueno=-0.271 (n=46)

- **FILTRO** `T_h` > `111.9668` → IC=-0.308 (n=45)

  - _Acción_: SKIP cuando `T_h` > 111.9668
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=16)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.007` → IC=-0.400 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.389 (n=7)

- **FILTRO** `T_h` > `119.1632` → IC=-0.400 (n=18)

  - _Acción_: SKIP cuando `T_h` > 119.1632
  - _Potencial_: sin este filtro IC_bueno=-0.389 (n=7)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.2367` → IC=+0.405 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2367 (IC base=+0.388)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.450 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.388)

- **PATRÓN** `T_h` > `0.8774` → IC=+0.425 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8774 (IC base=+0.388)

- **PATRÓN** `dist_50` > `0.4172` → IC=+0.474 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4172 (IC base=+0.388)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.420 (n=23)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.388)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.452 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.480)

### STREAK_FADE_15M
- **FILTRO** `hora_utc` < `7.0` → IC=-0.208 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.129 (n=68)

- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=75)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=142)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.127 (n=65)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 8.0 (IC base=+0.043)

- **PATRÓN** `streak_estiramiento` < `0.4095` → IC=+0.167 (n=34)

  - _Acción_: Kelly boost +0.83€ cuando `streak_estiramiento` < 0.4095 (IC base=+0.027)

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

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=22)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `hora_utc` < `3.0` → IC=-0.144 (n=43)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=171)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=191)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=193)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=205)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=295)

- **PATRÓN** `streak_estiramiento` < `0.3587` → IC=+0.158 (n=71)

  - _Acción_: Kelly boost +0.79€ cuando `streak_estiramiento` < 0.3587 (IC base=+0.031)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=581)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=307)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=384)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=1681)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=933)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=941)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.170 (n=204)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0036 (IC base=+0.140)

- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.183 (n=203)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0075 (IC base=+0.140)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1911` → IC=+0.142 (n=277)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.71€ cuando `delta_ratio_macro` |x|> 0.1911 (IC base=+0.140)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3329` → IC=+0.185 (n=296)

  - _Acción_: Kelly boost +0.92€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3329 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.140 (n=612)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.177 (n=274)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 6.0 (IC base=+0.140)

- **PATRÓN** `ibs_15` > `0.5919` → IC=+0.218 (n=609)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5919 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.1491` → IC=+0.142 (n=325)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.1491 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` < `0.5526` → IC=+0.141 (n=649)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.5526 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `15.547` → IC=+0.228 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 15.547 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.146 (n=605)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `9584.2249` → IC=+0.168 (n=203)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 9584.2249 (IC base=+0.140)

### UPDOWN_GBM#5min
- **FILTRO** `sigma_ewma_delta_pct` > `7.858` → IC=-0.204 (n=42)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.858
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=1242)

### UPDOWN_GBM#60min
- **FILTRO** `sigma_ewma_delta_pct` > `7.93` → IC=-0.134 (n=39)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.93
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=85)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=108)

### UPDOWN_GBM#BTC#15min
- **FILTRO** `sigma_h` < `0.0053` → IC=-0.130 (n=71)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0053
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=145)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.198 (n=114)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0031 (IC base=+0.175)

- **PATRÓN** `drift_60min` |x|≤ `0.1898` → IC=+0.198 (n=170)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.1898 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.198 (n=180)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 4.0 (IC base=+0.175)

- **PATRÓN** `ibs_15` > `0.8766` → IC=+0.300 (n=113)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8766 (IC base=+0.175)

- **PATRÓN** `dist_vwap_pct` > `0.3024` → IC=+0.189 (n=72)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.3024 (IC base=+0.175)

- **PATRÓN** `dist_vwap_pct` < `0.1221` → IC=+0.194 (n=109)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.1221 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.246` → IC=+0.221 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.246 (IC base=+0.175)

- **PATRÓN** `libro_liquidez` > `14737.8449` → IC=+0.246 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14737.8449 (IC base=+0.175)

### UPDOWN_GBM#BTC#5min
- **FILTRO** `sigma_h` < `0.0035` → IC=-0.200 (n=28)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0035
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=57)

- **FILTRO** `ibs_15` < `0.1827` → IC=-0.239 (n=21)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.1827
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=64)

- **FILTRO** `libro_liquidez` < `13612.3448` → IC=-0.121 (n=56)

  - _Acción_: SKIP cuando `libro_liquidez` < 13612.3448
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=29)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `ibs_15` < `0.8231` → IC=-0.125 (n=94)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8231
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=94)

- **FILTRO** `ibs_15` < `0.2522` → IC=-0.143 (n=26)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.2522
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=54)

- **FILTRO** `sigma_ewma_delta_pct` > `8.973` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.973
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=60)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.351` → IC=+0.145 (n=29)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 20.351 (IC base=+0.007)

### UPDOWN_GBM#ETH#15min
- **FILTRO** `ibs_15` < `0.6414` → IC=-0.200 (n=48)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6414
  - _Potencial_: sin este filtro IC_bueno=+0.189 (n=146)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2614` → IC=+0.167 (n=49)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.83€ cuando `delta_ratio_macro` |x|> 0.2614 (IC base=+0.092)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.122 (n=149)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` < 17.0 (IC base=+0.092)

- **PATRÓN** `ibs_15` > `0.6414` → IC=+0.189 (n=146)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.95€ cuando `ibs_15` > 0.6414 (IC base=+0.092)

- **PATRÓN** `dist_vwap_pct` < `0.1542` → IC=+0.144 (n=116)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1542 (IC base=+0.092)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.717` → IC=+0.157 (n=65)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 8.717 (IC base=+0.092)

### UPDOWN_GBM#ETH#5min
- **FILTRO** `hora_utc` > `8.0` → IC=-0.200 (n=28)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=95)

- **FILTRO** `dist_vwap_pct` > `0.215` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.215
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=107)

- **FILTRO** `drift_15min` |x|> `0.4824` → IC=-0.146 (n=159)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.4824
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=481)

- **FILTRO** `sigma_ewma_delta_pct` > `9.42` → IC=-0.120 (n=106)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.42
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=534)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `libro_spread` > `0.03` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=177)

- **FILTRO** `hora_utc` < `16.0` → IC=-0.206 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### UPDOWN_GBM#SOL#15min
- **FILTRO** `ibs_15` < `0.5217` → IC=-0.241 (n=25)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5217
  - _Potencial_: sin este filtro IC_bueno=+0.250 (n=78)

- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.250 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0076 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.1323` → IC=+0.143 (n=68)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.1323 (IC base=+0.129)

- **PATRÓN** `delta_ratio_macro` |x|> `0.209` → IC=+0.184 (n=36)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.92€ cuando `delta_ratio_macro` |x|> 0.209 (IC base=+0.129)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2102` → IC=+0.260 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2102 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.200 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.129)

- **PATRÓN** `ibs_15` > `0.5217` → IC=+0.250 (n=78)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5217 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` < `0.2349` → IC=+0.141 (n=76)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.2349 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.225` → IC=+0.370 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.225 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.132 (n=66)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `2917.9058` → IC=+0.210 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2917.9058 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.278 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.129)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `hora_utc` < `11.0` → IC=-0.143 (n=40)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=135)

### UPDOWN_GBM#SOL#60min
- **FILTRO** `sigma_ewma_delta_pct` < `12.798` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 12.798
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=10)

- **PATRÓN** `dist_vwap_pct` < `0.3849` → IC=+0.141 (n=51)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.3849 (IC base=+0.010)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `delta_ratio_macro` |x|> `0.0487` → IC=+0.163 (n=167)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.81€ cuando `delta_ratio_macro` |x|> 0.0487 (IC base=+0.134)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1718` → IC=+0.200 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1718 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.192 (n=76)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 6.0 (IC base=+0.134)

- **PATRÓN** `ibs_15` > `0.5695` → IC=+0.229 (n=149)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5695 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` > `0.1207` → IC=+0.199 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1207 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `15.916` → IC=+0.214 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 15.916 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=127)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `2682.2064` → IC=+0.218 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2682.2064 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.210 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.134)

- **PATRÓN** `ibs_15` < `0.1154` → IC=+0.181 (n=189)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.90€ cuando `ibs_15` < 0.1154 (IC base=+0.030)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.324 (n=140)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.321)

- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.389 (n=70)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0057 (IC base=+0.321)

- **PATRÓN** `drift_60min` |x|≤ `0.1141` → IC=+0.345 (n=140)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1141 (IC base=+0.321)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1426` → IC=+0.330 (n=139)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1426 (IC base=+0.321)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.133` → IC=+0.364 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.133 (IC base=+0.321)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.338 (n=227)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.321)

- **PATRÓN** `ibs_15` > `0.8357` → IC=+0.389 (n=187)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8357 (IC base=+0.321)

- **PATRÓN** `dist_vwap_pct` > `0.156` → IC=+0.341 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.156 (IC base=+0.321)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.39` → IC=+0.339 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.39 (IC base=+0.321)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.888` → IC=+0.326 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.888 (IC base=+0.321)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.328 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.321)

- **PATRÓN** `libro_liquidez` > `8557.9163` → IC=+0.356 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8557.9163 (IC base=+0.321)

- **PATRÓN** `ballena_activa_n` < `528.0` → IC=+0.362 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 528.0 (IC base=+0.321)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1145` → IC=+0.360 (n=41)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1145 (IC base=+0.311)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.317 (n=107)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.311)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.337 (n=41)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.311)

- **PATRÓN** `drift_60min` |x|≤ `0.1567` → IC=+0.326 (n=107)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1567 (IC base=+0.311)

- **PATRÓN** `drift_15min` |x|≤ `0.4089` → IC=+0.321 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4089 (IC base=+0.311)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1462` → IC=+0.319 (n=81)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1462 (IC base=+0.311)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.133` → IC=+0.409 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.133 (IC base=+0.311)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.357 (n=110)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.311)

- **PATRÓN** `ibs_15` > `0.8048` → IC=+0.355 (n=122)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8048 (IC base=+0.311)

- **PATRÓN** `dist_vwap_pct` > `0.2738` → IC=+0.385 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2738 (IC base=+0.311)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.509` → IC=+0.332 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 8.509 (IC base=+0.311)

- **PATRÓN** `libro_liquidez` > `8216.2794` → IC=+0.355 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8216.2794 (IC base=+0.311)

- **PATRÓN** `ballena_activa_n` < `626.0` → IC=+0.408 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 626.0 (IC base=+0.311)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.329 (n=39)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.331)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.381 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.331)

- **PATRÓN** `drift_60min` |x|≤ `0.1188` → IC=+0.369 (n=59)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1188 (IC base=+0.331)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0665` → IC=+0.343 (n=87)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0665 (IC base=+0.331)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2567` → IC=+0.336 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2567 (IC base=+0.331)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.335 (n=89)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.331)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.327 (n=79)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.331)

- **PATRÓN** `ibs_15` > `0.7601` → IC=+0.399 (n=87)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7601 (IC base=+0.331)

- **PATRÓN** `dist_vwap_pct` < `0.3157` → IC=+0.352 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3157 (IC base=+0.331)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.588` → IC=+0.378 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.588 (IC base=+0.331)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.348 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.331)

- **PATRÓN** `libro_liquidez` > `2812.5928` → IC=+0.338 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2812.5928 (IC base=+0.331)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.344 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 166.0 (IC base=+0.331)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0112` → IC=-0.190 (n=369)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0112
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=1111)

- **FILTRO** `ibs_15` < `0.5` → IC=-0.218 (n=122)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.195 (n=381)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.143 (n=387)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=1093)

- **FILTRO** `sigma_ewma_delta_pct` > `18.745` → IC=-0.153 (n=534)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.745
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=4068)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3537` → IC=+0.182 (n=215)

  - _Acción_: Kelly boost +0.91€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3537 (IC base=-0.065)

- **PATRÓN** `ibs_15` > `0.5` → IC=+0.195 (n=381)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.97€ cuando `ibs_15` > 0.5 (IC base=-0.065)

- **PATRÓN** `dist_vwap_pct` < `0.1752` → IC=+0.132 (n=229)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.1752 (IC base=-0.065)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1248` → IC=+0.222 (n=354)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1248 (IC base=-0.064)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1115` → IC=+0.235 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1115 (IC base=-0.064)

- **PATRÓN** `ibs_15` < `0.3676` → IC=+0.266 (n=531)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3676 (IC base=-0.064)

- **PATRÓN** `dist_vwap_pct` < `0.1516` → IC=+0.211 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1516 (IC base=-0.064)

- **PATRÓN** `ballena_activa_n` < `124.0` → IC=+0.214 (n=494)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 124.0 (IC base=-0.064)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0074` → IC=-0.225 (n=238)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0074
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=718)

- **FILTRO** `sigma_h` < `0.0038` → IC=-0.231 (n=314)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0038
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=642)

- **FILTRO** `sigma_ewma_delta_pct` > `19.475` → IC=-0.254 (n=173)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.475
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=783)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1163` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1163 (IC base=+0.029)

- **PATRÓN** `ibs_15` > `0.6077` → IC=+0.310 (n=56)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6077 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` < `0.1661` → IC=+0.219 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1661 (IC base=+0.029)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.6395` → IC=-0.247 (n=77)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6395
  - _Potencial_: sin este filtro IC_bueno=+0.258 (n=159)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=219)

- **PATRÓN** `drift_60min` |x|≤ `0.0806` → IC=+0.212 (n=78)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0806 (IC base=+0.092)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2769` → IC=+0.216 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2769 (IC base=+0.092)

- **PATRÓN** `ibs_15` > `0.6395` → IC=+0.258 (n=159)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6395 (IC base=+0.092)

- **PATRÓN** `dist_vwap_pct` < `0.1779` → IC=+0.128 (n=135)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` < 0.1779 (IC base=+0.092)

- **PATRÓN** `libro_liquidez` > `10832.5702` → IC=+0.199 (n=81)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 10832.5702 (IC base=+0.092)

- **PATRÓN** `sigma_h` < `0.0078` → IC=+0.246 (n=250)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0078 (IC base=+0.213)

- **PATRÓN** `sigma_h` > `0.0045` → IC=+0.213 (n=249)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0045 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.4386` → IC=+0.218 (n=250)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4386 (IC base=+0.213)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0918` → IC=+0.224 (n=223)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0918 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `19.0` → IC=+0.229 (n=83)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 19.0 (IC base=+0.213)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.282 (n=85)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.213)

- **PATRÓN** `ibs_15` < `0.3696` → IC=+0.274 (n=250)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3696 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` > `0.2343` → IC=+0.228 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2343 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` < `11.415` → IC=+0.230 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 11.415 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `3638.7885` → IC=+0.213 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3638.7885 (IC base=+0.213)

- **PATRÓN** `ballena_activa_n` < `128.0` → IC=+0.218 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 128.0 (IC base=+0.213)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1609` → IC=-0.195 (n=126)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1609
  - _Potencial_: sin este filtro IC_bueno=-0.099 (n=245)

- **FILTRO** `drift_15min` |x|> `0.8298` → IC=-0.266 (n=92)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8298
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=279)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.174 (n=127)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=244)

- **FILTRO** `sigma_ewma_delta_pct` > `16.45` → IC=-0.140 (n=184)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 16.45
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=1432)

- **PATRÓN** `ibs_15` > `0.8214` → IC=+0.262 (n=19)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8214 (IC base=-0.133)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0761` → IC=+0.161 (n=107)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.80€ cuando `delta_ratio_macro` |x|> 0.0761 (IC base=-0.049)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2087` → IC=+0.192 (n=76)

  - _Acción_: Kelly boost +0.96€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2087 (IC base=-0.049)

- **PATRÓN** `ibs_15` < `0.3814` → IC=+0.213 (n=120)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3814 (IC base=-0.049)

- **PATRÓN** `dist_vwap_pct` < `0.2528` → IC=+0.184 (n=112)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 0.2528 (IC base=-0.049)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.018` → IC=-0.226 (n=206)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.018
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=208)

- **FILTRO** `drift_15min` |x|> `1.1952` → IC=-0.243 (n=103)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.1952
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=311)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0953` → IC=+0.339 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0953 (IC base=-0.061)

- **PATRÓN** `ibs_15` < `0.3448` → IC=+0.271 (n=142)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3448 (IC base=-0.061)

- **PATRÓN** `dist_vwap_pct` > `0.5057` → IC=+0.344 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5057 (IC base=-0.061)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.275 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=-0.061)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.147 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0065 (IC base=+0.100)

- **PATRÓN** `drift_60min` |x|≤ `0.1349` → IC=+0.206 (n=15)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1349 (IC base=+0.100)

- **PATRÓN** `drift_15min` |x|≤ `0.4465` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4465 (IC base=+0.100)

- **PATRÓN** `ibs_15` > `0.2576` → IC=+0.208 (n=22)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.2576 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `0.0928` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.0928 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `12949.2689` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12949.2689 (IC base=+0.100)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.147 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0065 (IC base=+0.100)

- **PATRÓN** `drift_60min` |x|≤ `0.1349` → IC=+0.206 (n=15)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1349 (IC base=+0.100)

- **PATRÓN** `drift_15min` |x|≤ `0.4465` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4465 (IC base=+0.100)

- **PATRÓN** `ibs_15` > `0.2576` → IC=+0.208 (n=22)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.2576 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `0.0928` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.0928 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `12949.2689` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12949.2689 (IC base=+0.100)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.287 (n=359)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.283)

- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.294 (n=163)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0055 (IC base=+0.283)

- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.336 (n=120)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.283)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1322` → IC=+0.301 (n=239)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1322 (IC base=+0.283)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.109` → IC=+0.328 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.109 (IC base=+0.283)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.308 (n=379)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.283)

- **PATRÓN** `ibs_15` > `0.8332` → IC=+0.314 (n=359)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8332 (IC base=+0.283)

- **PATRÓN** `dist_vwap_pct` > `0.3017` → IC=+0.318 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3017 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.729` → IC=+0.285 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.729 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.246` → IC=+0.284 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.246 (IC base=+0.283)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.292 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `13887.9508` → IC=+0.328 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13887.9508 (IC base=+0.283)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.299 (n=137)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.282)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.289 (n=93)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.282)

- **PATRÓN** `drift_60min` |x|≤ `0.0813` → IC=+0.306 (n=91)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0813 (IC base=+0.282)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1252` → IC=+0.321 (n=138)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1252 (IC base=+0.282)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.316 (n=205)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.282)

- **PATRÓN** `ibs_15` > `0.9207` → IC=+0.327 (n=137)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9207 (IC base=+0.282)

- **PATRÓN** `dist_vwap_pct` > `0.306` → IC=+0.337 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.306 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.592` → IC=+0.333 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.592 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.915` → IC=+0.285 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.915 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `15468.9258` → IC=+0.345 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15468.9258 (IC base=+0.282)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.282 (n=154)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0071 (IC base=+0.283)

- **PATRÓN** `sigma_h` > `0.0053` → IC=+0.281 (n=103)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0053 (IC base=+0.283)

- **PATRÓN** `drift_60min` |x|≤ `0.0694` → IC=+0.329 (n=68)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0694 (IC base=+0.283)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1898` → IC=+0.319 (n=70)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1898 (IC base=+0.283)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1463` → IC=+0.330 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1463 (IC base=+0.283)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.316 (n=150)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.283)

- **PATRÓN** `ibs_15` > `0.8444` → IC=+0.321 (n=154)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8444 (IC base=+0.283)

- **PATRÓN** `dist_vwap_pct` > `0.2913` → IC=+0.300 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2913 (IC base=+0.283)

- **PATRÓN** `dist_vwap_pct` < `0.4822` → IC=+0.287 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4822 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.547` → IC=+0.295 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.547 (IC base=+0.283)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `10755.3155` → IC=+0.306 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10755.3155 (IC base=+0.283)

- **PATRÓN** `ballena_activa_n` < `184.0` → IC=+0.280 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 184.0 (IC base=+0.283)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0807` → IC=-0.253 (n=75)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0807
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=148)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.170 (n=107)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=58)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1226` → IC=-0.143 (n=40)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1226
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=82)

- **FILTRO** `drift_60min` |x|> `0.1544` → IC=-0.200 (n=18)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1544
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=20)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1979` → IC=-0.382 (n=15)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1979
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `drift_60min` |x|> `0.1352` → IC=-0.167 (n=16)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1352
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.0931` → IC=-0.214 (n=19)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0931
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### WEEKLY_PRICE
- **PATRÓN** `T_h` < `63.9918` → IC=+0.173 (n=53)

  - _Acción_: Kelly boost +0.86€ cuando `T_h` < 63.9918 (IC base=+0.121)

- **PATRÓN** `ratio` < `0.9932` → IC=+0.322 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9932 (IC base=+0.121)

- **PATRÓN** `T_h` > `145.9626` → IC=+0.417 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.9626 (IC base=+0.344)

- **PATRÓN** `ratio` > `1.0126` → IC=+0.343 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0126 (IC base=+0.344)

### WEEKLY_PRICE#BTC
- **PATRÓN** `ratio` < `0.9922` → IC=+0.300 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9922 (IC base=+0.096)

- **PATRÓN** `T_h` < `87.9918` → IC=+0.322 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 87.9918 (IC base=+0.285)

- **PATRÓN** `ratio` > `1.0126` → IC=+0.336 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0126 (IC base=+0.285)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` < `79.3918` → IC=+0.242 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 79.3918 (IC base=+0.174)

- **PATRÓN** `ratio` < `0.9911` → IC=+0.411 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9911 (IC base=+0.174)

- **PATRÓN** `T_h` > `87.9969` → IC=+0.328 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 87.9969 (IC base=+0.316)

- **PATRÓN** `ratio` > `1.012` → IC=+0.320 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.012 (IC base=+0.316)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `135.9824` → IC=+0.428 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 135.9824 (IC base=+0.409)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5919 sube el IC de +0.140 a +0.218 en UPDOWN_GBM#15min (n=609). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.8766 sube el IC de +0.175 a +0.300 en UPDOWN_GBM#BTC#15min (n=113). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6414 sube el IC de +0.092 a +0.189 en UPDOWN_GBM#ETH#15min (n=146). Ya aplicado como kelly_boost=+0.95€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.5217 sube el IC de +0.129 a +0.250 en UPDOWN_GBM#SOL#15min (n=78). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5695 sube el IC de +0.134 a +0.229 en UPDOWN_GBM#XRP#15min (n=149). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1154 sube el IC de +0.030 a +0.181 en UPDOWN_GBM#XRP#15min (n=189). Ya aplicado como kelly_boost=+0.90€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.5 sube el IC de -0.065 a +0.195 en UPDOWN_GBM_15M_TARDIO (n=381). Ya aplicado como kelly_boost=+0.97€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3676 sube el IC de -0.064 a +0.266 en UPDOWN_GBM_15M_TARDIO (n=531). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.6077 sube el IC de +0.029 a +0.310 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=56). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6395 sube el IC de +0.092 a +0.258 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=159). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3696 sube el IC de +0.213 a +0.274 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=250). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8214 sube el IC de -0.133 a +0.262 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=19). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3814 sube el IC de -0.049 a +0.213 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=120). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3448 sube el IC de -0.061 a +0.271 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=142). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_NO, IBS > 0.2576 sube el IC de +0.100 a +0.208 en UPDOWN_GBM_ETH_15M_HORA7 (n=22). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_NO, IBS > 0.2576 sube el IC de +0.100 a +0.208 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=22). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8332 sube el IC de +0.283 a +0.314 en UPDOWN_GBM_IBS_ALTO (n=359). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.9207 sube el IC de +0.282 a +0.327 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=137). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8444 sube el IC de +0.283 a +0.321 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=154). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.8357 sube el IC de +0.321 a +0.389 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=187). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8048 sube el IC de +0.311 a +0.355 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=122). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7601 sube el IC de +0.331 a +0.399 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=87). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min` — IC=+0.372 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL` — IC=+0.372 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 877 | +0.089 | +65.09€ | 2 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 877 | +0.089 | +65.09€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 25 | +0.056 | -0.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 25 | +0.056 | -0.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 588 | +0.105 | +51.08€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 588 | +0.105 | +51.08€ | 2 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 222 | +0.036 | -0.81€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 222 | +0.036 | -0.81€ | 5 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 42 | +0.159 | +15.07€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 42 | +0.159 | +15.07€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 16097 | -0.117 | -2578.15€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 994 | -0.016 | -145.57€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 15103 | -0.124 | -2432.58€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 2181 | -0.107 | -481.97€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 2181 | -0.107 | -481.97€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 994 | -0.016 | -145.57€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 994 | -0.016 | -145.57€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 2124 | -0.171 | -580.89€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 2124 | -0.171 | -580.89€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 4264 | -0.060 | -392.88€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 4264 | -0.060 | -392.88€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 3599 | -0.130 | -225.42€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 3599 | -0.130 | -225.42€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 2935 | -0.189 | -751.41€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 2935 | -0.189 | -751.41€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 5170 | -0.080 | +1937.47€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 1477 | -0.014 | +1061.62€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 3693 | -0.106 | +875.85€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 5170 | -0.080 | +1937.47€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 1477 | -0.014 | +1061.62€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 3693 | -0.106 | +875.85€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 111 | -0.040 | -11.46€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 111 | -0.040 | -11.46€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 111 | -0.040 | -11.46€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 111 | -0.040 | -11.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 51722 | +0.113 | -3119.91€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 8576 | +0.181 | -302.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 184 | -0.118 | -59.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 39066 | +0.099 | -2676.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 3896 | +0.115 | -80.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 6550 | +0.086 | -808.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 28 | -0.100 | +6.23€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 6507 | +0.088 | -803.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 10327 | +0.132 | -229.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 2529 | +0.197 | -120.48€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 6458 | +0.109 | -131.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 1298 | +0.123 | +43.84€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 6571 | +0.086 | -759.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 31 | +0.015 | +3.38€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 6525 | +0.088 | -751.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 11173 | +0.126 | -186.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 3211 | +0.170 | -33.33€ | 1 | 8 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 6502 | +0.112 | -107.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 1448 | +0.097 | -37.02€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 10548 | +0.121 | -696.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 2754 | +0.188 | -160.20€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 90 | -0.033 | -6.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 6554 | +0.094 | -442.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1150 | +0.129 | -87.59€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 6553 | +0.105 | -438.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 23 | -0.020 | +1.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 10 | +0.000 | +0.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 6520 | +0.105 | -440.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 8466 | +0.180 | -638.47€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 8466 | +0.180 | -638.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 2164 | +0.168 | -235.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 2164 | +0.168 | -235.13€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 149 | -0.136 | -0.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 149 | -0.136 | -0.83€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 2112 | +0.173 | -215.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 2112 | +0.173 | -215.26€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 1897 | +0.236 | -47.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 1897 | +0.236 | -47.97€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 2065 | +0.186 | -153.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 2065 | +0.186 | -153.05€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 420 | +0.441 | -1.19€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 420 | +0.441 | -1.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 161 | +0.439 | -0.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 161 | +0.439 | -0.20€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 160 | +0.438 | -0.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 160 | +0.438 | -0.00€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 95 | +0.428 | -1.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 95 | +0.428 | -1.22€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 27751 | +0.191 | -2508.48€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 27751 | +0.191 | -2508.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 4929 | +0.154 | -738.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 4929 | +0.154 | -738.65€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 4336 | +0.225 | -153.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 4336 | +0.225 | -153.78€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 4797 | +0.166 | -627.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 4797 | +0.166 | -627.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 4425 | +0.219 | -178.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 4425 | +0.219 | -178.73€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 4588 | +0.201 | -326.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 4588 | +0.201 | -326.02€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 4676 | +0.184 | -483.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 4676 | +0.184 | -483.75€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 10075 | +0.129 | +303.68€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 10075 | +0.129 | +303.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 4985 | +0.135 | +203.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 4985 | +0.135 | +203.29€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 5090 | +0.123 | +100.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 5090 | +0.123 | +100.39€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 999 | +0.291 | -11.64€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 999 | +0.291 | -11.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 432 | +0.277 | -12.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 432 | +0.277 | -12.96€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 472 | +0.295 | +3.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 472 | +0.295 | +3.63€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 95 | +0.325 | -2.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 95 | +0.325 | -2.31€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 434 | +0.422 | -12.79€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 434 | +0.422 | -12.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 195 | +0.419 | -7.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 195 | +0.419 | -7.06€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 202 | +0.426 | -5.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 202 | +0.426 | -5.27€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 37 | +0.372 | -0.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 37 | +0.372 | -0.46€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 531 | +0.097 | -1.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 186 | +0.090 | -4.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 345 | +0.099 | +3.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 36 | +0.079 | -0.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 36 | +0.079 | -0.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 414 | +0.106 | +7.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 69 | +0.134 | +4.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 345 | +0.099 | +3.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 81 | +0.054 | -9.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 81 | +0.054 | -9.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 15773 | +0.096 | -568.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 1400 | +0.076 | -24.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 14373 | +0.098 | -543.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 9384 | +0.098 | -209.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 1400 | +0.076 | -24.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 7984 | +0.102 | -184.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 2137 | +0.114 | +21.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 2137 | +0.114 | +21.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 4252 | +0.081 | -381.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 4252 | +0.081 | -381.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 590 | +0.255 | -79.43€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 590 | +0.255 | -79.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 590 | +0.255 | -79.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 590 | +0.255 | -79.43€ | 0 | 4 |
| ✅ GBM_LATE_15M | 13051 | +0.060 | +5621.72€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 13051 | +0.060 | +5621.72€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 2039 | +0.194 | +1481.96€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 2039 | +0.194 | +1481.96€ | 0 | 23 |
| ✅ GBM_LATE_15M#BTC | 1941 | +0.178 | +1333.29€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 1941 | +0.178 | +1333.29€ | 0 | 27 |
| ✅ GBM_LATE_15M#DOGE | 2092 | +0.193 | +1504.24€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 2092 | +0.193 | +1504.24€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 2007 | -0.034 | +137.07€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 2007 | -0.034 | +137.07€ | 2 | 11 |
| ✅ GBM_LATE_15M#SOL | 2062 | -0.051 | +501.64€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 2062 | -0.051 | +501.64€ | 4 | 7 |
| ✅ GBM_LATE_15M#XRP | 2910 | -0.065 | +663.50€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 2910 | -0.065 | +663.50€ | 4 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 13911 | +0.064 | +7197.28€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 13911 | +0.064 | +7197.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 2467 | +0.001 | +1753.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 2467 | +0.001 | +1753.24€ | 2 | 6 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 3001 | -0.015 | +474.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 3001 | -0.015 | +474.89€ | 1 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 1858 | +0.255 | +1816.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 1858 | +0.255 | +1816.80€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 2101 | -0.045 | +83.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 2101 | -0.045 | +83.70€ | 6 | 6 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 2313 | -0.008 | +851.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 2313 | -0.008 | +851.66€ | 3 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 2171 | +0.265 | +2216.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 2171 | +0.265 | +2216.98€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 10803 | +0.167 | +7642.58€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 10803 | +0.167 | +7642.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 1544 | +0.200 | +1185.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 1544 | +0.200 | +1185.07€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 1760 | +0.160 | +1287.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 1760 | +0.160 | +1287.47€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 1592 | +0.195 | +1185.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 1592 | +0.195 | +1185.85€ | 0 | 18 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 1769 | +0.138 | +1086.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 1769 | +0.138 | +1086.48€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 2017 | +0.117 | +1259.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 2017 | +0.117 | +1259.56€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 2121 | +0.198 | +1638.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 2121 | +0.198 | +1638.16€ | 0 | 23 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 2430 | +0.107 | +808.78€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 2430 | +0.107 | +808.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 91 | +0.113 | +37.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 91 | +0.113 | +37.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 621 | +0.086 | +181.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 621 | +0.086 | +181.57€ | 0 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 345 | +0.145 | +168.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 345 | +0.145 | +168.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 578 | +0.162 | +242.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 578 | +0.162 | +242.95€ | 0 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 408 | +0.002 | +26.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 408 | +0.002 | +26.19€ | 4 | 4 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 387 | +0.130 | +151.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 387 | +0.130 | +151.73€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 12968 | +0.174 | +9334.89€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#15min | 12968 | +0.174 | +9334.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 1959 | +0.220 | +1647.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 1959 | +0.220 | +1647.84€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 2086 | +0.161 | +1483.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 2086 | +0.161 | +1483.96€ | 0 | 28 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 1982 | +0.221 | +1674.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 1982 | +0.221 | +1674.44€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 2005 | +0.133 | +1202.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 2005 | +0.133 | +1202.11€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 2295 | +0.104 | +1267.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 2295 | +0.104 | +1267.65€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 2641 | +0.204 | +2058.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 2641 | +0.204 | +2058.88€ | 0 | 22 |
| ✅ GBM_LATE_5M | 4037 | +0.124 | +1880.31€ | 1 | 24 |
| ✅ GBM_LATE_5M#5min | 4037 | +0.124 | +1880.31€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 253 | +0.167 | +157.64€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 253 | +0.167 | +157.64€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1049 | +0.109 | +505.96€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1049 | +0.109 | +505.96€ | 1 | 13 |
| ✅ GBM_LATE_5M#DOGE | 604 | +0.158 | +351.64€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 604 | +0.158 | +351.64€ | 0 | 21 |
| ✅ GBM_LATE_5M#ETH | 1327 | +0.141 | +660.77€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 1327 | +0.141 | +660.77€ | 0 | 29 |
| ✅ GBM_LATE_5M#SOL | 173 | -0.014 | +5.96€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 173 | -0.014 | +5.96€ | 2 | 1 |
| ✅ GBM_LATE_5M#XRP | 631 | +0.097 | +198.34€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 631 | +0.097 | +198.34€ | 0 | 0 |
| ✅ GBM_LATE_60M | 796 | +0.023 | +197.29€ | 4 | 13 |
| ✅ GBM_LATE_60M#60min | 796 | +0.023 | +197.29€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 264 | +0.064 | +59.41€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 264 | +0.064 | +59.41€ | 0 | 11 |
| ✅ GBM_LATE_60M#ETH | 292 | +0.037 | +89.04€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 292 | +0.037 | +89.04€ | 3 | 14 |
| ✅ GBM_LATE_60M#SOL | 240 | -0.041 | +48.84€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 240 | -0.041 | +48.84€ | 2 | 7 |
| 🚫 GBM_LATE_60M_FADE | 224 | -0.301 | -36.39€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 224 | -0.301 | -36.39€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 87 | -0.253 | -9.24€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 87 | -0.253 | -9.24€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 74 | -0.355 | -22.17€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 74 | -0.355 | -22.17€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 63 | -0.285 | -4.98€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 63 | -0.285 | -4.98€ | 3 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 457 | +0.040 | +42.25€ | 1 | 5 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 457 | +0.040 | +42.25€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 187 | +0.045 | +25.52€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 187 | +0.045 | +25.52€ | 3 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 122 | +0.048 | -3.59€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 122 | +0.048 | -3.59€ | 1 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 148 | +0.027 | +20.33€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 148 | +0.027 | +20.33€ | 1 | 1 |
| ✅ LATE_WINDOW_5MIN | 44 | +0.217 | +18.24€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 44 | +0.217 | +18.24€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 44 | +0.217 | +18.24€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 44 | +0.217 | +18.24€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 673 | +0.100 | +163.43€ | 0 | 3 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 673 | +0.100 | +163.43€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 673 | +0.100 | +163.43€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 673 | +0.100 | +163.43€ | 0 | 3 |
| ✅ LIQUIDACIONES_15M | 317 | -0.099 | -37.91€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 317 | -0.099 | -37.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 73 | -0.113 | -10.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 73 | -0.113 | -10.20€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 66 | -0.073 | -6.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 66 | -0.073 | -6.94€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 97 | -0.025 | -3.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 97 | -0.025 | -3.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 1283 | -0.009 | -16.21€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 1283 | -0.009 | -16.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 74 | -0.026 | -4.71€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 74 | -0.026 | -4.71€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 151 | -0.029 | -2.51€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 151 | -0.029 | -2.51€ | 3 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 99 | -0.054 | -6.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 99 | -0.054 | -6.47€ | 2 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 420 | +0.021 | +11.51€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 420 | +0.021 | +11.51€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 447 | -0.006 | -8.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 447 | -0.006 | -8.07€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 92 | -0.064 | -5.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 92 | -0.064 | -5.96€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M | 669 | -0.025 | -7.05€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 669 | -0.025 | -7.05€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 197 | -0.043 | -10.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 197 | -0.043 | -10.75€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 203 | -0.002 | +2.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 203 | -0.002 | +2.91€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 269 | -0.028 | +0.78€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 269 | -0.028 | +0.78€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 8100 | -0.003 | -102.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 8100 | -0.003 | -102.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 557 | -0.008 | +0.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 557 | -0.008 | +0.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 880 | -0.018 | -19.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 880 | -0.018 | -19.32€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 1914 | +0.009 | -12.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 1914 | +0.009 | -12.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 1585 | +0.001 | +1.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 1585 | +0.001 | +1.75€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 1686 | -0.010 | -42.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 1686 | -0.010 | -42.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1478 | -0.005 | -30.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1478 | -0.005 | -30.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 13321 | -0.029 | +645.04€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 13321 | -0.029 | +645.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 2228 | -0.015 | +326.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 2228 | -0.015 | +326.55€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 2268 | -0.031 | -17.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 2268 | -0.031 | -17.24€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 2253 | -0.025 | +198.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 2253 | -0.025 | +198.34€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 2156 | -0.047 | -51.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 2156 | -0.047 | -51.06€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 2241 | -0.032 | +104.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 2241 | -0.032 | +104.51€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 2175 | -0.025 | +83.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 2175 | -0.025 | +83.94€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 833 | -0.088 | -47.36€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 833 | -0.088 | -47.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 121 | -0.020 | -3.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 121 | -0.020 | -3.70€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 125 | -0.153 | -15.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 125 | -0.153 | -15.16€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 36 | -0.105 | -4.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 36 | -0.105 | -4.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 172 | -0.167 | -15.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 172 | -0.167 | -15.01€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 238 | -0.058 | -0.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 238 | -0.058 | -0.57€ | 1 | 1 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 141 | -0.032 | -8.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 141 | -0.032 | -8.61€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M | 3185 | +0.004 | -4.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3185 | +0.004 | -4.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 185 | +0.008 | -2.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 185 | +0.008 | -2.27€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 136 | +0.000 | -1.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 136 | +0.000 | -1.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1163 | +0.008 | +8.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1163 | +0.008 | +8.30€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1386 | +0.006 | -1.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1386 | +0.006 | -1.47€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 35792 | -0.078 | +597.95€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 35792 | -0.078 | +597.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 5808 | -0.088 | +424.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 5808 | -0.088 | +424.64€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 5847 | -0.082 | -152.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 5847 | -0.082 | -152.64€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 5946 | -0.084 | +200.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 5946 | -0.084 | +200.30€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 5362 | -0.101 | -309.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 5362 | -0.101 | -309.07€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 6701 | -0.053 | +146.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 6701 | -0.053 | +146.72€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 6128 | -0.065 | +288.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 6128 | -0.065 | +288.01€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 6312 | -0.015 | -112.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 6312 | -0.015 | -112.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 995 | -0.018 | -20.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 995 | -0.018 | -20.76€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1345 | -0.011 | -13.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1345 | -0.011 | -13.76€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1002 | -0.020 | -30.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1002 | -0.020 | -30.79€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1372 | -0.006 | -10.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1372 | -0.006 | -10.19€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 862 | -0.022 | -13.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 862 | -0.022 | -13.83€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 736 | -0.020 | -23.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 736 | -0.020 | -23.66€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 765 | +0.115 | +263.54€ | 1 | 6 |
| ✅ ORDER_FLOW_5M#5min | 629 | +0.128 | +250.95€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 148 | +0.127 | +65.89€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 148 | +0.127 | +65.89€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#DOGE | 126 | +0.094 | +27.35€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 126 | +0.094 | +27.35€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 119 | +0.112 | +44.03€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 119 | +0.112 | +44.03€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 109 | +0.176 | +66.39€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 109 | +0.176 | +66.39€ | 0 | 6 |
| ✅ ORDER_FLOW_5M#XRP | 127 | +0.128 | +47.29€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 127 | +0.128 | +47.29€ | 0 | 6 |
| ✅ PRICE_TARGET_GBM | 357 | -0.130 | -16.07€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 157 | -0.198 | -37.75€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC#atexpiry | 127 | -0.252 | -39.52€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 30 | +0.031 | +1.77€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 134 | -0.103 | +1.91€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 97 | -0.126 | -5.22€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 37 | -0.038 | +7.13€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 66 | -0.015 | +19.77€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 49 | -0.049 | +12.68€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 17 | +0.067 | +7.08€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 273 | -0.173 | -32.05€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 84 | +0.012 | +15.98€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 386 | -0.214 | -17.25€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 167 | -0.180 | -16.16€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 143 | -0.169 | -14.88€ | 4 | 1 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 24 | -0.231 | -1.28€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 139 | -0.259 | -18.00€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 117 | -0.273 | -22.39€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 22 | -0.167 | +4.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 80 | -0.195 | +16.92€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 67 | -0.196 | +13.35€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 13 | -0.108 | +3.57€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 327 | -0.214 | -23.93€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#reach | 59 | -0.205 | +6.68€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 111 | +0.367 | +46.74€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#BTC | 19 | -0.023 | -4.28€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 19 | -0.023 | -4.28€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 26 | +0.321 | +5.89€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 26 | +0.321 | +5.89€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 66 | +0.485 | +45.13€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 66 | +0.485 | +45.13€ | 0 | 1 |
| ✅ RESOLUTION_SNIPER#sniper | 111 | +0.367 | +46.74€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 255 | +0.033 | -2.58€ | 3 | 2 |
| ✅ STREAK_FADE_15M#15min | 255 | +0.033 | -2.58€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 113 | +0.057 | +2.85€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 113 | +0.057 | +2.85€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 18 | +0.045 | +2.16€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 18 | +0.045 | +2.16€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 26 | +0.000 | -2.84€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 26 | +0.000 | -2.84€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP | 98 | +0.010 | -4.75€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 98 | +0.010 | -4.75€ | 0 | 0 |
| ✅ STREAK_FADE_5M | 1947 | -0.023 | -85.35€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 1947 | -0.023 | -85.35€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 801 | -0.018 | -26.43€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 801 | -0.018 | -26.43€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 553 | -0.026 | -25.13€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 553 | -0.026 | -25.13€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 141 | -0.038 | -12.96€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 141 | -0.038 | -12.96€ | 3 | 0 |
| ✅ STREAK_FADE_5M#XRP | 452 | -0.024 | -20.83€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 452 | -0.024 | -20.83€ | 4 | 0 |
| ✅ STREAK_FADE_60M | 45 | +0.011 | -0.05€ | 0 | 0 |
| ✅ STREAK_FADE_60M#60min | 45 | +0.011 | -0.05€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 28 | -0.067 | -2.41€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 28 | -0.067 | -2.41€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 17 | +0.112 | +2.36€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 17 | +0.112 | +2.36€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 4160 | +0.017 | +41.10€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 4160 | +0.017 | +41.10€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 1356 | +0.018 | +8.88€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 1356 | +0.018 | +8.88€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 848 | +0.031 | +26.85€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 848 | +0.031 | +26.85€ | 1 | 1 |
| ✅ STREAK_MOM_5M#SOL | 1223 | +0.006 | -7.84€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 1223 | +0.006 | -7.84€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 733 | +0.016 | +13.21€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 733 | +0.016 | +13.21€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 4431 | +0.012 | -24.69€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 4431 | +0.012 | -24.69€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 1700 | +0.012 | -10.81€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 1700 | +0.012 | -10.81€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 1766 | +0.020 | +4.43€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 1766 | +0.020 | +4.43€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 965 | -0.004 | -18.31€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 965 | -0.004 | -18.31€ | 2 | 0 |
| ✅ UPDOWN_GBM | 11370 | +0.011 | +383.31€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 3850 | +0.041 | +424.06€ | 0 | 12 |
| ✅ UPDOWN_GBM#240min | 478 | +0.006 | +6.32€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 6266 | -0.002 | -37.33€ | 1 | 0 |
| ✅ UPDOWN_GBM#60min | 720 | -0.007 | -7.96€ | 2 | 0 |
| ✅ UPDOWN_GBM#BNB | 567 | +0.068 | +57.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 188 | +0.111 | +41.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 11 | -0.021 | -0.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 368 | +0.049 | +15.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 2078 | +0.014 | +117.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 442 | +0.074 | +94.80€ | 1 | 8 |
| ✅ UPDOWN_GBM#BTC#240min | 145 | +0.044 | +8.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 1183 | -0.005 | +17.83€ | 3 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 287 | -0.002 | -4.49€ | 3 | 1 |
| ✅ UPDOWN_GBM#BTC#daily | 21 | -0.152 | +0.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 1344 | +0.010 | +13.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 130 | +0.091 | +29.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 10 | +0.042 | +0.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 1204 | +0.000 | -17.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 2301 | -0.001 | +12.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 1097 | +0.028 | +43.40€ | 1 | 5 |
| ✅ UPDOWN_GBM#ETH#240min | 135 | +0.018 | +7.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 763 | -0.037 | -34.35€ | 4 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 287 | -0.012 | -3.54€ | 2 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 19 | -0.158 | +0.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 3229 | +0.003 | +23.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 1017 | +0.006 | +28.36€ | 1 | 11 |
| ✅ UPDOWN_GBM#SOL#240min | 129 | -0.004 | -2.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 1923 | +0.004 | -1.06€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 146 | -0.007 | +0.07€ | 1 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 14 | -0.175 | -1.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 1849 | +0.022 | +161.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 976 | +0.054 | +185.57€ | 0 | 10 |
| ✅ UPDOWN_GBM#XRP#240min | 48 | -0.120 | -6.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 825 | -0.008 | -17.82€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 54 | -0.196 | +0.06€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 278 | +0.321 | +64.14€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 278 | +0.321 | +64.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 162 | +0.311 | +29.07€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 162 | +0.311 | +29.07€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 116 | +0.331 | +35.06€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 116 | +0.331 | +35.06€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 6082 | -0.064 | +1341.38€ | 4 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 6082 | -0.064 | +1341.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 311 | -0.050 | +343.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 311 | -0.050 | +343.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 1243 | -0.147 | -56.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 1243 | -0.147 | -56.24€ | 3 | 3 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 81 | +0.042 | +8.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 81 | +0.042 | +8.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 568 | +0.163 | +283.00€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 568 | +0.163 | +283.00€ | 2 | 16 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 1987 | -0.065 | +384.48€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 1987 | -0.065 | +384.48€ | 4 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 1892 | -0.084 | +378.72€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 1892 | -0.084 | +378.72€ | 2 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 58 | +0.067 | +3.64€ | 0 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 58 | +0.067 | +3.64€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 58 | +0.067 | +3.64€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 58 | +0.067 | +3.64€ | 0 | 6 |
| ✅ UPDOWN_GBM_IBS_ALTO | 478 | +0.283 | +375.87€ | 0 | 12 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 478 | +0.283 | +375.87€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 273 | +0.282 | +214.63€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 273 | +0.282 | +214.63€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 205 | +0.283 | +161.23€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 205 | +0.283 | +161.23€ | 0 | 13 |
| ✅ UPDOWN_OU_5M | 649 | -0.101 | -72.54€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#5min | 649 | -0.101 | -72.54€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 310 | -0.077 | -35.00€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 310 | -0.077 | -35.00€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 160 | -0.049 | -8.74€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 160 | -0.049 | -8.74€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 60 | -0.177 | -9.28€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 60 | -0.177 | -9.28€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 52 | -0.167 | -5.48€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 52 | -0.167 | -5.48€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 1471 | +0.296 | +656.89€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 477 | +0.229 | +25.18€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 491 | +0.279 | +154.58€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 503 | +0.373 | +477.13€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.081) — sin ventaja clara. oversold(IBS<0.3): IC=+0.025 n=3976 | neutral: IC=+0.007 n=4427 | overbought(IBS>0.7): IC=+0.088 n=4434
  - _Datos_: n=13332 IC=+0.041 PNL=+1394.49€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 235 celda(s) pasan gate riguroso completo de 1499 evaluadas (n>=40) y 2553 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.006 < 0.08 — monitorear
  - _Datos_: n=1017 IC=+0.006 PNL=+28.36€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=491/15 IC=+0.279 PNL=+154.58€ | BTC: n=477/15 IC=+0.229 PNL=+25.18€ | SOL: n=503/15 IC=+0.373 PNL=+477.13€

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 23 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH#60min, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC#60min
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
  - _Estado_: 11308 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.013 n=76/60 | contraria IC=+0.135 n=50 | gap=-0.122 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=162, boost estimado=-0.002. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 109 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=287/40 IC=-0.012 PNL=-3.54€ | BTC#60min: n=287/40 IC=-0.002 PNL=-4.49€ | SOL#60min: n=146/40 IC=-0.007 PNL=+0.07€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.063 n=168300 | tras_1loss IC=+0.054 n=132880 | tras_2loss IC=+0.018 n=59247/40 | gap=+0.045 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=-0.005 n=992 | contrario_BTC IC=-0.006 n=892/40 | gap=-0.001 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.215 > 0.08 con n=121 PNL=+89.35€
  - _Datos_: n=121 IC=+0.215 PNL=+89.35€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.145 > 0.08 con n=153 PNL=+52.49€
  - _Datos_: n=153 IC=+0.145 PNL=+52.49€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.278 > 0.08 con n=25 PNL=+21.66€
  - _Datos_: n=25 IC=+0.278 PNL=+21.66€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.336 > 0.1 con n=1238 PNL=+657.09€
  - _Datos_: n=1238 IC=+0.336 PNL=+657.09€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=88 IC=+0.033 PNL=+13.44€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=88 IC=+0.033 PNL=+13.44€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=33 IC=+0.186 PNL=+20.93€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=33 IC=+0.186 PNL=+20.93€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=11001 IC=+0.010 PNL=+330.53€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=11001 IC=+0.010 PNL=+330.53€

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
  - _Estado_: n=558 IC=+0.005 PNL=-1.15€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=558 IC=+0.005 PNL=-1.15€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=162 IC=-0.049 PNL=-6.81€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=162 IC=-0.049 PNL=-6.81€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=196 IC=-0.020 PNL=+4.24€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=196 IC=-0.020 PNL=+4.24€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.140 > 0.1 con n=812 PNL=+299.10€
  - _Datos_: n=812 IC=+0.140 PNL=+299.10€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=243 IC=+0.043 PNL=+37.64€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=243 IC=+0.043 PNL=+37.64€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=442 IC=+0.074 PNL=+94.80€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=442 IC=+0.074 PNL=+94.80€

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
  - _Estado_: n=2245 IC=+0.037 PNL=+259.94€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2245 IC=+0.037 PNL=+259.94€

**〰️ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: n=55 IC=-0.254 PNL=-6.56€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=55 IC=-0.254 PNL=-6.56€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=113 IC=-0.013 PNL=+8.43€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=113 IC=-0.013 PNL=+8.43€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=170 IC=+0.029 PNL=+16.61€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=170 IC=+0.029 PNL=+16.61€

**⏳ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: 15
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: 11/15 ops en el filtro definido (IC actual=+0.064 PNL=+1.63€)
  - _Datos_: n=11 IC=+0.064 PNL=+1.63€

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=2659 IC=-0.016 PNL=-42.97€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2659 IC=-0.016 PNL=-42.97€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.217 n=44) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=44 IC=+0.217 PNL=+18.24€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=2797 IC=+0.015 PNL=+123.09€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2797 IC=+0.015 PNL=+123.09€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=854 IC=+0.034 PNL=+41.90€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=854 IC=+0.034 PNL=+41.90€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.113 > 0.08 con n=228 PNL=+66.37€
  - _Datos_: n=228 IC=+0.113 PNL=+66.37€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.122 > 0.08 con n=207 PNL=+29.53€
  - _Datos_: n=207 IC=+0.122 PNL=+29.53€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.141 > 0.08 con n=182 PNL=+70.61€
  - _Datos_: n=182 IC=+0.141 PNL=+70.61€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=27153 IC=+0.103 PNL=+8552.65€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=27153 IC=+0.103 PNL=+8552.65€

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
  - _Estado_: n=1543 IC=+0.035 PNL=+91.46€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1543 IC=+0.035 PNL=+91.46€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.130 > 0.02 con n=430 PNL=+163.86€
  - _Datos_: n=430 IC=+0.130 PNL=+163.86€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.446 > 0.1 con n=761 PNL=+690.83€
  - _Datos_: n=761 IC=+0.446 PNL=+690.83€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=2978 IC=+0.039 PNL=+286.13€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=2978 IC=+0.039 PNL=+286.13€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.169 > 0.1 con n=1227 PNL=+504.56€
  - _Datos_: n=1227 IC=+0.169 PNL=+504.56€

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.189 < -0.1 con n=72 PNL=+3.27€
  - _Datos_: n=72 IC=-0.189 PNL=+3.27€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=754 IC=+0.030 PNL=+80.61€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=754 IC=+0.030 PNL=+80.61€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=35 IC=-0.176 PNL=+2.62€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=35 IC=-0.176 PNL=+2.62€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.119 > 0.1 con n=145 PNL=+37.82€
  - _Datos_: n=145 IC=+0.119 PNL=+37.82€

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
  - _Estado_: n=8606 IC=-0.139 PNL=+496.15€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=8606 IC=-0.139 PNL=+496.15€

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
  - _Estado_: n=1007 IC=+0.144 PNL=+551.86€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=1007 IC=+0.144 PNL=+551.86€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.142 > 0.08 con n=774 PNL=+284.73€
  - _Datos_: n=774 IC=+0.142 PNL=+284.73€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=1115 IC=+0.004 PNL=+11.33€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1115 IC=+0.004 PNL=+11.33€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.083 > 0.08 con n=1018 PNL=+603.01€
  - _Datos_: n=1018 IC=+0.083 PNL=+603.01€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.174 > 0.08 con n=225 PNL=+94.89€
  - _Datos_: n=225 IC=+0.174 PNL=+94.89€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.236 < -0.1 con n=933 PNL=-106.99€
  - _Datos_: n=933 IC=-0.236 PNL=-106.99€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=2414 IC=+0.143 PNL=+1445.23€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=2414 IC=+0.143 PNL=+1445.23€

**〰️ H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: n≥40 en cada rama (contrario y alineado) para separar señal de ruido
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: n=50 IC=+0.077 PNL=+10.85€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=50 IC=+0.077 PNL=+10.85€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=1019 IC=+0.004 PNL=+134.17€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1019 IC=+0.004 PNL=+134.17€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.187 > 0.08 con n=932 PNL=+646.46€
  - _Datos_: n=932 IC=+0.187 PNL=+646.46€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=1532 IC=-0.055 PNL=+337.46€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1532 IC=-0.055 PNL=+337.46€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.103 > 0.08 con n=333 PNL=-39.87€
  - _Datos_: n=333 IC=+0.103 PNL=-39.87€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.227 > 0.08 con n=2145 PNL=-222.60€
  - _Datos_: n=2145 IC=+0.227 PNL=-222.60€

**⏳ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: 19/40 ops en el filtro definido (IC actual=-0.068 PNL=+3.27€)
  - _Datos_: n=19 IC=-0.068 PNL=+3.27€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.093 n=362) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=362 IC=+0.093 PNL=+85.72€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.317 > 0.08 con n=118 PNL=+58.85€
  - _Datos_: n=118 IC=+0.317 PNL=+58.85€

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.421 n=301) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=301 IC=+0.421 PNL=+417.34€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=4929 IC=+0.154 PNL=-738.65€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=4929 IC=+0.154 PNL=-738.65€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.250 > 0.1 con n=66 PNL=+47.81€
  - _Datos_: n=66 IC=+0.250 PNL=+47.81€
