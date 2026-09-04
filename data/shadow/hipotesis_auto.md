# Hipótesis automáticas — 2026-09-04 02:43 UTC
_Generado por shadow_postmortem.py sobre 274906 resoluciones (PNL=+26747.58€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.505` → IC=-0.170 (n=107)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.256 (n=338)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.392 (n=81)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.127 (n=285)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.256 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.153)

- **PATRÓN** `n_ballena_banda` > `19.0` → IC=+0.166 (n=306)

  - _Acción_: Kelly boost +0.83€ cuando `n_ballena_banda` > 19.0 (IC base=+0.153)

- **PATRÓN** `n_total_lado` > `74.0` → IC=+0.248 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 74.0 (IC base=+0.153)

- **PATRÓN** `banda_hit_calibrado` > `0.6242` → IC=+0.252 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6242 (IC base=+0.153)

- **PATRÓN** `banda_z` > `11.788` → IC=+0.274 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.788 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.172 (n=236)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 11.0 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.153 (n=223)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 11.0 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.179 (n=347)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `3094.8617` → IC=+0.201 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3094.8617 (IC base=+0.153)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.127 (n=285)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.5 (IC base=+0.011)

- **PATRÓN** `ballena_activa_n` < `101.0` → IC=+0.125 (n=38)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 101.0 (IC base=+0.011)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=159)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=184)

- **PATRÓN** `py_entrada` > `0.705` → IC=+0.279 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.705 (IC base=+0.184)

- **PATRÓN** `n_ballena_banda` > `18.0` → IC=+0.195 (n=244)

  - _Acción_: Kelly boost +0.98€ cuando `n_ballena_banda` > 18.0 (IC base=+0.184)

- **PATRÓN** `n_total_lado` > `69.0` → IC=+0.247 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 69.0 (IC base=+0.184)

- **PATRÓN** `banda_hit_calibrado` > `0.802` → IC=+0.270 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.802 (IC base=+0.184)

- **PATRÓN** `banda_z` > `11.795` → IC=+0.268 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.795 (IC base=+0.184)

- **PATRÓN** `ballenas_wallet_edge_medio` > `3.102` → IC=+0.191 (n=79)

  - _Acción_: Kelly boost +0.96€ cuando `ballenas_wallet_edge_medio` > 3.102 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.192 (n=222)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 7.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.192 (n=170)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 12.0 (IC base=+0.184)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.202 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.184)

- **PATRÓN** `libro_liquidez` > `2935.919` → IC=+0.199 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2935.919 (IC base=+0.184)

- **PATRÓN** `py_entrada` < `0.485` → IC=+0.127 (n=116)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.485 (IC base=-0.007)

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
- **FILTRO** `restante_s_al_confirmar` < `146.54` → IC=-0.299 (n=3703)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 146.54
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=11115)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `139.02` → IC=-0.293 (n=481)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 139.02
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=1444)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` > `625.49` → IC=-0.139 (n=325)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` > 625.49
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=631)

- **FILTRO** `restante_s_al_confirmar` < `458.09` → IC=-0.172 (n=239)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 458.09
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=717)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `113.23` → IC=-0.405 (n=494)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 113.23
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=1483)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `142.85` → IC=-0.314 (n=822)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 142.85
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=2469)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `156.95` → IC=-0.378 (n=893)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 156.95
  - _Potencial_: sin este filtro IC_bueno=-0.104 (n=1817)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.7` → IC=+0.188 (n=8022)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.7 (IC base=+0.094)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.168 (n=2027)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.094)

- **PATRÓN** `libro_liquidez` > `2371.8427` → IC=+0.170 (n=1943)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2371.8427 (IC base=+0.094)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.146 (n=4825)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 18.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.153 (n=6486)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.141)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.253 (n=4899)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.184 (n=3854)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.02 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `1930.2375` → IC=+0.175 (n=3295)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 1930.2375 (IC base=+0.141)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.221 (n=893)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.207 (n=876)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.205)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.389 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.208 (n=1096)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `13087.3924` → IC=+0.221 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13087.3924 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.196 (n=831)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 7.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.200 (n=912)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` < `0.365` → IC=+0.259 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.365 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.191 (n=1171)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.01 (IC base=+0.189)

- **PATRÓN** `libro_liquidez` > `12459.7568` → IC=+0.208 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12459.7568 (IC base=+0.189)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.131 (n=660)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.115)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.125 (n=563)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 15.0 (IC base=+0.115)

- **PATRÓN** `py_entrada` > `0.555` → IC=+0.135 (n=633)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` > 0.555 (IC base=+0.115)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.130 (n=271)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `4800.0243` → IC=+0.151 (n=216)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4800.0243 (IC base=+0.115)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.191 (n=215)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 7.0 (IC base=+0.129)

- **PATRÓN** `py_entrada` < `0.41` → IC=+0.179 (n=331)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.41 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `5297.7285` → IC=+0.162 (n=235)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 5297.7285 (IC base=+0.129)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=93)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=1637)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.139 (n=1376)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 15.0 (IC base=+0.134)

- **PATRÓN** `py_entrada` > `0.69` → IC=+0.311 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.264 (n=624)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.259)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.264 (n=700)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.259)

- **PATRÓN** `py_entrada` < `0.2` → IC=+0.405 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.2 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.262 (n=707)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1943.5814` → IC=+0.267 (n=676)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1943.5814 (IC base=+0.259)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.137 (n=268)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 11.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.150 (n=338)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 15.0 (IC base=+0.135)

- **PATRÓN** `py_entrada` > `0.66` → IC=+0.260 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.66 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.144 (n=459)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.02 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `1872.8486` → IC=+0.160 (n=339)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 1872.8486 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.164 (n=144)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.072)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.214 (n=390)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` > `0.84` → IC=+0.424 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.84 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.213 (n=360)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.206)

- **PATRÓN** `py_entrada` < `0.225` → IC=+0.348 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.225 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.214 (n=805)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `918.1633` → IC=+0.216 (n=773)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 918.1633 (IC base=+0.206)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.192 (n=277)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 6.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.333 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.194 (n=171)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.02 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `3436.329` → IC=+0.181 (n=67)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 3436.329 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.125 (n=537)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 7.0 (IC base=+0.109)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.220 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.109)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.143 (n=295)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.02 (IC base=+0.109)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.8` → IC=-0.344 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=128)

- **FILTRO** `libro_liquidez` < `11311.3585` → IC=-0.264 (n=142)

  - _Acción_: SKIP cuando `libro_liquidez` < 11311.3585
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=48)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.195 (n=6150)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.195 (n=5202)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.188)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.202 (n=2944)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `3780.1464` → IC=+0.329 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3780.1464 (IC base=+0.188)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.177 (n=1349)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 15.0 (IC base=+0.165)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.179 (n=1587)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.74 (IC base=+0.165)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.244 (n=88)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.236 (n=89)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.420 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.330)

- **PATRÓN** `py_entrada` > `0.835` → IC=+0.380 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.835 (IC base=+0.330)

- **PATRÓN** `libro_liquidez` > `2916.5858` → IC=+0.343 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2916.5858 (IC base=+0.330)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.173 (n=1489)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 6.0 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.175 (n=1314)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 15.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.173 (n=1592)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.74 (IC base=+0.168)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.179 (n=1063)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` > 0.72 (IC base=+0.168)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.248 (n=1397)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.238 (n=1184)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.237)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.315 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.237)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.195 (n=1514)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.186 (n=1286)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 15.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.189 (n=788)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.7 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.182 (n=649)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.73 (IC base=+0.182)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.455 (n=266)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.447)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.449 (n=274)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.447)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.481 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.447)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.446 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.447)

- **PATRÓN** `libro_liquidez` > `3369.9988` → IC=+0.460 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3369.9988 (IC base=+0.447)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.447 (n=112)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.440)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.443 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.440)

- **PATRÓN** `libro_liquidez` > `10788.5508` → IC=+0.461 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10788.5508 (IC base=+0.440)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.456 (n=112)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.454 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.442)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.438 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.442)

- **PATRÓN** `libro_liquidez` > `2080.8345` → IC=+0.458 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2080.8345 (IC base=+0.442)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.438 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.446)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.446 (n=72)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.446)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.441 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.446)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.446)

- **PATRÓN** `libro_liquidez` > `1927.8949` → IC=+0.439 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1927.8949 (IC base=+0.446)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.198 (n=6364)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 18.0 (IC base=+0.187)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.206 (n=17480)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.187)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.151 (n=3575)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.147 (n=2425)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 12.0 (IC base=+0.146)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.176 (n=2575)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` > 0.72 (IC base=+0.146)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.228 (n=3008)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.258 (n=2217)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.225)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.177 (n=1111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 18.0 (IC base=+0.161)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.178 (n=3016)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` > 0.71 (IC base=+0.161)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.232 (n=1540)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.224 (n=1143)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.220)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.269 (n=1097)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.220)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.217 (n=1053)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.237 (n=1507)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.199)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.191 (n=1078)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 18.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.185 (n=2274)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 12.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.227 (n=1497)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.182)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.205 (n=2463)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.133)

- **PATRÓN** `restante_min` < `4.01` → IC=+0.147 (n=2323)

  - _Acción_: Kelly boost +0.73€ cuando `restante_min` < 4.01 (IC base=+0.133)

- **PATRÓN** `restante_min` > `4.93` → IC=+0.153 (n=2500)

  - _Acción_: Kelly boost +0.77€ cuando `restante_min` > 4.93 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.151 (n=3392)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 8.0 (IC base=+0.133)

- **PATRÓN** `lag_apertura_s` < `4.08` → IC=+0.157 (n=2312)

  - _Acción_: Kelly boost +0.78€ cuando `lag_apertura_s` < 4.08 (IC base=+0.133)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.210 (n=1245)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.138)

- **PATRÓN** `restante_min` < `3.95` → IC=+0.152 (n=1152)

  - _Acción_: Kelly boost +0.76€ cuando `restante_min` < 3.95 (IC base=+0.138)

- **PATRÓN** `restante_min` > `4.88` → IC=+0.152 (n=1594)

  - _Acción_: Kelly boost +0.76€ cuando `restante_min` > 4.88 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.163 (n=1677)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 8.0 (IC base=+0.138)

- **PATRÓN** `lag_apertura_s` < `6.97` → IC=+0.151 (n=1518)

  - _Acción_: Kelly boost +0.76€ cuando `lag_apertura_s` < 6.97 (IC base=+0.138)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.199 (n=1218)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.128)

- **PATRÓN** `restante_min` < `4.44` → IC=+0.136 (n=1543)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` < 4.44 (IC base=+0.128)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.160 (n=1307)

  - _Acción_: Kelly boost +0.80€ cuando `restante_min` > 4.94 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.130 (n=3489)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 6.0 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.139 (n=1715)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 8.0 (IC base=+0.128)

- **PATRÓN** `lag_apertura_s` < `3.32` → IC=+0.168 (n=1167)

  - _Acción_: Kelly boost +0.84€ cuando `lag_apertura_s` < 3.32 (IC base=+0.128)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.314 (n=637)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.293)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.293 (n=645)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.293)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.366 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `1765.9885` → IC=+0.294 (n=711)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1765.9885 (IC base=+0.293)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.295 (n=276)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.276)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.352 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.276)

- **PATRÓN** `libro_liquidez` > `4053.2751` → IC=+0.287 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4053.2751 (IC base=+0.276)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.336 (n=236)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.299)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.376 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.299)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.298 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.299)

- **PATRÓN** `libro_liquidez` > `1604.9934` → IC=+0.319 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1604.9934 (IC base=+0.299)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.338 (n=72)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.330)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.348 (n=64)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.330)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.367 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.330)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.346 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.330)

- **PATRÓN** `libro_liquidez` > `687.7728` → IC=+0.373 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 687.7728 (IC base=+0.330)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.436 (n=324)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.422)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.431 (n=272)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.422)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.426 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.422)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.432 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.422)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.422 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.422)

- **PATRÓN** `libro_liquidez` > `1988.111` → IC=+0.434 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1988.111 (IC base=+0.422)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.437 (n=140)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.419)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.429 (n=139)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.419)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.420 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.419)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.430 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.419)

- **PATRÓN** `libro_liquidez` > `5487.0105` → IC=+0.458 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5487.0105 (IC base=+0.419)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.433 (n=133)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.426)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.440 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.426)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.423 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.426)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.424 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.426)

- **PATRÓN** `libro_liquidez` > `1981.0007` → IC=+0.458 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1981.0007 (IC base=+0.426)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `py_entrada` > `0.93` → IC=+0.441 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.365)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.314 (n=159)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.263)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.423 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.263)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.283 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.263)

- **PATRÓN** `libro_liquidez` > `1042.1643` → IC=+0.280 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1042.1643 (IC base=+0.263)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.314 (n=159)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.263)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.423 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.263)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.283 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.263)

- **PATRÓN** `libro_liquidez` > `1042.1643` → IC=+0.280 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1042.1643 (IC base=+0.263)

### GBM_LATE_15M
- **PATRÓN** `ibs_20min` > `0.3571` → IC=+0.127 (n=3679)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` > 0.3571 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` > `0.1833` → IC=+0.223 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1833 (IC base=+0.080)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.606` → IC=+0.149 (n=1407)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 5.606 (IC base=+0.080)

- **PATRÓN** `volumen_regimen` < `0.6963` → IC=+0.220 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6963 (IC base=+0.080)

- **PATRÓN** `volumen_regimen` > `1.0858` → IC=+0.241 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0858 (IC base=+0.080)

- **PATRÓN** `volumen_pendiente_norm` > `0.1732` → IC=+0.175 (n=628)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1732 (IC base=+0.080)

- **PATRÓN** `volumen_spike_ratio` < `2.8793` → IC=+0.172 (n=2203)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 2.8793 (IC base=+0.080)

- **PATRÓN** `volumen_spike_ratio` > `1.4772` → IC=+0.169 (n=2203)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.4772 (IC base=+0.080)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.197 (n=1103)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 54.0 (IC base=+0.080)

- **PATRÓN** `ibs_20min` < `0.4028` → IC=+0.129 (n=3540)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` < 0.4028 (IC base=+0.042)

- **PATRÓN** `dist_vwap_pct` < `0.3413` → IC=+0.146 (n=1288)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.3413 (IC base=+0.042)

- **PATRÓN** `volumen_regimen` < `0.6876` → IC=+0.153 (n=551)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6876 (IC base=+0.042)

- **PATRÓN** `volumen_regimen` > `1.0462` → IC=+0.139 (n=568)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 1.0462 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.3041` → IC=+0.252 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3041 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` > `2.8566` → IC=+0.214 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8566 (IC base=+0.042)

- **PATRÓN** `ballena_activa_n` < `126.0` → IC=+0.215 (n=1429)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 126.0 (IC base=+0.042)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.184 (n=273)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0076 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.2797` → IC=+0.156 (n=820)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.2797 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.199 (n=300)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.273 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.634` → IC=+0.296 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.634 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.2291` → IC=+0.222 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2291 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.6736` → IC=+0.137 (n=722)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.6736 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `1.4481` → IC=+0.144 (n=722)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.4481 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.188 (n=655)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.04 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `62.0` → IC=+0.186 (n=469)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 62.0 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.260 (n=365)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.259)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.275 (n=491)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.259)

- **PATRÓN** `drift_60min` |x|≤ `0.1091` → IC=+0.324 (n=242)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1091 (IC base=+0.259)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.265 (n=500)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.259)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.271 (n=547)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.259)

- **PATRÓN** `ibs_20min` < `0.4014` → IC=+0.285 (n=482)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4014 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.165` → IC=+0.274 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.165 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` < `0.0675` → IC=+0.260 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0675 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` > `0.2958` → IC=+0.359 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2958 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` > `1.6099` → IC=+0.283 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6099 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.271 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1702.02` → IC=+0.285 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1702.02 (IC base=+0.259)

- **PATRÓN** `ballena_activa_n` < `64.0` → IC=+0.260 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 64.0 (IC base=+0.259)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.251 (n=215)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.210)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.224 (n=215)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.0973` → IC=+0.237 (n=215)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0973 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=672)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.9263` → IC=+0.239 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9263 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` > `0.1838` → IC=+0.221 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1838 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` < `0.4813` → IC=+0.213 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4813 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.225` → IC=+0.222 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.225 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.011` → IC=+0.211 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.011 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` < `1.2608` → IC=+0.214 (n=645)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2608 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` > `1.099` → IC=+0.225 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.099 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` < `0.0999` → IC=+0.215 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0999 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `1.4875` → IC=+0.242 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4875 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `11865.8018` → IC=+0.239 (n=576)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11865.8018 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.155 (n=471)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.004 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.1766` → IC=+0.153 (n=471)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1766 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.141 (n=636)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 8.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.148 (n=237)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 5.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` < `0.6598` → IC=+0.165 (n=706)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.6598 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` < `0.3368` → IC=+0.159 (n=679)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.3368 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.496` → IC=+0.217 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.496 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `0.618` → IC=+0.181 (n=236)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.618 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.1499` → IC=+0.219 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1499 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `1.7277` → IC=+0.157 (n=400)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.7277 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `1.3961` → IC=+0.157 (n=599)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.3961 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `12554.3019` → IC=+0.153 (n=471)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 12554.3019 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `294.0` → IC=+0.157 (n=342)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 294.0 (IC base=+0.141)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.204 (n=258)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.160)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.198 (n=289)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.160)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.257 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.160)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.319` → IC=+0.266 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.319 (IC base=+0.160)

- **PATRÓN** `volumen_pendiente_norm` < `0.1322` → IC=+0.158 (n=662)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` < 0.1322 (IC base=+0.160)

- **PATRÓN** `volumen_pendiente_norm` > `0.3896` → IC=+0.153 (n=96)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.3896 (IC base=+0.160)

- **PATRÓN** `volumen_spike_ratio` < `3.8947` → IC=+0.152 (n=688)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 3.8947 (IC base=+0.160)

- **PATRÓN** `volumen_spike_ratio` > `1.896` → IC=+0.174 (n=615)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.896 (IC base=+0.160)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.183 (n=796)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.04 (IC base=+0.160)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.216 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.160)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.254 (n=629)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.3789` → IC=+0.245 (n=552)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3789 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.245 (n=312)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.266 (n=288)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.0351` → IC=+0.307 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0351 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.545` → IC=+0.310 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.545 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.3786` → IC=+0.305 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3786 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` < `1.7033` → IC=+0.272 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7033 (IC base=+0.241)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.228 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 52.0 (IC base=+0.241)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.145 (n=170)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=544)

- **FILTRO** `ibs_20min` > `0.8252` → IC=-0.187 (n=289)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8252
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=868)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.149 (n=72)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=1085)

- **PATRÓN** `dist_vwap_pct` > `0.377` → IC=+0.271 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.377 (IC base=-0.032)

- **PATRÓN** `dist_vwap_pct` < `0.2033` → IC=+0.278 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2033 (IC base=-0.032)

- **PATRÓN** `volumen_regimen` < `0.6119` → IC=+0.362 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6119 (IC base=-0.032)

- **PATRÓN** `volumen_regimen` > `1.1956` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1956 (IC base=-0.032)

- **PATRÓN** `volumen_pendiente_norm` < `0.1203` → IC=+0.259 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1203 (IC base=-0.032)

- **PATRÓN** `volumen_pendiente_norm` > `0.2279` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2279 (IC base=-0.032)

- **PATRÓN** `volumen_spike_ratio` < `1.4376` → IC=+0.352 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4376 (IC base=-0.032)

- **PATRÓN** `volumen_spike_ratio` > `1.924` → IC=+0.269 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.924 (IC base=-0.032)

- **PATRÓN** `ballena_activa_n` < `175.0` → IC=+0.268 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 175.0 (IC base=-0.032)

- **PATRÓN** `dist_vwap_pct` > `0.293` → IC=+0.177 (n=60)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.293 (IC base=-0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.2781` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2781 (IC base=-0.040)

- **PATRÓN** `volumen_spike_ratio` > `1.573` → IC=+0.134 (n=181)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.573 (IC base=-0.040)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.143 (n=40)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=143)

- **FILTRO** `ibs_20min` < `0.28` → IC=-0.161 (n=60)

  - _Acción_: SKIP cuando `ibs_20min` < 0.28
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=123)

- **FILTRO** `sigma_ewma_delta_pct` > `8.312` → IC=-0.193 (n=203)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.312
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=1564)

- **FILTRO** `volumen_pendiente_norm` < `0.1267` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.1267
  - _Potencial_: sin este filtro IC_bueno=+0.196 (n=21)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.156 (n=62)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0066 (IC base=+0.041)

- **PATRÓN** `ibs_20min` > `0.28` → IC=+0.140 (n=123)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` > 0.28 (IC base=+0.041)

- **PATRÓN** `volumen_regimen` > `0.7744` → IC=+0.385 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7744 (IC base=+0.041)

- **PATRÓN** `volumen_spike_ratio` < `1.6091` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6091 (IC base=+0.041)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.375 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.041)

- **PATRÓN** `volumen_pendiente_norm` > `0.1267` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.1267 (IC base=-0.057)

- **PATRÓN** `volumen_spike_ratio` < `1.6234` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6234 (IC base=-0.057)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.5305` → IC=-0.158 (n=349)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.5305
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=679)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.198 (n=114)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=914)

- **FILTRO** `ibs_20min` > `0.7902` → IC=-0.188 (n=412)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7902
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=1237)

- **FILTRO** `sigma_ewma_delta_pct` > `8.885` → IC=-0.137 (n=191)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.885
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=1458)

- **PATRÓN** `dist_vwap_pct` > `0.5816` → IC=+0.342 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5816 (IC base=-0.103)

- **PATRÓN** `dist_vwap_pct` < `0.2197` → IC=+0.190 (n=69)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.2197 (IC base=-0.103)

- **PATRÓN** `volumen_regimen` > `0.6895` → IC=+0.237 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6895 (IC base=-0.103)

- **PATRÓN** `volumen_pendiente_norm` > `0.0602` → IC=+0.294 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0602 (IC base=-0.103)

- **PATRÓN** `volumen_spike_ratio` < `1.5219` → IC=+0.242 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5219 (IC base=-0.103)

- **PATRÓN** `volumen_spike_ratio` > `2.2623` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2623 (IC base=-0.103)

- **PATRÓN** `dist_vwap_pct` < `0.2681` → IC=+0.220 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2681 (IC base=-0.047)

- **PATRÓN** `volumen_regimen` < `0.742` → IC=+0.195 (n=93)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 0.742 (IC base=-0.047)

- **PATRÓN** `volumen_regimen` > `1.3132` → IC=+0.264 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.3132 (IC base=-0.047)

- **PATRÓN** `volumen_pendiente_norm` > `0.0964` → IC=+0.208 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0964 (IC base=-0.047)

- **PATRÓN** `volumen_spike_ratio` < `2.6599` → IC=+0.176 (n=106)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 2.6599 (IC base=-0.047)

- **PATRÓN** `volumen_spike_ratio` > `1.906` → IC=+0.167 (n=70)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.906 (IC base=-0.047)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.158 (n=71)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 20.0 (IC base=-0.047)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.172 (n=1515)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0094 (IC base=+0.070)

- **PATRÓN** `ibs_20min` > `0.2906` → IC=+0.139 (n=4543)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 0.2906 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.9224` → IC=+0.289 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9224 (IC base=+0.070)

- **PATRÓN** `volumen_regimen` > `0.6815` → IC=+0.217 (n=1317)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6815 (IC base=+0.070)

- **PATRÓN** `volumen_pendiente_norm` < `0.115` → IC=+0.212 (n=2143)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.115 (IC base=+0.070)

- **PATRÓN** `volumen_pendiente_norm` > `0.2534` → IC=+0.232 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2534 (IC base=+0.070)

- **PATRÓN** `volumen_spike_ratio` < `1.4925` → IC=+0.230 (n=738)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4925 (IC base=+0.070)

- **PATRÓN** `volumen_spike_ratio` > `2.8297` → IC=+0.223 (n=738)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8297 (IC base=+0.070)

- **PATRÓN** `ballena_activa_n` < `95.0` → IC=+0.294 (n=1666)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 95.0 (IC base=+0.070)

- **PATRÓN** `ibs_20min` < `0.582` → IC=+0.133 (n=4404)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.582 (IC base=+0.054)

- **PATRÓN** `dist_vwap_pct` > `0.7799` → IC=+0.248 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7799 (IC base=+0.054)

- **PATRÓN** `dist_vwap_pct` < `0.2283` → IC=+0.225 (n=1070)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2283 (IC base=+0.054)

- **PATRÓN** `volumen_regimen` < `0.7142` → IC=+0.232 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7142 (IC base=+0.054)

- **PATRÓN** `volumen_regimen` > `1.2263` → IC=+0.250 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2263 (IC base=+0.054)

- **PATRÓN** `volumen_pendiente_norm` > `0.2584` → IC=+0.348 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2584 (IC base=+0.054)

- **PATRÓN** `volumen_spike_ratio` > `2.8473` → IC=+0.279 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8473 (IC base=+0.054)

- **PATRÓN** `ballena_activa_n` < `66.0` → IC=+0.272 (n=1139)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 66.0 (IC base=+0.054)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2977` → IC=-0.149 (n=377)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2977
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=768)

- **FILTRO** `sigma_ewma_delta_pct` > `2.434` → IC=-0.160 (n=327)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.434
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=721)

- **PATRÓN** `ibs_20min` > `0.825` → IC=+0.213 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.825 (IC base=+0.021)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.053` → IC=+0.124 (n=429)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` > 2.053 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` > `0.2236` → IC=+0.344 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2236 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` < `1.9384` → IC=+0.221 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9384 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` > `2.7084` → IC=+0.268 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7084 (IC base=+0.021)

- **PATRÓN** `ballena_activa_n` < `77.0` → IC=+0.310 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 77.0 (IC base=+0.021)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` > `0.8608` → IC=-0.164 (n=382)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8608
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=1150)

- **PATRÓN** `ballena_activa_n` < `288.0` → IC=+0.145 (n=139)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 288.0 (IC base=-0.015)

- **PATRÓN** `dist_vwap_pct` < `0.1132` → IC=+0.167 (n=166)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1132 (IC base=-0.027)

- **PATRÓN** `volumen_regimen` < `0.5824` → IC=+0.221 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5824 (IC base=-0.027)

- **PATRÓN** `volumen_regimen` > `1.1078` → IC=+0.156 (n=59)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 1.1078 (IC base=-0.027)

- **PATRÓN** `volumen_pendiente_norm` > `0.2162` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2162 (IC base=-0.027)

- **PATRÓN** `volumen_spike_ratio` < `2.0367` → IC=+0.206 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0367 (IC base=-0.027)

- **PATRÓN** `volumen_spike_ratio` > `1.3908` → IC=+0.157 (n=132)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.3908 (IC base=-0.027)

- **PATRÓN** `ballena_activa_n` < `263.0` → IC=+0.181 (n=45)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 263.0 (IC base=-0.027)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.281 (n=331)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0084 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.1252` → IC=+0.222 (n=322)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1252 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.252 (n=272)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.283 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.319` → IC=+0.290 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.319 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` < `0.1087` → IC=+0.235 (n=598)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1087 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `1.727` → IC=+0.225 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.727 (IC base=+0.220)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.248 (n=748)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.220)

- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.331 (n=459)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0062 (IC base=+0.312)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.336 (n=345)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.312)

- **PATRÓN** `ibs_20min` < `0.3296` → IC=+0.326 (n=514)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3296 (IC base=+0.312)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.688` → IC=+0.344 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.688 (IC base=+0.312)

- **PATRÓN** `volumen_pendiente_norm` > `0.3587` → IC=+0.359 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3587 (IC base=+0.312)

- **PATRÓN** `volumen_spike_ratio` < `3.5056` → IC=+0.314 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.5056 (IC base=+0.312)

- **PATRÓN** `volumen_spike_ratio` > `2.3984` → IC=+0.323 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3984 (IC base=+0.312)

- **PATRÓN** `libro_liquidez` > `1841.9597` → IC=+0.328 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1841.9597 (IC base=+0.312)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.309 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 29.0 (IC base=+0.312)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.154 (n=229)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=504)

- **FILTRO** `ibs_20min` < `0.7743` → IC=-0.135 (n=483)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7743
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=250)

- **FILTRO** `ibs_20min` > `0.7357` → IC=-0.149 (n=414)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7357
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=804)

- **FILTRO** `dist_vwap_pct` < `0.0964` → IC=-0.136 (n=53)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0964
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=21)

- **FILTRO** `volumen_regimen` > `0.8624` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8624
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=49)

- **FILTRO** `volumen_regimen` < `0.6828` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.6828
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=50)

- **FILTRO** `volumen_pendiente_norm` < `0.1167` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.1167
  - _Potencial_: sin este filtro IC_bueno=+0.214 (n=5)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.131 (n=82)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=1136)

- **PATRÓN** `dist_vwap_pct` > `1.7185` → IC=+0.346 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.7185 (IC base=-0.059)

- **PATRÓN** `volumen_regimen` < `0.9592` → IC=+0.148 (n=89)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.9592 (IC base=-0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.0707` → IC=+0.278 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0707 (IC base=-0.059)

- **PATRÓN** `volumen_spike_ratio` < `2.0608` → IC=+0.254 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0608 (IC base=-0.059)

- **PATRÓN** `ballena_activa_n` < `102.0` → IC=+0.267 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 102.0 (IC base=-0.059)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.8085` → IC=-0.141 (n=647)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8085
  - _Potencial_: sin este filtro IC_bueno=+0.286 (n=334)

- **FILTRO** `ibs_20min` > `0.75` → IC=-0.224 (n=281)

  - _Acción_: SKIP cuando `ibs_20min` > 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=848)

- **FILTRO** `sigma_ewma_delta_pct` > `4.705` → IC=-0.150 (n=287)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.705
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=842)

- **PATRÓN** `ibs_20min` > `0.9219` → IC=+0.331 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9219 (IC base=+0.005)

- **PATRÓN** `dist_vwap_pct` > `0.5651` → IC=+0.324 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5651 (IC base=+0.005)

- **PATRÓN** `volumen_regimen` < `0.8696` → IC=+0.245 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8696 (IC base=+0.005)

- **PATRÓN** `volumen_regimen` > `1.1627` → IC=+0.296 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1627 (IC base=+0.005)

- **PATRÓN** `volumen_pendiente_norm` < `0.1169` → IC=+0.253 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1169 (IC base=+0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2306` → IC=+0.263 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2306 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` < `1.4502` → IC=+0.298 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4502 (IC base=+0.005)

- **PATRÓN** `ballena_activa_n` < `57.0` → IC=+0.306 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 57.0 (IC base=+0.005)

- **PATRÓN** `volumen_regimen` < `0.735` → IC=+0.153 (n=47)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.735 (IC base=-0.028)

- **PATRÓN** `volumen_pendiente_norm` > `0.2973` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2973 (IC base=-0.028)

- **PATRÓN** `volumen_spike_ratio` > `2.3913` → IC=+0.158 (n=36)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.3913 (IC base=-0.028)

- **PATRÓN** `ballena_activa_n` < `61.0` → IC=+0.194 (n=70)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 61.0 (IC base=-0.028)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.332 (n=493)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=+0.249)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.256 (n=351)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.249)

- **PATRÓN** `ibs_20min` > `0.8915` → IC=+0.322 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8915 (IC base=+0.249)

- **PATRÓN** `dist_vwap_pct` > `0.1621` → IC=+0.312 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1621 (IC base=+0.249)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.192` → IC=+0.288 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.192 (IC base=+0.249)

- **PATRÓN** `volumen_regimen` > `0.8448` → IC=+0.290 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8448 (IC base=+0.249)

- **PATRÓN** `volumen_pendiente_norm` > `0.2417` → IC=+0.293 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2417 (IC base=+0.249)

- **PATRÓN** `volumen_spike_ratio` < `2.5739` → IC=+0.256 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5739 (IC base=+0.249)

- **PATRÓN** `volumen_spike_ratio` > `1.844` → IC=+0.254 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.844 (IC base=+0.249)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.254 (n=862)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.249)

- **PATRÓN** `libro_liquidez` > `2467.4755` → IC=+0.253 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2467.4755 (IC base=+0.249)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.280 (n=266)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.279)

- **PATRÓN** `sigma_h` > `0.024` → IC=+0.301 (n=265)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.024 (IC base=+0.279)

- **PATRÓN** `drift_60min` |x|≤ `0.3199` → IC=+0.281 (n=531)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3199 (IC base=+0.279)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.292 (n=387)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.279)

- **PATRÓN** `ibs_20min` < `0.375` → IC=+0.318 (n=796)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.375 (IC base=+0.279)

- **PATRÓN** `dist_vwap_pct` > `0.5418` → IC=+0.280 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5418 (IC base=+0.279)

- **PATRÓN** `dist_vwap_pct` < `0.212` → IC=+0.282 (n=720)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.212 (IC base=+0.279)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.402` → IC=+0.312 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.402 (IC base=+0.279)

- **PATRÓN** `volumen_regimen` < `0.7178` → IC=+0.284 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7178 (IC base=+0.279)

- **PATRÓN** `volumen_regimen` > `1.2686` → IC=+0.305 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2686 (IC base=+0.279)

- **PATRÓN** `volumen_pendiente_norm` > `0.2435` → IC=+0.383 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2435 (IC base=+0.279)

- **PATRÓN** `volumen_spike_ratio` < `1.4369` → IC=+0.269 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4369 (IC base=+0.279)

- **PATRÓN** `volumen_spike_ratio` > `2.1971` → IC=+0.298 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1971 (IC base=+0.279)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.208 (n=1281)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0106 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.3423` → IC=+0.169 (n=3375)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.3423 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.168 (n=3846)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 6.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.283 (n=1754)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.161)

- **PATRÓN** `dist_vwap_pct` > `0.7907` → IC=+0.237 (n=846)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7907 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.699` → IC=+0.233 (n=1557)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.699 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` > `0.6285` → IC=+0.164 (n=2595)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.6285 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` > `0.1057` → IC=+0.183 (n=1432)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.1057 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` < `2.324` → IC=+0.162 (n=3141)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.324 (IC base=+0.161)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.165 (n=3918)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.03 (IC base=+0.161)

- **PATRÓN** `libro_liquidez` > `3936.5622` → IC=+0.177 (n=1278)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 3936.5622 (IC base=+0.161)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.178 (n=2750)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 143.0 (IC base=+0.161)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.190 (n=3148)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0083 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.0794` → IC=+0.214 (n=1192)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0794 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.197 (n=1748)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 15.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.188 (n=1640)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 7.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` < `0.4375` → IC=+0.232 (n=3576)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4375 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` < `0.2293` → IC=+0.176 (n=2699)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.2293 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.981` → IC=+0.219 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.981 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.1748` → IC=+0.170 (n=2702)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.1748 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` > `0.6226` → IC=+0.163 (n=2702)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6226 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2951` → IC=+0.256 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2951 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` < `1.5745` → IC=+0.174 (n=1297)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.5745 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6579` → IC=+0.202 (n=983)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6579 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `157.0` → IC=+0.182 (n=2536)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 157.0 (IC base=+0.181)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.179 (n=285)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0057 (IC base=+0.171)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.202 (n=293)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.2854` → IC=+0.194 (n=644)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.2854 (IC base=+0.171)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.228 (n=244)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.291 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.705` → IC=+0.273 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.705 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.2273` → IC=+0.252 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2273 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `2.6425` → IC=+0.161 (n=561)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.6425 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `1.4557` → IC=+0.164 (n=561)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.4557 (IC base=+0.171)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.203 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.171)

- **PATRÓN** `ballena_activa_n` < `66.0` → IC=+0.184 (n=372)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 66.0 (IC base=+0.171)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.265 (n=360)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.1585` → IC=+0.308 (n=269)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1585 (IC base=+0.242)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.268 (n=424)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.242)

- **PATRÓN** `ibs_20min` < `0.2712` → IC=+0.268 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2712 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.687` → IC=+0.252 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.687 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` < `0.0647` → IC=+0.229 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0647 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` > `0.2471` → IC=+0.297 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2471 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` < `1.9402` → IC=+0.239 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9402 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` > `2.791` → IC=+0.246 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.791 (IC base=+0.242)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.279 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.242)

- **PATRÓN** `libro_liquidez` > `1698.3448` → IC=+0.282 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1698.3448 (IC base=+0.242)

- **PATRÓN** `ballena_activa_n` < `63.0` → IC=+0.241 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 63.0 (IC base=+0.242)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.224 (n=190)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.166)

- **PATRÓN** `drift_60min` |x|≤ `0.4155` → IC=+0.172 (n=568)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.4155 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.194 (n=580)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 6.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` > `0.4793` → IC=+0.208 (n=567)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4793 (IC base=+0.166)

- **PATRÓN** `dist_vwap_pct` > `0.2046` → IC=+0.223 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2046 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.906` → IC=+0.227 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.906 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.405` → IC=+0.166 (n=540)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 7.405 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` < `0.6383` → IC=+0.182 (n=190)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6383 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` > `1.0731` → IC=+0.181 (n=258)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 1.0731 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` > `0.2332` → IC=+0.194 (n=119)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2332 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` < `1.4857` → IC=+0.203 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4857 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` > `2.4674` → IC=+0.165 (n=180)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.4674 (IC base=+0.166)

- **PATRÓN** `libro_liquidez` > `11309.5324` → IC=+0.190 (n=507)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 11309.5324 (IC base=+0.166)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.185 (n=658)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0061 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.2979` → IC=+0.176 (n=658)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2979 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.172 (n=610)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 7.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` < `0.4807` → IC=+0.194 (n=658)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.4807 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` < `0.2004` → IC=+0.177 (n=660)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.2004 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.118` → IC=+0.236 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.118 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` < `0.6967` → IC=+0.223 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6967 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` > `0.1584` → IC=+0.224 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1584 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `2.4411` → IC=+0.169 (n=550)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 2.4411 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` > `1.3961` → IC=+0.163 (n=550)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.3961 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `15532.7795` → IC=+0.162 (n=220)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 15532.7795 (IC base=+0.156)

- **PATRÓN** `ballena_activa_n` < `239.0` → IC=+0.156 (n=158)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 239.0 (IC base=+0.156)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.221 (n=199)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0095 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.2845` → IC=+0.184 (n=527)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.2845 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.183 (n=203)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 17.0 (IC base=+0.169)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.189 (n=207)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 5.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.546` → IC=+0.314 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.546 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.1304` → IC=+0.171 (n=217)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1304 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `2.4356` → IC=+0.160 (n=357)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.4356 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `1.7062` → IC=+0.161 (n=535)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.7062 (IC base=+0.169)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.193 (n=603)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.04 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.209 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.169)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.259 (n=470)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.2236` → IC=+0.260 (n=314)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2236 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.257 (n=323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.239 (n=209)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.3724` → IC=+0.273 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3724 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.563` → IC=+0.328 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.563 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.3671` → IC=+0.292 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3671 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `1.9277` → IC=+0.239 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9277 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `3.139` → IC=+0.229 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.139 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `1856.0032` → IC=+0.242 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1856.0032 (IC base=+0.239)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.208 (n=382)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.158)

- **PATRÓN** `drift_60min` |x|≤ `0.1299` → IC=+0.177 (n=252)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.1299 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.174 (n=584)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 6.0 (IC base=+0.158)

- **PATRÓN** `ibs_20min` > `0.4382` → IC=+0.202 (n=572)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4382 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` > `0.1514` → IC=+0.192 (n=400)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1514 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.201` → IC=+0.264 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.201 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` > `1.2091` → IC=+0.225 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2091 (IC base=+0.158)

- **PATRÓN** `volumen_pendiente_norm` > `0.2472` → IC=+0.214 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2472 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` < `1.4303` → IC=+0.158 (n=185)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.4303 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` > `2.6255` → IC=+0.206 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6255 (IC base=+0.158)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.159 (n=638)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.158)

- **PATRÓN** `libro_liquidez` > `8750.1763` → IC=+0.192 (n=381)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 8750.1763 (IC base=+0.158)

- **PATRÓN** `ballena_activa_n` < `135.0` → IC=+0.145 (n=342)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 135.0 (IC base=+0.158)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.216 (n=216)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.3806` → IC=+0.153 (n=644)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.3806 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.171 (n=220)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 18.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.144 (n=293)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 7.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.3934` → IC=+0.201 (n=567)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3934 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.3493` → IC=+0.144 (n=706)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.3493 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.371` → IC=+0.203 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.371 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `1.1618` → IC=+0.139 (n=644)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.1618 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` > `0.613` → IC=+0.139 (n=644)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 0.613 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.1044` → IC=+0.177 (n=218)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1044 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `1.8542` → IC=+0.149 (n=357)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.8542 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `2.5258` → IC=+0.158 (n=179)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.5258 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `5025.7991` → IC=+0.145 (n=429)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 5025.7991 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `181.0` → IC=+0.127 (n=405)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 181.0 (IC base=+0.133)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.154 (n=646)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0065 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.131 (n=755)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.114)

- **PATRÓN** `ibs_20min` > `0.5385` → IC=+0.194 (n=720)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.5385 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` > `1.162` → IC=+0.253 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.162 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.303` → IC=+0.270 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.303 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` > `0.7086` → IC=+0.130 (n=643)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` > 0.7086 (IC base=+0.114)

- **PATRÓN** `volumen_pendiente_norm` < `0.1682` → IC=+0.134 (n=717)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` < 0.1682 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` < `1.4402` → IC=+0.148 (n=228)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.4402 (IC base=+0.114)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.121 (n=724)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `3187.8673` → IC=+0.219 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3187.8673 (IC base=+0.114)

- **PATRÓN** `ballena_activa_n` < `57.0` → IC=+0.147 (n=528)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 57.0 (IC base=+0.114)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.150 (n=298)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0094 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.1005` → IC=+0.147 (n=219)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.1005 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.187 (n=308)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 15.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.4642` → IC=+0.228 (n=657)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4642 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.2523` → IC=+0.151 (n=619)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.2523 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.218` → IC=+0.177 (n=258)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 3.218 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `1.1973` → IC=+0.152 (n=657)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1973 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` > `0.8568` → IC=+0.150 (n=438)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.8568 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.2716` → IC=+0.226 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2716 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `2.1049` → IC=+0.203 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1049 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `2186.0307` → IC=+0.161 (n=438)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2186.0307 (IC base=+0.135)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0177` → IC=+0.216 (n=491)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0177 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.1721` → IC=+0.209 (n=324)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1721 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=769)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `0.8873` → IC=+0.271 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8873 (IC base=+0.190)

- **PATRÓN** `dist_vwap_pct` > `0.167` → IC=+0.224 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.167 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.223` → IC=+0.238 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.223 (IC base=+0.190)

- **PATRÓN** `volumen_regimen` > `0.6857` → IC=+0.208 (n=658)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6857 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.2396` → IC=+0.262 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2396 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` < `2.5276` → IC=+0.208 (n=697)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5276 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.192 (n=846)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.02 (IC base=+0.190)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.277 (n=249)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.6471` → IC=+0.224 (n=745)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6471 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.219 (n=340)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.213)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.251 (n=343)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` < `0.41` → IC=+0.258 (n=745)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.41 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` < `0.5151` → IC=+0.220 (n=822)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5151 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.582` → IC=+0.260 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.582 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` > `0.6252` → IC=+0.231 (n=744)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6252 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.2818` → IC=+0.328 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2818 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `2.658` → IC=+0.228 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.658 (IC base=+0.213)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.172 (n=269)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0097 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.167 (n=766)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 8.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.4545` → IC=+0.168 (n=807)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.4545 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.9501` → IC=+0.223 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9501 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.14` → IC=+0.184 (n=204)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 8.14 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.8709` → IC=+0.156 (n=434)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.8709 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `1.1694` → IC=+0.153 (n=217)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 1.1694 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.18` → IC=+0.168 (n=224)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.18 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.2724` → IC=+0.146 (n=662)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.2724 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.8529` → IC=+0.142 (n=501)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.8529 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=603)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `7621.927` → IC=+0.179 (n=269)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 7621.927 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.185 (n=195)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 12.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.31` → IC=+0.132 (n=547)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.31 (IC base=+0.069)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.150 (n=298)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 20.0 (IC base=+0.069)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` > `0.0036` → IC=+0.144 (n=116)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.0036 (IC base=+0.100)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.174 (n=139)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 10.0 (IC base=+0.100)

- **PATRÓN** `ibs_20min` > `0.6242` → IC=+0.161 (n=116)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.6242 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `0.2674` → IC=+0.208 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2674 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.537` → IC=+0.177 (n=63)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 3.537 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` < `0.573` → IC=+0.174 (n=44)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.573 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `11099.5571` → IC=+0.161 (n=116)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 11099.5571 (IC base=+0.100)

- **PATRÓN** `ballena_activa_n` < `165.0` → IC=+0.167 (n=34)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 165.0 (IC base=+0.100)

- **PATRÓN** `ibs_20min` < `0.6123` → IC=+0.147 (n=239)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.6123 (IC base=+0.063)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.02` → IC=+0.167 (n=52)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.02 (IC base=+0.063)

- **PATRÓN** `volumen_pendiente_norm` > `0.1656` → IC=+0.218 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1656 (IC base=+0.063)

- **PATRÓN** `ballena_activa_n` < `146.0` → IC=+0.163 (n=81)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 146.0 (IC base=+0.063)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.266 (n=135)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.257)

- **PATRÓN** `sigma_h` > `0.0074` → IC=+0.314 (n=68)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0074 (IC base=+0.257)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.297 (n=210)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.257)

- **PATRÓN** `ibs_20min` > `0.9308` → IC=+0.319 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9308 (IC base=+0.257)

- **PATRÓN** `dist_vwap_pct` > `0.1633` → IC=+0.290 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1633 (IC base=+0.257)

- **PATRÓN** `dist_vwap_pct` < `0.7834` → IC=+0.264 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.7834 (IC base=+0.257)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.316` → IC=+0.319 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.316 (IC base=+0.257)

- **PATRÓN** `volumen_regimen` < `0.8389` → IC=+0.274 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8389 (IC base=+0.257)

- **PATRÓN** `volumen_regimen` > `1.1605` → IC=+0.314 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1605 (IC base=+0.257)

- **PATRÓN** `volumen_pendiente_norm` > `0.0976` → IC=+0.347 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0976 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` < `1.374` → IC=+0.294 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.374 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` > `2.0363` → IC=+0.326 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.0363 (IC base=+0.257)

- **PATRÓN** `drift_60min` |x|≤ `0.1334` → IC=+0.147 (n=66)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.1334 (IC base=+0.043)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` < `0.5758` → IC=-0.177 (n=60)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5758
  - _Potencial_: sin este filtro IC_bueno=+0.101 (n=181)

- **FILTRO** `ibs_20min` > `0.4394` → IC=-0.222 (n=52)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4394
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=102)

- **FILTRO** `dist_vwap_pct` > `0.2318` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2318
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=133)

- **FILTRO** `volumen_pendiente_norm` > `0.2195` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.2195
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=115)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.170 (n=92)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 14.0 (IC base=+0.031)

- **PATRÓN** `ibs_20min` > `0.8462` → IC=+0.177 (n=122)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.8462 (IC base=+0.031)

- **PATRÓN** `dist_vwap_pct` > `0.6872` → IC=+0.214 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6872 (IC base=+0.031)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.196` → IC=+0.145 (n=60)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 7.196 (IC base=+0.031)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 25.0 (IC base=-0.045)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0223` → IC=+0.152 (n=139)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0223 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.3042` → IC=+0.161 (n=122)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.3042 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.180 (n=48)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 16.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.151 (n=61)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 7.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.4` → IC=+0.167 (n=139)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.4 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.1962` → IC=+0.172 (n=56)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1962 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` < `0.4345` → IC=+0.143 (n=155)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.4345 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.301` → IC=+0.175 (n=118)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` < 3.301 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `0.839` → IC=+0.170 (n=92)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 0.839 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` < `0.2201` → IC=+0.172 (n=120)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` < 0.2201 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `1.9259` → IC=+0.196 (n=77)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.9259 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.4996` → IC=+0.150 (n=115)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.4996 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.188 (n=94)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.228 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=+0.140)

- **PATRÓN** `sigma_h` > `0.0147` → IC=+0.204 (n=96)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0147 (IC base=+0.113)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.124 (n=99)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 10.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.0588` → IC=+0.128 (n=49)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` < 0.0588 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` > `1.0263` → IC=+0.350 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0263 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.481` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.481 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` > `0.6197` → IC=+0.137 (n=144)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 0.6197 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.2474` → IC=+0.242 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2474 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` > `2.8779` → IC=+0.174 (n=44)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.8779 (IC base=+0.113)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.151 (n=107)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 15.0 (IC base=+0.113)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0087` → IC=+0.200 (n=2088)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0087 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.171 (n=4607)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 6.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.300 (n=1576)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `0.2346` → IC=+0.200 (n=1723)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2346 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.639` → IC=+0.221 (n=2584)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.639 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` < `0.8847` → IC=+0.158 (n=2122)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8847 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` > `1.237` → IC=+0.154 (n=1061)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 1.237 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.1676` → IC=+0.188 (n=1246)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.1676 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` > `1.8748` → IC=+0.172 (n=2847)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 1.8748 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.168 (n=4338)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.02 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `3847.9652` → IC=+0.187 (n=1533)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 3847.9652 (IC base=+0.164)

- **PATRÓN** `ballena_activa_n` < `61.0` → IC=+0.210 (n=2164)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 61.0 (IC base=+0.164)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.197 (n=4253)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0109 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.4821` → IC=+0.198 (n=4252)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.4821 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.207 (n=1906)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` < `0.5605` → IC=+0.242 (n=4252)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5605 (IC base=+0.189)

- **PATRÓN** `dist_vwap_pct` < `0.4479` → IC=+0.175 (n=2994)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.4479 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.672` → IC=+0.214 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.672 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.585` → IC=+0.190 (n=4180)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 3.585 (IC base=+0.189)

- **PATRÓN** `volumen_regimen` < `0.6228` → IC=+0.175 (n=1011)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6228 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.237` → IC=+0.247 (n=699)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.237 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `2.3075` → IC=+0.203 (n=1607)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3075 (IC base=+0.189)

- **PATRÓN** `ballena_activa_n` < `141.0` → IC=+0.184 (n=3124)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 141.0 (IC base=+0.189)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.185 (n=255)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0053 (IC base=+0.184)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.235 (n=345)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.217 (n=284)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.184)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.326 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.073` → IC=+0.297 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.073 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` > `0.2233` → IC=+0.261 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2233 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` < `1.4804` → IC=+0.183 (n=225)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.4804 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` > `2.3086` → IC=+0.177 (n=305)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 2.3086 (IC base=+0.184)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.233 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.184)

- **PATRÓN** `ballena_activa_n` < `76.0` → IC=+0.233 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 76.0 (IC base=+0.184)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.275 (n=491)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.271)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.279 (n=558)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.271)

- **PATRÓN** `drift_60min` |x|≤ `0.1755` → IC=+0.294 (n=372)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1755 (IC base=+0.271)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.278 (n=508)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.271)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.280 (n=562)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.271)

- **PATRÓN** `ibs_20min` < `0.4058` → IC=+0.305 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4058 (IC base=+0.271)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.482` → IC=+0.284 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.482 (IC base=+0.271)

- **PATRÓN** `volumen_pendiente_norm` > `0.1771` → IC=+0.312 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1771 (IC base=+0.271)

- **PATRÓN** `volumen_spike_ratio` > `1.517` → IC=+0.289 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.517 (IC base=+0.271)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.276 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.271)

- **PATRÓN** `libro_liquidez` > `1459.068` → IC=+0.282 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1459.068 (IC base=+0.271)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.272 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 69.0 (IC base=+0.271)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.173 (n=252)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.003 (IC base=+0.159)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.160 (n=251)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0069 (IC base=+0.159)

- **PATRÓN** `drift_60min` |x|≤ `0.097` → IC=+0.169 (n=252)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.097 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.175 (n=753)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 6.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` > `0.3271` → IC=+0.205 (n=753)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3271 (IC base=+0.159)

- **PATRÓN** `dist_vwap_pct` > `0.2359` → IC=+0.221 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2359 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.721` → IC=+0.177 (n=184)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 9.721 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.417` → IC=+0.172 (n=657)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` < 4.417 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` < `0.7179` → IC=+0.177 (n=332)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.7179 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` > `1.1034` → IC=+0.166 (n=342)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 1.1034 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` < `0.0723` → IC=+0.173 (n=632)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` < 0.0723 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` > `0.147` → IC=+0.184 (n=207)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.147 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` < `2.413` → IC=+0.177 (n=704)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 2.413 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` > `1.7258` → IC=+0.179 (n=469)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.7258 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `10653.1142` → IC=+0.184 (n=673)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 10653.1142 (IC base=+0.159)

- **PATRÓN** `ballena_activa_n` < `510.0` → IC=+0.170 (n=629)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 510.0 (IC base=+0.159)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.172 (n=693)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0062 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.2721` → IC=+0.181 (n=609)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.2721 (IC base=+0.163)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.169 (n=717)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 18.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` < `0.6147` → IC=+0.200 (n=692)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6147 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` < `0.1465` → IC=+0.181 (n=594)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.1465 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.763` → IC=+0.206 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.763 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` < `0.6181` → IC=+0.238 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6181 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.1411` → IC=+0.232 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1411 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` < `1.395` → IC=+0.192 (n=199)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.395 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` > `2.0753` → IC=+0.180 (n=270)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 2.0753 (IC base=+0.163)

- **PATRÓN** `ballena_activa_n` < `289.0` → IC=+0.184 (n=166)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 289.0 (IC base=+0.163)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.224 (n=440)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0073 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.237 (n=314)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` > `0.6815` → IC=+0.252 (n=590)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6815 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.628` → IC=+0.335 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.628 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` < `0.2205` → IC=+0.209 (n=600)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2205 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` < `1.899` → IC=+0.201 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.899 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` > `2.4711` → IC=+0.205 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4711 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.232 (n=669)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `1452.72` → IC=+0.207 (n=660)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1452.72 (IC base=+0.203)

- **PATRÓN** `ballena_activa_n` < `63.0` → IC=+0.262 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 63.0 (IC base=+0.203)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.291 (n=223)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.244)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.251 (n=303)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0089 (IC base=+0.244)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.272 (n=309)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.244)

- **PATRÓN** `ibs_20min` < `0.4016` → IC=+0.296 (n=587)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4016 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.453` → IC=+0.301 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.453 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` > `0.3592` → IC=+0.280 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3592 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` < `3.0572` → IC=+0.248 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.0572 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` > `2.3399` → IC=+0.226 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3399 (IC base=+0.244)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.223 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 54.0 (IC base=+0.244)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.160 (n=668)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0071 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.1439` → IC=+0.146 (n=334)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.1439 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.160 (n=686)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 8.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `0.74` → IC=+0.240 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.74 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.377` → IC=+0.191 (n=309)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.377 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.362` → IC=+0.172 (n=346)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 4.362 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `0.9018` → IC=+0.172 (n=507)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.9018 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` > `1.2078` → IC=+0.159 (n=253)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 1.2078 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.2765` → IC=+0.225 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2765 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `2.1479` → IC=+0.202 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1479 (IC base=+0.145)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.146 (n=826)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `9488.8794` → IC=+0.243 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9488.8794 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.157 (n=534)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0072 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.4487` → IC=+0.155 (n=607)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.4487 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.141 (n=232)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.175 (n=269)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 7.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.6744` → IC=+0.180 (n=607)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.6744 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` > `0.219` → IC=+0.133 (n=257)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 0.219 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.4068` → IC=+0.138 (n=605)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.4068 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.358` → IC=+0.234 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.358 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.291` → IC=+0.135 (n=574)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 4.291 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.8251` → IC=+0.136 (n=405)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8251 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` > `1.1408` → IC=+0.167 (n=202)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 1.1408 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.2797` → IC=+0.266 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2797 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.4586` → IC=+0.150 (n=546)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.4586 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `11624.4939` → IC=+0.206 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11624.4939 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `192.0` → IC=+0.152 (n=466)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 192.0 (IC base=+0.133)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.148 (n=530)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0085 (IC base=+0.094)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.136 (n=539)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 12.0 (IC base=+0.094)

- **PATRÓN** `ibs_20min` > `0.48` → IC=+0.181 (n=794)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.48 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` > `1.1408` → IC=+0.197 (n=153)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 1.1408 (IC base=+0.094)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.403` → IC=+0.220 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.403 (IC base=+0.094)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.122 (n=551)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.01 (IC base=+0.094)

- **PATRÓN** `libro_liquidez` > `2942.126` → IC=+0.272 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2942.126 (IC base=+0.094)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.143 (n=502)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 54.0 (IC base=+0.094)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.171 (n=256)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0059 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.132` → IC=+0.174 (n=256)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.132 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.143 (n=376)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 15.0 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.142 (n=291)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 6.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.6` → IC=+0.200 (n=772)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` < `0.5176` → IC=+0.138 (n=735)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.5176 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.195` → IC=+0.137 (n=758)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 3.195 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `0.8761` → IC=+0.138 (n=512)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.8761 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.0725` → IC=+0.163 (n=256)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.0725 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.454` → IC=+0.144 (n=206)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.454 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` > `2.1867` → IC=+0.145 (n=280)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 2.1867 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2649.2833` → IC=+0.169 (n=348)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2649.2833 (IC base=+0.118)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.028` → IC=+0.256 (n=293)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.028 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.210 (n=919)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.300 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` > `0.1688` → IC=+0.251 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1688 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.141` → IC=+0.242 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.141 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` > `1.2338` → IC=+0.229 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2338 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` > `0.2361` → IC=+0.240 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2361 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` > `1.8278` → IC=+0.205 (n=551)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8278 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.207 (n=1004)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.198)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.283 (n=321)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.214)

- **PATRÓN** `sigma_h` > `0.0254` → IC=+0.225 (n=321)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0254 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.5323` → IC=+0.218 (n=847)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5323 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.215 (n=471)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.220 (n=1012)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` < `0.4977` → IC=+0.267 (n=963)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4977 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` < `0.2691` → IC=+0.224 (n=871)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2691 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.288` → IC=+0.281 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.288 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` > `0.7056` → IC=+0.225 (n=861)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7056 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.2836` → IC=+0.303 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2836 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `1.8631` → IC=+0.212 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8631 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.215 (n=1121)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.214)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.191 (n=683)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 34.0 (IC base=+0.214)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.128 (n=1728)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.133 (n=1323)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.01 (IC base=+0.119)

- **PATRÓN** `drift_60min` |x|≤ `0.5491` → IC=+0.129 (n=1502)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.5491 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.168 (n=507)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 18.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `0.921` → IC=+0.190 (n=501)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.921 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.96` → IC=+0.121 (n=1527)

  - _Acción_: Kelly boost +0.60€ cuando `sigma_ewma_delta_pct` < 5.96 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.1747` → IC=+0.150 (n=407)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.1747 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.4612` → IC=+0.147 (n=496)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4612 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` > `1.8963` → IC=+0.140 (n=991)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.8963 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `9005.1548` → IC=+0.135 (n=681)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 9005.1548 (IC base=+0.119)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.171 (n=436)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0039 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.5065` → IC=+0.145 (n=1308)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.5065 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.151 (n=491)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.152 (n=438)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 4.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` < `0.1994` → IC=+0.150 (n=576)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.1994 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `0.9977` → IC=+0.132 (n=180)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` > 0.9977 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.347` → IC=+0.136 (n=1307)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 6.347 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `1.2316` → IC=+0.135 (n=1276)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.2316 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` < `0.1472` → IC=+0.126 (n=1305)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1472 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.069` → IC=+0.144 (n=622)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.069 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `2.4725` → IC=+0.134 (n=1294)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.4725 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `1.7932` → IC=+0.132 (n=864)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 1.7932 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.128 (n=1728)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `8448.0568` → IC=+0.133 (n=1168)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 8448.0568 (IC base=+0.125)

### GBM_LATE_5M#BTC#5min
- **FILTRO** `sigma_ewma_delta_pct` > `2.471` → IC=-0.250 (n=26)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.471
  - _Potencial_: sin este filtro IC_bueno=+0.145 (n=181)

- **PATRÓN** `hora_utc` > `19.0` → IC=+0.161 (n=54)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 19.0 (IC base=+0.093)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.471` → IC=+0.145 (n=181)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 2.471 (IC base=+0.093)

- **PATRÓN** `volumen_regimen` > `0.7903` → IC=+0.123 (n=104)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` > 0.7903 (IC base=+0.093)

- **PATRÓN** `volumen_spike_ratio` < `1.4115` → IC=+0.167 (n=52)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.4115 (IC base=+0.093)

- **PATRÓN** `volumen_spike_ratio` > `2.2086` → IC=+0.130 (n=71)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.2086 (IC base=+0.093)

- **PATRÓN** `libro_liquidez` > `12645.8095` → IC=+0.145 (n=139)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 12645.8095 (IC base=+0.093)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.170 (n=274)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0035 (IC base=+0.112)

- **PATRÓN** `drift_60min` |x|≤ `0.0856` → IC=+0.141 (n=207)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.0856 (IC base=+0.112)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.157 (n=234)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.112)

- **PATRÓN** `ibs_20min` < `0.1654` → IC=+0.158 (n=273)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.1654 (IC base=+0.112)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.369` → IC=+0.139 (n=619)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 6.369 (IC base=+0.112)

- **PATRÓN** `volumen_regimen` < `0.8709` → IC=+0.149 (n=414)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.8709 (IC base=+0.112)

- **PATRÓN** `volumen_pendiente_norm` > `0.0635` → IC=+0.150 (n=292)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.0635 (IC base=+0.112)

- **PATRÓN** `volumen_spike_ratio` < `1.3995` → IC=+0.144 (n=206)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.3995 (IC base=+0.112)

- **PATRÓN** `libro_liquidez` > `11116.1452` → IC=+0.124 (n=620)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 11116.1452 (IC base=+0.112)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.202 (n=112)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.138)

- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.175 (n=152)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0105 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.4204` → IC=+0.146 (n=295)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.4204 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.254 (n=112)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.9524` → IC=+0.246 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9524 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.252` → IC=+0.216 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.252 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.671` → IC=+0.140 (n=284)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 2.671 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.215` → IC=+0.159 (n=83)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.215 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.6778` → IC=+0.167 (n=112)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.6778 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `2.433` → IC=+0.152 (n=222)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 2.433 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `1886.8848` → IC=+0.144 (n=299)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 1886.8848 (IC base=+0.138)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0089` → IC=+0.149 (n=557)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0089 (IC base=+0.133)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.133 (n=557)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` > 0.0046 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.4756` → IC=+0.145 (n=556)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.4756 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.194 (n=194)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 18.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.135 (n=253)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 6.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` > `0.185` → IC=+0.145 (n=556)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.185 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` > `1.0663` → IC=+0.174 (n=127)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 1.0663 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.4381` → IC=+0.141 (n=525)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.4381 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.914` → IC=+0.145 (n=559)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 6.914 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.7283` → IC=+0.160 (n=245)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.7283 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` < `0.117` → IC=+0.134 (n=514)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` < 0.117 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.1782` → IC=+0.159 (n=165)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.1782 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `1.4471` → IC=+0.176 (n=183)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.4471 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.8053` → IC=+0.138 (n=365)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.8053 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `8379.1781` → IC=+0.142 (n=556)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 8379.1781 (IC base=+0.133)

- **PATRÓN** `sigma_h` < `0.0078` → IC=+0.170 (n=365)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0078 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.4118` → IC=+0.205 (n=364)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4118 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.148 (n=211)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 15.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.155 (n=279)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 10.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.1084` → IC=+0.161 (n=414)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.1084 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.7334` → IC=+0.152 (n=458)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.7334 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.927` → IC=+0.190 (n=69)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 10.927 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `1.2227` → IC=+0.168 (n=414)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.2227 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` > `0.733` → IC=+0.148 (n=370)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 0.733 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` < `0.1472` → IC=+0.150 (n=421)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` < 0.1472 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.0698` → IC=+0.163 (n=182)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.0698 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `2.1713` → IC=+0.169 (n=357)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 2.1713 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `1.5315` → IC=+0.168 (n=362)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.5315 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `8201.961` → IC=+0.164 (n=414)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 8201.961 (IC base=+0.146)

### GBM_LATE_5M#SOL#5min
- **FILTRO** `ibs_20min` < `0.4237` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `ibs_20min` < 0.4237
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=75)

- **FILTRO** `dist_vwap_pct` < `0.7269` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.7269
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=28)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=+0.008)

### GBM_LATE_60M
- **FILTRO** `sigma_h` > `0.0105` → IC=-0.290 (n=60)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0105
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=183)

- **FILTRO** `hora_utc` > `9.0` → IC=-0.215 (n=114)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=129)

- **FILTRO** `dist_vwap_pct` > `0.1153` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1153
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=84)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.203 (n=227)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.188 (n=126)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 18.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` > `0.6544` → IC=+0.241 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6544 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` > `0.388` → IC=+0.233 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.388 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` < `0.2198` → IC=+0.162 (n=190)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.2198 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.907` → IC=+0.290 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.907 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `0.6319` → IC=+0.179 (n=110)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.6319 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` > `1.0983` → IC=+0.182 (n=83)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.0983 (IC base=+0.111)

- **PATRÓN** `volumen_pendiente_norm` < `0.0797` → IC=+0.219 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0797 (IC base=+0.111)

- **PATRÓN** `volumen_pendiente_norm` > `0.2799` → IC=+0.339 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2799 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` > `1.7387` → IC=+0.245 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7387 (IC base=+0.111)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.192 (n=209)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.02 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `1307.3076` → IC=+0.180 (n=201)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 1307.3076 (IC base=+0.111)

- **PATRÓN** `ibs_20min` < `0.0875` → IC=+0.210 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0875 (IC base=-0.133)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `sigma_h` > `0.0059` → IC=-0.167 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0059
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=60)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.221 (n=102)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.132 (n=55)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 10.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `0.7937` → IC=+0.233 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7937 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `0.325` → IC=+0.242 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.325 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.206` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.206 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `0.6265` → IC=+0.218 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6265 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` < `0.0635` → IC=+0.244 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0635 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.3553` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3553 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` > `1.9067` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9067 (IC base=+0.119)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0077` → IC=-0.357 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0077
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=59)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.217 (n=90)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.185 (n=52)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.5578` → IC=+0.283 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5578 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.469` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.469 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.1621` → IC=+0.214 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1621 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.568` → IC=+0.370 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.568 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.789` → IC=+0.222 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.789 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` > `1.0173` → IC=+0.203 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0173 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` < `0.1428` → IC=+0.282 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1428 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.2254` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2254 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `2.6009` → IC=+0.405 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6009 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.213 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `2227.7698` → IC=+0.245 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2227.7698 (IC base=+0.146)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.0159` → IC=-0.326 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0159
  - _Potencial_: sin este filtro IC_bueno=-0.142 (n=65)

- **FILTRO** `ibs_20min` > `0.1176` → IC=-0.300 (n=33)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1176
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=12)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.188 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 18.0 (IC base=+0.045)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.167 (n=61)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.6667 (IC base=+0.045)

- **PATRÓN** `dist_vwap_pct` > `0.9778` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9778 (IC base=+0.045)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.902` → IC=+0.250 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.902 (IC base=+0.045)

- **PATRÓN** `volumen_regimen` > `1.083` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` > 1.083 (IC base=+0.045)

- **PATRÓN** `volumen_pendiente_norm` > `0.0894` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0894 (IC base=+0.045)

- **PATRÓN** `volumen_spike_ratio` < `2.308` → IC=+0.188 (n=46)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 2.308 (IC base=+0.045)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.04 (IC base=+0.045)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `14.0` → IC=-0.463 (n=25)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.220 (n=80)

- **FILTRO** `ibs_20min` < `0.6354` → IC=-0.338 (n=78)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6354
  - _Potencial_: sin este filtro IC_bueno=-0.121 (n=27)

- **FILTRO** `volumen_pendiente_norm` < `0.1347` → IC=-0.409 (n=20)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.1347
  - _Potencial_: sin este filtro IC_bueno=-0.318 (n=9)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `volumen_regimen` < `1.3745` → IC=-0.286 (n=26)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.3745
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=14)

- **FILTRO** `sigma_h` < `0.0031` → IC=-0.288 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0031
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=14)

- **FILTRO** `dist_vwap_pct` < `0.1009` → IC=-0.362 (n=27)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1009
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=18)

- **FILTRO** `volumen_regimen` > `1.0011` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.0011
  - _Potencial_: sin este filtro IC_bueno=-0.219 (n=30)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.6354` → IC=-0.462 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6354
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **FILTRO** `volumen_regimen` > `0.6161` → IC=-0.357 (n=26)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.6161
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `sigma_h` < `0.0086` → IC=-0.231 (n=24)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0086
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `volumen_regimen` < `1.0152` → IC=-0.308 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.0152
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=8)

- **FILTRO** `sigma_h` < `0.0084` → IC=-0.326 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0084
  - _Potencial_: sin este filtro IC_bueno=-0.300 (n=8)

- **FILTRO** `dist_vwap_pct` < `0.2118` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.2118
  - _Potencial_: sin este filtro IC_bueno=-0.312 (n=14)

- **FILTRO** `volumen_regimen` < `1.1255` → IC=-0.413 (n=21)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.1255
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` < `0.6331` → IC=-0.237 (n=55)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6331
  - _Potencial_: sin este filtro IC_bueno=+0.131 (n=166)

- **PATRÓN** `ibs_20min` > `0.6331` → IC=+0.131 (n=166)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` > 0.6331 (IC base=+0.038)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.154 (n=79)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 15.0 (IC base=+0.055)

- **PATRÓN** `ibs_20min` < `0.4` → IC=+0.124 (n=163)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` < 0.4 (IC base=+0.055)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.866` → IC=+0.125 (n=70)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` > 5.866 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` > `0.0687` → IC=+0.143 (n=40)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.0687 (IC base=+0.055)

- **PATRÓN** `libro_liquidez` > `3965.7979` → IC=+0.158 (n=74)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 3965.7979 (IC base=+0.055)

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

- **PATRÓN** `sigma_ewma_delta_pct` < `14.501` → IC=+0.129 (n=87)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` < 14.501 (IC base=+0.109)

- **PATRÓN** `volumen_regimen` < `0.5658` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.5658 (IC base=+0.109)

- **PATRÓN** `volumen_spike_ratio` > `1.6024` → IC=+0.138 (n=45)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.6024 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `3671.9914` → IC=+0.139 (n=81)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 3671.9914 (IC base=+0.109)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.203 (n=35)

- **PATRÓN** `sigma_h` < `0.0024` → IC=+0.300 (n=28)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0024 (IC base=+0.079)

- **PATRÓN** `drift_60min` |x|≤ `0.2013` → IC=+0.141 (n=37)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.2013 (IC base=+0.079)

- **PATRÓN** `ibs_20min` > `0.8029` → IC=+0.218 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8029 (IC base=+0.079)

- **PATRÓN** `dist_vwap_pct` < `0.0986` → IC=+0.159 (n=39)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.0986 (IC base=+0.079)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.203 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.079)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.136 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 16.0 (IC base=+0.052)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.12` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.12 (IC base=+0.052)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `dist_vwap_pct` > `0.1937` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1937
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=37)

- **FILTRO** `volumen_regimen` < `0.9878` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9878
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=26)

- **PATRÓN** `ibs_20min` < `0.75` → IC=+0.145 (n=29)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.75 (IC base=+0.084)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.196 (n=44)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.7917 (IC base=+0.084)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.167 (n=46)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.03 (IC base=+0.084)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `libro_liquidez` > `2810.6983` → IC=+0.178 (n=85)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 2810.6983 (IC base=+0.091)

- **PATRÓN** `libro_liquidez` > `2270.1402` → IC=+0.138 (n=230)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 2270.1402 (IC base=+0.107)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `libro_liquidez` > `2810.6983` → IC=+0.178 (n=85)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 2810.6983 (IC base=+0.091)

- **PATRÓN** `libro_liquidez` > `2270.1402` → IC=+0.138 (n=230)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 2270.1402 (IC base=+0.107)

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
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=168)

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
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=1049)

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
  - _Potencial_: sin este filtro IC_bueno=+0.092 (n=47)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_usd_total` < `35093.65` → IC=-0.192 (n=37)

  - _Acción_: SKIP cuando `liq_usd_total` < 35093.65
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=78)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=18)

- **PATRÓN** `liq_usd_total` > `58893.21` → IC=+0.133 (n=58)

  - _Acción_: Kelly boost +0.67€ cuando `liq_usd_total` > 58893.21 (IC base=+0.004)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.144 (n=43)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.495 (IC base=+0.004)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9534` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9534
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=69)

- **FILTRO** `hora_utc` > `14.0` → IC=-0.167 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=76)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=351)

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
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=404)

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
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=61)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.7365` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.7365
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=58)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=61)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=158)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=158)

- **FILTRO** `py_entrada` > `0.555` → IC=-0.167 (n=43)

  - _Acción_: SKIP cuando `py_entrada` > 0.555
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=130)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=117)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=117)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.151 (n=41)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=91)

- **FILTRO** `py_entrada` > `0.54` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `py_entrada` > 0.54
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=29)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=40)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=40)

- **FILTRO** `py_entrada` > `0.55` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=38)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=48)

### MOMENTUM_IBS_15M#BNB#15min
- **FILTRO** `libro_liquidez` < `2179.3878` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `libro_liquidez` < 2179.3878
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=127)

### MOMENTUM_IBS_15M#BTC#15min
- **FILTRO** `ballena_activa_n` > `2.0` → IC=-0.172 (n=65)

  - _Acción_: SKIP cuando `ballena_activa_n` > 2.0
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=276)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=308)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=744)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=810)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.46` → IC=-0.179 (n=1452)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=4365)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.182 (n=1483)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=4588)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.222 (n=221)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=674)

- **FILTRO** `ibs_20min` < `0.7348` → IC=-0.210 (n=222)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7348
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=673)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.164 (n=251)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=808)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.56` → IC=-0.182 (n=234)

  - _Acción_: SKIP cuando `py_entrada` > 0.56
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=733)

- **FILTRO** `ballena_activa_n` > `61.0` → IC=-0.149 (n=240)

  - _Acción_: SKIP cuando `ballena_activa_n` > 61.0
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=727)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=932)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.205 (n=307)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=642)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.215 (n=240)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=786)

- **FILTRO** `ibs_20min` > `0.7151` → IC=-0.190 (n=256)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7151
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=770)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.161 (n=237)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=753)

- **FILTRO** `py_entrada` > `0.56` → IC=-0.165 (n=234)

  - _Acción_: SKIP cuando `py_entrada` > 0.56
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=747)

### MOMENTUM_IBS_15M_BALLENA#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.145 (n=263)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=717)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.160 (n=251)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=765)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.203 (n=224)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=694)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=903)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.201 (n=252)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=770)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `hora_utc` < `15.0` → IC=-0.357 (n=40)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=139)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.306 (n=29)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=150)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=467)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=473)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `19.0` → IC=-0.242 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 19.0
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=12)

- **FILTRO** `py_entrada` > `0.625` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `py_entrada` > 0.625
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=51)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `libro_liquidez` < `15251.0076` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `libro_liquidez` < 15251.0076
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=11)

- **FILTRO** `drift_20min_pct` |x|> `0.1599` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1599
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=83)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `drift_20min_pct` |x|> `0.1583` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1583
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=17)

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
- **FILTRO** `hora_utc` < `6.0` → IC=-0.138 (n=3062)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=11157)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.283 (n=3500)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=10719)

- **FILTRO** `ibs_7min` < `0.7112` → IC=-0.246 (n=3554)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7112
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=10665)

- **FILTRO** `ballena_activa_n` > `19.0` → IC=-0.171 (n=4754)

  - _Acción_: SKIP cuando `ballena_activa_n` > 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=9465)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.220 (n=4404)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=13542)

- **FILTRO** `ibs_7min` > `0.7134` → IC=-0.172 (n=4486)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7134
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=13460)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.154 (n=613)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=1458)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.316 (n=510)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=1561)

- **FILTRO** `ibs_7min` < `0.3` → IC=-0.259 (n=682)

  - _Acción_: SKIP cuando `ibs_7min` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=1389)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.227 (n=515)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=1556)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.231 (n=771)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=2349)

- **FILTRO** `drift_7min_pct` |x|> `0.1143` → IC=-0.126 (n=1058)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1143
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=2062)

- **FILTRO** `ibs_7min` > `0.8358` → IC=-0.190 (n=779)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8358
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=2341)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.136 (n=586)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=2070)

- **FILTRO** `py_entrada` < `0.36` → IC=-0.259 (n=646)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=2010)

- **FILTRO** `ibs_7min` < `0.7699` → IC=-0.194 (n=664)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7699
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=1992)

- **FILTRO** `ballena_activa_n` > `168.0` → IC=-0.178 (n=660)

  - _Acción_: SKIP cuando `ballena_activa_n` > 168.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=1996)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.247 (n=618)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=2051)

- **FILTRO** `ballena_activa_n` > `106.0` → IC=-0.174 (n=906)

  - _Acción_: SKIP cuando `ballena_activa_n` > 106.0
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=1763)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.185 (n=668)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=1436)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.311 (n=671)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=1433)

- **FILTRO** `ibs_7min` < `0.2105` → IC=-0.289 (n=525)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2105
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=1579)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.252 (n=494)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=1610)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.224 (n=747)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=2471)

- **FILTRO** `ibs_7min` > `0.7946` → IC=-0.170 (n=804)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7946
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=2414)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.140 (n=728)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=1682)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.259 (n=587)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=1823)

- **FILTRO** `ibs_7min` < `0.7519` → IC=-0.195 (n=602)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7519
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=1808)

- **FILTRO** `ballena_activa_n` > `26.0` → IC=-0.177 (n=807)

  - _Acción_: SKIP cuando `ballena_activa_n` > 26.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=1603)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.240 (n=789)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=1640)

- **FILTRO** `ibs_7min` > `0.2748` → IC=-0.176 (n=607)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2748
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=1822)

- **FILTRO** `ballena_activa_n` > `34.0` → IC=-0.183 (n=595)

  - _Acción_: SKIP cuando `ballena_activa_n` > 34.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=1834)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.250 (n=643)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=2008)

- **FILTRO** `ibs_7min` < `0.7317` → IC=-0.214 (n=660)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7317
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=1991)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.193 (n=630)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=2021)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.178 (n=802)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=2572)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.124 (n=753)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=1574)

- **FILTRO** `py_entrada` < `0.36` → IC=-0.296 (n=568)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=1759)

- **FILTRO** `ibs_7min` < `0.7333` → IC=-0.246 (n=580)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7333
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=1747)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.233 (n=564)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=1763)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.253 (n=617)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=2519)

- **FILTRO** `ibs_7min` > `0.775` → IC=-0.162 (n=783)

  - _Acción_: SKIP cuando `ibs_7min` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=2353)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=117)

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
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=474)

### ORDER_FLOW_5M
- **FILTRO** `total_vol_5m` > `215.224` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `total_vol_5m` > 215.224
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **PATRÓN** `delta_ratio` |x|> `0.3982` → IC=+0.143 (n=513)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.71€ cuando `delta_ratio` |x|> 0.3982 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.150 (n=304)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 11.0 (IC base=+0.129)

- **PATRÓN** `total_vol_5m` < `453.526` → IC=+0.169 (n=164)

  - _Acción_: Kelly boost +0.84€ cuando `total_vol_5m` < 453.526 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.127 (n=231)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `3300.6877` → IC=+0.147 (n=199)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 3300.6877 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `64.0` → IC=+0.128 (n=358)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 64.0 (IC base=+0.129)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.259 (n=52)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.114)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3984` → IC=+0.144 (n=88)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.72€ cuando `delta_ratio` |x|> 0.3984 (IC base=+0.097)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.127 (n=65)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `2005.686` → IC=+0.130 (n=79)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 2005.686 (IC base=+0.097)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4128` → IC=+0.190 (n=56)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.95€ cuando `delta_ratio` |x|> 0.4128 (IC base=+0.105)

- **PATRÓN** `total_vol_5m` < `498.822` → IC=+0.229 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 498.822 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `7409.4986` → IC=+0.151 (n=84)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 7409.4986 (IC base=+0.105)

- **PATRÓN** `ballena_activa_n` < `136.0` → IC=+0.145 (n=74)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 136.0 (IC base=+0.105)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4038` → IC=+0.222 (n=77)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4038 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.190 (n=27)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 18.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.219 (n=55)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.192)

- **PATRÓN** `total_vol_5m` < `6300.756` → IC=+0.214 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 6300.756 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `2689.7826` → IC=+0.209 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2689.7826 (IC base=+0.192)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.3998` → IC=+0.150 (n=78)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.75€ cuando `delta_ratio` |x|> 0.3998 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.146 (n=80)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 15.0 (IC base=+0.119)

- **PATRÓN** `total_vol_5m` < `370723.7` → IC=+0.146 (n=77)

  - _Acción_: Kelly boost +0.73€ cuando `total_vol_5m` < 370723.7 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.240 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.162 (n=69)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 55.0 (IC base=+0.119)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` > `0.0073` → IC=-0.340 (n=104)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0073
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=106)

- **FILTRO** `T_h` > `39.9947` → IC=-0.339 (n=128)

  - _Acción_: SKIP cuando `T_h` > 39.9947
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=44)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `T_h` > `39.9952` → IC=-0.372 (n=37)

  - _Acción_: SKIP cuando `T_h` > 39.9952
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=19)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.308 (n=24)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=-0.130)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `T_h` < `291.9853` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `T_h` < 291.9853
  - _Potencial_: sin este filtro IC_bueno=+0.192 (n=11)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0097` → IC=-0.196 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0097
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=13)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `T_h` > `135.9558` → IC=-0.157 (n=65)

  - _Acción_: SKIP cuando `T_h` > 135.9558
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=127)

- **FILTRO** `pct_vs_K` |x|> `5.45` → IC=-0.235 (n=47)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 5.45
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=145)

- **FILTRO** `T_h` > `145.7372` → IC=-0.375 (n=38)

  - _Acción_: SKIP cuando `T_h` > 145.7372
  - _Potencial_: sin este filtro IC_bueno=-0.313 (n=121)

- **FILTRO** `pct_vs_K` |x|> `4.4822` → IC=-0.446 (n=54)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.4822
  - _Potencial_: sin este filtro IC_bueno=-0.266 (n=105)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `T_h` > `87.9952` → IC=-0.167 (n=46)

  - _Acción_: SKIP cuando `T_h` > 87.9952
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=25)

- **FILTRO** `pct_vs_K` |x|> `3.6199` → IC=-0.441 (n=15)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.6199
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=56)

- **FILTRO** `sigma_h` < `0.0072` → IC=-0.318 (n=42)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0072
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=14)

- **FILTRO** `T_h` > `144.6172` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `T_h` > 144.6172
  - _Potencial_: sin este filtro IC_bueno=-0.281 (n=39)

- **PATRÓN** `T_h` < `87.9952` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `T_h` < 87.9952 (IC base=-0.048)

- **PATRÓN** `pct_vs_K` |x|≤ `1.2308` → IC=+0.269 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 1.2308 (IC base=-0.048)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `T_h` > `111.9866` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `T_h` > 111.9866
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=34)

- **FILTRO** `sigma_h` < `0.0045` → IC=-0.350 (n=18)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0045
  - _Potencial_: sin este filtro IC_bueno=-0.295 (n=37)

- **FILTRO** `T_h` > `145.5703` → IC=-0.328 (n=27)

  - _Acción_: SKIP cuando `T_h` > 145.5703
  - _Potencial_: sin este filtro IC_bueno=-0.300 (n=28)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.2492` → IC=+0.447 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2492 (IC base=+0.393)

- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.463 (n=25)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0085 (IC base=+0.393)

- **PATRÓN** `T_h` > `0.8774` → IC=+0.443 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8774 (IC base=+0.393)

- **PATRÓN** `dist_50` > `0.4178` → IC=+0.471 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4178 (IC base=+0.393)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.417 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.393)

### STREAK_FADE_15M
- **FILTRO** `hora_utc` < `6.0` → IC=-0.227 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=65)

- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=70)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=127)

- **PATRÓN** `streak_estiramiento` < `0.3698` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.3698 (IC base=+0.026)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=74)

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
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=144)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=164)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=166)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=186)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=272)

- **PATRÓN** `streak_estiramiento` < `0.2913` → IC=+0.180 (n=48)

  - _Acción_: Kelly boost +0.90€ cuando `streak_estiramiento` < 0.2913 (IC base=+0.035)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=541)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=265)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=360)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=1584)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=886)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=894)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` > `0.007` → IC=+0.157 (n=176)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.007 (IC base=+0.124)

- **PATRÓN** `drift_60min` |x|≤ `0.1677` → IC=+0.127 (n=464)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.63€ cuando `drift_60min` |x|≤ 0.1677 (IC base=+0.124)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0596` → IC=+0.126 (n=528)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.63€ cuando `delta_ratio_macro` |x|> 0.0596 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.128 (n=563)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 4.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.151 (n=236)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 6.0 (IC base=+0.124)

- **PATRÓN** `ibs_15` > `0.5788` → IC=+0.213 (n=528)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5788 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `0.4301` → IC=+0.150 (n=135)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.4301 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` < `0.5508` → IC=+0.121 (n=547)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.5508 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `15.311` → IC=+0.221 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 15.311 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=542)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `3043.835` → IC=+0.150 (n=352)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3043.835 (IC base=+0.124)

### UPDOWN_GBM#5min
- **FILTRO** `sigma_ewma_delta_pct` > `6.428` → IC=-0.205 (n=59)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.428
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=818)

### UPDOWN_GBM#60min
- **FILTRO** `sigma_ewma_delta_pct` > `16.462` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 16.462
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=61)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=64)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.189 (n=101)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0032 (IC base=+0.163)

- **PATRÓN** `sigma_h` > `0.0045` → IC=+0.171 (n=68)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0045 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.1916` → IC=+0.193 (n=151)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1916 (IC base=+0.163)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3033` → IC=+0.204 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3033 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.192 (n=157)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 4.0 (IC base=+0.163)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.162 (n=155)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 17.0 (IC base=+0.163)

- **PATRÓN** `ibs_15` > `0.8791` → IC=+0.284 (n=100)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8791 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `0.306` → IC=+0.206 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.306 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` < `0.5508` → IC=+0.167 (n=166)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.5508 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.367` → IC=+0.214 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.367 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` < `18.708` → IC=+0.162 (n=152)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 18.708 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `14354.3614` → IC=+0.250 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14354.3614 (IC base=+0.163)

### UPDOWN_GBM#BTC#5min
- **FILTRO** `sigma_h` > `0.0048` → IC=-0.200 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=58)

- **FILTRO** `ibs_15` < `0.1693` → IC=-0.214 (n=19)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.1693
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=57)

- **FILTRO** `libro_liquidez` < `12035.1668` → IC=-0.125 (n=38)

  - _Acción_: SKIP cuando `libro_liquidez` < 12035.1668
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=38)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `ibs_15` < `0.6426` → IC=-0.198 (n=41)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6426
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=124)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.671` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 18.671 (IC base=+0.005)

### UPDOWN_GBM#ETH#15min
- **FILTRO** `ibs_15` < `0.6314` → IC=-0.233 (n=43)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6314
  - _Potencial_: sin este filtro IC_bueno=+0.187 (n=132)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1908` → IC=+0.145 (n=60)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.73€ cuando `delta_ratio_macro` |x|> 0.1908 (IC base=+0.082)

- **PATRÓN** `ibs_15` > `0.6314` → IC=+0.187 (n=132)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.93€ cuando `ibs_15` > 0.6314 (IC base=+0.082)

### UPDOWN_GBM#ETH#5min
- **FILTRO** `hora_utc` > `8.0` → IC=-0.200 (n=28)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=74)

- **FILTRO** `dist_vwap_pct` > `0.1505` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1505
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=86)

- **FILTRO** `libro_liquidez` < `8064.8076` → IC=-0.123 (n=51)

  - _Acción_: SKIP cuando `libro_liquidez` < 8064.8076
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=51)

- **FILTRO** `drift_15min` |x|> `0.5024` → IC=-0.153 (n=142)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.5024
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=428)

### UPDOWN_GBM#SOL#15min
- **FILTRO** `ibs_15` < `0.5385` → IC=-0.214 (n=26)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5385
  - _Potencial_: sin este filtro IC_bueno=+0.268 (n=54)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0615` → IC=+0.129 (n=60)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.65€ cuando `delta_ratio_macro` |x|> 0.0615 (IC base=+0.110)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.196 (n=21)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 5.0 (IC base=+0.110)

- **PATRÓN** `ibs_15` > `0.5385` → IC=+0.268 (n=54)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5385 (IC base=+0.110)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.935` → IC=+0.382 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.935 (IC base=+0.110)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.125 (n=54)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.01 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `3020.8724` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3020.8724 (IC base=+0.110)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0251` → IC=-0.242 (n=29)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0251
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=91)

- **FILTRO** `hora_utc` < `7.0` → IC=-0.190 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=93)

- **FILTRO** `ibs_15` < `0.4286` → IC=-0.207 (n=39)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.4286
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=81)

### UPDOWN_GBM#SOL#60min
- **FILTRO** `sigma_ewma_delta_pct` < `8.524` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 8.524
  - _Potencial_: sin este filtro IC_bueno=+0.192 (n=11)

- **PATRÓN** `ibs_15` > `0.6` → IC=+0.128 (n=41)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.64€ cuando `ibs_15` > 0.6 (IC base=+0.018)

- **PATRÓN** `dist_vwap_pct` < `0.4088` → IC=+0.183 (n=39)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.4088 (IC base=+0.018)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `delta_ratio_macro` |x|> `0.0501` → IC=+0.152 (n=139)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio_macro` |x|> 0.0501 (IC base=+0.104)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.151 (n=64)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 6.0 (IC base=+0.104)

- **PATRÓN** `ibs_15` > `0.5676` → IC=+0.198 (n=124)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.99€ cuando `ibs_15` > 0.5676 (IC base=+0.104)

- **PATRÓN** `dist_vwap_pct` > `0.4411` → IC=+0.208 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4411 (IC base=+0.104)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.642` → IC=+0.250 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.642 (IC base=+0.104)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.128 (n=119)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `2492.3796` → IC=+0.159 (n=124)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 2492.3796 (IC base=+0.104)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.167 (n=40)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 30.0 (IC base=+0.104)

- **PATRÓN** `ibs_15` < `0.125` → IC=+0.171 (n=165)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.85€ cuando `ibs_15` < 0.125 (IC base=+0.035)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.320 (n=131)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.321)

- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.397 (n=66)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0057 (IC base=+0.321)

- **PATRÓN** `drift_60min` |x|≤ `0.1153` → IC=+0.350 (n=131)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1153 (IC base=+0.321)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1426` → IC=+0.327 (n=131)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1426 (IC base=+0.321)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.342 (n=213)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.321)

- **PATRÓN** `ibs_15` > `0.7862` → IC=+0.369 (n=196)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7862 (IC base=+0.321)

- **PATRÓN** `dist_vwap_pct` > `0.2966` → IC=+0.354 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2966 (IC base=+0.321)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.694` → IC=+0.330 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.694 (IC base=+0.321)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.888` → IC=+0.330 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.888 (IC base=+0.321)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.325 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.321)

- **PATRÓN** `libro_liquidez` > `8243.8465` → IC=+0.346 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8243.8465 (IC base=+0.321)

- **PATRÓN** `ballena_activa_n` < `528.0` → IC=+0.373 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 528.0 (IC base=+0.321)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1204` → IC=+0.329 (n=39)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1204 (IC base=+0.312)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.350 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.312)

- **PATRÓN** `drift_60min` |x|≤ `0.16` → IC=+0.335 (n=101)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.16 (IC base=+0.312)

- **PATRÓN** `drift_15min` |x|≤ `0.4136` → IC=+0.330 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4136 (IC base=+0.312)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1236` → IC=+0.400 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1236 (IC base=+0.312)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.345 (n=121)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.312)

- **PATRÓN** `ibs_15` > `0.9234` → IC=+0.385 (n=76)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9234 (IC base=+0.312)

- **PATRÓN** `dist_vwap_pct` > `0.2738` → IC=+0.385 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2738 (IC base=+0.312)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.716` → IC=+0.309 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.716 (IC base=+0.312)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.509` → IC=+0.333 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 8.509 (IC base=+0.312)

- **PATRÓN** `libro_liquidez` > `11439.5159` → IC=+0.352 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11439.5159 (IC base=+0.312)

- **PATRÓN** `ballena_activa_n` < `625.0` → IC=+0.426 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 625.0 (IC base=+0.312)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.342 (n=36)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.329)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.375 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.329)

- **PATRÓN** `drift_60min` |x|≤ `0.1189` → IC=+0.377 (n=55)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1189 (IC base=+0.329)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0642` → IC=+0.345 (n=82)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0642 (IC base=+0.329)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2105` → IC=+0.346 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2105 (IC base=+0.329)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.335 (n=83)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.329)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.327 (n=73)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.329)

- **PATRÓN** `ibs_15` > `0.7785` → IC=+0.393 (n=82)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7785 (IC base=+0.329)

- **PATRÓN** `dist_vwap_pct` < `0.3157` → IC=+0.340 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3157 (IC base=+0.329)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.588` → IC=+0.370 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.588 (IC base=+0.329)

- **PATRÓN** `sigma_ewma_delta_pct` < `19.88` → IC=+0.328 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 19.88 (IC base=+0.329)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.339 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.329)

- **PATRÓN** `libro_liquidez` > `2812.5928` → IC=+0.329 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2812.5928 (IC base=+0.329)

- **PATRÓN** `ballena_activa_n` < `167.0` → IC=+0.329 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 167.0 (IC base=+0.329)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0108` → IC=-0.207 (n=336)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0108
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=1012)

- **FILTRO** `ibs_15` < `0.4909` → IC=-0.223 (n=117)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.4909
  - _Potencial_: sin este filtro IC_bueno=+0.183 (n=354)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.142 (n=347)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=1001)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2968` → IC=+0.171 (n=168)

  - _Acción_: Kelly boost +0.85€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2968 (IC base=-0.070)

- **PATRÓN** `ibs_15` > `0.4909` → IC=+0.183 (n=354)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.91€ cuando `ibs_15` > 0.4909 (IC base=-0.070)

- **PATRÓN** `delta_ratio_macro` |x|> `0.124` → IC=+0.232 (n=300)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.124 (IC base=-0.063)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1028` → IC=+0.254 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1028 (IC base=-0.063)

- **PATRÓN** `ibs_15` < `0.3696` → IC=+0.270 (n=451)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3696 (IC base=-0.063)

- **PATRÓN** `dist_vwap_pct` < `0.2567` → IC=+0.223 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2567 (IC base=-0.063)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.234 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 52.0 (IC base=-0.063)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `ibs_15` < `0.6975` → IC=-0.136 (n=20)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6975
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=43)

- **FILTRO** `sigma_h` > `0.0074` → IC=-0.237 (n=226)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0074
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=680)

- **FILTRO** `sigma_h` < `0.0038` → IC=-0.233 (n=298)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0038
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=608)

- **FILTRO** `drift_15min` |x|> `0.7355` → IC=-0.202 (n=226)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.7355
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=680)

- **FILTRO** `sigma_ewma_delta_pct` > `19.475` → IC=-0.250 (n=166)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.475
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=740)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.136 (n=64)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0028 (IC base=+0.018)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1355` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1355 (IC base=+0.018)

- **PATRÓN** `ibs_15` > `0.8303` → IC=+0.353 (n=32)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8303 (IC base=+0.018)

- **PATRÓN** `dist_vwap_pct` < `0.354` → IC=+0.150 (n=38)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.354 (IC base=+0.018)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.5457` → IC=-0.307 (n=55)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5457
  - _Potencial_: sin este filtro IC_bueno=+0.208 (n=166)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=204)

- **PATRÓN** `drift_60min` |x|≤ `0.0608` → IC=+0.224 (n=56)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0608 (IC base=+0.079)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2866` → IC=+0.217 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2866 (IC base=+0.079)

- **PATRÓN** `ibs_15` > `0.5457` → IC=+0.208 (n=166)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5457 (IC base=+0.079)

- **PATRÓN** `libro_liquidez` > `10550.3134` → IC=+0.205 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10550.3134 (IC base=+0.079)

- **PATRÓN** `sigma_h` < `0.008` → IC=+0.250 (n=226)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.210)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.210 (n=226)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.4431` → IC=+0.219 (n=226)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4431 (IC base=+0.210)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0914` → IC=+0.216 (n=202)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0914 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `19.0` → IC=+0.225 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 19.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.285 (n=77)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.210)

- **PATRÓN** `ibs_15` < `0.2922` → IC=+0.291 (n=199)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.2922 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` > `0.1816` → IC=+0.223 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1816 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` < `0.4118` → IC=+0.210 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4118 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` < `11.326` → IC=+0.227 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 11.326 (IC base=+0.210)

- **PATRÓN** `ballena_activa_n` < `184.0` → IC=+0.208 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 184.0 (IC base=+0.210)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0104` → IC=-0.253 (n=83)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0104
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=250)

- **FILTRO** `drift_60min` |x|> `0.1627` → IC=-0.187 (n=113)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1627
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=220)

- **FILTRO** `drift_15min` |x|> `0.8627` → IC=-0.253 (n=83)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8627
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=250)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.153 (n=119)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=214)

- **PATRÓN** `ibs_15` > `0.8182` → IC=+0.237 (n=17)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8182 (IC base=-0.127)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1209` → IC=+0.162 (n=66)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.81€ cuando `delta_ratio_macro` |x|> 0.1209 (IC base=-0.046)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1843` → IC=+0.188 (n=62)

  - _Acción_: Kelly boost +0.94€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1843 (IC base=-0.046)

- **PATRÓN** `ibs_15` < `0.3814` → IC=+0.223 (n=99)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3814 (IC base=-0.046)

- **PATRÓN** `ibs_15` > `0.0741` → IC=+0.167 (n=88)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.83€ cuando `ibs_15` > 0.0741 (IC base=-0.046)

- **PATRÓN** `dist_vwap_pct` < `0.5697` → IC=+0.186 (n=103)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.5697 (IC base=-0.046)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.167 (n=88)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 42.0 (IC base=-0.046)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0227` → IC=-0.254 (n=124)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0227
  - _Potencial_: sin este filtro IC_bueno=-0.137 (n=243)

- **FILTRO** `drift_15min` |x|> `1.198` → IC=-0.253 (n=91)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.198
  - _Potencial_: sin este filtro IC_bueno=-0.151 (n=276)

- **FILTRO** `sigma_ewma_delta_pct` > `3.98` → IC=-0.177 (n=131)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 3.98
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=236)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.273 (n=42)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.164 (n=325)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1534` → IC=+0.345 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1534 (IC base=-0.058)

- **PATRÓN** `ibs_15` < `0.05` → IC=+0.321 (n=37)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.05 (IC base=-0.058)

- **PATRÓN** `dist_vwap_pct` > `0.5629` → IC=+0.346 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5629 (IC base=-0.058)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.297 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=-0.058)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `dist_vwap_pct` > `0.0928` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.0928 (IC base=+0.085)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `dist_vwap_pct` > `0.0928` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.0928 (IC base=+0.085)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.282 (n=333)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.282)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.304 (n=151)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.282)

- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.323 (n=111)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.282)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1294` → IC=+0.299 (n=222)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1294 (IC base=+0.282)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1077` → IC=+0.321 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1077 (IC base=+0.282)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.311 (n=347)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.282)

- **PATRÓN** `ibs_15` > `0.8341` → IC=+0.315 (n=333)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8341 (IC base=+0.282)

- **PATRÓN** `dist_vwap_pct` > `0.3041` → IC=+0.325 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3041 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` < `18.902` → IC=+0.283 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 18.902 (IC base=+0.282)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.287 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `13738.8823` → IC=+0.332 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13738.8823 (IC base=+0.282)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.298 (n=127)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.280)

- **PATRÓN** `sigma_h` > `0.006` → IC=+0.300 (n=63)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.280)

- **PATRÓN** `drift_60min` |x|≤ `0.1567` → IC=+0.293 (n=167)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1567 (IC base=+0.280)

- **PATRÓN** `drift_15min` |x|≤ `0.4223` → IC=+0.279 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4223 (IC base=+0.280)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1286` → IC=+0.312 (n=126)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1286 (IC base=+0.280)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.311 (n=199)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.280)

- **PATRÓN** `ibs_15` > `0.9689` → IC=+0.341 (n=86)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9689 (IC base=+0.280)

- **PATRÓN** `dist_vwap_pct` > `0.3186` → IC=+0.354 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3186 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.101` → IC=+0.318 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.101 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.606` → IC=+0.287 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 8.606 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `15415.1121` → IC=+0.346 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15415.1121 (IC base=+0.280)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.288 (n=144)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0074 (IC base=+0.282)

- **PATRÓN** `sigma_h` > `0.0042` → IC=+0.285 (n=128)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0042 (IC base=+0.282)

- **PATRÓN** `drift_60min` |x|≤ `0.0694` → IC=+0.318 (n=64)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0694 (IC base=+0.282)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1881` → IC=+0.321 (n=65)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1881 (IC base=+0.282)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3595` → IC=+0.304 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3595 (IC base=+0.282)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.321 (n=138)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.282)

- **PATRÓN** `ibs_15` > `0.8452` → IC=+0.315 (n=144)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8452 (IC base=+0.282)

- **PATRÓN** `dist_vwap_pct` > `0.0935` → IC=+0.302 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.0935 (IC base=+0.282)

- **PATRÓN** `dist_vwap_pct` < `0.4822` → IC=+0.282 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4822 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.791` → IC=+0.294 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.791 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` < `19.469` → IC=+0.292 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 19.469 (IC base=+0.282)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.298 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `10575.7678` → IC=+0.306 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10575.7678 (IC base=+0.282)

- **PATRÓN** `ballena_activa_n` < `112.0` → IC=+0.308 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 112.0 (IC base=+0.282)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0809` → IC=-0.257 (n=72)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0809
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=142)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.170 (n=107)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=58)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.174` → IC=-0.129 (n=60)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.174
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=61)

- **FILTRO** `sigma_h` > `0.0034` → IC=-0.200 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0034
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
- **FILTRO** `sigma_h` < `0.0033` → IC=-0.324 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0931` → IC=-0.214 (n=19)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0931
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### WEEKLY_PRICE
- **PATRÓN** `ratio` < `0.9779` → IC=+0.429 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9779 (IC base=+0.111)

- **PATRÓN** `T_h` > `145.9915` → IC=+0.420 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.9915 (IC base=+0.343)

- **PATRÓN** `ratio` > `1.012` → IC=+0.312 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.012 (IC base=+0.343)

### WEEKLY_PRICE#BTC
- **PATRÓN** `ratio` < `0.973` → IC=+0.370 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.096)

- **PATRÓN** `ratio` > `1.0104` → IC=+0.315 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0104 (IC base=+0.279)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` < `63.9712` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 63.9712 (IC base=+0.154)

- **PATRÓN** `ratio` < `0.9647` → IC=+0.433 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9647 (IC base=+0.154)

- **PATRÓN** `T_h` > `100.962` → IC=+0.322 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 100.962 (IC base=+0.313)

- **PATRÓN** `ratio` > `1.012` → IC=+0.300 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.012 (IC base=+0.313)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `127.3918` → IC=+0.426 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 127.3918 (IC base=+0.410)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5788 sube el IC de +0.124 a +0.213 en UPDOWN_GBM#15min (n=528). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.8791 sube el IC de +0.163 a +0.284 en UPDOWN_GBM#BTC#15min (n=100). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6314 sube el IC de +0.082 a +0.187 en UPDOWN_GBM#ETH#15min (n=132). Ya aplicado como kelly_boost=+0.93€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.5385 sube el IC de +0.110 a +0.268 en UPDOWN_GBM#SOL#15min (n=54). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5676 sube el IC de +0.104 a +0.198 en UPDOWN_GBM#XRP#15min (n=124). Ya aplicado como kelly_boost=+0.99€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.125 sube el IC de +0.035 a +0.171 en UPDOWN_GBM#XRP#15min (n=165). Ya aplicado como kelly_boost=+0.85€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.4909 sube el IC de -0.070 a +0.183 en UPDOWN_GBM_15M_TARDIO (n=354). Ya aplicado como kelly_boost=+0.91€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3696 sube el IC de -0.063 a +0.270 en UPDOWN_GBM_15M_TARDIO (n=451). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.8303 sube el IC de +0.018 a +0.353 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=32). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5457 sube el IC de +0.079 a +0.208 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=166). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.2922 sube el IC de +0.210 a +0.291 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=199). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8182 sube el IC de -0.127 a +0.237 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3814 sube el IC de -0.046 a +0.223 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=99). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS > 0.0741 sube el IC de -0.046 a +0.167 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=88). Ya aplicado como kelly_boost=+0.83€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.05 sube el IC de -0.058 a +0.321 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=37). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8341 sube el IC de +0.282 a +0.315 en UPDOWN_GBM_IBS_ALTO (n=333). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.9689 sube el IC de +0.280 a +0.341 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=86). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8452 sube el IC de +0.282 a +0.315 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=144). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7862 sube el IC de +0.321 a +0.369 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=196). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.9234 sube el IC de +0.312 a +0.385 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=76). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7785 sube el IC de +0.329 a +0.393 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=82). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min` — IC=+0.365 n=35. Faltan ~5 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL` — IC=+0.365 n=35. Faltan ~5 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `BALLENAS_CONFIRMADAS_15M#XRP#15min` — IC=+0.129 n=33. Faltan ~7 resoluciones para umbral n≥40. ETA: ~5h.
- **LIVE-CANDIDATA**: `BALLENAS_CONFIRMADAS_15M#XRP` — IC=+0.129 n=33. Faltan ~7 resoluciones para umbral n≥40. ETA: ~5h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 811 | +0.089 | +49.30€ | 2 | 11 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 811 | +0.089 | +49.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 24 | +0.077 | +1.55€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 24 | +0.077 | +1.55€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 532 | +0.109 | +41.17€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 532 | +0.109 | +41.17€ | 2 | 11 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 222 | +0.036 | -0.81€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 222 | +0.036 | -0.81€ | 5 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 33 | +0.129 | +7.38€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 33 | +0.129 | +7.38€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 14818 | -0.113 | -2536.54€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 956 | -0.010 | -142.62€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 13862 | -0.119 | -2393.93€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 1925 | -0.092 | -428.38€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 1925 | -0.092 | -428.38€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 956 | -0.010 | -142.62€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 956 | -0.010 | -142.62€ | 2 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 1977 | -0.170 | -547.95€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 1977 | -0.170 | -547.95€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 3959 | -0.050 | -371.02€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 3959 | -0.050 | -371.02€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 3291 | -0.128 | -290.80€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 3291 | -0.128 | -290.80€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 2710 | -0.194 | -755.78€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 2710 | -0.194 | -755.78€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 4105 | -0.071 | +1808.25€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 1168 | -0.009 | +853.12€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 2937 | -0.096 | +955.14€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 4105 | -0.071 | +1808.25€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 1168 | -0.009 | +853.12€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 2937 | -0.096 | +955.14€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 87 | -0.073 | -15.45€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 87 | -0.073 | -15.45€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 87 | -0.073 | -15.45€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 87 | -0.073 | -15.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 47734 | +0.113 | -3021.82€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 7979 | +0.184 | -285.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 162 | -0.110 | -54.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 35845 | +0.098 | -2608.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 3748 | +0.116 | -73.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 6022 | +0.082 | -806.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 27 | -0.121 | +3.75€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 5980 | +0.084 | -798.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 9571 | +0.132 | -230.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 2350 | +0.197 | -118.99€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 5920 | +0.109 | -137.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 1259 | +0.126 | +48.37€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 6036 | +0.081 | -770.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 29 | +0.016 | +3.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#240min | 9 | -0.143 | -7.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 5998 | +0.082 | -766.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 10327 | +0.126 | -169.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 2974 | +0.172 | -15.94€ | 1 | 8 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 5959 | +0.111 | -105.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 1382 | +0.095 | -40.02€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 9759 | +0.125 | -627.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 2578 | +0.192 | -159.00€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 79 | -0.006 | -2.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 5995 | +0.097 | -383.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1107 | +0.131 | -82.29€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 6019 | +0.105 | -417.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 21 | -0.022 | +1.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 5 | -0.018 | -1.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 5993 | +0.105 | -417.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 7935 | +0.177 | -623.31€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 7935 | +0.177 | -623.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 2025 | +0.165 | -228.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 2025 | +0.165 | -228.65€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 148 | -0.133 | -0.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 148 | -0.133 | -0.32€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 1978 | +0.168 | -212.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 1978 | +0.168 | -212.66€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 1772 | +0.237 | -38.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 1772 | +0.237 | -38.79€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 1933 | +0.182 | -156.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 1933 | +0.182 | -156.65€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 397 | +0.447 | +4.64€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 397 | +0.447 | +4.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 149 | +0.440 | +0.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 149 | +0.440 | +0.57€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 154 | +0.442 | +1.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 154 | +0.442 | +1.41€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 90 | +0.446 | +2.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 90 | +0.446 | +2.43€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 25469 | +0.187 | -2440.49€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 25469 | +0.187 | -2440.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 4538 | +0.146 | -730.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 4538 | +0.146 | -730.13€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 3973 | +0.225 | -144.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 3973 | +0.225 | -144.83€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 4408 | +0.161 | -613.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 4408 | +0.161 | -613.38€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 4048 | +0.218 | -170.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 4048 | +0.218 | -170.77€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 4211 | +0.198 | -321.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 4211 | +0.198 | -321.03€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 4291 | +0.182 | -460.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 4291 | +0.182 | -460.35€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 9246 | +0.133 | +354.43€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 9246 | +0.133 | +354.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 4594 | +0.138 | +214.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 4594 | +0.138 | +214.40€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 4652 | +0.128 | +140.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 4652 | +0.128 | +140.03€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 947 | +0.293 | -7.52€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 947 | +0.293 | -7.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 409 | +0.276 | -13.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 409 | +0.276 | -13.65€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 446 | +0.299 | +7.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 446 | +0.299 | +7.10€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 92 | +0.330 | -0.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 92 | +0.330 | -0.96€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 406 | +0.422 | -12.00€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 406 | +0.422 | -12.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 183 | +0.419 | -6.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 183 | +0.419 | -6.38€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 188 | +0.426 | -4.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 188 | +0.426 | -4.94€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 35 | +0.365 | -0.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 35 | +0.365 | -0.68€ | 0 | 1 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 465 | +0.102 | +1.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 155 | +0.099 | -3.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 310 | +0.103 | +4.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 26 | +0.143 | +2.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 26 | +0.143 | +2.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 368 | +0.111 | +9.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 58 | +0.150 | +5.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 310 | +0.103 | +4.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 71 | +0.034 | -11.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 71 | +0.034 | -11.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 13903 | +0.094 | -536.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 1252 | +0.073 | -28.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 12651 | +0.096 | -508.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 8376 | +0.097 | -196.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 1252 | +0.073 | -28.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 7124 | +0.101 | -167.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 1720 | +0.120 | +40.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 1720 | +0.120 | +40.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 3807 | +0.076 | -381.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 3807 | +0.076 | -381.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 559 | +0.263 | -64.11€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 559 | +0.263 | -64.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 559 | +0.263 | -64.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 559 | +0.263 | -64.11€ | 0 | 4 |
| ✅ GBM_LATE_15M | 11984 | +0.058 | +5086.24€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 11984 | +0.058 | +5086.24€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 1821 | +0.196 | +1331.16€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 1821 | +0.196 | +1331.16€ | 0 | 23 |
| ✅ GBM_LATE_15M#BTC | 1800 | +0.174 | +1201.83€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 1800 | +0.174 | +1201.83€ | 0 | 27 |
| ✅ GBM_LATE_15M#DOGE | 1865 | +0.196 | +1362.74€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 1865 | +0.196 | +1362.74€ | 0 | 19 |
| ✅ GBM_LATE_15M#ETH | 1871 | -0.037 | +103.45€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 1871 | -0.037 | +103.45€ | 3 | 12 |
| ✅ GBM_LATE_15M#SOL | 1950 | -0.048 | +475.12€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 1950 | -0.048 | +475.12€ | 4 | 7 |
| ✅ GBM_LATE_15M#XRP | 2677 | -0.069 | +611.94€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 2677 | -0.069 | +611.94€ | 4 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 12729 | +0.062 | +6662.89€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 12729 | +0.062 | +6662.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 2193 | -0.004 | +1694.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 2193 | -0.004 | +1694.12€ | 2 | 6 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 2771 | -0.021 | +415.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 2771 | -0.021 | +415.25€ | 1 | 8 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 1658 | +0.258 | +1644.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 1658 | +0.258 | +1644.10€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 1951 | -0.047 | +64.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 1951 | -0.047 | +64.15€ | 8 | 5 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 2110 | -0.013 | +757.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 2110 | -0.013 | +757.86€ | 3 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 2046 | +0.265 | +2087.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 2046 | +0.265 | +2087.41€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 9877 | +0.171 | +7051.23€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 9877 | +0.171 | +7051.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 1395 | +0.199 | +1063.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 1395 | +0.199 | +1063.94€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 1633 | +0.161 | +1179.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 1633 | +0.161 | +1179.37€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 1422 | +0.200 | +1091.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 1422 | +0.200 | +1091.76€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 1620 | +0.145 | +1000.69€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 1620 | +0.145 | +1000.69€ | 0 | 27 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 1834 | +0.124 | +1160.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 1834 | +0.124 | +1160.56€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 1973 | +0.202 | +1554.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 1973 | +0.202 | +1554.90€ | 0 | 20 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 2167 | +0.102 | +695.47€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 2167 | +0.102 | +695.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 73 | +0.087 | +25.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 73 | +0.087 | +25.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 535 | +0.075 | +148.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 535 | +0.075 | +148.89€ | 0 | 12 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 322 | +0.148 | +158.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 322 | +0.148 | +158.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 466 | +0.167 | +194.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 466 | +0.167 | +194.87€ | 0 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 395 | +0.001 | +25.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 395 | +0.001 | +25.29€ | 4 | 5 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 376 | +0.127 | +142.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 376 | +0.127 | +142.64€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO | 11797 | +0.176 | +8567.73€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#15min | 11797 | +0.176 | +8567.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 1749 | +0.221 | +1480.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 1749 | +0.221 | +1480.71€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 1926 | +0.161 | +1379.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 1926 | +0.161 | +1379.63€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 1769 | +0.224 | +1512.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 1769 | +0.224 | +1512.38€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 1820 | +0.140 | +1114.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 1820 | +0.140 | +1114.39€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 2081 | +0.106 | +1148.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 2081 | +0.106 | +1148.85€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 2452 | +0.206 | +1931.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 2452 | +0.206 | +1931.77€ | 0 | 22 |
| ✅ GBM_LATE_5M | 3745 | +0.122 | +1701.16€ | 1 | 23 |
| ✅ GBM_LATE_5M#5min | 3745 | +0.122 | +1701.16€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 235 | +0.171 | +149.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 235 | +0.171 | +149.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1033 | +0.109 | +490.25€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1033 | +0.109 | +490.25€ | 1 | 15 |
| ✅ GBM_LATE_5M#DOGE | 463 | +0.147 | +246.88€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 463 | +0.147 | +246.88€ | 0 | 11 |
| ✅ GBM_LATE_5M#ETH | 1292 | +0.138 | +625.80€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 1292 | +0.138 | +625.80€ | 0 | 29 |
| ✅ GBM_LATE_5M#SOL | 163 | -0.003 | +6.80€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 163 | -0.003 | +6.80€ | 2 | 1 |
| ✅ GBM_LATE_5M#XRP | 559 | +0.101 | +181.44€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 559 | +0.101 | +181.44€ | 0 | 0 |
| ✅ GBM_LATE_60M | 696 | +0.026 | +227.73€ | 3 | 14 |
| ✅ GBM_LATE_60M#60min | 696 | +0.026 | +227.73€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 232 | +0.060 | +62.71€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 232 | +0.060 | +62.71€ | 1 | 10 |
| ✅ GBM_LATE_60M#ETH | 257 | +0.060 | +116.69€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 257 | +0.060 | +116.69€ | 1 | 13 |
| ✅ GBM_LATE_60M#SOL | 207 | -0.055 | +48.32€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 207 | -0.055 | +48.32€ | 2 | 8 |
| 🚫 GBM_LATE_60M_FADE | 215 | -0.297 | -33.27€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 215 | -0.297 | -33.27€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 85 | -0.247 | -8.22€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 85 | -0.247 | -8.22€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 69 | -0.359 | -21.09€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 69 | -0.359 | -21.09€ | 2 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 61 | -0.278 | -3.96€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 61 | -0.278 | -3.96€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 437 | +0.047 | +41.81€ | 1 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 437 | +0.047 | +41.81€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 187 | +0.045 | +25.52€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 187 | +0.045 | +25.52€ | 3 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 111 | +0.066 | +0.58€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 111 | +0.066 | +0.58€ | 1 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 139 | +0.032 | +15.71€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 139 | +0.032 | +15.71€ | 2 | 3 |
| ✅ LATE_WINDOW_5MIN | 42 | +0.204 | +15.02€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 42 | +0.204 | +15.02€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 42 | +0.204 | +15.02€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 42 | +0.204 | +15.02€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 556 | +0.100 | +136.24€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 556 | +0.100 | +136.24€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 556 | +0.100 | +136.24€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 556 | +0.100 | +136.24€ | 0 | 2 |
| ✅ LIQUIDACIONES_15M | 314 | -0.095 | -36.38€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 314 | -0.095 | -36.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 71 | -0.103 | -9.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 71 | -0.103 | -9.18€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 66 | -0.073 | -6.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 66 | -0.073 | -6.94€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 96 | -0.020 | -3.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 96 | -0.020 | -3.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 1245 | -0.012 | -21.71€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 1245 | -0.012 | -21.71€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 70 | -0.014 | -3.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 70 | -0.014 | -3.67€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 148 | -0.033 | -4.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 148 | -0.033 | -4.86€ | 2 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 96 | -0.061 | -6.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 96 | -0.061 | -6.98€ | 2 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 397 | +0.011 | +7.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 397 | +0.011 | +7.33€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 444 | -0.004 | -7.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 444 | -0.004 | -7.56€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 90 | -0.065 | -5.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 90 | -0.065 | -5.96€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M | 626 | -0.014 | -1.05€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 626 | -0.014 | -1.05€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 187 | -0.034 | -9.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 187 | -0.034 | -9.30€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 189 | +0.013 | +5.68€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 189 | +0.013 | +5.68€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 250 | -0.020 | +2.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 250 | -0.020 | +2.57€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 7357 | -0.003 | -94.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 7357 | -0.003 | -94.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 542 | -0.004 | +2.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 542 | -0.004 | +2.87€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 668 | -0.013 | -10.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 668 | -0.013 | -10.86€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 1748 | +0.007 | -17.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 1748 | +0.007 | -17.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 1585 | +0.001 | +1.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 1585 | +0.001 | +1.75€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 1337 | -0.012 | -37.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 1337 | -0.012 | -37.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1477 | -0.006 | -32.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1477 | -0.006 | -32.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 11888 | -0.032 | +609.16€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 11888 | -0.032 | +609.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 1954 | -0.021 | +318.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 1954 | -0.021 | +318.61€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 2052 | -0.030 | -9.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 2052 | -0.030 | -9.73€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 1975 | -0.035 | +180.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 1975 | -0.035 | +180.21€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 1971 | -0.042 | -25.67€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 1971 | -0.042 | -25.67€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 1996 | -0.037 | +74.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 1996 | -0.037 | +74.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 1940 | -0.027 | +71.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 1940 | -0.027 | +71.40€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 667 | -0.083 | -40.75€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 667 | -0.083 | -40.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 105 | -0.033 | -4.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 105 | -0.033 | -4.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 108 | -0.136 | -11.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 108 | -0.136 | -11.28€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 36 | -0.105 | -4.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 36 | -0.105 | -4.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 141 | -0.143 | -13.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 141 | -0.143 | -13.21€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 176 | -0.045 | +0.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 176 | -0.045 | +0.56€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 101 | -0.044 | -7.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 101 | -0.044 | -7.92€ | 2 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 32165 | -0.076 | +646.10€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 32165 | -0.076 | +646.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 5191 | -0.088 | +441.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 5191 | -0.088 | +441.70€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 5325 | -0.077 | -108.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 5325 | -0.077 | -108.73€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 5322 | -0.081 | +180.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 5322 | -0.081 | +180.63€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 4839 | -0.098 | -233.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 4839 | -0.098 | -233.17€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 6025 | -0.054 | +96.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 6025 | -0.054 | +96.77€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 5463 | -0.066 | +268.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 5463 | -0.066 | +268.89€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 6205 | -0.012 | -106.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 6205 | -0.012 | -106.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 994 | -0.018 | -21.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 994 | -0.018 | -21.35€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1295 | -0.005 | -10.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1295 | -0.005 | -10.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1002 | -0.020 | -30.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1002 | -0.020 | -30.79€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1348 | -0.003 | -7.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1348 | -0.003 | -7.88€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 830 | -0.014 | -11.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 830 | -0.014 | -11.82€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 736 | -0.020 | -23.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 736 | -0.020 | -23.66€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 721 | +0.113 | +238.63€ | 1 | 6 |
| ✅ ORDER_FLOW_5M#5min | 585 | +0.125 | +226.03€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 138 | +0.114 | +54.74€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 138 | +0.114 | +54.74€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#DOGE | 117 | +0.097 | +27.02€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 117 | +0.097 | +27.02€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#ETH | 112 | +0.105 | +38.23€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 112 | +0.105 | +38.23€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 102 | +0.192 | +68.59€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 102 | +0.192 | +68.59€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 116 | +0.119 | +37.46€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 116 | +0.119 | +37.46€ | 0 | 5 |
| ✅ PRICE_TARGET_GBM | 337 | -0.128 | -13.63€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC | 147 | -0.205 | -35.98€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC#atexpiry | 117 | -0.265 | -37.75€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 30 | +0.031 | +1.77€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 127 | -0.105 | +1.06€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 90 | -0.130 | -6.07€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 37 | -0.038 | +7.13€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 63 | +0.008 | +21.30€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 46 | -0.021 | +14.21€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 17 | +0.067 | +7.08€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 253 | -0.174 | -29.61€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 84 | +0.012 | +15.98€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 351 | -0.214 | -9.87€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 151 | -0.173 | -10.21€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 127 | -0.159 | -8.93€ | 4 | 2 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 24 | -0.231 | -1.28€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 128 | -0.269 | -18.83€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 106 | -0.287 | -23.22€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 22 | -0.167 | +4.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 72 | -0.189 | +19.18€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 59 | -0.189 | +15.61€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 13 | -0.108 | +3.57€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 292 | -0.214 | -16.55€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#reach | 59 | -0.205 | +6.68€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 103 | +0.367 | +43.05€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#BTC | 18 | +0.000 | -2.75€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 18 | +0.000 | -2.75€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 26 | +0.321 | +5.89€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 26 | +0.321 | +5.89€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 59 | +0.484 | +39.91€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 59 | +0.484 | +39.91€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#sniper | 103 | +0.367 | +43.05€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 235 | +0.027 | -1.18€ | 3 | 1 |
| ✅ STREAK_FADE_15M#15min | 235 | +0.027 | -1.18€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 103 | +0.043 | +0.93€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 103 | +0.043 | +0.93€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 18 | +0.045 | +2.16€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 18 | +0.045 | +2.16€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 26 | +0.000 | -2.84€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 26 | +0.000 | -2.84€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP | 88 | +0.011 | -1.42€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 88 | +0.011 | -1.42€ | 0 | 0 |
| ✅ STREAK_FADE_5M | 1888 | -0.024 | -84.48€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 1888 | -0.024 | -84.48€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 788 | -0.015 | -23.77€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 788 | -0.015 | -23.77€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 553 | -0.026 | -25.13€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 553 | -0.026 | -25.13€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 141 | -0.038 | -12.96€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 141 | -0.038 | -12.96€ | 3 | 0 |
| ✅ STREAK_FADE_5M#XRP | 406 | -0.032 | -22.62€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 406 | -0.032 | -22.62€ | 4 | 0 |
| ✅ STREAK_FADE_60M | 45 | +0.011 | -0.05€ | 0 | 0 |
| ✅ STREAK_FADE_60M#60min | 45 | +0.011 | -0.05€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 28 | -0.067 | -2.41€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 28 | -0.067 | -2.41€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 17 | +0.112 | +2.36€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 17 | +0.112 | +2.36€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 3827 | +0.025 | +68.85€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 3827 | +0.025 | +68.85€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 1257 | +0.027 | +19.17€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 1257 | +0.027 | +19.17€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 771 | +0.042 | +34.15€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 771 | +0.042 | +34.15€ | 1 | 1 |
| ✅ STREAK_MOM_5M#SOL | 1132 | +0.012 | -0.47€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 1132 | +0.012 | -0.47€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 667 | +0.020 | +16.01€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 667 | +0.020 | +16.01€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 4183 | +0.010 | -30.24€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 4183 | +0.010 | -30.24€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 1603 | +0.010 | -13.42€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 1603 | +0.010 | -13.42€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 1662 | +0.019 | +1.28€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 1662 | +0.019 | +1.28€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 918 | -0.004 | -18.10€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 918 | -0.004 | -18.10€ | 2 | 0 |
| ✅ UPDOWN_GBM | 9740 | +0.009 | +271.14€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 3436 | +0.037 | +323.53€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 413 | +0.008 | +6.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 5229 | -0.007 | -59.20€ | 1 | 0 |
| ✅ UPDOWN_GBM#60min | 615 | +0.001 | +0.91€ | 2 | 0 |
| ✅ UPDOWN_GBM#BNB | 298 | +0.060 | +39.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 181 | +0.123 | +45.10€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 9 | -0.061 | -1.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 108 | -0.027 | -4.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 1891 | +0.016 | +97.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 389 | +0.068 | +69.08€ | 0 | 12 |
| ✅ UPDOWN_GBM#BTC#240min | 123 | +0.052 | +8.86€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 1134 | -0.001 | +19.24€ | 3 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 227 | +0.002 | -1.27€ | 1 | 1 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 1099 | +0.001 | +1.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 127 | +0.089 | +26.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 10 | +0.042 | +0.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 962 | -0.011 | -26.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 2063 | -0.001 | +9.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 1000 | +0.021 | +31.76€ | 1 | 2 |
| ✅ UPDOWN_GBM#ETH#240min | 116 | +0.034 | +7.86€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 672 | -0.036 | -30.11€ | 4 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 260 | +0.000 | +0.12€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 2817 | +0.005 | +19.14€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 898 | +0.006 | +13.97€ | 1 | 6 |
| ✅ UPDOWN_GBM#SOL#240min | 109 | -0.004 | -2.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 1670 | +0.008 | +6.07€ | 3 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 128 | +0.000 | +2.05€ | 1 | 2 |
| ✅ UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 1570 | +0.015 | +106.36€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 841 | +0.050 | +136.90€ | 0 | 9 |
| ✅ UPDOWN_GBM#XRP#240min | 46 | -0.125 | -6.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 683 | -0.020 | -23.83€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 261 | +0.321 | +60.10€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 261 | +0.321 | +60.10€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 152 | +0.312 | +27.03€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 152 | +0.312 | +27.03€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 109 | +0.329 | +33.06€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 109 | +0.329 | +33.06€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 5616 | -0.065 | +1301.97€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 5616 | -0.065 | +1301.97€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 307 | -0.050 | +341.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 307 | -0.050 | +341.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 1161 | -0.153 | -56.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 1161 | -0.153 | -56.25€ | 5 | 4 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 80 | +0.049 | +9.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 80 | +0.049 | +9.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 522 | +0.155 | +251.03€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 522 | +0.155 | +251.03€ | 2 | 15 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 1827 | -0.061 | +382.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 1827 | -0.061 | +382.11€ | 4 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 1719 | -0.083 | +373.71€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 1719 | -0.083 | +373.71€ | 4 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 50 | +0.058 | +0.88€ | 0 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 50 | +0.058 | +0.88€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 50 | +0.058 | +0.88€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 50 | +0.058 | +0.88€ | 0 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 443 | +0.282 | +343.01€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 443 | +0.282 | +343.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 252 | +0.280 | +192.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 252 | +0.280 | +192.57€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 191 | +0.282 | +150.44€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 191 | +0.282 | +150.44€ | 0 | 14 |
| ✅ UPDOWN_OU_5M | 640 | -0.098 | -72.71€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#5min | 640 | -0.098 | -72.71€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 310 | -0.077 | -35.00€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 310 | -0.077 | -35.00€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 159 | -0.047 | -8.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 159 | -0.047 | -8.23€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 54 | -0.161 | -8.04€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 54 | -0.161 | -8.04€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 50 | -0.173 | -7.40€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 50 | -0.173 | -7.40€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 1379 | +0.294 | +604.06€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 440 | +0.224 | +21.91€ | 0 | 2 |
| ✅ WEEKLY_PRICE#ETH | 454 | +0.274 | +132.22€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 485 | +0.373 | +449.93€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.085) — sin ventaja clara. oversold(IBS<0.3): IC=+0.025 n=3485 | neutral: IC=+0.003 n=3791 | overbought(IBS>0.7): IC=+0.088 n=3784
  - _Datos_: n=11502 IC=+0.040 PNL=+1159.04€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: (cache 894s) 177 celda(s) GATE OK de 2462 trackeadas

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.006 < 0.08 — monitorear
  - _Datos_: n=898 IC=+0.006 PNL=+13.97€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=454/15 IC=+0.274 PNL=+132.22€ | BTC: n=440/15 IC=+0.224 PNL=+21.91€ | SOL: n=485/15 IC=+0.373 PNL=+449.93€

**🟡 H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.066 n=153669 | tras_1loss IC=+0.051 n=120955 | tras_2loss IC=+0.015 n=54261/40 | gap=+0.051 (umbral 0.05)

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 22 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH#60min, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC#60min
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
  - _Estado_: 9678 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.078 n=62/60 | contraria IC=+0.143 n=40 | gap=-0.065 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=148, boost estimado=+0.011. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 102 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=260/40 IC=+0.000 PNL=+0.12€ | BTC#60min: n=227/40 IC=+0.002 PNL=-1.27€ | SOL#60min: n=128/40 IC=+0.000 PNL=+2.05€

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=-0.001 n=916 | contrario_BTC IC=-0.010 n=794/40 | gap=-0.009 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.187 > 0.08 con n=97 PNL=+60.31€
  - _Datos_: n=97 IC=+0.187 PNL=+60.31€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.141 > 0.08 con n=129 PNL=+43.58€
  - _Datos_: n=129 IC=+0.141 PNL=+43.58€

**⏳ H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: 25
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: 23/25 ops en el filtro definido (IC actual=+0.260 PNL=+17.70€)
  - _Datos_: n=23 IC=+0.260 PNL=+17.70€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.335 > 0.1 con n=1167 PNL=+604.98€
  - _Datos_: n=1167 IC=+0.335 PNL=+604.98€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=83 IC=+0.029 PNL=+13.25€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=83 IC=+0.029 PNL=+13.25€

**⏳ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: 30
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: 28/30 ops en el filtro definido (IC actual=+0.200 PNL=+19.04€)
  - _Datos_: n=28 IC=+0.200 PNL=+19.04€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=9463 IC=+0.006 PNL=+217.53€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=9463 IC=+0.006 PNL=+217.53€

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
  - _Estado_: n=497 IC=+0.009 PNL=+4.00€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=497 IC=+0.009 PNL=+4.00€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=118 IC=-0.033 PNL=-3.09€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=118 IC=-0.033 PNL=-3.09€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=173 IC=-0.031 PNL=+4.78€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=173 IC=-0.031 PNL=+4.78€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.124 > 0.1 con n=703 PNL=+208.08€
  - _Datos_: n=703 IC=+0.124 PNL=+208.08€

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
  - _Estado_: n=389 IC=+0.068 PNL=+69.08€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=389 IC=+0.068 PNL=+69.08€

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
  - _Estado_: n=2003 IC=+0.031 PNL=+169.45€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2003 IC=+0.031 PNL=+169.45€

**〰️ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: n=48 IC=-0.300 PNL=-12.01€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=48 IC=-0.300 PNL=-12.01€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=110 IC=-0.018 PNL=+7.94€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=110 IC=-0.018 PNL=+7.94€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=147 IC=+0.030 PNL=+9.72€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=147 IC=+0.030 PNL=+9.72€

**⏳ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: 15
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: 10/15 ops en el filtro definido (IC actual=+0.083 PNL=+2.14€)
  - _Datos_: n=10 IC=+0.083 PNL=+2.14€

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=2598 IC=-0.017 PNL=-44.58€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2598 IC=-0.017 PNL=-44.58€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.204 n=42) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=42 IC=+0.204 PNL=+15.02€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=2548 IC=+0.015 PNL=+108.63€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2548 IC=+0.015 PNL=+108.63€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=698 IC=+0.034 PNL=+20.02€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=698 IC=+0.034 PNL=+20.02€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.113 > 0.08 con n=210 PNL=+60.21€
  - _Datos_: n=210 IC=+0.113 PNL=+60.21€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.109 > 0.08 con n=172 PNL=+12.72€
  - _Datos_: n=172 IC=+0.109 PNL=+12.72€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.137 > 0.08 con n=155 PNL=+53.95€
  - _Datos_: n=155 IC=+0.137 PNL=+53.95€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=27077 IC=+0.102 PNL=+8506.42€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=27077 IC=+0.102 PNL=+8506.42€

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
  - _Estado_: n=1344 IC=+0.027 PNL=+70.99€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1344 IC=+0.027 PNL=+70.99€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.125 > 0.02 con n=398 PNL=+140.66€
  - _Datos_: n=398 IC=+0.125 PNL=+140.66€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.443 > 0.1 con n=719 PNL=+632.84€
  - _Datos_: n=719 IC=+0.443 PNL=+632.84€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=2364 IC=+0.028 PNL=+177.51€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=2364 IC=+0.028 PNL=+177.51€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.162 > 0.1 con n=1044 PNL=+388.55€
  - _Datos_: n=1044 IC=+0.162 PNL=+388.55€

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.189 < -0.1 con n=59 PNL=+0.07€
  - _Datos_: n=59 IC=-0.189 PNL=+0.07€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=656 IC=+0.035 PNL=+72.32€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=656 IC=+0.035 PNL=+72.32€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.102 > 0.1 con n=131 PNL=+28.41€
  - _Datos_: n=131 IC=+0.102 PNL=+28.41€

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
  - _Estado_: n=7666 IC=-0.142 PNL=+380.69€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=7666 IC=-0.142 PNL=+380.69€

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
  - _Estado_: n=941 IC=+0.141 PNL=+494.90€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=941 IC=+0.141 PNL=+494.90€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.125 > 0.08 con n=665 PNL=+193.71€
  - _Datos_: n=665 IC=+0.125 PNL=+193.71€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=922 IC=+0.000 PNL=+5.83€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=922 IC=+0.000 PNL=+5.83€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.084 > 0.08 con n=921 PNL=+560.58€
  - _Datos_: n=921 IC=+0.084 PNL=+560.58€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.162 > 0.08 con n=199 PNL=+69.83€
  - _Datos_: n=199 IC=+0.162 PNL=+69.83€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.235 < -0.1 con n=850 PNL=-97.86€
  - _Datos_: n=850 IC=-0.235 PNL=-97.86€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=2195 IC=+0.137 PNL=+1263.05€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=2195 IC=+0.137 PNL=+1263.05€

**🟡 H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: n≥40 en cada rama (contrario y alineado) para separar señal de ruido
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.100 > 0.08 con n=48 PNL=+14.93€
  - _Datos_: n=48 IC=+0.100 PNL=+14.93€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=953 IC=-0.008 PNL=+90.53€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=953 IC=-0.008 PNL=+90.53€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.182 > 0.08 con n=849 PNL=+559.06€
  - _Datos_: n=849 IC=+0.182 PNL=+559.06€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=1415 IC=-0.060 PNL=+312.79€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1415 IC=-0.060 PNL=+312.79€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.115 > 0.08 con n=315 PNL=-40.48€
  - _Datos_: n=315 IC=+0.115 PNL=-40.48€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.227 > 0.08 con n=2025 PNL=-213.96€
  - _Datos_: n=2025 IC=+0.227 PNL=-213.96€

**⏳ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: 17/40 ops en el filtro definido (IC actual=-0.022 PNL=+4.29€)
  - _Datos_: n=17 IC=-0.022 PNL=+4.29€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.107 n=306) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=306 IC=+0.107 PNL=+82.34€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.315 > 0.08 con n=106 PNL=+55.91€
  - _Datos_: n=106 IC=+0.315 PNL=+55.91€

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.423 n=283) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=283 IC=+0.423 PNL=+390.14€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=4538 IC=+0.146 PNL=-730.13€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=4538 IC=+0.146 PNL=-730.13€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.250 > 0.1 con n=62 PNL=+44.39€
  - _Datos_: n=62 IC=+0.250 PNL=+44.39€
